# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-js-files.md

# JS files

You can create and add JavaScript files to the agent from the **Configuration -> Add JS files** option. This feature is used to enhance the functionality of the agent. **Example**: Consider an "Order Status Pizza" skill for checking the status of a pizza order. You can take the order number from the user and get the order status via an API request to an external application (Mac Pizza Application). You can create and add a JS file, say, "orderStatus.js" to perform this functionality. See [REST API](https://docs.avaamo.com/user-guide/build-skills/create-skill/customize-your-skill/how-to/integrate-with-api-1/rest-and-soap-api#rest-api), for an example.

The following lists a few advantages of using JS files:

* **Easy Maintenance and Troubleshooting**: You can create JS files such that each file performs one specific task. It helps in easy maintenance and troubleshooting of errors in JS files. See [JS errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#js-errors), for more information.&#x20;
* **Easy Identification**: Modularizing the JS files also helps to identify and select the right JS files during publishing skills to the Skills store. See [Publish skill to skills store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information.&#x20;
* **Reusability**: The JS files added to the agent are available across all the skills in the agent. Hence, if you have certain functionalities that are common across all the skills, you can add JS with common functions at the agent level and use it across all the skills. **Example**: You can have a common function to authenticate a user in a JS file and re-use that function in other JS files, as required.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add JS files immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  {% endhint %}

### **Create JS file**

* In the **Configuration -> JS files** tab, click **Add new**.&#x20;
* Specify the name of the JS file and click **Create**.&#x20;
* A new empty JS file is created. In the **Scripts** page, add the code in the JS file as required.
  * See [Using Script and Code](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill), for an exhaustive list of functionality that can be achieved using JS.
  * Use `CTRL+ENTER` key to toggle between fullscreen mode. You can view the complete list of built-in functions with syntax and examples in the Built-in functions window available in the JS editor. See [Built-in functions window](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/built-in-functions-window), for more information.

```javascript
let greetingHandler = {
    getTimeOfDay: () => {
      var g = null;
      let m = moment();

      var split_afternoon = 12; //24hr time to split the afternoon
      var split_evening = 17; //24hr time to split the evening
      var currentHour = parseFloat(m.format("HH"));
    let zone_offset = await(context.user.getDevice()).zone_offset;
    currentHour += zone_offset;

      if(currentHour >= split_afternoon && currentHour <= split_evening) {
          g = "afternoon";
      } else if(currentHour >= split_evening) {
          g = "evening";
      } else {
          g = "morning";
      }

    return g;
  }
}

```

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0O7Mt26ufeeRj_3882%2Fhowto-js-greeting.png?alt=media\&token=292722dd-2984-4727-83f1-57e2c993f0db)

* Click **Save.**

### Edit JS file

* In the **Configuration -> JS files** tab, click the JS file that you wish to edit.
* Click **Edit** to unlock the JS file and edit the JS file.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FggFkWeG8IOH9iMn1Ngjh%2F6.3-edit-js-file.png?alt=media&#x26;token=e17490f4-79ab-416c-807b-b4bd7e74364c" alt=""><figcaption></figcaption></figure>

* If there is another user already editing the JS file, then the name of the user editing the JS file is displayed. Click **Force unlock**, if you still wish to edit the JS file. Note that when you force unlock a JS file, the changes made by the other user are lost. Hence, this option must be used with caution.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3ds6vc3UaJTwpU1PQdsm%2F6.3-JSFiles-Edit.png?alt=media&#x26;token=1716053f-83d6-44c8-8270-4ffa0eb8f461" alt=""><figcaption></figcaption></figure>

* You can also click the edit icon next to the JS file to edit the name of the JS file.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0O87l143Ev_Kf2JaUt%2Fhowto-js-edit-file.png?alt=media\&token=026fd151-f586-48bb-9182-d4b6331dc31b)

* Click **Save** to save the JS file.

### Delete JS file

* In the **Configuration -> JS files** tab, click the overflow menu icon for the JS file you wish to delete.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0O7jhqRM0-s1fTK_OQ%2Fhowto-js-edit.png?alt=media\&token=6c24e23c-1243-417d-818b-a6cac5130b48)

