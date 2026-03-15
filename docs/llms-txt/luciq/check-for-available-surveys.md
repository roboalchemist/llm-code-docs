# Source: https://docs.luciq.ai/references/in-app-surveys/check-for-available-surveys.md

# Get Available Surveys

This method returns all possible available surveys that can be shown to the user. A list of survey objects is returned by this API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.availableSurveys { (surveys) in
            
        }
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQSurveys availableSurveysWithCompletionHandler: ^(NSArray<LCQSurvey *> *validSurveys) {
        
    }];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.getAvailableSurveys();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.getAvailableSurveys()
```

{% endtab %}

{% tab title="RN" %}

```javascript
const availableSurveys = await Surveys.getAvailableSurveys();
```

{% endtab %}

{% tab title="Flutter" %}

```dart
final titles = Surveys.getAvailableSurveys();
```

{% endtab %}
{% endtabs %}
