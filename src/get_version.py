import importlib.util
from actions import *

## Version File Dir
version_file = env('version_file_path')
print(version_file)

# version_file = 'D:/Coding/IBD-Tool/version.py'
# Version File Name
# file_dir_w_name, file_ext = os.path.splitext(version_file)
# file_dir, file_name = os.path.split(file_dir_w_name)


# Load Module
spec = importlib.util.spec_from_file_location('version',version_file)  # This 'version' name seems no use
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# print(type(module.VER))
set_output('version', module.VER)


"""
version.py (file name can be different) must have a variable VER. e.g.

VER = 'v1.0.0'
"""