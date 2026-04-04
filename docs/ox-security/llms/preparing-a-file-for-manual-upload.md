# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/importing-issues-from-external-files/preparing-a-file-for-manual-upload.md

# Preparing a File for Manual Upload

The `OxThirdPartyIssue` interface is a template for creating a structured report about issues found in third-party apps.

The schema must include the `name` field that identifies the origin of the uploaded issues. The name you provide in this field is used after scan, when filtering the issues to view the imported issues in OX.

The interface is flexible, so you can report as much or as little as you know, as follows:

* **Required fields:** You must fill in.
* **Optional fields:** You add to the file only if you have the relevant information.

```
// interface OxThirdPartyIssue {
  reportId: string;
  dateGenerated: string;
  testerInfo: {
    name: string;
    email: string;
  };
  applications: Array<{
    name: string;
    tags?: string[];
    findings: Array<{
      id: string;
      title: string;
      severity: string;
      summary?: string;
      impact?: string;
      recommendation?: string;
      reference?: string;
      linkToExternalProduct?: string;
      libraryName?: string;
      libraryVersion?: string;
      assets?: Array<{
        filePath: string;
        snippet?: string;
        artifacts?: Array<{
          name: string;
          tags: string[];
          sha: string;
          region: string;
        }>;
      }>;
      vulnerabilities?: Array<{
        cve: string;
        cvssScore?: string;
        cvssVersion?: string;
        cveDescription?: string;
        epss?: string;
        percentile?: string;
        kev?: boolean;
        publishedExploitDate?: string;
        hasPublicExploit?: boolean;
        publicExploitLink?: string;
        attackVector?: string;
      }>;
      severityFactorsPerIssue?: Array<{
        name: string;
        type: "Exploitable"|"Reachable"|"Damage"
      }>;
    }>;
  }>;
}
```

## General info

<table><thead><tr><th width="158.66668701171875">Field</th><th>Type</th><th width="107.3333740234375">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>reportId</code></td><td>string</td><td>Required</td><td>Unique ID for the report</td></tr><tr><td><code>dateGenerated</code></td><td>string</td><td>Required</td><td>Date the report was created</td></tr><tr><td><code>testerInfo.name</code></td><td>string</td><td>Required</td><td>Name of the tester</td></tr><tr><td><code>testerInfo.email</code></td><td>string</td><td>Required</td><td>Email of the tester</td></tr></tbody></table>

## Applications

The following table presents the information about the applications that were tested and in which the issues were found.

| Field      | Type      | Required | Description                                      |
| ---------- | --------- | -------- | ------------------------------------------------ |
| `name`     | string    | Required | Name of the app                                  |
| `tags`     | string\[] | Optional | Labels for the app, for examle “web”, “finance”) |
| `findings` | array     | Required | List of issues found in the app                  |

## Findings

The following table presents the information about the problems that were identified in the applications.

| Field                   | Type   | Required | Description                             |
| ----------------------- | ------ | -------- | --------------------------------------- |
| `id`                    | string | Required | Unique ID for the issue                 |
| `title`                 | string | Required | Short name of the issue                 |
| `severity`              | string | Required | Severity level (e.g., “High”)           |
| `summary`               | string | Optional | Short explanation of the issue          |
| `impact`                | string | Optional | Why this issue is bad                   |
| `recommendation`        | string | Optional | Suggested fix                           |
| `reference`             | string | Optional | Link to more info/documentation         |
| `linkToExternalProduct` | string | Optional | Link to the tool/report that found this |
| `libraryName`           | string | Optional | Name of the software library involved   |
| `libraryVersion`        | string | Optional | Version of the library                  |

## Assets

The following table presents the information about the files/code affected by the issue, if such exist. This section is optional in case no files were damaged.

| Field       | Type   | Required | Description                           |
| ----------- | ------ | -------- | ------------------------------------- |
| `filePath`  | string | Required | File location where issue appears     |
| `snippet`   | string | Optional | Small piece of code showing the issue |
| `artifacts` | array  | Optional | Additional details                    |

## Artifacts

