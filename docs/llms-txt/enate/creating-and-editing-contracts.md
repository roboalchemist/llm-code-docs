# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/creating-and-editing-contracts.md

# Creating and Editing Contracts

## Creating Contracts <a href="#a-creating-contracts" id="a-creating-contracts"></a>

To add customer Contracts, click on the '+' icon at the top of the Service Matrix and select 'Contract'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWozQugbRH55dsf91SP%2Fimage.png?alt=media\&token=bce03137-010e-4d64-bd12-e50e2b9172b2)

Fill in the Contract settings in the resulting popup.

## Contract Settings <a href="#b-contract-settings" id="b-contract-settings"></a>

The settings for Contracts are:

| Setting                                        | Description                                                                                                                                                                                                                                                                    | Notes                                                                                                                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer                                       | The Company receiving service                                                                                                                                                                                                                                                  | Mandatory.                                                                                                                                                                                   |
| Name                                           | The Name of the Contract                                                                                                                                                                                                                                                       | Mandatory. Must be unique within Customer.                                                                                                                                                   |
| Description                                    | A description of the Contract                                                                                                                                                                                                                                                  |                                                                                                                                                                                              |
| Supplier                                       | The Company delivering service.                                                                                                                                                                                                                                                | Mandatory.                                                                                                                                                                                   |
| Working Hours per Day                          | <p>When a Due Date Rule references ‘Working Days’, this setting is used to translate Working Days into this number of working Hours.<br></p>                                                                                                                                   | Value specified should not exceed the difference between start and end hours of work in the Default calendar selected above.                                                                 |
| Customer Calendar                              | Working calendars are used when calculating any Due Date/Times for activities configured to use the Customer’s working hours (e.g. ‘must be completed within 5 working hours, according to the Customer’s Working Calendar).                                                   | Mandatory. Defaults to value set at Customer Company level, but can be overridden here.                                                                                                      |
| Supplier Calendar                              | The Supplier’s Working calendar is used when calculating any Due Date/Times for activities configured to use the Supplier’s working hours (e.g. ‘must be completed within 5 working hours, according to the Supplier’s Working Calendar).                                      | Mandatory. Defaults to value set at Service Provider Company level, but can be overridden here.                                                                                              |
| Timezone                                       | The standard Timezone for work carried out under this Contract                                                                                                                                                                                                                 | Mandatory.                                                                                                                                                                                   |
| Default Language                               | When creating a new Contract, any customer-level language will be set as the initial default value. If different to language this will supersede the language set at Customer level, and any changes made to the customer-level language will not affect the Contract setting. | Mandatory.                                                                                                                                                                                   |
| Default Currency                               | Select from the dropdown which currency you would like to set as the default currency at contract level                                                                                                                                                                        | Mandatory.                                                                                                                                                                                   |
| Team                                           | For use in auto-generation of large volumes of Queues per Contract - Queues will include this 'Team' Name. A dropdown option will appear that filters down as you start typing.                                                                                                | Optional.                                                                                                                                                                                    |
| Document Classification Model                  | <p>Enter the model you want to use here. You can refresh to view the updated list of models available.</p><p></p>                                                                                                                                                              | Only available if the Infrrd Document Extraction component, available in [Enate Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace), is enabled. |
| Allowed File Types for Document Classification | Enter the file types you want to be considered for file classification here.                                                                                                                                                                                                   | Only available if the Infrrd Document Extraction component, available in [Enate Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace), is enabled. |

## **Subsequent Editing** <a href="#d-subsequent-editing" id="d-subsequent-editing"></a>

To edit a contract's settings, click on the ellipses beside the Customer name and select the Edit link. Make your desired changes in the resulting popup and click OK to save changes.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWozpiINodyXeV9t-dS%2Fimage.png?alt=media\&token=9466a422-e2e4-446c-b36c-e22150edc438)

### Editing of Service Provider of Existing Contracts <a href="#editing-of-service-provider-of-existing-contracts" id="editing-of-service-provider-of-existing-contracts"></a>

In Builder you can edit the Service Provider of existing Contracts.

{% hint style="info" %}
When switching Service Providers the supplier calendar drop-down should be checked. The old and new suppliers may have a different Default calendar which may result in undesired changes to due dates.
{% endhint %}

Further aspects to be aware of include:

* Data is retrospectively changed for all Work Items, both running and complete. Depending on the number of Work Items in the system this may take a short amount of time to update in all views and reports.
* The Service Provider drop down is only shown when creating or editing Contracts if there are multiple Supplier companies in the system.

You can see what edits have been made to the customer and when, as well as when the customer was created, and even when a customer was deleted by clicking on the Show Activity button in the Edit screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWp-7aV_u7JtW856bvb%2Fimage.png?alt=media\&token=f5d96aad-5745-4aa8-b006-4469dadeb98c)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWp-ABzmDkRL167iFr4%2Fimage.png?alt=media\&token=dd97e627-fa4c-4899-97c1-ff7d47ada90e)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWozjnxDuAgIaxBAyOj%2Fimage.png?alt=media\&token=78e70149-b71c-4f3b-ad25-c9075bea987d)

You are also able to clone a contract by clicking on the Clone button in the Edit screen. This will clone all of the contract's settings apart from its name. You are able to make changes to any of the settings once the contract has been cloned.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXlL6td0YC_WekF49fg%2F-MXldkURjCqxuoyvOpF0%2Fimage.png?alt=media\&token=52bfbe4c-6521-41b3-b844-cdff021600d2)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXlL6td0YC_WekF49fg%2F-MXleb_AvX5kJJFXQN7n%2Fimage.png?alt=media\&token=ed458569-bf2a-466b-932b-d66fd24420a9)

{% hint style="warning" %}
Contract changes are versioned, so any changes you make to a Contract will only affect Work Items which are subsequently created. All existing Work Items will continue to use previous settings.
{% endhint %}

### Deleting a Contract <a href="#deleting-a-contract" id="deleting-a-contract"></a>

To delete a contract, click on the ellipses beside the Customer, hover over the delete link and click on 'Contract'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWozLv7lYVKZzS3IvE6%2F-MWp-0gdCL5p9XDe8bSj%2Fimage.png?alt=media\&token=c0930c63-8ad3-4bf3-b98a-3c7fc191d105)

If you delete a Contract which has linked [Email Routes](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes), you will be notified of this and will need to update the respective Email Routes in order to stop them from creating more work for this Contract.
