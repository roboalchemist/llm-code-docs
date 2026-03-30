# Source: https://docs.luciq.ai/references/user-identification-data/retrieve-uuid.md

# Retrieve UUID

You can use the following APIs to identify users and retrieve their UUIDs.

{% tabs fullWidth="true" %}
{% tab title="iOS" %}

```swift
(void)userUUID:(void (^)(NSString * _Nullable uuid))userUUIDCompletionHandler;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.getUserUUID((uuid)->{
//use the uuid
 });
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.getUserUUID { uuid -> 
//use the uuid
}
```

{% endtab %}
{% endtabs %}
