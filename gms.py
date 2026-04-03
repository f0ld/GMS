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
        print("loading config")
        config = load_config()
        start_url = config["start_url"]

        pdf_files = [] #This will save the temporary pdf files later on
        page_num = 1


        print("starting Browser...")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True) #starting Browser headless in the background

            #HTTP Basic Auth config (Hopefully this will work):
            context = browser.new_context(
                http_credentials={"username": config["username"], "password": config["password"]}
            )

        page = context.new_page()
        print(f"Navigate to: {start_url}")
        page.goto(start_url)



if __name__ == "__main__":
    main()