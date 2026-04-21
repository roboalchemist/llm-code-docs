# nsc login

Authenticate the `nsc` CLI to access Namespace products.

## Basic Usage

```bash
nsc login [--session]
```

## How It Works

When you run the command:

1. The CLI opens your browser to a login URL
2. You complete the authentication flow
3. The CLI confirms successful login once complete

## Key Option

**--session**: Creates a long-lived, revocable session that can be managed in your account settings at cloud.namespace.so/user/sessions.

## What You Can Do After Login

Once authenticated, you can use the nsc CLI to:

- Create ephemeral instances
- Build container images
- Run containers
- Set up previews
