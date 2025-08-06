import yaml
import os
def read_config():
    with open(os.path.join("config", "config.yaml"), "r") as f:
        return yaml.safe_load(f)
def get_username():
    return read_config().get("username")
def get_password():
    return read_config().get("password")
