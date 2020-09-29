
early = globals()["early"]


name = "reveries"

description = "Avalon post-production pipeline configuration module"

version = "1.1.0"

authors = [
    "davidlatwe",
    "rebeccalin209",
]


tools = [
]

requires = [
    # Dependencies
    "house",
    "avalon",
    "avalon_sftpc",
    "pyblish_qml",
]


private_build_requires = ["rezutil-1"]
build_command = "python {root}/rezbuild.py {install}"


# Set up environment
def commands():
    env = globals()["env"]
    resolve = globals()["resolve"]
    env.PYTHONPATH.prepend("{root}/payload")

    # Config
    env.AVALON_CONFIG = "reveries"
    env.CONFIG_ROOT = "{root}/payload"

    # Deadline
    env.AVALON_DEADLINE = "{env.HOUSE_PIPELINE_DEADLINE}"
    env.AVALON_DEADLINE_AUTH = "{env.HOUSE_PIPELINE_DEADLINE_AUTH}"
    env.AVALON_DEADLINE_APP = "{env.HOUSE_PIPELINE_DEADLINE_APP}"

    # DCC App Setup
    if "houdini" in resolve:
        env.HOUDINI_NO_ENV_FILE = "1"
        env.HOUDINI_MENU_PATH.append("{root}/payload/res/houdini")
        env.HOUDINI_OTLSCAN_PATH.append("{root}/payload/res/houdini/hda")
        env.AVALON_CACHE_ROOT = "Q:"

    if "nuke" in resolve:
        env.NUKE_PATH.append("{root}/payload/res/nuke/icons")
