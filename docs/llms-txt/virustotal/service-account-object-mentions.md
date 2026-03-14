# Source: https://virustotal.readme.io/reference/service-account-object-mentions.md

# 🔀 mentions

Comments mentioning the user.

The *mentions* relationship returns a list of ***all comments mentioning a given Service Account***.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/users-relationships) and returns a list of [Comment](https://virustotal.readme.io/reference/comments) objects.

```json /users/{user_id}/mentions
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
                "date": 1585745966,
                "html": "@spellman Do you like black cats?",
                "tags": [],
                "text": "@spellman Do you like black cats?",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "f-023238935e73803aa363523a03863c35e736393a139933c9354b3333c3a3b33e-3198f48a",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/f-023238935e73803aa363523a03863c35e736393a139933c9354b3333c3a3b33e-3198f48a"
            },
            "type": "comment"
        },
        {
            "attributes": {
                "date": 1594735512,
                "html": "@spellman it's witching hour!",
                "tags": [],
                "text": "@spellman it's witching hour!",
                "votes": {
                    "abuse": 0,
                    "negative": 0,
                    "positive": 0
                }
            },
            "id": "g-ge312b9e4a9534ec09c3e99b08ef139ef060eb0fe0d6e474eb19e22f3e6de362e-bab27ca0",
            "links": {
                "self": "https://www.virustotal.com/api/v3/comments/g-ge312b9e4a9534ec09c3e99b08ef139ef060eb0fe0d6e474eb19e22f3e6de362e-bab27ca0"
            },
            "type": "comment"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/users/spellman/mentions?limit=10"
    },
    "meta": {
        "count": 2
    }
}
```