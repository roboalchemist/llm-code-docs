# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content.md

# Advanced Custom Card Code

In Enate you can add custom content into your Tickets, Cases & Actions. This custom content is displayed via Custom Cards which can be set to display in the main section of the work item, and also as a section of the side panel on the right side of the screen.&#x20;

You can instantly create cards of your custom data fields or you can create Advanced Custom Cards that can be designed with HTML, JavaScript or CSS to show richer content such as external systems & webforms.

To create an Advanced Custom Card, select the 'Advanced' option in the Custom Card screen. This will allow you to add HTML, Typescript and CSS.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDGG7hIzZsa0jayXwKZiv%2Fimage.png?alt=media&#x26;token=b70f52ef-b626-4a46-935e-2054634f0615" alt=""><figcaption></figcaption></figure>

You will first be presented with a warning message highlighting that you're responsible for the errors / unexpected behaviour that may occur from your bespoke code.

You can revert back at any time by switching the customized setting back to off - this will remove any custom code and return the card to its original form.

{% hint style="info" %}
Please Note: A Custom Card is an angular component which is a combination of Typescript, HTML and CSS. Please go to <https://angular.io/guide/component-overview> and read through it before moving on. Custom Cards in Enate execute in Angular. Customers who use or are developing advanced custom card content should review the changelog of Angular (<https://github.com/angular/angular/blob/master/CHANGELOG.md>) for changes that may affect their custom code.
{% endhint %}

Check out the following sections for explanations for how they are structured plus some examples of standard content you may wish to use..

{% content-ref url="custom-card-content/custom-card-code" %}
[custom-card-code](https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content/custom-card-code)
{% endcontent-ref %}

{% content-ref url="custom-card-content/custom-card-html" %}
[custom-card-html](https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content/custom-card-html)
{% endcontent-ref %}

{% content-ref url="custom-card-content/custom-card-css" %}
[custom-card-css](https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content/custom-card-css)
{% endcontent-ref %}

You can check out our Github section that provides you with sample code integrations for Advanced Custom Cards here:

{% embed url="<https://github.com/EnateLtd/Custom-Card-Integration>" %}
