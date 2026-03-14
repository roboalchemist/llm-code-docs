# Source: https://virustotal.readme.io/reference/ip-object-user-votes.md

# 🔀🧑‍💻 user_votes

IP address' user votes.

The *votes* relationship returns a list ***containing the votes for a given IP address made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/ip-relationships). The response contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json /ip_addresses/{ip_address}/user_votes
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
```json Example
{
  "meta": {
    "count": 1
  },
  "data": [
    {
      "attributes": {
        "date": 1624368057,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "i-8.8.8.8-2fa03e13",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/i-8.8.8.8-2fa03e13"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/user_votes",
  }
}
```