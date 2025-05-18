import logging
from logging import *

class AiLogger(logging.Handler):
        def __init__(self):
            super().__init__()
            self.model = None
            
        def set_model(self, model):
            self.model = model            

        def emit(self, record):
            log_message = self.format(record)
            self.model.analyze(log_message)

        def close(self):
          super().close()


def configure(config, model):
    # Create a logger
    log_level = config.get("log_level", logging.INFO)
    logger = logging.getLogger("AiLogger")
    logger.setLevel(log_level)

    # Create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # Create a formatter and set it for the console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(ch)

    # Add the custom handler
    custom_handler = AiLogger()
    custom_handler.set_model(model)
    custom_handler.setFormatter(formatter)
    logger.addHandler(custom_handler)

    return logger