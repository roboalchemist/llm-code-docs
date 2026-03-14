# Source: https://virustotal.readme.io/reference/url-object-votes.md

# 🔀 votes

Votes for a given URL

The *votes* relationship returns a list ***containing the votes for a given URL***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/urls-relationships). The response contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json /urls/{url_id}/votes
{
  "data": [
  	<VOTE_OBJECT>,
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
    "count": 200,
    "cursor": "CswBChEKBGRhdGUSCQiJzeySu6bxAhKyAWoRc352aXJ1c3RvdGFsY2xvdWRynAELEgNVUkwiQGQwZTE5NmEwYzI1ZDM1ZGQwYTg0NTkzY2JhZTBmMzgzMzNhYTU4NTI5OTM2NDQ0ZWEyNjQ1M2VhYjI4ZGZjODYMCxIEVm90ZSJJZDBlMTk2YTBjMjVkMzVkZDBhODQ1OTNjYmFlMGYzODMzM2FhNTg1Mjk5MzY0NDRlYTI2NDUzZWFiMjhkZmM4Ni0xOGFmMDNmZAwYACAB"
  },
  "data": [
    {
      "attributes": {
        "date": 1624356005,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-b6f95068",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-b6f95068"
      }
    },
    {
      "attributes": {
        "date": 1624200709,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-18af03fd",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-18af03fd"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/urls/d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86/votes?limit=2",
    "next": "https://www.virustotal.com/api/v3/urls/d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86/votes?cursor=CswBChEKBGRhdGUSCQiJzeySu6bxAhKyAWoRc352aXJ1c3RvdGFsY2xvdWRynAELEgNVUkwiQGQwZTE5NmEwYzI1ZDM1ZGQwYTg0NTkzY2JhZTBmMzgzMzNhYTU4NTI5OTM2NDQ0ZWEyNjQ1M2VhYjI4ZGZjODYMCxIEVm90ZSJJZDBlMTk2YTBjMjVkMzVkZDBhODQ1OTNjYmFlMGYzODMzM2FhNTg1Mjk5MzY0NDRlYTI2NDUzZWFiMjhkZmM4Ni0xOGFmMDNmZAwYACAB&limit=2"
  }
}
```