# Source: https://virustotal.readme.io/reference/file-object-crowdsourced-yara-results.md

# crowdsourced_yara_results

YARA matches from crowdsourced rules.

YARA matches for the file. Every item on the list contains the following attributes:

* `author`: <*string*> rule author.
* `description`: <*string*> matched rule description.
* `match_in_subfile`: <*boolean*> whether the match was in a [subfile](https://virustotal.readme.io/reference/file-object-bundled-files) or not.
* `rule_name`: <*string*> matched rule name.
* `ruleset_id`: <*string*> VirusTotal's ruleset ID. You can use this ID to fetch the ruleset info in the [/api/v3/yara\_rulesets/{id}](https://virustotal.readme.io/reference/get-yara-rulesets) endpoint.
* `ruleset_name`: <*string*> matched rule's ruleset name.
* `source`: <*string*> ruleset source.