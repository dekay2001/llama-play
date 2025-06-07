import src.analyzers as analyzer
import src.llama_config as configuration
import src.llama_logging as logging


class LoggingAppTestHarness:
    def __init__(self):
        logging.info("Initializing LoggingAppTestHarness...")
        self.config = configuration.generate_config()
        self.stream = self.config.get('stream')
        self.model = self.config.get('model')
        self.log_analyzer = analyzer.create(self.model, self.stream, self.config)
        self.logger = logging.configure(self.config, self.log_analyzer)
        self.logger.info("LoggingAppTestHarness initialized successfully.")

    def run(self):
        self.logger.info("Running self.loggerAppTestHarness...")
        self.logger.info("This is a test log message.")
        self.logger.warning("This is a test warning message.")
        self.logger.error("This is a test error message.")
        self.logger.debug("This is a test debug message.")
        self.logger.critical("This is a test critical message.")
        self.logger.exception("This is a test exception message.")



def main():
    app = LoggingAppTestHarness()
    app.run()

if __name__ == "__main__":
    main()
