# 更新日志

## [0.20.12](https://github.com/WuLiFang/Nuke/compare/v0.20.11...v0.20.12) (2020-11-16)

### 修复

- **依赖:** 降级 pendulum 至 v1 ([ddfc3f4](https://github.com/WuLiFang/Nuke/commit/ddfc3f45ab8652754f4f5af2a1390e018ed9d807))
- **依赖:** 不使用 poetry ([4b8ee7f](https://github.com/WuLiFang/Nuke/commit/4b8ee7f1a95c14aa5318bfadb8cd424d3ab339ba))

## [0.20.11](https://github.com/WuLiFang/Nuke/compare/v0.20.10...v0.20.11) (2020-10-12)

### 功能

- **正则分割图层组:** 使用本地帮助文档 ([0a1da07](https://github.com/WuLiFang/Nuke/commit/0a1da07e01f4d72430948bd01d26d98ff27b3f14))
- 正则分割图层组 ([db6eb39](https://github.com/WuLiFang/Nuke/commit/db6eb391a777c4e4dd5cc8a20b6175939105380b))

### 修复

- **正则分割图层组:** 错误的 merge 输入 ([9c49457](https://github.com/WuLiFang/Nuke/commit/9c494578b77c92fc1721b0cb58e0f6d51260f8f6))
- **正则分割图层组:** 错误的对话框标题 ([2cfc1f9](https://github.com/WuLiFang/Nuke/commit/2cfc1f9e6ade8fbedeb8c1ab2664658de96d854d))
- **wlf_Write:** v1.56.3 deadline 任务提交 ([955c09a](https://github.com/WuLiFang/Nuke/commit/955c09a69937633a740164070c82a16d628c10c0))
- **wlf_Write:** v1.56.4 错误的序列输出条件 ([39268b8](https://github.com/WuLiFang/Nuke/commit/39268b8aa7e379e2799074252c20ac3e2b4a8bf8))

## [0.20.10](https://github.com/WuLiFang/Nuke/compare/v0.20.9...v0.20.10) (2020-08-20)

### 功能

- rotopaint uv 映射 ([483f95d](https://github.com/WuLiFang/Nuke/commit/483f95d2c1e8a1fd1455bb95fbd7029c9c4ce2ba))

### 修复

- **运动扭曲:** v0.2.2 修正向前运动 ([fbf639b](https://github.com/WuLiFang/Nuke/commit/fbf639bbe82be1a7010f9eb8bc3e099b8c6b01d0))
- **RotoPaint 运动扭曲:** 修正向后运动 ([11f2c56](https://github.com/WuLiFang/Nuke/commit/11f2c5674f0e7df5417ab21fcf5a34437c7a9bab))
- **RotoPaint 运动扭曲:** motion 层丢失提醒 ([c145fdb](https://github.com/WuLiFang/Nuke/commit/c145fdb3cac3cca13368e4917e6e3a71a69f4f64))
- **RotoPaint 运动扭曲:** 应当在采样完后再移动中心点 ([bb73f53](https://github.com/WuLiFang/Nuke/commit/bb73f5329144b7b6f9949d51ccf95d626c31d9db))

## [0.20.9](https://github.com/WuLiFang/Nuke/compare/v0.20.8...v0.20.9) (2020-08-18)

### 功能

- **RotoPaint 运动扭曲:** 在对话框确认后禁用代理 ([eb13fe5](https://github.com/WuLiFang/Nuke/commit/eb13fe5c5f789feaf7118cdbb1935d64a4a1b873))

### 修复

- 应该在 RotoPaint 运动扭曲前禁用代理 ([f18847a](https://github.com/WuLiFang/Nuke/commit/f18847a6e447a7e74ab10c9cc577fae295c3243a))

## [0.20.8](https://github.com/WuLiFang/Nuke/compare/v0.20.7...v0.20.8) (2020-08-18)

### 功能

- rotopaint 运动扭曲 ([f4406e6](https://github.com/WuLiFang/Nuke/commit/f4406e6c2ff2a0012c8b16a9a73c571d0c7327e0))
- **运动扭曲:** v0.2.0 支持设置基准帧 ([ed9c513](https://github.com/WuLiFang/Nuke/commit/ed9c5139cc5da1a8c96ce3d3024f1627d9cfdcd1))
- 添加创建运动扭曲命令 ([bf1c1cb](https://github.com/WuLiFang/Nuke/commit/bf1c1cb02cdbe35d0ae4cd4e582b34977188fd9b))
- 添加第三方 RealGlow 节点 ([e170849](https://github.com/WuLiFang/Nuke/commit/e170849ec451431f1acdbf01baa3d40734516cfb))

### 修复

- **MotionDistort:** v0.2.1 错误的边界框设置 ([871bdbe](https://github.com/WuLiFang/Nuke/commit/871bdbe8a9166f4890fe952611b5c11d7f112c40))
- NukeX 有重复的 pyblish 窗口 ([30f029b](https://github.com/WuLiFang/Nuke/commit/30f029ba53a807712d8d5e8e02ba3aeb1ebcabcb))
- 有重复的 pyblish 面板 ([0d23ec5](https://github.com/WuLiFang/Nuke/commit/0d23ec52331d3371d64829df3619d9865245e0f3))
- NukeStudio pyblish 窗口 ([8298f11](https://github.com/WuLiFang/Nuke/commit/8298f114141dce519642a85a41861f363c6f20d0))

## [0.20.7](https://github.com/WuLiFang/Nuke/compare/v0.20.6...v0.20.7) (2020-07-29)

### 功能

- 添加第三方节点 FilmicTonemappingOperator ([b83f142](https://github.com/WuLiFang/Nuke/commit/b83f142c46c2376286d4657f62788dbb003dbae0))
- arnold 预合成 ([5edd665](https://github.com/WuLiFang/Nuke/commit/5edd665c041d3c4e6d35e7242cae87691b1fd3e3))
- **RotateCrop:** v0.1.0 新节点 ([54cec0f](https://github.com/WuLiFang/Nuke/commit/54cec0f0f5b0a281ebc470ad3135ae8dc11232cc))
- **SoftGlow:** v0.1.2 添加宽度通道控制 ([4194084](https://github.com/WuLiFang/Nuke/commit/4194084f5757993d413b699b4abe367e702b0507))
- **SoftGlow:** v0.1.3 跳过尺寸小于 1 的辉光 ([0303209](https://github.com/WuLiFang/Nuke/commit/03032095aca1af311a9015b6c86a77016e656fdd))

### 修复

- **SoftGlow:** v0.1.4 应该总是使用默认输入 ([cb61203](https://github.com/WuLiFang/Nuke/commit/cb612037bff924d399e02df770f945504dc0dcb4))

## [0.20.6](https://github.com/WuLiFang/Nuke/compare/v0.20.5...v0.20.6) (2020-07-05)

### 功能

- 延长许可日期至 2021-07-01 ([c56d413](https://github.com/WuLiFang/Nuke/commit/c56d413470211686c5ead85019ace23fcf301db0))
- 添加 OnionSkin 节点 ([f47a6ef](https://github.com/WuLiFang/Nuke/commit/f47a6efeffb0c3fd457c198cad71d360bed219a8))
- 添加 SoftGlow 节点 ([c1e8643](https://github.com/WuLiFang/Nuke/commit/c1e8643d447f7b0d90acf92bce3f8174a3d9c188))
- **SoftGlow:** v0.1.1 添加更多控制 ([bf249b6](https://github.com/WuLiFang/Nuke/commit/bf249b63f6d23ba42aa8a74a5f0957c26ef97c7c))
- 在需要选择节点单未选择时弹出消息提示 ([c4c8002](https://github.com/WuLiFang/Nuke/commit/c4c80023a35339a558542641a71763a7fca35760))
- **OnionSkin:** 0.1.2 添加 effect_only 控制 ([09ccb1b](https://github.com/WuLiFang/Nuke/commit/09ccb1bca0c53c49d857249ccf541c1862779573))
- 添加 OnionSkin.knob_hash 以使过期缓存失效 ([979614d](https://github.com/WuLiFang/Nuke/commit/979614dacef9e97ab96803a2decca3b6ee826882))
- 添加 rotopaint 摄影表 ([0e8dc18](https://github.com/WuLiFang/Nuke/commit/0e8dc1836bea1e5ac567d5fcc8a7ac6526e3d12a))

### 修复

- 激活发布面板时应变更选中的标签页 ([012b652](https://github.com/WuLiFang/Nuke/commit/012b652945060a765bb55edad3e26f5e01213af6))
- 避免使用 nuke.openPanels() ([b9604bf](https://github.com/WuLiFang/Nuke/commit/b9604bf853573b9e9cbeb8cb5eba1248f1fa9372))
- 发布面板在关闭后再次激活无效 ([bd2c950](https://github.com/WuLiFang/Nuke/commit/bd2c950182b1add1f3a9045f53ee6cb5061c2e47))
- **OnionSkin:** 0.1.1 帧超出范围时的结果错误 ([f88e9e9](https://github.com/WuLiFang/Nuke/commit/f88e9e98a28defd835de5ad4f59fcefa343b402d))
- 在没有输入时尝试激活当前查看器输入 ([eed6775](https://github.com/WuLiFang/Nuke/commit/eed6775b0686717743d92c45501793e57d90c959))
- rotopaint 摄影表应处理两个关键帧在同一帧上的情况 ([fc3439f](https://github.com/WuLiFang/Nuke/commit/fc3439fbe91069441a558ded9fc733650cb64f76))
- rotopaint 摄影表产生未预期的过渡 ([2d58e21](https://github.com/WuLiFang/Nuke/commit/2d58e212233cc505955bb2f89ae7e1a9a77ce45e))

## [0.20.5](https://github.com/WuLiFang/Nuke/compare/v0.20.4...v0.20.5) (2020-05-19)

### 功能

- 添加更多文件前缀项目匹配规则 ([c8bc545](https://github.com/WuLiFang/Nuke/commit/c8bc54526aa6e387f6a93847d135baf2c676cc8f))
- 延长许可日期至 2021-01-01 ([d79a95c](https://github.com/WuLiFang/Nuke/commit/d79a95c22ec92f4da0ee923240d8f6e3527ef5e1))
- **wlf_Lightwrap:** 添加通道控制 ([7f5a71d](https://github.com/WuLiFang/Nuke/commit/7f5a71d51881b01d65d4682ff963f4544e7c9dcb))

### 修复

- **依赖:** 更新依赖 jinja2 至 v2.11.0 ([6f3ff93](https://github.com/WuLiFang/Nuke/commit/6f3ff93e9c8d9e4d4a4817eecd44f63664db1bdf))
- **wlf_Lightwrap:** 应该在 rgba 通道上模糊而不是 rgb 通道 ([a336040](https://github.com/WuLiFang/Nuke/commit/a33604093cdff9c609da9ca04fbcbec3304b2c30))

## [0.20.4](https://github.com/WuLiFang/Nuke/compare/v0.20.3...v0.20.4) (2020-01-10)

### 功能

- **DirectionLightKeyer:** 添加 axis 输入 (v0.5.0) ([e6b765b](https://github.com/WuLiFang/Nuke/commit/e6b765b2449fcd57d25196bf2eb52d8eac52fd1e))
- 添加 `GenerateVector` 插件 ([13e9f4e](https://github.com/WuLiFang/Nuke/commit/13e9f4eb1e273f35f69f63fb24945c6579d87a3e))
- **转换为序列工程:** 添加 HTML 报告 ([55af938](https://github.com/WuLiFang/Nuke/commit/55af938bdfe5c0986e8fbdbe57d9ce01ced06550))
- 添加 `WeightedErode` 节点 ([91e496b](https://github.com/WuLiFang/Nuke/commit/91e496b8e2e333f97bbf856b6d506afa07fe0717))
- 支持转换单帧工程为序列工程 ([01872c1](https://github.com/WuLiFang/Nuke/commit/01872c1332c450c5bbb56b2215b37d980338cd0e))
- 优化抽帧匹配的对话框 ([ccc556d](https://github.com/WuLiFang/Nuke/commit/ccc556dcd121296db9efe317d212a6e79008d45c))
- 更改 `GenerateVector` 的边界框(bbox)设置 ([a280f98](https://github.com/WuLiFang/Nuke/commit/a280f981a7c9109f200dc841aae8710d7ee6c5a4))
- 支持匹配抽帧 ([9354576](https://github.com/WuLiFang/Nuke/commit/9354576a83d09c9a1e6d8ca2bb0ab1b066693aa6))
- 延长许可日期至 2020-07-01 ([aee05f0](https://github.com/WuLiFang/Nuke/commit/aee05f0df14e29e5722a59868c6ce4e67f7ea090))

### 修复

- 资产监控可能导致崩溃 ([0504a29](https://github.com/WuLiFang/Nuke/commit/0504a2917f26c5a12fc7d84d7ba5309aaaa89cc6))
- 自动标签(autolabel)在很多节点时导致卡顿 ([a936c36](https://github.com/WuLiFang/Nuke/commit/a936c3681f76dad83f7e9cc336e6923558239f64))
- windows 终端编码问题 ([ad718c2](https://github.com/WuLiFang/Nuke/commit/ad718c2b3345b3ee92c33de81f86032305eab9d3))
- 把吾立方硬盘映射配置移到其他插件 ([6a5f1ee](https://github.com/WuLiFang/Nuke/commit/6a5f1ee713a999f2eed22ff78d43e0b7726ef849))
- 验证许可时 unicode error ([3b25782](https://github.com/WuLiFang/Nuke/commit/3b25782b4af69cb64848cac22530d401a70cecd3))
- **依赖:** 更新依赖 `cgtwq` ([d3d5cb0](https://github.com/WuLiFang/Nuke/commit/d3d5cb0e004bbf8da44db6fdab29097deac91c42))
- **转换为序列工程:** 修复批量模式 ([33ecf76](https://github.com/WuLiFang/Nuke/commit/33ecf763c5b40dae9f3022a5bc0b4c6e46110b08))
- **转换为序列工程:** 应该递归搜索 nk 文件 ([3b2b364](https://github.com/WuLiFang/Nuke/commit/3b2b364d6bdb1126bea729b1112ca158c6c78bd1))

## [0.20.3](https://github.com/WuLiFang/Nuke/compare/v0.20.2...v0.20.3) (2019-07-02)

### 杂项

- 延长许可日期到 2020 年 1 月 1 日

## [0.20.2](https://github.com/WuLiFang/Nuke/compare/v0.20.1...v0.20.2) (2019-05-23)

### 修复

- cgtw websocket 连接失败导致无法启动 ([863625e](https://github.com/WuLiFang/Nuke/commit/863625e))

### 构建系统

- 添加 Makefile ([ae065b9](https://github.com/WuLiFang/Nuke/commit/ae065b9))

## 0.20.1 (2019-05-11)

### 修复

- **wlf_Write:** 从 exr 渲染 png ([e79c85b](https://github.com/WuLiFang/Nuke/commit/e79c85b))
- Windows 10 启动时出现 IOError[0] 错误 ([1ac29c3](https://github.com/WuLiFang/Nuke/commit/1ac29c3))

### 构建系统

- 修正文档构建 ([5fe318f](https://github.com/WuLiFang/Nuke/commit/5fe318f))

## 0.20.0 (2019-02-20)

- `WlfWrite` 1.56.1:

  - 支持 png

## 0.19.2 (2019-01-02)

### 杂项

- 延长许可日期到 2019 年 7 月 1 日

## 0.19.1 (2018-09-26)

### 修复

- `SphereMP` 0.2.2:

  - 输入摄像机在`Dot`节点之前时失效出错

## 0.19.0 (2018-08-17)

### 功能

- 居中显示拖入创建的节点

## 0.18.0 (2018-08-16)

### 功能

- 在锁定帧范围(`Project Settings` - `lock range`)启用时拖入视频自动将视频对齐工程首帧

## 0.17.0 (2018-08-15)

### 功能

- 在未安装 CGTeamWork 的电脑上自动禁用相关功能更改

### 向下不兼容的更改

- 重构代码

## 0.16.2 (2018-08-14)

### 向下不兼容的更改

- 无视复制粘贴的拖放, 由 Nuke 自己处理

## 0.16.1 (2018-08-13)

### 修复

- DeepEXR 拖放无视序列素材

- 去掉拖放得到的 `VectorField` 节点标签中的花括号

## 0.16.0 (2018-08-13)

### 功能

- 拖放时自动导入 nk 文件为 `Group` 组节点, 组上有 `展开组` 的按钮以实现以前的效果

- 拖放 DeepEXR 素材时自动创建 `DeepRead` 节点而不是 `Read`节点

### 向下不兼容的更改

- 拖放时不会自动设为当前所选节点的输入(Nuke 默认行为会自动改节点输入)

- 拖放得到的节点如果报错将不会禁用保留, 而是直接删除, 在 `Error console` 中可以查看哪些素材导入失败

- 如果拖入 fbx 文件时摄像机有动画则不会自动创建 `ReadGeo` 节点

### 修复

- CGTeamWork 上拖入文件不能正确导入(`file://`协议识别出错)

## 0.15.4 (2018-08-08)

- `wlf_Write` 节点 1.55.4:

### 修复

- 会在 deadline 非分别渲染时尝试读取 EXR

## 0.15.3

### 功能

- 文档添加 `发布` 相关的内容

### 修复

- `编辑` - `修正读取错误`(F6) 处理中文路径时出错

- 发布提交时有时不会带图片(因为在上传单帧之前就提交了)

## 0.15.2 (2018-08-03)

### 修复

- 直接点三角不能正确发布(0.15.1 引入)

## 0.15.1 (2018-08-03)

### 修复

- 工程退出时自动发布会在下个工程载入时才运行导致错误结果(0.15.0 引入)

- 浮动发布面板布局时无法退出时自动发布

## 0.15.0 (2018-08-03)

### 功能

- 增强 Nuke 内置预合成创建面板( `CTRL+SHIFT+P` )

  汉化了界面, 并添加了 `预合成名称` 控制来快速设置工程路径和渲染路径

- Pyblish `发布` 插件: `上传预合成文件`

  预合成文件需要放到服务器才能 deadline 渲染

  此插件自动上传预合成文件到服务器并更改预合成节点读取文件路径到服务器

- 帮助文档新增 `指南` - `预合成分割`

### 修复

- **`wlf_Write` 节点 1.55.3**: Deadline 上低于`exr阈值`的分别渲染任务渲染 MOV 时不读取之前渲染好的 EXR

## 0.14.2 (2018-08-02)

### 修复

- **`wlf_Write` 节点 1.55.1**: 在中途取消渲染单帧之后渲染视频会出错的问题

## 0.14.1 (2018-07-27)

### 功能

- `提交任务`时会自动附上当前单帧图效果

### 修复

- `提交任务`的备注在 CGTeamWork 上无法正确显示

## 0.14.0 (2018-07-27)

### 功能

- pyblish 发布插件: `提交任务`

  因为合成阶段现在提交的是单帧而不是视频了, 所以合成阶段需要在上传单帧时就提交任务。

  此插件会在任务非检查状态时询问用户是否提交任务。

## 0.13.0 (2018-07-25)

### 功能

- `编辑` 菜单 - `最佳实践` - `Glow节点不使用mask`

  自动把使用遮罩的 Glow 节点改为使用 `width channel` (宽度通道)

  使用遮罩的 Glow 仅仅是把 Glow 过的图和没 Glow 过的图根据遮罩叠加起来, 并不是衰减效果。

  并且更耗内存, 可能导致渲染崩溃。

### 向下不兼容的更改

- `编辑` 菜单 - `最佳实践` - `清理无用节点`

  - 更改位置, 此前位于: `编辑` 菜单 - `整理` - `清理无用节点`
  - 重新支持中文节点名称(之前某次更新引入的 bug)
  - 支持清理被禁用的无用节点(有表达式引用的禁用节点除外)
  - 优化速度

- `编辑` 菜单 - `最佳实践` - `合并重复读取节点`

  - 更改位置, 此前位于: `编辑` 菜单 - `整理` - `合并重复读取节点`

- `PositionKeyer`节点 1.4.2: 规整代码

## 0.12.0 (2018-07-24)

### 功能

- `编辑`菜单 - `整理` - `合并重复读取节点`命令

  Nuke 中相同文件的多个读取节点会占用多份内存, 使用此命令节省内存占用。

## 0.11.0

- 升级至 cgteamwork 5.2

## 0.10.2 (2018-07-17)

- **`wlf_Write`节点 1.55.0:** - 提交 Deadline 分别渲染时自动启用序列输出, 无需为低于 100 帧的工程手动设置阈值

## 0.10.1

### 功能

- **`修正读取错误`(F6)**: 在脚本编辑器中显示操作记录

### 向下不兼容的更改

- **`修正读取错误`(F6)**: 如果在使用新素材后依旧节点出错则会回退至老素材路径

## 0.10.0 (2018-07-16)

### 功能

- `修正读取错误`(F6) 增强
  - 支持除 `Read` 节点之外的其他读取文件的节点(例如: `DeepRead`, `Camera`)
  - 支持识别表达式
  - 支持识别仅格式不同的文件为同一文件(例如: `%04d` = `####`)
  - 运行完毕后提示结果给用户

## 0.9.3 (2018-07-16)

### 向下不兼容的更改

- 插件面板(`多节点编辑`F2, `重命名通道`F4)在用户使用浮动节点控制面板时也使用浮动面板(之前为放入当前面板)

## 0.9.2 (2018-07-12)

### 修复

- **`wlf_Write` 1.54.2:** Deadline 在不分别渲染时会出错

## 0.9.1 (2018-07-11)

### 修复

- **`wlf_Write` 1.54.1:** 没选择`读取序列`也会读取序列

## 0.9.0 (2018-07-11)

### 功能

- **`wlf_Write` 1.54.0:** 支持 deadline 序列渲染完成后自动转换为 mov

### 向下不兼容的更改

- **`wlf_Write` 1.54.0:** `用序列渲染视频`按钮替换为`读取序列`勾选框, 勾选后再点击`渲染视频`即可实现用序列渲染视频, 并且缺帧会自动进行渲染补齐

## 0.8.0 (2018-07-05)

### 功能

- `通道重命名`(F4)支持`ID`层
- 发布失败时会有气泡信息提示
- 发布时会显示当前工程内存使用量

### 向下不兼容的更改

- 在发布时不检查素材是否更新, 因为已经有弹窗提示了

### 修复

- 为仙剑项目添加自定义转换以支持不符合以往规律的数据库名称(`XJCG` -> `XJ`)
- 批量合成出错(0.7 引入的 bug)

## 0.7.3 (2018-06-29)

### 修复

- 发布会导致工程变为已修改状态(已保存的文件发布后关闭会询问是否保存修改的文件)

## 0.7.2 (2018-06-27)

### 修复

- 设置了时间偏移的`Read`节点会导致错误的缺帧检查结果
- 0.7.0 引入的 bug:

  - `Read`节点帧范围识别错误
  - 插件节点不在菜单中显示和文档打不开
  - `检查素材更新`命令无效

## 0.7.1 (2018-06-26)

### 修复

- `自动合成`进度条导致报错
- 素材获取的时候会获取到 nuke 缓存路径

## 0.7.0 (2018-06-26)

### 功能

- 素材保存位置检查, 使用了本地素材会阻止上传

### 向下不兼容的更改

- 更新依赖
- 重构代码
- 材更新和缺帧提示改回以前的弹窗方式提醒

### 修复

- 修正在未保存时使用`检查素材更新`会报错的问题

## 0.6.4 (2018-06-13)

- 延长插件过期日期
- 更新依赖
- 渲染文件夹支持中文
- 上传图片时如果组长状态为`等待`将设为`检查`

## 0.6.3 (2018-04-26)

- 更新依赖

## 0.6.2

- 修正单帧上传

## 0.6.1 (2018-04-19)

- `wlf_Write` 1.53.4: 在序列转单帧的时候关闭 hash 检查

## 0.6.0

- 更新依赖

## 0.5.4 (2018-04-02)

- 修复首次导入上游视频时必定发布失败的问题

## 0.5.3 (2018-04-02)

- 修复保存并关闭时永远不能通过素材修改日期检查的问题

## 0.5.2 (2018-04-02)

### 修复

- 稍后启用
- 转换单帧为序列

## 0.5.1 (2018-03-29)

### 修复

- `pyblish`检查导致修改状态显示为修改过
- 恢复 0.4 版本的 CGTeamWork 自动打开和登录的功能
- tab 菜单不能创建插件节点的问题
- 上传单帧时没设置缩略图
- 比较修改日期时忽略了时区
- `pyblish`现在能在保存并退出时自动发布了

## 0.5.0 (2018-03-29)

- 重构
  - 以不修改默认编码的方式支持中文, 以增强兼容性
  - 依赖库重构 改为使用自制的 CGTeamWork 客户端库
  - 规范开发流程 添加大量添加测试用例
- 引入`pyblish`作为发布框架
- 移除色板集成, 因为改为使用色板服务器
- `wlf_Write`节点现在支持多视图

## 0.4.24 (2018-01-29)

- 支持虚拟环境导入 nuke 模块
- **`wlf_Write` 节点 1.53.0:** 适配 VR 立体工程, 调整面板

## 0.4.23 (2018-01-08)

- 自动合成支持 `OCC` 和 `SH` 的二合一层 `OCCSH`

## 0.4.22 (2017-12-31)

- 全部模块使用 `absolute_import`

## 0.4.21

- 修复增量版本保存会导致不上传 nk 文件至 CGTeamWork 的问题
- 现在开始取消模块独立版本号, 任意模块更新都更新整体版本号

## 0.4.20 (2017-12-22)

- 完善文档

## 0.4.19 (2017-12-21)

以下是自 0.3.2 以来的更新内容

Nuke 插件更新:

- 大量 Bug 修复

- 许多编程方面的改进

- 为此插件编写了文档, 在菜单 `帮助` - `吾立方插件文档` 中可查看。

- 添加了 `素材命名要求.md`

- 在 Nuke 控制台输出中文的插件命令日志

- 插件有了任务栏图标, 气泡提示统一从此处弹出

- 因为 Nuke 的 `Localiztion` 功能会导致看到的素材不是最新的, 现在默认禁用了此功能

  要加快读取请使用 `DiskCache` 节点代替

- 所有耗时操作都有了进度条提示

- 检查:

  - 缺帧检查: 保存时会检查素材缺帧并提示
  - 修改日期检查: 打开时如果有使用素材比本 nk 文件更新会有提示

- redshift 预合成(F1):

  - 添加自动开关
  - 支持更多的 redshift 图层种类
  - 支持 `Read` 以外的节点
  - 如果没有 `plus` 模式的节点, `Remove` 节点将会默认禁用
  - 撤销改为直接撤销到预合成前
  - 在不会导致卡死的情况下会开启节点的 `Postage stamp` (邮票式预览)
  - 在节点的标签中使用中文的层名称

- 多节点编辑(F2):

  新增 可以同时编辑选中的多个同类型节点

- 编辑/修复错误读取节点(F6):

  适用的情况更广了

- 界面:

  - 添加了 `TimeOffset` 节点的默认标签
  - 现在会在 Nuke 的控制台输出开启脚本时的插件命令消耗时间
  - 工具集 (`ToolSets`) 菜单中增添了以下内容:

    - 刷新
    - 创建共享工具集
    - 打开共享工具集菜单

  - 支持共享工具集给使用同一此插件副本的其他人

- 自动合成:

  - 除了背景层 `ZDefocus` 的 `depth layers` 默认值设为 5, 加快渲染
  - 支持新素材标签 `AO`
  - 添加自动合成设置菜单, 提供更精细的自动合成控制
  - 叠加额外层时改为使用 `rgb` 通道而不是`rgba`通道
  - 添加命令行界面
  - 添加默认使用 `Emission.alpha` 的辉光节点
  - 增强了镜头的帧范围识别
  - 使用 `DiskCache` 节点提升合成体验

- 批量自动合成:

  - 更强的多线程, 自动决定是否使用多线程, 避免死机
  - 添加自动合成设置面板
  - 优化批量自动合成日志的排版
  - 能够生成 `镜头备注.txt` 方便记录备注

- 首选项:

  - 更改了 `RolloffContrast` 节点的默认值
  - 更改了 `Denoise2` 节点的默认值

- 自动摆放:

  - 更换逻辑完全重构, 速度更快效果更好
  - 支持异步动画

- 文件/文件夹拖放:

  - 中文路径 mov 拖入时用一个备注代替, 因为中文路径的 mov 会导致卡死。

- 上传 mov:

  - 上传时不会导致 Nuke 失去响应了
  - 现在成为 Nuke 和 CGTeamWork 通用插件, 可在 CGTeamWork 右键菜单中访问, 支持其他流程的上传。
  - 打开时默认使用最近工程的 mov 渲染目录

- 扫描空文件夹:

  实验性 位于 `工具` 菜单 用于查看哪个镜头还没出素材

- 节点:

  - `wlf_Write`:

    - 支持渲染 exr
    - 提示长镜头输出 exr
    - 支持从渲染出来的 exr 生成 mov
    - 减少读取单帧时不能渲染单帧的问题

  - `PositionKeyer`:

    - 添加`渐变`以外的两个新模式: `距离` 和 `球`
    - 改进了取样的逻辑

  - `DepthFix`:

    添加尝试在错误输入情况下使用的提示

  - `Flicker`:

    新节点 灯光抖动生成器

  - `MotionRotate`:

    新节点 可以旋转速度层来达到旋转运动模糊方向的效果

  - `AntiAliasing`:

    新节点 较小的模糊可以用这个

  - `SphereMP`:

    成为插件, 此前是工具集

- 通道重命名

  - 支持 `rgba.alpha` 通道

- CGTeamWork 集成:

  - 特效素材检查:

    打开 nk 文件时会检查有无特效素材并自动打开文件夹

  - 上游匹配检查:

    - 打开和保存 nk 文件时会自动导入上游视频并连接到主查看器的输入 5 上
    - 如果工程帧速率和帧长度和上游视频不一致会弹出警告

  - 自动上传工作文件:

    保存时将会自动上传工作文件到服务器。

  - 自动上传单帧:

    保存并退出时 `wlf_Write` 节点会自动渲染并上传单帧到服务器

  - 检查制作者:

    保存时会检查 CGTeamWork 上分配的制作者, 如果不是当前登录用户将提示并不会上传任何文件。

- 创建色板:

  - 现在是通用插件, 并且改为使用 html 格式来代替巨大的 jpg 图像。

Nuke 和 CGTeamWork 通用插件更新:

- 创建色板:

  - 支持打包到本地
  - 支持实时更新
  - 支持视频(利用视频生成的 gif)

- 上传工具(上传 mov):

  - 用于上传成果的面板, 位于 `工具` 菜单
  - 上传时不会导致 Nuke 失去响应了
  - 支持带辅助信息的 `burn-in` 版本
  - 打开时默认使用最近工程的 mov 渲染目录

## 0.4.18 (2017-12-07)

## 0.4.17 (2017-11-28)

## 0.4.16 (2017-11-23)

## 0.4.15 (2017-11-19)

## 0.4.14 (2017-11-10)

## 0.4.12 (2017-11-01)

## 0.4.11 (2017-10-24)

## 0.4.10 (2017-10-21)

## 0.4.9 (2017-10-18)

## 0.4.8 (2017-10-18)

## 0.4.6 (2017-10-12)

## 0.4.5 (2017-10-10)

## 0.4.4 (2017-10-09)

## 0.4.3 (2017-10-06)

## 0.4.2 (2017-09-29)

## 0.4.1 (2017-09-25)

## 0.4.0 (2017-09-25)

## 0.3.10 (2017-09-21)

## 0.3.9 (2017-09-20)

## 0.3.8 (2017-09-19)

## 0.3.7 (2017-09-15)

## 0.3.6 (2017-09-14)

## 0.3.5 (2017-09-13)

## 0.3.4 (2017-09-11)

## 0.3.3 (2017-09-11)

## 0.3.2 (2017-09-06)

- 上传工具成为 Nuke 内置面板
- 调整初始化信息
- 修正 `wlf_Lightwrap`

## 0.3.1 (2017-09-06)

## 0.3.0 (2017-09-05)

## 0.2.0 (2017-08-25)

## 0.1.0 (2017-08-25)
