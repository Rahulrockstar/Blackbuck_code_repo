import os
import subprocess

# Open the downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
subprocess.Popen(f'explorer "{downloads_folder}"')

# Launch a certain application (e.g. Notepad)
subprocess.Popen('notepad.exe')
