from scrapy.crawler import CrawlerProcess
from propaccess.spiders.propaccess_v2 import PropaccessV2Spider


def main():
    # Create a CrawlerProcess instance
    process = CrawlerProcess()
    process.crawl(PropaccessV2Spider)
    process.start()


if __name__ == '__main__':
    main()
