# Source: https://plivo.com/docs/messaging/concepts/destination-number-validation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Destination Number Validation

> Validate destination numbers to improve delivery rates and reduce costs

By using Plivo’s [enhanced destination number validation](https://support.plivo.com/hc/en-us/articles/360041783651-Enhanced-Destination-Number-Validation-for-SMS), you can identify invalid destination numbers and numbers that aren’t enabled for SMS or MMS services. Enhanced validation fixes incorrect destination number formats too. Using enhanced validation should result in better delivery rates and increased cost savings from not sending messages to numbers that are incapable of accepting them

<Note>
  <strong>Note:</strong> MMS validation is available only for the US and Canada.
</Note>

## Synchronous handling for invalid numbers

SMS API requests to invalid and non-SMS-enabled numbers are rejected with a 400 Bad Request API response, which developers can easily propagate upstream. Let’s see how that would work for a one-time password (OTP) use case:

**Step 1:** End user requests OTP on an invalid destination number.

**Step 2:** The application initiates a Send SMS API request.

**Step 3:** Plivo returns a 400 Bad Request response synchronously.

**Step 4:** The application returns an “invalid number” error.

```json  theme={null}
{
    "api_id": "df5d4304-66af-11eb-91d8-0242ac110004",
    "error": "19332631167 is not a valid phone number"
}
```

## Synchronous handling for invalid MMS numbers

MMS API requests to invalid or non-MMS-enabled numbers are rejected with a 400 Bad Request API response, which developers can easily propagate upstream. Let’s see how that would work for sending an MMS message.

**Step 1:** The application initiates an MMS message to an non-MMS-enabled number.

**Step 2:** Plivo returns a 400 Bad Request response synchronously.

**Step 3:** The application returns a “not an MMS enabled phone number” error.

```json  theme={null}
{
    "api_id": "fd0ad4ee-66ae-11eb-8d40-0242ac110004",
    "error": "19003356789 is not an MMS enabled phone number"
}
```

## Format correction for phone numbers

The platform also intelligently reformats incorrectly formatted phone numbers. For example:

**Scenario 1:** If a user enters the Lithuanian phone number 370860112345 (country code 370), Plivo automatically reformats it to the E.164 international format +37060112345 before forwarding it to downstream carriers. Notice the missing 8 in the formatted number; 8 is only required when dialing a Lithuanian number from inside Lithuania.

**Scenario 2:** If a user enters the Mexican phone number 520455512345678 (country code 52), Plivo automatically reformats it to the E.164 international format +5215512345678. Notice that 045 has been replaced with 1, because 045 is only to be used when dialing a domestic cellphone from a landline, while 521 is the prefix for mobile phone numbers in E.164 format.

## Enabling destination number validation

New Plivo customers have enhanced destination number validation enabled by default. You can enable or disable enhanced destination number validation for SMS and MMS from the Messaging > [Other Settings](https://cx.plivo.com/messaging-settings) page of the Plivo console.

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/number_validation.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=014ccc65834839001542e96033e93d2b" alt="Destination Number Validation" width="1433" height="537" data-path="images/number_validation.png" />
</Frame>

<Note>
  <strong>Note:</strong>

  * Landlines in the US, Canada, and the UK can be enabled for both SMS and MMS. Therefore, Plivo does not reject messages to landline numbers in these countries.
  * Destination numbers of less than 9 and more than 15 numbers are rejected by default even when enhanced destination number validation is disabled.
</Note>
