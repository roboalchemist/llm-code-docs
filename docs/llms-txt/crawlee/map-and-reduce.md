# Source: https://crawlee.dev/js/docs/examples/map-and-reduce.md

# Dataset Map and Reduce methods

Copy for LLM

This example shows an easy use-case of the [`Dataset`](https://crawlee.dev/js/api/core/class/Dataset.md) [`map`](https://crawlee.dev/js/api/core/class/Dataset.md#map) and [`reduce`](https://crawlee.dev/js/api/core/class/Dataset.md#reduce) methods. Both methods can be used to simplify the dataset results workflow process. Both can be called on the [dataset](https://crawlee.dev/js/api/core/class/Dataset.md) directly.

Important to mention is that both methods return a new result (`map` returns a new array and `reduce` can return any type) - neither method updates the dataset in any way.

Examples for both methods are demonstrated on a simple dataset containing the results scraped from a page: the `URL` and a hypothetical number of `h1` - `h3` header elements under the `headingCount` key.

This data structure is stored in the default dataset under `{PROJECT_FOLDER}/storage/datasets/default/`. If you want to simulate the functionality, you can use the [`dataset.pushData()`](https://crawlee.dev/js/api/core/class/Dataset.md#pushData) method to save the example `JSON array` to your dataset.

```
[
    {
        "url": "https://crawlee.dev/",
        "headingCount": 11
    },
    {
        "url": "https://crawlee.dev/storage",
        "headingCount": 8
    },
    {
        "url": "https://crawlee.dev/proxy",
        "headingCount": 4
    }
]
```

### Map[​](#map "Direct link to Map")

The dataset `map` method is very similar to standard Array mapping methods. It produces a new array of values by mapping each value in the existing array through a transformation function and an options parameter.

The `map` method used to check if are there more than 5 header elements on each page:

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQsIEtleVZhbHVlU3RvcmUgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBkYXRhc2V0ID0gYXdhaXQgRGF0YXNldC5vcGVuPHtcXG4gICAgdXJsOiBzdHJpbmc7XFxuICAgIGhlYWRpbmdDb3VudDogbnVtYmVyO1xcbn0-KCk7XFxuXFxuLy8gU2VlZGluZyB0aGUgZGF0YXNldCB3aXRoIHNvbWUgZGF0YVxcbmF3YWl0IGRhdGFzZXQucHVzaERhdGEoW1xcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2LycsXFxuICAgICAgICBoZWFkaW5nQ291bnQ6IDExLFxcbiAgICB9LFxcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2L3N0b3JhZ2UnLFxcbiAgICAgICAgaGVhZGluZ0NvdW50OiA4LFxcbiAgICB9LFxcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2L3Byb3h5JyxcXG4gICAgICAgIGhlYWRpbmdDb3VudDogNCxcXG4gICAgfSxcXG5dKTtcXG5cXG4vLyBDYWxsaW5nIG1hcCBmdW5jdGlvbiBhbmQgZmlsdGVyaW5nIHRocm91Z2ggbWFwcGVkIGl0ZW1zLi4uXFxuY29uc3QgbW9yZVRoYW41aGVhZGVycyA9IChhd2FpdCBkYXRhc2V0Lm1hcCgoaXRlbSkgPT4gaXRlbS5oZWFkaW5nQ291bnQpKS5maWx0ZXIoKGNvdW50KSA9PiBjb3VudCA-IDUpO1xcblxcbi8vIFNhdmluZyB0aGUgcmVzdWx0IG9mIG1hcCB0byBkZWZhdWx0IGtleS12YWx1ZSBzdG9yZS4uLlxcbmF3YWl0IEtleVZhbHVlU3RvcmUuc2V0VmFsdWUoJ3BhZ2VzX3dpdGhfbW9yZV90aGFuXzVfaGVhZGVycycsIG1vcmVUaGFuNWhlYWRlcnMpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.dWnmTm2KruX_Ypcwm8jC0o6B-FFEiKkCEtDIWGEmXDQ\&asrc=run_on_apify)

```
import { Dataset, KeyValueStore } from 'crawlee';

const dataset = await Dataset.open<{
    url: string;
    headingCount: number;
}>();

// Seeding the dataset with some data
await dataset.pushData([
    {
        url: 'https://crawlee.dev/',
        headingCount: 11,
    },
    {
        url: 'https://crawlee.dev/storage',
        headingCount: 8,
    },
    {
        url: 'https://crawlee.dev/proxy',
        headingCount: 4,
    },
]);

// Calling map function and filtering through mapped items...
const moreThan5headers = (await dataset.map((item) => item.headingCount)).filter((count) => count > 5);

// Saving the result of map to default key-value store...
await KeyValueStore.setValue('pages_with_more_than_5_headers', moreThan5headers);
```

The `moreThan5headers` variable is an array of `headingCount` attributes where the number of headers is greater than 5.

The `map` method's result value saved to the [`key-value store`](https://crawlee.dev/js/api/core/class/KeyValueStore.md) should be:

```
[11, 8]
```

### Reduce[​](#reduce "Direct link to Reduce")

The dataset `reduce` method does not produce a new array of values - it reduces a list of values down to a single value. The method iterates through the items in the dataset using the [`memo` argument](https://crawlee.dev/js/api/core/class/Dataset.md#reduce). After performing the necessary calculation, the `memo` is sent to the next iteration, while the item just processed is reduced (removed).

Using the `reduce` method to get the total number of headers scraped (all items in the dataset):

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQsIEtleVZhbHVlU3RvcmUgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBkYXRhc2V0ID0gYXdhaXQgRGF0YXNldC5vcGVuPHtcXG4gICAgdXJsOiBzdHJpbmc7XFxuICAgIGhlYWRpbmdDb3VudDogbnVtYmVyO1xcbn0-KCk7XFxuXFxuLy8gU2VlZGluZyB0aGUgZGF0YXNldCB3aXRoIHNvbWUgZGF0YVxcbmF3YWl0IGRhdGFzZXQucHVzaERhdGEoW1xcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2LycsXFxuICAgICAgICBoZWFkaW5nQ291bnQ6IDExLFxcbiAgICB9LFxcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2L3N0b3JhZ2UnLFxcbiAgICAgICAgaGVhZGluZ0NvdW50OiA4LFxcbiAgICB9LFxcbiAgICB7XFxuICAgICAgICB1cmw6ICdodHRwczovL2NyYXdsZWUuZGV2L3Byb3h5JyxcXG4gICAgICAgIGhlYWRpbmdDb3VudDogNCxcXG4gICAgfSxcXG5dKTtcXG5cXG4vLyBjYWxsaW5nIHJlZHVjZSBmdW5jdGlvbiBhbmQgdXNpbmcgbWVtbyB0byBjYWxjdWxhdGUgbnVtYmVyIG9mIGhlYWRlcnNcXG5jb25zdCBwYWdlc0hlYWRpbmdDb3VudCA9IGF3YWl0IGRhdGFzZXQucmVkdWNlKChtZW1vLCB2YWx1ZSkgPT4ge1xcbiAgICByZXR1cm4gbWVtbyArIHZhbHVlLmhlYWRpbmdDb3VudDtcXG59LCAwKTtcXG5cXG4vLyBzYXZpbmcgcmVzdWx0IG9mIG1hcCB0byBkZWZhdWx0IEtleS12YWx1ZSBzdG9yZVxcbmF3YWl0IEtleVZhbHVlU3RvcmUuc2V0VmFsdWUoJ3BhZ2VzX2hlYWRpbmdfY291bnQnLCBwYWdlc0hlYWRpbmdDb3VudCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.L0rbLqQxTG_mkQh0PqIgkFgTsa2luGQx5z1Fh2bLdwo\&asrc=run_on_apify)

```
import { Dataset, KeyValueStore } from 'crawlee';

const dataset = await Dataset.open<{
    url: string;
    headingCount: number;
}>();

// Seeding the dataset with some data
await dataset.pushData([
    {
        url: 'https://crawlee.dev/',
        headingCount: 11,
    },
    {
        url: 'https://crawlee.dev/storage',
        headingCount: 8,
    },
    {
        url: 'https://crawlee.dev/proxy',
        headingCount: 4,
    },
]);

// calling reduce function and using memo to calculate number of headers
const pagesHeadingCount = await dataset.reduce((memo, value) => {
    return memo + value.headingCount;
}, 0);

// saving result of map to default Key-value store
await KeyValueStore.setValue('pages_heading_count', pagesHeadingCount);
```

The original dataset will be reduced to a single value, `pagesHeadingCount`, which contains the count of all headers for all scraped pages (all dataset items).

The `reduce` method's result value saved to the [`key-value store`](https://crawlee.dev/js/api/core/class/KeyValueStore.md) should be:

```
23
```
