from logging import getLogger, WARNING
import sys
from pathlib import Path
import json
import re

from pydub import AudioSegment

logger = getLogger(__name__)
logger.setLevel(WARNING)

CONFIG_FILE_PATH = "../config/audio-config.json"
SRC_FILE_DIR = "../mp3"

OUT_FILE_PATH = "../out.mp3"


class AudioCombiner():

    def __init__(self) -> None:

        conf_file = Path(CONFIG_FILE_PATH)

        print("Loading files...")

        if not conf_file.exists():
            logger.error("config file path is incorrect.")

        with open(str(conf_file)) as f:
            config = json.load(f)
            self.sections = config.get("sections", [])
            if len(self.sections) == 0:
                logger.warning(
                    "Please specify sections info in your config file.")

            self.metadata = config.get("metadata", {})

        src_file_dir = Path(SRC_FILE_DIR)

        if not src_file_dir.exists():
            logger.error("Source file path is incorrect.")
            sys.exit(1)

        try:
            self.src_files_path = sorted(src_file_dir.glob(
                "*.mp3"), key=lambda n: int(re.sub(r"\D", "", str(n))))
        except ValueError as e:
            logger.error(
                f"Please include an integer in your mp3 file names.({e})")

        self.src_files = [AudioSegment.from_file(
            str(f), format="mp3") for f in self.src_files_path]

        print(f"Got {len(self.src_files)} file(s)")

    def exec(self):

        result = AudioSegment.silent(duration=0)

        for section in self.sections:
            source = self.src_files[int(section.get("source", None))]
            start = int(1000 * section.get("start", 0))
            end = int(1000 * section.get("end")
                      ) if "end" in section else None
            silent_after = int(1000*section.get("silentAfter", 0))

            result += source[start:end]
            if silent_after > 0:
                result += AudioSegment.silent(duration=silent_after)

        print("Processing...")
        result.export(OUT_FILE_PATH, format="mp3", tags=self.metadata)
        print(f"file is saved to {str(Path(OUT_FILE_PATH))}")


if __name__ == "__main__":
    AudioCombiner().exec()
