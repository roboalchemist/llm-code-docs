# Source: https://docs.snowflake.com/en/sql-reference/account-usage/object_access_request_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# OBJECT_ACCESS_REQUEST_HISTORY view

This Account Usage view allows consumers to access audit logs that track the submission, rejection, and approval of object access requests through the Internal Marketplace to maintain security and compliance.

## Columns

The following table provides a description of each column in the view.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | The organization name of current account. |
| ACCOUNT_NAME | VARCHAR | The account name of the current account. |
| TIMESTAMP | TIMESTAMP_LTZ | The state transition event. |
| USER_REGION | VARCHAR | The region of the requester or approver. |
| USER_ACCOUNT_NAME | VARCHAR | The account name of the requester or approver. |
| USER_NAME | VARCHAR | The username of the requester or approver. |
| USER_EMAIL | VARCHAR | The email of the requester or approver. |
| USER_COMMENT | VARCHAR | For CREATE_REQUEST and CANCEL REQUEST, this shows the reason for access provided by the requester.  For APPROVE_REQUEST, DENY_REQUEST, and AUTO_APPROVE_REQUEST, this is the comment for approval/denial provided by the approver. |
| ACTION | VARCHAR | The requester or approver action. This can be one of the following:   *CREATE_REQUEST* CANCEL_REQUEST *APPROVE_REQUEST* DENY_REQUEST * AUTO_APPROVE_REQUEST |
| REQUEST_ID | VARCHAR | The UUID of the request. This can be used to track the history of the request. |
| OBJECT_DOMAIN | VARCHAR | The requested object domain. Currently, this can only be DATA_EXCHANGE_LISTING. |
| OBJECT_REGION | VARCHAR | The snowflake region name where the requested object is located. |
| OBJECT_ACCOUNT_NAME | VARCHAR | The account where the requested object is located. |
| OBJECT_NAME | VARCHAR | The name of the requested object. |
| GRANTEE_TO_AUTHORIZE | VARCHAR | For CREATE_REQUEST and CANCEL REQUEST, this shows the role provided by the requester.  For APPROVE_REQUEST, DENY_REQUEST, and AUTO_APPROVE_REQUEST, this is the role granted or denied by the approver. |
| GRANTEE_TYPE | VARCHAR | The type of the grantee. Currently, this can only be ROLE. |

## Usage notes

For approver-initiated actions, such as APPROVE_REQUEST, DENY_REQUEST, and AUTO_APPROVE_REQUEST, the requester can’t see the approver’s USER_ACCOUNT_NAME, USER_NAME, USER_EMAIL, and OBJECT_ACCOUNT_NAME.
