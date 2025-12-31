# Source: https://upstash.com/docs/qstash/api/authentication.md

# Source: https://upstash.com/docs/devops/developer-api/authentication.md

# Source: https://upstash.com/docs/qstash/api/authentication.md

# Source: https://upstash.com/docs/devops/developer-api/authentication.md

# Source: https://upstash.com/docs/qstash/api/authentication.md

# Source: https://upstash.com/docs/devops/developer-api/authentication.md

# Source: https://upstash.com/docs/qstash/api/authentication.md

# Source: https://upstash.com/docs/devops/developer-api/authentication.md

# Source: https://upstash.com/docs/qstash/api/authentication.md

# Source: https://upstash.com/docs/devops/developer-api/authentication.md

# Source: https://upstash.com/docs/qstash/api/authentication.md

# Authentication

> Authentication for the QStash API

You'll need to authenticate your requests to access any of the endpoints in the
QStash API. In this guide, we'll look at how authentication works.

## Bearer Token

When making requests to QStash, you will need your `QSTASH_TOKEN` — you will
find it in the [console](https://console.upstash.com/qstash). Here's how to add
the token to the request header using cURL:

```bash  theme={"system"}
curl https://qstash.upstash.io/v2/publish/... \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

## Query Parameter

In environments where setting the header is not possible, you can use the `qstash_token` query parameter instead.

```bash  theme={"system"}
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

Always keep your token safe and reset it if you suspect it has been compromised.
