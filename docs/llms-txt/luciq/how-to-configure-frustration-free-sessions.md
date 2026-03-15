# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/getting-started-with-luciq/frustration-free-sessions/how-to-configure-frustration-free-sessions.md

# How to Configure Frustration-free Sessions

Configure Frustration-Free Sessions your way to ensure your score reflects your unique app needs and how you define user frustration for your end users. You have full control over how different issue types contribute to frustration-free sessions and issue prioritization in the issues list.

### Define How Issue Types Affect Your Score

To adjust your configuration:

1. **Go to: Settings → Frustration-Free Sessions Config.**
2. You will see the issue types that factor into your score, based on your plan and platform.
3. (For owners only) Adjust the crash configuration of ANRs and OOMs.
   1. This dictates if a session should be considered crashing or not if an ANR or OOM occurred.
   2. If an issue type is set as crashing, its impact is set to highest and cannot be edited.
4. Adjust the **impact level** of each issue type to control how it influences session classification in frustration-free sessions and issue prioritization.

{% hint style="warning" %}
Configuring frustration-free sessions only affects future sessions; your historical score will remain unaffected.
{% endhint %}

### Impact Levels

The impact level determines how much an issue type contributes to marking a session as frustrating:

* **Highest impact**: Has a critical effect on session quality. A single occurrence of this type, even if there are other less significant issues in the session, will mark the session as frustrating.
* **High impact**: Strongly affects the session quality. Just one or two occurrences, when paired with other issues in the session, will mark the session as frustrating.
* **Medium impact**: Moderately affects session quality. A few occurrences in combination with other issues could mark the session as frustrating.
* **Low impact**: Has a small effect on session quality. Many frustrating occurrences of this type are required to mark the session as frustrating.
* **No impact**: Has no effect on session quality. Occurrences of this type do not contribute to session classification or affect frustration-free sessions.

{% hint style="info" %}
Fatal crashes are not editable; they are always set to the highest impact.\* Non-fatals are not editable; they are always set to no impact.
{% endhint %}

***

### Recommended Configuration

We recommend setting:

* **Fatals, OOMs, and ANRs** to highest impact since they completely disrupt the experience and should have the strongest influence on the score.
* **App hangs** to high impact, as they are highly noticeable and directly affect the user experience.
* **Force restarts** to high impact, as they are a strong signal of user frustration.
* **App launch** to high impact since it’s one of the most visible interactions, directly affecting user perception and app ratings.
* **Screen loading, UI hangs, and flows** to medium impact, as they moderately affect session quality.
* **Network issues** to low impact, as they occur very frequently in a session, and sometimes happen in the background. Keeping them at a low impact level ensures they don’t disproportionately affect the score.

<figure><img src="https://files.readme.io/436c8104ad7c434e0da5a05720c5e02beba5edf485d8c6de71d6a3282a74d390-Screenshot_2025-03-17_at_1.37.26_AM.png" alt=""><figcaption></figcaption></figure>

***

### Control APM Traces in Your Score

For **APM issues (App Launches, Flows, Networks, UI Hangs, Screen loading)**, which you can configure each trace as either a **Key Metric** or **Non-Key Metric**:

* **Key Metrics**: Affect your Frustration-Free Sessions score and issue prioritization.
* **Non-Key Metrics**: Do not contribute to session classification or affect the score.

By default, all traces are considered **Key Metrics**.

### Adjusting Key Metrics

You can exclude specific traces from your score in three ways:

1. From the **Issues List**

<figure><img src="https://files.readme.io/43b89150beb1ef899efecf64c4f326279ba2428caeed6f27fa6d13bdb84b6bce-Screenshot_2025-03-17_at_1.47.07_AM.png" alt=""><figcaption></figcaption></figure>

2. On the **List Page**

<figure><img src="https://files.readme.io/357910b534e44718c7d0d11c1354bf7aad1b28ee7024004c50d2441824635219-image.png" alt=""><figcaption></figcaption></figure>

3. In the **Details Page** for the issue type

<figure><img src="https://files.readme.io/712b94c06c5a4b2b4905c37ca58f16ef7f0eaa9254f6fb1cbcd003fc2f2f9e1d-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Updating your key metrics doesn't affect the already calculated app apdex and will be applied moving forward.
{% endhint %}

Fine-tuning these settings ensures that your frustration-free session score reflects only the most relevant signals for your app.
