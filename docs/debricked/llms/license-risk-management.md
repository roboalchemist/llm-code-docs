# Source: https://docs.debricked.com/product/license-risk-management.md

# License risk management

When working with open source, it is crucial to ensure and maintain open-source compliance, also from a commercial perspective. To help with that, OpenText Core SCA provides you with a comprehensive overview of all licenses in the repositories you have integrated with us. You can find that information in different areas of the tool.

### **View all licenses**

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FAUJdaB0dbe2lKUNjQUbm%2FLicense1.png?alt=media&#x26;token=5a96e3a4-d6e1-4fb7-a87a-21c4f14a14cf" alt=""><figcaption></figcaption></figure>

To view licenses, click **License** tab on the left side menu. Here, you can view the list of all your licenses in alphabetical order. The screen displays the following information:

* Name: The name of license.
* License Risk - The grade of potential compliance risks involved with the specific license, assessed based on the use case chosen for the repository.
* Dependencies - The number of dependencies affected by the license.
* License family - The family to which the license belongs.

### **View all repositories affected by license**

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FCB7XPA2YtFUyNtwD4bmG%2Fimage.png?alt=media&#x26;token=32ac3a45-3b5b-4308-906a-a7b4f6949ea2" alt=""><figcaption></figcaption></figure>

To view all repositories affected by license, follow these steps:

1. Click **License** tab on the left side menu. Here, you can view the with a list of all your licenses in alphabetical order.
2. Click a specific license to view all repositories with that specific license.  Here, you can also view the risk associated with the license within all affected repositories, as well as how many dependencies per repository are affected.
3. After you click a specific repository, the above-mentioned information can also be found in the **Licences** tab.

> You can export the filtered and visible data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### License review or override

{% hint style="info" %}
*This feature is only available for Enterprise users.*&#x20;
{% endhint %}

As a Repository or Company Admin (Enterprise), you can review and manually override the license found by OpenText Core SCA on a dependency level.

To do so:

1. From a repository page, go to the **License** tab. Here you can view the list of all licenses detected in the repository.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FdnQsHznl1JChKXMaegaZ%2FLicense2.png?alt=media&#x26;token=a4281b9e-2fa5-42da-a2cf-f000cb59c611" alt=""><figcaption></figcaption></figure>

2. Click **Review**. Here, you can find a list of all licenses detected and can override the data.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2F0G0Jg7YfPgoXVxQfN2u1%2Fimage.png?alt=media&#x26;token=82369f37-d1b4-45b6-8336-4be4d12e8828" alt=""><figcaption></figcaption></figure>

Depending on your needs, you can:

* Delete the license by clicking the **trashcan** icon.
* Change the detected license, by clicking **Change license** and selecting a new one from the dropdown menu
* Add license(s) by clicking the **+** button for multi-licensing.

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><a href="license-risk-management/licence-families"><strong>License families</strong></a></td><td></td><td></td></tr><tr><td><a href="license-risk-management/license-risks"><strong>License risks</strong></a></td><td></td><td></td></tr><tr><td><a href="license-risk-management/set-up-a-use-case"><strong>Set up a use case</strong></a></td><td></td><td></td></tr><tr><td><a href="license-risk-management/proxying-non-standard-license-identifiers"><strong>Proxying non-standard license identifiers</strong></a></td><td></td><td></td></tr></tbody></table>
