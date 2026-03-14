# Source: https://virustotal.readme.io/reference/user-object-votes.md

# 🔀 votes

Votes posted by a certain user

The *votes* relationship returns a list of ***all votes posted by a certain user***.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/users-relationships) and contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json /users/{user_id}/votes
{
  "data": [
    <VOTE_OBJECT>
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
		"count": 3,
		"cursor": "Cl4SWGoRc352aXJ1c3RvdGFsY2xvdWRyQwsSBkRvbWFpbiISd3d3LnZpcnVzdG90YWwuY29tDAsSBFZvdGUiG3d3dy52aXJ1c3RvdGFsLmNvbS1lNmJjNjcwOAwYACAA"
	},
	"data": [
		{
			"attributes": {
				"date": 1623250000,
				"verdict": "harmless",
				"value": 1
			},
			"type": "vote",
			"id": "d-www.virustotal.com-abcdef012",
			"links": {
				"self": "https://www.virustotal.com/api/v3/votes/d-www.virustotal.com-abcdef012"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/users/wcoyote/votes?limit=1",
		"next": "https://www.virustotal.com/api/v3/users/wcoyote/votes?cursor=Cl4SWGoRc352aXJ1c3RvdGFsY2xvdWRyQwsSBkRvbWFpbiISd3d3LnZpcnVzdG90YWwuY29tDAsSBFZvdGUiG3d3dy52aXJ1c3RvdGFsLmNvbS1lNmJjNjcwOAwYACAA&limit=1"
	}
}
```