# Source: https://virustotal.readme.io/reference/analyses-object.md

# Analyses

Partner contributors' analyses for files and URLs.

An *Analysis* object represents an analysis of a URL or file submitted to VirusTotal, against all our [partnered contributors](https://virustotal.readme.io/docs/contributors).  It's attributes are:

* `date`:  <*integer*> Unix epoch UTC time (seconds).
* `results`: <*dictionary*> dictionary having the engine's name as key and its result as value. Its subfields are:
  * `category`: <*string*> normalised result. Possible values are:
    * "confirmed-timeout" (AV reached a timeout when analysing that file. Only returned in file analyses.)
    * "timeout" (AV reached a timeout when analysing that file.)
    * "failure" (AV failed when analysing this file. Only returned in file analyses).
    * "harmless" (AV thinks the file is not malicious),
    * "undetected" (AV has no opinion about this file),
    * "suspicious" (AV thinks the file is suspicious),
    * "malicious" (AV thinks the file is malicious).
    * "type-unsupported" (AV can't analyse that file. Only returned in file analyses).
  * `engine_name`: <*string*> the engine's name.
  * `engine_update`: <*string*> the engine's update date in `%Y%M%D` format. Only returned in file analyses.
  * `engine_version`: <*string*> the engine's version. Only returned in file analyses.
  * `method`: <*string*> detection method.
  * `result`: <*string*> engine result. If there's no verdict available, it can be `null`.
* `stats`: <*dictionary*> summary of the `results` field. It's subfields are:
  * `confirmed-timeout`: <*integer*> number of AV engines that reach a timeout when analysing that file.
  * `failure`: <*integer*>  number of AV engines that fail when analysing that file.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`: <*integer*> number of timeouts when analysing this URL/file.
  * `type-unsupported`: <*integer*> number of AV engines that don't support that type of file.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `status`: <*string*> analysis status. Possible values are:
  * "completed" (the analysis is finished).
  * "queued" (the item is waiting to be analysed, the analysis object has empty results and stats).
  * "in-progress" (the file is being analysed, the analysis object has partial analysis results and stats).

```json Analysis object
{
  "data": {
    "attributes": {
    	 "date": <int:timestamp>,
       	"results": {
          	"<string>": {
            	"category": "<string>",
            	"engine_name": "<string>",
            	"engine_version": "<string>",
            	"engine_update": "<string>",
            	"method": "<string>",
            	"result": "<string>"
        	},
        	"stats": {
            	"confirmed-timeout": <int>,
           		"failure": <int>,
          		"harmless": <int>,
          		"malicious": <int>,
          		"suspicious": <int>,
          		"timeout": <int>,
           		"type-unsupported": <int>,
          		"undetected": <int>
        	},
        	"status": "<string>"      
    },
    "id": "<string>",
    "type": "analysis"
  }
}
```
```json File analysis example
{
    "data": {
        "attributes": {
            "date": 1591701363,
            "results": {
                "ALYac": {
                    "category": "malicious",
                    "engine_name": "ALYac",
                    "engine_update": "20200609",
                    "engine_version": "1.1.1.5",
                    "method": "blacklist",
                    "result": "Dialer.Webdialer.F"
                },
                "Avast": {
                    "category": "malicious",
                    "engine_name": "Avast",
                    "engine_update": "20200609",
                    "engine_version": "18.4.3895.0",
                    "method": "blacklist",
                    "result": "Win32:Dh-A [Heur]"
                },
                "Avast-Mobile": {
                    "category": "undetected",
                    "engine_name": "Avast-Mobile",
                    "engine_update": "20200609",
                    "engine_version": "200609-00",
                    "method": "blacklist",
                    "result": null
                },
                "CAT-QuickHeal": {
                    "category": "malicious",
                    "engine_name": "CAT-QuickHeal",
                    "engine_update": "20200609",
                    "engine_version": "14.00",
                    "method": "blacklist",
                    "result": "Trojan.Webdial"
                },
                "ClamAV": {
                    "category": "malicious",
                    "engine_name": "ClamAV",
                    "engine_update": "20200608",
                    "engine_version": "0.102.3.0",
                    "method": "blacklist",
                    "result": "Win.Trojan.Dialer-83"
                },
                "Comodo": {
                    "category": "malicious",
                    "engine_name": "Comodo",
                    "engine_update": "20200608",
                    "engine_version": "32518",
                    "method": "blacklist",
                    "result": "Malware@#1o6vtbly4swmm"
                }
            },
            "stats": {
                "confirmed-timeout": 0,
                "failure": 0,
                "harmless": 0,
                "malicious": 5,
                "suspicious": 0,
                "timeout": 0,
                "type-unsupported": 0,
                "undetected": 1
            },
            "status": "in-progress"
        },
        "id": "8zc5dTFiYmMxOTEpNzMzZWZmODE1ND7mYjU1ZjY5Npk6MTU5MlcwMTM2Mw==",
        "type": "analysis"
    }
}
```
```json URL analysis example
{
    "data": {
        "attributes": {
            "date": 1591701032,
            "results": {
                "ADMINUSLabs": {
                    "category": "harmless",
                    "engine_name": "ADMINUSLabs",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AegisLab WebGuard": {
                    "category": "harmless",
                    "engine_name": "AegisLab WebGuard",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AlienVault": {
                    "category": "harmless",
                    "engine_name": "AlienVault",
                    "method": "blacklist",
                    "result": "clean"
                },
                "Antiy-AVL": {
                    "category": "harmless",
                    "engine_name": "Antiy-AVL",
                    "method": "blacklist",
                    "result": "clean"
                },
                "Artists Against 419": {
                    "category": "harmless",
                    "engine_name": "Artists Against 419",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AutoShun": {
                    "category": "undetected",
                    "engine_name": "AutoShun",
                    "method": "blacklist",
                    "result": "unrated"
                },
                "Avira": {
                    "category": "harmless",
                    "engine_name": "Avira",
                    "method": "blacklist",
                    "result": "clean"
                },
                "BADWARE.INFO": {
                    "category": "harmless",
                    "engine_name": "BADWARE.INFO",
                    "method": "blacklist",
                    "result": "clean"
                }
            },
            "stats": {
                "harmless": 7,
                "malicious": 0,
                "suspicious": 0,
                "timeout": 0,
                "undetected": 1
            },
            "status": "completed"
        },
        "id": "u-9d11db1b0q1200ba75016e4c010bc93836366881d021a658ua7f85a8b65c3c1e-1591701032",
        "type": "analysis"
    }
}
```

## Relationships

In addition to the previously described attributes, analyses objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships)  section.

The following table shows a summary of available relationships.

| Relationship | Return object type                                  |
| :----------- | :-------------------------------------------------- |
| item         | A single [file](https://virustotal.readme.io/reference/files) or [URL](https://virustotal.readme.io/reference/url-object) |