# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/email_verification_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.email_verification_api

## Classes

### EmailVerificationApi

```python  theme={"system"}
edgeimpulse_api.api.email_verification_api.EmailVerificationApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### validate\_email

```python  theme={"system"}
edgeimpulse_api.api.email_verification_api.EmailVerificationApi.validate_email(
	self,
	email_validation_request: edgeimpulse_api.models.email_validation_request.EmailValidationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.validate_email_response.ValidateEmailResponse
```

Validate email for account sign-up

Validate whether an email is valid for sign up. Using an email that fails this check can result in the associated account missing communications and features that are distributed through email.

| Parameters                 |                                                                          |
| -------------------------- | ------------------------------------------------------------------------ |
| `self`                     | ` `                                                                      |
| `email_validation_request` | `edgeimpulse_api.models.email_validation_request.EmailValidationRequest` |
| `**kwargs`                 | ` `                                                                      |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.validate_email_response.ValidateEmailResponse` |


Built with [Mintlify](https://mintlify.com).