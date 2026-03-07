import glob
from os.path import dirname

def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*.py")

    all_modules = [
        f.replace(work_dir, "").replace("/", ".").replace(".py", "")
        for f in mod_paths
        if not f.endswith("__init__.py")
    ]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
