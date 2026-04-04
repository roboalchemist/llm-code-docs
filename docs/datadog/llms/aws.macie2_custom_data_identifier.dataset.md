# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.macie2_custom_data_identifier.dataset.md

---
title: Macie Custom Data Identifier
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Macie Custom Data Identifier
---

# Macie Custom Data Identifier

An AWS Macie Custom Data Identifier is a user-defined rule that helps Macie detect sensitive data unique to your organization. It allows you to specify patterns using regular expressions, along with optional keywords and contextual checks, to identify data that built-in identifiers may not cover. This enables more precise discovery and protection of sensitive information across your AWS environment.

```
aws.macie2_custom_data_identifier
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| arn                    | core | string        | The Amazon Resource Name (ARN) of the custom data identifier.                                                                                                                                                                                                                                                                                                                                           |
| created_at             | core | timestamp     | The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.                                                                                                                                                                                                                                                                                                    |
| deleted                | core | bool          | Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn't delete it permanently. Instead, it soft deletes the identifier.                                                                                                                                                                                                                  |
| description            | core | string        | The custom description of the custom data identifier.                                                                                                                                                                                                                                                                                                                                                   |
| id                     | core | string        | The unique identifier for the custom data identifier.                                                                                                                                                                                                                                                                                                                                                   |
| ignore_words           | core | array<string> | An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. Ignore words are case sensitive.                                                                                                                                                                 |
| keywords               | core | array<string> | An array that lists specific character sequences (keywords), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. Keywords aren't case sensitive.                                                                                                                                                                                               |
| maximum_match_distance | core | int64         | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. Otherwise, Macie excludes the result.      |
| name                   | core | string        | The custom name of the custom data identifier.                                                                                                                                                                                                                                                                                                                                                          |
| regex                  | core | string        | The regular expression (regex) that defines the pattern to match.                                                                                                                                                                                                                                                                                                                                       |
| severity_levels        | core | json          | Specifies the severity that's assigned to findings that the custom data identifier produces, based on the number of occurrences of text that match the custom data identifier's detection criteria. By default, Amazon Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie assigns the MEDIUM severity to those findings. |
| tags                   | core | hstore_csv    |
