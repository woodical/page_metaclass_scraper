import scraper
import fact


class KoderScraper(scraper.Scraper):
    cando = fact.StringFact('//*[@id="main-content"]/p[17]')
    what = fact.StringFact('//*[@id="main-content"]/p[1]')

    @classmethod
    def clean_cando(cls, value):
        return value.upper()

    @classmethod
    def clean_what(cls, value):
        return value.lower()


if __name__ == "__main__":
    url = "https://www.koderhq.com/tutorial/rust/trait/"
    result = KoderScraper(url)
    print(f"URL {url}")
    for fact_name, fact_value in result.items():
        print(f"\tFact : {fact_name}\n\t{fact_value}")
        print("-" * 80)
