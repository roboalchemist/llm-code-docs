# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/creating-an-app-in-vs-code.md

# Create an app in VS Code

Now that you have [generated your API key](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/generation-of-your-api-key) and [configured VS Code](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/configuration-of-vs-code), you can now create your app.

To create an app in VS Code:

{% stepper %}
{% step %}
Click the `+` icon in the header of the `My apps` section or call the `>New app` command directly from the command palette.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5287e7e940fb1d231600f01b354dc2bba7e21a63%2FScreenshot%202024-05-02%20at%2014.15.07.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter a label. This is the app name that users will see in the Scenario builder.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f6dcec30f1ff1154011aef3473af95d19fc4c28a%2FScreenshot%202024-05-02%20at%2014.25.45.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
A placeholder app ID is generated for you. It will be used in the URL paths and in the scenario blueprint. It should be clear to which app it leads and it has to match `(^[a-z][0-9a-z-]+[0-9a-z]$)` regular expression.

This value can't be changed.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-54bf2003a74274c0d1cd5ee8a248f85c71dbe97d%2FScreenshot%202024-05-02%20at%2014.27.21.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter the app version. Currently, you can only create apps in version 1.
{% endstep %}

{% step %}
Enter a description of your app.
{% endstep %}

{% step %}
Enter a color theme for your app. This is the color of the app's modules as seen in scenarios. The theme is in hexadecimal format. For example, the Make app's color is `#6e21cc`.
{% endstep %}

{% step %}
Enter the language of the app's interface. Most aps in Make are in English.
{% endstep %}

{% step %}
Enter countries where the app will be available. If you do not select any countries, Make will consider the app to be global.
{% endstep %}

{% step %}
Confirm the last dialog.
{% endstep %}
{% endstepper %}

Your app is in the My Apps view and you can start coding.
