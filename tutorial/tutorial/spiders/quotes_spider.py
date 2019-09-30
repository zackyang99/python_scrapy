import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    


    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #    self.log('Saved file %s' % filename)
		
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        # use urljoin to create full url
		#if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)	

		# response.follow supports relative url
        #if next_page is not None:
        #    yield response.follow(next_page, callback = self.parse)
		
		#For <a> elements there is a shortcut: response.follow uses their href attribute automatically	
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			