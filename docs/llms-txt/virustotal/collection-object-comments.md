# Source: https://virustotal.readme.io/reference/collection-object-comments.md

# 🔀 comments

Collection's comments

The *comments* relationship return the list of ***all comments in the Collection***.

This relationship can be retrieved using the [relationships API](https://virustotal.readme.io/reference/get-collections-relationship) endpoint. The response contains a list of [Comment](https://virustotal.readme.io/reference/comments) objects.

```json /collections/{id}/comments
{
  "data": [
    <COMMENT_OBJECT>,
    <COMMENT_OBJECT>,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
  "meta": {
    "count": 2,
    "cursor": "CnoKEQoEZGF0ZRIJCIeGybGKre4CEmFqEXN-dmlydXN0b3RhbGNsb3VkckwLEgpDb2xsZWN0aW9uIhN0ZXN0ZGF0YV9jb2xsZWN0aW9uDAsSB0NvbW1lbnQiHHRlc3RkYXRhX2NvbGxlY3Rpb24tOWVhYzZjM2MMGAAgAQ=="
  },
  "data": [
    {
      "attributes": {
        "votes": {
          "positive": 0,
          "abuse": 0,
          "negative": 0
        },
        "tags": [
          "_:web",
          "_:public"
        ],
        "text": "test",
        "html": "test",
        "date": 1611233999
      },
      "type": "comment",
      "id": "c-testdata_collection-9eac6c3c",
      "links": {
        "self": "https://virustotal.com/api/v3/comments/c-testdata_collection-9eac6c3c"
      }
    }
  ],
  "links": {
    "self": "https://virustotal.com/api/v3/collections/testdata_collection/comments?limit=1",
    "next": "https://virustotal.com/api/v3/collections/testdata_collection/comments?cursor=CnoKEQoEZGF0ZRIJCIeGybGKre4CEmFqEXN-dmlydXN0b3RhbGNsb3VkckwLEgpDb2xsZWN0aW9uIhN0ZXN0ZGF0YV9jb2xsZWN0aW9uDAsSB0NvbW1lbnQiHHRlc3RkYXRhX2NvbGxlY3Rpb24tOWVhYzZjM2MMGAAgAQ%3D%3D&limit=1"
  }
}
```