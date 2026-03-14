# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/screen-overview.md

# Screen Overview

## Service Matrix <a href="#a-service-matrix" id="a-service-matrix"></a>

The Service Matrix displays a list of all existing Customer companies with their corresponding Live contracts and Services, split across pages by individual Service Lines.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjYwMg==>" %}

The columns displayed for each Service Line represent the various types of Case and Ticket processes which can be created under this Service Line.&#x20;

You can select which service line you want to see from the dropdown list on the top-right of the page. Your last selected service line will be saved when you return to the Service Matrix Screen from other sections in Builder, and also after you logout and log back in.

Clicking on a Case or Ticket will open a dropdown list of options. The options vary depending on the state of the Case or the Ticket. Click here for more information on the [various State options](#b-service-matrix-key).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWoy0BELr5JyJrLTHOr%2F-MWoyMAPGjSn8hO0pTf4%2Fimage.png?alt=media\&token=8f571815-d038-4f52-98cf-352a2daac053)

{% hint style="info" %}
Please note that if you are loading more than 1000 rows in the service matrix, you will need to apply at least one filter before any content appears.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsQv79TzYgYAO0y11NAko%2Fimage.png?alt=media&#x26;token=ca789241-1a6d-4159-be37-3022010588e2" alt=""><figcaption></figcaption></figure>

## Service Matrix Key <a href="#b-service-matrix-key" id="b-service-matrix-key"></a>

The key in the top right tells you the status of the Cases and Ticket processes.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXlk29G07vRMfMey1tF%2F-MXllyLDMESkuAokIFgg%2Fimage.png?alt=media\&token=d522f8da-6be9-4631-8ca1-71ea1847e337)

For more information about these states, see below:

| State                       | Description                                                                                                                                                                                                           | Available Actions                                                                                                                                                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Draft                       | Configuration is in progress but it is not yet valid and Work Items cannot be run through it in Work Manager                                                                                                          | <ul><li>Open to view</li><li>Make further changes until valid (Edit).</li><li>Discard Draft changes</li><li>Delete (Retires process).</li></ul><p><em>Note: ‘Set Live’ option not shown in this state.</em></p>   |
| Validated changes           | Configuration in progress, and passes validation. This could be set live, or have test Work Items run through it in Work Manager (when in Test mode).                                                                 | <ul><li>Open to view</li><li>Make further changes (Edit).</li><li>Set live</li><li>Discard Draft changes</li><li>Delete (Retires process).</li></ul>                                                              |
| Live                        | Available to run Work Items through Work Manager.                                                                                                                                                                     | <ul><li>Open to view</li><li>Make changes (creates a new version to make changes in)</li><li>Delete (Retires process).</li></ul>                                                                                  |
| Live with draft changes     | Changes are being made to settings, but these new changes are not yet valid, so the Case or Ticket cannot be set live.                                                                                                | <ul><li>Open to view</li><li>Make further changes in the draft version until valid (edit).</li><li>Discard Draft changes</li><li>Delete (Retires process).</li></ul>                                              |
| Live with validated changes | The in-progress changes are now valid. You could publish these out to be live. New Work Items would then pick up these new settings. You can also run test Work Items through it in Work Manager (when in Test mode). | <ul><li>Open to view</li><li>Make further changes in the draft version until valid (edit).</li><li>Set live</li><li>Discard Draft changes</li><li>Delete (Retires process).</li></ul>                             |
| Deleted Versions            | This icon indicates that processes contain retired versions.                                                                                                                                                          | Note: This state and icon will only be shown if the 'Show deleted objects' setting is switched on. See [here ](https://docs.enate.net/enate-help/builder/user-dropdown#b-show-deleted-items)for more information. |

## Sorting and Filtering <a href="#d-sorting-and-filtering" id="d-sorting-and-filtering"></a>

The filter function in the top-right of the screen lets you filter the Services Matrix to show specific groups of data.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWoy0BELr5JyJrLTHOr%2F-MWoylGFNfWeum6Qtb5S%2Fimage.png?alt=media\&token=3de8d148-8535-4fa4-afe5-b0167db73aa0)

You can filter by Customer, Contract and/or Service by using the dropdown list or by using the free text search function. You can add multiple Customers, Contracts and/or Services into your search filters.&#x20;

Your applied filters will be saved when you return to the Service Matrix Screen from other sections in Builder, and also after you logout and log back in.

Your applied Customer and Contract filters will be saved when you switch between Service Lines in the Service Matrix, but the the Service filter will be removed.

## Adding Data to the Service Matrix <a href="#c-adding-data-to-the-service-matrix" id="c-adding-data-to-the-service-matrix"></a>

The '+' icon lets you add [Customers](https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/creating-and-editing-customers), [Contracts ](https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/creating-and-editing-customers)and [Services ](https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/creating-and-editing-services)to the Service Matrix, as well as [Case and Ticket types](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-a-new-ticket-case-to-a-service#creating-case-and-ticket-types-from-the-service-matrix).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MexoCfIfodN0wD8xz5f%2F-Mexog8w-lvdcJ0hnqVC%2Fimage.png?alt=media\&token=8dbe3423-2598-4485-86c0-4188c3bc2134)
