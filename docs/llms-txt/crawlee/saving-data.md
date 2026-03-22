# Source: https://crawlee.dev/js/docs/introduction/saving-data.md

# Saving data

Copy for LLM

A data extraction job would not be complete without saving the data for later use and processing. You've come to the final and most difficult part of this tutorial so make sure to pay attention very carefully!

First, add a new import to the top of the file:

```
import { PlaywrightCrawler, Dataset } from 'crawlee';
```

Then, replace the `console.log(results)` call with:

```
await Dataset.pushData(results);
```

and that's it. Unlike earlier, we are being serious now. That's it, you're done. The final code looks like this:

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyLCBEYXRhc2V0IH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIHJlcXVlc3RIYW5kbGVyOiBhc3luYyAoeyBwYWdlLCByZXF1ZXN0LCBlbnF1ZXVlTGlua3MgfSkgPT4ge1xcbiAgICAgICAgY29uc29sZS5sb2coYFByb2Nlc3Npbmc6ICR7cmVxdWVzdC51cmx9YCk7XFxuICAgICAgICBpZiAocmVxdWVzdC5sYWJlbCA9PT0gJ0RFVEFJTCcpIHtcXG4gICAgICAgICAgICBjb25zdCB1cmxQYXJ0ID0gcmVxdWVzdC51cmwuc3BsaXQoJy8nKS5zbGljZSgtMSk7IC8vIFsnc2VubmhlaXNlci1ta2UtNDQwLXByb2Zlc3Npb25hbC1zdGVyZW8tc2hvdGd1bi1taWNyb3Bob25lLW1rZS00NDAnXVxcbiAgICAgICAgICAgIGNvbnN0IG1hbnVmYWN0dXJlciA9IHVybFBhcnRbMF0uc3BsaXQoJy0nKVswXTsgLy8gJ3Nlbm5oZWlzZXInXFxuXFxuICAgICAgICAgICAgY29uc3QgdGl0bGUgPSBhd2FpdCBwYWdlLmxvY2F0b3IoJy5wcm9kdWN0LW1ldGEgaDEnKS50ZXh0Q29udGVudCgpO1xcbiAgICAgICAgICAgIGNvbnN0IHNrdSA9IGF3YWl0IHBhZ2UubG9jYXRvcignc3Bhbi5wcm9kdWN0LW1ldGFfX3NrdS1udW1iZXInKS50ZXh0Q29udGVudCgpO1xcblxcbiAgICAgICAgICAgIGNvbnN0IHByaWNlRWxlbWVudCA9IHBhZ2VcXG4gICAgICAgICAgICAgICAgLmxvY2F0b3IoJ3NwYW4ucHJpY2UnKVxcbiAgICAgICAgICAgICAgICAuZmlsdGVyKHtcXG4gICAgICAgICAgICAgICAgICAgIGhhc1RleHQ6ICckJyxcXG4gICAgICAgICAgICAgICAgfSlcXG4gICAgICAgICAgICAgICAgLmZpcnN0KCk7XFxuXFxuICAgICAgICAgICAgY29uc3QgY3VycmVudFByaWNlU3RyaW5nID0gYXdhaXQgcHJpY2VFbGVtZW50LnRleHRDb250ZW50KCk7XFxuICAgICAgICAgICAgY29uc3QgcmF3UHJpY2UgPSBjdXJyZW50UHJpY2VTdHJpbmc_LnNwbGl0KCckJylbMV07XFxuICAgICAgICAgICAgY29uc3QgcHJpY2UgPSBOdW1iZXIocmF3UHJpY2U_LnJlcGxhY2VBbGwoJywnLCAnJykpO1xcblxcbiAgICAgICAgICAgIGNvbnN0IGluU3RvY2tFbGVtZW50ID0gcGFnZVxcbiAgICAgICAgICAgICAgICAubG9jYXRvcignc3Bhbi5wcm9kdWN0LWZvcm1fX2ludmVudG9yeScpXFxuICAgICAgICAgICAgICAgIC5maWx0ZXIoe1xcbiAgICAgICAgICAgICAgICAgICAgaGFzVGV4dDogJ0luIHN0b2NrJyxcXG4gICAgICAgICAgICAgICAgfSlcXG4gICAgICAgICAgICAgICAgLmZpcnN0KCk7XFxuXFxuICAgICAgICAgICAgY29uc3QgaW5TdG9jayA9IChhd2FpdCBpblN0b2NrRWxlbWVudC5jb3VudCgpKSA-IDA7XFxuXFxuICAgICAgICAgICAgY29uc3QgcmVzdWx0cyA9IHtcXG4gICAgICAgICAgICAgICAgdXJsOiByZXF1ZXN0LnVybCxcXG4gICAgICAgICAgICAgICAgbWFudWZhY3R1cmVyLFxcbiAgICAgICAgICAgICAgICB0aXRsZSxcXG4gICAgICAgICAgICAgICAgc2t1LFxcbiAgICAgICAgICAgICAgICBjdXJyZW50UHJpY2U6IHByaWNlLFxcbiAgICAgICAgICAgICAgICBhdmFpbGFibGVJblN0b2NrOiBpblN0b2NrLFxcbiAgICAgICAgICAgIH07XFxuXFxuICAgICAgICAgICAgLy8gaGlnaGxpZ2h0LW5leHQtbGluZVxcbiAgICAgICAgICAgIGF3YWl0IERhdGFzZXQucHVzaERhdGEocmVzdWx0cyk7XFxuICAgICAgICB9IGVsc2UgaWYgKHJlcXVlc3QubGFiZWwgPT09ICdDQVRFR09SWScpIHtcXG4gICAgICAgICAgICAvLyBXZSBhcmUgbm93IG9uIGEgY2F0ZWdvcnkgcGFnZS4gV2UgY2FuIHVzZSB0aGlzIHRvIHBhZ2luYXRlIHRocm91Z2ggYW5kIGVucXVldWUgYWxsIHByb2R1Y3RzLFxcbiAgICAgICAgICAgIC8vIGFzIHdlbGwgYXMgYW55IHN1YnNlcXVlbnQgcGFnZXMgd2UgZmluZFxcblxcbiAgICAgICAgICAgIGF3YWl0IHBhZ2Uud2FpdEZvclNlbGVjdG9yKCcucHJvZHVjdC1pdGVtID4gYScpO1xcbiAgICAgICAgICAgIGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgICAgIHNlbGVjdG9yOiAnLnByb2R1Y3QtaXRlbSA-IGEnLFxcbiAgICAgICAgICAgICAgICBsYWJlbDogJ0RFVEFJTCcsIC8vIDw9IG5vdGUgdGhlIGRpZmZlcmVudCBsYWJlbFxcbiAgICAgICAgICAgIH0pO1xcblxcbiAgICAgICAgICAgIC8vIE5vdyB3ZSBuZWVkIHRvIGZpbmQgdGhlIFxcXCJOZXh0XFxcIiBidXR0b24gYW5kIGVucXVldWUgdGhlIG5leHQgcGFnZSBvZiByZXN1bHRzIChpZiBpdCBleGlzdHMpXFxuICAgICAgICAgICAgY29uc3QgbmV4dEJ1dHRvbiA9IGF3YWl0IHBhZ2UuJCgnYS5wYWdpbmF0aW9uX19uZXh0Jyk7XFxuICAgICAgICAgICAgaWYgKG5leHRCdXR0b24pIHtcXG4gICAgICAgICAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICAgICAgICAgIHNlbGVjdG9yOiAnYS5wYWdpbmF0aW9uX19uZXh0JyxcXG4gICAgICAgICAgICAgICAgICAgIGxhYmVsOiAnQ0FURUdPUlknLCAvLyA8PSBub3RlIHRoZSBzYW1lIGxhYmVsXFxuICAgICAgICAgICAgICAgIH0pO1xcbiAgICAgICAgICAgIH1cXG4gICAgICAgIH0gZWxzZSB7XFxuICAgICAgICAgICAgLy8gVGhpcyBtZWFucyB3ZSdyZSBvbiB0aGUgc3RhcnQgcGFnZSwgd2l0aCBubyBsYWJlbC5cXG4gICAgICAgICAgICAvLyBPbiB0aGlzIHBhZ2UsIHdlIGp1c3Qgd2FudCB0byBlbnF1ZXVlIGFsbCB0aGUgY2F0ZWdvcnkgcGFnZXMuXFxuXFxuICAgICAgICAgICAgYXdhaXQgcGFnZS53YWl0Rm9yU2VsZWN0b3IoJy5jb2xsZWN0aW9uLWJsb2NrLWl0ZW0nKTtcXG4gICAgICAgICAgICBhd2FpdCBlbnF1ZXVlTGlua3Moe1xcbiAgICAgICAgICAgICAgICBzZWxlY3RvcjogJy5jb2xsZWN0aW9uLWJsb2NrLWl0ZW0nLFxcbiAgICAgICAgICAgICAgICBsYWJlbDogJ0NBVEVHT1JZJyxcXG4gICAgICAgICAgICB9KTtcXG4gICAgICAgIH1cXG4gICAgfSxcXG5cXG4gICAgLy8gTGV0J3MgbGltaXQgb3VyIGNyYXdscyB0byBtYWtlIG91ciB0ZXN0cyBzaG9ydGVyIGFuZCBzYWZlci5cXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogNTAsXFxufSk7XFxuXFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwczovL3dhcmVob3VzZS10aGVtZS1tZXRhbC5teXNob3BpZnkuY29tL2NvbGxlY3Rpb25zJ10pO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.9brryI4iuXbQaDc9Rrlr-uC_sc_YFA-SvBwHgCCTI3g\&asrc=run_on_apify)

