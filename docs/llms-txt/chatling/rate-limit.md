# Source: https://docs.chatling.ai/general-settings/rate-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limit

> Learn how to set a rate limit for your chatbot to prevent it from being spammed.

Rate limiting allows you to limit the number of messages a user can send to your chatbot in a given period of time. This helps prevent end-users from spamming your chatbot and depleting your account credits.

## How to set a rate limit

1. Open your chatbot's dashboard.
2. Go to chatbot settings.

<img src="https://chatling-assets.b-cdn.net/open-chatbot-settings.jpg" width="300" alt="Open chatbot settings" />

3. Click the `Security` tab.
4. Under the `Rate limiting` section, add a rate limit, e.g. 10 messages per minute. You can add multiple rate limits for different periods of time, such as per minute, per hour, or per day.
   <Note>The rate limit is applied to individual users. For example, if you set a rate limit of 10 messages per minute, each user can send up to 10 messages per minute.</Note>
5. You can also add a custom error message to be displayed when the rate limit is exceeded. If left blank, a default error message will be displayed.
   <Note>The default error message is automatically translated into the language of your chatbot widget. If you override it with a custom message, it won't be translated.</Note>
6. Click `Save`.

Once you've set the rate limits, your chatbot will prevent end-users from sending more messages than the rate limit in a given period of time. If the rate limit is exceeded, an error message will be displayed.
