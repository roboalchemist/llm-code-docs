# Source: https://docs.base44.com/Building-your-app/Update-to-new-infrastructure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating your app to the new infrastructure

> Update once to get faster performance, greater stability, and new capabilities.

***

## About the new infrastructure

We have upgraded Base44’s infrastructure to deliver faster load times, improved performance, greater stability, and support for advanced new features. To get these benefits, you need to update your app to the new infrastructure manually.

This upgrade prepares your app for everything coming next on Base44, such as the ability to add [NPM packages](https://docs.base44.com/Building-your-app/NPM-packages) to your app. It also makes sure your app is ready for future updates, new tools, and continued improvements as Base44 evolves.

<Warning>
  **Important:**

  * New apps are built on the new infrastructure and do not need to update. If you do not see the update button in your app editor, then you are already using the new infrastructure.
  * This is a **one-time update** that is required for older apps built on the old infrastructure.
  * You should complete the update by **February 1, 2026**. After this date, if you have not updated yet, your live app keeps running and your data stays safe, but the editor for that app is blocked. You cannot edit or publish changes until you update to the new infrastructure. You can edit your app again as soon as you complete the update.
</Warning>

<Tip>
  To help you get started with the new infrastructure, you automatically receive **15 credits** when you update your app.
</Tip>

***

## Updating your app

You can update your app with a simple click from inside your app editor.

<Note>
  **Before you begin:** We recommend [backing up your app data](https://docs.base44.com/Building-your-app/Managing-your-app-data#exporting-data) before updating, in case you need to restore anything after the update.
</Note>

**To update your app:**

1. Go to your app editor.
2. Click **Update Infrastructure** at the top.

<Frame>
  <img src="https://mintcdn.com/base44/9Q7KziXXEVqbm_ra/UpdateInfra.png?fit=max&auto=format&n=9Q7KziXXEVqbm_ra&q=85&s=f13d2667a4ad3c4c6a41d49f4ed61816" alt="Updating your Base44 app to the new infrastructure" title="Updating your Base44 app to the new infrastructure" className="mx-auto" style={{ width:"100%" }} width="911" height="128" data-path="UpdateInfra.png" />
</Frame>

If you experience any problems, use the AI prompt that appears to fix the issue.

***

## Troubleshooting

Most apps move smoothly, but some issues may occur during the update. Follow the solutions below or reach out to support if problems persist.

**You might experience the following issues:**

* **Preview not working:** Build errors in auto-generated files, or preview not loading as expected.
* **Dynamic routes failing:** Files with \[param] in the name (for example dynamic route folders) causing syntax or routing errors.
* **CSS or styling differences:** The production build looks different from preview after the update.
* **Import path errors:** Code referring to files that were moved or renamed during the migration.

**What you can try:**

* If any errors happen during the update, you will get a **Resolve with AI** notification. You should let the AI fix the issues for you.
* If your app is broken right after updating and you see a Revert option in the editor, switch back to the previous infrastructure temporarily while you investigate.
* If preview works but production does not:
  * Be aware that preview may load CDN resources that production does not include.
  * Make sure any CSS frameworks such as Tailwind are bundled correctly for production.
  * Clear your browser cache and any CDN caches after rebuilding, then try loading the live app again.

**When to contact support:**

* Errors appear in auto-generated files (such as pages.config.js or other files you did not create yourself).
* The issue looks related to platform-level build scripts rather than your own code.
* Reverting to the old infrastructure and updating again produces the same errors.

<Note>
  **Note:** Some migration issues require platform-level fixes. When you contact support, include the exact error messages, file paths, and your app URL so we can investigate faster.
</Note>

***

## FAQs

Click a question below to learn more.

<AccordionGroup>
  <Accordion title="Why am I seeing errors in unused pages?">
    On the old infrastructure, errors in unused pages were ignored. In the new infrastructure, these errors appear in the **Resolve with AI** tool. You can either fix the errors with "Resolve with AI," or ask the AI to remove pages that are no longer needed by your app.
  </Accordion>

  <Accordion title="Why am I seeing errors about import paths after updating?">
    Some errors may occur if your code uses incorrect import paths (for example, using the wrong file extension such as `.js` instead of `.jsx`). If you see an import path error, copy the error message and let the **Resolve with AI** tool fix it for you.
  </Accordion>

  <Accordion title="What should I do if I get errors about legacy SDK usage?">
    You might encounter errors in code using dynamic imports with the legacy Base44 SDK (for example, `import('@entities/all')`). You can resolve these by asking the AI to remove any usage of the legacy SDK from your app.
  </Accordion>

  <Accordion title="Can I revert back to the old infrastructure?">
    Reverting back to the old infrastructure is possible, but it’s not recommended. When moving your app back, you lose access to the latest performance, stability, and feature improvements. You also risk missing out on important updates in the future.

    <Warning>
      **Important:** After February 1, 2026, you will only be able to edit your app if it’s on the new infrastructure.
    </Warning>

    To help you make the transition, 15 free credits are added to your account so you can test and update your app as needed. We strongly suggest staying on the new infrastructure to get the best experience and updates. Our support team is here to help, so please let us know if you are experiencing issues with the update.
  </Accordion>

  <Accordion title="What happens if I do not update by February 1, 2026?">
    If you do not update by this date, your live app keeps running as normal. People using your app can still access it, and you can still open your app dashboard to view data and manage access or invite teammates.

    However, the editor for that app is blocked. You cannot open the editor, make changes, or publish new versions until you update to the new infrastructure. As soon as you complete the update, you can edit and publish again.
  </Accordion>

  <Accordion title="What happens if I have multiple apps to update?">
    You will need to update each app individually from the app editor, there is no way to update all your apps in one go.

    You will receive 15 credits as a one-time gift to help you enjoy the new experience. You might need to use some credits if you need to resolve any issues during the updates, but this is uncommon. Note that you do not receive extra credits for updating additional apps - credits are given per user, not per app.
  </Accordion>
</AccordionGroup>

**Still need help?**

If the problem persists, [contact us](https://app.base44.com/support/conversations) and we will be happy to help. For a faster response, include the name or URL of your app, the version of your browser and operating system, and a description or screenshot of the problem.


Built with [Mintlify](https://mintlify.com).