```
import { PlaywrightCrawler, Dataset } from 'crawlee';

const crawler = new PlaywrightCrawler({
    requestHandler: async ({ page, request, enqueueLinks }) => {
        console.log(`Processing: ${request.url}`);
        if (request.label === 'DETAIL') {
            const urlPart = request.url.split('/').slice(-1); // ['sennheiser-mke-440-professional-stereo-shotgun-microphone-mke-440']
            const manufacturer = urlPart[0].split('-')[0]; // 'sennheiser'

            const title = await page.locator('.product-meta h1').textContent();
            const sku = await page.locator('span.product-meta__sku-number').textContent();

            const priceElement = page
                .locator('span.price')
                .filter({
                    hasText: '$',
                })
                .first();

            const currentPriceString = await priceElement.textContent();
            const rawPrice = currentPriceString?.split('$')[1];
            const price = Number(rawPrice?.replaceAll(',', ''));

            const inStockElement = page
                .locator('span.product-form__inventory')
                .filter({
                    hasText: 'In stock',
                })
                .first();

            const inStock = (await inStockElement.count()) > 0;

            const results = {
                url: request.url,
                manufacturer,
                title,
                sku,
                currentPrice: price,
                availableInStock: inStock,
            };

            await Dataset.pushData(results);
        } else if (request.label === 'CATEGORY') {
            // We are now on a category page. We can use this to paginate through and enqueue all products,
            // as well as any subsequent pages we find

            await page.waitForSelector('.product-item > a');
            await enqueueLinks({
                selector: '.product-item > a',
                label: 'DETAIL', // <= note the different label
            });

            // Now we need to find the "Next" button and enqueue the next page of results (if it exists)
            const nextButton = await page.$('a.pagination__next');
            if (nextButton) {
                await enqueueLinks({
                    selector: 'a.pagination__next',
                    label: 'CATEGORY', // <= note the same label
                });
            }
        } else {
            // This means we're on the start page, with no label.
            // On this page, we just want to enqueue all the category pages.

            await page.waitForSelector('.collection-block-item');
            await enqueueLinks({
                selector: '.collection-block-item',
                label: 'CATEGORY',
            });
        }
    },

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

await crawler.run(['https://warehouse-theme-metal.myshopify.com/collections']);
```

