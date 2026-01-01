# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/domains/domains-sandbox.md

# Sandbox Domain

Want to immediately send email from your account without setting up your own Domain?

Each new Mailgun account is automatically provisioned with a sandbox domain, sandbox `<uniq-alpha-numeric-string\>@mailgun.org`. This is for testing purposes only. Sandbox domains can only send to authorized recipients.

Your Sandbox Domain allows:

- Sending messages to lists with up to 5 [authorized participants](https://help.mailgun.com/hc/en-us/articles/217531258-Authorized-Recipients)
- Receiving Messages (limited to one Route)
- Tracking Messages


Info
Sending limitations are also in effect for Routes that are triggered by message addresses to the sandbox domain and mailing lists created under that domain.

#### To use your Sandbox Domain:

1. Log in to your Mailgun account
2. Go to the Mailgun Control Panel
3. On the left side control panel, click 'Send' to expand the sidebar, then click 'Domains'
4. Click on the sandbox domain
5. From the Setup tab in Domain Settings, add authorized recipients and view code examples to send email using your sandbox domain