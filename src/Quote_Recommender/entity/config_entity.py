from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    save_path: Path
    tags: list
    num_pages: int