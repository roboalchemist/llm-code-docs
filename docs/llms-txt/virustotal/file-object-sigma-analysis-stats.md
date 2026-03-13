# Source: https://virustotal.readme.io/reference/file-object-sigma-analysis-stats.md

# sigma_analysis_stats

Sigma analysis stats for the file.

Dictionary containing the number of matched sigma rules, grouped by its severity.

* `critical`: <*integer*> number of matched critical severity rules.
* `high`: <*integer*> number of matched high severity rules.
* `low`: <*integer*> number of matched low severity rules.
* `medium`: <*integer*> number of matched medium severity rules.