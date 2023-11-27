# scrapy_splash

This Python Scrapy + Splash project is able to scrape the [Adamchoi](https://adamchoi.co.uk/overs/detailed) website, which is a JavaScript-based website.


## how to use:
```
$ docker run -it -p 8050:8050 scrapinghub/splash
$ scrapy crawl <app_name>
$ scrapy crawl <app_name> -o <output.ext>
$ docker <stop|rm> $(docker ps -aq)
```
