# Source: https://docs.apify.com/sdk/js/docs/examples/map-and-reduce.md

# Dataset Map and Reduce methods

Copy for LLM

This example shows an easy use-case of the [`Dataset`](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) [`map`](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md#map) and [`reduce`](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md#reduce) methods. Both methods can be used to simplify the dataset results workflow process. Both can be called on the [dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) directly.

Important to mention is that both methods return a new result (`map` returns a new array and `reduce` can return any type) - neither method updates the dataset in any way.

Examples for both methods are demonstrated on a simple dataset containing the results scraped from a page: the `URL` and a hypothetical number of `h1` - `h3` header elements under the `headingCount` key.

This data structure is stored in the default dataset under `{PROJECT_FOLDER}/storage/datasets/default/`. If you want to simulate the functionality, you can use the [`Actor.pushData()`](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md#pushData) method to save the example `JSON array` to your dataset.

```
[
    {
        "url": "https://apify.com/",
        "headingCount": 11
    },
    {
        "url": "https://apify.com/storage",
        "headingCount": 8
    },
    {
        "url": "https://apify.com/proxy",
        "headingCount": 4
    }
]
```

### Map[](#map)

The dataset `map` method is very similar to standard Array mapping methods. It produces a new array of values by mapping each value in the existing array through a transformation function and an options parameter.

The `map` method used to check if are there more than 5 header elements on each page:

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcblxcbmF3YWl0IEFjdG9yLmluaXQoKTtcXG5cXG5jb25zdCBkYXRhc2V0ID0gYXdhaXQgQWN0b3Iub3BlbkRhdGFzZXQ8eyBoZWFkaW5nQ291bnQ6IG51bWJlciB9PigpO1xcblxcbi8vIGNhbGxpbmcgbWFwIGZ1bmN0aW9uIGFuZCBmaWx0ZXJpbmcgdGhyb3VnaCBtYXBwZWQgaXRlbXNcXG5jb25zdCBtb3JlVGhhbjVoZWFkZXJzID0gKFxcbiAgICBhd2FpdCBkYXRhc2V0Lm1hcCgoaXRlbSkgPT4gaXRlbS5oZWFkaW5nQ291bnQpXFxuKS5maWx0ZXIoKGNvdW50KSA9PiBjb3VudCA-IDUpO1xcblxcbi8vIHNhdmluZyByZXN1bHQgb2YgbWFwIHRvIGRlZmF1bHQgS2V5LXZhbHVlIHN0b3JlXFxuYXdhaXQgQWN0b3Iuc2V0VmFsdWUoJ3BhZ2VzX3dpdGhfbW9yZV90aGFuXzVfaGVhZGVycycsIG1vcmVUaGFuNWhlYWRlcnMpO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.rEYgnbXjDJ4eTxXqxEB8PtTkf-Ky6EDTYuYqMHw2XKE\&asrc=run_on_apify)

```
import { Actor } from 'apify';

await Actor.init();

const dataset = await Actor.openDataset<{ headingCount: number }>();

// calling map function and filtering through mapped items
const moreThan5headers = (
    await dataset.map((item) => item.headingCount)
).filter((count) => count > 5);

// saving result of map to default Key-value store
await Actor.setValue('pages_with_more_than_5_headers', moreThan5headers);

await Actor.exit();
```

The `moreThan5headers` variable is an array of `headingCount` attributes where the number of headers is greater than 5.

The `map` method's result value saved to the [`key-value store`](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md) should be:

```
[11, 8];
```

### Reduce[](#reduce)

The dataset `reduce` method does not produce a new array of values - it reduces a list of values down to a single value. The method iterates through the items in the dataset using the [`memo` argument](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md#reduce). After performing the necessary calculation, the `memo` is sent to the next iteration, while the item just processed is reduced (removed).

Using the `reduce` method to get the total number of headers scraped (all items in the dataset):

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcblxcbmNvbnN0IGRhdGFzZXQgPSBhd2FpdCBBY3Rvci5vcGVuRGF0YXNldCgpO1xcblxcbi8vIGNhbGxpbmcgcmVkdWNlIGZ1bmN0aW9uIGFuZCB1c2luZyBtZW1vIHRvIGNhbGN1bGF0ZSBudW1iZXIgb2YgaGVhZGVyc1xcbmNvbnN0IHBhZ2VzSGVhZGluZ0NvdW50ID0gYXdhaXQgZGF0YXNldC5yZWR1Y2UoKG1lbW8sIHZhbHVlKSA9PiB7XFxuICAgIHJldHVybiBtZW1vICsgdmFsdWUuaGVhZGluZ0NvdW50O1xcbn0sIDApO1xcblxcbi8vIHNhdmluZyByZXN1bHQgb2YgbWFwIHRvIGRlZmF1bHQgS2V5LXZhbHVlIHN0b3JlXFxuYXdhaXQgQWN0b3Iuc2V0VmFsdWUoJ3BhZ2VzX2hlYWRpbmdfY291bnQnLCBwYWdlc0hlYWRpbmdDb3VudCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.Ca5oSQWfTfmi-fp-gu9TTQKaoJ4BQW-1AhHXekmCV9c\&asrc=run_on_apify)

```
import { Actor } from 'apify';

const dataset = await Actor.openDataset();

// calling reduce function and using memo to calculate number of headers
const pagesHeadingCount = await dataset.reduce((memo, value) => {
    return memo + value.headingCount;
}, 0);

// saving result of map to default Key-value store
await Actor.setValue('pages_heading_count', pagesHeadingCount);
```

The original dataset will be reduced to a single value, `pagesHeadingCount`, which contains the count of all headers for all scraped pages (all dataset items).

The `reduce` method's result value saved to the [`key-value store`](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md) should be:

```
23;
```
