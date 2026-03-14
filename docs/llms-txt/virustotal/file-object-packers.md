# Source: https://virustotal.readme.io/reference/file-object-packers.md

# packers

identification of packers used by files.

`packers` identifies packers used on Windows PE files by several tools and AVs. Keys are tool names and values are identified packers, both strings.

```json PEiD packer identifier
{
  "data": {
		...
    "attributes" : {
      ...
      "packers": {
        	"<string>": "<string>", ...
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "packers": {
                "F-PROT": "UPX",
                "PEiD": "UPX v0.89.6 - v1.02 / v1.05 -v1.22 (Delphi) stub"
            }
        }
    }
}
```