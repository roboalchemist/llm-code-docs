# Source: https://docs.zapier.com/platform/manage/clone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone a version

> Cloning allows you to duplicate an existing version of your integration. This is particularly useful when you want to introduce new features or fixes without altering the original integration. When a previous version of your integration has more than 5 active users, you will need to clone that version to make modifications.

> **Note**: The term “cloning” is specific to the Platform UI and is not used with Platform CLI. However, the concept is similar to updating the version number in your `package.json` file and running [`zapier push`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#push) to create a new version you can access within your Zaps for testing.

## How to clone an integration version

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Manage* section in the left sidebar, click **Versions**.
4. On your existing version, click the **three dots icon**
   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=474baae7334a3792216fdb05aa9d46c1" data-og-width="224" width="224" data-og-height="447" height="447" data-path="images/7ff6381b55b013ebfc2bdda0e4662676.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=cb46fff8ec67fa2457d985d648cd54c0 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e313abdf303e9a672cf855f5546d969e 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9f1f849596f400d6d4dc3a9e3abfd734 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f3bb4c8724bbc9a7c0155fb7513ee2a3 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=4a8f21a16dc8a3f9968988cdd215dc53 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7ff6381b55b013ebfc2bdda0e4662676.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=990e0ffa1867e0efb6f556ab42643f54 2500w" />
   </Frame>
5. From the dropdown menu, select **Clone**.
6. The *Clone Version* dialog box will appear. In the dropdown field, select which **version** you want to clone your existing version too.
   * **Patch (e.g., 1.0.0 to 1.0.1)**: Ideal for backward-compatible changes such as bug fixes or updating help text.
   * **Minor (e.g., 1.0.0 to 1.1.0)**: Use this for adding new functionalities that do not disrupt existing features, like creating a new trigger or action.
   * **Major (e.g., 1.0.0 to 2.0.0)**: Choose this option for changes that are likely to break existing Zaps, like removing triggers or actions, altering authentication methods, or revamping the entire integration.
7. Click **Clone**.
8. A dialog box will appear confirming you've cloned your version.

Now you can make edits and improvements to your integration.

## Video Tutorial

You can refer to this video on cloning an integration version:

<video controls src="https://cdn.zappy.app/be796f184a0787c5cd848fb8c9dbd8ed.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
