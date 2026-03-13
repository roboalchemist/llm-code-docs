# Source: https://virustotal.readme.io/reference/file-object-file-javascript-info.md

# javascript_info

Information extracted out of Javascript files

`javascript_info` returns information about [Javascript files](https://en.wikipedia.org/wiki/JavaScript). It contains the following fields:

* `tags`: <*list of strings*> interesting elements in the code. Can be any of:
  * `aes-encoded`
  * `Aes.Ctr.decrypt`
  * `charAt`
  * `charCodeAt`
  * `document.getElementById`
  * `document.write`
  * `eval`
  * `eval+unescape`
  * `fromCharCode`
  * `location`
  * `malformed`
  * `Math`
  * `obfuscated`
  * `ParseInt`
  * `replace`
  * `substr`
  * `unescape`
  * `write`
  * `write+unescape`

```json Javascript information
{
  "data": {
    "attributes": {
      "javascript_info": {
        "tags": ["<string>", ...]
      }
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "javascript_info": {
        "tags": [
          "document.getElementById",
          "unescape",
          "charAt",
          "charCodeAt",
          "replace",
          "write",
          "substr",
          "location",
          "eval",
          "Math",
          "fromCharCode"
        ]
      }
    }
  }
}
```