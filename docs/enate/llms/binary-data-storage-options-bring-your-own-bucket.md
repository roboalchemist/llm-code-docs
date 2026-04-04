# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/administration/binary-data-storage-options-bring-your-own-bucket.md

# Binary Data Storage Options - 'Bring Your Own Bucket'

Binary storage is utilized for storing large files. At Enate, we employ it to store raw communications, communication attachments, files attached to work items, and files exported from Advanced Search views.

Enate is always provisioned with the primary binary storage configured in an Enate Azure tenant. You can see details of your Binary Storage locations in the 'Azure Binary Storage' section of the System Settings in Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFeBdAZ3cal1IJiY2bvGf%2FAzure%20Binary%20Storage.png?alt=media&#x26;token=c8771b01-5246-464d-8463-f6dfa4d9220c" alt=""><figcaption></figcaption></figure>

However, you can if you wish choose to change where your binary data is stored, and switch this to be your own Azure tenant.

{% hint style="info" %}
Important note: Changing your Binary storage location will not transfer your existing data to the new location. You should exercise extreme care when making this change, in order to avoid irrevocable loss of binary data.\
**You should contact Enate's Customer Success team if you wish to make such a change, so the activity can be carried out with our team's advice.**
{% endhint %}

### Information on Creating Storage Locations

To enable this feature of setting your own storage locations, you will need to perform activities outside Enate as well as within this section of Builder. You will need to do the following:

* Create two Azure Storage Accounts in two separate Azure Regions within your Azure tenant. We recommend that one of these regions is Europe West to maximise performance.
* Create an Azure App Registration that is granted access to these storage accounts.
* Configure Enate to use these storage accounts rather than the Enate Default.

{% hint style="warning" %}
NOTE: If your organisation is not proficient at managing Azure storage then you should **NOT** adopt this option. Deletion or corruption of data in these storage accounts will result in immediate and irrevocable data loss.
{% endhint %}

### Adding Details of your Azure Binary Storage Location in Enate

To add a new Storage Location in Enate, click the '+' icon in the Azure Binary Storage section in Builder's system settings. This will show a popup where details of the new Storage location you have set up in Azure should be entered:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTm3pkccHqk3RVgWMKZXz%2FLocation%20Popup.png?alt=media&#x26;token=206ac43d-66a7-4a3c-bb4e-de5148bfcda6" alt=""><figcaption></figcaption></figure>

The general data asked for is as follows:

| Item                               | Details                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                               | A Name for this Binary Storage Location                                                                                                     |
| Description                        | A Description for this Binary Storage Location                                                                                              |
| Primary Endpoint                   | The first Azure storage location primary endpoint URL                                                                                       |
| Secondary Endpoint                 | The second Azure storage location primary endpoint URL                                                                                      |
| Container Name                     | The exact container name of first Azure storage account. NOTE: both the first and second storage account must have the same container name. |
| Key Size                           | This will be used to encrypt and decrypt binary data.                                                                                       |
| Encryption Key (plus Confirmation) | This secret key will be used to encrypt and decrypt binary data.                                                                            |

{% hint style="info" %}
**Important Note: Once you set the encryption key and key size here, they cannot be changes. You must ensure that you securely save the encryption key as it cannot be modified later.**
{% endhint %}

In addition to these General settings, there is also information to fill in on the Azure details tab:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6h3xIrqAyrfJroVq5HRg%2FBIn.png?alt=media&#x26;token=fd87d8d8-4942-4517-a032-b79fe8c1cb0f" alt=""><figcaption></figcaption></figure>

| Item                                                 | Details                                                                                                                                                  |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tenant ID or Domain                                  | Get this from the registered app 'Host Name' in the overview menu in Azure                                                                               |
| Application ID                                       | Get this from the registered app 'Application (client) ID' in the overview menu in Azure                                                                 |
| Authentication with Certificate / with Client Secret | You can generate a secret in the Azure app registration certification and secret section, however Enate  recommends using the Certificate approach here. |

### Creating / Uploading a Certificate

You can generate Certificates or upload an existing on by selecting the 'Authentication ith Certificate' option on the Azure details tab. This will bring up a further popup to allow you to generate or upload a certificate:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDzwYwm7X7hfKA65Zj3zs%2FConfCert.png?alt=media&#x26;token=4150f67a-a40b-4295-8114-5958a63c92e8" alt=""><figcaption></figcaption></figure>

If you fill in the Subject here and click on Submit, a certificate will be generates and you will be given a Download link to allow you to download the public key certificate.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDOZulSX7o21biVzvWX2c%2FBInred.png?alt=media&#x26;token=eea50e81-fe0a-4ce7-aea3-fbaab36a7e8f" alt=""><figcaption></figcaption></figure>

You should upload this Certificate in the Azure app registration 'certificate and secret' section.

Note: You need to make sure that you upload the certificate / create the secret in Azure App Registration before saving, as the configuration will not save until it can successfully test that all the information provided is correct.

Alternatively you can Upload an existing certificate if you have one.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLX5yTkjfzyRCcIwQBDKf%2Fupload%20cert.png?alt=media&#x26;token=81171584-e125-4d73-b6a4-1f0f1cc5d5b4" alt=""><figcaption></figcaption></figure>

Once you have entered all required information you can Test your connection and, once successfully tested, save it.

### Changing your Binary Storage Location

Once you have successfully created your own Azure storage locations and linked it to your Enate instance, yo can choose to set that location as your primary storage location. You will be met with a popup asking you to confirm your decision, and reminding you that your existing data will NOT be automatically transferred to the new location.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC6q84DLZXrAwsHgrfE44%2Fconf.png?alt=media&#x26;token=a37cb3f6-c55e-4e91-b872-330b48774d42" alt=""><figcaption></figcaption></figure>

### Controlling Access to Binary Storage Feature

Access to being able to modify these settings should be tightly controlled. Access is managed via the 'Binary Storage' access option within Builder User Roles setup, under the 'Edit System Settings' section:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXgy59BC183wYMPQJsdYe%2FBRole.png?alt=media&#x26;token=f82441a3-0502-4405-9647-98078f22074f" alt=""><figcaption></figcaption></figure>

### Important Points / Limitations regarding Binary Storage Locations

When dealing with storage locations and encryption keys for Binary data, there are a number of important points to keep in mind:

* Only one single Binary Storage location can be active at one time.
* You cannot be make any updates to or delete any Enate-managed Binary Storage.
* The Encryption Key and Size cannot be changed after creating
* While you *can* switch between binary storage configurations, this will NOT automatically migrate any of your existing data, so you must exercise extreme caution when choosing this option.
* You can only delete a Storage location if that configuration has yet to ever be used (And you cannot do this at all with any Enate-managed storage locations).
* Management of your Certificates / Secrets with regards to e.g. expiry of these is completely managed be you, and no management of these is provided by Enate. &#x20;

{% hint style="info" %}
**To reiterate: If you are thinking of changing you Binary Storage location settings, we stringly recommend that you contact Enate's Customer Success team, so the activity can be carried out with our team's advice.**
{% endhint %}
