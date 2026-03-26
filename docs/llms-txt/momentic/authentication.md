# Source: https://momentic.ai/docs/environment/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

<Warning>
  Avoid using Momentic tests to log in using SSO. Providers like Google,
  Facebook, and GitHub often have security measures that block automated
  browsers.
</Warning>

## Username and password

Username and password authentication is the easiest and most straightforward
method for authenticating users in your tests.

## Email magic link

<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript  theme={null}
// fetch the latest email from the inbox
const msg = await email.fetchLatest({
  inbox: "<YOUR USERNAME HERE>",
});

// extract the magic link using regex
const link = msg.text.match(/https?:\/\/[^\s]+/)[0];

return link;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `MAGIC_LINK`.

Then, use the [Navigate](/steps/navigate) step with content
`{{ env.MAGIC_LINK }}` to navigate to the magic link and complete the login
process.

## Email One-Time Password (OTP)

<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript  theme={null}
// fetch the latest email from the inbox
const msg = await email.fetchLatest({
  inbox: "<YOUR USERNAME HERE>",
});

// extract the code using regex
const code = msg.text.match(/\b\d{6}\b/);

return code;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `OTP_CODE`.

Then, use the [Type](/steps/type) step with content `{{ env.OTP_CODE }}` to
input the OTP code and complete the login process.

## SMS One-Time Password (OTP)

<Info>**Prerequisites**: A SMS number must be provisioned by Momentic.</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript  theme={null}
// fetch the latest message from the inbox
const msg = await sms.fetchLatest({
  to: "<YOUR SMS NUMBER HERE>",
});

// extract the code using regex
const code = msg.body.match(/\b\d{6}\b/);

return code;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `OTP_CODE`.

Then, use the [Type](/steps/type) step with content `{{ env.OTP_CODE }}` to
input the OTP code and complete the login process.

## Vercel Deployment Projection

Follow the instructions
[here](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
for Playwright. You can configure headers in test options.

## IP whitelist

For teams that use Momentic Cloud, you can whitelist Momentic's fixed egress IP:
`34.106.239.183`


Built with [Mintlify](https://mintlify.com).