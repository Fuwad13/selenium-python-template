from browsers import Browser

def main():
    browser = Browser.get_browser("chrome")
    browser.get("https://www.google.com")
    browser.quit()

if __name__ == "__main__":
    main()