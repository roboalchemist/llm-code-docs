# Source: https://docs.luciq.ai/references/report-data/visual-repro-steps.md

# Repro Steps

Much like user steps, repro steps are also collected by default. They show the user steps, which are the steps the user has taken until the report was sent in compiled by view.

User Repro Collection can be disabled using this method.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.reproStepsMode = .disable
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.reproStepsMode = LCQUserStepsModeDisable;
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Method 1
new Luciq.Builder(this, “APP_TOKEN”)
    .setInvocationEvents(LuciqInvocationEvent.SHAKE)
  .setReproStepsState(State.DISABLED)
    .build(); 

//Method 2
Luciq.setReproStepsState(State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Method 1
Luciq.Builder(this, “APP_TOKEN”)
    .setInvocationEvents(LuciqInvocationEvent.SHAKE)
  .setReproStepsState(State.DISABLED)
    .build(); 

//Method 2
Luciq.setReproStepsState(State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
import Luciq, { ReproStepsMode } from '@luciq/react-native';

Luciq.setReproStepsMode(ReproStepsMode.enabled);
```

{% endtab %}
{% endtabs %}

**Repro Steps Parameters:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Enable
.enable
//Enable without Screenshots
.enabledWithNoScreenshots
//Disable
.disable
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Enable
LCQUserStepsModeEnable
//Enable without Screenshots
LCQUserStepsModeEnabledWithNoScreenshots
//Disable
LCQUserStepsModeDisable
```

{% endtab %}

{% tab title="Android" %}

```java
//Enabled
State.ENABLED;
//Enable without Screenshots
State.ENABLED_WITH_NO_SCREENSHOTS
//Disabled
State.DISABLED;
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Enabled
ReproStepsMode.enabled
//Enabled without Screenshots
ReproStepsMode.enabledWithNoScreenshots
//Disabled
ReproStepsMode.disabled
```

{% endtab %}

{% tab title="Cordova" %}

```javascript
//Enabled
'enabled'
//Disabled
'disabled'
```

{% endtab %}
{% endtabs %}
