# Source: https://configcat.com/docs/integrations/segment.md

# Twilio Segment - Monitor your feature flag change events and feature flag analytics

Copy page

## Overview[​](#overview "Direct link to Overview")

There are two available integration opportunities between [ConfigCat and Twilio Segment](https://segment.com/docs/connections/sources/catalog/cloud-apps/configcat/):

* [Sending feature flag change events to Twilio Segment](#changeevents)
* [Sending feature flag evaluation analytics to Twilio Segment](#analytics)

## Sending feature flag change events to Twilio Segment[​](#changeevents "Direct link to Sending feature flag change events to Twilio Segment")

Ensures that every setting change in ConfigCat is sent to Segment as a [track event](https://segment.com/docs/connections/spec/track/).

![Twilio Segment Feature Flag Changed event](/docs/assets/segment/featureflagchanged.png)

### Installation[​](#installation "Direct link to Installation")

1. Have a [Twilio Segment account.](https://segment.com/)
2. Add the [ConfigCat source](https://segment.com/catalog/integrations/source/configcat/) to your Twilio Segment account and copy the Write Key.
3. Open the [integrations tab](https://app.configcat.com/product/integrations) on the ConfigCat Dashboard.
4. Click on Twilio Segment's CONNECT button and set the Twilio Segment Write Key acquired while adding the ConfigCat source in Twilio Segment.
5. OPTIONAL - Set the proper server of your Twilio Segment account. [More about Segment servers](https://segment.com/docs/guides/regional-segment/).
6. You're all set. Go ahead and make some changes to your feature flags, then check your events in Twilio Segment.

### Un-installation[​](#un-installation "Direct link to Un-installation")

1. Open the [integrations tab](https://app.configcat.com/product/integrations) on the ConfigCat Dashboard.
2. Click on Twilio Segment's DISCONNECT button.

### Event details[​](#event-details "Direct link to Event details")

Every feature flag change event sent to Twilio Segment by ConfigCat has the following properties:

* **event name:** `Feature Flag Changed`.
* **timestamp:** When the change happened.
* **details:** A summary of the change.
* **product\_id, product\_name**: The product where the change happened.
* **config\_id, config\_name**: The config where the change happened.
* **environment\_id, environment\_name**: The environment where the change happened.
* **url**: A direct link to the config/feature flag.
* **userId, user\_email, user\_full\_name**: Who made the changes.

## Sending feature flag evaluation analytics to Twilio Segment[​](#analytics "Direct link to Sending feature flag evaluation analytics to Twilio Segment")

Ensures that feature flag evaluations are sent into the Twilio Segment [ConfigCat source](https://segment.com/catalog/integrations/source/configcat/). With this integration, you get advanced analytics on your feature flag usage and A/B test results in any of Segment's destinations.

### Setup[​](#setup "Direct link to Setup")

1. **Add ConfigCat source in Twilio Segment:** Add the ConfigCat source in Twilio Segment.

2. **Install SDKs:** Add both the ConfigCat SDK and Segment SDK to your application.

3. **Configure SDKs:**

   * **ConfigCat SDK:** Initialize with your ConfigCat SDK key.
   * **Twilio Segment SDK:** Set up with the Twilio Segment Write Key acquired while adding the ConfigCat source in Twilio Segment.

4. **Integrate Feature Flag Evaluations:**

   * During the initialization of the ConfigCat SDK, subscribe to the `flagEvaluated` hook.

   * Send feature flag evaluation data to Twilio Segment using the `Feature Flag Evaluated` event name. Include the following parameters:

     <!-- -->

     * `feature_flag_key`: the feature flag's key.
     * `value`: the evaluated feature flag's value or Variation ID.
     * `variation_id` (optional): the evaluated feature flag's Variation ID.
     * `userId` (optional): the user object's identifier used during feature flag evaluation.
     * `user` (optional): the user object used during feature flag evaluation.

Code samples:

* JavaScript, Node, SSR
* React
* Python
* Ruby
* Go
* Java
* Android
* Swift (iOS)
* Other languages

```js
const segmentAnalytics = AnalyticsBrowser.load({ writeKey: "#YOUR_SEGMENT_WRITE_KEY#" });
segmentAnalytics.addSourceMiddleware(({payload, next}) => {
    payload.obj.context.integration = payload.obj.context.integration || {};
    payload.obj.context.integration['name'] = 'configcat';
    payload.obj.context.integration['version'] = '1.0.0';
    next(payload);
});

const configCatClient = configcat.getClient("#YOUR_SDK_KEY#", PollingMode.AutoPoll, {
    setupHooks: (hooks) =>
        hooks.on('flagEvaluated', evaluationDetails => {
            if (evaluationDetails.user) {
                segmentAnalytics.identify(evaluationDetails.user.identifier, evaluationDetails.user);
            }
            segmentAnalytics.track('Feature Flag Evaluated',
                {
                    'feature_flag_key': evaluationDetails.key,
                    'value': evaluationDetails.value,
                    'variation_id': evaluationDetails.variationId,
                    'user': evaluationDetails.user
                });
        }),
});

```

```tsx
const segmentAnalytics = AnalyticsBrowser.load({ writeKey: "#YOUR_SEGMENT_WRITE_KEY#" });
segmentAnalytics.addSourceMiddleware(({payload, next}) => {
    payload.obj.context.integration = payload.obj.context.integration || {};
    payload.obj.context.integration['name'] = 'configcat';
    payload.obj.context.integration['version'] = '1.0.0';
    next(payload);
});

//...

<ConfigCatProvider
  sdkKey="#YOUR_SDK_KEY"
  pollingMode={PollingMode.AutoPoll}
  options={{
    setupHooks: (hooks) =>
      hooks.on('flagEvaluated', evaluationDetails => {
        if (evaluationDetails.user) {
            segmentAnalytics.identify(evaluationDetails.user.identifier, evaluationDetails.user);
        }
        segmentAnalytics.track('Feature Flag Evaluated',
            {
                'feature_flag_key': evaluationDetails.key,
                'value': evaluationDetails.value,
                'variation_id': evaluationDetails.variationId,
                'user': evaluationDetails.user
            });
      }),
  }}
>
</ConfigCatProvider>

```

```python
import segment.analytics as analytics
import configcatclient
from configcatclient.configcatoptions import ConfigCatOptions, Hooks
import uuid

analytics.write_key = '#YOUR_SEGMENT_WRITE_KEY#'

def on_flag_evaluated(evaluation_details):
    if evaluation_details.user is not None:
        analytics.track(user_id=evaluation_details.user.get_identifier(), 
            event='Feature Flag Evaluated',  
            properties={
                'feature_flag_key': evaluation_details.key,
                'value': evaluation_details.value,
                'variation_id': evaluation_details.variation_id,
                'user': vars(evaluation_details.user)
            }, 
            context={
                'integration': {
                    'name': 'configcat',
                    'version': '1.0.0'
                }
            }
        )
    else:
        analytics.track(anonymous_id=str(uuid.uuid4()), # Or any other kind of random anonymus id.
        event='Feature Flag Evaluated',  
        properties={
            'feature_flag_key': evaluation_details.key,
            'value': evaluation_details.value,
            'variation_id': evaluation_details.variation_id
        }, 
        context={
            'integration': {
                'name': 'configcat',
                'version': '1.0.0'
            }
        })
    pass

client = configcatclient.get('#YOUR_SDK_KEY#',
    ConfigCatOptions(
        hooks=Hooks(on_flag_evaluated=on_flag_evaluated)
    )
)

```

```ruby
require 'configcat'
require 'segment/analytics'
require 'securerandom'

Analytics = Segment::Analytics.new({
    write_key: '#YOUR-SEGMENT-WRITE-KEY#',
    on_error: Proc.new { |status, msg| print msg }
})

def on_flag_evaluated(evaluation_details)
    if evaluation_details.user
        Analytics.track(
            user_id: evaluation_details.user.get_identifier(),
            event: "Feature Flag Evaluated",  
            properties: {
                feature_flag_key: evaluation_details.key,
                value: evaluation_details.value,
                variation_id: evaluation_details.variation_id,
                user: evaluation_details.user
            },
            context: {
                integration: {
                    name: 'configcat',
                    version: '1.0.0'
                }
            }
        )
    else
        Analytics.track(
            anonymous_id: SecureRandom.uuid, # Or any other kind of random anonymus id.
            event: "Feature Flag Evaluated",  
            properties: {
                feature_flag_key: evaluation_details.key,
                value: evaluation_details.value,
                variation_id: evaluation_details.variation_id
            },
            context: {
                integration: {
                    name: 'configcat',
                    version: '1.0.0'
                }
            }
        )
    end
end

client = ConfigCat.get("#YOUR-SDK-KEY#",
    ConfigCat::ConfigCatOptions.new(
        hooks: ConfigCat::Hooks.new(on_flag_evaluated: method(:on_flag_evaluated))
    )
)

```

```go
import (
	configcat "github.com/configcat/go-sdk/v9"
	"github.com/google/uuid"
	"github.com/segmentio/analytics-go"
)

analyticsClient := analytics.New("#YOUR_SEGMENT_WRITE_KEY#")

configCatClient := configcat.NewCustomClient(configcat.Config{SDKKey: "#YOUR_SDK_KEY#",
    Hooks: &configcat.Hooks{OnFlagEvaluated: func(details *configcat.EvaluationDetails) {
        if details.Data.User != nil {
            analyticsClient.Enqueue(analytics.Track{
                UserId: details.Data.User.(*configcat.UserData).Identifier,
                Event:  "Feature Flag Evaluated",
                Properties: analytics.NewProperties().
                    Set("feature_flag_key", details.Data.Key).
                    Set("value", details.Value).
                    Set("variation_id", details.Data.VariationID).
                    Set("user", details.Data.User.(*configcat.UserData)),
                Context: &analytics.Context{
                    Extra: map[string]interface{}{
                        "integration": map[string]interface{}{
                            "name":    "configcat",
                            "version": "1.0.0",
                        },
                    },
                },
            })
        } else {
            analyticsClient.Enqueue(analytics.Track{
                AnonymousId: uuid.New().String(), // Or any other kind of random anonymus id.
                Event:       "Feature Flag Evaluated",
                Properties: analytics.NewProperties().
                    Set("feature_flag_key", details.Data.Key).
                    Set("value", details.Value).
                    Set("variation_id", details.Data.VariationID),
                Context: &analytics.Context{
                    Extra: map[string]interface{}{
                        "integration": map[string]interface{}{
                            "name":    "configcat",
                            "version": "1.0.0",
                        },
                    },
                },
            })
        }
    }}})

```

```java
import com.configcat.ConfigCatClient;
import com.configcat.User;
import com.segment.analytics.Analytics;
import com.segment.analytics.messages.TrackMessage;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

//...

Analytics analytics = Analytics.builder("#YOUR_SEGMENT_WRITE_KEY#").build();
ConfigCatClient client = ConfigCatClient.get("#YOUR-SDK-KEY#", options -> {
    options.hooks().addOnFlagEvaluated(details -> {
        
        Map<String, String> contextMapIntegrations = new HashMap<>();
        contextMapIntegrations.put("name", "configcat");
        contextMapIntegrations.put("version", "1.0.0");

        Map<String, Object> contextMap = new HashMap<>();
        contextMap.put("integration", contextMapIntegrations);

        Map<String, Object> propertiesMap = new HashMap<>();
        propertiesMap.put("feature_flag_key", details.getKey());
        propertiesMap.put("value", details.getValue());
        propertiesMap.put("variation_id", details.getVariationId());

        if (details.getUser() != null){
            propertiesMap.put("user", details.getUser());

            analytics.enqueue(TrackMessage.builder("Feature Flag Evaluated")
                    .userId(details.getUser().getIdentifier())
                    .properties(propertiesMap)
                    .context(contextMap)
            );
        } else {
            analytics.enqueue(TrackMessage.builder("Feature Flag Evaluated")
                    .anonymousId(UUID.randomUUID().toString())
                    .properties(propertiesMap)
                    .context(contextMap)
            );
        }
    });
});

```

```java
Analytics analytics = new Analytics.Builder(getApplicationContext(), "#YOUR_SEGMENT_WRITE_KEY#").build();
Analytics.setSingletonInstance(analytics);
ConfigCatClient client = ConfigCatClient.get("#YOUR-SDK-KEY#", options -> {
    options.cache(new SharedPreferencesCache(getApplicationContext()));
    options.hooks().addOnFlagEvaluated(details -> {
        Properties properties = new Properties()
            .putValue("feature_flag_key", details.getKey())
            .putValue("value", details.getValue())
            .putValue("variation_id", details.getVariationId());

        Map<String, Object> contextMapIntegrations = new HashMap<>();
        contextMapIntegrations.put("name", "configcat");
        contextMapIntegrations.put("version", "1.0.0");

        Options optionsAnalytics = new Options().putContext("integration", contextMapIntegrations);

        if (details.getUser() != null){
            analytics.identify(details.getUser().getIdentifier());
            properties.putValue("user", details.getUser());
        } else {
            analytics.identify(new Traits().putValue("anonymousId", UUID.randomUUID().toString()));
        }

        analytics.track("Feature Flag Evaluated", properties, optionsAnalytics);
    });
});

```

```swift
import ConfigCat
import Segment

let configuration = Configuration(writeKey: "#YOUR_SEGMENT_WRITE_KEY#")
let analytics = Analytics(configuration: configuration)
analytics.add { ev in
    var event = ev
    if var ctx = ev?.context?.dictionaryValue {
        ctx[keyPath: "integration.name"] = "configcat"
        ctx[keyPath: "integration.version"] = "1.0.0"
        event?.context = try? JSON(ctx)
    }
    return event
}
let client = ConfigCatClient.get(sdkKey: "#YOUR-SDK-KEY#") { options in
    options.hooks.addOnFlagEvaluated { details in
        if let user = details.user {
            analytics.identify(userId: user.identifier)
        }

        analytics.track(name: "Feature Flag Evaluated", properties: [
            "feature_flag_key": details.key,
            "value": details.value,
            "variation_id": details.variationId ?? "",
            "user": details.user?.description ?? ""
        ])
    }
}

```

While our documentation primarily provides code examples for languages that Twilio Segment natively supports and has an official SDK, you can integrate with other languages by sending an event to Twilio Segment with a third-party SDK or with using the [Segment's HTTP API source](https://segment.com/docs/connections/sources/catalog/libraries/server/http-api/).

1. **Subscribe to the FlagEvaluated hook** in the ConfigCat SDK.

2. **Send an event to Twilio Segment** using the `Feature Flag Evaluated` event name. If the feature flag was evaluated with a user object, set the event's `userId` property to the user object's identifier. Otherwise, set the `anonymousId` property to a random generated string. Also, include the following event properties:

   <!-- -->

   * `feature_flag_key`: the feature flag's key from the FlagEvaluated hook's EvaluationDetails.
   * `value`: the evaluated feature flag's value or the variationId from the FlagEvaluated hook's EvaluationDetails.
   * `variation_id`: the evaluated feature flag's value or the variationId from the FlagEvaluated hook's EvaluationDetails.
   * `user` (optional): the user object used during feature flag evaluation.

note

For Text feature flags with lengthy values (e.g., JSON), send the `variationId` instead of the `value` as the `value` to Twilio Segment. The `variationId` is a hashed version of the feature flag value, accessible on the ConfigCat Dashboard by enabling the *Show VariationIDs to support A/B testing* setting. Learn more [here](https://app.configcat.com/product/preferences).

4. Deploy your application and wait for feature flag evaluations to happen so feature flag evaluation events can be sent to Twilio Segment.
5. Add the preferred destination in Twilio Segment for your source and configure your mappings.
6. Enable the destination and utilize advanced feature flag analytics in the destination.

### Example event[​](#example-event "Direct link to Example event")

Check your source's debugger to see the events.

![Twilio Segment event debugger](/docs/assets/segment/featureflagevaluated.png)

## Useful Resources[​](#useful-resources "Direct link to Useful Resources")

* [Using Twilio and ConfigCat to Understand Your Business - Blog Post](https://configcat.com/blog/2024/11/28/using-twilio-and-configcat/)
* [ConfigCat Integrations API](https://configcat.com/docs/api/reference/integrations/)
