# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/configuration-of-vs-code.md

# Configure VS Code

To configure VS Code, first [generate an API key in Make](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/generation-of-your-api-key).&#x20;

Then install the Make Apps Editor. You can get the Make Apps Editor from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Integromat.apps-sdk) or install it in the Extensions tab in VS Code.

{% stepper %}
{% step %}
Click the Make icon on the VS code sidebar. This activates the Map Apps Editor.

If you haven't set up a development environment, you will see a message in a pop-up window.
{% endstep %}

{% step %}
Click the **Add environment** button to launch the environment setup or execute the command: `>Make Apps: Add SDK Environment` from the command palette.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3a650ef0b9550f15fdb57c974e20ce832a3161cb%2FScreenshot%202024-05-02%20at%2013.36.23.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Fill in the API URL in the next pop-up window. The API URL depends on your Make zone.

For example, the US1 Make zone has the API URL: `us1.make.com/api`.

If the app you want to access originates from a different zone than your account, enter the app's zone.
{% endstep %}

{% step %}
Fill in the label for the environment in the next pop-up window. Press **Enter** to confirm the environment label.
{% endstep %}

{% step %}
Enter your [Make API key](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/generation-of-your-api-key) that you previously created in Make.
{% endstep %}
{% endstepper %}

The Make Apps Editor extension restarts with the environment configuration.

A new sidebar appears in VS code with a list of your custom apps and Make open-source apps. If you previously created any, your custom apps are listed in the block **My apps**. The Make open-source apps are listed in the **Open source apps** field at the bottom of the VS code sidebar.

{% hint style="info" %}
The open-source apps code is only available in the EU1 zone.

If your zone is different and you want to access their code, create a new environment with the `eu1.make.com/api` environment URL.
{% endhint %}

## Switch between environments

In the Make Apps Editor, you can work across multiple environments.

To identify the active environment, check the indicator in the bottom status bar. Click the environment indicator to switch between environments.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-06aacb81277b70f97e6fc92a3f44e37853c9abfb%2Fimage%20(62).png?alt=media" alt="" width="563"><figcaption><p>Environment indicator</p></figcaption></figure></div>

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-452f05f21164094ca340a8aae954d7e9921606f6%2FScreenshot%202024-05-08%20at%2017.19.51.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

Add another environment by executing the `>Add SDK environment` command again, as described in Step 2 above.

### Useful settings

Navigate to **Extensions > Make Apps Editor > Extension Settings > Edit in settings.json** to add more settings.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d27681ab189a6d086098c589d5b9c1fdea9f52e2%2FScreenshot%202024-05-03%20at%2010.10.33.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

Here are some settings for better performance and experience:

* Set `editor.formatOnSave` to `true` in VS Code settings. Source codes will be formatted automatically when you save them.
* Set `editor.quickSuggetions.strings` to `true` in VS Code settings. Keyword recommendations will automatically show up while you're typing in IML strings too.

## Log out and log in of an environment

You can log out using the `>Logout` command and log back in with the `>Login` command.

When you log out, the API key is removed from the `settings.json` file.

To log in again, you will need to enter your API key.

{% hint style="info" %}
You can use this flow to change your API key in an environment.
{% endhint %}
