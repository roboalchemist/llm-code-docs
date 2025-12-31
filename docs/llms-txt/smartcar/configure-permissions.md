# Source: https://smartcar.com/docs/getting-started/how-to/configure-permissions.md

# How to Configure Permissions for Vehicle Data Collection

> Step-by-step guide to selecting signals, commands, and attributes in the Smartcar Dashboard and requesting the right permissions from vehicle owners.

To retrieve vehicle data through Smartcar, you must configure your application to request the correct permissions from vehicle owners. This guide walks you through the process using the Smartcar Dashboard.

<Steps>
  <Step title="Open the Configuration Page in the Dashboard">
    Go to the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration) and select your application. Navigate to the <b>Configuration</b> section and choose the <b>Vehicle access</b> tab.
  </Step>

  <Step title="Select Signals, Commands, and Attributes">
    Under the <b>Signals</b>, <b>Commands</b>, and <b>Attributes</b> tabs, select the specific vehicle data points and actions your application needs. Each selection corresponds to a permission that the vehicle owner must approve.

    <Frame type="simple" caption="Application Configuration in Smartcar Dashboard">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=8dbd5a5cbf7561ce6890e8b74d2e3af1" alt="Smartcar Dashboard configuration page showing signal selection and Connect Preview." data-og-width="5014" width="5014" data-og-height="2966" height="2966" data-path="images/how-to/vehicle-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=cddfd1c093f18c5addf4747182e51a93 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ea20d97a8cd21ed0f9b792cdcafb7655 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=8e81876d3862241affee92b987706cea 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=31c470447fe2ebdf68c75dd3d160a1fd 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ca57dad41510fe85b7c5407384adfac0 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a95f7e18664d6b9d3592652f3c662607 2500w" />
    </Frame>

    <ul>
      <li><b>Signals:</b> Dynamic vehicle data (e.g., battery level, odometer, location).</li>
      <li><b>Commands:</b> Actions your app can perform (e.g., lock/unlock, start charging).</li>
      <li><b>Attributes:</b> Static vehicle info (e.g., make, model, year).</li>
    </ul>

    <Note>
      Only select the permissions your application truly needs. This improves user trust and increases the likelihood of successful connections.
    </Note>
  </Step>

  <Step title="Preview the Owner Experience">
    As you select signals, commands, and attributes, the <b>Connect Preview</b> on the right updates to show what the vehicle owner will see when connecting their vehicle. This preview lists the permissions your app is requesting and the vehicles that will be connected.
  </Step>

  <Step title="Publish Your Configuration">
    Once you are satisfied with your selections, click <b>Publish</b> to save your configuration. Your application will now request these permissions from vehicle owners during the Smartcar Connect flow.
  </Step>
</Steps>

## Dynamic Permissions

If your application needs to access different permissions based on user actions or vehicle types, you can leverage the `scope` parameter in the Smartcar Connect URL to dynamically request permissions at runtime. This allows you to tailor the permissions based on the specific vehicle or user context.
Keep in mind that any permissions you pass via the `scope` parameter will override the permissions configured in the Smartcar Dashboard for that specific connection.

### Notes

* If you need to change permissions later, you can return to this configuration page and update your selections. Vehicle owners will need to reauthorize your application to grant any new permissions.
* The permissions you select here will determine the data and actions available to your application. Make sure to choose only what is necessary for your use case.

***

## What’s Next

* [How to Connect Vehicles](/getting-started/connect-vehicles)
* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [API Reference: Permissions](/api-reference/permissions)
