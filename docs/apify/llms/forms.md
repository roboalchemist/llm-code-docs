# Source: https://docs.apify.com/sdk/js/docs/examples/forms.md

# Forms

Copy for LLM

This example demonstrates how to use [`PuppeteerCrawler`](https://crawlee.dev/api/puppeteer-crawler/class/PuppeteerCrawler) to automatically fill and submit a search form to look up repositories on [GitHub](https://github.com) using headless Chrome / Puppeteer. The actor first fills in the search term, repository owner, start date and language of the repository, then submits the form and prints out the results. Finally, the results are saved either on the Apify platform to the default [`dataset`](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) or on the local machine as JSON files in `./storage/datasets/default`.

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IGxhdW5jaFB1cHBldGVlciB9IGZyb20gJ2NyYXdsZWUnO1xcblxcbmF3YWl0IEFjdG9yLmluaXQoKTtcXG5cXG4vLyBMYXVuY2ggdGhlIHdlYiBicm93c2VyLlxcbmNvbnN0IGJyb3dzZXIgPSBhd2FpdCBsYXVuY2hQdXBwZXRlZXIoKTtcXG5cXG4vLyBDcmVhdGUgYW5kIG5hdmlnYXRlIG5ldyBwYWdlXFxuY29uc29sZS5sb2coJ09wZW4gdGFyZ2V0IHBhZ2UnKTtcXG5jb25zdCBwYWdlID0gYXdhaXQgYnJvd3Nlci5uZXdQYWdlKCk7XFxuYXdhaXQgcGFnZS5nb3RvKCdodHRwczovL2dpdGh1Yi5jb20vc2VhcmNoL2FkdmFuY2VkJyk7XFxuXFxuLy8gRmlsbCBmb3JtIGZpZWxkcyBhbmQgc2VsZWN0IGRlc2lyZWQgc2VhcmNoIG9wdGlvbnNcXG5jb25zb2xlLmxvZygnRmlsbCBpbiBzZWFyY2ggZm9ybScpO1xcbmF3YWl0IHBhZ2UudHlwZSgnI2Fkdl9jb2RlX3NlYXJjaCBpbnB1dC5qcy1hZHZhbmNlZC1zZWFyY2gtaW5wdXQnLCAnYXBpZnktanMnKTtcXG5hd2FpdCBwYWdlLnR5cGUoJyNzZWFyY2hfZnJvbScsICdhcGlmeScpO1xcbmF3YWl0IHBhZ2UudHlwZSgnI3NlYXJjaF9kYXRlJywgJz4yMDE1Jyk7XFxuYXdhaXQgcGFnZS5zZWxlY3QoJ3NlbGVjdCNzZWFyY2hfbGFuZ3VhZ2UnLCAnSmF2YVNjcmlwdCcpO1xcblxcbi8vIFN1Ym1pdCB0aGUgZm9ybSBhbmQgd2FpdCBmb3IgZnVsbCBsb2FkIG9mIG5leHQgcGFnZVxcbmNvbnNvbGUubG9nKCdTdWJtaXQgc2VhcmNoIGZvcm0nKTtcXG5hd2FpdCBQcm9taXNlLmFsbChbXFxuICAgIHBhZ2Uud2FpdEZvck5hdmlnYXRpb24oKSxcXG4gICAgcGFnZS5jbGljaygnI2Fkdl9jb2RlX3NlYXJjaCBidXR0b25bdHlwZT1cXFwic3VibWl0XFxcIl0nKSxcXG5dKTtcXG5cXG4vLyBPYnRhaW4gYW5kIHByaW50IGxpc3Qgb2Ygc2VhcmNoIHJlc3VsdHNcXG5jb25zdCByZXN1bHRzID0gYXdhaXQgcGFnZS4kJGV2YWwoJ2Rpdi5mNC50ZXh0LW5vcm1hbCBhJywgKG5vZGVzKSA9PlxcbiAgICBub2Rlcy5tYXAoKG5vZGUpID0-ICh7XFxuICAgICAgICB1cmw6IG5vZGUuaHJlZixcXG4gICAgICAgIG5hbWU6IG5vZGUuaW5uZXJUZXh0LFxcbiAgICB9KSksXFxuKTtcXG5cXG5jb25zb2xlLmxvZygnUmVzdWx0czonLCByZXN1bHRzKTtcXG5cXG4vLyBTdG9yZSBkYXRhIGluIGRlZmF1bHQgZGF0YXNldFxcbmF3YWl0IEFjdG9yLnB1c2hEYXRhKHJlc3VsdHMpO1xcblxcbi8vIENsb3NlIGJyb3dzZXJcXG5hd2FpdCBicm93c2VyLmNsb3NlKCk7XFxuXFxuYXdhaXQgQWN0b3IuZXhpdCgpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.50kP3gcHDUJWt6VevBrpm1zXyG6s5l7JYuSd2JiWhVg\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { launchPuppeteer } from 'crawlee';

await Actor.init();

// Launch the web browser.
const browser = await launchPuppeteer();

// Create and navigate new page
console.log('Open target page');
const page = await browser.newPage();
await page.goto('https://github.com/search/advanced');

// Fill form fields and select desired search options
console.log('Fill in search form');
await page.type('#adv_code_search input.js-advanced-search-input', 'apify-js');
await page.type('#search_from', 'apify');
await page.type('#search_date', '>2015');
await page.select('select#search_language', 'JavaScript');

// Submit the form and wait for full load of next page
console.log('Submit search form');
await Promise.all([
    page.waitForNavigation(),
    page.click('#adv_code_search button[type="submit"]'),
]);

// Obtain and print list of search results
const results = await page.$$eval('div.f4.text-normal a', (nodes) =>
    nodes.map((node) => ({
        url: node.href,
        name: node.innerText,
    })),
);

console.log('Results:', results);

// Store data in default dataset
await Actor.pushData(results);

// Close browser
await browser.close();

await Actor.exit();
```
