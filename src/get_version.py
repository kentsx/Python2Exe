import importlib.util
from actions import *
# import os

## Version File Dir
version_file = env('version_file_path')
# version_file = 'version.py'  #强制给一个路径
# print('='*30)
# print(os.environ.get('VERSION_FILE_PATH'))
# print(os.environ.get('INPUTS'))
# print('='*30)
# print(version_file)
# print('='*30)



# Load Module
spec = importlib.util.spec_from_file_location('version',version_file)  # This 'version' name seems no use
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print('='*30)
print('Release Tag: ', module.VER)
print('='*30)
set_output('version', module.VER)


"""
version.py (file name can be different) must have a variable VER. e.g.

VER = 'v1.0.0'
"""