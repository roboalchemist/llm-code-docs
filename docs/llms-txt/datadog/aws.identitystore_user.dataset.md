# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.identitystore_user.dataset.md

---
title: Identity Store User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Store User
---

# Identity Store User

An Identity Store User in AWS represents a user identity within the AWS Identity Store, which is part of AWS Single Sign-On (IAM Identity Center). It contains core user attributes such as username, display name, email, and unique identifiers. This resource is used to manage and reference individual users for authentication and access control across AWS accounts and applications.

```
aws.identitystore_user
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                              | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| addresses          | core | json       | A list of Address objects containing addresses associated with the user.                                                                                                                                                                                                                               |
| emails             | core | json       | A list of Email objects containing email addresses associated with the user.                                                                                                                                                                                                                           |
| external_ids       | core | json       | A list of ExternalId objects that contains the identifiers issued to this resource by an external identity provider.                                                                                                                                                                                   |
| group_memberships  | core | json       | A list of GroupMembership objects in the group for a specified member.                                                                                                                                                                                                                                 |
| identity_store_id  | core | string     | The globally unique identifier for the identity store.                                                                                                                                                                                                                                                 |
| locale             | core | string     | A string containing the geographical region or location of the user.                                                                                                                                                                                                                                   |
| name               | core | json       | An object containing the name of the user.                                                                                                                                                                                                                                                             |
| nick_name          | core | string     | A string containing an alternate name for the user.                                                                                                                                                                                                                                                    |
| phone_numbers      | core | json       | A list of PhoneNumber objects containing phone numbers associated with the user.                                                                                                                                                                                                                       |
| preferred_language | core | string     | A string containing the preferred language of the user. For example, "American English" or "en-us."                                                                                                                                                                                                    |
| profile_url        | core | string     | A string containing a URL that might be associated with the user.                                                                                                                                                                                                                                      |
| tags               | core | hstore_csv |
| timezone           | core | string     | A string containing the time zone of the user.                                                                                                                                                                                                                                                         |
| title              | core | string     | A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.                                                                                                                                                                   |
| user_id            | core | string     | The identifier for a user in the identity store.                                                                                                                                                                                                                                                       |
| user_name          | core | string     | A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. |
| user_type          | core | string     | A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.                                                                                                                                                                        |
