import scrapy

#Sem fazer o request pois o scrapy roda o parse() e é o callback default por trás.
class QuotesSpider(scrapy.Spider):
    name = 'quotes3'
    start_urls = [
        'http://quotes.toscrape.com/page/1'
    ]
  
    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            #yield scrapy.request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
        
        # for href in response.css('ul.pager a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)
        
        # for a in response.css('ul.pager a'):
        #     yield response.follow(a, callback=self.parse)
        
        # anchors = response.css('ul.pager a')
        # yield from response.follow_all(anchors, callback=self.parse)
        
        # yield from response.follow_all(css='ul.pager a', callback=self.parse)