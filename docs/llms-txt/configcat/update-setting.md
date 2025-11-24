# Source: https://configcat.com/docs/api/reference/update-setting.md

# Update Flag

```
PATCH 
/v1/settings/:settingId
```

This endpoint updates the metadata of a Feature Flag or Setting with a collection of [JSON Patch](https://jsonpatch.com) operations in a specified Config.

Only the `name`, `hint` and `tags` attributes are modifiable by this endpoint. The `tags` attribute is a simple collection of the [tag IDs](https://configcat.com/docs/docs/api/reference/get-tags/.md) attached to the given setting.

The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change.

For example: We have the following resource.

```
{
  "settingId": 5345,
  "key": "myGrandFeature",
  "name": "Tihs is a naem with soem typos.",
  "hint": "This flag controls my grandioso feature.",
  "settingType": "boolean",
  "tags": [
    {
      "tagId": 0, 
      "name": "sample tag", 
      "color": "whale"
    }
  ]
}
```

If we send an update request body as below (it changes the `name` and adds the already existing tag with the id `2`):

```
[
  {
    "op": "replace", 
    "path": "/name", 
    "value": "This is the name without typos."
  }, 
  {
    "op": "add", 
    "path": "/tags/-", 
    "value": 2
  }
]
```

Only the `name` and `tags` are updated and all the other attributes remain unchanged. So we get a response like this:

```
{
  "settingId": 5345, 
  "key": "myGrandFeature", 
  "name": "This is the name without typos.", 
  "hint": "This flag controls my grandioso feature.", 
  "settingType": "boolean", 
  "tags": [
    {
      "tagId": 0, 
      "name": "sample tag", 
      "color": "whale"
    }, 
    {
      "tagId": 2, 
      "name": "another tag", 
      "color": "koala"
    }
  ]
}
```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
