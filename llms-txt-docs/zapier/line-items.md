# Source: https://docs.zapier.com/platform/build/line-items.md

# Add line item group field to actions

> Input fields in Zapier add one item each time the Zap runs. But, if you want users to be able to add multiple items in a single Zap run, then this can be achieved by using a line item group. This group takes line items, which are comma-separated values, and adds each instance of the values to the app in a single Zap run.

<Info>
  **Tip**: Learn more about line items from Zapier's
  [guide](https://zapier.com/blog/formatter-line-item-automation/) and [help
  documentation](https://help.zapier.com/hc/en-us/articles/8496277737997).
</Info>

Line items can be challenging for users to work with as a concept, so make sure to consider what a user would be inputting and do not add line item group fields unless there is a clear use case for them.

## Before adding a line item group

Before adding a line item group to an action:

* You should have already added an [action](/platform/build/action) where this line item group would be added.
* Your app's API should be able to accept and work with line item values.

## Add a line item group

To add a line item group to an action:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section in the left sidebar, click the **name of your action**.
4. Click the Input Designer tab
5. Click **Add** to display the dropdown menu and select **Line Item Group**.
6. In the **Line Item Group Label** field, add a name for the Line Item Group. This should be something users would recognize as being a set of values where each one would be added individually.
7. In the **Line Item Group Key** field, add a key for the Line Item Group. This will let Zapier identify this group internally.
8. Click the **Add Line Item** button.
9. Add in the relevant fields as you would for an [input field](/platform/build/field-definitions#add-fields). Each field that you add here will be received as line item values. Note that the *Allows Multiples* and *Alters Dynamic Field* options will not appear, as those options cannot be used in line item fields, as they are mutually exclusive.
10. After adding all the line item fields, click **Save**.

Your new Line Item groups will show up in the Zap editor as a separate block with the different line item input fields within:

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=19eb1b25cc5a5ca74214b338d930d9f4" data-og-width="880" width="880" data-og-height="626" height="626" data-path="images/41f81ef42d5101767810a9ffc5626e95.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e8b84bfa15c94b386f99f32f7a5083d6 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3ca36a334aa9ada7872d6db4783c5704 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=906b1180708828e4983c3e5d7b8e8065 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=760221ad9b81c53ead582ac0dd639cf8 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4875e8603320d269d07e5dd163e6326a 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41f81ef42d5101767810a9ffc5626e95.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d538c5679f926300880307faff13253a 2500w" />
</Frame>

Users will need to map line item values from earlier steps in their Zap into the fields within the line item group. They would be sent to your API as an array of individual objects. Users cannot input comma separated values into a line item field, they need to be provided from the trigger or a prior action in line item format for them to be sent this way.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8e0d1a3652b2391fd142a95a0954cbaf" data-og-width="931" width="931" data-og-height="232" height="232" data-path="images/533efc7f7719fa85587f72b04204371f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9459fdf850001f0b72521c51b3762449 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3488e91261bd732bf7c9a5122dc8b6bb 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=319af94b3fe20412bc1eae2f0d983e2a 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=97c07b8d93a20761fdf43b196d9a8231 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=c05eeba801d369b3c74e1ff6dff5b608 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/533efc7f7719fa85587f72b04204371f.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f45b0f001bc163ed6a465d3a1c7005f7 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c55426420b374b83be9c550631815943" data-og-width="356" width="356" data-og-height="149" height="149" data-path="images/a7bad08984545eb39e96ed2782660737.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=ab0cfdb124597fcb5c778fe1d9aa462f 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a9769bd18599214aec8bedefc0598e59 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=473ec41d9bdba15f1a507ad6280144ec 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d4de9e21d8d32a2ea9b571f6cbbe4671 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e4f9f382443c128a7f95c121587641bd 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a7bad08984545eb39e96ed2782660737.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0b87bf389239980d036a4f04ad062fe5 2500w" />
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
