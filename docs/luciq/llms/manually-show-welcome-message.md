# Source: https://docs.luciq.ai/references/user-interface-design/manipulating-the-welcome-message/manually-show-welcome-message.md

# Manually Show Welcome Message

This API can be used to manually show the welcome message at anytime. Only one argument is passed to this method which is an enum detailing whether to show the beta testers welcome message or the live user welcome message.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - ObjC" %}

```objectivec
[Luciq showWelcomeMessageWithMode:LCQWelcomeMessageModeBeta];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.showWelcomeMessage(WelcomeMessage.State.BETA);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.showWelcomeMessage(WelcomeMessage.State.BETA)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.showWelcomeMessage(Luciq.welcomeMessageMode.beta)
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.showWelcomeMessageWithMode(WelcomeMessageMode.beta)
```

{% endtab %}
{% endtabs %}

#### Welcome Message Parameters

{% tabs fullWidth="true" %}
{% tab title="iOS - ObjC" %}

```objectivec
//Beta testers message
LCQWelcomeMessageModeBeta
//Live users message
LCQWelcomeMessageModeLive
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Beta testers message
WelcomeMessage.State.BETA
//Live users message
WelcomeMessage.State.LIVE
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Beta testers message
WelcomeMessage.State.BETA
//Live users message
WelcomeMessage.State.LIVE
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Beta testers message
Luciq.welcomeMessageMode.beta
//Live users message
Luciq.welcomeMessageMode.live
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Beta testers message
WelcomeMessageMode.beta
//Live users message
WelcomeMessageMode.live
```

{% endtab %}
{% endtabs %}
