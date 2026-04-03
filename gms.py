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

        while True:
            page.wait_for_load_state("networkidle") #Wait for everything to load because the Math Stuff needs bandwidth
            time.sleep(2) #Short Buffer to wait for JavasSript-Render (maybe needs an increase...)

            #Save Page as PDF
            pdf_filename = f"temp_page_{page_num:03d}.pdf"
            page.pdf(
                path=pdf_filename,
                format = "A4",
                print_background = True,
                margin = {"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
            )
            pdf_files.append(pdf_filename)
            print(f"Saved: Page {page_num} ({page.url}")

            #seach for next page button (might need to check if MySt standard classes are used)
            next_button = page.locator("a.right-next, a.next-page, a.next").first
            if next_button.count() > 0 and next_button.is_visible():
                print("Jumping to next page...")
                next_button.click()
                page_num += 1
            else:
                print("No Next Button found. End of Script reached...")
                break

        browser.close()

        


if __name__ == "__main__":
    main()