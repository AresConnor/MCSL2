
import traceback

from typing import Tuple

def get_version() -> Tuple[str, str]:
    # 尽量不要写死在构建脚本里
    # 用点邪门的方法
    VERSION = ""
    BUILD_VERSION = ""
    try:
        with open('./MCSL2Lib/__init__.py', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith("VERSION"):
                    VERSION = line.strip('BUILD_VERSION = "')[:-2]
                if line.startswith("BUILD_VERSION"):
                    BUILD_VERSION = line.strip('BUILD_VERSION = "')[:-2]
    except:
        # 尽量不导入
        traceback.print_exc()
        from MCSL2Lib import VERSION, BUILD_VERSION
    return (VERSION, BUILD_VERSION)

if __name__ == "__main__":

    with open("pyproject.toml", "rw", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        if line.startswith("product-version"):
            line = f'product-version = "{get_version()[0]}"\n'
        if line.startswith("build-version"):
            line = f'build-version = "{get_version()[1]}"\n'