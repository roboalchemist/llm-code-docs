# Source: https://docs.instabug.com/android/set-up-luciq-for-android/setup-in-app-surveys/survey-callbacks-for-android.md

# Survey Callbacks for Android

{% hint style="warning" %}

### Avoiding Memory Leaks

These APIs hold the callbacks in a strong reference, so we strongly suggest to avoid registering callbacks without unregistering them when needed, as it may cause a memory leak.
{% endhint %}

You can execute code in a callback that gets called before a survey is shown and after it has been dismissed. You can use this for things like pausing and resuming a game, for example.

### Before Showing the Survey

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Surveys.setOnShowCallback(OnShowCallback {
                //Pause game
            }            
        )
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Surveys.setOnShowCallback(new Runnable() {
	@Override
	public void run() {
		//Pause game
	}
});
```

{% endcode %}
{% endtab %}
{% endtabs %}

### After the Survey Has Been Dismissed

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Surveys.setOnFinishCallback(OnFinishCallback {
            }
        )
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Surveys.setOnFinishCallback(new OnFinishCallback() {
            @Override
            public void onFinish(String surveyId, String state, JSONObject response) {
            }
        });
```

{% endcode %}
{% endtab %}
{% endtabs %}
