from pathlib import Path
import json
import sys

if (sys.version_info.major, sys.version_info.minor) < (3, 6):
    raise TypeError("at least python 3.6 is required for this script")

if len(sys.argv) > 1:
    PKG_NAME = sys.argv[1]
else:
    raise TypeError("package name must be passed")

if len(sys.argv) > 2:
    VCPKG_PATH = Path(sys.argv[2])
else:
    print("no vcpkg path has been passed. Assuming vcpkg root is on the same level as this script file")
    VCPKG_PATH = Path(__file__).parent / 'vcpkg'

if len(sys.argv) > 3:
    print("the argumnets after the second one are ignored")


if not VCPKG_PATH.exists():
    raise FileNotFoundError(f"dir does not exist: {VCPKG_PATH}")

VERSIONS_PATH = VCPKG_PATH / 'versions'
if not VERSIONS_PATH.exists():
    raise FileNotFoundError(f"dir does not exist: {VERSIONS_PATH}")

PKG_VERSION_PATH = VERSIONS_PATH / (PKG_NAME[0] + '-')
if not PKG_VERSION_PATH.exists():
    raise FileNotFoundError(f"dir does not exist: {PKG_VERSION_PATH}")

PKG_VERSION_JSON_PATHNAME = PKG_VERSION_PATH / (PKG_NAME + '.json')
if not PKG_VERSION_JSON_PATHNAME.exists:
    raise FileNotFoundError(f"dir does not exist: {PKG_VERSION_JSON_PATHNAME}")


print(f'reading versions from {PKG_VERSION_JSON_PATHNAME}')
with open(PKG_VERSION_JSON_PATHNAME) as f:
    pkg_versions_file = json.load(f)
    info_list = pkg_versions_file["versions"]

    for info in info_list:
        print(info["version-string"])