# Source: https://doc.keepnetlabs.com/next-generation-product/platform/callback-simulator/manage-callback-scenarios/callback-templates.md

# Callback Templates

The **Callback** **Templates** page will show you all the available templates you have to send to your target users. From this page, you can create, edit, or delete any callback templates that you would like.

## Callback Templates Lists

The components of the **Vishing Template** page are explained below.

<table data-header-hidden><thead><tr><th width="204.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Template Name</td><td>Name of the callback template</td><td></td></tr><tr><td>Language</td><td>The language available for the template</td><td></td></tr><tr><td>Voice</td><td>List the available templates sorted by AI voice</td><td></td></tr><tr><td>Difficultly</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../..#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td><td></td></tr><tr><td>Created By</td><td>The company that created the template</td><td></td></tr><tr><td>Date Created</td><td>Date and time the training item was created</td><td></td></tr><tr><td>Available For</td><td>The companies that this template is available for</td><td></td></tr><tr><td>Tags</td><td>Tags assigned to the template to facilitate search efforts</td><td></td></tr><tr><td>Actions > Preview</td><td>Preview the template before launching to target users</td><td></td></tr><tr><td>Actions > Edit</td><td>Edit and customize the template</td><td></td></tr><tr><td>Actions > Duplicate</td><td>Duplicate the template for editing and customization</td><td></td></tr><tr><td>Actions > Delete</td><td>Permanently delete the template</td><td></td></tr></tbody></table>

## How to Create a Callback Template

Follow the steps below to create a new callback template.

* Click on the **+NEW** button on the **Callback Templates** page.
* On the **Template Info** page, complete the following fields:
  * **Select the difficulty level:** The difficulty rating for the template
  * **Template name:** Name of the callback template
  * **Description:** The brief description for the template
  * **Tags:** Tags assigned to the template to facilitate search efforts
* If you’re a Reseller, you can choose what companies this template is available for
* Click **Next**
* On the **Dialog Settings** page complete the following fields:
  * Select the **Language and Voice** that the callback template will be voiced in
  * Enter a message for the **Caller** **Greeting**. The caller is expected to enter a 6-digit phishing code at the end of the call greeting message.
  * Enter the **Steps** that define your callback template
    * Select **Text-To-Speech** or **MP3** steps to create your callback campaign.
      * **Text-to-speech:** The text written by the admin will be narrated by the AI in the chosen language and voice.
      * **MP3 Audio File:** The mp3 voice file will be played to the end user.
      * **Pause:** The call will be held on in silence in seconds after the previous step is completed before the second step is played.
    * Next, enter the number of number digits that the end user will have to enter to move on to the next step.
      * Leave by default zero if no required digit must be dialed by the end user for the related step.
    * You need to choose one step, “**Digit Entering Step**”, in order to mark the end user as phished on the report if the user comes to the related marked step.
    * Finally, complete the fields for **Invalid Dialing Notice.** This notice will be played when the user fails to enter the requested amount of digits correctly.
      * Under **Methods**, select if you would like to use voice to text or if you would like to upload an mp3 file.
        * If you select the **voice-to-text** option, enter the text for the AI to narrate
* Once you are happy with your template, click **Save**.

{% hint style="info" %}
You can add up to five steps for your callback template.
{% endhint %}

## **Utilizing Merge Tags in Callback Templates**

Here's a list of merge tags to help you make your callback template more personal. Adding these tags can make your phishing campaign more tailored to the recipient.

<table><thead><tr><th width="210.5">Merge Tag</th><th>Description</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td></tr></tbody></table>

## Video Tutorial

Callback Templates are designed to create voice phishing steps for your target audience. You can see how to create, edit, and delete the callback templates from the following video.

{% embed url="<https://youtu.be/j3W4JLCeLXM?si=BReJQW6rkKBlxSOq>" %}

## FAQ

### Q: Can I restore a deleted template?

A: No. Once an item has been deleted, it is no longer available.

### Q: Can I use a different file type than MP3 for the Invalid Dial Notice?

A: No. The platform only supports MP3.

### Q: Can I upload an MP3 file with a size of more than 1MB?

A: No. The platform only supports MP3 files of 1MB size.
