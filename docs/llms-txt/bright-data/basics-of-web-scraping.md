# Source: https://docs.brightdata.com/datasets/scraper-studio/basics-of-web-scraping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Basics of Web Scraping

> This article describes the basic concepts in web scraping, like Navigation, Parsing, Worker type, and main Challenges

If you're familiar with JavaScript but new to web data scraping, understanding the basic approach and key tactics will set you up for success.

**Core Concepts**

Web scraping consists of two main parts:

1. **Navigation** - Moving through websites to reach target data
2. **Parsing** - Extracting and structuring the data

The tactics you use depend on your chosen technical approach: Browser worker or Code worker.

## Browser Worker vs. Code Worker

Browser worker and code worker are two technical approaches for scraping, and you should choose between them based on your needs and technical challenges you’re facing with the website you’re scraping.

**Browser Workers** simulates user interactions with websites through a headless browser, capable of handling complex scraping tasks such as user input and dynamic content loading.

**Code Workers**, on the other hand, run on the server-side and perform scraping tasks through HTTP requests. A script or program sends requests to the target website, extracts data from the individual responses, and saves it to a file or database. Running your code with a code workers can bring faster results.

**Switching Between Workers**

You can switch between worker types per scraper at any time, so you're never committed to a specific worker. However, be aware that some functions (like 'wait') are designed for and limited to Browser Workers only. Lean more about [worker types](/datasets/functions/worker-types)

## Interaction and Parsing

Interaction and parsing are two key steps in web scraping. Together, they let you navigate a website, load the relevant content, and extract structured data from it.

**Interaction** is the process of navigating through a website to reach the pages or sections that contain the data you want to collect. This can include:

* Sending **GET** or **POST** requests
* Following links and handling pagination
* Submitting forms
* Performing browser actions such as **click**, **type**, and **wait**

Once the page contains the data you need, call `parse()` to extract it. This triggers the **Parser code**, which reads the page content (HTML/JSON) and returns the extracted fields.

After parsing, call `collect()` to add the extracted record to your final dataset.

For example:

```js  theme={null}
let data = parse();
collect({
    url: new URL(location.href),
    title: data.title,
    links: data.links,
});
```

Parsing refers to the process of extracting the relevant data from the HTML content of a website. This involves identifying the HTML elements that contain the data you want to scrape, and using regular expressions or other techniques to extract the data from those elements.

For example:

```js  theme={null}
return {
  title: $('h1').text().trim(),
  links: $('a').toArray().map(e=>new URL($(e).attr('href'))),
};
```

For instance, let’s say that you would like to scrape an e-commerce website based on a search term, and return the (title, description, price) for each product.

```js  theme={null}
let search_url = `https`:
navigate(search_url)
let max_page = parse().max_page
for (let i = 1; i <= max_page; i++)
{
    let search_page = new URL(search_url)
     if (i>1)
          search_page.searchParams.set('page', i)
     next_stage({search_page})
}
```

```js  theme={null}
navigate(input.search_page)
let listings = parse().listings
for (let listing_url of listings)
     next_stage({listing_url})
```

```scss  theme={null}
navigate(input.listing_url)
collect(parse())
```

1. Navigate to the search page of the ecommerce website
2. Locate the HTML elements that contain the number of pages
3. Parse the HTML to extract the number of search results pages
4. Call `next_stage({ search_page })` to queue the next stage with that page’s URL as input.
5. Navigate to each result page
6. Locate the HTML elements that contain each search result data
7. Parse the HTML content of each search results to collect all listing URLs found on that page
8. Navigate to each product/listing page
9. Locate the HTML elements that contain the desired product data
10. Parse the HTML to extract the desired product data

## The challenges and barriers of scraping at scale

Scraping can be fast and easy when done on a small scale, but when your project requires a high-volume data collection, you may encounter several challenges. Many websites implement technical measures such as CAPTCHAs or IP blocking to prevent scraping.

While there are ways to overcome those challenges, doing it yourself might be complex and time consuming. To solve this, we've built our IDE cloud service on top of our proprietary [proxy infrastructure](/proxy-networks/introduction) and [Unlocker API](/scraping-automation/web-unlocker), so you won't have to face these challenges.