The following table presents the information about the additional info inside the affected file.

| Field    | Type      | Required | Description                             |
| -------- | --------- | -------- | --------------------------------------- |
| `name`   | string    | Required | Name of the artifact                    |
| `tags`   | string\[] | Required | Tags describing the artifact            |
| `sha`    | string    | Required | Unique identifier (digital fingerprint) |
| `region` | string    | Required | Region/location in the file             |

## Vulnerabilities

The following table presents the information that is included only in case the issue is linked to a known security flaw, for example, a CVE.

<table><thead><tr><th width="148.66668701171875">Field</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>cve</code></td><td>string</td><td>Required</td><td>CVE ID (e.g. "CVE-2024-0001")</td></tr><tr><td><code>cvssScore</code></td><td>string</td><td>Optional</td><td>Severity score (0–10)</td></tr><tr><td><code>cvssVersion</code></td><td>string</td><td>Optional</td><td>Version of the scoring system</td></tr><tr><td><code>cveDescription</code></td><td>string</td><td>Optional</td><td>Description of the vulnerability</td></tr><tr><td><code>epss</code></td><td>string</td><td>Optional</td><td>Likelihood of exploitation</td></tr><tr><td><code>percentile</code></td><td>string</td><td>Optional</td><td>How this compares to other CVEs</td></tr><tr><td><code>kev</code></td><td>boolean</td><td>Optional</td><td>Is it a Known Exploited Vulnerability?</td></tr><tr><td><code>publishedExploitDate</code></td><td>string</td><td>Optional</td><td>When an exploit became public</td></tr><tr><td><code>hasPublicExploit</code></td><td>boolean</td><td>Optional</td><td>Is there public code to attack it?</td></tr><tr><td><code>publicExploitLink</code></td><td>string</td><td>Optional</td><td>Link to exploit code</td></tr><tr><td><code>attackVector</code></td><td>string</td><td>Optional</td><td>How the attack works (e.g. "Network")</td></tr></tbody></table>

## Severity factors

The following table presents the information that explains why this issue is considered severe.

| Field  | Type   | Required | Description                                    |
| ------ | ------ | -------- | ---------------------------------------------- |
| `name` | string | Required | Name of the factor (e.g. "Remote Execution")   |
| `type` | string | Required | Type/category (e.g. "Security", "Performance") |

## Example of a file for manual upload

