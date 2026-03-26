# Source: https://coolify.io/docs/troubleshoot/applications/failed-to-get-token.md

---
url: /docs/troubleshoot/applications/failed-to-get-token.md
description: >-
  Fix GitHub access token errors in Coolify deployments caused by NTP time
  synchronization issues affecting JWT 'iat' claim validation during
  authentication.
---

# Failed To Get Access Token

Your deployment failed because it cannot get the access token from GitHub.

The error is usually related to NTP time synchronization issue.

## Error

`'Issued at' claim (iat) must be an Integer representing the time that assertion issued.`

## Solution

You must do the same as the [2FA Stopped Working](/troubleshoot/server/two-factor-stopped-working) solution.
