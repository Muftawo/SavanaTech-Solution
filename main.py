import logging

from src.extract import Extract
from src.transform import transformer


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:
    setup_logging()

    org_name = "Scytale-exercise"

    logging.info("Begin data extraction...")
    Extract.extract_and_save(org_name)
    logging.info("Extraction completed !!")

    logging.info("Begin Trasnformation...")
    transformer()
    logging.info("Transformation Done.")


if __name__ == "__main__":
    main()
