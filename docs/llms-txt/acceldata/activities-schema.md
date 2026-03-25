# Source: https://docs.acceldata.io/api/activities-schema.md

# Activities Schema

Returned by [Activities (Votes & Comments)](https://docs.acceldata.io/acceldata-data-observability-cloud/api/activities--votes---comments-).

## Top-level Fields

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| upVoteCount | integer | Total upvotes | 12 | 
| downVoteCount | integer | Total downvotes | 3 | 
| upvoted | boolean | User upvoted? | true | 
| downvoted | boolean | User downvoted? | false | 
| comments | array | User comments | — | 


## Nested: comments[]

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| comment | string | Comment text | Dataset is reliable | 
| userName | string | Commenter name | Alice | 


## Example JSON

```json
{ 
  "upVoteCount": 12, 
  "comments": 
  	[
      { "comment": "Dataset is reliable", 
       "userName": "Alice" 
      }
    ] 
}
```

