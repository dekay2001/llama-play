import src.analyzers as analyzer
import src.llama_logging as logging

def main():
    config = {
        "log_level": "INFO",
    }
    logger = logging.configure(config, analyzer.LlamaChat('llama3.1'))
    logger.info("Logging configured successfully.")


if __name__ == "__main__":
    main()
