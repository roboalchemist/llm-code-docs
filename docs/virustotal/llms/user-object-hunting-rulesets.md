# Source: https://virustotal.readme.io/reference/user-object-hunting-rulesets.md

# 🔀🧑‍💻 hunting_rulesets

Hunting rulesets editable by the user.

The *hunting\_rulesets* relationship returns a list of ***all hunting rulesets editable by a given user***. This relationship is only visible for the account's owner.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/users-relationships) and it returns a list of [Hunting Rulesets](https://virustotal.readme.io/reference/hunting-ruleset-object) objects.

```json /users/{id}/hunting_rulesets
{
  "data": [
    <HUNTING_RULESET_OBJECT>,
    <HUNTING_RULESET_OBJECT>,
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
        "creation_date": 1594997826,
        "enabled": false,
        "limit": 100,
        "modification_date": 1597394885,
        "name": "test",
        "notification_emails": [],
        "number_of_rules": 1,
        "rule_names": [
          "yara_template"
        ],
        "rules": "/*\n    Template YARA ruleset\n*/\nrule yara_template\n{\n    strings:\n        $a = \"VirusTotal\"\n    condition:\n        all of them\n}"
      },
      "id": "0000000000000000",
      "links": {
        "self": "https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/0000000000000000"
      },
      "type": "hunting_ruleset"
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/users/spellman/hunting_rulesets?limit=10"
  },
  "meta": {
    "count": 1
  }
}
```