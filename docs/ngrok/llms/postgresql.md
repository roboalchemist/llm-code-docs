# Source: https://ngrok.com/docs/using-ngrok-with/postgresql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with PostgreSQL

> Connect to your local PostgreSQL database remotely using ngrok TCP endpoints on port 5432.

This guide walks you through connecting to your local PostgreSQL database remotely using ngrok TCP endpoints.

## What you'll need

* PostgreSQL installed and running locally.
* An ngrok account.
* Your ngrok authtoken.
* A valid payment method added to your account (TCP endpoints are only available on a free plan after adding a valid payment method).

## Expose your PostgreSQL database

After installing the database, you can connect to it using a standard ngrok TCP endpoint sending traffic to port `5432`.

```bash  theme={null}
ngrok tcp 5432
```

## Connect to your database

Once ngrok is forwarding traffic to your PostgreSQL service, you can use the TCP address provided to connect to it remotely.

```bash  theme={null}
psql -h 0.tcp.ngrok.io -p 12345 -U postgres -d postgres
```


Built with [Mintlify](https://mintlify.com).