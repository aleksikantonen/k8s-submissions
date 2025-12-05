import time
import uuid
from datetime import datetime

rand_string = str(uuid.uuid4())

while True:
    timestamp = datetime.now().isoformat()
    print(f"{timestamp}: {rand_string}")
    time.sleep(5)