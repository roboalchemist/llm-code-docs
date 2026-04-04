# pre-request-scripts

Write pre-request scripts to add dynamic behavior in Postman
===========================================================

You can use pre-request scripts in Postman to run JavaScript before a request runs. By including code in the **Pre-request** tab for a request, collection, or folder, you can carry out pre-processing such as setting variable values, parameters, headers, and body data. You can also use pre-request scripts to debug code, for example, by logging output to the Postman Console.

## Pre-request scripting example

The following is an example of using pre-request scripts:

* You have a series of requests in a collection and are running them in a sequence, such as when using the [Collection Runner](/docs/collections/running-collections/intro-to-collection-runs/).
* The second request is dependent on a value returned from the first request.
* The value needs to be processed before you pass it to the second request.
* The first request sets the data value from a response field to a variable in its post-response script.
* The second request retrieves the value and processes it in its pre-request script, then sets the processed value to a variable. This variable is then referenced in the second request, for example, in its parameters.

## Scripting before your request runs

To include code you want to run before Postman sends a request, do the following:

1. Click **Collections** in the sidebar.
2. Open the request, then select the **Scripts** tab.
3. Click the **Pre-request** tab.
4. Enter the JavaScript you need to process before the request runs, then click **Save**.
5. Click **Send** to send the request. The code runs before Postman sends the request to the API.

    ![Pre-Request Code](https://assets.postman.com/postman-docs/v11/pre-request-script-v11-12.jpg)

To make your code more readable, click **Beautify** in the lower right of the code editor.

## Add documentation to pre-request scripts

Postman supports JSDoc for documenting JavaScript functions in your pre-request scripts. Documentation added to your functions using JSDoc display in a popup window when you call your functions. You can use the official [JSDoc documentation](https://jsdoc.app/) to learn how to add documentation to your pre-request scripts.

The following example has documentation for the `logger` function using JSDoc. The documentation explains what the function does, and defines what the `data` parameter is used for and that it accepts a string data type.

```js
/**
 * This function prints a string to the Postman Console.
 * @param {string} data - The text to print to the Postman Console.
 */
function logger (data) {
    console.log(`Logging information to the console, ${data}`)
}
```

## Reuse pre-request scripts

You can add pre-request scripts to entire collections and folders within collections. In both cases, your pre-request script will run before every request in the collection or direct child request in the folder. This enables you to define commonly used pre-processing or debugging steps you need to run for multiple requests.

* You can define a pre-request script when you first create a collection or folder, or at any time after that. You can also [store pre-request scripts in the Postman Package Library](/docs/tests-and-scripts/write-scripts/packages/package-library/). This lets you maintain commonly used scripts in a single location, share them with your team, and reuse them in your internal workspaces.

To add pre-request scripts to a collection or folder, do the following:

1. Click **Collections** in the sidebar.
2. Select a collection or folder.
3. Click the **Scripts** tab.
4. Click the **Pre-request** tab. Enter code that will run before every request in the collection or direct child request in the folder.
5. Click **Save**.

## Next steps

After learning the basics of writing pre-request scripts, you can extend your scripts:

* To learn more about how to use the `pm` object, visit the [Postman JavaScript reference](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/overview/).
* For more information about storing and reusing commonly used scripts, learn about [the package library](/docs/tests-and-scripts/write-scripts/packages/package-library/) in Postman.

---

**Note:** The Postman Power Pass is available with Postman Enterprise plans with the Advanced Security Administration add-on. [Postman Power Pass](https://www.postman.com/pricing/) is a free, premium access to the platform that enables collaboration across the entire API development lifecycle.

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**To migrate your Enterprise team to an Organization, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

**To migrate your teams to Organizations, contact your Customer Success Manager.**

**Learn more about:**

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Postman Organizations** streamline API collaboration, reduce clutter in