from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "ReactionMaster")
DEFAULT_GRADE = int(os.getenv("DEFAULT_GRADE", 8))
ENABLE_HINTS = os.getenv("ENABLE_HINTS", "true").lower() == "true"
MAX_COEFFICIENT = int(os.getenv("MAX_COEFFICIENT", 12))
RANDOM_SEED = int(os.getenv("RANDOM_SEED", 0))
