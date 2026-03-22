# Source: https://crawlee.dev/js/docs/examples/file-download.md

# Download a file

Copy for LLM

When webcrawling, you sometimes need to download files such as images, PDFs, or other binary files. This example demonstrates how to download files using Crawlee and save them to the default key-value store.

The script simply downloads several files with plain HTTP requests using the custom [`FileDownload`](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md) crawler class and stores their contents in the default key-value store. In local configuration, the data will be stored as files in `./storage/key_value_stores/default`.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEZpbGVEb3dubG9hZCB9IGZyb20gJ2NyYXdsZWUnO1xcblxcbi8vIENyZWF0ZSBhIEZpbGVEb3dubG9hZCAtIGEgY3VzdG9tIGNyYXdsZXIgaW5zdGFuY2UgdGhhdCB3aWxsIGRvd25sb2FkIGZpbGVzIGZyb20gVVJMcy5cXG5jb25zdCBjcmF3bGVyID0gbmV3IEZpbGVEb3dubG9hZCh7XFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgYm9keSwgcmVxdWVzdCwgY29udGVudFR5cGUsIGdldEtleVZhbHVlU3RvcmUgfSkge1xcbiAgICAgICAgY29uc3QgdXJsID0gbmV3IFVSTChyZXF1ZXN0LnVybCk7XFxuICAgICAgICBjb25zdCBrdnMgPSBhd2FpdCBnZXRLZXlWYWx1ZVN0b3JlKCk7XFxuXFxuICAgICAgICBhd2FpdCBrdnMuc2V0VmFsdWUodXJsLnBhdGhuYW1lLnJlcGxhY2UoL1xcXFwvL2csICdfJyksIGJvZHksIHsgY29udGVudFR5cGU6IGNvbnRlbnRUeXBlLnR5cGUgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gVGhlIGluaXRpYWwgbGlzdCBvZiBVUkxzIHRvIGNyYXdsLiBIZXJlIHdlIHVzZSBqdXN0IGEgZmV3IGhhcmQtY29kZWQgVVJMcy5cXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKFtcXG4gICAgJ2h0dHBzOi8vcGRmb2JqZWN0LmNvbS9wZGYvc2FtcGxlLnBkZicsXFxuICAgICdodHRwczovL2Rvd25sb2FkLmJsZW5kZXIub3JnL3BlYWNoL2JpZ2J1Y2tidW5ueV9tb3ZpZXMvQmlnQnVja0J1bm55XzMyMHgxODAubXA0JyxcXG4gICAgJ2h0dHBzOi8vdXBsb2FkLndpa2ltZWRpYS5vcmcvd2lraXBlZGlhL2NvbW1vbnMvYy9jOC9FeGFtcGxlLm9nZycsXFxuXSk7XFxuXFxuLy8gUnVuIHRoZSBkb3dubG9hZGVyIGFuZCB3YWl0IGZvciBpdCB0byBmaW5pc2guXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cXG5jb25zb2xlLmxvZygnQ3Jhd2xlciBmaW5pc2hlZC4nKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.lA9lShaKL-UqYLrTmBECFTAxDjy9wuV88662NBW9hTg\&asrc=run_on_apify)

```
import { FileDownload } from 'crawlee';

// Create a FileDownload - a custom crawler instance that will download files from URLs.
const crawler = new FileDownload({
    async requestHandler({ body, request, contentType, getKeyValueStore }) {
        const url = new URL(request.url);
        const kvs = await getKeyValueStore();

        await kvs.setValue(url.pathname.replace(/\//g, '_'), body, { contentType: contentType.type });
    },
});

// The initial list of URLs to crawl. Here we use just a few hard-coded URLs.
await crawler.addRequests([
    'https://pdfobject.com/pdf/sample.pdf',
    'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4',
    'https://upload.wikimedia.org/wikipedia/commons/c/c8/Example.ogg',
]);

// Run the downloader and wait for it to finish.
await crawler.run();

console.log('Crawler finished.');
```
