# Source: https://documentation.onesignal.com/docs/en/apple-app-privacy-requirements.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Apple App Privacy Requirements

> Understand how to accurately disclose your use of OneSignal in your iOS app to comply with Apple's App Privacy requirements. Learn which data types OneSignal collects and how to report them in App Store Connect.

Starting December 8, 2020, Apple requires a [privacy disclosure for all new apps and app updates](https://developer.apple.com/app-store/app-privacy-details). You must complete the privacy questionnaire in the App Privacy section of [App Store Connect](https://appstoreconnect.apple.com). Apple's official instructions are [available here](https://help.apple.com/app-store-connect/#/dev1b4647c5b).

As OneSignal is a third-party service, it is your responsibility to accurately disclose what data you collect and how it’s used through OneSignal.

By default, OneSignal collects select **in-app purchase data (Consumable)** and **usage data** such as session activity and notification clicks. If you collect additional information via **Data Tags**, **Outcomes**, or **custom integrations**, you must disclose that as well.

## Data types and their relevance to OneSignal

Use the following table to determine which data types you must disclose when using OneSignal:

✅ = Required when using OneSignal
💡 = May be required, depending on configuration
❌ = Not required when using OneSignal

| Data Type            | Required?                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contact Info**     | 💡 If you collect personal identifiers (e.g., name, email) using Data Tags or Outcomes                                                                                                 |
| **Health & Fitness** | 💡 If you collect health data via custom tags or Outcomes                                                                                                                              |
| **Financial Info**   | 💡 If you collect financial data through tags or Outcomes                                                                                                                              |
| **Location**         | 💡 Only if your app requests and collects location data, and sends it to OneSignal                                                                                                     |
| **Sensitive Info**   | 💡 If you collect sensitive user data (e.g., race, politics, biometrics) via tags or Outcomes                                                                                          |
| **Contacts**         | 💡 If you upload address books or contacts via Data Tags                                                                                                                               |
| **User Content**     | 💡 If you collect user-generated content through OneSignal                                                                                                                             |
| **Browsing History** | ❌ Not collected                                                                                                                                                                        |
| **Search History**   | ❌ Not collected                                                                                                                                                                        |
| **Identifiers**      | ✅ OneSignal assigns a unique OneSignal ID for each user (not linked to identity by default). <br /> 💡 If you link other IDs (e.g., email, alias), disclosure requirements may change. |
| **Purchases**        | ✅ Consumable in-app purchase events are collected                                                                                                                                      |
| **Usage Data**       | ✅ Session counts, durations, and notification interactions are collected                                                                                                               |
| **Diagnostics**      | 💡 OneSignal does not collect crash or energy logs, but does collect metadata like device type, OS, network state, etc.                                                                |

## Required data disclosures in App Store Connect

### Type: Purchases

If your app includes in-app purchases, you must report collection of **‘Purchases’** data.

<Frame caption="Select Purchases data type">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/33ec09e-Purchase.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=f8bf2a9238dd781cf7ae411d150dd945" width="550" height="107" data-path="images/docs/33ec09e-Purchase.png" />
</Frame>

#### Purchase History

Mark ‘Analytics’ as a minimum. This enables OneSignal to provide dashboard features like Segments and Outcomes.

<Frame caption="Select usage purpose for Purchases">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5452615-Purchase_usage.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=ee2eb17e61ab721e5917ed914be5c9b2" width="600" height="722" data-path="images/docs/5452615-Purchase_usage.png" />
</Frame>

<Info>
  If you use OneSignal for other purposes (e.g., personalization or app functionality), be sure to select those as well.
</Info>

#### Linked to user identity?

If you're only using OneSignal's anonymous IDs and don’t associate them with identifiable users, you can select **‘No’**.

If you link user data (e.g., email or name) via your backend or third-party tools, select **‘Yes’**.

<Frame caption="Indicate if purchase history is linked to user identity">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2bada53-Purchase_linked_to_identy.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=d0be711a45705d6eab4977187da7b2f8" width="600" height="215" data-path="images/docs/2bada53-Purchase_linked_to_identy.png" />
</Frame>

#### Used for tracking?

OneSignal does not track users across other apps. Select ‘No’ unless you use third-party tools or integrations that perform tracking.

<Frame caption="Indicate if purchase data is used for tracking">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/39a7ff8-Purchase_for_tracking.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=610b833cda681ad4a4496892a0d85527" width="598" height="360" data-path="images/docs/39a7ff8-Purchase_for_tracking.png" />
</Frame>

After saving, you should see a summary like:

<Frame caption="Privacy summary showing Purchases">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1fca027-Purchase_overview.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=e173fa092a21199e559ac1406ac10ee8" width="607" height="192" data-path="images/docs/1fca027-Purchase_overview.png" />
</Frame>

### Type: Usage Data – Product Interaction

You must disclose collection of **‘Product Interaction’** under **Usage Data**.

<Frame caption="Select Product Interaction data type">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c9fae50-Product_interaction.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=9f8b5584de133b00dff6d9b979587fd2" width="598" height="282" data-path="images/docs/c9fae50-Product_interaction.png" />
</Frame>

#### Product Interaction

Select **‘Analytics’** to reflect how OneSignal uses this data in Segments and Outcomes.

<Frame caption="Select usage purpose for Product Interaction">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/dfadded-Product_interaction_usage.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=218ec98d82e24d6225b93d944a431aba" width="599" height="723" data-path="images/docs/dfadded-Product_interaction_usage.png" />
</Frame>

<Info>
  If you use this data for other purposes, such as app functionality or personalization, include those as well.
</Info>

#### Linked to user identity?

Same guidance as with Purchases — if anonymous, select ‘No’. If linked via user ID or contact info, select ‘Yes’.

<Frame caption="Indicate if product interaction is linked to user identity">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9d3e5b3-Product_interaction_linked_to_identity.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=70006f5d87f0eb38b7f644bbab72e5e3" width="600" height="210" data-path="images/docs/9d3e5b3-Product_interaction_linked_to_identity.png" />
</Frame>

#### Used for tracking?

OneSignal does not use this data for tracking across apps. Select ‘No’ unless other SDKs or integrations do.

<Frame caption="Indicate if product interaction data is used for tracking">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/75a7a60-Product_interaction_for_tracking.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=ef32f29a369ab08a476b2412efaf0bf2" width="598" height="380" data-path="images/docs/75a7a60-Product_interaction_for_tracking.png" />
</Frame>

You should then see this summary:

<Frame caption="Privacy summary showing Product Interaction">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/914ddcf-Product_interaction_overview.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=e2139cac2e02fab6db9b79abdc425ccb" width="609" height="225" data-path="images/docs/914ddcf-Product_interaction_overview.png" />
</Frame>

### Final review

After completing all sections, Apple will show a preview of your app’s privacy disclosure. If you correctly selected Purchases and Usage Data, it should resemble the following:

<Frame caption="Final privacy details summary in App Store Connect">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/da5b3ea-Overview.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=0cb0f0529d1c49716f7ed2e52166b72b" width="598" height="187" data-path="images/docs/da5b3ea-Overview.png" />
</Frame>

## Ongoing compliance

If your data collection practices change — for example, if you add new tags, link identifiers, or update your SDK version — return to App Store Connect and update your disclosures accordingly.

***

Built with [Mintlify](https://mintlify.com).
