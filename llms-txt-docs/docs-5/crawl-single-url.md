# Source: https://docs.apify.com/sdk/js/docs/examples/crawl-single-url.md

# Crawl a single URL

Copy for LLM

This example uses the [`got-scraping`](https://github.com/apify/got-scraping) npm package to grab the HTML of a web page.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IGdvdFNjcmFwaW5nIH0gZnJvbSAnZ290LXNjcmFwaW5nJztcXG5cXG4vLyBHZXQgdGhlIEhUTUwgb2YgYSB3ZWIgcGFnZVxcbmNvbnN0IHsgYm9keSB9ID0gYXdhaXQgZ290U2NyYXBpbmcoeyB1cmw6ICdodHRwczovL3d3dy5leGFtcGxlLmNvbScgfSk7XFxuY29uc29sZS5sb2coYm9keSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.0S1i1yD10_82mLCH3VWFtCZTU4-BDrDU1UGY208IqgE\&asrc=run_on_apify)

```
import { gotScraping } from 'got-scraping';

// Get the HTML of a web page
const { body } = await gotScraping({ url: 'https://www.example.com' });
console.log(body);
```

If you don't want to hard-code the URL into the script, refer to the [Accept User Input](https://docs.apify.com/sdk/js/sdk/js/docs/examples/accept-user-input.md) example.
