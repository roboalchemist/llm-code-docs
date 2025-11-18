# Source: https://docs.zapier.com/platform/build/pagination-trigger.md

# Use pagination in triggers

> By default, Zapier triggers fetch new or recently updated data to start Zaps, and only need to find the most recently added items. Triggers can also be used to populate [dynamic dropdown fields](/platform/build/add-fields#dynamic-dropdown), and there they need to find all possible items to populate the field.

These triggers used for populating dynamic dropdown fields will often find dozens or hundreds of items. Many APIs let you split the results into pages. The first API call will return the first set of results — often 20 to 100. The items from this result would be seen as options in the dynamic dropdown field. If you want additional entries, you can make a new API call requesting page 2 and get the next set of results, iterating through the pages until the API has sent every possible option.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=da18230fd58c644c3ecfe9ad14e48191" data-og-width="958" width="958" data-og-height="1016" height="1016" data-path="images/f59291e5a74d1977648850f84513e33e.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=9bc8c64ca4d948e93fc9f217b2b95d73 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=b71a371e9c7e921f03362a3cfec5ad32 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=fea9924b13021855d0ddcaa0cc69cd2c 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=aedaf366f969c7c05c0136a8e2031998 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=bf545a1dfef50d8d26170dac03be8c9f 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f59291e5a74d1977648850f84513e33e.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e5688b3cfa1663dc2cca686dc75c4bc2 2500w" />

  {" "}
</Frame>

## 1. Enable pagination

* Log into the [Platform UI](https://zapier.com/app/developer).
* Select your **integration**.
* In the *Build* section in the left sidebar, click on the trigger that should power the dynamic dropdown field. This can be an existing trigger or a new trigger you set as *Hidden* if its only purpose is to power the dynamic dropdown.
* Go to the **API Configuration** tab
* In the **Configure your API Request** section, select the **Support Paging** checkbox, which should only be applied to triggers built to power dynamic dropdown menus. This enables Zapier's `bundle.meta.page` value which tracks the pages Zapier has loaded, along with a Load more option in the user-facing Zapier editor's dropdown menus.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=75d9a8ec4b6064ebfd0c1c63ef1ffbf2" data-og-width="905" width="905" data-og-height="153" height="153" data-path="images/4680b6dd27b3db71b8364177e351fdd5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a57d369b922354377a9f0f0e7fbdae9f 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b9ddb139e3b17466482ef177c22a84b1 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7c053bdef45096f4054b9742b32b5e8b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3489dd4ab1e0e25f3b25d050caad271e 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=304ddda4339b7c193b740434fce480ed 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4680b6dd27b3db71b8364177e351fdd5.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3f161ee4cf5d1a086ae98eac8be42b93 2500w" />

  {" "}
</Frame>

* In the API Endpoint section, click *Show Options* to include `bundle.meta.page` in your API call as Zapier does not include that automatically, then add a new URL Param for your API's paging option (or optionally add it to your HTTP Headers if your API expects the paging value there). Use the page request field name from your API on the left, and `{{bundle.meta.page}}` on the right to have Zapier pull in the correct page value.
  <Frame>
    {" "}

    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=7d940f4c2046a93fdf63fdde774cb269" data-og-width="1504" width="1504" data-og-height="1411" height="1411" data-path="images/2492cb37ec953861cceaf243c0625285.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=036f4bfd1760ca31ce2712f59c33a05c 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=d080f580bd5cc1a81e496574cad8095f 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f224813cb1a5424306024611f0d480fa 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5ed8dfcfef37abe2e1c28d1f8080420e 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=08280eca90ea31d4ede9f4a77bb3e087 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/2492cb37ec953861cceaf243c0625285.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8ef6c59f3dcf23dae5e6f1b30feef2a7 2500w" />

    {" "}
  </Frame>

Note that Zapier's `bundle.meta.page` value uses zero-based numbering. The first time Zapier fetches data from your API, it uses a page value of 0, followed by 1 the second time, and so on. If your API expects the first API call to request page 1, with 2 for the second page and so on, you'll need to [switch to code mode](/platform/build/code-mode) and add `+ 1` to `bundle.meta.page`. So pagination in the code would look like the below (substituting `page` with the correct field name your API uses for pagination):

`'page': bundle.meta.page + 1`

<img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e3afbcd2509fecfca972875e7d816688" alt="Zapier pagination code mode" data-og-width="956" width="956" data-og-height="648" height="648" data-path="images/8e7923caa73ff68ea6061d61ad37e451.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9cb66ca46f2f8105b5160f94faefd4ef 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=265e7604b18ecf1910294457531908b6 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6f52cb871e2f414ffce01f170f1b67b8 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=679c7fc69d054dcd5ae499d0277c8bd9 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8f538cfc140d1220df85fe601ff1aa3f 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7923caa73ff68ea6061d61ad37e451.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d3fd7747b7f764d5c7a06efabbf7f2da 2500w" />

* Test the API Request in the Platform UI and check the HTTP tab to see the request Zapier sent your app. Zapier should show a `page=0` value (or the correct term for pages in your API) under the Request Params header by default, or `page=1` if you're customizing the page requests to start at 1.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=92751d2cb36ff4d37ebdda80dd7f0af5" data-og-width="1047" width="1047" data-og-height="1138" height="1138" data-path="images/78b76bad2188b7594325c2c6bb85f121.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=57b6378888c21f5dc99627de2d953e3e 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3df2c5343c713c0693899ec199a7fa42 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=c9d69103fc45439fc2360beaf9d5b7d0 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d2553d50b4ee98779dcac7d88f4ebe8f 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=41528b8a144f5d6666e967c4e1c1645e 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/78b76bad2188b7594325c2c6bb85f121.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=583487f05abd9f323760819fafbb6a2f 2500w" />

  {" "}
</Frame>

## 2. Test pagination

To test your paginating trigger:

* Build an action in the Platform UI that uses this trigger in a dynamic dropdown.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=11c5023c9ee0e99f90066878e8b2f666" data-og-width="2014" width="2014" data-og-height="1943" height="1943" data-path="images/d7d14e885062e466c4bcbbab8dcfd535.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3530e7a7c043ccb0b986e406a87ea00c 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=918ce0374a78a8765876fb4a0c14ea59 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b84b500a8ab884d9cd9b31ce3d22875b 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=21382586e8c8d0c5ecd0e0a8aed1aa6d 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=43769ac63f40fe3fb71ae0bab1ffa9aa 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d7d14e885062e466c4bcbbab8dcfd535.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=5c1e61ff8d9c1a406053f02e5194b2dd 2500w" />

  {" "}
</Frame>

* Make a new Zap in the user-facing Zap editor that uses your action with the dynamic dropdown field. Click the dropdown field, scroll to the end, and click the **Load More** button. Repeat until it loads the last options, which will show a *We couldn't find any more choices* prompt.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0dec03879cf03f4a92eced7f2b381d49" data-og-width="1546" width="1546" data-og-height="1290" height="1290" data-path="images/b2d1a5bf597c95f8615ca009ee7d66c6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9a7bad827dbd92c23f0e8f46222b9888 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=51038ac5fac8d39ff6cde01603fc1e62 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2667b39bd9a54cfecefa2eadf201c734 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=813d3d964306635ec3a5bc23da36376b 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=23c12cd7c0f0c16ed381307b1bd3dd6d 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b2d1a5bf597c95f8615ca009ee7d66c6.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=86593a3ae72faa2279642e336b738fd8 2500w" />

  {" "}
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
