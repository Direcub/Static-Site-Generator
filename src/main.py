from textnode import *
from htmlnode import *
from standalone_methods import *
import os 
import shutil

def static_to_public(start, end):
    if os.path.exists(end):
        shutil.rmtree(end)
    os.mkdir(end)
    for item in os.listdir(start):
        start_path = os.path.join(start, item)
        end_path = os.path.join(end, item)
        if os.path.isfile(start_path):
            shutil.copy(start_path, end_path)
            print(f"Copied file: {end_path}")
        elif os.path.isdir(start_path):
            static_to_public(start_path, end_path)
            print(f"Copied file: {end_path}")
    


def main():
    static_to_public("static", "public")
    print("Starting page generation...")
    generate_pages_recursive("content/", "template.html","public")
    print("Page generation complete")



if __name__ == "__main__":
    main()