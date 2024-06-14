# Python2Exe
An action to pyinstaller and release/artifact

[中文说明](https://github.com/kentsx/Python2Exe/blob/main/README-zh.md)|[ENGLISH](https://github.com/kentsx/Python2Exe/blob/main/README.md)
---

### Introduction
Mainly for personal usage, and greatly inspired by [@sayyid5416](https://github.com/sayyid5416/pyinstaller), [@eric2788](https://github.com/eric2788/pyinstaller-build) and [@ncipollo](https://github.com/ncipollo/release-action)

#### Main Function
- Setup Python with cache
- Create artifact and upload executable (optinal), by default, executable will not be upload to artifact
- Create release with executable (optional), by default, a release will be made.

### Attention
- Before use the action, you must have a `requirements.txt` file in repo root, even if you don't have packages to `pip install`.
- This action will only create onefile python executable.




### Available Inputs
  | Input                 | Default <br> _(`-` = empty string)_  | Required |Description 
  |-----------------------|:--------:|:--------:|-------------
  | `main`   |         | yes |Path of your `.py`, without`.py`
  | `dist`        | `./dist` | no |Path of your executable file
  | `python_version`       | 3.9 | no  | Specific python version you want to use
  | `pyinstaller_version`  | 6.7 | no  | Specific pyinstaller version you want to use <br>*(with proper signs, like `5.13.2`)*
  | `exe_name`            | `main`| no | executable upload to artifact and release with this name. DO NOT MAKE SPACE BETWEEN WORDS, use `_` i.e. `my_executable`
  | `use-dependencies`| `true` | no   | Whether to install `requirements.txt`
  | `no-console`      | true  | no   | whether to disappear console terminal. If true, console won't be displayed
  | `icon`      | NONE  | no   | Add the icon mark into your executable, the file path of your ico, e.g. logo.png or logo.ico'
  | `artifact`      | false  | no   | If true, then the executable will be upload to artifact
  | `compression_level`   | 6    | no    | Level of compression for archive. <br>Range: 0 and 9. <br>_(0 = No compression, 9 = Max compression)_.
  | `release`   | true    | no    | Whether create a release with the executable
  | `token`   | `${{ github.token }}`    | no    | The Github token. Make sure you have the permission to create release.
  | `tag`   | `${{ github.ref_name }}-Run#${{ github.run_id }}-Attempt#${{ github.run_attempt }}`    | no    | An optional tag for the release.
  | `bodyfile`   | `-`    | no    | An optional body file for the release. This should be the path to the file, e.g. `body.MD`. The default will take commit message as release note.

###  Examples

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