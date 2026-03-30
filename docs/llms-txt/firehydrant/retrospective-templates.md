# Source: https://docs.firehydrant.com/docs/retrospective-templates.md

# Retrospective Templates

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Plans
      </th>

      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        * <Glossary>Free Plan</Glossary> (up to 1 template)
        * <Glossary>Pro Plan</Glossary> (up to 3 templates)
        * <Glossary>Enterprise Plan</Glossary> (unlimited)
      </td>

      <td style={{ textAlign: "left" }}>
        * `Manage Incidents`
      </td>
    </tr>
  </tbody>
</Table>

Creating a retrospective template allows your team to standardize and customize how you capture learnings from incidents. Every organization has unique needs when conducting retrospectives - from the questions asked to the data collected. With our template system, you can build multiple templates that match different incident types or team requirements, automatically include relevant incident data, and create targeted questions that drive meaningful discussion.

## Prerequisites

* You'll need <Glossary>Owner</Glossary> permissions

## Setting Up a New Template

<Image align="center" alt="Adding a retrospective template" caption="Adding a retrospective template" src="https://files.readme.io/be843f5eaa9a2d97bd2bd4b7c412b3e5d3cddec91f739c719171ff750ff4b59d-retrospectives-create-template.png" width="650px" />

1. Navigate to the FireHydrant Retrospective templates page
2. Click **Add Retrospective Template**
3. Enter required template information:
   * **Name**: Give your template a descriptive name
   * **Description**: Provide context about when and how to use this template

### Adding Questions

<Image align="center" caption="Adding Field to Retrospective Templates" src="https://files.readme.io/43bd7e2bf54ef71787d604832e80f3f6e6182ded30e3b96caa1cca230595facb-image.png" />

You can add questions to your template in two ways: using recommended questions or creating custom questions.

#### Creating custom questions

1. Click **Add a Question**
2. Choose a field type:
   * **Text**: For open-ended written responses. Note that this type also allows specifying full templates and preclude text. This may be useful for specifying a format or instructions for users
   * **Text Select**: For single-choice dropdown selections
   * **Multi-select**: For multiple-choice selections
   * **Numeric**: For number-based responses
   * **Date**: For temporal information
   * **Contributing Factors**: For tracking incident causes
   * **Instructional Text**: For adding guidance or section headers
3. Configure the question:
   * Enter a field name (required)
   * Add tooltip text to provide guidance (optional)
   * Select whether the question is required for publication
   * Add any additional configuration specific to the field type

#### Using recommended questions

FireHydrant provides pre-configured question sets for common retrospective needs:

* Blameless retrospective ground rules
* Areas of improvement
* Lessons learned
* Recognitions

To add recommended questions:

1. In the Retrospective Question Set section, navigate to the recommended questions section
2. Select the desired question set/s
3. Click **Add Selected**

<Callout icon="📘" theme="info">
  **Note**:

  Recommended questions and incident sections are only available for getting started. They are not available once you have created questions or added sections.
</Callout>

### Pre-Templated Rich Text

<Image align="center" alt="Retrospective question with pre-templated content" caption="Retrospective question with pre-templated content" src="https://files.readme.io/438eeb55940cecb867e44be6d0e758dd454dc6276ac5e03f0b6625e82d971b53-CleanShot_2025-06-20_at_15.59.552x.jpg" width="650px" />

When using the **Text** question type, we support full rich text capabilities and collaborative editing with multiple users. In particular, you can set pre-configured question/text content as well, enabling capabilities like you would find in a Google Docs template.

Simply ensure you have checked the option to "Prefill text field with template."

### Incident Sections

<Image align="center" alt="Recommended retrospective questions and incident sections " caption="Recommended retrospective questions and incident sections" src="https://files.readme.io/702206245aa24e43dfac935aeb6d20d74397eaa59b40d79ed48a0b67491505d9-retrospectives-getting-started.png" width="650px" />

You can customize what incident data is shown in your retrospective by adding, deleting, and reordering various types of incident data, including:

