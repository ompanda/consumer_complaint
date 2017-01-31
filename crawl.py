# import scrapy
#
#
# class ConsumerComplaintCrawl(scrapy.Spider):
#     name = "consumer_complaint"
#     start_urls = ['https://www.consumercomplaints.in/']
#
#     def parse(self, response):
#         print(response)
#         SET_SELECTOR = 'div'
#         for brickset in response.css(SET_SELECTOR):
#             NAME_SELECTOR = 'a'
#             yield {
#                 'name': brickset.css(NAME_SELECTOR).extract_first(),
#             }
#
#             # next_page = brickset.css('a::attr("href")').extract_first()
#             # if next_page is not None:
#             #     next_page = response.urljoin(next_page)
#             # yield scrapy.Request(next_page, callback=self.parse)



