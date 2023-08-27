"""Nothing you should concern yourself with"""
import pyperclip
from datetime import datetime

# Copy current tz aware timestamp to clipboard

pyperclip.copy(int(datetime.now().astimezone().timestamp()))
print("Copied local timestamp to your clipboard")