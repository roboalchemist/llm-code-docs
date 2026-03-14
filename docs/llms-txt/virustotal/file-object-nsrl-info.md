# Source: https://virustotal.readme.io/reference/file-object-nsrl-info.md

# nsrl_info

Whitelisted files from the NSRL.

> 🚧 Deprecated
>
> This field is deprecated. Use [known\_distributors](#known_distributors) instead.
>
> The field will be removed from the API on January 1st 2022.

`nsrl_info` is a dictionary only present for files in the [National Software Reference Library](http://www.nsrl.nist.gov/). These files have a `nsrl` tag (see `tag` attribute). The object contains two fields:

* `products`: <*list of strings*> contains the software products in which the given file was found.
* `filenames`: <*list of strings*> contains the filenames with which the file was found in any of these products.

```json NSRL information
{
    "data": {
        "attributes": {
            ...
            "nsrl_info": {
                "filenames": ["<strings>"],
                "products": ["<strings>"]
            },
            ...
        },
        ...
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "nsrl_info": {
                "filenames": [
                    "NULL.TXT",
                    "x0r.{kf",
                    "x0r.{kc"
                ],
                "products": [
                    "Quicken (Unknown)",
                    "Linux Format Great Game Demos (Future Publishing)",
                    "DISTROS GALORE Gentoo Linux 2005.0 and Ubuntu 5.04 (Future Publishing)",
                    "Slackware Linux 10.1 (Linux Magazine)"
                ]
            }
        }
    }
}
```