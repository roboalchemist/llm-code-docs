# Source: https://virustotal.readme.io/reference/collection-object-owner.md

# 🔀 owner

Collection's owner

The *owner* relationship return the ***owner of the Collection***.

This relationship can be retrieved using the [relationships API](https://virustotal.readme.io/reference/get-collections-relationship) endpoint. The response contains a [User](https://virustotal.readme.io/reference/user-object) object.

```json /collections/{id}/owner
{
  "data": <USER_OBJECT>,
  "links": {
    "self": <string>
  },
  "meta": {
    "count": <int>
  }
}
```
```json Example
{
	"meta": {
		"count": 1
	},
	"data": {
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
	},
	"links": {
		"self": "https://virustotal.com/api/v3/collections/3255c967b5d9866682dd68d2bf181f106659094677076609939be4d70f972b86/owner"
	}
}
```