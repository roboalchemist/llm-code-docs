# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/super-flexible-cards.md

# Advanced Custom Cards

If you want your Custom Card to contain bespoke content, you can select the 'Customized' option. This will allow you to add HTML, Typescript and CSS.&#x20;

You will first be presented with a warning message highlighting that you're responsible for the errors / unexpected behaviour that may occur from your bespoke code.

You can revert back at any time by switching the customized setting back to off - this will remove any custom code and return the card to its original form.

{% hint style="info" %}
Please Note: Custom Cards in Enate execute in Angular 10. Customers who use or are developing advanced custom card content should review the changelog of Angular 10 (<https://github.com/angular/angular/blob/master/CHANGELOG.md>) for changes that may affect their custom code.
{% endhint %}

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpqPkURnnhAbPlU81G%2FSelecting-Customized.gif?alt=media\&token=32ab9a0c-a279-47e6-8fcc-c2028b23e58a)

Selecting the 'Customized' option will will expose HTML, Typescript and CSS tabs on screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpqWp5eQKIvqTKS8q3%2Fimage.png?alt=media\&token=94c1de47-6006-470d-a07d-b68a5e1bfca2)

When you click on one of these tabs, you will see the existing auto-generated code for the Custom Card. You can adjust / overwrite this code as desired.

| Attribute      | Description                                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **HTML**       | <p>The HTML Code will populate the Custom Data Fields on the Ticket/Case/Action. Also specifies the input format in which the data needs to be added. </p><p></p><p>If you reference a custom data field in the HTML for a card, the field must be added to the card in order to work.</p> |
| **Typescript** | The Typescript will do the binding of data and adjust the HTML before rendering it to the webpage. It can also perform the validations where it can highlight the mandatory fields.                                                                                                        |
| **CSS**        | Deals with styling required for the HTML; example hiding the up/down arrow on a number field control etc.                                                                                                                                                                                  |

{% hint style="warning" %}
When you update the Custom Card by adding new Custom Data Fields to it, you will have to disable and re-enable the 'Customized' toggle option in order to generate the customised code for the new fields.
{% endhint %}

You can see what edits have been made to the Custom Card and when, as well as when the Custom Card was created, and even when a Custom Card was deleted by clicking on the Show Activity button.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpqj6uaForukhAkArM%2Fimage.png?alt=media\&token=ae87c284-13ca-4050-a8b1-efa0d78d6f2e)

### Custom Card Code Examples <a href="#custom-card-code-examples" id="custom-card-code-examples"></a>

Check out the [Custom Card Code](https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content) section of the Enate Extensions area to learn more about the code you can write and how to interact with data fields and validation.
