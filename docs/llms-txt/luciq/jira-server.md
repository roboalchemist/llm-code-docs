# Source: https://docs.luciq.ai/product-guides-and-integrations/integrations/jira-server.md

# Jira Server

{% stepper %}
{% step %}
Insert your **username**, **password**, and **URL**.
{% endstep %}

{% step %}
Pick the **project** you want to forward to as well as the **assignee**. Fields can be mapped from Luciq to Jira fields. You can also choose which information is forwarded from your Luciq dashboard to Jira.
{% endstep %}

{% step %}
At this point, we just need to test your integration so that we're sure everything is working smoothly.
{% endstep %}

{% step %}
All done! Your integration is now set up and ready to go. From this final page, you can allow automatic forwarding (don't worry, though, these can be reconfigured at any time!)
{% endstep %}

{% step %}
Start receiving issues on the spot on your Jira dashboard.

With this integration, bugs and feedback can be converted manually into issues on Jira with just a click.
{% endstep %}
{% endstepper %}

### Mapping Custom Fields

This section covers how to map Jira custom fields to fields from the Luciq dashboard.

{% stepper %}
{% step %}
Create the custom field on Jira
{% endstep %}

{% step %}
Choose a type for the field you've created in the previous step.
{% endstep %}

{% step %}
Reconfigure your Jira integration
{% endstep %}

{% step %}
Map the Jira custom fields to the corresponding Luciq fields (make sure they have the same type).
{% endstep %}

{% step %}
Test your integration
{% endstep %}

{% step %}
Finished — All done!
{% endstep %}
{% endstepper %}

### PAT Tokens

PAT stands for Personal Access Token. Use the PAT token, generated from Jira Server, to add a layer of authentication on Luciq ↔︎ Jira Server integration.

Using a PAT token is more secure than authenticating an integration with a username and password.

Setup steps

{% stepper %}
{% step %}
Navigate to your Luciq dashboard.
{% endstep %}

{% step %}
Navigate to your app’s Settings page.
{% endstep %}

{% step %}
Navigate to the Integrations tab.
{% endstep %}

{% step %}
Launch a new Jira Server integration wizard.
{% endstep %}

{% step %}
Toggle from Basic Authentication to PAT Token
{% endstep %}

{% step %}
Enter your PAT Token and Jira Site URL.
{% endstep %}

{% step %}
Navigate to [this link](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) to create a PAT Token on Jira.
{% endstep %}

{% step %}
Copy the created PAT Token to the PAT Token field on Luciq’s wizard.
{% endstep %}

{% step %}
Continue setting up the integration normally.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}

### Limitations

* Token Expiry:
  * The token expiry date is controlled from the Jira side, not from Luciq.
  * If a token is created with a specific expiry date, it must be updated on Luciq’s dashboard before expiry, otherwise, there is a risk of not forwarding some data between Luciq and Jira during the period of non-validity of the PAT Token provided until it’s updated.
    {% endhint %}

### Editing Current Integrations

Currently, editing already existing integrations is not supported so a new one will need to be created.
