# Source: https://virustotal.readme.io/reference/rulesets-owner.md

# 🔀 🧑‍💻owner

Collection's owner

The *owner* relationship returns the ***owner of the ruleset***.

This relationship can be retrieved using the [relationships API](https://virustotal.readme.io/reference/get-hunting-ruleset-full-relationships) endpoint. The response contains a [User](https://virustotal.readme.io/reference/user-object) object.

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
		"self": "https://virustotal.com/api/v3/hunting_rulesets/11245226372/owner"
	}
}
```