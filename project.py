import subprocess
import time
import os

FRONTEND_PATH = r"C:\Users\Rushikesh\ddos-detection-ml\frontend"
BACKEND_PATH = r"C:\Users\Rushikesh\ddos-detection-ml\backend"

def start_frontend():
    print("Starting the React frontend...")
    subprocess.Popen(["npm", "start"], cwd=FRONTEND_PATH, shell=True)
    time.sleep(5)

def start_backend():
    print("Starting the upload server...")
    subprocess.Popen(["python", "upload.py"], cwd=BACKEND_PATH, shell=True)
    time.sleep(5)

    print("Triggering file upload...")
    subprocess.Popen(["python", "auto_upload.py"], cwd=BACKEND_PATH, shell=True)

def main():
    print("Starting the project...")
    start_frontend()
    start_backend()

if __name__ == "__main__":
    main()