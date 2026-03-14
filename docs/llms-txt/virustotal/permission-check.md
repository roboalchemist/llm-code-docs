# Source: https://virustotal.readme.io/reference/permission-check.md

# permissions_checked

Records a query to see whether a given component/package/process/service has a particular permission.

`permissions_checked` contains a list of **Android permissions that the app checks to see if they are granted.**

It is a list of dictionaries, every item in the list contains the following fields:

* `owner`: <*string*> name of the application that has been granted the checked permission.
* `permission`: <*string*> example: android.permission.INTERNET.

```json Checked permissions
{
    "data": {
        "attributes": {
            "permissions_checked": [
                {
                    "owner": "<string>",
                    "permission": "<string>"
                },...
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "permissions_checked": [
                {
                    "owner": "blablabla",
                    "permission": "android.permission.INTERNET"
                },
                {
                    "owner": "blablabla",
                    "permission": "android.permission.ACCESS_NETWORK_STATE"
                }
            ]
        }
    }
}
```