# Python2Exe
使用Pyinstaller以及生成release/artifact

[中文说明](https://github.com/kentsx/Python2Exe/blob/main/README-zh.md)|[ENGLISH](https://github.com/kentsx/Python2Exe/blob/main/README.md)
---

### 简介
个人使用为主， 参考了[@sayyid5416](https://github.com/sayyid5416/pyinstaller), [@eric2788](https://github.com/eric2788/pyinstaller-build) 和 [@ncipollo](https://github.com/ncipollo/release-action)等

#### 主要功能
- 设置Python环境，且带cache
- 生成exe类文件并上传到artifact (可选), 默认【不上传】
- 生成exe类文件并上发布release (可选), 默认【发布】

### 注意
- 要使用这个action，即使你没有需要`pip install`非原生包，也要在repo根目录有`requirements.txt`文件。
- 这个action只能生成单一文件的exe




### Available Inputs
  | 输入参数                 | 默认值 <br> _(`-` = 空数据)_  | 必需性 | 备注
  |-----------------------|:--------:|:--------:|-------------
  | `main`   |         | 是 | `.py`文件路径, 不要带`.py`后缀
  | `dist`        | `./dist` | 否 | 生成的 exe文件路径
  | `python_version`       | 3.9 | 否  | 指定python版本
  | `pyinstaller_version`  | 6.7 | 否  | 指定pyinstaller版本 <br>*(如 `5.13.2`)*
  | `exe_name`            | `main`| 否 | 上传exe文件的名称； 名称中不要有空格, 用 `_` i.e. `my_executable`
  | `use-dependencies`| `true` | 否  | 是否pip安装 `requirements.txt`
  | `no-console`      | true  | 否 | exe文件是否显示console. 如果是, console不显示
  | `icon`      | NONE  | 否 | 添加程序图标；需要图片文件的路径和后缀, 如 logo.png 或者 logo.ico'
  | `artifact`      | false  | 否  | 如是, exe文件会上传到artifact
  | `compression_level`   | 6    | 否  | 压缩程度. <br>范围: 0 到 9. <br>_(0 = 不压缩, 9 = 最大压缩)_.
  | `release`   | true    | 否  | 是否蒋exe文件发布到一个release中
  | `token`   | `${{ github.token }}`    | 否 | Github密钥， 确保你有发布release的权限
  | `tag`   | `${{ github.ref_name }}-Run#${{ github.run_id }}-Attempt#${{ github.run_attempt }}`    | no    | tag名称
  | `bodyfile`   | `-`    | 否 | release的正文部分。需要为一个文件路径, 如 `body.MD`. 默认则是将commit信息作为正文部分

###  案例

```yaml
jobs:
  pyinstaller-build:
    runs-on: <windows-latest / ubuntu-latest / ..... etc>
    steps:
      - name: Build and Release
        uses: kentsx/Python2Exe@v1.0.0
        with:
          main: main
          exe_name: 'My Executable'
          icon: 'logo.png'
          artifact: false
          release: true
          token: ${{ secrets.TOKEN }}
          tag: ${{ github.ref_name }}
          bodyfile: 'readme.MD'
```