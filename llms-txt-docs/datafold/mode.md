# Source: https://docs.datafold.com/integrations/bi-data-apps/mode.md

# Mode

## Obtain credentials from Mode

<Note>
  **INFO**

  To complete this integration, your **Mode** account must be a part of a [Mode Business Workspace](https://mode.com/compare-plans) in order to generate an API Token.
</Note>

<Note>
  **INFO**

  You need to have **Admin** privileges in your Mode Workspace to be able to create an API Token.
</Note>

In **Mode**, navigate to **Workspace Settings** → **Privacy & Security** → **API**.

Click the <Icon icon="gear" /> icon, and choose **Create new token**.

<Frame caption="Tokens">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=218032a87bc1d3f56b623a1eec0a9a00" data-og-width="1691" width="1691" data-og-height="267" height="267" data-path="images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=58c1cb56a809187118184cd69200a35b 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e8b3268bc2db3bb2aa31045bce9631b2 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e817ac0717fd115a7d277df6cc108027 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a59203a5a10594174ea08cdd2b97af9e 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=633af3fa499865c6c8d363c01c987e7e 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tokens-40fd2f50b2ec5d0acc295c11ae9e0548.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=83502a7e22c1f9a5d96203f221833d84 2500w" />
</Frame>

Take note of:

* Token Name,
* Token Password,
* And the URL of the page that lists the tokens. It should look like this:

  [https://app.mode.com/organizations/\{workspace}/api\_keys](https://app.mode.com/organizations/\{workspace}/api_keys)

Take note of `{workspace}` part, we will need it when configuring Datafold.

## Configure Datafold

Navigate to **Settings** → **Integrations** → **BI & Data Apps**.

<Frame caption="Add New Integration">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

Choose **Mode** Integration to add.

<Frame caption="Choose Type">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=064bac3962b7e9812daae5972457b5c2" data-og-width="1073" width="1073" data-og-height="667" height="667" data-path="images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dbdaaf4597a7d6cba715ab6df01d9fca 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7fcd5d2a579d4623982ce61dad054fa1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a302a76e06c0ad63b8658519c10bba04 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=11102d708ea0b66c27013da12bbcc548 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=700f899f072a1b4da648e15ed4e9c3d4 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/choose-type-bf9b2d554dc7739742b1f007c9bef227.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e436b0081860afe17c309aa747e604f 2500w" />
</Frame>

This will bring up **Mode** integration parameters.

<Frame caption="Create Integration">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7ec9e93eb717c2a1c1becefe2c29a768" data-og-width="1059" width="1059" data-og-height="706" height="706" data-path="images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f88f8562400cd02c7b32b2421b4b33b 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=590aaaa136ed31c276f8b85e0828f470 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=662051cc22c31fcc70cfc762ff9610c7 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=337a027c1e0bc4bb091de29f18c1491c 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4c6105cbd370fffab35add37d5ccfa38 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-585f8b3a1e9f38c5bde10e6528e0c6b4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ef510d1b9ffa273419ac34279184095b 2500w" />
</Frame>

Complete the configuration by specifying the following fields:

| Field Name       | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| Integration name | An identifier used in Datafold to identify this Data App configuration. |
| Token            | API token, as generated above.                                          |
| Password         | API token password, as generated above.                                 |
| Workspace        | Workspace name obtained from your workspace URL.                        |

<Note>
  **INFO**

  **Workspace Name** field is not marked as required on this screen. That's for backwards compatibility: the legacy type of Mode API token, known as **Personal Token**, does not require that parameter. However, such tokens can no longer be created, so we're no longer providing instructions for them.
</Note>

When completed, click **Save**.

Datafold will try to connect to Mode and, if any issues with the connection arise you will be alerted.

Datafold will start to sync your reports. It can take some time to fetch all the reports, depending on how many of them there are.

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>

Now that Mode sync has completed — you can browse your Mode reports!

<Frame caption="Tokens">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d53ed5013896c0e70df4d551e6478ab" data-og-width="1720" width="1720" data-og-height="1082" height="1082" data-path="images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5172bb0c7607aa6a4b8a96dcfa869ba9 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a52b6998b01c3799b768cc0c0a8f22c6 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f5e659695bdc8ffcd6b904b191554511 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c5ab2ddfed858c2ba9637742dfb8db79 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e29cda5dc55550bcee43f6c027012ea1 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/mode_sync_results-dd76443d59234b676d29c6999f278c48.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d31fdcc6533c62543ba8918e76ef860d 2500w" />
</Frame>
