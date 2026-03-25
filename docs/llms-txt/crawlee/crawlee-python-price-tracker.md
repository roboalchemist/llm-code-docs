# Source: https://crawlee.dev/blog/crawlee-python-price-tracker.md

# How to build a price tracker with Crawlee and Apify

April 8, 2025 ·

<!-- -->

11 min read

[![Percival Villalva](https://avatars.githubusercontent.com/u/70678259?v=4)](https://github.com/PerVillalva)

[Percival Villalva](https://github.com/PerVillalva)

Community Member of Crawlee

Build a price tracker with Crawlee for Python to scrape product details, export data in multiple formats, and send email alerts for price drops, then deploy and schedule it as an Apify Actor.

![Crawlee for Python Price Tracker](/assets/images/crawlee-python-price-tracker-8ffc0121eee82024852513938dd525ab.webp)

In this tutorial, we’ll build a price tracker using Crawlee for Python and Apify. By the end, you’ll have an Apify Actor that scrapes product details from a webpage, exports the data in various formats (CSV, Excel, JSON, and more), and sends an email alert when the product’s price falls below your specified threshold.

## 1. Project Setup[​](#1-project-setup "Direct link to 1. Project Setup")

Our first step is to install the [Apify CLI](https://docs.apify.com/cli/docs). You can do this using either Homebrew or NPM with the following commands: s

### Homebrew[​](#homebrew "Direct link to Homebrew")

```
brew install apify-cli
```

### Via NPM[​](#via-npm "Direct link to Via NPM")

```
npm -g install apify-cli
```

Next, let’s run the following commands to use one of Apify’s pre-built templates. This will streamline the setup process and get us coding right away:

```
apify create price-tracking-actor
```

A dropdown list will appear. To follow along with this tutorial, select **`Python`** and **`Crawlee + BeautifulSoup`** `template`. Once the template is installed, navigate to the newly created folder and open it in your preferred IDE.

![actor-templates](/assets/images/actor-templates-88fa253dabe612261cb2fe95430c4c04.webp)

Navigate to **`src/main.py`** in your project, and you’ll find that a significant amount of boilerplate code has already been generated for you. If you’re new to Apify or Crawlee, don’t worry, it’s not as complex as it might seem. This pre-written code is designed to save you time and jumpstart your development process.

![crawlee-bs4-template](/assets/images/crawlee-bs4-template-528a9eee4ab1c859feb2ed42e3328045.webp)

In fact, this template comes with fully functional code that scrapes the Apify homepage. To test it out, simply run the command **`apify run`**. Within a few seconds, you’ll see the **`storage/datasets`** directory populate with the scraped data in JSON format.

![json-data](/assets/images/json-data-9ec19a8958775e66dcd094d0d46faa90.webp)

## 2. Customizing the template[​](#2-customizing-the-template "Direct link to 2. Customizing the template")

Now that our project is set up, let’s customize the template to scrape our target website: [Raspberry Pi 5 (8GB RAM) on Central Computer](https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html).

First, on the `src/main.py` file, go to the `crawler.run(start_urls)` and replace it with the URL for the target website, as shown below:

```
await crawler.run(['https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html'])
```

Normally, you could let users specify a URL through the Actor input, and the Actor would prioritize it. However, since we’re scraping a specific page, we’ll just use the hardcoded URL for simplicity. Keep in mind that dynamic input is still an option if you want to make the Actor more flexible later.

### Extracting the Product’s Name and Price[​](#extracting-the-products-name-and-price "Direct link to Extracting the Product’s Name and Price")

Finally, let’s modify our template to extract key elements from the page, such as the product name and price.

Starting with the **product name**, inspect the [target page](https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html) using DevTools to find suitable selectors for targeting the element.

![product-name](/assets/images/product-name-dbaba09d2d06b4b8a6b9a340698739af.webp)

Next, create a `product_name_element` variable to hold the element selected with the CSS selectors found on the page and update the `data` dictionary with the element’s text contents. Also, remove the line of code that previously made the Actor crawl the Apify website, as we now want it to scrape only a single page.

Your `request_handler` function should look similar to the example below:

```
@crawler.router.default_handler
async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
    url = context.request.url
    Actor.log.info(f'Scraping {url}...')

    # Select the product name and price elements.
    product_name_element = context.soup.find('div', class_='productname')

    # Extract the desired data.
    data = {
        'url': context.request.url,
        'product_name': product_name_element.text.strip() if product_name_element else None,
    }

    # Store the extracted data to the default dataset.
    await context.push_data(data)

    # Enqueue additional links found on the current page.
    # await context.enqueue_links() -> REMOVE THIS LINE
```

It’s a good practice to test our code after every significant change to ensure it works as expected.

Run `apify run` again, but this time, add the `–-purge` flag to prevent the newly scraped data from mixing with previous runs:

```
apify run --purge
```

Navigate to `storage/datasets`, and you should find a file with the scraped content:

```
{
    "url": "https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html",
    "product_name": "Raspberry Pi 5 8GB RAM Board"}
}
```

Now that you’ve got the hang of it, let’s do the same thing for the price: `79.99`.

![product\_price.png](/assets/images/product-price-fa3ab906b4a95258251defe78c19b6d3.webp)

In the code below, you’ll notice a slight difference: instead of extracting the element’s text content, we’re retrieving the value of its `data-price-amount` attribute. This approach avoids capturing the dollar sign `($)` that would otherwise come with the text.

If you prefer working with text content instead, that’s perfectly fine, you can simply use `.replace('$', '')` to remove the dollar sign.

Also, keep in mind that the extracted price will be a `string` by default. To perform numerical comparisons, we need to convert it to a `float`. This conversion will allow us to accurately compare the price values later on.

Here’s how the updated code looks so far:

```
# main.py

# ...previous code

@crawler.router.default_handler
async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
    url = context.request.url
    Actor.log.info(f'Scraping {url}...')

    # Select the product name and price elements.
    product_name_element = context.soup.find('div', class_='productname')
    product_price_element = context.soup.find('span', id='product-price-395001')

    # Extract the desired data.
    data = {
        'url': context.request.url,       
        'product_name': product_name_element.text.strip() if product_name_element else None,
        'price': float(product_price_element['data-price-amount']) if product_price_element else None,
    }

    # Store the extracted data to the default dataset.
    await context.push_data(data)
```

Again, try running it with `apify run --purge` and check if you get a similar output as the example below:

```
{
    "url": "https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html", 
    "product_name": "Raspberry Pi 5 8GB RAM Board", 
    "price": 79.99
}
```

That’s it for the extraction part! Below is the complete code we’ve written so far.

> 💡 **TIP:** If you’d like to get some more practice, try scraping additional elements such as the **`model`**, **`Item #`**, or **`stock availability (In stock)`**.

```
# main.py

from apify import Actor
from crawler.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext


async def main() -> None:

    # Enter the context of the Actor.
    async with Actor:
        # Create a crawler.
        crawler = BeautifulSoupCrawler(
            # Limit the crawl to max requests. Remove or increase it for crawling all links.
            max_requests_per_crawl=50,
        )

        # Define a request handler, which will be called for every request.
        @crawler.router.default_handler
        async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
            url = context.request.url
            Actor.log.info(f'Scraping {url}...')
            
            # Select the product name and price elements.
            product_name_element = context.soup.find('div', class_='productname')
            product_price_element = context.soup.find('span', id='product-price-395001')

            # Extract the desired data.
            data = {
                'url': context.request.url,
                'product_name': product_name_element.text.strip() if product_name_element else None,
                'price': float(product_price_element['data-price-amount']) if product_price_element else None,
            }

            # Store the extracted data to the default dataset.
            await context.push_data(data)

        # Run the crawler with the starting requests.
        await crawler.run(['https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html'])
```

## 3. Sending an Email Alert[​](#3-sending-an-email-alert "Direct link to 3. Sending an Email Alert")

From this point forward, you’ll need an **Apify account**. You can create one for free [here](https://console.apify.com/sign-up).

We need an Apify account because we’ll be making an API call to a pre-existing Actor from the **Apify Store,** the “Send Email Actor”, to handle notifications. Apify’s email system takes care of sending alerts, so we don’t have to worry about handling **2FA** in our automation.

```
# main.py

# ...previous code

# Define a price threshold
price_threshold = 80

# Call the "Send Email" Actor when the price goes below the threshold            
if data['price'] < price_threshold:
    actor_run = await Actor.start(
        actor_id="apify/send-mail",
        run_input={
            "to": "your_email@email.com",
            "subject": "Python Price Alert",
            "text": f"The price of '{data['product_name']}' has dropped below ${price_threshold} and is now ${data['price']}.\n\nCheck it out here: {data['url']}",
        },
    )
    Actor.log.info(f"Email sent with run ID: {actor_run.id}")
```

In the code above, we’re using the **Apify Python SDK**, which is already included in our project, to call the “Send Email” Actor with the required input.

To make this API call work, you’ll need to log in to your Apify account from the terminal using your **`APIFY_API_TOKEN`**.

To get your **`APIFY_API_TOKEN`**, sign up for an Apify account, then navigate to **Settings → API & Integrations**, and copy your **Personal API token**.

![apify-api-token](/assets/images/apify-api-token-eb76078df32c242a7f064ab71e63c7fa.webp)

Next, enter the following command in the terminal inside your **Price Tracking Project**:

```
apify login
```

Select `Enter API Token Manually` , paste the token you copied from your account and hit enter.

![apify-login](data:image/webp;base64,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)

You’ll see a confirmation that you’re now logged into your Apify account. When you run the code, the API token will be automatically inferred from your account, allowing you to use the **Send Email Actor**.

If you encountered any issues, double-check that your code matches the one below:

```
from apify import Actor
from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext


async def main() -> None:

    # Enter the context of the Actor.
    async with Actor:
        # Create a crawler.
        crawler = BeautifulSoupCrawler(
            # Limit the crawl to max requests. Remove or increase it for crawling all links.
            max_requests_per_crawl=50,
        )

        # Define a request handler, which will be called for every request.
        @crawler.router.default_handler
        async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
            url = context.request.url
            Actor.log.info(f'Scraping {url}...')
            
            # Select the product name and price elements.
            product_name_element = context.soup.find('div', class_='productname')
            product_price_element = context.soup.find('span', id='product-price-395001')

            # Extract the desired data.
            data = {
                'url': context.request.url,
                'product_name': product_name_element.text.strip() if product_name_element else None,
                'price': float(product_price_element['data-price-amount']) if product_price_element else None,
            }
            
            price_threshold = 80
            
            if data['price'] < price_threshold:
                actor_run = await Actor.start(
                    actor_id="apify/send-mail",
                    run_input={
                        "to": "your_email@gmail.com",
                        "subject": "Python Price Alert",
                        "text": f"The price of '{data['product_name']}' has dropped below ${price_threshold} and is now ${data['price']}.\n\nCheck it out here: {data['url']}",
                    },
                )
                Actor.log.info(f"Email sent with run ID: {actor_run.id}")

            # Store the extracted data to the default dataset.
            await context.push_data(data)

        # Run the crawler with the starting requests.
        await crawler.run(['https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html'])
```

> 🔖 Replace the placeholder email address with your actual email, the one where you want to receive notifications. Make sure it matches the email you used to register your **Apify account**.

Then, run the code using:

```
apify run --purge
```

If everything works correctly, you should receive an email like the one below in your inbox.

![price-alert](/assets/images/price-alet-530cccd85b681fd98e32a81e4f52e488.webp)

## 4. Deploying your Actor[​](#4-deploying-your-actor "Direct link to 4. Deploying your Actor")

It’s time to deploy your Actor to the cloud, allowing it to take full advantage of the Apify Platform’s features.

Fortunately, this process is incredibly simple. Since you’re already logged into your account, just run the following command:

```
apify push
```

In just a few seconds, you’ll find your newly created Actor in your Apify account by navigating to **Actors → Development → Price Tracking Actor**.

![price-tracking-actor](/assets/images/price-tracking-actor-c91e4f5243ea20363d2621424d89985f.webp)

Note that the **Start URLs** input has been reset to **apify.com**, so be sure to replace it with our target website:

<https://www.centralcomputer.com/raspberry-pi-5-8gb-ram-board.html>

Once updated, click the green ***Save & Start*** button at the bottom of the page to run your Actor.

After the run completes, you’ll see a **preview of the results** in the ***Output*** tab. You can also export your data in multiple formats from the ***Storage*** tab.

![actor-run](/assets/images/actor-run-faa6f7deb56846b88c7d446e9eb05e1d.webp)

**Export dataset:**

![actor-export-dataset](/assets/images/export-dataset-9d56cd86006ff21fbbd695a72cd5529c.webp)

## 5. Schedule your runs[​](#5-schedule-your-runs "Direct link to 5. Schedule your runs")

Now, a **price monitoring script** wouldn’t be very effective unless it ran on a schedule, automatically checking the product’s price and notifying us when it drops below the threshold.

Since our Actor is already deployed on **Apify**, scheduling it to run, say, every hour, is incredibly simple.

On your Actor page, click the three dots in the top-right corner of the screen and select **“Schedule Actor.”**

![schedule-run](/assets/images/schedule-run-3c2c1975cb23d5f4bdbe8116172a2a47.webp)

Next, choose how often you want your Actor to run, and that’s it! Your script will now run in the cloud, continuously monitoring the product’s price and sending you an email notification whenever it goes on sale.

![actor-schedule](/assets/images/actor-schedule-2fe3df75d91fa3270776f814ed6888dc.webp)

## That’s a wrap\![​](#thats-a-wrap "Direct link to That’s a wrap!")

Congratulations on completing this tutorial! I hope you enjoyed getting your feet wet with Crawlee and feel confident enough to tweak the code to build your own price tracker.

We’ve only scratched the surface of what Apify and Crawlee can do. As a next step, join our [Discord community](https://discord.com/invite/jyEM2PRvMU) to connect with other web scraping developers and stay up to date with the latest news about Crawlee and Apify!