```
//  {
  "reportId": "RPT-20250730-001",
  "dateGenerated": "2025-07-30",
  "testerInfo": {
    "name": "Alice Green",
    "email": "alice.green@example.com"
  },
  "applications": [
    {
      "name": "FinanceApp",
      "tags": ["financial", "web", "production"],
      "findings": [
        {
          "id": "FIN-001",
          "title": "Outdated jQuery Version",
          "severity": "High",
          "summary": "jQuery 1.7.2 is outdated and vulnerable to known attacks.",
          "impact": "May allow XSS and other vulnerabilities.",
          "recommendation": "Upgrade to jQuery 3.x or later.",
          "reference": "https://snyk.io/vuln/npm:jquery",
          "linkToExternalProduct": "https://tracker.example.com/issue/FIN-001",
          "libraryName": "jquery",
          "libraryVersion": "1.7.2",
          "assets": [
            {
              "filePath": "public/js/vendor/jquery.js",
              "snippet": "/*! jQuery v1.7.2 | (c) 2012 jQuery Foundation */",
              "artifacts": [
                {
                  "name": "jquery.js",
                  "tags": ["library", "javascript"],
                  "sha": "abc123def456",
                  "region": "us-east-1"
                },
                {
                  "name": "jquery.min.js",
                  "tags": ["minified", "production"],
                  "sha": "xyz789ghi012",
                  "region": "us-west-2"
                }
              ]
            },
            {
              "filePath": "public/js/vendor/maxim.js",
              "snippet": "/*! jQuery v1.7.2 | (c) 2012 jQuery Foundation */",
              "artifacts": [
                {
                  "name": "jquery.js",
                  "tags": ["library", "javascript"],
                  "sha": "abc123def456",
                  "region": "us-east-1"
                },
                {
                  "name": "jquery.min.js",
                  "tags": ["minified", "production"],
                  "sha": "xyz789ghi012",
                  "region": "us-west-2"
                }
              ]
            }
          ],
          "vulnerabilities": [
            {
              "cve": "CVE-2012-6708",
              "cvssScore": "6.1",
              "cvssVersion": "3.1",
              "cveDescription": "XSS in jQuery 1.7.2 via input manipulation.",
              "epss": "0.91",
              "percentile": "99.7",
              "kev": true,
              "publishedExploitDate": "2017-05-12",
              "hasPublicExploit": true,
              "publicExploitLink": "https://www.exploit-db.com/exploits/38269",
              "attackVector": "Network"
            },
            {
              "cve": "CVE-2015-9251",
              "cvssScore": "6.1",
              "cvssVersion": "3.0",
              "cveDescription": "XSS vulnerability due to improper sanitization.",
              "epss": "0.88",
              "percentile": "98.1",
              "kev": false,
              "publishedExploitDate": "2018-02-27",
              "hasPublicExploit": true,
              "publicExploitLink": "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
              "attackVector": "Network"
            }
          ],
          "severityFactorsPerIssue": [
            {
              "name": "Weak Entropy Source",
              "type": "Damage"
            },
            {
              "name": "Used in Token Generation",
              "type": "Reachable"
            }
          ]
        },
        {
          "id": "FIN-002",
          "title": "Hardcoded Credentials",
          "severity": "Critical",
          "summary": "Hardcoded database credentials found in source code.",
          "impact": "May allow attackers to access database.",
          "recommendation": "Remove hardcoded credentials and use environment variables.",
          "assets": [
            {
              "filePath": "config/database.js",
              "snippet": "const password = 'dbadmin123';",
              "artifacts": [
                {
                  "name": "database.js",
                  "tags": ["config", "sensitive"],
                  "sha": "d3adb33f",
                  "region": "eu-central-1"
                },
                {
                  "name": "backup-database.js",
                  "tags": ["backup", "deprecated"],
                  "sha": "feedface",
                  "region": "eu-west-1"
                }
              ]
            }
          ],
          "severityFactorsPerIssue": [
            {
              "name": "Weak Entropy Source",
              "type": "Damage"
            },
            {
              "name": "Used in Token Generation",
              "type": "Reachable"
            }
          ]
        },
        {
          "id": "LOGI-003",
          "title": "Use of Insecure Random Generator",
          "severity": "Medium",
          "summary": "The `Math.random()` function is used to generate session tokens.",
          "impact": "Predictable session IDs can lead to session hijacking.",
          "recommendation": "Use a cryptographically secure random number generator.",
          "assets": [
            {
              "filePath": "src/utils/token.js",
              "snippet": "return Math.random().toString(36).substring(2);",
              "artifacts": [
                {
                  "name": "token.js",
                  "tags": ["auth", "token"],
                  "sha": "cafebabe",
                  "region": "us-west-1"
                },
                {
                  "name": "legacy-token.js",
                  "tags": ["deprecated"],
                  "sha": "facefeed",
                  "region": "us-east-2"
                }
              ]
            },
            {
              "filePath": "src/security/session.js",
              "snippet": "const token = Math.random();",
              "artifacts": [
                {
                  "name": "session.js",
                  "tags": ["security"],
                  "sha": "deadbeef",
                  "region": "us-west-2"
                },
                {
                  "name": "session-backup.js",
                  "tags": ["backup"],
                  "sha": "beadfeed",
                  "region": "us-central-1"
                }
              ]
            }
          ],
          "severityFactorsPerIssue": [
            {
              "name": "Credential Exposure",
              "type": "Damage"
            },
            {
              "name": "Accessible in Public Repo",
              "type": "Reachable"
            }
          ]
        }
      ]
    }
  ]
}

                    "name": "jquery.js",
                    "tags": [
                      "library",
                      "javascript"
                    ],
                    "sha": "abc123def456",
                    "region": "us-east-1"
                  },
                  {
                    "name": "jquery.min.js",
                    "tags": [
                      "minified",
                      "production"
                    ],
                    "sha": "xyz789ghi012",
                    "region": "us-west-2"
                  }
                ]
              }
            ],
            "vulnerabilities": [
              {
                "cve": "CVE-2012-6708",
                "cvssScore": "6.1",
                "cvssVersion": "3.1",
                "cveDescription": "XSS in jQuery 1.7.2 via input manipulation.",
                "epss": "0.91",
                "percentile": "99.7",
                "kev": true,
                "publishedExploitDate": "2017-05-12",
                "hasPublicExploit": true,
                "publicExploitLink": "https://www.exploit-db.com/exploits/38269",
                "attackVector": "Network"
              },
              {
                "cve": "CVE-2015-9251",
                "cvssScore": "6.1",
                "cvssVersion": "3.0",
                "cveDescription": "XSS vulnerability due to improper sanitization.",
                "epss": "0.88",
                "percentile": "98.1",
                "kev": false,
                "publishedExploitDate": "2018-02-27",
                "hasPublicExploit": true,
                "publicExploitLink": "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                "attackVector": "Network"
              }
            ],
            "severityFactorsPerIssue": [
              {
                "name": "Public Exploit Available",
                "type": "Exploitable"
              },
              {
                "name": "Widely Used Library",
                "type": "Reachable"
              },
              {
                "name": "Damage",
                "type": "Damage"
              }
            ]
          },
          {
            "id": "FIN-002",
            "title": "Hardcoded Credentials",
            "severity": "Critical",
            "summary": "Hardcoded database credentials found in source code.",
            "impact": "May allow attackers to access database.",
            "recommendation": "Remove hardcoded credentials and use environment variables.",
            "assets": [
              {
                "filePath": "config/database.js",
                "snippet": "const password = 'dbadmin123';",
                "artifacts": [
                  {
                    "name": "database.js",
                    "tags": [
                      "config",
                      "sensitive"
                    ],
                    "sha": "d3adb33f",
                    "region": "eu-central-1"
                  },
                  {
                    "name": "backup-database.js",
                    "tags": [
                      "backup",
                      "deprecated"
                    ],
                    "sha": "feedface",
                    "region": "eu-west-1"
                  }
                ]
              }
            ],
            "severityFactorsPerIssue": [
              {
                "name": "Credential Exposure",
                "type": "Impact"
              },
              {
                "name": "Accessible in Public Repo",
                "type": "Exposure"
              }
            ]
          },
          {
            "id": "LOGI-003",
            "title": "Use of Insecure Random Generator",
            "severity": "Medium",
            "summary": "The `Math.random()` function is used to generate session tokens.",
            "impact": "Predictable session IDs can lead to session hijacking.",
            "recommendation": "Use a cryptographically secure random number generator.",
            "assets": [
              {
                "filePath": "src/utils/token.js",
                "snippet": "return Math.random().toString(36).substring(2);",
                "artifacts": [
                  {
                    "name": "token.js",
                    "tags": ["auth", "token"],
                    "sha": "cafebabe",
                    "region": "us-west-1"
                  },
                  {
                    "name": "legacy-token.js",
                    "tags": ["deprecated"],
                    "sha": "facefeed",
                    "region": "us-east-2"
                  }
                ]
              },
              {
                "filePath": "src/security/session.js",
                "snippet": "const token = Math.random();",
                "artifacts": [
                  {
                    "name": "session.js",
                    "tags": ["security"],
                    "sha": "deadbeef",
                    "region": "us-west-2"
                  },
                  {
                    "name": "session-backup.js",
                    "tags": ["backup"],
                    "sha": "beadfeed",
                    "region": "us-central-1"
                  }
                ]
              }
            ],
            "severityFactorsPerIssue": [
              {
                "name": "Weak Entropy Source",
                "type": "Cryptography"
              },
              {
                "name": "Used in Token Generation",
                "type": "Authentication"
              }
            ]
          }
        ]
      }
    ]
  }
```
