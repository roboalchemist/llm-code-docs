# Source: https://smartcar.com/docs/connect/advanced-config/flows.md

# Connect Flows

> Connect can be launched with three different workflows (defult, single select, and single select with VIN). Depending on your use case and what information you  have about the vehicle ahead of a launching Connect, you may be able to leverage one of these flows for a more streamlined Connect experience.

<Tabs>
  <Tab title="Default" defaultOpen="true">
    When you launch Connect, users will be able to select the brand of their vehicle from a list before they enter their credentials and grant access to your application.

    <Frame caption="Default Smartcar Connect Flow">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cd906b5876221be223249b7ba0c8ef" data-og-width="3782" width="3782" data-og-height="1942" height="1942" data-path="images/default-connect-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=57674aaf78d5e84ec7acf3a3e987101d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3009ebe305a4b1cbe0559c525f3b8bde 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2d05dffc04980fbac98e83da00a09218 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4c7f94b577ddffff375afe841fe094b5 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dc9a2de37a38d85955d176e3eea6a968 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfc194d9d2adabe6d5b0d2478dbe5954 2500w" />
    </Frame>
  </Tab>

  <Tab title="Authorizing a Single Vehicle">
    In some cases you may only want to connect to a single vehicle, even if there are more than one on your user's connected services account. Smartcar provides two ways for you to do this:

    * Single Select
    * Single Select with VIN

    ### Single Select

    Limits the user's selection on the permissions screen to a single car if there are multiple vehicles on their connected services account. Notice that check-boxes turn into radio buttons, and the call to action wording changes slightly.

    <Frame caption="Grant Screen - Single Select without VIN">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c0ea2b982a0c93a3ea88f57b73e22041" data-og-width="863" width="863" data-og-height="1867" height="1867" data-path="images/single-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a3620d3ee18252ab2ca59ff4e87fe53a 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ebc0df1e6ee5fbb05d56a42e0b326958 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=7976153b366c422d046291d2783b1846 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ef5334216cccf2e27d08afee2e632dd2 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=bd9266503099f1caba742b83d7c9bb94 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=e3e1effe1e6566d0962278db31c4d410 2500w" />
    </Frame>

    To enable Single Select, you can pass `single_select=true` as URL parameter when launching Smartcar Connect.

    ### Single Select with VIN

    In addition, if you know the user’s VIN ahead of time you can pass this over to us in the connect URL. In doing so:

    1. Smartcar  decodes the VIN to get the brand and send the user to the appropriate login form directly
    2. If the owner has more than one vehicle on their connected services account, we’ll only show the VIN that was passed to us on the permission grant screen.

    <Frame caption="Single Select /w VIN: Preamble > Brand’s Login Form > Grant Screen  - no vehicle choice">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f27cd7030d595ec7c56f9a3dd537cfbc" data-og-width="2822" width="2822" data-og-height="1946" height="1946" data-path="images/single-select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=2bed927de3ccb4ffcf2b97bd0451cc0a 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=884a0ea1717068601a7a1ce8e8b6d0c0 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c3adb6503c4c610b99c9cae241e5f65f 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=43e2c5bab7ff3861f6aee498b2ae81b7 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=428c81f882fb76a74c9fbebf816fa50f 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=34424df262f891adcb7281f89fbfc220 2500w" />
    </Frame>

    To enable Single Select with VIN, you can pass `single_select=true` and `single_select_vin=:vin` as URL parameters when launching Smartcar Connect.
  </Tab>

  <Tab title="Bypassing the Brand Selection Screen">
    ### Brand Select

    Instead of having users go through the brand selector screen, you can pass us a brand in the Connect URL and send the user to the appropriate login form directly.

    <Frame caption="Brand Select">
      <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8c25487faed02ad5dfba4e3a853a8ad0" data-og-width="2822" width="2822" data-og-height="1946" height="1946" data-path="images/brand-select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=60a46248faa5b363388cedaee53ef617 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f5c68e202d9fa45e93cfbc145acad703 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6b43c15fd66151bcb7bfbce57bbfb923 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c938d1dd783ddd36b1bcee393fd95769 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8a255483bf29d22f3aaaea0157d64cf3 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3b1a65832e403075d321921f96c928a9 2500w" />
    </Frame>

    To enable Brand Select, you can pass `make` as URL parameter when launching Connect. For example, `make=TESLA`
  </Tab>
</Tabs>
