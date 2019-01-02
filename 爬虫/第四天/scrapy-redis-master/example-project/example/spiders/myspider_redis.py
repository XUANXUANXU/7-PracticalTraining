from scrapy_redis.spiders import RedisSpider
import scrapy

class MySpider(RedisSpider):
    #step1:将爬虫文件继承的类修改为RedisSpider
    #step2:将start_urls删除，添加redis_key

    #注意事项：
    #  1.构建Resqest对象,meta携带参数的时候，不能携带Selector对象
    #　2.不能够重写start_requests方法

    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
