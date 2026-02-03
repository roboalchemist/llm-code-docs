# Source: https://docs.intelligems.io/integrations/klaviyo-integration.md

# Klaviyo Integration

## What you can do with Klaviyo

Use a **Klaviyo segment** (like VIP customers) to control **who sees a specific Test or Personalization** in Intelligems.

### How it Works

1. When a visitor is cookied by Klaviyo we use that cookie (`_kx`) to “ask” Klaviyo: “Which segments is this visitor
2. If Klaviyo is able to identify the visitor (i.e. they completed a signup flow, clicked through an email/sms, returned to a site from a browser they previously made a purchase, etc.) then so is Intelligems.

{% hint style="info" %}
If we're unable to identify the visitor, they will be shown the control / not enter the experience.&#x20;
{% endhint %}

### Why This is Better Targeting Than Using UTMs

1. **Does not require clickthrough** - They do *not* have to click through a Klaviyo email in order for this targeting to work, it’s based on their cookies (which could have been previously set).
2. **Cross-browser identification** - If the visitor later opens up a Klaviyo email on a *different* device and/or visits the website and logs in, we will now have the ability to target new browser/device (cookie) and can serve up cross-device experiences.

### Prerequisites

* Intelligems is installed on your store
* Klaviyo is installed and set up. [Install here](https://app.intelligems.io/integrations).&#x20;
* You have at least one **Klaviyo segment** (e.g. “VIP”)<br>

### Step 1: Connect Klaviyo to Intelligems

1. In Intelligems, on the left navigation, click on **Integrations**
2. Find **Klaviyo** under Analytics
3. Click **Sign in with Klaviyo**
4. Log in if prompted
5. Approve permissions (profiles + segments)
6. Confirm Klaviyo shows as **Active** in the Intelligems integrations page.

### Step 2: Confirm Your Segment in Klaviyo

1. Open Klaviyo
2. Go to **Lists & Segments**
3. Confirm the **Segment** you want to target (e.g. **VIP**) exists

{% hint style="info" %}
We can only identify visitors in **Segments.** \
We *cannot* identify visitors in Lists or using Profile Tags.&#x20;
{% endhint %}

4. *Optional* Send yourself an email so your profile is tagged with that Segment

{% hint style="success" %}
We recommend you star/favorite **Segments** inside of Klaviyo that are active in a Test or Personalization
{% endhint %}

### Step 3: Apply the Segment to a Test or Personalization

1. Create a **Test** or **Personalization** in Intelligems
2. Go to the **Targeting** tab
3. Select **Custom**
4. In the **Targeting type** dropdown, select **Klaviyo Segment**

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FzRez9ZG8rfG7p96ibZZ3%2FScreenshot%202026-02-02%20at%2011.58.17%E2%80%AFAM.png?alt=media&#x26;token=011bbe00-e18a-4430-818a-8fe43ce53936" alt=""><figcaption></figcaption></figure>

5. Add a condition **Klaviyo segment equals `VIP`** &#x20;

{% hint style="info" %}
To add multiple Segments, use the +Or Condition and +AND Condition option&#x20;
{% endhint %}

6. Click **Save**&#x20;

{% hint style="warning" %}
For Tests, use **Advanced**, not Custom Targeting, if you want to avoid default assignment.\
Otherwise, users may get a default variation first and never switch when the segment is detected.
{% endhint %}

### Step 4: Verify It’s Working

1. Open the Klaviyo email you sent
2. Click the link to your store
3. Watch the URL — you should see a Klaviyo cookie parameter
4. The page may load the default first, then update
5. Confirm the correct experience appears (e.g. your personalized discount appears)

### Result

Users in the targeted Klaviyo segment see the intended Intelligems variation automatically 🎯

### FAQs

<details>

<summary><strong>Does Intelligems receive customer profile data from Klaviyo?</strong></summary>

No. Only segment membership is resolved via exchange ID.

</details>

<details>

<summary><strong>Is segment membership evaluated in real time?</strong></summary>

Segment membership is resolved on visit and cached for up to 24 hours.

</details>

<details>

<summary><strong>Does this work across devices?</strong></summary>

Yes, if the visitor clicks a Klaviyo link on each device or logs into that store. If Klaviyo is able to identify the visitor, then so is Intelligems.&#x20;

</details>

<details>

<summary><strong>Does this work with Klaviyo lists?</strong></summary>

No, this is only for Segments.

</details>

<details>

<summary><strong>Does this read Klaviyo profile tags?</strong></summary>

No, this is only for Segments.

</details>

### Additional questions about the Klaviyo Integration?

[See Klaviyo API documentation](https://developers.klaviyo.com/en/reference/segments_api_overview) or [email us](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).&#x20;
