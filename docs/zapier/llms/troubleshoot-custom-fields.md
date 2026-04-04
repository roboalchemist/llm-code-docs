# Source: https://docs.zapier.com/platform/build/troubleshoot-custom-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot custom fields

## Configuring the trigger/action in Zap editor

### Constraint

If your trigger, action, or search supports retrieving custom fields from your API, these are limited to 1000 custom fields, the output of the method to retrieve the fields must be returned within 30 seconds and the response payload must be less than 20MB.

### Errors user will see if constraint is hit

* Slow rendering of the step when it is added or edited in the Zap editor
* Custom fields might not display
* Not all output fields will be available for mapping in later steps
* *“The app did not respond in-time. It may or may not have completed successfully.”*
* *"Response payload size exceeded maximum allowed payload size"*

### Best practice

Here is an example of the way one integration works around all three of these constraints. [Hubspot](https://zapier.com/apps/hubspot/integrations) offers a CRM product, and users often have thousands of custom fields for Company records.

In the ***Create Company*** action, instead of presenting an overwhelming number of custom fields, they present a set of default fields that all companies have, then allow the user to select the other fields they might need from an ***Additional Properties to Retrieve*** dropdown menu field.

The fields chosen are then retrieved by the Zap editor for user editing. This helps in both making sure the request can be accomplished within the time and size limits, and making sure the user can easily find the custom fields important to their specific workflow.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b02eb4ac0554100aa96ff00a68ab8f16" data-og-width="637" width="637" data-og-height="344" height="344" data-path="images/4ac409c47f194303c54adff79fcd693f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=95df1e169bde66df3c9a732ee3858319 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4a5299088cd2ac3fe821626c2e09451e 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=68ea9afcaa3c595b063a24eae873eaf8 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c5aa025f214275ab07fa3aa7d5c03714 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=dc20bd7e371a18b752db182f01b21870 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4ac409c47f194303c54adff79fcd693f.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=52773014cceb7a8a10a2908db04794e4 2500w" />
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
