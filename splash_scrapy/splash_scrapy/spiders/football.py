import scrapy
from scrapy_splash import SplashRequest


class FootballSpider(scrapy.Spider):
    name = "football"
    allowed_domains = ["adamchoi.co.uk"]
    start_url = "https://adamchoi.co.uk/overs/detailed"

    script = '''
        function main(splash, args)
            splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
            matches[2]:mouse_click()
            assert(splash:wait(0.5))
            splash:set_viewport_full()
            return {
                 html = splash:html()
            }
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url=self.start_url,
            callback=self.parse,
            endpoint="execute",
            args={"lua_source":self.script}
        )

    def parse(self, response):
        rows = response.xpath("//tr")
        for row in rows:
            date = row.xpath("./td[1]/text()").get()
            home_team = row.xpath("./td[2]/text()").get()
            score = row.xpath("./td[3]/text()").get()
            away_team = row.xpath("./td[4]/text()").get()

            yield {
                "date": date,
                "home_team": home_team,
                "score": score,
                "away_team": away_team
            }
