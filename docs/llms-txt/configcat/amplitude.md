# Source: https://configcat.com/docs/integrations/amplitude.md

# Amplitude - Add feature flag changes to your charts

Copy page

## Overview[​](#overview "Direct link to Overview")

There are two available integration opportunities between ConfigCat and Amplitude:

* [Monitoring your feature flag change events in Amplitude with Annotations](#annotations)
* [Sending feature flag evaluation analytics to Amplitude Experiments](#experiments)

## Monitoring your feature flag change events in Amplitude with Annotations[​](#annotations "Direct link to Monitoring your feature flag change events in Amplitude with Annotations")

Every feature flag change in ConfigCat is annotated on the Amplitude charts as a vertical line and some details are added automatically about the change.

![amplitude\_chart](/docs/assets/amplitude_chart.png)

### Installation[​](#installation "Direct link to Installation")

1. Have an [Amplitude subscription.](https://www.amplitude.com/)
2. Get an [Amplitude API Key and Secret Key.](https://www.docs.developers.amplitude.com/analytics/find-api-credentials/) ![amplitude\_apikey\_secretkey](/docs/assets/amplitude_apikey_secretkey.png)
3. Open the [integrations tab](https://app.configcat.com/product/integrations) on ConfigCat Dashboard.
4. Click on Amplitude's **Connect** button and set your Amplitude API key and Secret key.
5. You're all set. Go ahead and make some changes on your feature flags, then check your charts in Amplitude.

### Un-installation[​](#un-installation "Direct link to Un-installation")

1. Open the [integrations tab](https://app.configcat.com/product/integrations) on ConfigCat Dashboard.
2. Click on Amplitude's **Connected** button.
3. Select the connection from the **Connected** dropdown.
4. Click the **Disconnect** button in the edit dialog.
5. Click **Yes** in the confirmation dialog.

### Chart Annotation[​](#chart-annotation "Direct link to Chart Annotation")

Every annotation sent to Amplitude by ConfigCat has:

* **Name:** A brief summary of the change.
* **Description:** A direct link to the Product/Config/Environment of the feature flag in ConfigCat.

![amplitude\_annotation](/docs/assets/amplitude_annotation.png)

## Sending feature flag evaluation analytics to Amplitude Experiments[​](#experiments "Direct link to Sending feature flag evaluation analytics to Amplitude Experiments")

Ensures that feature flag evaluations are logged into [Amplitude Experiments](https://amplitude.com/docs/experiment/). With this integration, you can have advanced analytics about your feature flag usages, A/B test results.

### Setup[​](#setup "Direct link to Setup")

1. **Install SDKs:** Add both the ConfigCat SDK and Amplitude SDK to your application.

2. **Configure SDKs:**

   * **ConfigCat SDK:** Initialize with your ConfigCat SDK key.
   * **Amplitude SDK:** Set up with your Amplitude ApiKey.

3. **Integrate Feature Flag Evaluations:**

   * During the initialization of the ConfigCat SDK, subscribe to the `flagEvaluated` hook.

   * Send feature flag evaluation data to Amplitude using the `$exposure` event name. Include the following parameters:

     <!-- -->

     * `flag_key`: the feature flag's key.
     * `variant`: the evaluated feature flag's value or variation ID
     * `variation_id` (optional): the evaluated feature flag's variation ID

   * You can use the [Identify API](https://www.docs.developers.amplitude.com/analytics/apis/identify-api/) in Amplitude to enrich all your events with feature flag metadata. This way you can easily group/filter your existing Amplitude events by feature flag evaluations.

Code samples:

* JavaScript, Node, SSR
* React
* Python
* Go
* Java
* Android
* Swift (iOS)
* Other languages

```js
const configCatClient = configcat.getClient("#YOUR_SDK_KEY", PollingMode.AutoPoll, {
    setupHooks: (hooks) =>
        hooks.on('flagEvaluated', evaluationDetails => {
            // Send an `$exposure` event.
            amplitude.track('$exposure',
                {
                    'flag_key': evaluationDetails.key,
                    'variant': evaluationDetails.value,
                    'variation_id': evaluationDetails.variationId
                });

            // Use the identify API.
            const identifyEvent = new amplitude.Identify();
            identifyEvent.set("configcat_" + evaluationDetails.key, evaluationDetails.value);
            amplitude.identify(identifyEvent);
        }),
});

```

```tsx
<ConfigCatProvider
  sdkKey="#YOUR_SDK_KEY"
  pollingMode={PollingMode.AutoPoll}
  options={{
    setupHooks: (hooks) =>
      hooks.on('flagEvaluated', evaluationDetails => {
         // Send an `$exposure` event.
         amplitude.track('$exposure',
               {
                  'flag_key': evaluationDetails.key,
                  'variant': evaluationDetails.value,
                  'variation_id': evaluationDetails.variationId
               });

         // Use the identify API.
         const identifyEvent = new amplitude.Identify();
         identifyEvent.set("configcat_" + evaluationDetails.key, evaluationDetails.value);
         amplitude.identify(identifyEvent);
      }),
  }}
>
</ConfigCatProvider>

```

```python
def on_flag_evaluated(evaluation_details):
   # Send an `$exposure` event.
   amplitude.track(
      BaseEvent(
         event_type="$exposure",
         user_id=evaluation_details.user.get_identifier(),
         event_properties={
            "flag_key": evaluation_details.key,
            "variant": evaluation_details.value,
            "variation_id": evaluation_details.variation_id
         }
   ))

   # Use the identify API.
   identify_obj=Identify()
   identify_obj.set(f'configcat_{evaluationDetails.key}', evaluation_details.value)
   amplitude.identify(identify_obj, EventOptions(user_id=evaluation_details.user.get_identifier()))
   pass

client = configcatclient.get('#YOUR-SDK-KEY#',
    ConfigCatOptions(
        hooks=Hooks(on_flag_evaluated=on_flag_evaluated)
    )
)

```

```go
client := configcat.NewCustomClient(configcat.Config{SDKKey: "#YOUR-SDK-KEY#",
    Hooks: &configcat.Hooks{OnFlagEvaluated: func(details *configcat.EvaluationDetails) {
         // Send an `$exposure` event.
         amplitude.Track(amplitude.Event{
            UserID:    details.Data.User.(*configcat.UserData).Identifier,
            EventType: "$exposure",
            EventProperties: map[string]interface{}{
               "flag_key": details.Data.Key,
               "variant": details.Value,
               "variation_id": details.Data.VariationID,
            },
         })
        
         // Use the identify API.
         identifyObj := amplitude.Identify{}
         identifyObj.Set("configcat_" + details.Data.Key, details.Value)
         amplitude.Identify(identifyObj, amplitude.EventOptions{UserID: details.Data.User.(*configcat.UserData).Identifier})
    }}})

```

```java
ConfigCatClient client = ConfigCatClient.get("#YOUR-SDK-KEY#", options -> {
   options.hooks().addOnFlagEvaluated(details -> {
      // Send an `$exposure` event.
      JSONObject eventProps = new JSONObject();
      eventProps.put("flag_key", details.getKey());
      eventProps.put("variant", details.getValue());
      eventProps.put("variation_id", details.getVariationId());
      Event event = new Event("$exposure", details.getUser().getIdentifier());
      amplitude.logEvent(event);

      // Use the identify API.
      JSONObject userProps = new JSONObject();
      userProps.put("configcat_" + details.getKey(), details.getValue());
      Event updateUser = new Event("$identify", details.getUser().getIdentifier());
      updateUser.userProperties = userProps;
      amplitude.logEvent(event);
   });
});

```

```java
ConfigCatClient client = ConfigCatClient.get("#YOUR-SDK-KEY#", options -> {
   options.hooks().addOnFlagEvaluated(details -> {
      // Send an `$exposure` event.
      amplitude.track(
         "$exposure",
         mutableMapOf<String, Any?>(
            "flag_key" to details.getKey(), 
            "variant" to details.getValue(), 
            "variation_id" to details.getVariationId()
      ))

      // Use the identify API.
      val identify = Identify()
      identify.set("configcat_" + details.getKey(), details.getValue())
    });
});

```

```swift
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
   options.hooks.addOnFlagEvaluated { details in
      // Send an `$exposure` event.
      let event = BaseEvent(
         eventType: "$exposure", 
         eventProperties: [
            "flag_key": details.key,
            "variant": details.value,
            "variation_id": details.variationId ?? ""
         ]
      )

      // Use the identify API.
      let identify = Identify()
      identify.set(property: "configcat_" + details.key, value: details.value)
      amplitude.identify(identify: identify)
   }
}

```

While our documentation primarily provides code examples for languages that Amplitude natively supports and has an official SDK, you can integrate with other languages by sending an event to Amplitude with a third-party SDK or with using the [Amplitude's Upload request API](https://www.docs.developers.amplitude.com/analytics/apis/http-v2-api/#upload-request).

1. **Subscribe to the FlagEvaluated hook** in the ConfigCat SDK.

2. **Send an event to Amplitude** using the `$exposure` event name. Include the following event properties:

   <!-- -->

   * `flag_key`: the feature flag's key from the FlagEvaluated hook's EvaluationDetails
   * `variant`: the evaluated feature flag's value or the variationId from the FlagEvaluated hook's EvaluationDetails
   * `variation_id`: the evaluated feature flag's value or the variationId from the FlagEvaluated hook's EvaluationDetails
   * `user_id` (optional): in case you are using the tracking in a backend component or you don't identify all your event sendings to Amplitude with user details, you have to send the `user_id` property as well to identify your user. You can use the User object's Identifier property from the FlagEvaluated hook or a value that best describes your user.

note

For Text feature flags with lengthy values (e.g., JSON), send the `variationId` instead of the `value` as the `variant` to Amplitude. The `variationId` is a hashed version of the feature flag value, accessible on the ConfigCat Dashboard by enabling the *Show VariationIDs to support A/B testing* setting. Learn more [here](https://app.configcat.com/product/preferences).

4. Deploy your application and wait for feature flag evaluations to happen so Experiments in Amplitude could be populated.

### Usage with Experiments[​](#usage-with-experiments "Direct link to Usage with Experiments")

Check your Experiments page in Amplitude and select your feature flag as the Experiment.

### Usage with custom chart[​](#usage-with-custom-chart "Direct link to Usage with custom chart")

If you don't have access to the Experiments feature in Amplitude, you can create a custom chart based on the `Exposure` event. You can filter for your feature flag keys with the `Flag Key` property and visualize the different variants by using the `Variant` property as a Breakdown. Example:

![Amplitude custom chart](/docs/assets/amplitude/customchart.png)

### Usage with enriched user properties for your custom events.[​](#usage-with-enriched-user-properties-for-your-custom-events "Direct link to Usage with enriched user properties for your custom events.")

If you use the [Identify API](https://www.docs.developers.amplitude.com/analytics/apis/identify-api/) approach, you'll be able to use the feature flag evaluation data in your current reports. You can Group Segments by your feature flag evaluations:

![Amplitude chart with enriched data](/docs/assets/amplitude/enriched.png)

## Useful Resources[​](#useful-resources "Direct link to Useful Resources")

* [A/B Testing in Android Kotlin with ConfigCat and Amplitude - Blog post](https://configcat.com/blog/2023/06/09/how-to-ab-test-kotlin/)
* [Discover User Insights with Amplitude and ConfigCat - Blog post](https://configcat.com/blog/2024/09/24/user-insights-amplitude-configcat/)
* [A/B testing in React with Amplitude and ConfigCat - Blog post](https://configcat.com/blog/2022/05/18/measuring-the-impact-of-a-test-variation-in-react/)
* [A/B Testing in iOS with Feature Flags and Amplitude](https://configcat.com/blog/2023/01/24/how-to-implement-ab-testing-in-ios/)
* [ConfigCat Integrations API](https://configcat.com/docs/api/reference/integrations/)
