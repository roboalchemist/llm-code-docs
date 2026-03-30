# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-in-app-replies/disabling-enabling-in-app-replies.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-in-app-replies/disabling-enabling-in-app-replies.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/in-app-replies/disabling-enabling-in-app-replies.md

# Disabling/Enabling in app replies

Explained in this page is how to hide the replies page in your React Native apps.

When the Luciq SDK is invoked, a popup appears to your app users with default [Prompt Options](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/in-app-replies/broken-reference) for them to "Report a problem" (send you a bug report), "Suggest an improvement" (send you feedback), or "Ask a Question" (send you a question). There is also an option to view the chat history, or replies, page.

The API below can be used to hide the replies page from the user as well as disable it. The button in the prompt options will no longer be visible if this API is used. The in-app notifications will also be disabled, and manually showing the chats list won't have an effect.

{% hint style="info" %}
Disabling replies will both hide the replies button in the prompt options and disable in-app notifications. Manually invoking the chats list will not display replies when disabled.
{% endhint %}

{% code title="JavaScript" %}

```javascript
Replies.setEnabled(true);
```

{% endcode %}
