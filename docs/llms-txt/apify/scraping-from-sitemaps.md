# Source: https://docs.apify.com/academy/node-js/scraping-from-sitemaps.md

# How to scrape from sitemaps

Processing sitemaps automatically with Crawlee

Crawlee allows you to scrape sitemaps with ease. If you are using Crawlee, you can skip the following steps and just gather all the URLs from the sitemap in a few lines of code.


```
import { RobotsFile } from 'crawlee';

const robots = await RobotsFile.find('https://www.mysite.com');

const allWebsiteUrls = await robots.parseUrlsFromSitemaps();
```


**The sitemap.xml file is a jackpot for every web scraper developer. Take advantage of this and learn an easier way to extract data from websites using Crawlee.**

***

Let's say we want to scrape a database of craft beers ([brewbound.com](https://www.brewbound.com/)) before summer starts. If we are lucky, the website will contain a sitemap at [brewbound.com/sitemap.xml](https://www.brewbound.com/sitemap.xml).

> Check out [Sitemap Sniffer](https://apify.com/vaclavrut/sitemap-sniffer), which can discover sitemaps in hidden locations!

## Analyzing the sitemap

The sitemap is usually located at the path **/sitemap.xml**. It is always worth trying that URL, as it is rarely linked anywhere on the site. It usually contains a list of all pages in [XML format](https://en.wikipedia.org/wiki/XML).


```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://www.brewbound.com/advertise</loc>
        <lastmod>2015-03-19</lastmod>
        <changefreq>daily</changefreq>
    </url>
    <url>
    ...
```


The URLs of breweries take this form:


```
http://www.brewbound.com/breweries/[BREWERY_NAME]
```


And the URLs of craft beers look like this:


```
http://www.brewbound.com/breweries/[BREWERY_NAME]/[BEER_NAME]
```


They can be matched using the following regular expression:


```
http(s)?:\/\/www\.brewbound\.com\/breweries\/[^\/]+\/[^\/<]+
```


Note the two parts of the regular expression `[^\/<]` containing the `<` symbol. This is because we want to exclude the `</loc>` tag, which closes each URL.

## Scraping the sitemap in Crawlee

If you're scraping sitemaps (or anything else, really), [Crawlee](https://crawlee.dev) is perfect for the job.

First, let's add the beer URLs from the sitemap to the [RequestList](https://crawlee.dev/api/core/class/RequestList) using our regular expression to match only the (craft!!) beer URLs and not pages of breweries, contact page, etc.


```
const requestList = await RequestList.open(null, [{
    requestsFromUrl: 'https://www.brewbound.com/sitemap.xml',
    regex: /http(s)?:\/\/www\.brewbound\.com\/breweries\/[^/<]+\/[^/<]+/gm,
}]);
```


Now, let's use [PuppeteerCrawler](https://crawlee.dev/api/puppeteer-crawler/class/PuppeteerCrawler) to scrape the created `RequestList` with [Puppeteer](https://pptr.dev/) and push it to the final dataset.


```
const crawler = new PuppeteerCrawler({
    requestList,
    async requestHandler({ page }) {
        const beerPage = await page.evaluate(() => {
            return document.getElementsByClassName('productreviews').length;
        });
        if (!beerPage) return;

        const data = await page.evaluate(() => {
            const title = document.getElementsByTagName('h1')[0].innerText;
            const [brewery, beer] = title.split(':');
            const description = document.getElementsByClassName('productreviews')[0].innerText;

            return { brewery, beer, description };
        });

        await Dataset.pushData(data);
    },
});
```


## Full code

If we create a new Actor using the code below on the [Apify platform](https://docs.apify.com/academy/apify-platform.md), it returns a nicely formatted spreadsheet containing a list of breweries with their beers with descriptions.

Make sure to use the **apify/actor-node-puppeteer-chrome** image for your Dockerfile, otherwise the run will fail.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQsIFB1cHBldGVlckNyYXdsZXIsIFJlcXVlc3RMaXN0IH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgcmVxdWVzdExpc3QgPSBhd2FpdCBSZXF1ZXN0TGlzdC5vcGVuKG51bGwsIFt7XFxuICAgIHJlcXVlc3RzRnJvbVVybDogJ2h0dHBzOi8vd3d3LmJyZXdib3VuZC5jb20vc2l0ZW1hcC54bWwnLFxcbiAgICByZWdleDogL2h0dHAocyk_OlxcXFwvXFxcXC93d3dcXFxcLmJyZXdib3VuZFxcXFwuY29tXFxcXC9icmV3ZXJpZXNcXFxcL1teLzxdK1xcXFwvW14vPF0rL2dtLFxcbn1dKTtcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICByZXF1ZXN0TGlzdCxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyBwYWdlIH0pIHtcXG4gICAgICAgIGNvbnN0IGJlZXJQYWdlID0gYXdhaXQgcGFnZS5ldmFsdWF0ZSgoKSA9PiB7XFxuICAgICAgICAgICAgcmV0dXJuIGRvY3VtZW50LmdldEVsZW1lbnRzQnlDbGFzc05hbWUoJ3Byb2R1Y3RyZXZpZXdzJykubGVuZ3RoO1xcbiAgICAgICAgfSk7XFxuICAgICAgICBpZiAoIWJlZXJQYWdlKSByZXR1cm47XFxuXFxuICAgICAgICBjb25zdCBkYXRhID0gYXdhaXQgcGFnZS5ldmFsdWF0ZSgoKSA9PiB7XFxuICAgICAgICAgICAgY29uc3QgdGl0bGUgPSBkb2N1bWVudC5nZXRFbGVtZW50c0J5VGFnTmFtZSgnaDEnKVswXS5pbm5lclRleHQ7XFxuICAgICAgICAgICAgY29uc3QgW2JyZXdlcnksIGJlZXJdID0gdGl0bGUuc3BsaXQoJzonKTtcXG4gICAgICAgICAgICBjb25zdCBkZXNjcmlwdGlvbiA9IGRvY3VtZW50LmdldEVsZW1lbnRzQnlDbGFzc05hbWUoJ3Byb2R1Y3RyZXZpZXdzJylbMF0uaW5uZXJUZXh0O1xcblxcbiAgICAgICAgICAgIHJldHVybiB7IGJyZXdlcnksIGJlZXIsIGRlc2NyaXB0aW9uIH07XFxuICAgICAgICB9KTtcXG5cXG4gICAgICAgIGF3YWl0IERhdGFzZXQucHVzaERhdGEoZGF0YSk7XFxuICAgIH0sXFxufSk7XFxuXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.KFqjQiNxNkx_HPnvJ4H_W0e58W3L7D_Ga9pq_ZQ7tqI&asrc=run_on_apify)


```
import { Dataset, PuppeteerCrawler, RequestList } from 'crawlee';

const requestList = await RequestList.open(null, [{
    requestsFromUrl: 'https://www.brewbound.com/sitemap.xml',
    regex: /http(s)?:\/\/www\.brewbound\.com\/breweries\/[^/<]+\/[^/<]+/gm,
}]);

const crawler = new PuppeteerCrawler({
    requestList,
    async requestHandler({ page }) {
        const beerPage = await page.evaluate(() => {
            return document.getElementsByClassName('productreviews').length;
        });
        if (!beerPage) return;

        const data = await page.evaluate(() => {
            const title = document.getElementsByTagName('h1')[0].innerText;
            const [brewery, beer] = title.split(':');
            const description = document.getElementsByClassName('productreviews')[0].innerText;

            return { brewery, beer, description };
        });

        await Dataset.pushData(data);
    },
});

await crawler.run();
```
