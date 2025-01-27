from dataclasses import dataclass
from typing import Optional

@dataclass
class DataIngestionArtifact: 
    feature_store_anime_file_path:str
    feature_store_userrating_file_path:str
