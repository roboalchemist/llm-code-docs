# Source: https://virustotal.readme.io/reference/yara-rulesets.md

# YARA Rulesets

YARA rulesets objects

A YARA Ruleset object represents one of the rulesets used in our crowdsourced YARA results. It has the following attributes:

* `name`: <*string*> ruleset name.
* `rules`: <*string*> string containing the ruleset file.
* `source`: <*string*> repository the ruleset was downloaded from.

```json YARA ruleset object
{
  "data": {
    "attributes": {
      "name": "<string>",
      "rules": "<string>",
      "source": "<string>"
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/yara_rulesets/<id>"
    },
    "type": "yara_ruleset"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "name": "evilness",
      "rules": "/*\n    Template YARA ruleset\n*/\nrule yara_template\n{\n    strings:\n        $a = \"VirusTotal\"\n    condition:\n        all of them\n}",
      "source": "https://example.com/evil/ruleset"
    },
    "id": "000abc43",
    "links": {
      "self": "https://www.virustotal.com/api/v3/yara_rulesets/000abc43"
    },
    "type": "yara_ruleset"
  }
}
```

## Relationships

In addition to the previously described attributes, YARA rulesets objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships for YARA rulesets objects.

| Relationship | Description                                       | Accessibility | Return object typ                     |
| :----------- | :------------------------------------------------ | :------------ | :------------------------------------ |
| yara\_rules  | Returns all YARA rules contained in this ruleset. | Everyone.     | A list of [YARA Rules](https://virustotal.readme.io/reference/yara-rule) |