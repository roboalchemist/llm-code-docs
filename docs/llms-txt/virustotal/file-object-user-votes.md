# Source: https://virustotal.readme.io/reference/file-object-user-votes.md

# 🔀🧑‍💻 user_votes

Votes for a given file made by the current user

The *votes* relationship returns a list ***containing the votes for a given file made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/files-relationships). The response contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json /files/{file_hash}/user_votes
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
        "date": 1592125710,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de/user_votes"
  }
}
```