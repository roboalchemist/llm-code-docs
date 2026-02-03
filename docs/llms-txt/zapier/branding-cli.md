# Source: https://docs.zapier.com/platform/publish/branding-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add integration branding in Platform CLI

> When you make a new integration in Zapier CLI, you can add the app's name, description, and homepage to the `package.json` file.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b8d3978e083577ea421edcb2f4f7ca9e" data-og-width="800" width="800" data-og-height="439" height="439" data-path="images/5373ba1686dbea3e9d942b56101a5b40.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=953aec7e058e99a7cebde561ae703885 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=63a2d17f8f903f2f45823b930c5551e2 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d5f572971242cf9b37d6a00fbd1ac152 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d901278c17892036261bd7547f43fc2e 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=ec9b34551d1932358947ab9b89c8b88b 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/5373ba1686dbea3e9d942b56101a5b40.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=22be15d63488489c3961cb834718939b 2500w" />
</Frame>

The rest of your app's branding needs to be added in Zapier's online Platform UI.

Focus first on building your integration. When you've added your app's core details, authentication, triggers, and actions, push your integration to Zapier with a `zapier-platform push` (or deprecated `zapier push`) command. Zapier will use the name you added in the CLI integration settings, along with a placeholder icon for your app.

Then, before launching your integration, add your app's branding via Zapier's Platform UI at [zapier.com/app/developer](https://zapier.com/app/developer). There you will see every Zapier integration you've built. The top *Integrations* section includes every app you've added via Zapier's Platform UI or CLI. Look for the integration you built with Zapier CLI and click its name.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=29d017e36489ccc4c7be6aede8dda02e" data-og-width="1112" width="1112" data-og-height="691" height="691" data-path="images/21501f70d3d15a341e6dc7ea90690ee6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=4e4d4f35468ebb331fec80a0b57ab4d9 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8ee72db2e083b157fc92b4015b2f7c75 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=182d73bc7370e33e9b7e556c858f3f4e 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=896d75a11bb9f81183f59f0cc5bd0c55 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1bf18f6dbae57f85f43228800b19244b 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/21501f70d3d15a341e6dc7ea90690ee6.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8dea0230e169713a920dd11c732bae74 2500w" />
</Frame>

You can't edit authentication, triggers, and actions in Zapier's Platform UI for integrations built with Zapier's CLI. But you can edit branding.

To do that, click the gear icon in the upper left hand corner near your app's name and placeholder icon. You can then edit your integration's name and description, and upload your app's icon (a square, transparent PNG at least 256x256px). Below that, you can set your app's category and other brand settings. Click *Update* to save your settings.

You can then make further changes to your integration in your Zapier CLI code and push them to Zapier anytime without affecting your branding. If you ever need to change your app icon or other branding again, just come back to the [Zapier Platform UI](https://zapier.com/app/developer) and edit it as before.

*→ Check [Zapier's app logo, name, and description guidelines](https://platform.zapier.com/partners/planning-guide#app-logo) to ensure your app's branding fits into the Zapier platform.*

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
