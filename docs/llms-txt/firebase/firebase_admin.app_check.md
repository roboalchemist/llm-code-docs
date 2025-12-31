# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.app_check.md.txt

# firebase_admin.app_check module

Firebase App Check module.

## Functions

|                                                                                                                                                                     ### verify_token firebase_admin.app_check.verify_token(*token: str* , *app=None* ) â Dict\[str, Any\]                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verifies a Firebase App Check token. Parameters: : - **token** -- A token from App Check. - **app** -- An App instance (optional). Returns: :   The token's decoded claims. Return type: :   Dict\[str, Any\] Raises: : - **ValueError** -- If the app's project_id is invalid or unspecified, - **or if the token's headers** **or** **payload are invalid.** -- - **PyJWKClientError** -- If PyJWKClient fails to fetch a valid signing key. |