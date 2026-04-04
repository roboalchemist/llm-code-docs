# Source: https://getlago.com/docs/guide/security/api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Keys

## Reveal and copy API key

To copy your API key, go to the **Developers > API keys** section and click the Reveal button.
This will display the selected API key, allowing you to copy it to your clipboard.

<Frame caption="Reveal your API keys">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2e281a1c80d756075f2fd5e0f7ef3d11" data-og-width="2720" width="2720" data-og-height="1536" height="1536" data-path="guide/security/images/reveal-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9300e760a5cdc28c7d14130ad1305aa2 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=60e78fb55eb46625a44109e589a1b702 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=fe2ea651938bf638c19b87adacdfc140 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=54d15ce5b724c8815a8d51ec4d42b994 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e86b03de7951491aee8767cd7a0d8fe9 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/reveal-api-key.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ceec5ab391fe8ef4317c6aa715505d92 2500w" />
</Frame>

## Create an API key

<Info>
  **PREMIUM FEATURE** ✨

  This feature is only available to users with a premium license. Please
  **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago
  Self-Hosted Premium.
</Info>

To create a new API key, navigate to the **Developers > API keys** section and click the Add a key button.
You will be prompted to provide an optional Name. While naming the key is not mandatory, it is highly recommended to make it easier to identify later. Once created, the API key will be ready for immediate use.

Whenever a new API key is created, all organization admins are notified via email. The key becomes active and usable instantly.

## Rotate an API key

### Rotate API key instantly

To rotation an API key, navigate to the **Developers > API keys** section and click the Rotate API key button. A new API key will be generated instantly, and the previous key will immediately become inactive and unusable.

Whenever an API key is rotated, all organization admins receive an email notification. The newly generated key becomes active and ready for use immediately.

### Schedule an API key rotation

<Info>
  **PREMIUM FEATURE** ✨

  This feature is only available to users with a premium license. Please
  **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago
  Self-Hosted Premium.
</Info>

With this feature, you can schedule an API key rotation for a future time. Options include rotating the key `now`, in `1 hour`, `24 hours`, `48 hours`, or `7 days`. By hovering over the current API key, you can view the scheduled rotation time.

Whenever an API key is rotated, all organization admins receive an email notification. The newly generated key becomes active and ready for use immediately, while the previous key remains available until the scheduled rotation time is reached.

## Set API key permissions

<Info>
  **PREMIUM FEATURE** ✨

  This feature is only available to users with an enterprise add-on. Please
  **[contact us](mailto:hello@getlago.com)** to get access to this feature.
</Info>

When creating or editing an API key, you can configure permissions for all objects exposed in the Lago API.
Permissions can be set individually for each object, allowing `read`, `write`, or `read and write` access.

If an API key lacks the necessary permissions to access a specific endpoint, the API will deny the request and return an appropriate error response.

<Frame caption="Permissions on API key">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ee95b833eb61cdf7714c65497f39f5c8" data-og-width="836" width="836" data-og-height="591" height="591" data-path="guide/security/images/api-key-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3d9ba01fd0634919971255663a18e32f 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a26ec9c54cc32f0f46c7cf9272f0e461 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=03f2252bd3cc600b39d34b82dde1f10b 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9c6bc54c7ea3e797c8b26cbbe6229517 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e78f3c1795f67191af9eb57f73f39f94 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/security/images/api-key-permissions.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a1bcf4770f990fb8bd5955079ebb635c 2500w" />
</Frame>

## Delete an API key

To delete an API key, navigate to the **Developers > API keys** section and click the delete button. The API key will be permanently deleted and immediately rendered unusable.
Please note that you can only delete an API key if your organization has more than one API key defined.

## API key "Last used" field

For security purposes, a Last used field displays the last time this API key was accessed. This serves as a helpful indicator to determine if the key is still actively in use.

<Info>
  For scalability reasons and to avoid adding complexity to a high-traffic endpoint, we have decided that the events endpoint will not update the `Last used` field.
</Info>
