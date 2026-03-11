# Source: https://developers.activecampaign.com/docs/python-create-and-test-your-first-app-using-pipedream.md

# Create Your First App using Pipedream and Python: Part 1

PART 1: Build your first CX App that communicates with a Python API

App Studio is used to build native applications and integrations for the ActiveCampaign platform. We call them CX Apps. CX is short for "Customer Experience." A CX App built with App Studio can be published privately (for internal use by your organization) or publicly in the [ActiveCampaign App Ecosystem](https://www.activecampaign.com/apps/).

In this tutorial, you will learn how to use App Studio to build an outbound CX App and test the app using [Pipedream](https://pipedream.com/). Pipedream is a powerful serverless platform for connecting systems. Pipedream can be used to prototype APIs, test integrations, host webhooks, or build production apps and integrations. *Outbound* CX Apps are used as actions in [Automations](https://help.activecampaign.com/hc/en-us/articles/218788657-What-are-automations-in-ActiveCampaign-An-overview) to send data from ActiveCampaign to other systems.

## Tutorial Overview

In this tutorial, you will learn to create the following.

1. **Create a mocked API in Pipedream using Python**. Your API will authenticate a login, return data to populate a dynamic list of options that is different for each user, and will both receive and save contact information from ActiveCampaign.
2. **Create an app in App Studio**. You will use create a JSON configuration file that describes how ActiveCampaign will interact with your API.
3. **Create an Automation to test the app**. By creating an Automation, you will see how an ActiveCampaign customer would configure your app, and you will be able to inspect the data that is sent from ActiveCampaign to the API as part of the app lifecycle.

## Prerequisites

### A free [ActiveCampaign sandbox account](https://developers.activecampaign.com/page/developer-sandbox-accounts)

### A free [Pipedream](https://pipedream.com/) account

## Create an App in App Studio

Login to your ActiveCampaign sandbox account. Click **Apps** and then **App Studio**. Click **Build a New App**.

<Image title="app-studio-build-app.png" alt={1596} align="center" border={true} src="https://files.readme.io/c666e32-app-studio-build-app.png">
  App Studio, Build a New App
</Image>

Complete the **Create New App** form using your email address and click **Submit**.

<Image title="app-studio-create-new-app-form.png" alt={1854} align="center" border={true} src="https://files.readme.io/8e66009-app-studio-create-new-app-form.png">
  Create New App form
</Image>

Click the **Home** tab. Click **Start Building**.

<Image title="app-studio-start-building.png" alt={1640} align="center" border={true} src="https://files.readme.io/048f757-app-studio-start-building.png">
  Start building
</Image>

CX Apps built with App Studio are configured in the App Configuration Editor. An app config is a [JSON document](https://en.wikipedia.org/wiki/JSON) that conforms to the App Studio [Configuration Specification](https://developers.activecampaign.com/docs/configuration-specification-v2).

<Image title="app-studio-editor.png" alt={2168} align="center" border={true} src="https://files.readme.io/15422d9-app-studio-editor.png">
  App Studio Editor
</Image>

## Create a Pipedream Workflow

In this step, you will use Pipedream to create a mock API for your CX App to connect and interact. First, create a new workflow in Pipedream. This workflow will become the API for your CX App.

<Image title="pipedream-create-new-workflow.png" alt={2264} align="center" border={true} src="https://files.readme.io/e4c0e24-pipedream-create-new-workflow.png">
  Create a new workflow in Pipedream
</Image>

Next, select the **HTTP / Webhook Requests** trigger for the workflow.

<Image title="click_http_webhook.png" alt={2470} align="center" src="https://files.readme.io/0c34559-click_http_webhook.png">
  Click HTTP / Webhook Requests trigger
</Image>

Edit the trigger to **Return a custom response from your workflow**

![](https://files.readme.io/e5b971a-return_a_custom_response.png "return_a_custom_response.png")

You now have a URL you can use for your App, but it does not do anything, yet. Click on the plus (**+**) to add a step to the workflow.

<Image title="ready_for_action.jpg" alt={2557} align="center" border={true} src="https://files.readme.io/7aebf11-ready_for_action.jpg">
  Add step
</Image>

Click on **Run custom code**.

<Image title="click_run_custom_code.jpg" alt={2552} align="center" border={true} src="https://files.readme.io/135ff82-click_run_custom_code.jpg">
  Click Run custom code
</Image>

<Image alt="Select &#x22;Python&#x22; to write Python code blocks" align="center" src="https://files.readme.io/3b73106-small-SCR-20230425-oczk.png">
  Select "Python" to write Python code blocks
</Image>

<Image
  alt="The Python Code Block should look similar to this, we'll come back to it in a bit.

"
  align="center"
  src="https://files.readme.io/0f4a249-small-SCR-20230425-odcx.png"
>
  The Python Code Block should look similar to this, we'll come back to it in a bit.
</Image>

## Create a Pipedream Data Store

### Create the Store

In this step, you will set up a Data Store in Pipedream that will be where Contacts are stored when they are sent from the CX app to your API.

<Image alt="Select &#x22;Data Stores&#x22; in the right menu" align="center" src="https://files.readme.io/26f4f5c-small-SCR-20230425-ofli.png">
  Select "Data Stores" in the right menu
</Image>

Enter the following code inside the existing `async` code block.

<Image alt="Name the Data Store &#x22;contacts&#x22;" align="center" src="https://files.readme.io/e7970e5-small-SCR-20230425-oike.png">
  Name the Data Store "contacts"
</Image>

Here is an example of how data stores can be used in Pipedream:

```python
def handler(pd: "pipedream"):
    store = pd.inputs["data_store"]
    store['darth'] = 'vader' # Storing
    name = store['darth'] # Retrieving
    print(f"The name stored is: {name}"
    # --> The data stored is: vader
```

### Connect it to your Python Code Block

Go back to your workflow and select the code block we created earlier. To connect the data store with this code block, do the following:

1. Select **CONFIGURE**
2. Select the **Data\_store**
3. Select the **contacts** data store we created.

![](https://files.readme.io/38d5387-small-SCR-20230425-onob.png)

## Finish the Python Code in Pipedream

> 👍 Don't just copy and paste the api! Use the recipe below to learn how every part works - we'll be building a lot of features on this in future tutorials.

<TutorialTile backgroundColor="#018FF4" emoji="🐍" id="644843cfaea02000d16c84db" link="https://developers.activecampaign.com/v3/recipes/create-your-first-app-part-1-python-api-code" slug="create-your-first-app-part-1-python-api-code" title="Create Your First App (Part 1:  python api code)" />

Copy and replace everything in the Pipedream workflow from the recipe above, and click **Save**.

## Deploy Your Code

Next, test the API code you just added. Click the **Test** button to validate there are no errors, and then the **Deploy** button. Copy the URL assigned to this Pipedream URL. Open another browser window or tab, paste the URL, and press **Enter**.

> 📘 Remember to "deploy" your changes
>
> Your Pipedream workflows aren't available until they are deployed.

You should see the following data returned in your browser window. This response is an example of what ActiveCampaign expects to receive when authenticating with your API.

If you are familiar with Python or other programming languages, you may be able to follow the code logic. However, it's totally okay if you don't understand all of the code. The features of the API include the following.

* The API uses Basic Authentication to validate every request. Any request that does not include a valid username and password will be rejected with a standard HTTP 401 error.
* An API request sent to `/me` will return a JSON object that includes an account ID and username.
* An API request sent to `/options` will return a JSON object that includes an array of options.
* An API request sent to `/fields` will return a JSON object with a `fields` array for the mapping step.
* JSON data sent to `/contact` will respond with a 200 http code, and will save it to our `contacts` data store.

[In the Python API we built](https://developers.activecampaign.com/v3/recipes/python-cx-app-python-api), you will see there are two hard-coded users and credentials:

| USERNAME                | PASSWORD            | NAME       | ID    |
| :---------------------- | :------------------ | :--------- | :---- |
| `johndoe@example.com`   | `johnDoePassword`   | John Doe   | 22222 |
| `lisasmith@example.com` | `lisaSmithPassword` | Lisa Smith | 33333 |

The **Username** and **Password** will become the credentials you must enter when you test your CX App in ActiveCampaign. The **ID** and **Name** are the values the `/me` API will return with a successful authentication.

## Update the App Config in App Studio

> 👍 Don't just copy and paste the CX app configuration! Use the recipe below to learn how every part works, it'll help you write your own CX apps in the future!

<TutorialTile backgroundColor="#018FF4" emoji="⚙️" id="644abd818d58b30042bc710a" link="https://developers.activecampaign.com/v3/recipes/create-your-first-app-part-1-cx-app-code" slug="create-your-first-app-part-1-cx-app-code" title="Create Your First App (Part 1: cx app code)" />

In the app config, there are two placeholders currently set to `{{your-pipedream-url}}`. Go to your Pipedream workflow and copy the URL assigned to your workflow. Replace the two placeholders in App Studio with your personal Pipedream URL.

When you have finished updating the JSON in the App Configuration Editor, click **Save** and click **Test App in Sandbox**.

<Image title="app-studio-save-and-test.png" alt={2168} align="center" border={true} src="https://files.readme.io/d1e0a49-app-studio-save-and-test.png">
  Edit, save, and test app
</Image>

When you click the **Test App in Sandbox** button, you will be directed to your CX App's connections page. The first time you do this, there will be no connections listed. Once a connection is established you can return here to view a list of active connections. You can also find usage logs for your connected CX App here.

<Image title="my-first-app.png" alt={2118} align="center" border={true} src="https://files.readme.io/c830447-my-first-app.png">
  List of existing connections and usage logs
</Image>

> 📘
>
> Any time you make a change in App Studio, click both the **Save** and the **Test app in sandbox** buttons. If you have your CX App open in another browser tab or window, refresh the page to ensure you are seeing the latest version of your app.

## Create a New Automation

So far, you have created an API in Pipedream and CX App using App Studio. The next step is to create an Automation you will use to test the CX App. Click the **Automations** link in the navigation menu and then click the **Create an Automation** button.

<Image title="create-automation.png" alt={2238} align="center" border={true} src="https://files.readme.io/41aca7b-create-automation.png">
  Create a new automation
</Image>

Click on the **Start from Scratch** option then click the **Continue** button.

<Image title="automation-start-from-scratch.png" alt={1838} align="center" border={true} src="https://files.readme.io/bb7d41a-automation-start-from-scratch.png">
  Start from Scratch
</Image>

Click **Start without a trigger**. You will manually add a Contact to the Automation when you are ready to test it.

<Image title="automation-start-without-a-trigger.png" alt={1558} align="center" border={true} src="https://files.readme.io/c8ab20c-automation-start-without-a-trigger.png">
  Start without a trigger
</Image>

Click the **+** button to add a new action to the Automation.

<Image title="automation-click-plus.png" alt={756} align="center" border={true} src="https://files.readme.io/6f37dc6-automation-click-plus.png">
  Click the + button
</Image>

Click on the **CX Apps** tab and then click on your CX App.

<Image title="automation-add-a-new-action.png" alt={1728} align="center" border={true} src="https://files.readme.io/b92a4b1-automation-add-a-new-action.png">
  Add a new CX App action using your CX App
</Image>

When your CX App is added to the Automation you will need to establish a connection. This connection will use the authentication scheme defined in the `auth` section of your CX App's config file. Enter the same **Username** and **Password** you set in the Pipedream workflow *params* section. Click the **Connect** button.

<Image alt="Enter CX App credentials" align="center" src="https://files.readme.io/1a0524f-small-SCR-20230427-obto.png">
  Enter CX App credentials
</Image>

The username and password will be sent to your Pipedream API to verify it is valid. If the username and password do not match what is stored in Pipedream, you will see an error and you may retry the login.

> 📘 Remember the credentials?
>
> | USERNAME                | PASSWORD            |
> | :---------------------- | :------------------ |
> | `johndoe@example.com`   | `johnDoePassword`   |
> | `lisasmith@example.com` | `lisaSmithPassword` |

![](https://files.readme.io/02bb5b9-small-SCR-20230426-ljse.png)

Next, you will configure your outbound workflow. In the app config, three form fields were defined.

* A drop-down list that is populated by making a call to your `/options` API endpoint.
* A multi-select list populated with a static list of options.
* A textarea field that can be personalized with contact data.

The credentials entered here will be sent to your Pipedream API when the CX App's outbound workflow is executed. These fields were defined on the `select` object for the `workflow` in the App Config file.

The **Dropdown Example** box is populated with a call to `/options`, and the **Multiselect Example** is populated from the hard-coded options already included in the app.

![](https://files.readme.io/092e6fd-small-SCR-20230426-ldfr.png)

<Image alt="Note that if you log in as lisasmith@example.com, the options in the dropdown will change to what's available for that user, because that is what is returned with the GET call to /options" align="center" src="https://files.readme.io/e35e90b-small-SCR-20230426-lekj.png">
  Note that if you log in as [lisasmith@example.com](mailto:lisasmith@example.com), the options in the dropdown will change to what's available for that user, because that is what is returned with the GET call to /options
</Image>

![](https://files.readme.io/10abb09-small-SCR-20230426-lfhr.png)

<Image alt="This is how each part of the configuration file maps directly to how it is rendered" align="center" src="https://files.readme.io/85fab4c-small-config_changes.png">
  This is how each part of the configuration file maps directly to how it is rendered
</Image>

![](https://files.readme.io/61308d6-small-SCR-20230426-lgnm.png)

Next, you will configure the mapping of ActiveCampaign fields to the outbound system. These fields were defined in the `map` object for the `workflow` in the App Config file. Mappings are optional, but this example is designed so you can see how the mappings work.

Enter a name for your automation then click the **Save** button. Then click the **Active** button before testing.

![](https://files.readme.io/75660e1-small-SCR-20230426-lotk.png)

<Image title="automation-rename-save-active.png" alt={2104} align="center" border={true} src="https://files.readme.io/e26025d-automation-rename-save-active.png">
  Name and save the automation
</Image>

## Test the Automation Using a Contact

Now that the Automation has been created and set to **Active** you can add a Contact to the Automation to test the CX App. Click on **Contacts** and then click on a Contact to go to the Contact Details page.

<Image title="contact-select-contact.png" alt={2330} align="center" border={true} src="https://files.readme.io/a071c72-contact-select-contact.png">
  Contacts page and Contact selection
</Image>

In the Details page for your Contact click the **+ Add** button next to **Automations**. Select the Automation that you just created and then click *Okay*.

<Image title="contact-add-automation.png" alt={1880} align="center" border={true} src="https://files.readme.io/316e784-contact-add-automation.png">
  Add the Contact to the Automation
</Image>

Once the Contact has been added to the Automation your workflow should have executed. Navigate back to your CX App's Connections page by clicking on **Apps** and then clicking on **Connected Apps**. In your CX App's Connections page click **View Logs**. You should see a log entry for the Contact that you added to the Automation in the last step.

<Image title="view-app-logs.png" alt={2372} align="center" border={true} src="https://files.readme.io/54151e6-view-app-logs.png">
  View logs for your CX app
</Image>

Back in Pipedream you can also view the data that was sent to your API when the outbound workflow was executed:

<Image alt="Inside your **data store &#x22;contacts&#x22;** you should see your contact saved." align="center" src="https://files.readme.io/bea1c18-small-SCR-20230426-lxge.png">
  Inside your **data store "contacts"** you should see your contact saved.
</Image>

## A Quick Review:

If you have made it this far, congratulations! You have successfully created and tested a CX App using App Studio, that talks to a Python Api! Let review what we built, and *exactly* is happening:

![](https://files.readme.io/d87a0ca-CX_APP_OVERVIEW_PT1.jpg)

## Next Steps

Feel free to make changes to your CX App configuration, such as lists and textarea, and re-run the Automation as many times as you wish. See how those changes affect the data posted to Pipedream. Explore and tweak the API code and the app config and see how that affects the CX App.

Pipedream is a powerful platform for building custom integrations. You may want to use Pipedream as the "glue" between ActiveCampaign and another system you wish to integrate. Or, continue to use Pipedream to test and mock any part of a CX App you are building whenever you need to inspect requests or data sent from ActiveCampaign.