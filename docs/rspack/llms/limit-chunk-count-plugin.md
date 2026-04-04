# Source: https://rspack.dev/plugins/webpack/limit-chunk-count-plugin.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/plugins/limit-chunk-count-plugin/](https://webpack.js.org/plugins/limit-chunk-count-plugin/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# LimitChunkCountPlugin

While writing your code, you may have already added many code split points to load stuff on demand. After compiling you might notice that some chunks are too small - creating larger HTTP overhead. `LimitChunkCountPlugin` can post-process your chunks by merging them.

```js
new rspack.optimize.LimitChunkCountPlugin({
  // Options...
});
```

## Options

### maxChunks

- **Type:** `number`

Limit the maximum number of chunks using a value greater than or equal to `1`. Using `1` will prevent any additional chunks from being added as the entry/main chunk is also included in the count.

```js
new rspack.optimize.LimitChunkCountPlugin({
  maxChunks: 5,
});
```
