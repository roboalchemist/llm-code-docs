# Source: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/index.md

---

title: ReadableStreamBYOBReader · Cloudflare Workers docs
description: BYOB is an abbreviation of bring your own buffer. A
  ReadableStreamBYOBReader allows reading into a developer-supplied buffer, thus
  minimizing copies.
lastUpdated: 2026-02-11T15:04:03.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/
  md: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/index.md
---

## Background

`BYOB` is an abbreviation of bring your own buffer. A `ReadableStreamBYOBReader` allows reading into a developer-supplied buffer, thus minimizing copies.

An instance of `ReadableStreamBYOBReader` is functionally identical to [`ReadableStreamDefaultReader`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/) with the exception of the `read` method.

A `ReadableStreamBYOBReader` is not instantiated via its constructor. Rather, it is retrieved from a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/):

```js
const { readable, writable } = new TransformStream();
const reader = readable.getReader({ mode: 'byob' });
```

***

## Methods

* `read(bufferArrayBufferView)` : Promise\<ReadableStreamBYOBReadResult>

  * Returns a promise with the next available chunk of data read into a passed-in buffer.

* `readAtLeast(minBytes, bufferArrayBufferView)` : Promise\<ReadableStreamBYOBReadResult>

  * Returns a promise with the next available chunk of data read into a passed-in buffer. The promise will not resolve until at least `minBytes` bytes have been read. However, fewer than `minBytes` bytes may be returned if the end of the stream is reached or the underlying stream is closed. Specifically:

    * If `minBytes` or more bytes are available, the promise resolves with `{ value: <buffer view sized to bytes read>, done: false }`.
    * If the stream ends after some bytes have been read but fewer than `minBytes`, the promise resolves with the partial data: `{ value: <buffer view sized to bytes actually read>, done: false }`. The next call to `read` or `readAtLeast` will then return `{ value: undefined, done: true }`.
    * If the stream ends with zero bytes available (that is, the stream is already at EOF), the promise resolves with `{ value: <zero-length view>, done: true }`.
    * If the stream errors, the promise rejects.
    * `minBytes` must be at least 1, and must not exceed the byte length of `bufferArrayBufferView`, or the promise rejects with a `TypeError`.

***

## Common issues

Warning

`read` provides no control over the minimum number of bytes that should be read into the buffer. Even if you allocate a 1 MiB buffer, the kernel is perfectly within its rights to fulfill this read with a single byte, whether or not an EOF immediately follows.

In practice, the Workers team has found that `read` typically fills only 1% of the provided buffer.

`readAtLeast` is a non-standard extension to the Streams API which allows users to specify that at least `minBytes` bytes must be read into the buffer before resolving the read. If the stream ends before `minBytes` bytes are available, the partial data that was read is still returned rather than throwing an error — refer to the [`readAtLeast` method documentation above](#methods) for the full details.

***

## Related resources

* [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
* [Background about BYOB readers in the Streams API WHATWG specification](https://streams.spec.whatwg.org/#byob-readers)
