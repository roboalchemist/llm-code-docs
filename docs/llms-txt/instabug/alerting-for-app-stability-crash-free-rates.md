# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/alerting-for-app-stability-crash-free-rates.md

# Alerting for App Stability - Crash Free Rates

Crash-Free Rates are one of the most important metrics for any mobile app. Setting up these alerts allows you to proactively detect and address stability issues, ensuring a smoother user experience. They provide quick insights into problematic app versions, enabling faster resolution and better decision-making.

## Setting Up Alerts

1. **Go to the Alerts and Rules page**:

   <figure><img src="https://files.readme.io/a212f99777f0870d960ff23eafe29fedee0752ce692aa824b9c89544e877f44d-alerting-for-app-stability-crash-free-sessions-11.png" alt=""><figcaption></figcaption></figure>
2. **Create a new Rule**:

   <figure><img src="https://files.readme.io/ada4309aba5a80da71289be45cfe2fb33c596443514eb19bc0a3dbf70f986f1f-alerting-for-app-stability-crash-free-sessions-6.png" alt=""><figcaption></figcaption></figure>
3. **Select "Overall App" to set up the rule**:

   <figure><img src="https://files.readme.io/0034b9c3814522743440ee24927b697a1c8b7b972b1e3b22ee4db65be3a25753-alerting-for-app-stability-crash-free-sessions-7.png" alt=""><figcaption></figcaption></figure>

### Crash-Free Sessions

Set a threshold and get alerted whenever the application’s crash-free sessions rate drops below the specified threshold.

1. **Trigger**:
   * Select "Crash-free sessions in the last 24 hours".<br>

     <figure><img src="https://files.readme.io/f0835ff-image.png" alt=""><figcaption></figcaption></figure>

2. **Select the Threshold for Crash-Free Sessions**: Any drop below this point will trigger an alert.<br>

   <figure><img src="https://files.readme.io/9496a34-image.png" alt=""><figcaption></figcaption></figure>

3. **Breakout by App Version**: (Optional)
   * By toggling "Send an alert for every app version," you will get alerted for every app version that has its crash-free sessions rate drop below the threshold.

4. **Conditions**:
   * If no condition is added, the rule will be applied to the app/app version if it exceeds 100 sessions.
   * You have 2 conditions you can choose from:

     <figure><img src="https://files.readme.io/4a5bcc5-image.png" alt=""><figcaption></figcaption></figure>

     * **App Version**: Select "Top Releases" or "Latest Releases", or specify app versions.<br>

       <figure><img src="https://files.readme.io/565c942-image.png" alt=""><figcaption></figcaption></figure>

       <br>
     * **Session count**: The minimum number of sessions the app (or selected versions) has to have for the alert to trigger. Specify "Greater than" or "Less than" to set a number of sessions and reduce the noise.

       <figure><img src="https://files.readme.io/8098b92-image.png" alt=""><figcaption></figcaption></figure>

5. **Forward Alert**:
   * Set the option to forward the alert to your favorite integrated tool.<br>

     <figure><img src="https://files.readme.io/404f973-image.png" alt=""><figcaption></figcaption></figure>

### Crash-Free Users

{% hint style="info" %}
Note: Crash-free users data will only be retrieved for SDK versions newer than v11.12.0 for iOS and v11.5.2 for Android
{% endhint %}

Set a threshold and get alerted whenever the application’s crash-free user rate drops below the specified threshold.

1. **Trigger**:
   * Select "Crash-free users in the last 24 hours".<br>

     <figure><img src="https://files.readme.io/c4ee329-image.png" alt=""><figcaption></figcaption></figure>

2. **Select the Threshold for Crash-Free Users**: Any drop below this point will trigger an alert.<br>

   <figure><img src="https://files.readme.io/ae22313-image.png" alt=""><figcaption></figcaption></figure>

3. **Breakout by App Version**: (Optional)
   * By toggling "Send an alert for every app version," you will get alerted for every app version that has its crash-free user rate drop below the threshold.

4. **Conditions**:
   * If no condition is added, the rule will be applied to the app/app version if it exceeds 100 sessions.
   * You have 3 conditions you can choose from:

     <figure><img src="https://files.readme.io/dbc3e0f-image.png" alt=""><figcaption></figcaption></figure>

     * **App Version**: Select "Top Releases" or "Latest Releases", or specify app versions.

       <figure><img src="https://files.readme.io/554acfe-image.png" alt=""><figcaption></figcaption></figure>

     * **User Count**: minimum number of users the app (or selected versions) has to have for the alert to trigger. Specify "Greater than" or "Less than" to set a number of users and reduce the noise.<br>

       <figure><img src="https://files.readme.io/76472b6-image.png" alt=""><figcaption></figcaption></figure>

     * **Session Count**: The minimum number of sessions the app (or selected versions) has to have for the alert to trigger. Specify "Greater than" or "Less than" to set a number of sessions and reduce the noise.

       <figure><img src="https://files.readme.io/896c89a-image.png" alt=""><figcaption></figcaption></figure>

5. **Forward Alert**:
   * Set the option to forward the alert to your favorite integrated tool.<br>

     <figure><img src="https://files.readme.io/b6b18b5-image.png" alt=""><figcaption></figcaption></figure>

6.

```
<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FFR1LcNYNtXfQGUQ0IZB2%2Fimage.png?alt=media&#x26;token=d06400c7-fb9e-49f9-a013-f42716b1d9a2" alt=""><figcaption></figcaption></figure>
```
