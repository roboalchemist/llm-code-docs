# Source: https://docs.instabug.com/organization-settings/gdpr.md

# GDPR

At Luciq, we've been hard at work ensuring that all your user data protected while being fully transparent with you.

Now, Luciq is fully compliant with the European **General Data Protection Regulation (GDPR)** which is effective as of May 25, 2018.

Please refer [here](https://luciq.ai/dpa) for the **Data Protection Addendum (DPA)**.

The updated terms of service can be found [here](https://luciq.ai/terms).

{% hint style="info" %}

#### Personally Identifiable Information

The personally identifiable information collected by Luciq's SDK by default is **name**, **email**, and **IP**.

Any other custom attributes are set through the application code.
{% endhint %}

### Luciq User ID (UUID)

Luciq automatically generates a unique user ID when the app runs for the first time on your end user's device. This identifier is randomly created and **is not intended to persist across app reinstallations or different devices**. It is included with each reported issue or session to help estimate the number of distinct users affected by a given problem and link the issues relevant to this user.

This ID does **not reveal any personally identifiable information (PII)** and is not linked to a specific user account unless you explicitly set a [custom user identifier](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification#user-email-and-name) using the Luciq SDK. If the app is reinstalled, a new user ID is generated, and any reports or sessions sent to Luciq will be tagged with this new ID.

The primary purpose of this identifier is to **aggregate issue impact** by showing how many unique user sessions have encountered a specific error or behavior, and also issues relevant to this user. This allows teams to prioritize issues that affect a larger portion of their user base.

If needed, you can use the below APIs to identify and remove user data.

### Delete User API

We've added an API that allows you to delete the data of a specific user on-demand. This API will delete any personally identifiable information, custom attributes, logs, screenshots and any data that we have for this user. This action is irreversible.

### Identify User

In order to delete a user, they need to be identified first, whether through email or UUID. In case you need to find the user's UUID, you can use the below methods available in the SDK:

{% tabs %}
{% tab title="iOS" %}
{% code overflow="wrap" %}

```objective-c
(void)userUUID:(void (^)(NSString * _Nullable uuid))userUUIDCompletionHandler;
```

{% endcode %}
{% endtab %}

{% tab title="Android" %}

```java
//Java
Luciq.getUserUUID((uuid)->{
//use the uuid
 });

//Kotlin
Luciq.getUserUUID { uuid -> 
//use the uuid
}
```

{% endtab %}
{% endtabs %}

#### Via Email

You can delete a user's data via their email. The API for this is as follows:

{% code title="cURL" overflow="wrap" %}

```curl
curl -XDELETE 'https://api.instabug.com/api/web/public/users/v1'\?application_token\="app_token"\&email\="email"
```

{% endcode %}

### Via UUID

Alternatively, you can delete a user's data via UUID instead of email using the below cURL:

{% code title="cURL" overflow="wrap" %}

```curl
curl --location --request DELETE 'https://api.instabug.com/api/web/public/users/uuid/v1?application_token=app_token&uuid=uuid' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token" : "SECRET_TOKEN"
}'
```

{% endcode %}

{% hint style="info" %}
*Please note that for security purposes, you can get the secret token for your application by reaching out to our support team.*
{% endhint %}

### Data Retention and Export

You can now customize how long Luciq retains your users' data. This is set by default based on your plan. You can request an export of all the data that we have for your account or for a specific user. Please reach out to us at <contactus@luciq.ai>
