from abc import ABC, abstractmethod


class ConfigInerface(ABC):
    @abstractmethod
    def get(self, key: str, default=None):
        pass


DEFAULT_CONFIG = {
    'log_level': 'INFO',
    'stream': False,
    'model': 'llama3.1',
}

class _DictConfig(ConfigInerface):
    def __init__(self, config: dict):
        self._config = config

    def get(self, key: str, default=None):
        return self._config.get(key, default)


config = None

def generate_config():
    global config
    if config is None:
        config = _DictConfig(DEFAULT_CONFIG)
    return config


