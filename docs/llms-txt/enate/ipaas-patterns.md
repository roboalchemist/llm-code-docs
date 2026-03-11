# Source: https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic/ipaas-patterns.md

# iPaaS Patterns

When using Enate with iPaaS there are four different basic ‘patterns’ that you can use. All use cases fit within one of these models.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZpQU0ns7uuWT2oUFxpAA%2Fimage.png?alt=media&#x26;token=bed0ec87-2a5b-4ad4-b410-03d26f38090b" alt=""><figcaption><p>The 4 patterns covering iPaaS use cases with Enate</p></figcaption></figure>

There are a few integration patterns to consider, and you can choose one or all based on your use cases. Enate's clients currently perform integration at their end using their own iPaaS tool. However, we are researching a new tool that Enate can offer to its clients, but the coding, maintenance and support will be the responsibility of the clients themselves.

## Pattern 1 - Enate Workflow Updates External Application

**When should I use this pattern?** - This is the most common integration pattern. Use it when in this pattern when you want to update or get data from an external system at a known point in an Enate Workflow.&#x20;

**How does it work?** Enate calls iPaaS to start a recipe that will update an external application.

1. **Trigger**: Enate workflow task calls the iPaaS API to start the recipe.
2. **iPaaS:** Upon receiving the Enate call, transform the data and send it to the external application via API call.&#x20;
3. **Receiver:** External application gets new information and data is updated / action is taken.
4. **Optional:** Enate can either wait for the iPaaS to call back confirming that the other application has completed the updates, or just move on with the process.

**Pattern 1 use cases:**

* Upon creation of a new Deal in your sales department, you want to grab data from HubSpot to help with onboarding.
* At the end of an onboarding process, you want to upload the signed employee contract to the HR system.&#x20;
* At the start of the Accounts Payable process, you want to get the relevant Purchase Order details from the ERP system into Enate.

### Walkthrough creating Pattern 1

Look at how to build your own example of this pattern using Enate, a 3rd party system, and Enate Integration Services (SnapLogic):

{% content-ref url="build-your-pipeline-enate-integration-pattern-1" %}
[build-your-pipeline-enate-integration-pattern-1](https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic/build-your-pipeline-enate-integration-pattern-1)
{% endcontent-ref %}

## Pattern 2 - Synchronize Data in Enate on External Events

**When should I use this pattern?** You should use this pattern when you want data to be updated or action taken in Enate whenever something specific happens in an external system (i.e. there is a specific event in that system).&#x20;

**How does it work? -** In this pattern, events in an external application will fire webhooks triggering the iPaaS to execute a recipe and update Enate.&#x20;

1. **Trigger:** Data is changed in an external application causing a webhook to be triggered.
2. **iPaaS:** Monitor the external application by subscribing to the webhook related to this event and call Enate API with an update when it happens.
3. **Receiver:** Enate receives new information over the API and updates the system or takes action depending on the API called by the iPaaS.

**Pattern 2 use cases:**

* A new deal is created in Salesforce, it needs to trigger a customer onboarding workflow in Enate.
* A new employee is onboarded to the HR system and they need to be set up as a User in Enate.
* A new message is received in a client web Portal and it needs to notify the Enate user processing that customer’s case.
* The list of Exception Types in SAP needs to be synchronised into Enate so that it can be shown in a Custom Card.

## Pattern 3 - Synchronize data in External Systems on Events in Enate

**When should I use this pattern?**  This is very similar to Pattern 2, but in this case you want data that is mastered in Enate to be automatically synchronised to the 3rd party system. &#x20;

**How does it work?** The flow is identical to Pattern 2 but with the systems reversed i.e. Listen to Enate webhook and update the external system.&#x20;

**Pattern 3 use cases:**

* A new email is received in Enate and it needs to be uploaded to a client portal so that it is visible online for the client.

## Pattern 4 - Transform Data within an Enate Process

**When should I use this pattern?** This makes use of some of the additional feature of iPaaS systems. Because system integration is about transforming the data from System A to fit the data in System B, iPaaS are very good at data transformation. You can make use of this feature by sending data form Enate up to the iPaaS system and using a pattern to transform the data.&#x20;

**How does it work?** In this pattern, Enate data is transformed into a new format but does not necessarily need to connect to a third-party system.&#x20;

1. **Trigger:** Enate workflow task calls the iPaaS API to start the pattern.
2. **iPaaS:** on Enate call, transform the data and send it back via update API.
3. **Receiver:** Enate gets new information and updates it.&#x20;

**Pattern 4 use cases:**

* A spreadsheet received form a client containing new payroll data needs to be transformed so that it can be automatically uploaded to a Payroll system.
