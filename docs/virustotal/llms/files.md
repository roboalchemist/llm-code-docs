# Source: https://virustotal.readme.io/reference/files.md

# Files

Information about files

Files are one of the most important type of objects in the VirusTotal API. We have a huge dataset of more than 2 billion files that have been analysed by VirusTotal over the years. A file object can be obtained either by [uploading a new file](https://virustotal.readme.io/reference/files-scan) to VirusTotal, by [searching for an already existing file hash](https://virustotal.readme.io/reference/file-info) or by other meanings when searching in [VT Enterprise services](https://virustotal.readme.io/reference/search).

A file object ID is its SHA256 hash.

## Object Attributes

In a File object you are going to find some relevant basic attributes about the file and its relationship with VirusTotal, you can find the full list of attributes at [this article](https://virustotal.readme.io/docs/file-attributes-full-list):

* `capabilities_tags`: <*list of strings*> list of representative tags related to the file's capabilities. Only available for Premium API users.
* `creation_date`: <*integer*> extracted when possible from the file's metadata. Indicates when it was built or compiled. It can also be faked by malware creators. UTC timestamp.
* `downloadable`: <*boolean*>  true if the file can be downloaded, false otherwise. Only available for Premium API users.
* `first_submission_date`: <*integer*> date when the file was first seen in VirusTotal. UTC timestamp.
* `last_analysis_date`: <*integer*> most recent scan date. UTC timestamp.
* `last_analysis_results`: <*dictionary*> latest scan results. For more information about its format, check the [Analysis](https://virustotal.readme.io/reference/analyses-object) object `results` attribute.
* `last_analysis_stats`: <*dictionary*> a summary of the latest scan results. For more information about its format, check the [Analysis](https://virustotal.readme.io/reference/analyses-object) object `stats` attribute.
* `last_modification_date`: <*integer*> date when the object itself was last modified. UTC timestamp.
* `last_submission_date`: <*integer*> most recent date the file was posted to VirusTotal. UTC timestamp.
* `main_icon`: <*dictionary*> icon's relevant hashes, the dictionary contains two keys:
  * `raw_md5`: <*string*> icon's MD5 hash.
  * `dhash`: <*string*> icon's difference hash. It can be used to search for files with similar icons using the [/intelligence/search](https://virustotal.readme.io/reference/intelligence-search) endpoint.
* `md5`: <*string*> file's MD5 hash.
* `meaningful_name`: <*string*> the most interesting name out of all file's names.
* `names`: <*list of strings*> all file names associated with the file.
* `reputation`: <*integer*> file's score calculated from all votes posted by the VirusTotal community. To know more about how reputation is calculated, check [this article](https://virustotal.readme.io/docs/community).
* `sandbox_verdicts`: <*dictionary*> A summary of all sandbox verdicts:
  * `category`: <*string*> normalized verdict category. It can be one of `suspicious`, `malicious`, `harmless` or `undetected`.
  * `confidence`: <*integer*> verdict confidence from 0 to 100.
  * `malware_classification`: <*list of strings*> raw sandbox verdicts.
  * `malware_names`: <*list of strings*> malware family names.
  * `sandbox_name`: <*string*> sandbox that provided the verdict.
* `sha1`: <*string*> file's SHA1 hash.
* `sha256`: <*string*> file's SHA256 hash.
* `sigma_analysis_summary`: <*dictionary*> dictionary containing the number of matched sigma rules group by its severity, same as `sigma_analysis_stats` but split by ruleset. Dictionary key is the ruleset name and value is the stats for that specific ruleset.
* `size`: <*integer*> file size in bytes.
* `tags`: <*list of strings*> list of representative attributes.
* `times_submitted`: <*integer*> number of times the file has been posted to VirusTotal.
* `tlsh`: <*string*> file's TLSH hash.
* `permhash`: <*string*> file's Permhash.
* `total_votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious":
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `type_description`: <*string*> describes the file type.
* `type_extension`: <*string*> specifies file extension.
* `type_tag`: <*string*> tag representing the file type. Can be used to filter by file type in [VirusTotal intelligence searches](https://virustotal.readme.io/docs/file-search-modifiers).
* `type_tags`: <*list of strings*> broader tags related to the specific file type, for instance, for a DLL this list would include - executable, windows, win32, pe, pedll. Can be used to filter in [VirusTotal intelligence searches](https://www.virustotal.com/gui/search/type%253Adocument/files), all *typetags get added to the \_type* search modifier.
* `unique_sources`: <*integer*> indicates from how many different sources the file has been posted from.
* `vhash`: <*string*> in-house similarity clustering algorithm value, based on a simple structural feature hash allows you to find similar files.
* `crowdsourced_ai_results` : <*dictionary*> A summary of all crowdsourced ai results:
  * `analysis` : <*string*> Natural language summary of code snippets.
  * `source`: <*string*> result source.
  * `id`: <*string*> id of the crowdsourced\_ai result.
* `threat_verdict`: <*string*>.
  * `VERDICT_UNKNOWN`: we were not able to generate a verdict for this entity.
  * `VERDICT_UNDETECTED`: no immediate evidence of malicious intent.
  * `VERDICT_SUSPICIOUS`: possible malicious activity detected, requires further investigation.
  * `VERDICT_MALICIOUS`: high confidence that the entity poses a threat.
* `threat_severity`: <*dictionary*>.
  * `last_analysis_date`: <*int*> timestamp when the threat severity was calculated.
  * `threat_severity_level`:
    * `SEVERITY_NONE`: this is the level assigned to entities with non-malicious verdict.
    * `SEVERITY_LOW`: the threat likely has a minor impact but should still be monitored
    * `SEVERITY_MEDIUM`: indicates a potential threat that warrants attention.
    * `SEVERITY_HIGH`: immediate action is recommended; the threat could have a critical impact
    * `SEVERITY_UNKNOWN`: not enough data to assess a severity.
  * `level_description`: \<string> a human readable description of the signals that contributed to determine the severity level.
  * `version`: <*int*>
  * `threat_severity_data`: <*dictionary*>
    * `popular_threat_category`: <*string*> Popular\_threat\_category when the severity score was calculated.
    * `type_tag`: <*string*> File type when the severity score was calculated.
    * `has_similar_files_with_detections`: <*bool*> Files similar to this by vhash have detections.
    * `is_matched_by_crowdsourced_yara_with_detections`: <*bool*> At least 1 yara rule matching this file matches other files with detections.
    * `has_vulnerabilities`: <*bool*>  The file is affected by CVE vulnerabilities.
    * `can_be_detonated`: <*bool*> The file has been characterized in sandboxes (behaviour).
    * `has_legit_tag`: <*bool*> The file has the 'legit' tag
    * `num_gav_detections`: <*int*> The number of Google antivirus detections
    * `has_execution_parents_with_detections`: <*bool*> Parent files have detections
    * `has_dropped_files_with_detections`: <*bool*> Dropped files have detections.
    * `has_contacted_ips_with_detections`: <*bool*> Has contacted IPs, domains and URLs with detections.
    * `has_contacted_domains_with_detections`: <*bool*>
    * `has_contacted_urls_with_detections`: <*bool*>
    * `has_embedded_ips_with_detections`: <*bool*> Has embedded IPs with detections.
    * `has_embedded_domains_with_detections`: <*bool*> Has embedded domains with detections.
    * `has_embedded_urls_with_detections`: <*bool*> Has embedded URLs with detections.
    * `has_malware_configs`: <*bool*>
    * `has_references`: <*bool*>
    * `belongs_to_threat_actor`: <*bool*>
    * `belongs_to_bad_collection`: <*bool*>
    * `num_av_detections`: <*int*> Number of regular AV detections if available.
    * `has_bad_sandbox_verdicts`: <*bool*>: The file has been identified as malicious in dynamic analysis.

Additionally VirusTotal together with each Antivirus scan runs a set of tool that allows us to collect more information about the file. All this tool information is included in the "attributes" key, together with the rest of fields previously described. These tools and the data they extract, are documented in the subsections below.

```json "file" object
{
    "data": {
        "attributes": {
          	"capabilities_tags": [
              	"<strings>",....
            ],
            "creation_date": <int:timestamp>,
            "crowdsourced_ids_results": [
                {
                    "alert_context": [
                        {
                            "dest_ip": "<string>",
                            "dest_port": <int>,
                            "hostname": "<string>",
                            "protocol": "<string>",
                            "src_ip": "<string>",
                            "src_port": <int>,
                            "url": "<string>"
                        }
                    ],
                    "alert_severity": "<string>",
                    "rule_category": "<string>",
                    "rule_id": "<string>",
                    "rule_msg": "<string>",
                    "rule_source": "<string>"
                }
            ],
            "crowdsourced_ids_stats": {
                "info": <int>,
                "high": <int>,
                "low": <int>,
                "medium": <int>
            },
            "crowdsourced_yara_results": [
                {
                    "description": "<string>",
                    "match_in_subfile": <boolean>,
                    "rule_name": "<string>",
                    "ruleset_id": "<string>",
                    "ruleset_name": "<string>",
                    "source": "<string>"
                }
            ],
            "downloadable": <bool>,
            "first_submission_date": <int:timestamp>,
            "last_analysis_date": <int:timestamp>,
            "last_analysis_results": {
                "<string:engine_name>": {
                    "category": "<string>",
                    "engine_name": "<string>",
                    "engine_update": "<string>",
                    "engine_version": "<string>",
                    "method": "<string>",
                    "result": "<string>"
                }
            },
            "last_analysis_stats": {
                "confirmed-timeout": <int>,
                "failure": <int>,
                "harmless": <int>,
                "malicious": <int>,
                "suspicious": <int>,
                "timeout": <int>,
                "type-unsupported": <int>,
                "undetected": <int>
            },
            "last_modification_date": <int:timestamp>,
            "last_submission_date": <int:timestamp>,
            "md5": "<string>",
            "meaningful_name": "<string>",
            "names": [
                "<strings>",...
            ],
            "permhash": <str>,
            "reputation": <int>,
            "sandbox_verdicts": {
                "<string:sandbox_name>": {
                    "category": "<string>",
                    "confidence": <int>,
                    "malware_classification": [
                        "<string>"
                    ],
                    "malware_names": [
                        "<string>"
                    ],
                    "sandbox_name": "<string>"
                }
            },
            "sha1": "<string>",
            "sha256": "<string>",
            "sigma_analysis_results": [{
              "rule_title": "<string>",
              "rule_source": "<string>",
              "match_context": [{
                "values": {
                  "<string>": "<string>"}}],
              "rule_level": "<string>",
              "rule_description": "<string>",
              "rule_author": "<string>",
              "rule_id": "<string>"
            }],
            "sigma_analysis_stats": {
                "critical": <int>,
                "high": <int>,
                "low": <int>,
                "medium": <int>
            },
            "sigma_analysis_summary": {
                "<string:ruleset_name>": {
                    "critical": <int>,
                    "high": <int>,
                    "low": <int>,
                    "medium": <int>
                }
            },
            "size": <int>,
            "tags": [
                "<strings>",...
            ],
            "times_submitted": <int>,
            "tlsh": "<string>",
            "total_votes": {
                "harmless": <int>,
                "malicious": <int>
            },
            "type_description": "<string>",
            "type_extension": "<string>",
            "type_tag": "<string>",
            "unique_sources": <int>,
            "vhash": "<string>"
        },
        "id": "<SHA256>",
        "links": {
            "self": "https://www.virustotal.com/ui/files/<SHA256>"
        },
        "type": "file"
    }
}
```
```json Example
{
    "data": {
        "attributes": {
          	"capabilities_tags": [
                "str_win32_internet_api",
                "cred_ff",
                "win_mutex",
                "keylogger",
                "str_win32_winsock2_library",
                "sniff_audio",
                "network_dropper",
                "ldpreload",
                "win_files_operation",
                "str_win32_wininet_library",
                "inject_thread"
            ],
            "creation_date": 1589251011,
            "crowdsourced_ids_results": [
              {
                "alert_context": [
                  {
                    "proto": "TCP",
                    "src_ip": "152.126.25.42",
                    "src_port": 80
                  }
                ],
                "alert_severity": "high",
                "rule_category": "Potential Corporate Privacy Violation",
                "rule_id": "32481",
                "rule_msg": "POLICY-OTHER Remote non-JavaScript file found in script tag src attribute",
                "rule_source": "snort"
               }
            ],
            "crowdsourced_ids_stats": {
                "high": 1,
                "info": 0,
                "low": 0,
                "medium": 0
             },
            "crowdsourced_yara_results": [
                {
                    "description": "Detects a very evil attack",
                    "match_in_subfile": true,
                    "rule_name": "evil_a_b",
                    "ruleset_id": "000abc43",
                    "ruleset_name": "evilness",
                    "source": "https://example.com/evil/ruleset"
                }
            ],
            "downloadable": true,
            "first_submission_date": 1592134853,
            "last_analysis_date": 1592141610,
            "last_analysis_results": {
                "ALYac": {
                    "category": "malicious",
                    "engine_name": "ALYac",
                    "engine_update": "20200614",
                    "engine_version": "1.1.1.5",
                    "method": "blacklist",
                    "result": "Trojan.GenericKDZ.67102"
                },
                "APEX": {
                    "category": "malicious",
                    "engine_name": "APEX",
                    "engine_update": "20200613",
                    "engine_version": "6.36",
                    "method": "blacklist",
                    "result": "Malicious"
                },
                "AVG": {
                    "category": "malicious",
                    "engine_name": "AVG",
                    "engine_update": "20200614",
                    "engine_version": "18.4.3895.0",
                    "method": "blacklist",
                    "result": "Win32:PWSX-gen [Trj]"
                },
                "Acronis": {
                    "category": "undetected",
                    "engine_name": "Acronis",
                    "engine_update": "20200603",
                    "engine_version": "1.1.1.76",
                    "method": "blacklist",
                    "result": null
                }
            },
            "last_analysis_stats": {
                "confirmed-timeout": 0,
                "failure": 0,
                "harmless": 0,
                "malicious": 3,
                "suspicious": 0,
                "timeout": 0,
                "type-unsupported": 0,
                "undetected": 2
            },
            "last_modification_date": 1592141790,
            "last_submission_date": 1592141610,
            "md5": "5a430646b4d3c04f0b43b444ad48443f",
            "meaningful_name": "o4oz44Z4E444.exe",
            "names": [
                "myfile.exe",
                "o4oz44Z4E444.exe"
            ],
            "reputation": 0,
            "sandbox_verdicts": {
                "VirusTotal Jujubox": {
                    "category": "malicious",
                    "confidence": 70,
                    "malware_classification": [
                        "MALWARE",
                        "TROJAN"
                    ],
                    "malware_names": [
                        "XMRigMiner"
                    ],
                    "sandbox_name": "VirusTotal Jujubox"
                },
            },
            "sha1": "54fdf53af86f90bf446f0a5fe26f6e4fd5f4c9fd",
            "sha256": "3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf",
			"sigma_analysis_summary": {
				"Sigma Integrated Rule Set (GitHub)": {
					"high": 0,
					"medium": 0,
					"critical": 0,
					"low": 1
				},
				"SOC Prime Threat Detection Marketplace": {
					"high": 1,
					"medium": 0,
					"critical": 0,
					"low": 0
				}
			},
			"sigma_analysis_stats": {
				"high": 1,
				"medium": 0,
				"critical": 0,
				"low": 1
			},
			"sigma_analysis_results": [
				{
					"rule_title": "File deletion via CMD (via cmdline)",
					"rule_source": "SOC Prime Threat Detection Marketplace",
					"match_context": [
						{
							"values": {
								"TerminalSessionId": "0",
								"ProcessGuid": "C784477D-ED34-629E-4105-000000003000",
								"ProcessId": "4164",
								"Product": "Microsoft® Windows® Operating System",
								"Description": "Windows Command Processor",
								"Company": "Microsoft Corporation",
								"ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
								"User": "NT AUTHORITY\\SYSTEM",
								"Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
								"OriginalFileName": "Cmd.Exe",
								"ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
								"FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
								"ParentProcessId": "5204",
								"CurrentDirectory": "C:\\Windows\\system32\\",
								"CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\ipconfig.exe /flushdns >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
								"EventID": "1",
								"LogonGuid": "C784477D-EC60-629E-E703-000000000000",
								"LogonId": "999",
								"Image": "C:\\Windows\\System32\\cmd.exe",
								"IntegrityLevel": "System",
								"ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
								"UtcTime": "2022-06-07 06:16:20.702",
								"RuleName": "-"
							}
						},
						{
							"values": {
								"TerminalSessionId": "0",
								"ProcessGuid": "C784477D-ED34-629E-4405-000000003000",
								"ProcessId": "1368",
								"Product": "Microsoft® Windows® Operating System",
								"Description": "Windows Command Processor",
								"Company": "Microsoft Corporation",
								"ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
								"User": "NT AUTHORITY\\SYSTEM",
								"Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
								"OriginalFileName": "Cmd.Exe",
								"ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
								"FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
								"ParentProcessId": "5204",
								"CurrentDirectory": "C:\\Windows\\system32\\",
								"CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\netsh.exe interface ip delete arpcache >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
								"EventID": "1",
								"LogonGuid": "C784477D-EC60-629E-E703-000000000000",
								"LogonId": "999",
								"Image": "C:\\Windows\\System32\\cmd.exe",
								"IntegrityLevel": "System",
								"ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
								"UtcTime": "2022-06-07 06:16:20.741",
								"RuleName": "-"
							}
						}
					],
					"rule_level": "high",
					"rule_description": "Detects \"cmd\" utilization to self-delete files in some critical Windows destinations.",
					"rule_author": "Ariel Millahuel",
					"rule_id": "f9333cf120369debd56e4e238fffa10bdb2a1497c11e08a082befd02f9f3bdf2"
				},
				{
					"rule_title": "Failed Code Integrity Checks",
					"rule_source": "Sigma Integrated Rule Set (GitHub)",
					"match_context": [
						{
							"values": {
								"EventID": "5038",
								"param1": "\\Device\\HarddiskVolume4\\Program Files (x86)\\sandbox\\driver\\sandbox-driver.sys"
							}
						}
					],
					"rule_level": "low",
					"rule_description": "Code integrity failures may indicate tampered executables.",
					"rule_author": "Thomas Patzke",
					"rule_id": "134564d292d785dff102940b8a1ee06dba2d462c5fb852124b3771a49d7885f1"
				}
			],
            "size": 374272,
            "tags": [
                "peexe",
                "runtime-modules",
                "assembly",
                "direct-cpu-clock-access",
                "detect-debug-environment"
            ],
            "times_submitted": 3,
            "total_votes": {
                "harmless": 0,
                "malicious": 0
            },
            "type_description": "Win32 EXE",
            "type_tag": "exe",
            "type_tag": "peexe",
            "unique_sources": 3,
            "vhash": "2350f6f515f29f93f147f0f0"
        },
        "id": "3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf",
        "links": {
            "self": "https://www.virustotal.com/ui/files/3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf"
        },
        "type": "file"
    }
}
```

## Relationships

In addition to the previously described attributes (and the ones described in the following subsections), File objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships for file objects.

| Relationship             | Description                                                                       | Accessibility                                     | Return object type                                      |
| :----------------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------ | :------------------------------------------------------ |
| analyses                 | Analyses for the file                                                             | VT Enterprise users only                          | A list of [Analyses](https://virustotal.readme.io/reference/analyses-object)               |
| behaviours               | Behaviour reports for the file. See [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary). | Everyone                                          | A list of [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary). |
| bundled\_files           | Files bundled within the file.                                                    | Everyone                                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| carbonblack\_children    | Files derived from the file according to Carbon Black.                            | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| carbonblack\_parents     | Files from where the file was derived according to Carbon Black.                  | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| ciphered\_bundled\_files | Files within a ciphered bundle.                                                   | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| ciphered\_parents        | Compressed bundle files where a file is contained.                                | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| collections              | Collections where the file is present.                                            | Everyone                                          | A list of [Collections](https://virustotal.readme.io/reference/collections-object)         |
| comments                 | Comments for the file.                                                            | Everyone                                          | A list of [Comments](https://virustotal.readme.io/reference/comments).                     |
| compressed\_parents      | Compressed files that contain the file.                                           | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| contacted\_domains       | Domains contacted by the file.                                                    | Everyone                                          | A list of [Domains](https://virustotal.readme.io/reference/domains-object).                |
| contacted\_ips           | IP addresses contacted by the file.                                               | Everyone                                          | A list of [IP addresses](https://virustotal.readme.io/reference/ip-object).                |
| contacted\_urls          | URLs contacted by the file.                                                       | Everyone                                          | A list of [URLs](https://virustotal.readme.io/reference/url-object).                       |
| dropped\_files           | Files dropped by the file during its execution.                                   | Everyone                                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| email\_attachments       | Files attached to the email.                                                      | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| email\_parents           | Email files that contained the file.                                              | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| embedded\_domains        | Domain names embedded in the file.                                                | VT Enterprise users only                          | A list of [Domains](https://virustotal.readme.io/reference/domains-object).                |
| embedded\_ips            | IP addresses embedded in the file.                                                | VT Enterprise users only                          | A list of [IP addresses](https://virustotal.readme.io/reference/ip-object).                |
| embedded\_urls           | URLs embedded in the file.                                                        | VT Enterprise users only                          | A list of [URLs](https://virustotal.readme.io/reference/url-object).                       |
| execution\_parents       | Files that executed the file.                                                     | Everyone                                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| graphs                   | Graphs that include the file.                                                     | Everyone                                          | A list of [Graphs](https://virustotal.readme.io/reference/graph-object).                   |
| itw\_domains             | In the wild domain names from where the file has been downloaded.                 | VT Enterprise users only                          | A list of [Domains](https://virustotal.readme.io/reference/domains-object).                |
| itw\_ips                 | In the wild IP addresses from where the file has been downloaded.                 | VT Enterprise users only                          | A list of [IP addresses](https://virustotal.readme.io/reference/ip-object).                |
| itw\_urls                | In the wild URLs from where the file has been downloaded.                         | VT Enterprise users only                          | A list of [URLs](https://virustotal.readme.io/reference/url-object).                       |
| memory\_pattern\_domains | Domain names in the memory pattern of the file.                                   | VT Enterprise users only.                         | A list of [Domains](https://virustotal.readme.io/reference/domains-object).                |
| memory\_pattern\_ips     | IP addresses in the memory pattern of the file.                                   | VT Enterprise users only.                         | A list of [IP addresses](https://virustotal.readme.io/reference/ip-object).                |
| memory\_pattern\_urls    | URLs in the memory pattern of the file.                                           | VT Enterprise users only.                         | A list of [URLs](https://virustotal.readme.io/reference/url-object).                       |
| overlay\_children        | Files contained by the file as an overlay.                                        | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| overlay\_parents         | File that contain the file as an overlay.                                         | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| pcap\_children           | Files contained within the PCAP file.                                             | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| pcap\_parents            | PCAP files that contain the file.                                                 | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| pe\_resource\_children   | Files contained by a PE file as a resource.                                       | Everyone                                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| pe\_resource\_parents    | PE files containing the file as a resource.                                       | Everyone                                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| related\_references      | References related to the file.                                                   | VT Enterprise users with Threat Landscape **(1)** | A list of [References](https://virustotal.readme.io/reference/references).                 |
| related\_threat\_actors  | Threat actors related to the file.                                                | VT Enterprise users with Threat Landscape **(1)** | A list of [Threat Actors](https://virustotal.readme.io/reference/threat-actors-object).    |
| similar\_files           | Files that are similar to the file.                                               | VT Enterprise users only                          | A list of [Files](https://virustotal.readme.io/reference/files).                           |
| submissions              | Submissions for the file.                                                         | VT Enterprise users only                          | A list of [Submissions](https://virustotal.readme.io/reference/submission-object).         |
| screenshots              | Screenshots related to the sandbox execution of the file.                         | VT Enterprise users only                          | A list of [Screenshots](https://virustotal.readme.io/reference/screenshots).               |
| urls\_for\_embedded\_js  | URLs where a given JS script is embedded.                                         | VT Enterprise users only                          | A list of [URLs](https://virustotal.readme.io/reference/url-object).                       |
| votes                    | Votes for the file.                                                               | Everyone                                          | A list of [Votes](https://virustotal.readme.io/reference/vote-object).                     |

**(1)** This endpoint requires you to have access to the Threat Landscape module, which only comes with our top packages