## What's `Dataset.pushData()`[​](#whats-datasetpushdata "Direct link to whats-datasetpushdata")

​[`Dataset.pushData()`](https://crawlee.dev/js/api/core/class/Dataset.md#pushData) is a function that saves data to the default [`Dataset`](https://crawlee.dev/js/api/core/class/Dataset.md). `Dataset` is a storage designed to hold data in a format similar to a table. Each time you call `Dataset.pushData()` a new row in the table is created, with the property names serving as column titles. In the default configuration, the rows are represented as JSON files saved on your disk, but other storage systems can be plugged into Crawlee as well.

Automatic dataset initialization in Crawlee

Each time you start Crawlee a default `Dataset` is automatically created, so there's no need to initialize it or create an instance first. You can create as many datasets as you want and even give them names. For more details see the [Result storage guide](https://crawlee.dev/js/docs/guides/result-storage.md#dataset) and the [`Dataset.open()`](https://crawlee.dev/js/api/core/class/Dataset.md#open) function.

## Finding saved data[​](#finding-saved-data "Direct link to Finding saved data")

Unless you changed the configuration that Crawlee uses locally, which would suggest that you knew what you were doing, and you didn't need this tutorial anyway, you'll find your data in the `storage` directory that Crawlee creates in the working directory of the running script:

```
{PROJECT_FOLDER}/storage/datasets/default/
```

The above folder will hold all your saved data in numbered files, as they were pushed into the dataset. Each file represents one invocation of `Dataset.pushData()` or one table row.

Single file data storage options

If you would like to store your data in a single big file, instead of many small ones, see the [Result storage guide](https://crawlee.dev/js/docs/guides/result-storage.md#key-value-store) for Key-value stores.

## Next steps[​](#next-steps "Direct link to Next steps")

Next, you'll see some improvements that you can add to your crawler code that will make it more readable and maintainable in the long run.
