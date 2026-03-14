# Source: https://virustotal.readme.io/reference/file-object-sandbox-verdicts.md

# sandbox_verdicts

Sandbox verdicts for the file.

A summary of all sandbox verdicts for a given file. It's a dictionary, where each key is the sandbox name and each value is a dictionary containing the following keys:

* `category`: <*string*> normalized verdict category. It can be one of `suspicious`, `malicious`, `harmless` or `undetected`.
* `confidence`: <*integer*> verdict confidence from 0 to 100.
* `malware_classification`: <*list of strings*> raw sandbox verdicts.
* `malware_names`: <*list of strings*> malware family names.
* `sandbox_name`: <*string*> sandbox that provided the verdict.