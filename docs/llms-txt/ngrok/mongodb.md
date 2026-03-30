# Source: https://ngrok.com/docs/using-ngrok-with/mongodb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with MongoDB

> Expose your local MongoDB server to the internet using ngrok TCP endpoints on port 27017.

This guide explains how to expose your local MongoDB server using ngrok TCP endpoints.

## What you'll need

* MongoDB installed and running locally.
* An ngrok account.
* Your ngrok authtoken.
* A valid payment method added to your account (TCP endpoints are only available on a free plan after adding a valid payment method).

## Expose your MongoDB server

Use a TCP endpoint to expose your local MongoDB server.
Open an ngrok TCP endpoint to your local MongoDB service, which is usually running on port `27017`.

```bash  theme={null}
ngrok tcp 27017
```

## Connect to your database

Once ngrok is forwarding traffic to your MongoDB service, use the TCP address and port from the ngrok output to connect from your preferred client.


Built with [Mintlify](https://mintlify.com).