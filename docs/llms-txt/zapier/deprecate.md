# Source: https://docs.zapier.com/platform/manage/deprecate.md

# Deprecate or delete a version

> Deprecation is an optional process that allows you to set a date from which an integration version cannot be used anymore. Zapier is normally a “set it and forget it” experience for users, so use this feature carefully. Only if the version will no longer function, should it be deprecated. Please note that deprecating a version is significantly disruptive to our mutual users if a migration to a different version is not possible.

When users use any but the promoted version, they will [see the version displayed](https://help.zapier.com/hc/en-us/articles/18755649454989-App-versions-in-Zapier) and be able to manually update to the promoted version.

## What happens after setting a version to deprecate

The deprecation date must be between 3 weeks and 1 year in the future. We won't communicate the deprecation until 2 weeks before the deprecation date. This gives you time to migrate users to a newer version, before we start notifying them that they need to manually migrate.

### 1. Email notification

A notification email will be sent exactly 14 days before the configured deprecation date. This email includes the deprecation reason that newer versions of the Zapier CLI ask you for. We do recommend supplementing these automated messages by also notifying your general user base through in-app announcements or email marketing campaigns. For privacy reasons, Zapier cannot provide you with an email list of users of your integration.

### 2. Deprecation date reached

* Zaps that haven't been updated will be automatically paused.
* A second email, titled “X Zaps paused over deprecated apps,” will be sent out to those users. Customizing this email is not possible.
* Any attempts to test triggers or actions on the deprecated version will result in an error, and Zaps that use it cannot be enabled.
* The deprecated version will be labelled as “Deprecated” in the Zap editor, with a prompt for users to update to the latest version.

### 3. Post-deprecation

After the deprecation date, the version will still be visible in the Versions page for your future reference. Users will not be able to see the version once they select a different version in their Zaps.

## Deprecate a version with Platform UI

To deprecate an integration version:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Manage* section in the left sidebar, click **Version**.
4. Click the **three dot** icon in line with the integration version you want to deprecate.
5. Click **Deprecate**.
6. In the dialog box, add the **Deprecation Reason** and **Deprecation Date**. You can set a deprecation date anytime between 3 weeks and 1 year from the current date. The deprecation reason will be used in user notifications.
7. Click **Deprecate**.
8. Click **Close**

## Deprecate a version with Platform CLI

To deprecate an integration version use the command `zapier-platform deprecate` (or deprecated `zapier deprecate`). Learn more about [Platform CLI commands](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#deprecate).

## Deleting deprecated versions

After your version has been deprecated, you have the option to delete versions entirely. Exercise this option with extreme caution. Deleting a version makes it permanently inaccessible, both to you and to your users. Deleted versions cannot be restored by Zapier Developer Support. Deletion should be a last resort, used only when you are certain that the version will never be needed again.

Deletion is also only possible when 0 users remain on a version. The count of users on the *Versions* page includes live Zaps only. If you're seeing the error `Unable to delete app version`, this can be caused by users on that version not included in the visible count (paused Zaps, app authentications for example).

<Frame><img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=22d014a182a3169a62238e8e2e23a318" alt="" data-og-width="776" width="776" data-og-height="505" height="505" data-path="images/1722db1a2658ec77e47f5d4de58720ff.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=e4b04fc08b3d5bd2359037176fa4327b 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=abcc0d49596c98ff451558450f541318 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=0ff51ad08a85ed43317eecc42b815a3d 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5ba0e06e24da18df13bcb59510de9b13 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=46f877d0b86b65e0d51048a6b9041158 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1722db1a2658ec77e47f5d4de58720ff.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=351d94908be937998cdf9ebbff9e42a4 2500w" /></Frame>

***

### **We’re no longer supporting our integration and would like to remove it from the app listing. How can I unpublish the integration and deactivate it?**

For any public integration, the first step is to revert that integration to private, which will prevent new users from seeing it in the Zapier App Directory or in the Zap editor.

Once the integration is private, you can deprecate each version of that app (except the latest version, which will remain private if there are users still on the version). to deprecate an integration version, please follow the steps outlined above.

If the product's API endpoints will be shutdown, any users still using that now-private app in their Zaps, will begin to see errors when requests are made to those endpoints and their Zaps will eventually be turned off, no longer making requests.

That said, if you want to proceed with this, please reach out to Developer Support and we’ll help you revert your integration to private so that you can proceed with the next steps.

[*Need help? Tell us about your problem and we'll connect you with the right resource or contact support.*](https://developer.zapier.com/contact)
