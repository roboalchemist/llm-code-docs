# Source: https://developers.activecampaign.com/docs/twillio-sms-outbound-example.md

# Twillio SMS Outbound Example

The following example is Twillio SMS outbound example, using token authentication. [Click here for information on the Twillio SMS Api.](https://www.twilio.com/docs/sms/api)

```json
{
  "api": {
    "base_url": "https://api.twilio.com/2010-04-01"
  },
  "auth": {
    "twilio-basicauth": {
      "type": "basic",
      "verify_url": "https://api.twilio.com/2010-04-01/Accounts.json",
      "defined_fields": {
        "username": {
          "label": "Account SID",
          "placeholder": "Enter Your Account SID",
          "help_text": "Login to your account to find API credentials here: twilio.com/user/account/settings"
        },
        "password": {
          "label": "Auth Token",
          "placeholder": "Enter Your Auth Token",
          "help_text": "Found immediately below your Account SID"
        }
      }
    }
  },
  "workflows": [
    {
      "label": "Twilio - Send an SMS",
      "description": "Send messages to your contacts using Twilio",
      "name": "twilio-send-a-message",
      "type": "automations",
      "auth": "twilio-basicauth",
      "setup": {
        "connect": {
          "label": "Connect"
        },
        "select": {
          "label": "Message Settings",
          "description": "Select a Project and Phone Number or Messaging Service to send SMS messages using Twilio. For Twilio SMS, there is a 1,600 character limit.",
          "form_fields": [
            {
              "label": "Project",
              "id": "sub_account",
              "type": "dropdown",
              "placeholder": "Select A Project",
              "options": {
                "!pipe": [
                  {
                    "!http": {
                      "method": "GET",
                      "path": "/Accounts.json?Status=active"
                    }
                  },
                  {
                    "!jq": "[.accounts[] | {display: .friendly_name, value: .sid}]"
                  }
                ]
              }
            },
            {
              "label": "Phone Number or Messaging Service",
              "id": "phone_number",
              "type": "dropdown",
              "placeholder": "Select A Phone Number or Messaging Service",
              "options": {
                "!pipe": [
                  {
                    "!http": {
                      "method": "GET",
                      "path": "/Accounts/${custom_data.sub_account.value}/IncomingPhoneNumbers.json?PageSize=350"
                    }
                  },
                  {
                    "!jq": "[.incoming_phone_numbers[] | select(.capabilities.sms == true) | {display: .friendly_name, value: .phone_number}]"
                  },
                  {
                    "!http": {
                      "method": "GET",
                      "url": "https://messaging.twilio.com/v1/Services?PageSize=350"
                    }
                  },
                  {
                    "!jq": "[.services[] | {display: .friendly_name, value: .sid}]"
                  },
                  {
                    "!jq": ". + ${piped_content.2}"
                  }
                ]
              }
            },
            {
              "label": "Enter Message",
              "id": "message",
              "type": "textarea",
              "personalize": "ActiveCampaignContact"
            }
          ]
        },
        "map": {
          "label": "Mapping",
          "describe_source": {
            "label": "ActiveCampaign",
            "options": {
              "!resource": "ActiveCampaignContact.fields"
            }
          }
        }
      },
      "data_pipeline": {
        "source": {
          "!resource": "ActiveCampaignContact"
        },
        "target": {
          "!pipe": [
            {
              "!jq": "${custom_data.phone_number.value}"
            },
            {
              "!switch": {
                "jq": "if . | test(\"MG.*\") then 1 else 0 end",
                "cases": [
                  {
                    "!http": {
                      "method": "POST",
                      "url": "https://api.twilio.com/2010-04-01/Accounts/${custom_data.sub_account.value}/Messages.json",
                      "body": {
                        "To": "${piped_content.0.phone}",
                        "From": "${custom_data.phone_number.value}",
                        "Body": "${custom_data.message.value}"
                      },
                      "headers": {
                        "Content-Type": "application/x-www-form-urlencoded"
                      }
                    }
                  },
                  {
                    "!http": {
                      "method": "POST",
                      "url": "https://api.twilio.com/2010-04-01/Accounts/${custom_data.sub_account.value}/Messages.json",
                      "body": {
                        "To": "${piped_content.0.phone}",
                        "MessagingServiceSid": "${custom_data.phone_number.value}",
                        "Body": "${custom_data.message.value}"
                      },
                      "headers": {
                        "Content-Type": "application/x-www-form-urlencoded"
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ],
  "$version": "2"
}
```