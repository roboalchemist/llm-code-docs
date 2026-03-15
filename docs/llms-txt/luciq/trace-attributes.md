# Source: https://docs.luciq.ai/references/application-performance-monitoring/network/trace-attributes.md

# Trace Attributes

You can add/edit a custom trace attribute using the following APIs, passing a `string` key and a `string` value.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let urlPattern = "*.example.com/*"
let urlPredicate = NSPredicate(format: "SELF LIKE[c] '\(urlPattern)'")
APM.addNetworkTraceAttributesForURL(matching: urlPredicate, owner: self) { trace in
    return [
        "trace": "example"
    ]
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQAPM addNetworkTraceAttributesForURLMatchingPredicate:[NSPredicate predicateWithFormat:@"SELF LIKE[c] '%@'", @"*.example.com/*"]
                                                   owner:self
                                            usingHandler:^NSDictionary<NSString *,NSString *> * _Nullable(LCQNetworkTrace * _Nonnull networkTrace) {
    return @{
        @"type": @"example"
    };
}];
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.addOnNetworkTraceListener(new OnNetworkTraceListener(
    new UrlPredicate() {
        @Override
        public boolean check(@NonNull String url) {
            // Add filter here the URL 
            // return boolean
        }
    }); 
    {
        @Override
        public Map<String, String> addAttributesOnFinish(NetworkTrace trace) {
            Map<String, String> map;
            map.put("Key", "Value");
            // Up to five attributes
            return map;
        }
    }
);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.addOnNetworkTraceListener(
    object: OnNetworkTraceListener(
                UrlPredicate { url:String ->
                    // Add filter here the URL 
                    // return boolean
                }
    )
    {
        override fun addAttributesOnFinish(trace: NetworkTrace?): MutableMap<String, String?> {
            // Return map of Pairs (i.e. keys and values)
            return mutableMapOf(
                        // Up to five attributes
                    Pair("Key", "Value")
            )
        }
    }
)
```

{% endtab %}
{% endtabs %}
