import time
import hashlib
import sys

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def watch(path, interval=2):
    last = file_hash(path)
    while True:
        time.sleep(interval)
        current = file_hash(path)
        if current != last:
            print(f"[CHANGED] {path}")
            last = current

if __name__ == "__main__":
    watch(sys.argv[1])
