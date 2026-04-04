# Source: https://www.courier.com/docs/external-integrations/email/postmark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Postmark

> Integrate Postmark with Courier to send emails using recipient profiles, apply message overrides, and use Postmark templates and attachments with support for custom config like MessageStream.

## Setup

You will need a [Postmark](https://postmarkapp.com/) account with a verified sender signature. In Postmark, navigate to your server's API Tokens page to get your Server API Token. In Courier, navigate to the [Postmark Integration](https://app.courier.com/integrations/catalog/postmark) page, enter your API token and From Address, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Postmark, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "email": "alice@acme.com"
    }

    // ... rest of message definition
  }
}
```

## Subject Character Limit

<Info>
  The Postmark API imposes a subject line limit of \~60 characters. Due to encoding, using emojis or special characters in the subject line will decrease this limit.
</Info>

## Overrides

You can use a provider override to replace what we send to Postmark's Email API. For example, you can add [MessageStream](https://postmarkapp.com/support/article/1207-how-to-create-and-send-through-message-streams) and an attachment to your request:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "postmark": {
        "override": {
          "config": {
            "MessageStream": "message_stream_id"
          },
          "body": {
            "Attachments": [
              {
                "Name": "readme.txt",
                "Content": "dGVzdCBjb250ZW50",
                "ContentType": "text/plain"
              }
            ]
          }
        }
      }
    }
  }
}
```

The `message.providers.postmark.override` property can be used to replace what we send to Postmark's Email API. Note: the override does not replace the entire object, only the elements that you define in the body of the override. You can see all the available options by visiting the [Postmark API docs](https://postmarkapp.com/developer/api/email-api).

## Using Postmark Templates

```json  theme={null}
{
	"message": {
		"to": {
			"email": "rodrigo@courier.com"
		},
		"template": "NOTIFICATION_TEMPLATE_ID",
		"providers": {
			"postmark": {
				"override": {
					"config": {
						"url": "https://api.postmarkapp.com/email/withTemplate"
					},
					"body": {
						"TemplateId": "123456",
						"TemplateModel": {
							"product_url": "product_url_Value",
							"product_name": "product_name_Value",
							"name": "name_Value",
							"action_url": "action_url_Value",
							"login_url": "login_url_Value",
							"username": "username_Value",
							"trial_length": "trial_length_Value",
							"trial_start_date": "trial_start_date_Value",
							"trial_end_date": "trial_end_date_Value",
							"support_email": "support_email_Value",
							"live_chat_url": "live_chat_url_Value",
							"sender_name": "sender_name_Value",
							"help_url": "help_url_Value",
							"company_name": "company_name_Value",
							"company_address": "company_address_Value"
						}
					}
				}
			}
		}
	}
}
```

The `message.providers.postmark.override.config` property can be used to override Courier templates and use Postmark's [Templates API](https://postmarkapp.com/developer/api/templates-api).

Be sure to include the `https://api.postmarkapp.com/email/withTemplate` URL in the config object along with the `TemplateId` and `TemplateModel` in the the body.

<Warning>
  When using Postmark templates - make sure your request uses a `template` parameter instead of `content`. Otherwise the `content` object will take presedence over the Postmark override. The `template_id` must be valid or an error will occur.
</Warning>
