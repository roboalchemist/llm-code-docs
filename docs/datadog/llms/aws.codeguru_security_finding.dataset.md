# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeguru_security_finding.dataset.md

---
title: CodeGuru Security Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeGuru Security Finding
---

# CodeGuru Security Finding

This table represents the CodeGuru Security Finding resource from Amazon Web Services.

```
aws.codeguru_security_finding
```

## Fields

| Title         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                  | Description |
| ------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string        |
| account_id    | core | string        |
| created_at    | core | timestamp     | The time when the finding was created.                                                                                                                                                                                                                                                                                     |
| description   | core | string        | A description of the finding.                                                                                                                                                                                                                                                                                              |
| detector_id   | core | string        | The identifier for the detector that detected the finding in your code. A detector is a defined rule based on industry standards and AWS best practices.                                                                                                                                                                   |
| detector_name | core | string        | The name of the detector that identified the security vulnerability in your code.                                                                                                                                                                                                                                          |
| detector_tags | core | array<string> | One or more tags or categorizations that are associated with a detector. These tags are defined by type, programming language, or other classification such as maintainability or consistency.                                                                                                                             |
| generator_id  | core | string        | The identifier for the component that generated a finding such as AmazonCodeGuruSecurity.                                                                                                                                                                                                                                  |
| id            | core | string        | The identifier for a finding.                                                                                                                                                                                                                                                                                              |
| remediation   | core | json          | An object that contains the details about how to remediate a finding.                                                                                                                                                                                                                                                      |
| resource      | core | json          | The resource where Amazon CodeGuru Security detected a finding.                                                                                                                                                                                                                                                            |
| rule_id       | core | string        | The identifier for the rule that generated the finding.                                                                                                                                                                                                                                                                    |
| severity      | core | string        | The severity of the finding. Severity can be critical, high, medium, low, or informational. For information on severity levels, see <a href="https://docs.aws.amazon.com/codeguru/latest/security-ug/findings-overview.html#severity-distribution">Finding severity</a> in the <i>Amazon CodeGuru Security User Guide</i>. |
| status        | core | string        | The status of the finding. A finding status can be open or closed.                                                                                                                                                                                                                                                         |
| tags          | core | hstore_csv    |
| title         | core | string        | The title of the finding.                                                                                                                                                                                                                                                                                                  |
| type          | core | string        | The type of finding.                                                                                                                                                                                                                                                                                                       |
| updated_at    | core | timestamp     | The time when the finding was last updated. Findings are updated when you remediate them or when the finding code location changes.                                                                                                                                                                                        |
| vulnerability | core | json          | An object that describes the detected security vulnerability.                                                                                                                                                                                                                                                              |
