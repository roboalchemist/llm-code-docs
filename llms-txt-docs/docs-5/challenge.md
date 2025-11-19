# Source: https://docs.apify.com/academy/web-scraping-for-beginners/challenge.md

# Challenge

**Test your knowledge acquired in the previous sections of this course by building an Amazon scraper using Crawlee's CheerioCrawler!**

***

Before moving onto the other courses in the academy, we recommend following along with this section, as it combines everything you've learned in the previous lessons into one cohesive project that helps you prove to yourself that you've thoroughly understood the material.

We recommend that you make sure you've gone through both the https://docs.apify.com/academy/web-scraping-for-beginners/data-extraction.md and https://docs.apify.com/academy/web-scraping-for-beginners/crawling.md sections of this course to ensure the smoothest development process.

## Learning 🧠

Before continuing, it is highly recommended to do the following:

* Look over https://crawlee.dev/docs/introduction/first-crawler and ideally **code along**.
* Read https://docs.apify.com/academy/node-js/request-labels-in-apify-actors about https://crawlee.dev/api/core/class/Request#label (this will be extremely useful later on).
* Check out https://docs.apify.com/academy/node-js/dealing-with-dynamic-pages.md about dynamic pages.
* Read about the https://crawlee.dev/api/core/class/RequestQueue.

## Our task

On Amazon, we can use this link to get to the results page of any product we want:


```
https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=KEYWORD
```


Our crawler's input will look like this:


```
{
    "keyword": "iphone"
}
```


The goal at hand is to scrape all of the products from the first page of results for whatever keyword was provided (for our test case, it will be **iPhone**), then to scrape all available offers of each product and push the results to the dataset. For context, the offers for a product look like this:

![Amazon product offers](/assets/images/product-offers-20910dbac0f5cc3df6089143b924ac5b.jpg)

In the end, we'd like our final output to look something like this:


```
[
    {
        "title": "Apple iPhone 6 a1549 16GB Space Gray Unlocked (Certified Refurbished)",
        "asin": "B07P6Y7954",
        "itemUrl": "https://www.amazon.com/Apple-iPhone-Unlocked-Certified-Refurbished/dp/B00YD547Q6/ref=sr_1_2?s=wireless&ie=UTF8&qid=1539772626&sr=1-2&keywords=iphone",
        "description": "What's in the box: Certified Refurbished iPhone 6 Space Gray 16GB Unlocked , USB Cable/Adapter. Comes in a Generic Box with a 1 Year Limited Warranty.",
        "keyword": "iphone",
        "sellerName": "Blutek Intl",
        "offer": "$162.97"
    },
    {
        "title": "Apple iPhone 6 a1549 16GB Space Gray Unlocked (Certified Refurbished)",
        "asin": "B07P6Y7954",
        "itemUrl": "https://www.amazon.com/Apple-iPhone-Unlocked-Certified-Refurbished/dp/B00YD547Q6/ref=sr_1_2?s=wireless&ie=UTF8&qid=1539772626&sr=1-2&keywords=iphone",
        "description": "What's in the box: Certified Refurbished iPhone 6 Space Gray 16GB Unlocked , USB Cable/Adapter. Comes in a Generic Box with a 1 Year Limited Warranty.",
        "keyword": "iphone",
        "sellerName": "PLATINUM DEALS",
        "offer": "$169.98"
    },
    {
        "...": "..."
    }
]
```


> The `asin` is the ID of the product, which is data present on the Amazon website.

Each of the items in the dataset will represent a scraped offer and will have the same `title`, `asin`, `itemUrl`, and `description`. The offer-specific fields will be `sellerName` and `offer`.

## First up

From this course, you should have all the knowledge to build this scraper by yourself. Give it a try, then come back to compare your scraper with our solution.

The challenge can be completed using either https://crawlee.dev/api/cheerio-crawler/class/CheerioCrawler or https://crawlee.dev/api/playwright-crawler/class/PlaywrightCrawler. Playwright is significantly slower but doesn't get blocked as much. You will learn the most by implementing both.

Let's start off this section by https://docs.apify.com/academy/web-scraping-for-beginners/challenge/initializing-and-setting-up.md our project with the Crawlee CLI (don't worry, no additional installation is required).
