# Source: https://documentation.mailgun.com/docs/inboxready/domains-ir.md

# Domains

This section describes domain management for Sinch Optimize products. Use these APIs to register domains for domain-based reputation monitoring tools such as [Spam Trap Monitoring](/docs/inboxready/spam-trap-ir) and [Domain Blocklist Monitoring](/docs/inboxready/domain-blocklist-ir).

## Add Domain

This endpoint allows domains to be registered for reputation monitoring.


```
POST /v1/inboxready/domains
```

The available request fields are as follows:

| Field | Description |
|  --- | --- |
| `domain` | Required. The domain or subdomain that you wish to add. |


Example 200 response:


```JSON
{
  "domain": {
    "ID": "<ID>",
    "created_at": 123456789,
    "name": "example.com",
    "verified": {
      "verified_at": 0,
      "status": "inbox_ready"
    },
    "services": {
      "spam_trap_monitoring": true,
      "domain_blocklist_monitoring": true,
    },
    "txt_record": "<HASHED TXT RECORD KEY>"
  }
}
```

## Get Domains

This endpoint returns a list of domains.


```
GET /v1/inboxready/domains
```

Example 200 response:


```JSON
{
  "items": [
    {
      "ID": "<ID>",
      "created_at": 123456789,
      "name": "example.com",
      "verified": {
        "verified_at": 123456789,
        "status": "inbox_ready"
      },
      "services": {
        "spam_trap_monitoring": true,
        "domain_blocklist_monitoring": true
      },
      "txt_record": "<HASHED TXT RECORD KEY>"
    },
    ...
  ],
  "paging": {
    "previous": "<URL>",
    "first": "<URL>",
    "next": "<URL>",
    "last": "<URL>"
  }
}
```

## Remove Domain

This endpoint can be used to remove a domain from reputation monitoring.


```
DELETE /v1/inboxready/domains
```

The available request fields are as follows:

| Field | Description |
|  --- | --- |
| `domain` | Required. The domain or subdomain that you wish to remove. |


Example 200 response:


```JSON
{
  "message": "example.com has been removed from InboxReady"
}
```