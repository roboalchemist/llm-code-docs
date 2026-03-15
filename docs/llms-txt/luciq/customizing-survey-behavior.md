# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-in-app-surveys/customizing-survey-behavior.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-in-app-surveys/customizing-survey-behavior.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-in-app-surveys/customizing-survey-behavior.md

# Customizing Survey Behavior

### Showing a Welcome Screen

You can show your users a welcome screen before a survey rather than asking the first question immediately. By default, this is disabled. To enable the survey welcome screen, use the following method.

{% code title="JavaScript" %}

```javascript
Surveys.setShouldShowWelcomeScreen(true);
```

{% endcode %}

![](https://content.gitbook.com/content/6lIBifTCHAMDxXnztiBK/blobs/PMgg6KneRrhyMsp0LSmi/55e666ab57e064ec43574179730de7f79eac9e53c1f0e61b8aebb7259cc37393%20react%20native%20customizing%20survey%20behavior%201.png)

### Integrating with Slack

If you have an existing Slack integration (or plan to create one), you can enable auto-forwarding of survey responses. If enabled, all NPS survey score responses and Custom survey responses will be forwarded to your Slack integration on the channel you choose.

* Forwarded NPS responses will display user email, responses, and score.
* Custom survey responses will display the user email and every question and its response.
* You'll also have the option to reply to the user, which will redirect you to the chat window to reply.

![](https://content.gitbook.com/content/6lIBifTCHAMDxXnztiBK/blobs/ypnghWGTDCMMVkjZw9hU/85de4236538c036fc98075858556e631f2eb3cfb43bcce35d0e1edc67cc594ce%20react%20native%20customizing%20survey%20behavior%202.png) ![](https://content.gitbook.com/content/6lIBifTCHAMDxXnztiBK/blobs/Gru9APX1wSuZblWvCDfo/9b73a6f8336e4e42b53f110024678f0eaeee910066a789950cb1df14f8dd6b57%20react%20native%20customizing%20survey%20behavior%203.png)

### Setting App Store URL

While the SDK will normally automatically link to your application on the app store when needed, if your application is limited to certain regions, the automatic linking might not work. In these cases, use the API below to manually set the URL of your application in the store.

{% code title="JavaScript" %}

```javascript
Surveys.setAppStoreURL('URL');
```

{% endcode %}
