# Source: https://virustotal.readme.io/reference/service-account-object-comments.md

# 🔀 comments

Comments posted by a certain user

The *comments* relationship returns a list of ***all comments posted by a certain Service Account***.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/users-relationships) and contains a list of [Comment](https://virustotal.readme.io/reference/comments) objects.

```json /users/{user_id}/comments
{
  "data": [
    <COMMENT_OBJECT>
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
                "date": 1593902009,
                "html": "#spam #malware",
                "tags": [],
                "text": "#spam #malware",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "d-spamverybad.com-905fd26e",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/d-spamverybad-905fd26e"
            },
            "type": "comment"
        },
        {
            "attributes": {
                "date": 1560708145,
                "html": "is this a false positive?<br />",
                "tags": [],
                "text": "is this a false positive?\n",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "f-cb3c63183c53153833c53b93e5c3e2e315b30c0e3314833d77231bab37e8c33a-a3a313c8",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/f-cb3c63183c53153833c53b93e5c3e2e315b30c0e3314833d77231bab37e8c33a-a3a313c8"
            },
            "type": "comment"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/users/spellman/comments?limit=10"
    },
    "meta": {
        "count": 2
    }
}
```