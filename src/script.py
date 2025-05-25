import time
from browsers import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import base64 
from pathlib import Path

def main():
    # Initialize the browser
    browser: WebDriver = Browser.get_browser("chrome")

    # http://bdlaws.minlaw.gov.bd/act-print-700.html
    # [1, 1537]
    for act_page in range(238, 1538):
        browser.get(f"http://bdlaws.minlaw.gov.bd/act-print-{act_page}.html")
        pdf = browser.execute_cdp_cmd("Page.printToPDF", {"PrintBackground": True})
        filepath = Path(__file__).parent.parent / "ACT-PDF" / f"act-{act_page}.pdf"
        with open(filepath, "wb") as file:
            file.write(base64.b64decode(pdf['data']))
        print(f"Saved act-{act_page}.pdf")
        

    browser.quit()


if __name__ == "__main__":
    main()
