# Source: https://crawlee.dev/js/docs/examples/add-data-to-dataset.md

# Add data to dataset

Copy for LLM

This example saves data to the default dataset. If the dataset doesn't exist, it will be created. You can save data to custom datasets by using [`Dataset.open()`](https://crawlee.dev/js/api/core/class/Dataset.md#open)

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyBwdXNoRGF0YSwgcmVxdWVzdCwgYm9keSB9KSB7XFxuICAgICAgICAvLyBTYXZlIGRhdGEgdG8gZGVmYXVsdCBkYXRhc2V0XFxuICAgICAgICBhd2FpdCBwdXNoRGF0YSh7XFxuICAgICAgICAgICAgdXJsOiByZXF1ZXN0LnVybCxcXG4gICAgICAgICAgICBodG1sOiBib2R5LFxcbiAgICAgICAgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuYXdhaXQgY3Jhd2xlci5hZGRSZXF1ZXN0cyhbXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMScsXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMicsXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMycsXFxuXSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.y9kz_gyD0gZNJaNVFyYfICCT63Qx-6Kf2Lk6EddXLt4\&asrc=run_on_apify)

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    // Function called for each URL
    async requestHandler({ pushData, request, body }) {
        // Save data to default dataset
        await pushData({
            url: request.url,
            html: body,
        });
    },
});

await crawler.addRequests([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
    'http://www.example.com/page-3',
]);

// Run the crawler
await crawler.run();
```

Each item in this dataset will be saved to its own file in the following directory:

```
{PROJECT_FOLDER}/storage/datasets/default/
```
