# Source: https://screenshotone.com/docs/errors/script-triggers-redirect/

# Script Trigger Redirect

It is an API error returned when the API detects that the script will trigger a redirect and screenshots won't be rendered successfully.

```json
{
    "is_successful": false,
    "error_code": "script_triggers_redirect",
    "error_message": "The specified \"scripts\" option might trigger a redirect, please, specify the \"scripts_wait_until\" option. If you think it is a mistake, please, reach out at `support@screenshotone.com`.",
    "documentation_url": "https://screenshotone.com/docs/script-triggers-redirect/"
}
```

## Reasons and how to fix

Let's quickly consider possible reasons and possible solutions.

### Add some wait options

Since the custom script you add with the "scripts" options triggers a redirect, you must also set [the "scripts_wait_until" option](/docs/options/#scripts_wait_until), too.

And to force the API to wait until the new page is loaded.

## Reach out to support

If nothing helps you, please, reach out to `support@screenshotone.com` and we will try to help you as fast as possible.