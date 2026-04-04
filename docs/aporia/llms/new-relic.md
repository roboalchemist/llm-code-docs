# Source: https://docs.aporia.com/v1/integrations/new-relic.md

# New Relic

Aporia allows you to connect alerts generated from Aporia’s monitors to New Relic’s Incident Intelligence engine and the predictions data in order to create a comprehensive monitoring dashboard in New Relic for your models in production.

### Integrate New Relic with Aporia

1. Log into Aporia’s console. On the navbar on the left, click on **Integrations** and choose **New Relic**.\
   &#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FppSr1EcrAzmRmiTxwLyC%2Fnr_01.png?alt=media" alt=""><figcaption></figcaption></figure>
2. Log into your New Relic account, and click on **+ Add more data**.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FNq7uSwIfvBPeXWRG6T4S%2Fnr_02.png?alt=media" alt=""><figcaption></figcaption></figure>
3. In the search bar type **Aporia** (or scroll down to the **MLOps Integrations** section) and click on the **Aporia** icon.

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FgYJgyYasu90z2VGNzuM2%2Fnr_03.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Under **Prediction data**, click the **Select or create API key** to create a new API key or use an existing one.

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FZOQvItpJRURvIwsokY79%2Fnr_04.png?alt=media" alt=""><figcaption></figcaption></figure>

1. After creating the token, click on the copy symbol to copy the token.
2. Then go back to the Aporia dashboard and paste the token under **New Relic Insert Token**.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F9TIh6IbA7HXiCiJip85Z%2Fnr_07.png?alt=media" alt=""><figcaption></figcaption></figure>
3. Return to the New Relic dashboard. Copy the account ID.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FvhtotmCnBwEQX7PsgmC9%2Fnr_08.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Go back to the Aporia dashboard and paste it under **New Relic Account ID**. ![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F5nKHUu0U4ExgKtLmQJKn%2Fnr_09.png?alt=media)
5. In the Aporia dashboard, click on the **Verify Tokens** button to verify both tokens are working correctly. Green check marks or red error marks should appear to indicate the status. ![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FTwWR6b1cdzfKe12sXgYr%2Fnr_10.png?alt=media)
6. Once everything is set, click on the **Save** button.
7. Return to the New Relic dashboard and click on the **See your data** button. This will redirect you to a dashboard displaying data reported to Aporia in New Relic. ![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FLMtK9WSdDQFfVlfWMiXw%2Fnr_11.png?alt=media)

**Congratulations: You’ve now successfully integrated Aporia with New Relic!**

#### Easy data filtering – Monitoring Platform for Machine Learning Models

You can make it easy to filter the data, on both the **Most Active Models** chart and the **Most Active Model Versions** chart by making the adjustments shown below:

1. Click on the **…** symbol and click **edit**. ![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2Fl5j3OMKy5yJ6tRw4qBmt%2Fnr_12.png?alt=media)
2. On the right navbar, under **User as filter** activate **Filter the current dashboard** and click **Save**.![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FQYkBzcIBRCk9KqlVkbGz%2Fnr_13.png?alt=media)

### Additional ML Graphs

Additional graphs display statistics over the predictions reported:

1. The **Model Inferences** graph displays the number of unique inferences reported for each model and version.
2. The **Average Numeric Inferences** graph displays the average value numeric inferences reported for each model and version.
3. The **Numeric Inferences Heatmaps** graph displays heatmaps of the numeric inferences values reported for each model and version.
4. The **Categorical Inferences** graph displays the different unique values and their frequencies of categorical predictions reported for each model and version.

![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FP69icAZ5ECSyC6ZwFxeg%2Fnr_14.png?alt=media)

### Alerts and Applied Intelligence for ML models

When a new alert is detected by Aporia, it will be reported to New Relic’s Incident Intelligence engine. To view these alerts in New Relic, click on **Alerts & AI** and on the left navbar click on **Issues & activity**.

![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F0n0QoQmsZE4WWNJx4Hn6%2Fnr_15.png?alt=media)

On this page you will be able to see the correlated alerts. Clicking on an issue will open a screen with additional data, including all the related activities to the issue and their payloads.

![New Relic Integration](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FfTaD1UWVQ6n29Iuncbe2%2Fnr_16.png?alt=media)

Newly created alerts will now be correlated with your New Relic alerts and you should be able to see data about newly reported predictions.

Happy Monitoring!
