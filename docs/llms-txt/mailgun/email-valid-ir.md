# Source: https://documentation.mailgun.com/docs/validate/email-valid-ir.md

# Email Validation API

Note:
Our Single and Bulk Email Validation service is available via the EU API.

This API endpoint is an email address validation service that will validate the given address based on:

- Mailbox detection
- Syntax checks (RFC defined grammar)
- DNS validation
- Spell checks
- Email Service Provider (ESP) specific local-part grammar (if available).


The Email Validation API endpoint is available at:


```
v4/address/validate
```

Pricing details for Mailgun's email validation service can be found on our [pricing page](https://www.mailgun.com/pricing).

Mailgun's email validation service is intended to verify email addresses submitted through forms like newsletters, online registrations and shopping carts. Refer to our [Acceptable Use Policy (AUP)](http://mailgun.com/aup) for more information about how to use the service appropriately.

Note:
A previous version of the API is described here [Email Validation (Deprecated)](https://documentation.mailgun.com/en/latest/api-email-validation-deprecated.html#api-email-validation)