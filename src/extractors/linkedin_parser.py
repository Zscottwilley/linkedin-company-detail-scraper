thonimport requests
from bs4 import BeautifulSoup
from config.settings import LINKEDIN_COOKIES

class LinkedInParser:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Cookie": LINKEDIN_COOKIES
        }

    def parse_company_data(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the URL: {url}")

        soup = BeautifulSoup(response.content, 'html.parser')

        company_data = {
            "name": self.extract_company_name(soup),
            "url": url,
            "description": self.extract_description(soup),
            "industry": self.extract_industry(soup),
            "contact_details": self.extract_contact_details(soup),
            "employee_count": self.extract_employee_count(soup),
            "followers_count": self.extract_followers_count(soup),
            "logo": self.extract_logo(soup)
        }
        
        return company_data

    def extract_company_name(self, soup):
        return soup.find("h1", {"class": "org-top-card-summary__title"}).text.strip()

    def extract_description(self, soup):
        return soup.find("div", {"class": "org-top-card-summary__tagline"}).text.strip()

    def extract_industry(self, soup):
        return soup.find("div", {"class": "org-top-card-summary__industry"}).text.strip()

    def extract_contact_details(self, soup):
        contact_info = soup.find("div", {"class": "org-contact-info"})
        return {
            "phone": contact_info.find("span", {"class": "contact-info__phone"}).text.strip(),
            "website": contact_info.find("a", {"class": "org-contact-info__website"}).text.strip()
        }

    def extract_employee_count(self, soup):
        return int(soup.find("div", {"class": "org-top-card-summary__employees-count"}).text.strip().split()[0])

    def extract_followers_count(self, soup):
        return int(soup.find("span", {"class": "org-top-card-summary__followers-count"}).text.strip())

    def extract_logo(self, soup):
        logo_tag = soup.find("img", {"class": "org-top-card-summary__logo"})
        return logo_tag["src"] if logo_tag else None