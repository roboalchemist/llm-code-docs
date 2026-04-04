# Source: https://docs.zapier.com/platform/manage/promote.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Promote a version

> After your integration has entered the beta or public status, you can set a new default version for public use. This process is called promoting a version.

Prior to promoting a version, run the [automated validation checks](/platform/publish/integration-checks-reference). All Errors and Publishing Tasks must be validated. Warnings are non-blocking and not strictly required to proceed as they would not prevent you from promoting a version, though we do recommend you review them for usability of your integration.

## Promote a version with Platform UI

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Manage* section in the left sidebar, click your **Versions**.
4. On the version you want to promote, click the **three dots icon**
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=65fca4fae14dd38db561fb8c1a28c8a7" data-og-width="1319" width="1319" data-og-height="512" height="512" data-path="images/2ee11c82946187818a9622c4b4bf65bc.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8014625e5be9021b5cbb016f0ff50337 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=383c216798748ad493caf1ee7960a306 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=bddaeadd15fed4c60378631d73a9df3c 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b16c070f2b96648dfc4c22839cd69387 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8c84248f9c2fec740940d3bf46d0171c 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ee11c82946187818a9622c4b4bf65bc.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=56be6d3f26151e67c5871926d8f5b069 2500w" />
   </Frame>
   and **Promote**.
5. Fill in the [changelog form](/platform/manage/user-feedback#3-close-resolved-issues) and click **Promote**. Selecting specific features added and bugs fixed will automatically queue up the issue(s) to be reviewed by our internal team for closure.

> **Note**: If you have a private integration, you will not see the *Promote* option. Instead, you can [share your new version](/platform/manage/sharing) with users.

> **Note**: Labeled versions are not eligible for promotion and will not show the *Promote* option. Clone to a non-labeled version instead, then promote that.

## Promote a version with Platform CLI

In the Platform CLI, you can run `zapier-platform promote [version]` to make the specified version number the new public and default version. Learn more about [promoting a version using the Platform CLI](https://docs.zapier.com/platform/reference/cli-docs#promoting-an-integration-version) .

## What happens after you promote a version?

After successfully promoting a version:

* **Zap templates update**: If there are no breaking changes, all Zap templates will be updated to use the new public version.
* **New triggers and actions**: Any newly added triggers or actions will be displayed on your integration's public app page.
* **User experience**: Users who select your integration for a new Zap will interact with the promoted version by default.

By following these steps, you can seamlessly promote a new version of your integration, ensuring that new users have access to the latest features and improvements.

## Video Tutorial

You can refer to this video on promoting a version:

<video controls src="https://cdn.zappy.app/ecc8ac28dd942caa1621f8ca623a2500.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
