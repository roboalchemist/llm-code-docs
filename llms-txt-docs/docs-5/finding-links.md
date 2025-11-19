# Source: https://docs.apify.com/academy/web-scraping-for-beginners/crawling/finding-links.md

# Finding links

**Learn what a link looks like in HTML and how to find and extract their URLs when web scraping using both DevTools and Node.js.**

***

Many kinds of links exist on the internet, and we'll cover all the types in the advanced Academy courses. For now, let's think of links as https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a with `<a>` tags. A typical link looks like this:


```
<a href="https://example.com">This is a link to example.com</a>
```


On a webpage, the link above will look like this: https://example.com When you click it, your browser will navigate to the URL in the `<a>` tag's `href` attribute (`https://example.com`).

> `href` means **H**ypertext **REF**erence. You don't need to remember this - just know that `href` typically means some sort of link.

## Extracting links 🔗

If a link is an HTML element, and the URL is an attribute, this means that we can extract links the same way as we extracted data. To test this theory in the browser, we can try running the following code in our DevTools console on any website.


```
// Select all the <a> elements.
const links = document.querySelectorAll('a');
// For each of the links...
for (const link of links) {
    // get the value of its 'href' attribute...
    const url = link.href;
    // and print it to console.
    console.log(url);
}
```


Go to the https://warehouse-theme-metal.myshopify.com/collections/sales, open the DevTools Console, paste the above code and run it.

![links extracted from Warehouse store](/assets/images/warehouse-links-37f7c3164546c93f7b75ca83cf6e0773.png)

***Boom*** 💥, all the links from the page have now been printed to the console. Most of the links point to other parts of the website, but some links lead to other domains like facebook.com or instagram.com.

## Extracting link URLs in Node.js

DevTools Console is a fun playground, but Node.js is way more useful. Let's create a new file in our project called **crawler.js** and add some basic crawling code that prints all the links from the https://warehouse-theme-metal.myshopify.com/collections/sales.

We'll start from a boilerplate that's very similar to the scraper we built in https://docs.apify.com/academy/web-scraping-for-beginners/data-extraction/node-js-scraper.md.

https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCAqIGFzIGNoZWVyaW8gZnJvbSAnY2hlZXJpbyc7XFxuaW1wb3J0IHsgZ290U2NyYXBpbmcgfSBmcm9tICdnb3Qtc2NyYXBpbmcnO1xcblxcbmNvbnN0IHN0b3JlVXJsID0gJ2h0dHBzOi8vd2FyZWhvdXNlLXRoZW1lLW1ldGFsLm15c2hvcGlmeS5jb20vY29sbGVjdGlvbnMvc2FsZXMnO1xcblxcbmNvbnN0IHJlc3BvbnNlID0gYXdhaXQgZ290U2NyYXBpbmcoc3RvcmVVcmwpO1xcbmNvbnN0IGh0bWwgPSByZXNwb25zZS5ib2R5O1xcblxcbmNvbnN0ICQgPSBjaGVlcmlvLmxvYWQoaHRtbCk7XFxuXFxuLy8gLS0tLS0tLSBuZXcgY29kZSBiZWxvd1xcblxcbmNvbnN0IGxpbmtzID0gJCgnYScpO1xcblxcbmZvciAoY29uc3QgbGluayBvZiBsaW5rcykge1xcbiAgICBjb25zdCB1cmwgPSAkKGxpbmspLmF0dHIoJ2hyZWYnKTtcXG4gICAgY29uc29sZS5sb2codXJsKTtcXG59XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.28PdE3s27h6nCqUFLj6UYLwH9RJRqGQBH5KqnfjfBGw&asrc=run_on_apify


```
import * as cheerio from 'cheerio';
import { gotScraping } from 'got-scraping';

const storeUrl = 'https://warehouse-theme-metal.myshopify.com/collections/sales';

const response = await gotScraping(storeUrl);
const html = response.body;

const $ = cheerio.load(html);

// ------- new code below

const links = $('a');

for (const link of links) {
    const url = $(link).attr('href');
    console.log(url);
}
```


Aside from importing libraries and downloading HTML, we load the HTML into Cheerio and then use it to retrieve all the `<a>` elements. After that, we iterate over the collected links and print their `href` attributes, which we access using the https://cheerio.js.org/docs/api/classes/Cheerio#attr method.

When you run the above code, you'll see quite a lot of links in the terminal. Some of them may look wrong, because they don't start with the regular `https://` protocol. We'll learn what to do with them in the following lessons.

## Next Up

The https://docs.apify.com/academy/web-scraping-for-beginners/crawling/filtering-links.md will teach you how to select and filter links, so that your crawler will always work only with valid and useful URLs.
