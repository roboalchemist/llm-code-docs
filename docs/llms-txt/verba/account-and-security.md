# Source: https://docs.verba.ink/guides/account-and-security.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Account and security

> Magic-link login, 2FA, API keys, connected services, and account safety.

## Questions this guide answers

* How does passwordless magic-link login work?
* How do I enable and verify 2FA?
* How many API keys can I create?
* What happens when I revoke a key?
* Can I disconnect Patreon anytime?

## Passwordless login (magic link)

Verba supports passwordless email auth.

Flow:

1. Request a magic link with your email.
2. Open the email and click the link.
3. Verba verifies the token and signs you in.

Important behavior:

* Magic links expire after `20 minutes`.
* You can request a resend.
* Invalid/expired links must be requested again.

## Two-factor authentication (2FA)

### Setup

* Open settings security section.
* Generate QR/secret.
* Confirm with a valid authenticator code.
* Save backup codes.

### Login verification

During protected login flows, Verba may require:

* 6-digit authenticator token
* Or 8-character backup code

Backup codes are one-time use and removed after successful verification.

### Disable 2FA

* Requires valid 2FA verification to disable.

## API keys

### Key format and limits

* Keys use prefix: `vka_`
* Active key limit: up to `3` keys

### Key lifecycle

* Create from Settings -> Security -> API Keys.
* Full key value is shown once on creation.
* Revoke any key instantly from dashboard.
* Revoked keys stop authenticating immediately.

### Authentication headers

Use one of:

* `Authorization: Bearer vka_...`
* `x-api-key: vka_...`

## Connected services

### Patreon linking

* Patreon can be linked from settings.
* Tier/benefits sync with account profile.

### Patreon disconnect guard

Disconnect may be blocked while an active Patreon subscription is still attached.

## Profile asset uploads

From settings:

* Avatar/banner image uploads are validated and moderated.
* Keep files under dashboard limits (commonly `10MB` for profile uploads).

## Deleting your account

Account deletion removes your account data and associated records.

Behavior includes cleanup for:

* Verbs and related references
* Group/DM associations
* Messages and conversation records tied to deleted entities

Group ownership handling:

* If other members exist, ownership can transfer.
* If no replacement exists, owned groups may be removed.

<Warning>
  Account deletion is destructive. Export or copy anything you need before
  confirming deletion.
</Warning>

<CardGroup cols={2}>
  <Card title="Public API v1" icon="code" href="/guides/api">
    Full endpoint docs for authentication, requests, streaming, and errors.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fix login, 2FA, and API key issues quickly.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
