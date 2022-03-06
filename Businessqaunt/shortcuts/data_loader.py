import os

DATA_BASE_DIR = "Data"

data_path = lambda filename, *args: \
            os.path.join(DATA_BASE_DIR, *args, filename)
