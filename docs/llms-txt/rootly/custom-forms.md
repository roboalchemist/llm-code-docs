# Source: https://docs.rootly.com/configuration/custom-forms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Forms

> Build tailored forms with specific field combinations to collect targeted incident data at different stages of the response lifecycle.

Throughout the lifecycle of an incident, teams might want to prompt responders to input various incident properties outside of the [standard built-in forms](/configuration/built-in-forms). Custom forms enable teams to define their own forms that can be triggered either through a custom Slack command or a button within a custom Slack block.

You can access the custom forms by navigating to **Configurations >** [**Forms**](https://rootly.com/account/forms) and scrolling to the bottom of the page.

# **Example Use Cases**

* **Targeted Data Collection**: Create a form specifically for the Comms Lead, which only displays fields that are important to the leadership (e.g. `status`, `summary`, `severity`). This streamlines the communication process by helping teams only focus on the relevant information.
* **Guided Response:** Create various forms that collect specific sets of data at specific points of the incident life cycle. Dynamically display each custom form to guide responders through their response effort.

# **Create Custom Form**

Click on the `Create Form` button to initiate the form creation wizard.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-20at13.43.26@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=487afe5b204439fdcf911c619f260b22" alt="Clean Shot2025 08 20at13 43 26@2x Pn" width="3456" height="1978" data-path="images/CleanShot2025-08-20at13.43.26@2x.png" />

A dialogue will appear requesting the following fields:

<AccordionGroup>
  <Accordion title="Name">
    Assign the custom form a name.
  </Accordion>

  <Accordion title="Command">
    Define a Slack command that would prompt to open the form in Slack.

    <Note>
      The full command you would enter in Slack is `/rootly customform your-custom-slack-command`. You only need to enter the `your-custom-slack-command` portion in this field.
    </Note>
  </Accordion>

  <Accordion title="Description">
    You can provide an optional description for your custom form.

    After providing the necessary details, click on `Save`. You’ll be redirected to the following page where you can begin customizing the new form.
  </Accordion>
</AccordionGroup>

# **Edit Custom Form**

To begin editing a form, select the Configure button under the form you'd like to edit.

You'll be navigated to the edit form page of the selected form. The **left side of the page is the edit pane** where you can edit what fields are displayed and how they are displayed. The **right side of the page is the preview** of the form.

<Tip>
  You can create separate versions of the form for Slack and Rootly Web/Mobile by toggling between the tabs on the left hand side. To ensure incident data is captured consistently, we recommend keeping the fields for each channel in sync.
</Tip>

## Adding fields to a form

Add new fields to your form by selecting the **Add Fields** button. Select all of the fields you'd like to add to the form, then **Add Fields**.

Once these fields are added to your form, you can drag and drop them to reorder the form. Remove a field by selecting the **minus** button on the right hand side of the field.

## Editing fields on a form

Once a field is added to a form, you can control when the field is displayed and if it is required. Select the edit button on the field that you want to make changes to.

If you only want the field to display under certain conditions or be required under certain conditions, select the **Conditionally** option under **Display this field **or**Require this field** .

Form fields can be displayed or required conditionally depending on the value of any field set above the field that you're editing. For example, if the first field on your form called "Teams" is set to a certain value, your second field can be conditionally displayed depending on the team's value.

# Preview

The preview on the right-hand side is interactive and generated in real-time. This is a great way to test out the user experience of your form, and ensure behavior of each field is correct.

# Trigger Custom Form

Custom forms can be triggered in various ways: Slack command, custom Slack block, or web UI.

## Prompt Form via Slack Command

A custom form can be prompted in an incident Slack channel via manual command. The command can be found on the edit screen of the specific form.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-20at13.45.48@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=7451788ea9ec531858820c4efc6c5ede" alt="Clean Shot2025 08 20at13 45 48@2x Pn" width="3080" height="1988" data-path="images/CleanShot2025-08-20at13.45.48@2x.png" />

When you write the command in an incident Slack channel, you'll be prompted with the custom form.

## Prompt Form via Slack Block

A custom form can also be prompted in an incident Slack channel via a button in a custom block. The following demo will walk you through how to set this up.

<iframe width="100%" height="420" src="https://www.loom.com/embed/20952749582a47df984839a06cb3fed4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen autoplay />

## Prompt Form via Web UI

Lastly, a custom form can also be prompted from the Rootly web UI. First navigate to a specific incident and then select the Custom Form dropdown at the top. The dropdown will contain all custom forms that have been configured in the organization.

<Frame />


Built with [Mintlify](https://mintlify.com).