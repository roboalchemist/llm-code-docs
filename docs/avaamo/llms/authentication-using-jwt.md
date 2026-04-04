# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/authentication-using-jwt.md

# Authorization using JWT

Consider that you have agents deployed to a web channel that can be accessed only via authentication. In such cases, customers can generate a JWT token and pass the user information to the agent at the time the agent is initialized to authorize the users using the following steps:

* [Generate JWT token](#generate-jwt-token)
* [Embed JWT token in the web URL](#embed-jwt-token-in-the-web-url)

Later, in the Platform, you can access the user information using a context object. See [Accessing user information](#accessing-user-information).

## **Enable custom user authentication**

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the **Channels** page, click **View** in Web Channel.&#x20;
* In the **Security** section, check **Use custom user authentication** and click **Save**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbAYUxFomRUcyOx_Vnm%2F-MbAZubOzXQq1Vhg3n0G%2F5.7-web-channel-security.png?alt=media\&token=d3d4a385-9c4c-43a4-ad92-02f3a825fe67)

* Click **Save** to save the changes to the agent.

## **Generate JWT token**

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the **Channels** page, click **View** in the Web Channe&#x6C;**.**
* In the **Security** section, click the **Copy** icon at the end of the **JWT secret key** textbox to copy the key. You must use the HS256 algorithm with the secret key to encode the user information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbA_0UhvjsUDQ_NenR5%2F-MbA_TwOkAipemp5oMNl%2F5.7-web-channel-security-jwt-copy.png?alt=media\&token=bfa3950d-f3ed-4244-b016-3a1b51039ae0)

* The **JWT** is generated for passing a unique user identifier, first name, last name, email/phone (if available), and other optional user information that the agent can use to enhance its interaction with the user. See [JWT](https://jwt.io/), for more information on how to encode user payload with the secret key using the HS256 algorithm:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0HLEca8I4Q7vB-FHBu%2F-M0HQzM6cHcpDJY7HBWI%2Fweb-channel-jwt.png?alt=media\&token=f1b7e076-be70-4c96-946e-7921b6967d5f)

{% hint style="info" %}
**Note:** JWT is used for **signature verification only**. It is recommended **not to include sensitive information or PII** such as access tokens or phone numbers within the token payload.
{% endhint %}

**Example 1**: The following is a sample user payload with some basic user details such as email, and phone, all of which are single string values :

```javascript
{
 "uuid": "<unique user id>",
 "email": "john.doe@avaamo.com",
 "phone": "+1234567890",
 "first_name": "John",
 "last_name": "Doe",
 "iat": 1516239022,
 "exp": 1519339022
}
```

**Example 2**: The following is a sample user payload with some basic user details such as email, and all are single string values and an additional country property with an array of values:

```json
{
 "uuid": "<unique user id>",
 "email": "john.doe@avaamo.com",
 "phone": "+1234567890",
 "first_name": "John",
 "last_name": "Doe",
 "iat": 1516239022,
 "country": ["India","Australia"];
 "exp": 1519339022
}
```

{% hint style="success" %}
**Key Points**: Ensure that *uuid* is used in the payload. This is used to maintain a single identity across the channel and multichannel sync.
{% endhint %}

## Embed JWT token in the web URL

The generated JWT token must be embedded in the **user\_info** parameter of the channel URL:

```
https://cx.avaamo.com/web_channels/a1d80b67-1260-4685-8ef4-82b8915a61bb?
theme=avm-blue&user_info=<JWT>

where, <JWT> is a JSON Web Token generated at the server side and 
embedded into the script at the time of webpage HTML generation
```

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the **Channels** page, click **View** in the Web Channel and **Test**.&#x20;
* A sample script is generated that is used to deploy the agent to a web-page:

```markup
<!DOCTYPE html>
<html>
<head>
  <title>Web Channel</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
</head>
<body>
  
  <script type="text/javascript">
    var AvaamoChatBot=function(t){function o(t,o){var n=document.createElement("script");n.setAttribute("src",t),n.onload=o,document.body.appendChild(n)}return this.options=t||{},this.load=function(t){o(this.options.url,function(){window.Avaamo.addFrame(),t&&"function"==typeof(t)&&t(window.Avaamo)})},this};
    var chatBox = new AvaamoChatBot({url: 
    'https://cx.avaamo.com/web_channels/c7f7274b-c933-79a7?theme=avm-messenger'});
    chatBox.load();
  </script>
</body>
</html>
```

* The user information can be passed to this script by adding the URL parameter **user\_info** to the embedded URL:

```markup
https://cx.avaamo.com/web_channels/c7f7274b-c933-79a7?
theme=avm-messenger&user_info=<JWT>

where <JWT> is a JSON Web Token generated at the server side 
and embedded into the script at the time of webpage HTML generation.
```

## Accessing user information

The information passed via the JWT can be accessed in the agent using the **context.user** object. You can use the following code to access the uuid (unique id) assigned to the user:

```javascript
if(context.user.custom_properties){
  return `User Employee ID is ${context.user.custom_properties.employee_id}, User Department is ${context.user.custom_properties.department}`;
} else {
  return "No user details found.";
};
```

{% hint style="success" %}
**Key Point:** The uuid property is not accessible inside the agent in JavaScript. ${context.user.custom\_properties.uuid} does not return any value. You must pass another property containing the same value if you need to access it in JavaScript.
{% endhint %}
