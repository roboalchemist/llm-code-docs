# Source: https://virustotal.readme.io/reference/file-object-ssdeep.md

# ssdeep

CTPH hash of the file content.

`ssdeep` is a program for computing [Context Triggered Piecewise Hashes](https://ssdeep-project.github.io/ssdeep/index.html). Also called fuzzy hashes, it allows identifying similar files by comparing (via Edit Distance) their hashes.

```json ssdeep
{
  "data": {
		...
    "attributes" : {
      ...
      "ssdeep": "<string>"
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "ssdeep": "98504:G5j6i51u5gM0P5kv5GzH5AY5NfrL5sZte5vw5CA:e5AA5i5vw"
        }
    }
}
```