# Source: https://virustotal.readme.io/reference/file-object-sigma-analysis-results.md

# sigma_analysis_results

Sigma results for the file.

List of dictionaries containing aggregated [sigma](https://github.com/SigmaHQ/sigma) analyses results from all sandbox generated EVTX files. Each item contains the following subfields:

* `rule_title`: <*string*> matched sigma rule title.
* `rule_source`: <*string*> sigma ruleset where this rule belongs to.
* `match_context`: <*dictionary*> specific matched events. This dictionary contains the following key:
  * `values`: <*list of map\<str, str>>* all matched events represented as key-value.
* `rule_level`: <*string*> rule level, can be either of "critical", "high", "medium", "low".
* `rule_description`: <*string*> rule description
* `rule_author`: <*string*> rule author
* `rule_id`: <*string*> rule ID in VirusTotal. You can use this to find other files matching this same rule.