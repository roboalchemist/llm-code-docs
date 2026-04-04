# Source: https://virustotal.readme.io/reference/file-object-magic.md

# magic

identification of files via magic number.

`magic` gives a guess of the file type, based on a popular parsing tool from unix.

```json File type guess based on "magic" tool
{
  "data": {
		...
    "attributes" : {
      ...
      "magic": "<string>",
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "magic": "Mach-O fat file with 2 architectures"
        }
    }
}
```