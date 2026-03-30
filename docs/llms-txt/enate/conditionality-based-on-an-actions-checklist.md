# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-conditionality/conditionality-based-on-an-actions-checklist.md

# Conditionality Based on an Action's Checklist

When using conditionality in your Case flows, you can use a number of types of system data as part of your condition, for example standard system work item fields and custom data fields.

We have now added the ability to use the results of individual checklist items, both global and local, in your conditions, letting you choose alternate routes depending on how a check has gone.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7lmza7sVEkrtFRJQ8JU2%2Fimage.png?alt=media&#x26;token=fb1cd63d-1031-4558-a648-229496c03490" alt=""><figcaption></figcaption></figure>

Watch this video to see how that can be done, or read below for more specifics and details:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM1MjkwMA==>" %}

Clicking on the dropdown will reveal the Actions that have checklists to choose from. They will be displayed in the order in which the Actions appear in the flow. Clicking on an Action will show the checks that you can choose to base your condition on, displayed in order in which they appear on the checklist.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4hhHA1Mt3N5oK1EW7wlb%2Fimage.png?alt=media&#x26;token=2c84becc-6d59-460e-9353-335c7dd59769" alt=""><figcaption></figcaption></figure>

You can only use the 'Equals' and 'Not Equals' conditions for conditions based on the results of a check in an Action's checklist, just as you would short text data fields.

The values you can create conditions for against a checklist item are "Yes", "No", and "NA" for Not Applicable. Be aware that these values are case sensitive and should be entered in the value field exactly as above within double quotes.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1FCwJZ8foUXB4hdUSYXs%2Fimage.png?alt=media&#x26;token=e644c9a5-e411-44ec-9bb9-49ff916396bf" alt=""><figcaption></figcaption></figure>

As standard, make sure to create an 'else' branch, to handle the flow when you're conditions are not met. At runtime, if the condition is not met, the system will execute the 'else' branch.&#x20;

If you're using the advanced option to build a more complex expression, checklist items can also be incorporated here - once you've picked them from the dropdown list they'll be added into your expression with a unique identifying GUID.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjSfQJDwUxfqVtr9Cb6Qo%2Fimage.png?alt=media&#x26;token=afe55e71-05f5-4aea-af3d-1f4f2231219f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that you can only use checks from Actions in a previous step in your conditional expressions and you cannot use check from ad-hoc Actions.&#x20;
{% endhint %}

Once you're happy with your condition settings, click 'validate' to ensure they'll work at runtime, then 'OK' to apply the condition to the Case flow.
