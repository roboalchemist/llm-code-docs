# Source: https://docs.zapier.com/platform/build/dynamic-field.md

# Send or receive dynamic user-defined fields through your API

> Dynamic fields are a type of field built from an API call. Custom code runs to show fields based on other input field data. These are especially useful with project management apps, CRM apps, databases, and any other app where users can add custom, user-defined fields.

## Add a dynamic field

You can use dynamic fields, to retrieve fields in three different contexts:

* Whenever the value of a field with `altersDynamicFields` is changed.
* Whenever the *Set up* section for the action is opened in the Zap editor.
* Whenever the *Refresh Fields* button is used on the action.

In the [Platform UI](https://zapier.com/app/developer):

1. In the *Build* section in the left sidebar, click on your **action**.
2. Click the **Input Designer** tab.
3. Click **Add** and select **Dynamic Field**.
4. A code box will appear. Add your **JavaScript code** to make an API call and fetch the fields from your app's API. Use Zapier's `z.request` to make the API call. Your code should return each custom field's key and name to Zapier in an array, so they display correctly in the Zap editor. Learn more about using [Z Object to call a function](https://github.com/zapier/zapier-platform/blob/master/packages/cli/README.md#z-object).
5. Once you've added your JavaScript code, click **Save**.

<Info>
  **Note**:

  * Do not rely on any input fields already having a value, since they won't have one the first time the Zap editor loads.
  * Dynamic fields using `z.request` will not show in the Zap editor preview.
  * Dynamic fields can only be added to actions, not triggers.
</Info>

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e78f6bb0c16c45024388416a0436c420" data-og-width="1663" width="1663" data-og-height="958" height="958" data-path="images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8cb1f064e0fa9dc3ed267288c3d98feb 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=dda1db88d388ea113060aa8648fbb076 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=89e6f614134d66da1012dbceb60b14a9 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5e5729bb70b77e8e832640f4ca4cb976 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e04611fa69e0dbdf6ef2cc69ae8950b7 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/8177dce9ee77e014b8fe65f4f6d6e5ba.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=0b4eb841c158267355ab64ea638219bf 2500w" />
</Frame>

## Create a dynamic field based on previous input field data

In the [Platform UI](https://zapier.com/app/developer):

1. In the *Build* section in the left sidebar, click on your **action**.
2. Click the **Input Designer** tab.
3. Review your input field settings, you'll need at least one input field that has **Alters Dynamic Fields** selected. This is the field that Zapier will use to decide if the dynamic field should be shown.
4. Click **Add** and select **Dynamic Field**.
5. A code box will appear. Add your JavaScript code that evaluates data from previous fields (referencing `bundle.inputData.field_key` where `field_key` is replaced with the actual key of the prior input field that must be checked), including logic and details on another field to show depending on the value of the former.
6. Once you've added your JavasScript code, click **Save**.

## Send dynamic field data to your API

In the [Platform UI](https://zapier.com/app/developer):

1. In the *Build* section in the left sidebar, click on your **action**.
2. Click the **API Configuration** tab.
3. Click **Switch to Code Mode**
4. In the dialog box, click **Switch to Code Mode**
5. A code box will appear. Add your Javascript code, that include `body: { ...bundle.inputData }` to send every input field, including pre-defined or dynamic fields in the body of your API call to your app. You can also use `bundle.inputData.field_key` to include individual lists of dynamic fields.
6. Once you've added your JavasScript code, click **Save**.

## Test a dynamic field

To test how your dynamic fields will appear in the Zap editor:

1. [Create a new Zap](https://zapier.com/app/editor/).
2. Add the action to your Zap that includes your dynamic field. This will allow for you to test how your action will appear to users.

If you want more details about the API calls being made, in the [Platform UI](https://zapier.com/app/developer):

* In the *Manage* section in the left sidebar, click **Monitoring**.
* You'll see a graph and be able to click on data points to view events and details to troubleshoot your setup further.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
