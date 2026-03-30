# Source: https://virustotal.readme.io/reference/collection-object-references.md

# 🔀 references

Collection's references

The *references* relationship return the list of ***all references in the Collection***.

This relationship can be retrieved using the [relationships API](https://virustotal.readme.io/reference/get-collections-relationship) endpoint. The response contains a list of [Reference](https://virustotal.readme.io/reference/references) objects.

```json /collections/{id}/references
{
  "data": [
    <REFERENCE_OBJECT>,
    <REFERENCE_OBJECT>,
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
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  },
  "data": [
    {
      "attributes": {
        "last_modification_date": 1611767525,
        "url": "https://www.brighttalk.com/webcast/10703/261205",
        "creation_date": 1495584000,
        "author": "Nick Carr",
        "title": "APT32: New Cyber Espionage Group"
      },
      "type": "reference",
      "id": "14234d82d870c887c83186cdb2c1382650f4bdd9efb79ea7cf2694589d24ae00",
      "links": {
        "self": "https://virustotal.com/api/v3/references/14234d82d870c887c83186cdb2c1382650f4bdd9efb79ea7cf2694589d24ae00"
      }
    }
  ],
  "links": {
    "self": "https://virustotal.com/api/v3/collections/testdata_collection/references?limit=1",
    "next": "https://virustotal.com/api/v3/collections/testdata_collection/references?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D&limit=1"
  }
}
```