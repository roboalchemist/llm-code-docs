# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/using-storage.md

# Use storage

You can use storage functions to store variables in a [global session](#set-and-get-global-variables) (applicable to all the users) or store variables specific to a [user session.](#set-and-get-user-variables)

{% hint style="success" %}
**Key point**: It is recommended to use storage variables for transactional data that is specific to your agent or users, such as, agent configuration parameters, user attributes. Typically, these are in smaller data sets. For large data sets such as blob and files, which have thousands or millions of data records, the recommended approach is to develop external APIs for storing and managing such data. You can then pass parameters to query the API to get only filtered data that is required for your agent. Such large data sets must not be stored in the storage variables, as it may impact performance.
{% endhint %}

### Set and get global variables

You can use [Storage.global.set](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/storage#global-session) and [Storage.global.get](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/storage#global-session) to set the value and retrieve a value in a global session respectively.

Consider that you wish to get the status of your pizza order:

* Get the order number from the user
* Send an API request to an external application (Mac Pizza Application) to get the order status. Now, consider that the API request to get the order status requires an access token from an Authentication Service such as OAuth. As the access token remains the same across all the users, you can use **Storage.global.get** and **Storage.global.set** to set the value and retrieve a value in a global session respectively.

The following is a sample JS that stores the received API Bearer token from authentication service, gets the value, and the displays on the console:

```javascript
await(Storage.global.set("BearerToken", body.access_token)); //POST request body received from Auth service
let storedvalue = Storage.global.get("BearerToken");
console.log("Bearer token is - "+storedvalue);
```

### Set and get user variables

You can use [Storage.user.set](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/storage#user-session) and [Storage.user.get](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/storage#user-session) to set the value and retrieve a value in a user session respectively.

Consider that you wish to keep a count of all the unhandled user queries in the MacPizza agent such that if there are more than 2 unhandled queries in a user session, then a customized message is displayed. You can achieve this by, creating a JS node in the main node and set a count storage variable in a user session:

```javascript
await(Storage.user.set("unhandledCount", 0));
```

In the **Unhandled** intent, create a JS node to get the unhandled count from a user session and display a customized message based on the number of unhandled counts:

```javascript
if(Number(Storage.user.get("unhandledCount")) === 1){
 Storage.user.set("unhandledCount", 0);
 return "I am sorry, I am still learning. Visit MacPizza website, for more options.";
}
else{
 await(Storage.user.set("unhandledCount", 1));
 return "I am sorry, I am still learning. Can you rephrase your request?";
}
```

The following response is displayed in the agent if there are more than 2 unhandled queries in a user session:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDjNkF35FHLP6hLLJiXZa%2Fimage.png?alt=media\&token=f26b34fd-2ab0-483b-b742-38f9b0c2745f)
