from email.policy import default
import scrapy

#Sem fazer o request pois o scrapy roda o parse() e é o callback default por trás.
class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
  
    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)
    
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthday': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text')
        }