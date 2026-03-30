# Source: https://crawlee.dev/js/docs/examples/file-download-stream.md

# Download a file with Node.js streams

Copy for LLM

For larger files, it is more efficient to use Node.js streams to download and transfer the files. This example demonstrates how to download files using streams.

The script uses the [`FileDownload`](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md) crawler class to download files with streams, log the progress, and store the data in the key-value store. In local configuration, the data will be stored as files in `./storage/key_value_stores/default`.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IHBpcGVsaW5lLCBUcmFuc2Zvcm0gfSBmcm9tICdzdHJlYW0nO1xcblxcbmltcG9ydCB7IEZpbGVEb3dubG9hZCwgdHlwZSBMb2cgfSBmcm9tICdjcmF3bGVlJztcXG5cXG4vLyBBIHNhbXBsZSBUcmFuc2Zvcm0gc3RyZWFtIGxvZ2dpbmcgdGhlIGRvd25sb2FkIHByb2dyZXNzLlxcbmZ1bmN0aW9uIGNyZWF0ZVByb2dyZXNzVHJhY2tlcih7IHVybCwgbG9nLCB0b3RhbEJ5dGVzIH06IHsgdXJsOiBVUkw7IGxvZzogTG9nOyB0b3RhbEJ5dGVzOiBudW1iZXIgfSkge1xcbiAgICBsZXQgZG93bmxvYWRlZEJ5dGVzID0gMDtcXG5cXG4gICAgcmV0dXJuIG5ldyBUcmFuc2Zvcm0oe1xcbiAgICAgICAgdHJhbnNmb3JtKGNodW5rLCBfLCBjYWxsYmFjaykge1xcbiAgICAgICAgICAgIGlmIChkb3dubG9hZGVkQnl0ZXMgJSAxZTYgPiAoZG93bmxvYWRlZEJ5dGVzICsgY2h1bmsubGVuZ3RoKSAlIDFlNikge1xcbiAgICAgICAgICAgICAgICBsb2cuaW5mbyhcXG4gICAgICAgICAgICAgICAgICAgIGBEb3dubG9hZGVkICR7ZG93bmxvYWRlZEJ5dGVzIC8gMWU2fSBNQiAoJHtNYXRoLmZsb29yKChkb3dubG9hZGVkQnl0ZXMgLyB0b3RhbEJ5dGVzKSAqIDEwMCl9JSkgZm9yICR7dXJsfS5gLFxcbiAgICAgICAgICAgICAgICApO1xcbiAgICAgICAgICAgIH1cXG4gICAgICAgICAgICBkb3dubG9hZGVkQnl0ZXMgKz0gY2h1bmsubGVuZ3RoO1xcblxcbiAgICAgICAgICAgIHRoaXMucHVzaChjaHVuayk7XFxuICAgICAgICAgICAgY2FsbGJhY2soKTtcXG4gICAgICAgIH0sXFxuICAgIH0pO1xcbn1cXG5cXG4vLyBDcmVhdGUgYSBGaWxlRG93bmxvYWQgLSBhIGN1c3RvbSBjcmF3bGVyIGluc3RhbmNlIHRoYXQgd2lsbCBkb3dubG9hZCBmaWxlcyBmcm9tIFVSTHMuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBGaWxlRG93bmxvYWQoe1xcbiAgICBhc3luYyBzdHJlYW1IYW5kbGVyKHsgc3RyZWFtLCByZXF1ZXN0LCBsb2csIGdldEtleVZhbHVlU3RvcmUgfSkge1xcbiAgICAgICAgY29uc3QgdXJsID0gbmV3IFVSTChyZXF1ZXN0LnVybCk7XFxuXFxuICAgICAgICBsb2cuaW5mbyhgRG93bmxvYWRpbmcgJHt1cmx9IHRvICR7dXJsLnBhdGhuYW1lLnJlcGxhY2UoL1xcXFwvL2csICdfJyl9Li4uYCk7XFxuXFxuICAgICAgICBhd2FpdCBuZXcgUHJvbWlzZTx2b2lkPigocmVzb2x2ZSwgcmVqZWN0KSA9PiB7XFxuICAgICAgICAgICAgLy8gV2l0aCB0aGUgJ3Jlc3BvbnNlJyBldmVudCwgd2UgaGF2ZSByZWNlaXZlZCB0aGUgaGVhZGVycyBvZiB0aGUgcmVzcG9uc2UuXFxuICAgICAgICAgICAgc3RyZWFtLm9uKCdyZXNwb25zZScsIGFzeW5jIChyZXNwb25zZSkgPT4ge1xcbiAgICAgICAgICAgICAgICBjb25zdCBrdnMgPSBhd2FpdCBnZXRLZXlWYWx1ZVN0b3JlKCk7XFxuICAgICAgICAgICAgICAgIGF3YWl0IGt2cy5zZXRWYWx1ZShcXG4gICAgICAgICAgICAgICAgICAgIHVybC5wYXRobmFtZS5yZXBsYWNlKC9cXFxcLy9nLCAnXycpLFxcbiAgICAgICAgICAgICAgICAgICAgcGlwZWxpbmUoXFxuICAgICAgICAgICAgICAgICAgICAgICAgc3RyZWFtLFxcbiAgICAgICAgICAgICAgICAgICAgICAgIGNyZWF0ZVByb2dyZXNzVHJhY2tlcih7IHVybCwgbG9nLCB0b3RhbEJ5dGVzOiBOdW1iZXIocmVzcG9uc2UuaGVhZGVyc1snY29udGVudC1sZW5ndGgnXSkgfSksXFxuICAgICAgICAgICAgICAgICAgICAgICAgKGVycm9yKSA9PiB7XFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIChlcnJvcikgcmVqZWN0KGVycm9yKTtcXG4gICAgICAgICAgICAgICAgICAgICAgICB9LFxcbiAgICAgICAgICAgICAgICAgICAgKSxcXG4gICAgICAgICAgICAgICAgICAgIHsgY29udGVudFR5cGU6IHJlc3BvbnNlLmhlYWRlcnNbJ2NvbnRlbnQtdHlwZSddIH0sXFxuICAgICAgICAgICAgICAgICk7XFxuXFxuICAgICAgICAgICAgICAgIGxvZy5pbmZvKGBEb3dubG9hZGVkICR7dXJsfSB0byAke3VybC5wYXRobmFtZS5yZXBsYWNlKC9cXFxcLy9nLCAnXycpfS5gKTtcXG5cXG4gICAgICAgICAgICAgICAgcmVzb2x2ZSgpO1xcbiAgICAgICAgICAgIH0pO1xcbiAgICAgICAgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gVGhlIGluaXRpYWwgbGlzdCBvZiBVUkxzIHRvIGNyYXdsLiBIZXJlIHdlIHVzZSBqdXN0IGEgZmV3IGhhcmQtY29kZWQgVVJMcy5cXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKFtcXG4gICAgJ2h0dHBzOi8vZG93bmxvYWQuYmxlbmRlci5vcmcvcGVhY2gvYmlnYnVja2J1bm55X21vdmllcy9CaWdCdWNrQnVubnlfMzIweDE4MC5tcDQnLFxcbiAgICAnaHR0cHM6Ly9kb3dubG9hZC5ibGVuZGVyLm9yZy9wZWFjaC9iaWdidWNrYnVubnlfbW92aWVzL0JpZ0J1Y2tCdW5ueV82NDB4MzYwLm00dicsXFxuXSk7XFxuXFxuLy8gUnVuIHRoZSBkb3dubG9hZGVyIGFuZCB3YWl0IGZvciBpdCB0byBmaW5pc2guXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.p6REYoHLUmIyvUTwyLYhetG0F1lH4usCZiuf0iBHM6w\&asrc=run_on_apify)

