# Source: https://docs.zapier.com/platform/manage/migrate.md

# Migrate users to a new version

> If this isn't the first time you've promoted your app - you might have users on older versions.

If you have made minor, non-breaking changes to improve your integration, you can migrate users to the latest version. When you migrate users to your latest version, it will update all of their Zaps, including Zaps turned on.

## What's the difference between minor and major changes?

Minor changes allow Zaps to continue to work as normal. Minor changes need to be compatible with both the previous and new version.

When migrating users to a new version, only active Zaps (not [draft](https://help.zapier.com/hc/en-us/articles/8496260938125-Create-drafts-of-your-Zaps)) are migrated. In some cases, after migration, users that have drafts with an older version of the app may edit that draft and publish the draft, thereby publishing a Zap with an older version of the app.

Zapier recommends migrating a small portion of your existing users to the new integration version to make sure everything is working as expected. Monitor the logs in the Monitoring tab, and migrate the remainder of your users to the new version when ready.

Major changes would cause active Zaps to error and potentially turn off. They would require users to manually update the Zap in order to get it working again. Learn more about [breaking changes to your integration](/platform/manage/planning-changes), best practices and the user impacts.

Zapier recommends not to attempt to migrate users for major changes. **Migration is not required unless the older version will no longer function.** If necessary, you can [deprecate the version](/platform/manage/versions#deprecating-versions) to prompt users to [manually update to the latest integration version](https://help.zapier.com/hc/en-us/articles/18755649454989-Update-to-the-latest-app-version-in-Zaps). Please note that deprecating a version is significantly more disruptive to our mutual users than migrating to the latest promoted version, or than leaving users on an older (now) private version when migration is not possible.

When users are left on an older private version, they will see a [prompt in the Zap editor](https://help.zapier.com/hc/en-us/articles/18755649454989-Update-to-the-latest-app-version-in-Zaps) to encourage them to make the update themselves.

## Migrate users to new version with Platform UI

In the [Platform UI](https://zapier.com/app/developer):

1. In the *Manage* section in the left sidebar, click your **Versions**.
2. On your existing version, click the **three dots icon**
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=474baae7334a3792216fdb05aa9d46c1" data-og-width="224" width="224" data-og-height="447" height="447" data-path="images/7ff6381b55b013ebfc2bdda0e4662676.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=cb46fff8ec67fa2457d985d648cd54c0 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e313abdf303e9a672cf855f5546d969e 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9f1f849596f400d6d4dc3a9e3abfd734 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f3bb4c8724bbc9a7c0155fb7513ee2a3 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=4a8f21a16dc8a3f9968988cdd215dc53 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=990e0ffa1867e0efb6f556ab42643f54 2500w" />
   </Frame>
3. Click **Migrate**
4. The *Versioning* sidebar will appear on the right hand side. You'll need to specify:
   * **From Version**. Select which version
   * **To Version**. Select the new version you wish to migrate new users too.
   * **Note:** Labeled versions, i.e. `1.0.0-beta`, are not eligible for migration and will not show in either dropdown.
5. In the *Which users(s) to migrate* field, select either:
   * **By percentage**. This will allow you to migrate users, based on percentage between 5% to 100%. This cautious approach helps ensure that minor updates haven't inadvertently caused any issues.
     * Select a **percentage**
     * Click **Migrate**.
   * **By email**. To migrate users one at a time, by email. When you select this option, you'll see a toggle that controls the scope of the migration:
     * **Individual**: (Default) Only the user's private Zaps under the user's individual account will be migrated. Zaps that are [shared across the team](https://help.zapier.com/hc/en-us/articles/8496277647629), [shared app connections](https://help.zapier.com/hc/en-us/articles/8496326497037-Share-app-connections-with-your-team), or in a [team/enterprise account](https://help.zapier.com/hc/en-us/articles/22330977078157-Collaborate-with-members-of-your-Team-or-Enterprise-account) will **not** be migrated.
     * **Organization**: Both private Zaps under the user's individual account and Zaps shared across the user's organization accounts will be migrated. **⚠️ Use with caution** as this can break shared Zaps for other users.
     * In the *Email* field, add the **user's email address** attached to their Zapier account.
     * Click **Migrate**.
6. The *Versioning sidebar* will update to show *Update status:Estimating*. Once the migration has been completed, the *Versioning sidebar* will disappear.

Once you're confident that the new version works well, you can go ahead and migrate the rest of your users.

## Migrate users to new version with Platform CLI

For Platform CLI users, it's possible to perform full or partial migrations using the `zapier-platform migrate` command (or the deprecated `zapier migrate` command). See the [CLI documentation](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#migrate) for more details.

**Examples**

```bash  theme={null}
# migrate 100% of your users between version 1.0.0 over to 1.0.1
# (deprecated) zapier migrate 1.0.0 1.0.1
zapier-platform migrate 1.0.0 1.0.1

# migrate 15% of your users between version 1.0.1 over to 2.0.0
# (deprecated) zapier migrate 1.0.1 2.0.0 15
zapier-platform migrate 1.0.1 2.0.0 15

# migrate the specific user user@example.com between version 2.0.0 to 2.0.1
# (deprecated) zapier migrate 2.0.0 2.0.1 --user=user@example.com
zapier-platform migrate 2.0.0 2.0.1 --user=user@example.com
```

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
