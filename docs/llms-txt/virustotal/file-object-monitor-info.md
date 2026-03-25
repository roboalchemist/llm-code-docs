# Source: https://virustotal.readme.io/reference/file-object-monitor-info.md

# monitor_info

Information from VT monitor

> 🚧 Deprecated
>
> This field is deprecated. Use [known\_distributors](#known_distributors) instead.
>
> The field will be removed from the API on January 1st 2022.

`monitor_info` contains information extracted from our VT Monitor service. Indicates that this file is present in a VirusTotal Monitor collection.

* `filenames`: <*list of strings*> all different filenames the file has been submitted under.
* `organizations`: <*list of strings*> organization names who uploaded the file.

```json monitor_info
{
  "data": {
    "attributes": {
      "monitor_info": {
        "filenames": [
          "<strings>"
        ],
        "organizations": [
          "<strings>"
        ]
      }
    }
}
```
```json Example
{
  "data": {
    "attributes": {
      "monitor_info": {
        "filenames": [
          "testfilename"
        ],
        "organizations": [
          "Example Inc."
        ]
      },
    }
}
```