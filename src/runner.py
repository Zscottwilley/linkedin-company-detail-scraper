thonimport json
import requests
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import JSONExporter
from config.settings import API_URL

def run_scraper(company_urls):
    parser = LinkedInParser()
    exporter = JSONExporter()

    all_company_data = []

    for url in company_urls:
        try:
            print(f"Scraping data for: {url}")
            company_data = parser.parse_company_data(url)
            all_company_data.append(company_data)
        except Exception as e:
            print(f"Error while scraping {url}: {e}")
    
    exporter.export_data(all_company_data, "output.json")
    print(f"Scraping completed. Data saved to output.json")

if __name__ == "__main__":
    company_urls = ["https://www.linkedin.com/company/company-1", "https://www.linkedin.com/company/company-2"]
    run_scraper(company_urls)