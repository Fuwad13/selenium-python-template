# Selenium Python Template

A template repository for Selenium WebDriver automation projects using Python. This template provides a structured foundation for creating browser automation scripts with cross-platform support.

## Features

- Cross-platform support for Windows and Linux environments
- Structured directory organization for maintainable code
- Preconfigured browser drivers for Chrome and Firefox
- Factory pattern implementation for easy browser instantiation
- Configuration management using pydantic-settings

## Directory Structure

```
selenium-python-template/
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── browsers/
│   │   ├── __init__.py
│   │   └── browser.py
│   └── webdrivers/
│       ├── linux/
│       │   ├── chrome/
│       │   │   └── chromedriver
│       │   └── firefox/
│       │       └── geckodriver
│       └── windows/
│           └── chrome/
│               └── chromedriver.exe
```

## Requirements

- Python 3.x
- Required packages listed in `requirements.txt`:
  - pip==24.3.1
  - pydantic-settings==2.8.1
  - PySocks==1.7.1
  - selenium==4.30.0

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/selenium-python-template.git
   cd selenium-python-template
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the correct WebDriver versions for your browser installations.
   - The template includes WebDrivers for Chrome and Firefox, but you may need to update them to match your browser versions.

## Usage

The template provides a simple demonstration in the `__main__.py` file:

```python
from browsers import Browser

def main():
    browser = Browser.get_browser("chrome")
    browser.get("https://www.google.com")
    browser.quit()

if __name__ == "__main__":
    main()
```

To run the example:

```bash
python -m src
```

## Customization

### Adding Custom Browser Options

Modify the `Browser` class in `src/browsers/browser.py` to add custom browser options:

```python
# Example for Chrome
options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--headless")  # Add headless mode
options.add_argument("--disable-gpu")  # Add additional options
```

### Updating WebDriver Paths

Edit the `config.py` file to update paths to WebDrivers:

```python
CHROMEDRIVER_PATH_LINUX: Path = Path("path/to/your/chromedriver")
CHROMEDRIVER_PATH_WINDOWS: Path = Path("path/to/your/chromedriver.exe")
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## License

This project is licensed under the terms included in the LICENSE file.
