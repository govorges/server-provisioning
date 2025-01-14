print(__import__('json').dumps({key: { 
    subKey: str(subValue) for subKey, subValue in value.items()
} if not isinstance(value, str) else value for key, value in {
    config.name: config.__dict__ for config in __import__('configurations').Loading.ListServerConfigurations()
}.items()}, indent=2) if __import__("dotenv").load_dotenv() and __import__("os").environ.get('CLIENT_TOKEN') is not None \
else "CLIENT_TOKEN was not set in the environment")
# Obligatory overly-long-python-comprehension-for-fun. This file is still a WIP.



