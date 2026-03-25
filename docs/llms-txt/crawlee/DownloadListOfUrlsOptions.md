# Source: https://crawlee.dev/js/api/utils/interface/DownloadListOfUrlsOptions.md

# DownloadListOfUrlsOptions<!-- -->

## Index[**](#Index)

### Properties

* [**encoding](#encoding)
* [**proxyUrl](#proxyUrl)
* [**url](#url)
* [**urlRegExp](#urlRegExp)

## Properties<!-- -->[**](#Properties)

### [**](#encoding)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/extract-urls.ts#L16)optionalencoding

**encoding?

<!-- -->

: BufferEncoding = BufferEncoding

The encoding of the file.

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/extract-urls.ts#L26)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Allows to use a proxy for the download request.

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/extract-urls.ts#L10)url

**url: string

URL to the file

### [**](#urlRegExp)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/extract-urls.ts#L23)optionalurlRegExp

**urlRegExp?

<!-- -->

: RegExp = RegExp

Custom regular expression to identify the URLs in the file to extract. The regular expression should be case-insensitive and have global flag set (i.e. `/something/gi`).
