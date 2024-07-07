import requests
from crewai_tools import BaseTool
from bs4 import BeautifulSoup

class HtmlScraperTool(BaseTool):
    name: str = "HTML Scraper Tool"
    description: str = "This tool scrapes the HTML content of a given URL and returns the prettified HTML."

    def _run(self, url: str) -> str:
        # Send a GET request to the URL
        response = requests.get(url)

        # If the GET request is successful, the status code will be 200
        if response.status_code == 200:
            # Get the content of the response
            page_content = response.content

            # Create a BeautifulSoup object and specify the parser
            soup = BeautifulSoup(page_content, 'html.parser')

            # Return the HTML page source
            return soup.prettify()
        else:
            return "Failed to retrieve the webpage."

# Test the custom tool
if __name__ == "__main__":
    scraper_tool = HtmlScraperTool()
    url = "https://www.saucedemo.com/v1/"  # Replace with your URL
    print(scraper_tool._run(url))
