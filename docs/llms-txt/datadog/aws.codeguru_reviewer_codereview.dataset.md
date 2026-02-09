# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeguru_reviewer_codereview.dataset.md

---
title: CodeGuru Reviewer Codereview
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeGuru Reviewer Codereview
---

# CodeGuru Reviewer Codereview

This table represents the CodeGuru Reviewer Codereview resource from Amazon Web Services.

```
aws.codeguru_reviewer_codereview
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| code_review_arn         | core | string     | The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object.                                                                                                                                                                                                                                |
| created_time_stamp      | core | timestamp  | The time, in milliseconds since the epoch, when the code review was created.                                                                                                                                                                                                                                                                                                       |
| last_updated_time_stamp | core | timestamp  | The time, in milliseconds since the epoch, when the code review was last updated.                                                                                                                                                                                                                                                                                                  |
| metrics_summary         | core | json       | The statistics from the code review.                                                                                                                                                                                                                                                                                                                                               |
| name                    | core | string     | The name of the code review.                                                                                                                                                                                                                                                                                                                                                       |
| owner                   | core | string     | The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID. |
| provider_type           | core | string     | The provider type of the repository association.                                                                                                                                                                                                                                                                                                                                   |
| pull_request_id         | core | string     | The pull request ID for the code review.                                                                                                                                                                                                                                                                                                                                           |
| repository_name         | core | string     | The name of the repository.                                                                                                                                                                                                                                                                                                                                                        |
| source_code_type        | core | json       |
| state                   | core | string     | The state of the code review. The valid code review states are: <ul> <li> <code>Completed</code>: The code review is complete. </li> <li> <code>Pending</code>: The code review started and has not completed or failed. </li> <li> <code>Failed</code>: The code review failed. </li> <li> <code>Deleting</code>: The code review is being deleted. </li> </ul>                   |
| tags                    | core | hstore_csv |
| type                    | core | string     | The type of the code review.                                                                                                                                                                                                                                                                                                                                                       |
