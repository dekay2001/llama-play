import os

from abc import ABC, abstractmethod


class ConfigInterface(ABC):
    @abstractmethod
    def get(self, key: str, default=None):
        pass

_ANALYSIS_LOG_FILE = os.path.join(os.getcwd(), 'analysis-thor.log')

DEFAULT_CONFIG = {
    'log_level': 'INFO',
    'stream': True,
    #'model': 'llama3.1',
    'model': 'Thor',
    'file_path': _ANALYSIS_LOG_FILE,
}

class _DictConfig(ConfigInterface):
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


