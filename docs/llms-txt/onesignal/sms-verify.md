# Source: https://documentation.onesignal.com/docs/en/sms-verify.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS Verify

> Send SMS verification codes for two-factor authentication and security.

The OneSignal Verify API allows you to send verification codes to users via SMS , making it ideal for two-factor authentication, account registration, and password resets.

## To set up verify

1. **Create a verification service** Make a request to the create verification service endpoint and provide a `FriendlyName`. The friendly name should be a descriptive string that you create to describe the verification service. This is the name used in the SMS sent to the end-user. (e.g. Your \[`FriendlyName`] verification code is: XXXXXX) It can be up to 32 characters long. This value should not contain PII. Optionally, you can also provide these additional parameters:

   1. `CodeLength` The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
   2. `LookupEnabled`: Whether to perform a lookup with each verification started and return info about the phone number
   3. `SkipSMSToLandlines`: Whether to skip sending SMS verifications to landlines. Requires lookup\_enabled.
   4. `Psd2Enabled`: Whether to pass PSD2 transaction parameters when starting a verification.
   5. `DoNotShareWarningEnabled`: Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: Your AppName verification code is: 1234. Don't share this code with anyone; our employees will never ask for the code
   6. `CustomCodeEnabled`: Whether to allow sending verifications with a custom code instead of a randomly generated one.
   7. `Totp.Issuer`: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
   8. `Totp.TimeStep`: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time\_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
   9. `Totp.CodeLength`: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
   10. `Totp.Skew`: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1 Note: by default, the message to the end user will say "Your \[friend name] verification code is: XXXXXX". To customize this language, reach out to support.

2. **Send a verification code** Make a request to the create verification endpoint. Provide the user's phone number and the channel (SMS) you want to use. This will send the verification code to the user.

3. **Check the verification code** Make a request to the verification check endpoint. Provide the user's phone number and the user sent verification code you want to check.

**Additional Considerations**

* Expiration Time: default is 10 mins (reach out to support to customize the expiration)
* Retries: Make sure to consider your user's experience for failed verification attempts and retries.
* Security: Implement best practices for handling sensitive information like phone numbers and verification codes.

For more detailed information and examples, refer to the Twilio Verify API documentation: [https://www.twilio.com/docs/verify](https://www.twilio.com/docs/verify)

Built with [Mintlify](https://mintlify.com).
