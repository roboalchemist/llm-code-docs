# Source: https://virustotal.readme.io/reference/group-administrators.md

# 🔀🧑‍💻 administrators

Users administrating the group

The *administrators* relationship returns all ***users administrating a given group***. This relationship is only visible for the groups members.

It can be fetched using the [relationships API endpoint](https://virustotal.readme.io/reference/groups-relationships) and it returns a list of [User](https://virustotal.readme.io/reference/user-object) objects.

```json /groups/{id}/administrators
{
  "data": [
    <USER_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
  "data": [
    {
      "attributes": {
        "first_name": "Salem",
        "last_name": "Spellman",
        "profile_phrase": "Meow",
        "reputation": 1,
        "status": "active",
        "user_since": 1557214525
      },
      "id": "salem",
      "links": {
        "self": "https://www.virustotal.com/api/v3/users/salem"
      },
      "type": "user"
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/groups/spellmans/administrators?limit=10"
  },
  "meta": {
    "count": 1
  }
}
```