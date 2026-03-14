# Source: https://docs.mailtrap.io/email-marketing/campaigns/email-templates.md

# Source: https://docs.mailtrap.io/email-api-smtp/email-templates.md

# Email Templates

### Overview

Email Templates allow you to design, edit, and host HTML email templates, and reference them via API.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9ff933e3fb8c346003904bf50374326db5d665cf%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

By storing the template on Mailtrap and calling it via API, you can easily change the template code without committing to your codebase.

Email Templates support Variables, and Mailtrap uses Handlebars as a template engine.

You can put {{user\_name}} into your template and pass "John" as the "user\_name" value via API.

For a complete guide on using Handlebars with email templates, see [Handlebars Guide](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars).

### Creating a template

{% stepper %}
{% step %}
Navigate to the **Templates** menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-472bf2d946c91f5f5d547e55913798aaa2fda7f6%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the **Create New Template** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-08c42f957e72d0bf718a9b46f35119e185237472%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the drop-down menu to select one of your domains, enter the **Template name**, **Subject**, and **Category**, and click **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e305265aa6521ed901e2095b7037b3d0b50ab2eb%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Choose the **Drag & Drop Editor** to build the template without coding, or select **HTML Editor** if you prefer to write/modify the code.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f56822fb58761484b716c51f934ff2c46dc90448%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Create/modify the design and click **Finish**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-04acabe528652a54e28c38bb6295c6ee24da3316%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

The main **Templates** menu features all your saved templates. To quickly access a saved template, just click on it within the main menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bb74cbc0483f284c95a1cceebe12226f7e22d94c%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Managing templates

#### List of templates and user permissions

Clicking on Templates in the side menu lists all the templates you can access. Access to templates is managed on a domain level. You need to have Admin access to a domain to manipulate the templates. In case you don't have Edit rights, you can't change the template. Each account can have up to 200 email templates.

{% hint style="warning" %}
You can delete a template. However, this action is irreversible, so be sure to change the sending/testing code after deletion. When the template is deleted, the UUID is also deleted, and Mailtrap won't be able to render it.
{% endhint %}

### Next steps

* [Editing and Customizing Templates](https://docs.mailtrap.io/email-api-smtp/email-templates/editing-and-customizing) - Learn how to customize templates with the Drag & Drop or Code Editor
* [Handlebars Guide](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars) - Complete guide to using Handlebars syntax in templates
* [Integration](https://docs.mailtrap.io/email-api-smtp/email-templates/integration) - Integrate templates with Email API/SMTP
* [Debugging](https://docs.mailtrap.io/email-api-smtp/email-templates/debugging) - Test templates with Email Sandbox
