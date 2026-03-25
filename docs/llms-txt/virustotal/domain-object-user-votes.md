# Source: https://virustotal.readme.io/reference/domain-object-user-votes.md

# 🔀🧑‍💻 user_votes

Domain's user votes.

The *votes* relationship returns a list ***containing the votes for a given domain made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/domains-relationships). The response contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json
{
  "data": [
  	<VOTE_OBJECT>
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
```json
{
  "meta": {
    "count": 1
  },
  "data": [
    {
      "attributes": {
        "date": 1623254696,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "d-www.virustotal.com-e6bc6708",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/d-www.virustotal.com-e6bc6708"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/domains/www.virustotal.com/user_votes"
  }
}
```