
import os
import sys
import shutil


url_prefix = "https://github.com/MoonShineVFX/reveries-config/archive"


def build(source_path, build_path, install_path, targets=None):
    from rezutil import lib

    targets = targets or []

    if "install" in targets:
        dst = install_path + "/payload"
    else:
        dst = build_path + "/payload"

    dst = os.path.normpath(dst)

    if os.path.isdir(dst):
        shutil.rmtree(dst)

    filename = "%s.zip" % os.environ["REZ_BUILD_PROJECT_VERSION"]

    # Download the source
    url = "%s/%s" % (url_prefix, filename)
    archive = lib.download(url, filename)

    # Unzip the source
    source_root = lib.open_archive(archive)

    # Deploy
    shutil.copytree(source_root, dst)

    # (TODO) Deploy Deadline scripts
    #   (or decouple it into another repo)


if __name__ == "__main__":
    build(source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
          build_path=os.environ["REZ_BUILD_PATH"],
          install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
          targets=sys.argv[1:])
