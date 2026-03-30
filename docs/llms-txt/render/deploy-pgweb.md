# Source: https://render.com/docs/deploy-pgweb.md

# Deploy Pgweb — a PostgreSQL Client

This guide shows how to deploy [Pgweb](https://github.com/sosedoff/pgweb), a web-based database client for PostgreSQL, written in Go. It lets you connect to, browse, and run queries against any local or remote PostgreSQL database.

Pgweb uses [dep](https://github.com/golang/dep) for dependency management and this guide also demonstrates Render's native support for `dep`.

## Deployment

1. Fork [sosedoff/pgweb](https://github.com/sosedoff/pgweb) on GitHub.

2. Create a new *Web Service* on Render, and give Render permission to access your new repo.

3. Select `Go` for the runtime and use the following values during creation:

   *Build Command*: *`go build -o app`*

   *Start Command*: *`./app --bind=0.0.0.0`*

That's it! Your pgweb install will be available on your `onrender.com` URL as soon as the deploy is live. You can enter your credentials to connect to your database and start browsing!

To connect to your Render databases from Pgweb deployed on Render, make sure to append *`?sslmode=require`* to your internal database URL.

## Pgweb Screenshots

#### Connection Screen

[image: pgweb connect]

#### Table Browser

[image: pgweb browser]

