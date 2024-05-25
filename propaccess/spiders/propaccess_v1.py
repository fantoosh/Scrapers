import scrapy
from scrapy import FormRequest


class PropaccessV1Spider(scrapy.Spider):
    name = "propaccess_v1"
    allowed_domains = ["example.com"]

    # start_urls = ["https://example.com"]

    def start_requests(self):
        yield scrapy.Request(
            url='https://propaccess.trueautomation.com/ClientDB/PropertySearch.aspx?cid=21',
            meta={'playwright': True, 'playwright_page': True},
        )

    def parse(self, response, **kwargs):
        page = response.meta['playwright_page']
        yield FormRequest.from_response(response,
                                        "https://propaccess.trueautomation.com/clientdb/PropertySearch.aspx?cid=93",
                                        formdata={
                                            "propertySearchOptions:searchText": "AB",
                                            "propertySearchOptions:search": "Search",
                                            "propertySearchOptions:ownerName": "",
                                            "propertySearchOptions:streetNumber": "",
                                            "propertySearchOptions:streetName": "",
                                            "propertySearchOptions:propertyid": "",
                                            "propertySearchOptions:geoid": "",
                                            "propertySearchOptions:dba": "",
                                            "propertySearchOptions:abstract": "",
                                            "propertySearchOptions:subdivision": "",
                                            "propertySearchOptions:mobileHome": "",
                                            "propertySearchOptions:condo": "",
                                            "propertySearchOptions:agentCode": "",
                                            "propertySearchOptions:taxyear": "2023",
                                            "propertySearchOptions:propertyType": "All",
                                            "propertySearchOptions:orderResultsBy": "Owner Name",
                                            "propertySearchOptions:recordsPerPage": "250",
                                        }, clickdata={'type': 'submit'})

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
