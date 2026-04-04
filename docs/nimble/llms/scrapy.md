# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/scrapy.md

# Scrapy

Scrapy is a popular open-source web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It is written in Python and provides a complete toolset for scraping tasks.&#x20;

Scrapy simplifies the process of writing complex spiders, which are programs that browse the Web and extract data based on a set of instructions. It's highly extensible, allowing for the implementation of custom functionality through plugins, and it can handle a wide range of web scraping and crawling tasks, making it an ideal choice for projects ranging from simple data extraction to large-scale web mining.

## Configuration

#### **Setting Up Your Nimble Account**

If you haven't already, you'll need to create an account with [Nimble](https://nimbleway.com/) to access their Web API [here](https://nimbleway.com/nimble-api/web/).

#### **Configure Scrapy Settings**

The first step is to install Nimble's Scrapy middleware using `pip`:

```bash
pip install scrapy-nimble
```

Next, configure your Scrapy project to interact with Nimble's Web API by updating your [settings.py](https://pypi.org/):&#x20;

```python
# settings.py
NIMBLE_ENABLED = True

NIMBLE_USERNAME = "username"
NIMBLE_PASSWORD = "password"
```

Then, add the Nimble middleware to your downloader middlewares:

```python
# settings.py
DOWNLOADER_MIDDLEWARES = {
    "scrapy_nimble.middlewares.NimbleWebApiMiddleware": 570,
}
```

Ensure that the Nimble middleware is configured to run before the default `scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware` which is enabled by default in [DOWNLOADER\_MIDDLEWARES\_BASE](https://docs.scrapy.org/en/latest/topics/settings.html#std-setting-DOWNLOADER_MIDDLEWARES_BASE) set at an order of 590.

## Basic Usage

### **Middleware Handling**

With the middleware configured, every request sent from your Scrapy spiders will automatically pass through the Nimble Web API. There's no need for additional changes in your spider code for basic usage.

### Advanced Features

#### **Real-time URL Requests**

The [Nimble Web API](https://docs.nimbleway.io/general/faqs/nimble-api) enhances your scraping capabilities with options for real-time URL requests. This feature allows for dynamic content rendering, geolocated requests, and [more](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions).

![](https://lh7-us.googleusercontent.com/y6rzwqSZ6qpp39zea1A40Ckq31XtDEuLJO6QOaaZBv7iE4-bnNnCZy_kLYbyLh_AQmS6NKHwgZzUOEk_LpQjuHNhKLsYk_6rE8KbxJOnOVqloNN72u5Tlr8kgt80Q4dGa_ln-6ObQA5bd6DaO2krPbE)&#x20;

To use these features, you add specific options in the meta section of your request. Here’s how you can specify these options:

```python
# Inside your spider
yield scrapy.Request(
   "https://nimbleway.com",
   meta={
      "nimble_country": "DE",
      "nimble_locale": "uk",
      "nimble_render": True,
   }
)
```

### Development Environment Setup

#### **Python Environment**

It's recommended to use [pyenv](https://github.com/pyenv/pyenv) for managing Python versions and creating an isolated development environment:

```bash
pyenv virtualenv 3.11.6 myvenv
pyenv activate myvenv
python -m pip install -e .
```

Now, your development environment is set up, and you're ready to develop your Scrapy project with Nimble's Web API.
