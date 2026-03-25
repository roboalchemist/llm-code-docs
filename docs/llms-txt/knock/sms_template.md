# Source: https://docs.knock.app/mapi-reference/templates/schemas/sms_template.md

### SmsTemplate

An SMS template.

#### Attributes

- **settings** (object) - The settings for the SMS template. Can be omitted.
- **text_body** (string) *required* - The message of the SMS.

#### Example

```json
{
  "settings": {
    "payload_overrides": "{\"name\": \"John\"}",
    "to_number": "+1234567890"
  },
  "text_body": "Hello, world!"
}
```

