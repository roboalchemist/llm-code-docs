# Source: https://docs.logrocket.com/reference/shouldparsexhrblob.md

# Parse XML Blobs

Control whether or not LogRocket parses blobs in response bodies

## Enable parsing of Blobs from XMLHTTPRequest response bodies

#### `shouldParseXHRBlob` - Boolean

##### optional (default - `false`)

LogRocket will save XMLHTTPRequest bodies of [responseType](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType) `Blob` as `[object Blob]` by default in the network request details. To have Blobs that encode JSON text decoded, enable this option.

If you want to enable this feature, add this option to your configuration:

```javascript
LogRocket.init(YOUR_APP_ID, {
  shouldParseXHRBlob: true,
});
```

> 📘 The popular package `cross-fetch` provides an implementation of `fetch()` using XMLHTTPRequests. In order to avoid having all fetch response bodies recorded as Blobs, enable this option.