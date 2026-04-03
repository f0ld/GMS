import json
import time
import os
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

#Little helper to load config.json
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

def main():
        config = load_config()
        start_url = config["start_url"]

        pdf_files = [] #This will save the temporary pdf files later on
        page_num = 1
        






if __name__ == "__main__":
    main()