# Source: https://docs.luciq.ai/references/application-performance-monitoring/network/index.md

# Enable or disable network logging

Network monitoring works out of the box. You can enable or disable it using the following APIs and passing a `boolean` to it.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
NetworkLogger.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQNetworkLogger.enabled = NO;
```

{% endtab %}

{% tab title="Android" %}

```groovy
//Disable
Luciq {
    APM {
        networkInterceptingEnabled false
    }
}

//Enable
Luciq {
    APM {
        networkInterceptingEnabled true
    }
}
```

{% endtab %}

{% tab title="RN - iOS" %}

```javascript
// Enable
APM.setNetworkEnabledIOS(true)

// Disable
APM.setNetworkEnabledIOS(false)
```

{% endtab %}

{% tab title="RN - Android" %}

```groovy
Luciq {
    APM {
        networkInterceptingEnabled false
    }
}
```

{% endtab %}
{% endtabs %}
