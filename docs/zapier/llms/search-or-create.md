# Source: https://docs.zapier.com/platform/build/search-or-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a search or create action

> When adding a _search_ action type, you'll see the option to _Pair an existing search and a create to enable “Find or Create” functionality_ in the _Settings_ page. This embeds the _create_ inside the _search_ step to find or create items in one step of the Zap.

## Add a *create* action

* Add a relevant *create* action to your integration. If your *search* action is looking for contacts, say, you would need a *Add New Contact* action to pair with it. Open your integration's *Actions* page in a new tab and add a new *create* action if your integration does not have an appropriate one already.

## Configure the *search* action

* Back in your new *search* action's settings, check the *Pair an existing search and a create* box

* Select the relevant action from the *Create Action* menu and add a new label that Zapier will show on this step if users choose to have the action create new items as well.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=1a52c08c51162ee379c2ab71d50aaea9" data-og-width="1167" width="1167" data-og-height="420" height="420" data-path="images/41334f793dfce14d21e6c35361179721.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=adf94fb86e11b476eb52cd5dbf9b7fdc 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7259dae09954d932591b5c6369a0e678 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=6e3fa3b6e60e39b2755de578be564e15 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a39deac38b8a4ca67f7ffda3dff3220a 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a919d8a40c67f9e16dbb1f34eeaa9d1d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/41334f793dfce14d21e6c35361179721.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=cb7e66c3f45e7b44a248fd1e58472772 2500w" />
</Frame>

* When users use the search action in a Zap, Zapier will show your core *search* action settings that you set in the *Input Designer* by default. Then, if users click the checkbox to create an item if nothing is found, Zapier will load the *create* action's input fields inside the search action so users can fill both out.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=6e15bfdf617783b558cc13de77a798fc" data-og-width="1546" width="1546" data-og-height="1717" height="1717" data-path="images/32ba8f867d02cf60cb6c344a0447b5a5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3ff5c8625beb27f2369440bfb32b68c0 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=561a4aa020a442326133c8d24846fb39 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5ed15549c6b0de5b2d9f7438eda61c9e 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5fd12d4ba8ca3968d34e1a684271b141 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=6652fbe412c47225767f8ff8442b346d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/32ba8f867d02cf60cb6c344a0447b5a5.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=09ced71a989489fb1054f550906bcfeb 2500w" />
  </Frame>

* Configure the rest of your search action as normal, including the [Test API Request](/platform/build/test-triggers-actions) and [Output](/platform/build/sample-data) sections.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
