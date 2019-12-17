# -*- coding=UTF-8 -*-
"""Batch runner.  """
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import io
import logging
import os
import subprocess
import tempfile
import webbrowser
from datetime import datetime

import jinja2
import nuke
import six

from nuketools import utf8
from wlf.codectools import get_encoded as e
from wlf.codectools import get_unicode as u
from wlf.decorators import run_async
from wlf.path import Path
from wlf.progress import CancelledError, progress

from . import __main__, files
from .config import Config, START_MESSAGE

LOGGER = logging.getLogger(__name__)


@run_async
def run(input_dir, output_dir):
    cfg = Config()
    temp_fd, temp_fp = tempfile.mkstemp("-script_use_seq")
    try:
        for _ in progress(["获取文件列表……"], '匹配文件'):
            footages = files.search(
                include=cfg['seq_include'].splitlines(),
                exclude=cfg['seq_exclude'].splitlines())
        if not footages:
            raise ValueError("No footages")
        with io.open(temp_fd, 'w', encoding='utf8') as f:
            f.write("\n".join(six.text_type(i) for i in footages))
        result = []
        try:
            for i in progress(Path(e(input_dir)).glob("**/*.nk"), "转换Nuke文件为序列工程", total=-1):
                start_time = datetime.now()
                output = Path(output_dir) / i.name
                cmd = [nuke.EXE_PATH,
                       '-t',
                       __main__.__file__.rstrip('c'),
                       '--input', i,
                       '--output', output,
                       '--footage-list', temp_fp,
                       ]
                cmd = [e(j) for j in cmd]
                LOGGER.debug("command: %s", cmd)

                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = proc.communicate()
                stdout = u(stdout)
                stderr = u(stderr)
                if START_MESSAGE in stdout:
                    stdout = stdout.partition(
                        START_MESSAGE)[2].strip()
                proc.wait()
                if proc.returncode:
                    nuke.tprint(utf8(stdout))
                    nuke.tprint(utf8(stderr))
                    LOGGER.error("Process failed: filename=%s", i)
                result.append(dict(
                    start_time=start_time.isoformat(),
                    end_time=datetime.now().isoformat(),
                    returncode=proc.returncode,
                    input=six.text_type(i),
                    output=six.text_type(output),
                    cmd=cmd,
                    stdout=stdout,
                    stderr=stderr,
                ))
        except CancelledError:
            pass

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.abspath(__file__ + '/../../../templates')))
        template = env.get_template('script_use_seq.html')
        report = template.render(
            result=sorted(result, key=lambda v: v['input']))
        with io.open(
            e(os.path.join(output_dir, '!序列工程转换报告.html')),
            'w',
                encoding='utf8') as f:
            f.write(report)
        webbrowser.open(output_dir)
    finally:
        try:
            os.unlink(temp_fp)
        except OSError:
            pass
