# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/email-connector-level-control-over-email-integrations.md

# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/email-connector-level-control-over-email-integrations.md

# Email Connector-level control over Email Integrations

You can choose to disable any of your Email-related Integrations for specific Mailbox Connectors, so the Integration doesn't run for any emails coming in to that specific mailbox. This more flexible steup lets you implement new AI technology while safeguarding specific work activities which you want to keep running as-is.

#### How to Disable and Re-Enable EnateAI Integrations per Connectors <a href="#how-to-disable-and-re-enable-enateai-integrations-per-connectors" id="how-to-disable-and-re-enable-enateai-integrations-per-connectors"></a>

When an Email-related Integration is activated in the Enate Marketplace, it is automatically applied to all email connectors. However, in certain scenarios, users may only want certain Email integrations to apply to certain email connectors. To disable integrations for a specific connector users should go to the Connectors page in the Email section of Builder. There they will see a new column titled 'Integrations', which will show the total number of Integrations available, and the number of those which are switched on for that Connector, e.g. '3/4' will mean that 3 of the 4 email integrations are running.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FA78jDYAJ6OseyYKivnPz%2Fimage.png?alt=media&#x26;token=281e4407-e662-4a0a-84d7-32ad8a643163" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Users must have the edit Email Connectors feature access granted in their User Role to be able to edit integrations for connectors.
{% endhint %}

To disable / re-enable integrations for a specific connector simply click on the relevant link in the 'Integrations' column box for the desired connector. This will bring up the 'Edit a Connector' pop-up, showing all activated Email integrations for that connector.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZoYr1V4tCg5g8yN5VTtu%2Fimage.png?alt=media&#x26;token=d7f9bf81-3f3a-4967-8ce2-d54408f18c93" alt=""><figcaption></figcaption></figure>

Toggle the settings on / off as desired to enable / disable an Integration. Please note the following:

* Whenever a new email connector is created, ALL integrations that are active in Marketplace will automatically be activated for the new connector.
* Whenever an Integration is enabled in Marketplace for a certain Email Integration pattern, e.g. 'Sentiment Analysis', it will be switched on for ALL Connectors. If an EmailAI pattern gets switched off in Marketplace and subsequently turned back on, it will be active in all connectors once again.

## Outgoing Connectors <a href="#outgoing-connectors" id="outgoing-connectors"></a>

Email Integrations cannot be turned on for email connectors that are just for outgoing emails, since currently these integrations are only relevant for incoming emails. For these connector an 'NA' will be displayed in the 'Integrations' column.
