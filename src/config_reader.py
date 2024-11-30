import os
import tomli

def get_config():
    config_file = os.path.join(os.path.dirname(__file__), "config", "config.toml")
    with open(config_file, "rb") as f:
        return tomli.load(f)