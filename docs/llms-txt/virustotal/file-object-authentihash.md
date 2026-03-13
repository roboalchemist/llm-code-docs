# Source: https://virustotal.readme.io/reference/file-object-authentihash.md

# authentihash

hash to verify PE files.

`authentihash` is a sha256 hash [used by Microsoft](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) to verify that the relevant sections of a PE image file have not been altered. This specific type of hash is used by Microsoft AppLocker.

```json
{
  "data": {
		...
    "attributes" : {
      ...
      "authentihash": "<string>",
    }
  }
}
```
```json
{
    "data": {
        "attributes": {
            "authentihash": "6b9740557544535e594ba5e6585d78e6724be0bed40350211909d3cd97d8be1e",
        }
    }
}
```