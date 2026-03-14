# Source: https://virustotal.readme.io/reference/comment-object-author.md

# 🔀 author

Comment votes.

The *author* relationship returns a dictionary ***containing the author for a given comment***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/comments-relationships). The response contains the deatils of the comment's author.

```json /comments/{comment_id}/author
{
  "data": [
  	<AUTHOR_OBJECT>,
  ],
  "links": {
    "next": "<string>",
  },
  "meta": {
    	"count": <int>
  }
}
```
```json Example
{
    "links": {
        "self": "https://www.virustotal.com/api/v3/comments/f-8ebc97e05c8e1073bda2efb6f4d00ad7e789260afa2c276f0c72740b838a0a93-5a3e38e3/author"
    },
    "meta": {
        "count": 1
    },
    "data": {
        "id": "userid",
        "type": "user",
        "links": {
            "self": "https://www.virustotal.com/api/v3/users/userid"
        },
        "attributes": {
            "profile_phrase": "",
            "last_name": "LastNAme",
            "reputation": 1,
            "user_since": 1551688503,
            "first_name": "FirstName",
            "collections_count": 1,
            "certified": false,
            "status": "active"
        }
    }
}
```