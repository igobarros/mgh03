from pathlib import Path  # python3 only
from dotenv import load_dotenv
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

GMAPS_API = os.getenv("GMAPS_API")
ATLAS_URI = os.getenv("ATLAS_URI")
GMAPS_API_TWO = os.getenv("GMAPS_API_TWO")