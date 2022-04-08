import scrapy

#Sem fazer o request pois o scrapy roda o parse() e é o callback default por trás.
class QuotesSpider(scrapy.Spider):
    name = 'quotes2'
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        'http://quotes.toscrape.com/page/2'
    ]
  
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes2-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
