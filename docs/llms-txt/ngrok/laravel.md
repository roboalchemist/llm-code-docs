# Source: https://ngrok.com/docs/using-ngrok-with/laravel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with Laravel

> Learn how to use ngrok with Laravel Valet to share your local Laravel development sites with others.

This guide explains how to use ngrok with Laravel Valet to share your local Laravel development sites with others.

## What you'll need

* Laravel Valet installed.
* Your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).

## Set your ngrok authtoken

ngrok is built into Laravel Valet.
To learn more about using your existing ngrok account with Laravel, see the Laravel Valet documentation.

```bash  theme={null}
valet set-ngrok-token YOUR_TOKEN_HERE
```

Replace `YOUR_TOKEN_HERE` with your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).


Built with [Mintlify](https://mintlify.com).