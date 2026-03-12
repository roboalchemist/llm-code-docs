# Source: https://docs.tray.ai/platform/introduction/getting-started/quickstart

Title: Quickstart - Getting Started - Tray.ai Documentation

URL Source: https://docs.tray.ai/platform/introduction/getting-started/quickstart

Markdown Content:
Getting Started

Get started with a walkthrough of key Tray building principles

### [](https://docs.tray.ai/platform/introduction/getting-started/quickstart#the-basics-of-tray)
The basics of Tray

Essentially, building automations in Tray is about doing three things:

*   **Getting data** from one service
*   **Doing something** with that data
*   **Sending that data** to another service When you start building Tray workflows, you need to then ask yourself the following questions:
*   **How do I get data** from the first service?
*   **What do I do with the data**?
*   **How do I send it** to the second service? When using Tray, the[Trigger](https://docs.tray.ai/connectors/browse/trigger)that you choose for your workflow will be dictated by**how**you get your data. Two of the most common scenarios are:
*   A workflow triggered by an event happening in a 3rd party service (using a pre-built Tray service trigger, or the Tray [webhook trigger](https://docs.tray.ai/connectors/trigger/webhook-trigger) if no dedicated service trigger exists)
*   A [scheduled trigger](https://docs.tray.ai/connectors/trigger/scheduled-trigger) workflow where you periodically query the 3rd party service for new updated records (known as polling) This Quickstart will take you through a service trigger-based scenario and introduce you to basic data processing principles. The key thing that it will introduce you to is how to think about dealing with the data that comes into your workflows. It will also introduce you to some key concepts in Tray usage:
*   [Project config](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/config-variables)
*   [Conditional logic](https://docs.tray.ai/platform/automation-integration/building-workflows/branching-looping/conditional-logic)
*   [Callable workflows](https://docs.tray.ai/platform/automation-integration/building-workflows/composable-workflows/calling-other-workflows)
*   [Data mapping](https://docs.tray.ai/connectors/core/data-mapper)
*   [Transforming data for input](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/input-schema)
*   [Error handling](https://docs.tray.ai/platform/automation-integration/building-workflows/error-handling/what-is-an-error)
*   [Environment variables](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/environment-variables)

### Quickstart template overview

The use case that we are dealing with in this quickstart is processing survey results from Typeform: ![Image 1: typeform-survey-ui](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1cRX065DzgjeOEW63qP7WK_typeform-survey-ui.png) Ultimately we want to process each survey response to a Google Sheet: ![Image 2: sheets-typeform-survey-responses](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/MdWDzX2moWuzR8spCyZJS_sheets-typeform-survey-responses.png) And notify a company Slack channel that a response has been processed: ![Image 3: typeform-slack-notification](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/77I2WpdeIiXeKbasi8bHuh_typeform-slack-notification.png)

Please install and run the[Add Typeform survey responses to Google Sheets](https://tray.io/documentation/templates/getting-started/add-typeform-survey-responses-to-google-sheets/)template associated with this project. It only takes 10 minutes to set up a free Typeform account and start filling in test survey responses to test it out. The template instruction page will take you through installing, configuring and testing the template. This guide will then take you through the key points in how it was built

### Working with data payloads​

Every service operation or trigger that you work with will have its own payload structure that you will have to work with every time you receive or fetch data from it. So this quickstart will introduce you to the general principles of working with payloads that can then be applied any time you are working with Tray. With Typeform survey responses we are dealing with payloads 300+ lines long: ![Image 4: typeform-trigger-payload](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1nxFTZB82hdACKnS0meQ3A_typeform-trigger-payload.png) On inspection we find that key sections are:

*   The`form_response.definition.fields`array which includes:
    *   The `title`of each question
    *   The `type`of each question (dropdown, multiple choice, boolean etc.)

*   The`form_response.answers`array which includes:
    *   The `choice`the responder made for each question The template is set up to automatically extract the key information from these sections, using the principles outlined in[Mapping data between steps](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/mapping-data-between-steps).

This workflow is not included in the template.It is only being shown here for introduction purposes.

The most simple implementation of this use case (minus the Slack notification) is a single workflow which makes use of Tray's pre-built Typeform trigger. Once you have authenticated your Typeform trigger you will be able to choose which of the forms in your account you wish to trigger the workflow: ![Image 5: quickstart-typeform-trigger](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/7gXsHmyJDyb3B7ypRcSasL_quickstart-typeform-trigger.png) Then we can make use of the methods outlined in[Mapping data between steps](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/mapping-data-between-steps)to use the following jsonpaths to get at the answers from the payload returned by the trigger:

*   `$.steps.trigger.form_response.answers[0].choice.label`
*   `$.steps.trigger.form_response.answers[1].choice.label`
*   `$.steps.trigger.form_response.answers[2].choice.label`
*   `$.steps.trigger.form_response.answers[3].choice.label` Note that the exact trigger payload and the jsonpaths will depend on the service. Thus the payload and jsonpaths here are specific to Typeform. Please see[Mapping data between steps](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/mapping-data-between-steps)for more guidance. ![Image 6: typeform-sheets-simple](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1cra6pvv6Aov8jj3kk7RzO_typeform-sheets-simple.png)

### Overview

The template itself has 2 processing workflows:

*   **A 'static' workflow** whereby it only deals with a fixed Typeform survey with 'string'-type answers and a fixed Google Sheet which already has its headers set up
*   **A 'dynamic' workflow** whereby it will deal with any Typeform survey and create the headers for an empty Google Sheet

### Project config

Looking at the project config you will see that we have a`processing_method`variable which allows you to switch between static and dynamic processing. For Typeform, Google Sheets and Slack, there are also variables for`form_id`,`spreadsheet_id`,`worksheet_name`and`slack_channel`as a best practice for single-sourcing variables that are used repeatedly in a project: ![Image 7: quickstart-project-config](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/4JG39VaeJtwNLlX8fzosEU_quickstart-project-config.png)

### The Typeform trigger workflow

In the first 'Typeform trigger' workflow you will notice that a Branch connector is used. The branch uses the`processing_method`config variable to decide which branch to go down, and whether to call the static or dynamic workflow: ![Image 8: quickstart-typeform-trigger-workflow](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/ZTZXAlMBYn34jtHxs2CDb_quickstart-typeform-trigger-workflow.png) Then each branch calls the appropriate workflow and sends the trigger payload as 'Data': ![Image 9: quickstart-typeform-call-static-workflow](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/5TRmAnHE6UW2JOGgfVbu5A_quickstart-typeform-call-static-workflow.png)

### The static processing workflow

You will remember that this workflow is called 'static' as it only deals with a fixed Typeform survey and adds them to a Google Sheet which already has all the headers added. However it does introduce you to some other Tray concepts: **1. Data mapping** We have decided that, for the purposes of our records it is more useful to have customers identified as:

![Image 10: quickstart-send-error-message-to-slack](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1FLqEJvzZ2pYqRBfT3lsNH_quickstart-send-error-message-to-slack.png) In that message we are making use of the following[environment variables](https://docs.tray.ai/platform/automation-integration/building-workflows/mapping-data/environment-variables):

*   `{$.env.workflow_uuid}`to compose the url of the workflow
*   `{$.env.execution_log_url}`to link directly to the logs for the failed execution It also makes use of the`{$.config.spreadsheet_id}`project config in order to construct the url for the Google Sheet. The end result is a message such as: ![Image 11: quickstart-error-message-slack-example](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1UEwzme3XDMhmiEOtAeI28_quickstart-error-message-slack-example.png)

### The dynamic processing workflow

**Check if the sheet has been started** The first thing we do in the dynamic processing workflow is check if the worksheet has already been started. This is done by using the Google Sheets 'get sheet data' operation and then using the Boolean connector 'property exists?' operation to see if any 'values' were returned: ![Image 12: quickstart-dynamic-property-exists](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/57AwO9pVT90oLUvkhDrDtX_quickstart-dynamic-property-exists.png) If no values have been returned this tells us that the sheet is empty. **2. Creating the sheet headers** So on the 'false' branch we use the List Helpers 'pluck' operation to get all the answers using the`$.steps.trigger.form_response.definition.fields`jsonpath and plucking each 'title': ![Image 13: typeform-pluck-questions](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/7BjEzdVjUlm3dTKxW4lbwg_typeform-pluck-questions.png) We can use the[Tray Operations Explorer dev tool](https://developer.tray.io/developer-portal/dev-tools/ops-explorer/ops-explorer-tool/)to investigate the input schema requirements for the Google Sheets 'Create column headers for sheet' operation: ![Image 14: ops-explorer-create-sheet-headers](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/1FZ4Z2Y1Xy6BczIBNuNVZI_ops-explorer-create-sheet-headers.png) So we know that we can just pass a basic array into 'Row data' and the headers will be added: ![Image 15: typeform-question-headers-to-sheets](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/5hCvTqzGb22fVmTIfBxPcV_typeform-question-headers-to-sheets.png)**3. Getting the answers** In order to respond dynamically to the answers given in a response to any survey, we need to allow for the fact that answers in the payload coming from Typeform could be in a number of formats: number, boolean, string etc. So we use a javascript connector step to write a switch statement to deal with each type and create a final array of answers: ![Image 16: typeform-answers-switch-statement](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/4eyPpxwKDAFBnkMe4TE6I_typeform-answers-switch-statement.png) 4. **Adding the answers to Google Sheets** In order to dynamically add answers we must send them as a dynamically generated array, since we don't know how many there are. A key point here is that any connector operation which allows you to add multiple records will have a particular input schema. To find this out we can do a manual test run of the Google Sheets 'create row' operation and inspect the input logs in the Tray UI: ![Image 17: sheets-test-data-input-schema](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/4kWDcNtGqqz1MBIy9n3YxJ_sheets-test-data-input-schema.png) (Note that you could also make use of our[Tray Operations Explorer dev tool (beta)](https://developer.tray.io/developer-portal/dev-tools/ops-explorer/ops-explorer-tool/)) to create a dummy input payload and find out the required schema) This tells us that we must transform our simple array of answers:

Into an array of 'column_heading' / 'value' pairs. In the 'Construct GSheet input array' step this is done using a simple for loop: ![Image 18: script-transform-sheets-input-array](https://docs.tray.ai/images/platform/introduction/getting-started/quickstart/38DtjRp9TRqM4lNitxEpOG_script-transform-sheets-input-array.png) When building your own workflows this is a script you could write yourself, or you could make use of our[Data transformer tool (beta)](https://developer.tray.io/developer-portal/dev-tools/data-transformer/introduction/)to generate the script for you! The result of this script step can then be passed directly into the 'Row data' for the Google Sheets 'create row' operation.