* **Timeline**: Shows the sequence of incident events
* **Key Data** : Milestones, participants, and impacts
  * **Milestones**: Key events during the incident
  * **Milestones with time elapsed**: Shows duration between key events
  * **Responders**: Team members involved in incident response
  * **Impact**: Services, environments, and functionalities
* **Details**: Descriptions, summaries, and custom data
  * **Incident Summary**: An AI generated summary of your incident based on incident data available in FireHydrant.
  * **Description**: Incident Description
  * **Customer Impact**: Summary of impact on customers
  * **Custom Fields**: Any custom data fields configured for your organization
  * **Labels**: Incident categorization and tags
* **Resources**: Reference resources from the incident
  * **Links**: Links added to the incident
  * **Change events**: Associate any change to your system to your incident
  * **Runbooks**: Runbooks attached to the incident.
  * **Related Incident**: Related incidents

#### Adding sections

1. Scroll to the Incident Sections area

2. Choose from available incident data types

3. Add your sections:
   * Add new sections by clicking **Add Incident Sections**
   * Remove sections by clicking the delete icon
   * Reorder items within each section by dragging them to the desired position

#### Recommended incident sections

FireHydrant provides common incident sections for your retrospective needs:

1. Scroll to the Incident Sections area
2. Choose from available sections:
   * **Timeline**: Shows the sequence of incident events
   * **Overview**: Includes incident summary and customer impact
   * **Tasks**: Includes tasks and follow-up tickets
   * **Essential Incident Info**: Includes milestones and responder information
3. Click **Add Selected**

### Preview and Testing

<Image align="center" alt="Preview a retrospective" caption="Preview a retrospective" src="https://files.readme.io/2171e4b0aed6121862ac9c2446befd75ded8ae6db8941e36c58442ac51e2edd4-retrospective-preview.png" width="650px" />

1. Click **Preview** to review:
   * All questions and their formatting
   * Incident section layouts
   * Navigation between tabs (Details, Timeline, Actions)
2. Save and test your template:
   * Click **Create Retrospective Template**
   * Select a Runbook from the dropdown
   * Click **Add and Test** to see it in action

## Making Adjustments

After creating your template, you can:

1. Return to Retrospective Templates
2. Select your template
3. Make any needed changes:
   * Add or remove questions
   * Modify incident sections
   * Update configuration settings
4. Save your changes

Your template is now ready to be used in actual incidents. You can attach it to runbooks for automatic use or select it manually during incident retrospectives.

## Attaching Retro Templates to Incidents

Templates can be applied in two ways, automatically via a runbook or manually from the respective view of an incident.

The added capability for Retrospectives is that you can automatically attach them to incidents based on various conditions in a Runbook. Using Runbooks, you can automatically attach Retrospectives to incidents based on any conditions set, ensuring the appropriate retrospective is instantly available.

### Adding the Runbook step

<Image align="center" alt="Add a retrospective step" caption="Add a retrospective step" src="https://files.readme.io/c7820515b0c3efd52785dad25c0e69ce24b57d0ecf877710bdaa8626607eed61-retrospective_runbook.png" width="650px" />

1. Go into a Runbook, click "Edit Runbook," then click '+ Add step.'
2. Search for "retrospective" and click **Add a retrospective**. Then select the Retrospective you'd like added to the incident.
3. Configure conditions for when the template should be applied.

For more information, examples, and best practices, visit [Add a Retrospective](https://docs.firehydrant.com/docs/runbook-step-add-a-retrospective).

### Manually attach a template

<Image align="center" alt="Manually attach a template" caption="Manually attach a template" src="https://files.readme.io/7052b413cccb5980887563b7f69b6346ca2f64631fdf4a72b90c6f98237978e0-retrospectives-manually.png" width="650px" />

There are instances where you need to manually attach a retrospective to an incident.

1. Open the retrospective view of an incident
2. If there is a template attached, click the **" + "** next to current template
3. If no template is attached click the **"Attach template"**
4. Choose your desired template. Then click **“Attach”**