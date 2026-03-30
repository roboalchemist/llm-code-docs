# Source: https://docs.snowflake.com/en/user-guide/errors-saml.md

# Federated authentication and SSO troubleshooting

This topic provides information to help troubleshoot a federated authentication environment, including the error codes and messages that
are generated during an unsuccessful user login attempt.

## Password-related errors

A user with an expired Snowflake password cannot log in with SSO even though they are not using the password. This behavior is
intentional and prevents someone from logging in using expired credentials.

SSO logins are also rejected if an administrator set the `MUST_CHANGE_PASSWORD` parameter to TRUE when creating the user, but the user
has not changed the password yet.

## Error codes

Errors are generated for each failed login attempt. These errors can be obtained from the [Snowflake Information Schema](../sql-reference/info-schema.md) or the
[ACCOUNT_USAGE schema](../sql-reference/account-usage.md):

* The Snowflake Information Schema provides data from within the past 7 days and can be queried using
  the [LOGIN_HISTORY , LOGIN_HISTORY_BY_USER](../sql-reference/functions/login_history.md) table functions.
* The [LOGIN_HISTORY](../sql-reference/account-usage/login_history.md) view in the ACCOUNT_USAGE schema provides similar data from within the past year.

### Federated authentication error codes

The table below contains the error codes and messages related to federated authentication.

| Error Code | Error | Description |
| --- | --- | --- |
| 390136 | FED_REAUTH_PENDING | Authentication response is pending from IDP. |
| 390137 | FED_REAUTH | Federated authentication request URL is generated. |
| 390138 | FED_REAUTH_TIMEOUT | Timeout waiting for authentication response from IDP. |
| 390139 | AUTHENTICATOR_NOT_SUPPORTED | The specified authenticator is not accepted by your Snowflake account configuration. Please contact your local system administrator to get the correct URL to use. |
| 390140 | FED_PASSWORD_EXPIRED | Identity Provider (IdP) password has expired. Contact your IdP team. |
| 390191 | USERNAMES_MISMATCH | The user you were trying to authenticate as differs from the user currently logged in at the IDP. |

### SAML error codes

Troubleshooting a login failure differs depending on whether the error message has an UUID.

If you encounter an error message associated with a failed SAML SSO login attempt, and the error message does not have a UUID, then ensure
the user exists. If the user exists, then the SAML response is invalid and the number of login attempts is too high.

If you encounter an error message associated with a failed SAML SSO login attempt, and the error message has a UUID, you can ask an
administrator that has MONITOR privilege assigned to their role to get a more detailed description of the error by following the steps
below:

1. Find the UUID in the error message:

   > ```output
   > SAML response is invalid or matching user is not found. Contact your local system administrator. [eb55b777-50a4-4db5-b231-9ee457fb3981]
   > ```
>
2. Use the UUID as an argument to the SYSTEM$GET_LOGIN_FAILURE_DETAILS function, and extract the error using the
   [JSON_EXTRACT_PATH_TEXT](../sql-reference/functions/json_extract_path_text.md) function:

   > ```sqlexample
   > SELECT JSON_EXTRACT_PATH_TEXT(SYSTEM$GET_LOGIN_FAILURE_DETAILS('eb55b777-50a4-4db5-b231-9ee457fb3981'), 'errorCode');
   > ```
>
3. Find the error description in the table below:

   > | Error Code | Error | Description |
   > | --- | --- | --- |
   > | 390133 | SAML_RESPONSE_INVALID | The SAML response was invalid for an unspecified reason, although it is most likely malformed (this is also used if there is an error on parsing). |
   > | 390165 | SAML_RESPONSE_INVALID_SIGNATURE | The SAML response contains an invalid Signature. |
   > | 390166 | SAML_RESPONSE_INVALID_DIGEST_METHOD | The SAML response contains an invalid “DigestMethod” attribute or omits it entirely. |
   > | 390167 | SAML_RESPONSE_INVALID_SIGNATURE_METHOD | The SAML response contains an invalid “SignatureMethod” or omits it entirely. |
   > | 390168 | SAML_RESPONSE_INVALID_DESTINATION | The “Destination” attribute in the SAML response does not match a valid destination URL on the account. |
   > | 390169 | SAML_RESPONSE_INVALID_AUDIENCE | The SAML response does not contain exactly one audience or the audience URL does not match what we expect the audience URL to be. |
   > | 390170 | SAML_RESPONSE_INVALID_MISSING_INRESPONSETO | The “InResponseTo” attribute in the SAML assertion is missing. |
   > | 390171 | SAML_RESPONSE_INVALID_RECIPIENT_MISMATCH | The “Recipient” attribute does not match a valid destination URL. |
   > | 390172 | SAML_RESPONSE_INVALID_NOTONORAFTER_VALIDATION | This typically indicates that the time in which the SAML assertion is valid has expired. |
   > | 390173 | SAML_RESPONSE_INVALID_NOTBEFORE_VALIDATION | This typically indicates that the time in which the SAML assertion is valid has not yet come. |
   > | 390174 | SAML_RESPONSE_INVALID_USERNAMES_MISMATCH | The login names do not match during re-authentication. |
   > | 390175 | SAML_RESPONSE_INVALID_SESSIONID_MISSING | During re-authentication, we were unable to find a session corresponding to the user. |
   > | 390176 | SAML_RESPONSE_INVALID_ACCOUNTS_MISMATCH | During re-authentication, the names of the accounts were found to not match. |
   > | 390177 | SAML_RESPONSE_INVALID_BAD_CERT | The x.509 certificate contained in the SAML response is either malformed or does not match the expected certificate. |
   > | 390178 | SAML_RESPONSE_INVALID_PROOF_KEY_MISMATCH | The proof keys do not match with respect to the authentication request ID. |
   > | 390179 | SAML_RESPONSE_INVALID_INTEGRATION_MISCONFIGURATION | The SAML IdP configuration is invalid. |
   > | 390180 | SAML_RESPONSE_INVALID_REQUEST_PAYLOAD | During authentication, using an invalid payload or using an invalid federated OAuth connection string. |
   > | 390181 | SAML_RESPONSE_INVALID_MISSING_SUBJECT_CONFIRMATION_BEARER | The Subject confirmation with Bearer method is missing and cannot be validated. |
   > | 390182 | SAML_RESPONSE_INVALID_MISSING_SUBJECT_CONFIRMATION_DATA | The Subject confirmation data is missing in the assertion. |
   > | 390183 | SAML_RESPONSE_INVALID_CONDITIONS | The SAML assertion is not valid for a reason that is different than the preceding conditions in this table. |
   > | 390184 | SAML_RESPONSE_INVALID_ISSUER | The SAML Response contained an issuer/entityID value different from the one configured in the SAML IDP Configuration. |
