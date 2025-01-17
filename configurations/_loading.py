"""Contains functions used for loading server configurations."""
from os import listdir
from os import path

from importlib import import_module

from ._configuration import Configuration

# from os.path import isfile, isdir

CONFIGURATIONS_DIR = path.dirname(path.realpath(__file__))

def ListServerConfigurations(file: None | str = None) -> list:
    """
    Lists all present server configurations. 
    If `file` is provided and is not None, lists only server configurations present in the given JSON filename.
    Otherwise, all objects inherited from the Configuration class in every Python filename will be returned.
    """
    server_configurations = []

    if file is None:
        config_files = listdir(CONFIGURATIONS_DIR)
    else:
        config_files = [file]

    for _file in config_files:
        if not path.isfile(path.join(CONFIGURATIONS_DIR, _file)):
            continue
        filename, ext = _file.rsplit(".", 1)
        if ext != "py":
            continue
        if "_" in filename:
            continue

        configuration_file = import_module(f"configurations.{filename}")
        try:
            server_configurations.append(configuration_file.SERVER_CONFIGURATION)
        except:
            print(f"WARNING: No variable named `SERVER_CONFIGURATION` present in configuration file `{_file}`")
    return server_configurations

def GetConfigurationByName(name: str) -> Configuration:
    server_configurations = ListServerConfigurations()
    for configuration in server_configurations:
        if configuration._name == name:
            return configuration
    return None

if __name__ == "__main__":
    ListServerConfigurations(None)