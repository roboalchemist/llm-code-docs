# Source: https://crawlee.dev/js/docs/examples/forms.md

# Fill and Submit a Form using Puppeteer

Copy for LLM

This example demonstrates how to use [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) to automatically fill and submit a search form to look up repositories on [GitHub](https://github.com) using headless Chrome / Puppeteer. The crawler first fills in the search term, repository owner, start date and language of the repository, then submits the form and prints out the results. Finally, the results are saved either on the Apify platform to the default [`dataset`](https://crawlee.dev/js/api/core/class/Dataset.md) or on the local machine as JSON files in `./storage/datasets/default`.

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQsIGxhdW5jaFB1cHBldGVlciB9IGZyb20gJ2NyYXdsZWUnO1xcblxcbi8vIExhdW5jaCB0aGUgd2ViIGJyb3dzZXIuXFxuY29uc3QgYnJvd3NlciA9IGF3YWl0IGxhdW5jaFB1cHBldGVlcigpO1xcblxcbi8vIENyZWF0ZSBhbmQgbmF2aWdhdGUgbmV3IHBhZ2VcXG5jb25zb2xlLmxvZygnT3BlbiB0YXJnZXQgcGFnZScpO1xcbmNvbnN0IHBhZ2UgPSBhd2FpdCBicm93c2VyLm5ld1BhZ2UoKTtcXG5hd2FpdCBwYWdlLmdvdG8oJ2h0dHBzOi8vZ2l0aHViLmNvbS9zZWFyY2gvYWR2YW5jZWQnKTtcXG5cXG4vLyBGaWxsIGZvcm0gZmllbGRzIGFuZCBzZWxlY3QgZGVzaXJlZCBzZWFyY2ggb3B0aW9uc1xcbmNvbnNvbGUubG9nKCdGaWxsIGluIHNlYXJjaCBmb3JtJyk7XFxuYXdhaXQgcGFnZS50eXBlKCcjYWR2X2NvZGVfc2VhcmNoIGlucHV0LmpzLWFkdmFuY2VkLXNlYXJjaC1pbnB1dCcsICdhcGlmeS1qcycpO1xcbmF3YWl0IHBhZ2UudHlwZSgnI3NlYXJjaF9mcm9tJywgJ2FwaWZ5Jyk7XFxuYXdhaXQgcGFnZS50eXBlKCcjc2VhcmNoX2RhdGUnLCAnPjIwMTUnKTtcXG5hd2FpdCBwYWdlLnNlbGVjdCgnc2VsZWN0I3NlYXJjaF9sYW5ndWFnZScsICdKYXZhU2NyaXB0Jyk7XFxuXFxuLy8gU3VibWl0IHRoZSBmb3JtIGFuZCB3YWl0IGZvciBmdWxsIGxvYWQgb2YgbmV4dCBwYWdlXFxuY29uc29sZS5sb2coJ1N1Ym1pdCBzZWFyY2ggZm9ybScpO1xcbmF3YWl0IFByb21pc2UuYWxsKFtcXG4gICAgcGFnZS53YWl0Rm9yTmF2aWdhdGlvbih7IHdhaXRVbnRpbDogJ25ldHdvcmtpZGxlMicgfSksXFxuICAgIHBhZ2UuY2xpY2soJyNhZHZfY29kZV9zZWFyY2ggYnV0dG9uW3R5cGU9XFxcInN1Ym1pdFxcXCJdJyksXFxuXSk7XFxuXFxuLy8gT2J0YWluIGFuZCBwcmludCBsaXN0IG9mIHNlYXJjaCByZXN1bHRzXFxuY29uc3QgcmVzdWx0cyA9IGF3YWl0IHBhZ2UuJCRldmFsKCdbZGF0YS10ZXN0aWQ9XFxcInJlc3VsdHMtbGlzdFxcXCJdIGRpdi5zZWFyY2gtdGl0bGUgPiBhJywgKG5vZGVzKSA9PlxcbiAgICBub2Rlcy5tYXAoKG5vZGUpID0-ICh7XFxuICAgICAgICB1cmw6IG5vZGUuaHJlZixcXG4gICAgICAgIG5hbWU6IG5vZGUuaW5uZXJUZXh0LFxcbiAgICB9KSksXFxuKTtcXG5cXG5jb25zb2xlLmxvZygnUmVzdWx0czonLCByZXN1bHRzKTtcXG5cXG4vLyBTdG9yZSBkYXRhIGluIGRlZmF1bHQgZGF0YXNldFxcbmF3YWl0IERhdGFzZXQucHVzaERhdGEocmVzdWx0cyk7XFxuXFxuLy8gQ2xvc2UgYnJvd3NlclxcbmF3YWl0IGJyb3dzZXIuY2xvc2UoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.AQF16S0-_uJ55mZ5XgWHl5zj4KbRk-NJAuFJL7sL9VY\&asrc=run_on_apify)

```
import { Dataset, launchPuppeteer } from 'crawlee';

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
    page.waitForNavigation({ waitUntil: 'networkidle2' }),
    page.click('#adv_code_search button[type="submit"]'),
]);

// Obtain and print list of search results
const results = await page.$$eval('[data-testid="results-list"] div.search-title > a', (nodes) =>
    nodes.map((node) => ({
        url: node.href,
        name: node.innerText,
    })),
);

console.log('Results:', results);

// Store data in default dataset
await Dataset.pushData(results);

// Close browser
await browser.close();
```
