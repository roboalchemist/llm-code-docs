# Source: https://www.electronjs.org/docs/latest/api/structures/protocol-response

# ProtocolResponse Object

- `error` Integer (optional) - When assigned, the `request` will fail with the `error` number . For the available error numbers you can use, please see the [net error list](https://source.chromium.org/chromium/chromium/src/+/main:net/base/net_error_list.h).
- `statusCode` number (optional) - The HTTP response code, default is 200.
- `charset` string (optional) - The charset of response body, default is `"utf-8"`.
- `mimeType` string (optional) - The MIME type of response body, default is `"text/html"`. Setting `mimeType` would implicitly set the `content-type` header in response, but if `content-type` is already set in `headers`, the `mimeType` would be ignored.
- `headers` Record\<string, string \| string\[\]\> (optional) - An object containing the response headers. The keys must be string, and values must be either string or Array of string.
- `data` (Buffer \| string \| ReadableStream) (optional) - The response body. When returning stream as response, this is a Node.js readable stream representing the response body. When returning `Buffer` as response, this is a `Buffer`. When returning `string` as response, this is a `string`. This is ignored for other types of responses.
- `path` string (optional) - Path to the file which would be sent as response body. This is only used for file responses.
- `url` string (optional) - Download the `url` and pipe the result as response body. This is only used for URL responses.
- `referrer` string (optional) - The `referrer` URL. This is only used for file and URL responses.
- `method` string (optional) - The HTTP `method`. This is only used for file and URL responses.
- `session` Session (optional) - The session used for requesting URL. The HTTP request will reuse the current session by default.
- `uploadData` [ProtocolResponseUploadData](/docs/latest/api/structures/protocol-response-upload-data) (optional) - The data used as upload data. This is only used for URL responses when `method` is `"POST"`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/protocol-response.md)