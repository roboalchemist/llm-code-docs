# Source: https://virustotal.readme.io/reference/rulesets-viewers.md

# 🔀🧑‍💻 viewers

Users and groups that can edit the rules

The *viewers* relationship returns all ***users and groups that can view a ruleset***. This relationship is only visible for the account's owner.

It can be fetched using the [relationships API endpoint](#get-hunting-ruleset-relationship) and it returns a list of [User](https://virustotal.readme.io/reference/user-object) and [Group](https://virustotal.readme.io/reference/group-object) objects.

```json /hunting_rulesets/{id}/editors
{
  "data": [
    <GROUP_OBJECT>,
    <USER_OBJECT>,
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
                "auto_add_users": [],
                "country": "United States",
                "country_iso": "US",
                "domain_name": "blabla.com",
                "industry": "IT",
                "organization": "Company",
                "organization_legal_name": "Company Inc",
                "privileges": {
                    "admin": {
                        "granted": false
                    },
                    "allinfo": {
                        "granted": false
                    },
                    "big-files": {
                        "expiration_date": 1601510400,
                        "granted": true
                    },
                    "cases": {
                        "granted": false
                    },
                    "click_to_accept": {
                        "granted": false
                    }
                },
                "quota_usage_by_user": {},
                "quotas": {
                    "api_requests_daily": {
                        "allowed": 1000,
                        "used": 13
                    },
                    "api_requests_hourly": {
                        "allowed": 60000,
                        "used": 1
                    },
                    "api_requests_monthly": {
                        "allowed": 30000,
                        "used": 104
                    }
                }
            },
            "id": "blabla",
            "links": {
                "self": "https://www.virustotal.com/api/v3/groups/blabla"
            },
            "type": "group"
        },
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/0000000000000000/editors?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```