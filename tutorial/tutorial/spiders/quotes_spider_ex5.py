import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes4'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get().replace("\u201c", "'").replace("\u201d","'").replace("\u2019","'"),
                'author': quote.css('small.author::text').get()
            }
        next_page = response.css('li.next a::attr(href').get()
        if next_page is not None:
            yield response.folow(next_page, self.parse)
