# Source: https://ngrok.com/docs/using-ngrok-with/cgnat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with CGNAT

> Learn how to use ngrok with CGNAT networks like Starlink to expose local services without router port forwarding.

This guide shows you how to use ngrok with CGNAT networks like Starlink to expose local services without router port forwarding.
ngrok is a great solution when you don't have access to open ports on your router.
This is the case for Starlink and other systems that use CGNAT or similar software.

<Note>
  For more details, see [Don Simpson's blog post about using ngrok with CGNAT](https://www.donaldsimpson.co.uk/using-ngrok-to-work-around-carrier-grade-nat-cgnat).
</Note>

## What you'll need

* [ngrok](https://download.ngrok.com) installed.
* Your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).

## 1. Install and configure ngrok

[Install ngrok](https://download.ngrok.com) using the method that works best for your system.

Add your ngrok authtoken:

```bash  theme={null}
ngrok config --add-authtoken TOKEN
```

## 2. Start an ngrok endpoint

Start an ngrok endpoint:

```bash  theme={null}
ngrok http 80
```

No changes are needed for your network or router.


Built with [Mintlify](https://mintlify.com).