from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_jobs.items import CraigslistJobsItem

class MySpider(BaseSpider):
	name = "craig"
	allowed_domains = ["craigslist.org"]
	start_urls = ["https://newyork.craigslist.org/search/jjj"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//span[@class='pl']")
		for titles in titles:
			title = titles.select("a/text()").extract()
			link  = titles.select("a/@href").extract
			print title, link