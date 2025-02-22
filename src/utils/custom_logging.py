import logging


def setup_basic_logging(nom_logger: str, fichier_log: str) -> logging.Logger:
    logger = logging.getLogger(nom_logger)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(fichier_log), logging.StreamHandler()],
    )
    return logger


def setup_advanced_logging(nom_logger: str, fichier_log: str) -> logging.Logger:
    logger = logging.getLogger(nom_logger)
    logger.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # create console handler and set level to debug
    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = logging.FileHandler(fichier_log)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


if __name__ == "__main__":
    log = setup_advanced_logging("advanced", "fichier")
    log.debug("message debug")
    log.info("message info")
    log.warning("message warning")
    log.error("message error")
