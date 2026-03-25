# Source: https://developers.make.com/custom-apps-documentation/community-apps/tips-and-tricks/control-of-access-in-apps-using-basic-connection.md

# Access control using basic connection

If your app uses a [basic](https://developers.make.com/custom-apps-documentation/app-components/connections/basic-connection) connection, you can control access to your app by implementing access control and transforming the connection from a [basic](https://developers.make.com/custom-apps-documentation/app-components/connections/basic-connection) to an [OAuth](https://developers.make.com/custom-apps-documentation/app-components/connections/oauth2) connection. The transformation offers several advantages, including:

* restricting app usage to only those users with granted access
* revoking access when necessary, such as in cases of expired subscriptions to your app
* maintaining the authorization flow that establishes a new connection with provided credentials to the API service
* ensuring that the access control flow is secure and not exposed in the browser console or [DevTool](https://developers.make.com/custom-apps-documentation/debug-your-app/make-devtool)
* centralizing access control code within a single location, preventing redundancy across modules or RPCs
* managing a reasonable volume of requests to the backend responsible for access control within your app

{% hint style="info" %}
The solution described below is just one of many possible approaches. Feel free to explore alternative methods as well.
{% endhint %}

## Database of users with granted access to your app

First, you need a database with the list of users with granted access, their credentials, time zone, and the date of access expiration.

In our guide, we store the list of users and their credentials in a Google Sheets spreadsheet. The spreadsheet contains the following columns:

* **EMAIL** (text): Email of the user for better recognition.
* **TOKEN** (text): Token that was provided to the user to access the app.
* **VALID UNTIL** (date-time): The date until which the user can access the app.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2a777fbeb12879790403bb1f059e6bd88d0ffef5%2FScreenshot%202023-09-20%20at%2020.19.02.png?alt=media" alt="" width="510"><figcaption></figcaption></figure></div>

{% hint style="info" %}
You can automate the subscription flow with a scenario in Make, for example:

* the generation of a token for a new user
* updating the date of expiration upon the user's payment for the month/year subscription
  {% endhint %}

## Backend for the access control flow

To access the database of users you need to implement an endpoint that, whenever called, will return information on whether the user has been granted access to your API. In our guide, we use a scenario in Make that handles the backend of the access control.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-9a01af9749b0de45bc0aad10d1c263b9d9cd7e6b%2FScreenshot%202023-09-20%20at%2016.42.45.png?alt=media" alt="" width="563"><figcaption><p>Scenario handling the backend for access control</p></figcaption></figure>

{% hint style="info" %}
Create the scenario from this [template](http://www.make.com/en/integration/11151-access-control-to-an-ad).
{% endhint %}

### Scenario used as the backend for the access control

1. **Webhooks > Custom webhook**: Listens to a request that contains data with user's credentials that you have provided to the user. In this case, we used the parameter `token`.
2. **Google Sheets > Search Rows**: Searches for the record belonging to the user. Here, we look up via the `token` parameter.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3bd6b9d123b1fa616826a6ffbbdaef9a90a1505e%2Fbackendaccesscontrol_googlesheets.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

3. **Router**: Handles two available results - the user does/doesn't have access to the app.

{% tabs %}
{% tab title="Filter in the 1st route" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4ee9b76eec039f2b25ad7b978cd88130be70df19%2Ffirstroute_accesscontrol.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the function works with the `timezone` parameter. The `timezone` of the **developer** is used.

The `timezone` parameter is used because the mapped date-time is not a timestamp and does not include information about the time zone.

Do not forget to edit the `timezone` value according to the time zone your system is working in.
{% endhint %}
{% endtab %}

{% tab title="Filter in the 2nd route" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7de6e197c69b85851fdb1e8033f7b9133f41f196%2Fsecondroute_accesscontrol.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the checked checkbox for the fallback route. When the first route is not executed, the route for returning error will be triggered.
{% endhint %}
{% endtab %}
{% endtabs %}

4. **Webhooks > Webhook Response (1)**: If the user **does** have access to the app, status code `200` is returned to the webhook together with the date of expiration.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0e78de97b8bf1b4f6c7ce74f59a5ecbf2b763846%2Fwebhook_response.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the function works with the `timezone` parameter. The time zone of the **developer** is used.

The time zone parameter is used because the mapped date-time is not a timestamp and does not include information about the time zone.

This ensures that the date of expiration is correctly parsed and the connection will expire in the **user's** time zone, for example `22.9.2023 23:59:59` in `America/Chicago.`

Do not forget to edit the `timezone` value according to the time zone your system is working in.
{% endhint %}

5. **Webhooks > Webhook Response (2)**: If the user **doesn't** have access to the app, status code `400` is returned to the webhook. Additionally, the error message is returned.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8865119f2fdc9cd8e587db513fb72aea27668917%2Fwebhook_response2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Notice, that we differentiate 2 situations:

* the user doesn't have the correct credentials
* the user does have the correct credentials but their subscription has expired
  {% endhint %}

## Connection implementation in the app

Now, since we have the backend for access control ready, we can use it in our app.

{% hint style="info" %}
It is recommended to first implement the basic connection and make sure it works correctly.
{% endhint %}

### 1. The current implementation of basic connection

In our guide, the API we connect our app to uses basic access authentication. Therefore, this code in the communication tab in basic connection was originally implemented:

Go to your basic connection, that you have implemented and tested, and have it open in your web browser.

{% tabs %}
{% tab title="Source" %}

```json
{
  "url": "https://api.example.cz/v2/whoami",
  "headers": {
    "authorization": "Basic {{base64(parameters.username + ':' + parameters.password)}}"
  },
  "response": {
    "valid": {
      "condition": "{{body.status != 'error'}}"
    },
    "error": {
      "200": {
        "message": "[{{body.status}}]: {{ifempty(body.message.items, body.message)}}"
      },
      "message": "[{{statusCode}}]: {{body.reason || body.message}}"
    },
    "metadata": {
      "type": "text",
      "value": "{{body.username}}"
    }
  }
}
```

{% endtab %}
{% endtabs %}

### 2. Creation of a new OAuth connection

In your web browser, open a new tab with your app, go to the Connections tab, and click **Create a new Connection.** In the pop-up window, select the type `Oauth 2 (authorization code)`. Click **Save**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-6fd4fc7d62d97078b6016bc2bd6ffe3c6beeaf0d%2Fnewoauth.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

### 3. Set up connection parameters

Go to the tab with the `basic` connection and copy the connection parameters to your clipboard. Then, go to the second tab with your new OAuth connection and paste the connection parameters from your clipboard. Next, enter the parameters you use for your access control. Save the changes.

In our guide, we used our `token` parameter.

{% tabs %}
{% tab title="Appearance in the module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-63135be4f777e0c2fbc650c606aa6bd9469b0d1f%2Fconnection_parameters_token.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the `token` parameter that doesn't belong to the integrated API.

The `token` parameter is used by us to control the app access.
{% endhint %}
{% endtab %}

{% tab title="Connection parameters" %}

```json
[
    
    {
        "name": "username",
        "type": "text",
        "label": "Email",
        "required": true
    },
    {
        "name": "password",
        "type": "password",
        "label": "API Key",
        "required": true
    },
    {
        "name": "token",
        "type": "text",
        "label": "Token",
        "required": true,
        "help": "Token you obtained from app developer."
    }
]
```

{% hint style="info" %}
Note the `token` parameter that doesn't belong to the integrated API.

The `token` parameter is used by us to control the app access.
{% endhint %}
{% endtab %}
{% endtabs %}

### 4. Set up the access control flow in connection

#### **Implementation of authentication to the API**

Go to the tab with the `basic` connection and copy the code in the communication tab. Then go to the second tab with your new OAuth connection and paste the code into the `info` directive. Nothing needs to be changed in the code.

#### **Implementation of access control to our app**

Now, you need to implement the `token` directive that will call the backend for access control. The `token` directive should contain:

* **URL**: The URL of the endpoint that handles the access control. In our guide we used our [webhook](#backend-for-the-access-control-flow).
* **User's credentials parameters**: The parameters that you share with the user are passed to the endpoint handling access control. In our guide, we used the `token` parameter.
* **Error handling**: The directive that handles the error returned from the endpoint. Also, it returns the error message from the response.
* **Access control flow**: The flow that ensures the connection is created only if the user has been granted access to the app, or re-verified when the user's connection expires. The flow works with these parameters:
  * `condition` - A condition that makes sure the token directive is also executed whenever the existing connection expires. When a module with an expired connection is triggered in a scenario, the token directive is executed.
  * `response.data.expires` - A date-time parameter that says when the connection will expire. This ensures that once the connection expires, the token directive with the endpoint for checking whether the user still has a valid subscription to your app will be called, and the date of expiration extended.

After you implement the code in the communication tab, save the changes.

**Connection's communication code with comments explaining the functionality of each parameter:**

{% tabs %}
{% tab title="Source" %}

```json
{
  // Token directive is used for access control flow.
  "token": {
    // The condition ensures that the token directive is not only executed when
    // connection is being created, but also when the connection is going to
    // expire in 1 minute.
    // The call in the token directive is executed when a module with expired
    // connection is triggered.
    "condition": "{{if(data.expires, data.expires < addMinutes(now, 1), true)}}",
    // URL to the webhook in the scenario handling access control backend.
    // Passing the user's token to the webhook.
    "url": "https://hook.eu1.make.com/webhookID?token={{parameters.token}}",
    "response": {
      "error": {
        // Mapping the error message from the webhook's response.
        "message": "[{{statusCode}}]: {{body.error}}"
      },
      "data": {
        // Mapping the date-time of expiration from the webhook's response.
        "expires": "{{body.expires}}"
      }
    }
  },
  // Info directive is used for validation of the user's credentials in the API service.
  // Nothing needs to be changed in the original code.
  "info": {
    "url": "https://api.example.cz/v2/whoami",
    "headers": {
      "authorization": "Basic {{base64(parameters.username + ':' + parameters.password)}}"
    },
    "response": {
      "valid": {
        "condition": "{{body.status != 'error'}}"
      },
      "error": {
        "200": {
          "message": "[{{body.status}}]: {{ifempty(body.message.items, body.message)}}"
        },
        "message": "[{{statusCode}}]: {{body.reason || body.message}}"
      },
      "metadata": {
        "type": "text",
        "value": "{{body.username}}"
      }
    }
  }
}
```

{% hint style="info" %}
Note that we don't use `sanitization` so the connection logs will not be available. The webhook's URL will not be exposed.
{% endhint %}
{% endtab %}
{% endtabs %}

### 5. Connect the new OAuth connection to a module

To test the right functionality of the OAuth connection, you need to connect it to an existing module. Go to a module and remove the current basic connection, then connect the new oauth connection.

{% tabs %}
{% tab title="1st step" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-608f6eb42da206c683e53e88137f17ba96b432fc%2Fremove_connection.png?alt=media" alt="" width="563"><figcaption><p>Remove the basic connection</p></figcaption></figure></div>
{% endtab %}

{% tab title="2nd step" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f9113e1bb27611cf5e23731968fdec2fa3b5e5d3%2FremapNewconnection.png?alt=media" alt="" width="563"><figcaption><p>Map an OAuth connection as the primary connection</p></figcaption></figure></div>
{% endtab %}

{% tab title="3rd step (optional)" %}
If you need to test or compare the functionality of the basic connection, you can map it as the alternative connection.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8e0b26a8571ce8457724783fae0004ed0bd8eec8%2Ftest_connection.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

### 6. Test the correct functionality of access control in the app

Since the new OAuth connection is created and connected to a module, you can test its correct functionality and adjust it if needed. The test cases in our example are described below.

{% hint style="info" %}
To ensure the proper evaluation of access control functionality within your application, you will need to periodically modify the value in the `VALID UNTIL` column in the table of users multiple times.

For example, now is `22.9.2023 15:43:00`and you need to verify, that the verification process will work correctly, therefore, you can set the date `22.9.2023 15:45:59` so that you have enough time to create a connection and then run the module after the expiration.
{% endhint %}

#### Testing the creation of a connection

{% tabs %}
{% tab title="Invalid token" %}

* **Test case**: An invalid token has been provided.
* **Expected result**: A connection is not created due to an error from the access control endpoint.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d7a5588abcb95ffa50394cefab7b699dd2a94efc%2Finvalid_token.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the error message that was returned from the access control endpoint.
{% endhint %}
{% endtab %}

{% tab title="Expired token" %}

* **Test case**: A valid token has been provided but the access has expired.
* **Expected result**: A connection is not created due to an error from access control endpoint.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d3d07a5e2f3e54a71ff52b114ea72491036c3ce1%2Fexpired_token.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the error message that was returned from the access control endpoint.
{% endhint %}
{% endtab %}

{% tab title="Wrong credentials to API service" %}

* **Test case**: A valid token has been provided but credentials to the API service are incorrect.
* **Expected result**: A connection is not created due to an error from the API service.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-72e2a27d884d76ac6489702203066a04ff486454%2Fwrong_credentials.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note the error message that was returned from the API service.
{% endhint %}
{% endtab %}
{% endtabs %}

#### Testing the expiration of the connection during the app's use

The goal of access control is to be able to manage the expiration of the access to the app.

Below, you can see how it behaves when the connection expires and the access to the app hasn't been prolonged. The user is not able to use the module until they pay for their subscription.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2e76a52ee0840204a9f9b83730fca41321b2c753%2Ftesting_expiration.png?alt=media" alt="" width="332"><figcaption></figcaption></figure></div>

### 7. Switch the connection from basic to OAuth in all modules, webhooks, RPCs

If you already have created modules, webhooks, and/or RPCs, once you confirm that your OAuth connection with access control works as expected, you need to switch the connection from the original one (basic) to the new one (OAuth) in all modules, webhooks and RPCs.

If you just created the app and made the connection work, just connect the new (OAuth) connection to the new module/webhook/RPC whenever you create it.

{% hint style="info" %}
If your app is still [private](https://developers.make.com/custom-apps-documentation/create-your-first-app/app-visibility#private-app), you can delete the old (basic) connection.

If your app is already [public](https://developers.make.com/custom-apps-documentation/create-your-first-app/app-visibility#public-app), it is recommended to rename the old connection (basic) so it is obvious it should not be used anymore.

Example of a new connection label: `[DO NOT USE] Make`
{% endhint %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f609c80f83e1bc62463099f4e468beef33150c55%2Fswitch_connections.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
