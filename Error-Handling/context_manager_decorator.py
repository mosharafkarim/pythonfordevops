import os
from contextlib import contextmanager

@contextmanager
def change_directory(destination):

    try:
        origin_dir = os.getcwd()
        os.makedirs(destination, exist_ok=True)
        os.chdir(destination)
        yield os.getcwd()
    
    finally:
        print(f"Reverting to original dir: {origin_dir}")
        os.chdir(origin_dir)


print(f"Start: {os.getcwd()}")

with change_directory("temp_dir") as d:
    print(f"Inside: {d}")

print(f"End: {os.getcwd()}")
