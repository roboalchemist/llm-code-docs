# Source: https://www.activepieces.com/docs/admin-guide/guides/manage-oauth2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Override OAuth2 Apps

> Use your own OAuth2 credentials instead of the default Activepieces apps

<Snippet file="enterprise-feature.mdx" />

## Default Behavior

When users connect to services like Google Sheets or Slack, they see "Activepieces" as the app requesting access. This works out of the box with no setup required.

## Why Replace OAuth2 Apps?

* **Branding**: Show your company name instead of "Activepieces" in authorization screens
* **Higher Limits**: Some services have stricter rate limits for shared OAuth apps
* **Compliance**: Your organization may require using company-owned credentials

## How to Configure

1. Go to **Platform Admin → Setup → Pieces**
2. Find the piece you want to configure (e.g., Google Sheets)
3. Click the lock icon to open the OAuth2 settings
4. Enter your own Client ID and Client Secret

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ae4a69b85e7b43aed22fbb9dd46649f7" alt="Manage Oauth2 apps" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-oauth2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=45966a16aee3040843fe538688b723ec 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=d66ef69ce3fd46f2e057b8fc3a2b42ac 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=00726611c4158525b3aa93ccc78e10c1 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=13d656b4e36b87012b5d170000b96def 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=640a7d4db7ee4c97732e7ed6d8e615cf 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-oauth2.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=33b36a1667c9879a845e9ffa6302678c 2500w" />
