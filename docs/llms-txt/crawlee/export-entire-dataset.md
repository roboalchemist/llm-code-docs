# Source: https://crawlee.dev/js/docs/examples/export-entire-dataset.md

# Export entire dataset to one file

Copy for LLM

This `Dataset` example uses the `exportToValue` function to export the entire default dataset to a single CSV file into the default key-value store.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQgfSBmcm9tICdjcmF3bGVlJztcXG5cXG4vLyBSZXRyaWV2ZSBvciBnZW5lcmF0ZSB0d28gaXRlbXMgdG8gYmUgcHVzaGVkXFxuY29uc3QgZGF0YSA9IFtcXG4gICAge1xcbiAgICAgICAgaWQ6IDEyMyxcXG4gICAgICAgIG5hbWU6ICdmb28nLFxcbiAgICB9LFxcbiAgICB7XFxuICAgICAgICBpZDogNDU2LFxcbiAgICAgICAgbmFtZTogJ2JhcicsXFxuICAgIH0sXFxuXTtcXG5cXG4vLyBQdXNoIHRoZSB0d28gaXRlbXMgdG8gdGhlIGRlZmF1bHQgZGF0YXNldFxcbmF3YWl0IERhdGFzZXQucHVzaERhdGEoZGF0YSk7XFxuXFxuLy8gRXhwb3J0IHRoZSBlbnRpcmV0eSBvZiB0aGUgZGF0YXNldCB0byBhIHNpbmdsZSBmaWxlIGluXFxuLy8gdGhlIGRlZmF1bHQga2V5LXZhbHVlIHN0b3JlIHVuZGVyIHRoZSBrZXkgXFxcIk9VVFBVVFxcXCJcXG5hd2FpdCBEYXRhc2V0LmV4cG9ydFRvQ1NWKCdPVVRQVVQnKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.BLrD3LxSd28XkttXUERpIQj2dQIkUd5kRf1WgkgH6po\&asrc=run_on_apify)

```
import { Dataset } from 'crawlee';

// Retrieve or generate two items to be pushed
const data = [
    {
        id: 123,
        name: 'foo',
    },
    {
        id: 456,
        name: 'bar',
    },
];

// Push the two items to the default dataset
await Dataset.pushData(data);

// Export the entirety of the dataset to a single file in
// the default key-value store under the key "OUTPUT"
await Dataset.exportToCSV('OUTPUT');
```