* Click **Delete.** If there is another user already editing the JS file, then the same message is displayed to the user. Click **Force delete** to delete the JS file.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fr4JELrqgesm7lstxlTc7%2F6.3-force-delete-js-file.png?alt=media&#x26;token=1b011aef-e77a-4cfd-a58f-9d5c6b01ea62" alt=""><figcaption></figcaption></figure>

### Open in a new tab

* In the **Configuration -> JS files** tab, click the overflow menu icon for the JS file you wish to open in a new tab.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0O7jhqRM0-s1fTK_OQ%2Fhowto-js-edit.png?alt=media\&token=6c24e23c-1243-417d-818b-a6cac5130b48)

* Click **Open in New tab.** The JS file is opened in a new browser tab.
* If there is another user already editing the JS file, then the name of the user editing the JS file is displayed. Click **Force unlock**, if you still wish to edit the JS file. Note that when you force unlock a JS file, the changes made by the other user are lost. Hence, this option must be used with caution.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F1WrkXUEZ7eh5pIMVfMjo%2F6.3-open-new-tab-js-file.png?alt=media&#x26;token=965c0cba-0de5-41af-9161-75fa20c2c2f8" alt=""><figcaption></figcaption></figure>

### Best practices

The following lists a few best practices that you can follow when using JS file functionality:

* As skills perform well-defined tasks, it is also recommended to modularize your JS code accordingly, by creating separate JS files for each task.
* Do not place all the common code functionality into one common JS. Instead, logically break and modularize code into different JS files. This helps in easy maintenance. It also helps in debugging and troubleshooting the issues in JS files. See [JS errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#js-errors), for more information.&#x20;
* Name the JS file in a way that helps you to identify if the JS file is used in a specific skill or for a specific task. This also helps to identify and select the right JS files during publishing skills to the skill store. See [Publish skill to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information.&#x20;

  **Examples**:&#x20;

  * greetingHandler.js -  JS file for displaying a greeting message to the user based on the time of the day. &#x20;
  * orderStatus.js - JS file for getting the status of the pizza order using the order number.
* Use namespaces in your JS file. This helps to avoid conflicts if you are using the same variable names and functions in multiple JS files. **Example**: Use "let" to define the variable scope:&#x20;

```javascript
let greetingHandler = {
    getTimeOfDay: () => {...
    ...
    }
}
```

In the code, you can call **getTimeofDay** as follows:

```javascript
return `Good ${greetingHandler.getTimeOfDay()}, 
Welcome to MacPizza. How can I help you today?`;
```

See [Best practices](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/best-practices), for general guidelines on programming.

### Example

In the MacPizza agent, consider that the following JS files and methods are added:

* `greetingHandler.getTimeofDay()` -  Used in the greeting message to display greetings according to the time of the day.
* `orderStatus.getstatus(<<orderNumber>>)` - Check the status of the pizza order using the order number.

**Example 1**: In the Greetings skill, you can call greetings.getTimeofDay() method as follows:

```javascript
return `Good ${greetingHandler.getTimeOfDay()}, 
Welcome to MacPizza. How can I help you today?`;
```

Test the agent to view the response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEotALF2Fxptwy8HiLAoi%2Fimage.png?alt=media\&token=9efc301c-0eec-4a1d-8a16-c8930fdaf5d4)

**Example 2**: In the Order Status skill, you can call the `orderStatus.getstatus(<<orderNumber>>)` the method in a JS response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0OCd0jg_wpg5nGYgTZ%2Fhowto-js-order-status.png?alt=media\&token=280e0587-6831-4472-9d1c-d24bf23094d1)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0O5bh_JKBwU2Z_9VL2%2F-M0ODfP2wTx8kI2wVgce%2Fhowto-js-order-status-js.png?alt=media\&token=2c00eb00-ea04-4c0a-91ad-3c50d2b25b33)

Note that here, the JS file and functions are defined at the agent level and all the methods are available at the skill level.

* Test the agent to view the response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FrmfJQO8Ujh2J83OJ1khQ%2Fimage.png?alt=media\&token=b8dec46f-25f9-4c66-b105-a337ae349c20)
