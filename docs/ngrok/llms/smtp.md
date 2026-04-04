# Source: https://ngrok.com/docs/using-ngrok-with/smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with SMTP Mail Servers

> Learn how to connect to your local SMTP mail server using ngrok TCP endpoints on ports 25, 465, 587, or 2525.

The common port for the SMTP protocol used by most mail servers is `25` for insecure traffic and `465` for secure traffic. You can use an ngrok TCP endpoint to connect to a local mail server with the following command.

```bash  theme={null}
ngrok tcp 25
```

```bash  theme={null}
ngrok tcp 465
```

<Tip>
  ngrok works with whatever port your mail server is running on, including `587` or `2525`. Just adjust the command above accordingly.
</Tip>

<Warning>
  TCP endpoints are only available on a free plan after [adding a valid payment method](https://dashboard.ngrok.com/settings#id-verification) to your account.
</Warning>


Built with [Mintlify](https://mintlify.com).