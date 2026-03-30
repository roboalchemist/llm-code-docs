# Source: https://virustotal.readme.io/reference/graph-group.md

# 🔀 group

Group owning the graph

The *group* relationship returns ***the group owning a given graph***.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/graphs-relationships) and returns a [Group](https://virustotal.readme.io/reference/group-object) object.

```json /graphs/{id}/group
{
  "data": {
    <GROUP_OBJECT>
  },
  "links": {
    "self": "<string>"
  },
  "meta": {
    "count": 1
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "auto_add_users": [],
      "country": "United States",
      "country_iso": "US",
      "domain_name": "blablabla.com",
      "organization": "Company Inc.",
      "preferences": {},
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
      "quotas": {
        "api_requests_daily": {
          "allowed": 99000000,
          "used": 12372
        },
        "api_requests_hourly": {
          "allowed": 3300000,
          "used": 1655
        },
        "api_requests_monthly": {
          "allowed": 2000000000,
          "used": 38910
        },
        "cases_creation_monthly": {
          "allowed": 20,
          "used": 0
        }
      }
    },
    "id": "company",
    "links": {
      "self": "https://www.virustotal.com/api/v3/groups/company"
    },
    "type": "group"
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/graphs/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37/group"
  },
  "meta": {
    "count": 1
  }
}
```