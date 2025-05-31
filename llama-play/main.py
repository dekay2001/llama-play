import src.analyzers as analyzer
import src.llama_config as configuration
import src.llama_logging as logging


def main():
    config = configuration.generate_config()
    stream = config.get('stream')
    model = config.get('model')
    log_analyzer = analyzer.create(model, stream)
    logger = logging.configure(config, log_analyzer)
    logger.info("Logging configured successfully.")


if __name__ == "__main__":
    main()
