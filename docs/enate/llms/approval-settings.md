# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/approval-settings.md

# Approval Settings

## Approval Rules

The Approval Rules section is where you can supply the rules which determine who approval requests are to be sent to.&#x20;

There can be any number of different business rules, from the simple to very complex, involved here. Rather than create a dedicated rule interface in Builder for you to try to build them directly there (which would be very unlikely to cover such a wide range of required business scenarios), we instead use an approach where you can upload an Excel file where you can define whatever business rules you need to, as long as the result passes up to Enate the names of the individuals who are to be the approvers.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FU0WAnqrRlzbHTnPke0r7%2Fimage.png?alt=media&#x26;token=33883cd9-022a-4e23-b09e-9a67f017f49a" alt=""><figcaption></figcaption></figure>

You can download an Excel template from the Approval Rules section of the System Settings page in Builder that you can use as a guide for your own rule creation.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUxTnt5RIQT28HMHwrjR9%2Fimage.png?alt=media&#x26;token=204a3fcf-0f70-4459-b318-1955f4cc319e" alt=""><figcaption></figcaption></figure>

The first sheet of the template contains instructions about how you should correctly format your own approval rules.

Some of the excel template consists of standard sections where you'll need to provide data in a certain way, while other sections are more freeform where you can enter whatever business logic you need to. Note that the variables defined will need to be information Enate has access to, and the Approvers specified will at least need to have a Contact record set for them within the system.

The Input Parameters sheet is were you define the values that they will use in their rule conditions.

The Rules sheet is where users define your rule conditions. These rules should be based on the Input Parameters specified in the Input Parameters tab.

The Approver sheet is where you provide their approvers, and their approval levels. When an approval process is triggered in Enate, Enate will use these values to determine who to send the approval request to.

Whenever an Approval Action is triggered in a workflow, Enate will automatically run through the rules in the Excel template (passing in whatever variable values are asked for from the work item) extract the resulting approver names and email addresses and then send the approval requests to those individuals.

Once you have uploaded a valid rule file, it will be marked as having 'Validated Changes' .&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnwoRJlazoSHjHRrPCWrc%2Fimage.png?alt=media&#x26;token=a08854d4-8e02-4027-a8a4-f90c8d4bc177" alt=""><figcaption></figcaption></figure>

This means it can be used for testing in Work Manager using test mode. Once you have done your testing and you are happy with your rules, set the rules sheet to live so that it can be used in live processes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZhpDnbpj5aG7P11bSbG8%2Fimage.png?alt=media&#x26;token=483beea7-0ee3-4394-a968-b1225eff837c" alt=""><figcaption></figcaption></figure>

You can also download, delete and view the activity history of the rules file using the ellipses menu on each uploaded sheet.

## Approval Rejection Reasons

At runtime, if an approver decides to decline a request, they will have to specify a rejection reason.

The rejection reasons they can choose from are set the 'Approval Rejection Reasons' section of the System Settings page in Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXiP3ywn2kA26KAQHmnhC%2Fimage.png?alt=media&#x26;token=1d6f1213-7dd0-4548-8f8d-2a75d4201d94" alt=""><figcaption></figcaption></figure>

There are a number of default, out-of-the-box reasons, which include:

| Rejection Reason                    | Description                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Budget Constraints                  | The requested funds exceed the allocated budget or available funds for the specified period.            |
| Duplicate Requests                  | The same request has been submitted multiple times.                                                     |
| Incorrect or Incomplete Information | The submitted data or documentation is inaccurate, incomplete, or contains errors.                      |
| Missing Supporting Documentation    | Required supporting documents, such as invoices, receipts, or contracts, are missing.                   |
| Policy Non-Compliance               | The request or transaction violates company policies, regulatory requirements, or compliance standards. |
| Vendor or Partner Issues            | The proposed vendor or partner has encountered issues or concerns that impact the request's viability.  |

If these don't quite meet your needs, you can also create new rejection reasons. To create a brand new reason, click on the plus symbol.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsmFHlRDB2wZScrENz2SW%2Fimage.png?alt=media&#x26;token=e7d46269-d8a1-4ae1-8c47-fe41a6ccdc00" alt=""><figcaption></figcaption></figure>

Give the reason a name and a description and click to create.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiHzipf0pd8fJHxEEazUt%2Fimage.png?alt=media&#x26;token=bdba6495-2a8d-4688-a789-48255d0250ba" alt=""><figcaption></figcaption></figure>

You can always edit a rejection reason after it has been created by clicking on it and editing its details in the subsequent pop-up, and you can delete a reason by hovering over the reason and clicking on the 'X'.&#x20;
