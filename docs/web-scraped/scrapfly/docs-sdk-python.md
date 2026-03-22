# Source: https://scrapfly.io/docs/sdk/python

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/sdk/python

Markdown Content:
Python SDK
----------

Python SDK gives you a handy abstraction to interact with **Scrapfly API**. It includes all of scrapfly features and many convenient shortcuts:

*   Automatic base64 encode of JS snippet
*   Error Handling
*   Body json encode if `Content-Type: application/json`
*   Body URL encode and set `Content Type: application/x-www-form-urlencoded` if no content type specified
*   Convert Binary response into a python `ByteIO` object

### Step by Step Introduction

For a hands-on introduction see our Scrapfly SDK introduction page!

[Discover Now](https://scrapfly.io/docs/onboarding)

The Full python API specification is available here: [https://scrapfly.github.io/python-scrapfly/docs/scrapfly](https://scrapfly.github.io/python-scrapfly/scrapfly/)

> For more on Python SDK use with Scrapfly, select "Python SDK" option in Scrapfly docs top bar.

[Installation](https://scrapfly.io/docs/sdk/python#installation)
----------------------------------------------------------------

Source code of **Python SDK** is available on [Github](https://github.com/scrapfly/python-scrapfly)**scrapfly-sdk** package is available through [PyPi](https://pypi.org/).

`pip install 'scrapfly-sdk'`

You can also install extra package `scrapfly[speedups]` to get **[brotli](https://github.com/google/brotli)** compression and **[msgpack](https://msgpack.org/)** serialization benefits.

`pip install 'scrapfly-sdk[speedups]'`

You can also install `scrapfly[all]` to get all optional Scrapfly features without any extra impact on your scrapfly performance.

`pip install 'scrapfly-sdk[all]'`

[Scrape](https://scrapfly.io/docs/sdk/python#scrape_usage)
----------------------------------------------------------

> If you plan to scrape protected website - **make sure to enable [Anti Scraping Protection](https://scrapfly.io/docs/onboarding#asp)**

```
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}')

api_response:ScrapeApiResponse = scrapfly.scrape(scrape_config=ScrapeConfig(url='https://httpbin.dev/anything'))

# Automatic retry errors marked "retryable" and wait delay recommended before retrying
api_response:ScrapeApiResponse = scrapfly.resilient_scrape(scrape_config=ScrapeConfig(url='https://httpbin.dev/anything'))

# Automatic retry error based on status code
api_response:ScrapeApiResponse = scrapfly.resilient_scrape(scrape_config=ScrapeConfig(url='https://httpbin.dev/status/500'), retry_on_status_code=[500])

# scrape result, content, iframes, response headers, response cookies states, screenshots, ssl, dns etc
print(api_response.scrape_result)

# html content
print(api_response.scrape_result['content'])

# Context of scrape, session, webhook, asp, cache, debug
print(api_response.context)

# raw api result
print(api_response.content)

# True if the scrape respond with >= 200 < 300 http status
print(api_response.success)

# Api status code /!\ Not the api status code of the scrape!
print(api_response.status_code)

# Upstream website status code
print(api_response.upstream_status_code)

# Convert API Scrape Result into well known requests.Response object
print(api_response.upstream_result_into_response())
```

Discover python full specification:

*   Client : [https://scrapfly.github.io/python-scrapfly/scrapfly/client.html](https://scrapfly.github.io/python-scrapfly/scrapfly/client.html)
*   ScrapeConfig : [https://scrapfly.github.io/python-scrapfly/scrapfly/scrape_config.html](https://scrapfly.github.io/python-scrapfly/scrapfly/scrape_config.html)
*   API response : [https://scrapfly.github.io/python-scrapfly/scrapfly/api_response.html](https://scrapfly.github.io/python-scrapfly/scrapfly/api_response.html)

### [Using Context](https://scrapfly.io/docs/sdk/python#using-context)

```
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}')

with scrapfly as scraper:
    response: ScrapeApiResponse = scraper.scrape(ScrapeConfig(url='https://httpbin.dev/anything', country='fr'))
```

[How to configure Scrape Query](https://scrapfly.io/docs/sdk/python#parameters)
-------------------------------------------------------------------------------

You can check the `ScrapeConfig` implementation to check all available options [available here.](https://scrapfly.github.io/python-scrapfly/scrapfly/scrape_config.html)

All parameters listed in this documentation can be used when you construct the scrape config object.

[Download Binary Response](https://scrapfly.io/docs/sdk/python#download)
------------------------------------------------------------------------

```
from scrapfly import ScrapflyClient, ScrapeApiResponse

api_response:ScrapeApiResponse = scrapfly.scrape(scrape_config=ScrapeConfig(url='https://www.intel.com/content/www/us/en/ethernet-controllers/82599-10-gbe-controller-datasheet.html'))
scrapfly.sink(api_response) # you can specify path and name via named arguments
```

[Error Handling](https://scrapfly.io/docs/sdk/python#error_handling)
--------------------------------------------------------------------

Error handling is a big part of scraper, so we design a system to reflect what happened when it's going bad to handle it properly from Scraper. Here a simple snippet to handle errors on your owns

```
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse, UpstreamHttpClientError, \
ScrapflyScrapeError, UpstreamHttpServerError

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}')

try:
    api_response:ScrapeApiResponse = scrapfly.scrape(scrape_config=ScrapeConfig(
        url='https://httpbin.dev/status/404',
    ))
except UpstreamHttpClientError as e: # HTTP 400 - 500
    print(e.api_response.scrape_result['error'])
    raise e
except UpstreamHttpServerError as e:  # HTTP >= 500
    print(e.api_response.scrape_result['error'])
    raise e
# UpstreamHttpError can be used to catch all related error regarding the upstream website
except ScrapflyScrapeError as e:
    print(e.message)
    print(e.code)
    raise e
```

Errors with related code and explanation are documented and available [here](https://scrapfly.io/docs/scrape-api/errors), if you want to know more.

*   [scrapfly.UpstreamHttpClientError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.UpstreamHttpClientError) Upstream website that you scrape response with http code >= 300 < 400
*   [scrapfly.UpstreamHttpServerError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.UpstreamHttpServerError) Upstream website that you scrape response with http code >= 500 < 600
*   [scrapfly.ApiHttpClientError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ApiHttpClientError) Scrapfly API respond with >= 300 < 400
*   [scrapfly.ApiHttpServerError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ApiHttpServerError) Scrapfly API respond with >= 500 < 600
*   [scrapfly.ScrapflyProxyError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflyProxyError) Error related to Proxy
*   [scrapfly.ScrapflyThrottleError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflyThrottleError) Error related to Throttle
*   [scrapfly.ScrapflyAspError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflyAspError) Error related to ASP
*   [scrapfly.ScrapflyScheduleError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflyScheduleError) Error related to Schedule
*   [scrapfly.ScrapflyWebhookError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflyWebhookError) Error related to Webhook
*   [scrapfly.ScrapflySessionError](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.ScrapflySessionError) Error related to Session
*   [scrapfly.TooManyConcurrentRequest](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.TooManyConcurrentRequest) Maximum of concurrent request allowed by your plan reached
*   [scrapfly.QuotaLimitReached](https://scrapfly.github.io/python-scrapfly/scrapfly/index.html#scrapfly.QuotaLimitReached) Quota Limit of your plan or project reached

```
error.message              # Message
error.code                 # Error code of error
error.retry_delay         # Recommended time wait before retrying if retryable
error.retry_times         # Recommended retry times if retryable
error.resource            # Related resource, Proxy, ASP, Webhook, Spider
error.is_retryable        # True or False
error.documentation_url   # Documentation explaining the error in details
error.api_response        # Api Response object
error.http_status_code    # Http code
```

By default, if the upstream website that you scrape responds with bad HTTP code, the SDK will raise `UpstreamHttpClientError` or `UpstreamHttpServerError` regarding the HTTP status code. You can disable this behavior by setting the **raise_on_upstream_error** attribute to false. `ScrapeConfig(raise_on_upstream_error=False)`

If you want to report to your app for monitoring / tracking purpose on your side, checkout [reporter](https://scrapfly.io/docs/onboarding#reporter) feature.

[Account](https://scrapfly.io/docs/sdk/python#account)
------------------------------------------------------

You can retrieve account information

```
from scrapfly import ScrapflyClient

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}')
print(scrapfly.client.account())
```

[Keep Alive HTTP Session](https://scrapfly.io/docs/sdk/python#keep_alive_session)
---------------------------------------------------------------------------------

Take benefits of `Keep-Alive` Connection

```
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}')

with scrapfly as client:
    api_response:ScrapeApiResponse = scrapfly.scrape(scrape_config=ScrapeConfig(
        url='https://news.ycombinator.com/',
        render_js=True,
        screenshots={
            'main': 'fullpage'
        }
    ))
    # more scrape calls
```

[Concurrency out of the box](https://scrapfly.io/docs/sdk/python#concurrency)
-----------------------------------------------------------------------------

You can run scrape concurrently out of the box. We use `asyncio` for that.

In python, there are many ways to achieve concurrency. You can also check:

*   [ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)
*   [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)

First of all, ensure you have installed concurrency module

`pip install 'scrapfly-sdk[concurrency]'`

```
import asyncio

import logging as logger
from sys import stdout

scrapfly_logger = logger.getLogger('scrapfly')
scrapfly_logger.setLevel(logger.DEBUG)
logger.StreamHandler(stdout)

from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

scrapfly = ScrapflyClient(key='{{ YOUR_API_KEY }}', max_concurrency=2)

async def main():
    targets = [
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True),
        ScrapeConfig(url='https://httpbin.dev/anything', render_js=True)
    ]
    async for result in scrapfly.concurrent_scrape(scrape_configs=targets):
        print(result)

asyncio.run(main())
```

[Webhook Server](https://scrapfly.io/docs/sdk/python#webhook_server)
--------------------------------------------------------------------

The **Scrapfly Python SDK** offers a built-in webhook server feature, allowing developers to easily set up and handle webhooks for receiving notifications and data from Scrapfly services. This documentation provides an overview of the create_server function within the SDK, along with an example of its usage.

### Example Usage

> In order to expose the local server to internet we use [ngrok](https://ngrok.com/)and you need a free account to run the example.

Below is an example demonstrating how to use the create_server function to set up a webhook server:

1.   Install dependencies: `pip install ngrok flask scrapfly`
2.   Export your ngrok auth token in your terminal: `export NGROK_AUTHTOKEN=MY_NGROK_TOKEN`
3.    Create a webhook on your [Scrapfly dashboard](https://scrapfly.io/dashboard/webhook) with any endpoint (For example from [https://webhook.site](https://webhook.site/)). Since Ngrok endpoint is only known at runtime only and random on each run, we will edit the endpoint once ngrok advertised it in the next step. 
4.   Retrieve your webhook signing secret
5.   Run the command `python webhook_server.py --signing-secret=MY_SIGNING_SECRET`
6.   Once the server is running, copy the exposed url advertised below the log line `"====== LISTENING ON ======"`
7.   [Edit your webhook](https://scrapfly.io/dashboard/webhook) url and replace it by the advertised url

> With ngrok free plan, on each start of the server, a new random tunnel url is assigned, you need edit the webhook

```
import argparse
from typing import Dict
import flask
import ngrok
from scrapfly import webhook
from scrapfly.webhook import ResourceType

# Define the webhook callback function
def webhook_callback(data: Dict, resource_type: ResourceType, request: flask.Request):
    if resource_type == ResourceType.SCRAPE.value:
        # Process scrape result
        upstream_response = data['result']
        print(upstream_response)
    else:
        # Process other resource types
        print(data)

# Set up ngrok listener for tunneling
listener = ngrok.werkzeug_develop()

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Webhook server with signing secret")
parser.add_argument("--signing-secret", required=True, help="Signing secret to verify webhook payload integrity")
args = parser.parse_args()

# Create Flask application and set up webhook server
app = flask.Flask("Scrapfly Webhook Server")
webhook.create_server(signing_secrets=(args.signing_secret,), callback=webhook_callback, app=app)

# Start the server and print the webhook endpoint URL
print("====== LISTENING ON ======")
print(listener.url() + "/webhook")
print("==========================")
app.run()
```

In this example, the webhook server is set up using create_server, with a callback function webhook_callback defined to handle incoming webhook payloads. The signing secret is provided as a command-line argument, and ngrok is used for exposing the local server to the internet for testing.

[External Integration](https://scrapfly.io/docs/sdk/python#external_integration)
--------------------------------------------------------------------------------

### LlamaIndex

LlamaIndex, formerly known as GPT Index, is a data framework designed to facilitate the connection between large language models (LLMs) and a wide variety of data sources. It provides tools to effectively ingest, index, and query data within these models.

[Integrate Scrapfly with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/?h=scrap#using-scrapfly)

### Langchain

LangChain is a robust framework designed for developing applications powered by language models. It focuses on enabling the creation of applications that can leverage the capabilities of large language models (LLMs) for a variety of use cases.

[Integrate Scrapfly with Langchain](https://python.langchain.com/v0.2/docs/integrations/document_loaders/scrapfly/#scrapfly)
