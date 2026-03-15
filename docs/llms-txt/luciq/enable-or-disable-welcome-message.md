# Source: https://docs.luciq.ai/references/user-interface-design/manipulating-the-welcome-message/enable-or-disable-welcome-message.md

# Set Welcome Message Mode

This method can be used to set whether or not the welcome message is shown by default on the first app launch and whether to show the beta testers welcome message or the live users welcome message.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - ObjC" %}

```objectivec
[Luciq setWelcomeMessageMode:LCQWelcomeMessageModeBeta]
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setWelcomeMessageState(WelcomeMessage.State.BETA);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setWelcomeMessageState(WelcomeMessage.State.BETA)
```

{% endtab %}

{% tab title="RN" %}

```javascript
import Luciq, { WelcomeMessageMode } from '@luciq/react-native';

Luciq.setWelcomeMessageMode(WelcomeMessageMode.beta) // For beta testers
Luciq.setWelcomeMessageMode(WelcomeMessageMode.live) // For live users
Luciq.setWelcomeMessageMode(WelcomeMessageMode.disabled) // Disable welcome message
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.setWelcomeMessageMode(WelcomeMessageMode.beta)
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
//Disable welcome message
LCQWelcomeMessageModeDisabled
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Beta testers message
WelcomeMessage.State.BETA
//Live users message
WelcomeMessage.State.LIVE
//Disable welcome message
WelcomeMessage.State.DISABLED
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Beta testers message
WelcomeMessage.State.BETA
//Live users message
WelcomeMessage.State.LIVE
//Disable welcome message
WelcomeMessage.State.DISABLED
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Beta testers message
WelcomeMessageMode.beta
//Live users message
WelcomeMessageMode.live
//Disable welcome message
WelcomeMessageMode.disabled
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Beta testers message
WelcomeMessageMode.beta
//Live users message
WelcomeMessageMode.live
//Disable welcome message
WelcomeMessageMode.disabled
```

{% endtab %}
{% endtabs %}