```
import { pipeline, Transform } from 'stream';

import { FileDownload, type Log } from 'crawlee';

// A sample Transform stream logging the download progress.
function createProgressTracker({ url, log, totalBytes }: { url: URL; log: Log; totalBytes: number }) {
    let downloadedBytes = 0;

    return new Transform({
        transform(chunk, _, callback) {
            if (downloadedBytes % 1e6 > (downloadedBytes + chunk.length) % 1e6) {
                log.info(
                    `Downloaded ${downloadedBytes / 1e6} MB (${Math.floor((downloadedBytes / totalBytes) * 100)}%) for ${url}.`,
                );
            }
            downloadedBytes += chunk.length;

            this.push(chunk);
            callback();
        },
    });
}

// Create a FileDownload - a custom crawler instance that will download files from URLs.
const crawler = new FileDownload({
    async streamHandler({ stream, request, log, getKeyValueStore }) {
        const url = new URL(request.url);

        log.info(`Downloading ${url} to ${url.pathname.replace(/\//g, '_')}...`);

        await new Promise<void>((resolve, reject) => {
            // With the 'response' event, we have received the headers of the response.
            stream.on('response', async (response) => {
                const kvs = await getKeyValueStore();
                await kvs.setValue(
                    url.pathname.replace(/\//g, '_'),
                    pipeline(
                        stream,
                        createProgressTracker({ url, log, totalBytes: Number(response.headers['content-length']) }),
                        (error) => {
                            if (error) reject(error);
                        },
                    ),
                    { contentType: response.headers['content-type'] },
                );

                log.info(`Downloaded ${url} to ${url.pathname.replace(/\//g, '_')}.`);

                resolve();
            });
        });
    },
});

// The initial list of URLs to crawl. Here we use just a few hard-coded URLs.
await crawler.addRequests([
    'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4',
    'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_640x360.m4v',
]);

// Run the downloader and wait for it to finish.
await crawler.run();
```
