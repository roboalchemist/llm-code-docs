# Source: https://ngrok.com/docs/using-ngrok-with/mysql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with MySQL

> Connect to your local MySQL database remotely using ngrok TCP endpoints on port 3306.

This guide explains how to connect to your local MySQL database remotely using ngrok TCP endpoints.

## What you'll need

* MySQL installed and running locally.
* An ngrok account.
* Your ngrok authtoken.
* A valid payment method added to your account (TCP endpoints are only available on a free plan after adding a valid payment method).

## Expose your MySQL database

To connect to a database using ngrok, you need to use a TCP endpoint.
Once you have your database up and running, you can remotely connect to it using an ngrok TCP endpoint and the default port of `3306`.

```bash  theme={null}
ngrok tcp 3306
```

## Connect to your database

Once ngrok is forwarding traffic, use the TCP address and port from the ngrok output to connect from your preferred MySQL client.

## Further resources

* [Configure Site-to-Site Connectivity for Databases](../guides/site-to-site-connectivity/)
* [Configure Site-to-Site Connectivity for Databases with mTLS](../guides/site-to-site-connectivity/)


Built with [Mintlify](https://mintlify.com).