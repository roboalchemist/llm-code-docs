# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codebuild_source_credentials.dataset.md

---
title: CodeBuild Source Credential
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeBuild Source Credential
---

# CodeBuild Source Credential

CodeBuild Source Credential in AWS is a resource that stores authentication details for connecting AWS CodeBuild to external source code repositories such as GitHub, GitHub Enterprise, or Bitbucket. It allows CodeBuild projects to securely access private repositories by managing tokens or credentials, eliminating the need to embed sensitive information directly in build specifications.

```
aws.codebuild_source_credentials
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                                            | Description |
| ----------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name (ARN) of the token.                                                                                                         |
| auth_type   | core | string     | The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH, PERSONAL_ACCESS_TOKEN, CODECONNECTIONS, or SECRETS_MANAGER. |
| resource    | core | string     | The connection ARN if your authType is CODECONNECTIONS or SECRETS_MANAGER.                                                                           |
| server_type | core | string     | The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, GITLAB, GITLAB_SELF_MANAGED, or BITBUCKET.                             |
| tags        | core | hstore_csv |
