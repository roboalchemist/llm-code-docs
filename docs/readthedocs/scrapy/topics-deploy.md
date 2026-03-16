# Deploying Spiders

This section describes the different options you have for deploying your Scrapy
spiders to run them on a regular basis. Running Scrapy spiders in your local
machine is very convenient for the (early) development stage, but not so much
when you need to execute long-running spiders or move spiders to run in
production continuously. This is where the solutions for deploying Scrapy
spiders come in.

Popular choices for deploying Scrapy spiders are:

- 

Scrapyd (open source)

- 

Zyte Scrapy Cloud (cloud-based)

## Deploying to a Scrapyd Server

Scrapyd [https://github.com/scrapy/scrapyd] is an open source application to run Scrapy spiders. It provides
a server with HTTP API, capable of running and monitoring Scrapy spiders.

To deploy spiders to Scrapyd, you can use the scrapyd-deploy tool provided by
the scrapyd-client [https://github.com/scrapy/scrapyd-client] package. Please refer to the scrapyd-deploy
documentation [https://scrapyd.readthedocs.io/en/latest/deploy.html] for more information.

Scrapyd is maintained by some of the Scrapy developers.

## Deploying to Zyte Scrapy Cloud

Zyte Scrapy Cloud [https://www.zyte.com/scrapy-cloud/] is a hosted, cloud-based service by Zyte [https://www.zyte.com/], the company
behind Scrapy.

Zyte Scrapy Cloud removes the need to setup and monitor servers and provides a
nice UI to manage spiders and review scraped items, logs and stats.

To deploy spiders to Zyte Scrapy Cloud you can use the shub [https://shub.readthedocs.io/en/latest/] command line
tool.
Please refer to the Zyte Scrapy Cloud documentation [https://docs.zyte.com/scrapy-cloud.html] for more information.

Zyte Scrapy Cloud is compatible with Scrapyd and one can switch between
them as needed - the configuration is read from the `scrapy.cfg` file
just like `scrapyd-deploy`.