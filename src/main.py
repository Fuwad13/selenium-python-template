from browsers.browser_factory import BrowserFactory

def main():
    browser = BrowserFactory.get_driver("chrome")
    browser.get("https://www.google.com")
    browser.quit()

if __name__ == "__main__":
    main()