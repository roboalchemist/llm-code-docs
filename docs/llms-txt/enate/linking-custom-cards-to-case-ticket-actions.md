# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/linking-custom-cards-to-case-ticket-actions.md

# Linking Custom Cards to Cases / Tickets / Actions

Watch this video for an example of how to create Custom Data and Custom Cards for a Case.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjU3Nw==>" %}

Once you have created you custom fields you can link them to a Custom Card for subsequent displaying in a Ticket / Case or Action Screen. Cards can be displayed as part of the main section for Cases, Tickets and Actions, and as a side panel.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpqrIkDQGOzfgh5k6K%2Fimage.png?alt=media\&token=a84c9af6-fd82-4aef-8941-a145d6aed4d5)

* Side Panel card displays between the Contacts card and the Files card.
* Main Panel card appears:
  * Ticket: After the Ttimeline card.
  * Case: After the Timeline / Action display card.
  * Action: After the Checklist card.

You can add a single card to the Main / Side panel section for a Case / Ticket / Action instance in Builder. Neither is mandatory.

{% hint style="info" %}
Note: The same card should not be added in both locations and the same field should not be referenced in two cards showing on the same Ticket / Case / Action.
{% endhint %}

## Linking Cards to a Case <a href="#a-linking-cards-to-a-case" id="a-linking-cards-to-a-case"></a>

Select available cards from the ‘Main Card’ and / or ‘Side Card’ dropdowns in the Case Info tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpr-MUeEJ6QZJ-Bkk6%2Fimage.png?alt=media\&token=36b26056-b104-432b-9ac8-3e9fb91c7e57)

## Linking Cards to an Action <a href="#b-linking-cards-to-an-action" id="b-linking-cards-to-an-action"></a>

Select available cards from the ‘Main Screen’ and / or ‘Side Panel’ dropdowns in the Action Info tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpr42KHwnw8QoSErMk%2Fimage.png?alt=media\&token=d7db85f6-c540-4f81-9917-05c943cc84e8)

## Linking Cards to a Ticket <a href="#c-linking-cards-to-a-ticket" id="c-linking-cards-to-a-ticket"></a>

Custom Card definition for a Ticket is done at the header level rather than per Ticket category. Access the card definitions for a Ticket via the settings toolbar icon:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpr9VSf-bgzeHU8tyq%2Fimage.png?alt=media\&token=67db9db9-17ec-47c2-ab48-3443fd265e95)

Set the desired main and/or side panel card in the resulting popup:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWprCvxrQ5RYEaD3E71%2Fimage.png?alt=media\&token=e6290256-49a4-4bcc-b960-5c9e54e93995)

{% hint style="info" %}
Note that for Tickets you can also define a Smart Card to be used for Self Service Ticket submissions (these much be created separately from the smart cards defined for Work Manager Work Items).
{% endhint %}
