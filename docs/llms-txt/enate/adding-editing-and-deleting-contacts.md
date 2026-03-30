# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/adding-editing-and-deleting-contacts.md

# Adding, Editing and Deleting Contacts

## Adding Contacts

External contacts can be created in Enate in several ways.

### **1) Automatically from an incoming email**

The Enate system can be set to automatically create new external Contact records when incoming emails arrive which contain new email addresses if the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

The system will auto-populate the first name and last name of the contact based on the email display name. More specifics on this:&#x20;

* If there is a space in the email display name, anything before the first space will be used as the contact's first name and anything after the last space will be used as their last name. For example, if the email display name is 'John Smith' then the contact's first name will be auto-filled as 'John' and their last name will be auto-filled as 'Smith'.
* If there is a comma in the email display name, anything before the first comma will be used as the contact's last name and anything after the comma but before the space will be used as their first name. For example, if the email display name is 'Smith, John' then the contact's last name will be auto-filled as 'Smith' and their first name will be auto-filled as 'John'.
* If the system can't auto-fill the first name and last name with confidence, then the contact will be auto-created without a first and last name and the user will be prompted to fill this themselves when they submit the work item.

Additionally the [company set](#company-name-external-contact-scoping) to an auto-created contact will depend on the [contact scope setting in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). If it's set to 'Global', or 'Global and Local', the auto-created contact will have a Global scope, i.e. not linked to any specific company.  If it is set to 'Local', the auto-created contact will be created under the company that the related Work item exists under.

### **2) Adding an individual contact from the Contact Management page**&#x20;

You can add contacts from the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) by clicking on the Create Contact icon and filling out the details for the contact in the resulting popup.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK62ZZNAWwA6Gs8trMXXj%2F7%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=d4a08dc8-4439-4fbb-a257-a8e4a72fec07" alt=""><figcaption></figcaption></figure>

### **3) Importing contacts to the Contact Management page from an Excel template**

You can import a list of contacts from an Excel spreadsheet in the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page). A template is provided and the template is supported in all of the languages that Enate offers.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtwXbX4m1KzyOayzQnRHh%2F7%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=f67af277-5f68-49e3-8a46-a64fd9aacaa6" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
It is mandatory to fill in the email address when importing Contacts from an Excel template. If you don't specify a company, the contact will automatically be set to global. See here for more information about [company scoping](#company-name-external-contact-scoping).
{% endhint %}

### **4) Adding a contact from Quickfind**

If you are searching for a new contact which does not currently exist in the system, you can create a new contact from [Quickfind ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind)itself. Navigate to the people search function in Quickfind and click on ‘add a contact’.

When you click on ‘add a contact’, the system will decode and auto-populate the first name, last name and email address. Once you fill in all the information and click on create, you will be taken to  the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of the new contact.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Note: The contact email address must be unique in the system.
{% endhint %}

### **5) Adding a contact from the Contacts Card of a Work Item**

You can also create a new contact from the [contacts card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) a work item. When you search for a user in the contacts card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0LlSloVJ3b9h0UndDyZ9%2F7-Create-Contact-from-Work-Item.gif?alt=media\&token=fe7d24c4-1b2b-4f38-a480-524d59f6e5fa)

{% hint style="info" %}
Please note that if you create a new contact in test mode, that contact will only be available for running test packets in the system.
{% endhint %}

## Automatic vs Manual Contact Creation

You can see if an external contact has been automatically created by the system or manually created by a user by looking at the 'Auto-Created' column in the [Contact Management Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/contact-management-page#b-configuring-grid-settings).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe7d4RTbYmrBWAIk5QaEz%2Fimage.png?alt=media\&token=513bd818-d217-42d4-9c2d-8e6f29ccea4f)

{% hint style="info" %}
Please note that once a contact that auto-created has had edits made to it, it will no longer display as an auto-created contact in the 'Auto Created' column of the Contact Management Page.
{% endhint %}

## Company Name - External Contact Scoping

Depending upon how it has been configured in Builder, you will have various options when assigning a company to an external contact:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4e1NkPn732m2IQnJpK6P%2F7-Company-Scope.gif?alt=media\&token=58472a1a-c708-408d-b6ca-9041e4aa0b3a)

* **All Companies/Global**&#x20;
  * Setting the company to this means that external contact can create and access work items for all companies.
  * It also means that work manager users are able to search for other all external contacts on a work item.

{% hint style="info" %}
Please note that this setting is only available if the External Contact Scope has been set to 'Global' or 'Global and Local' in Builder. See [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#contact-scope)for more information.
{% endhint %}

* **A particular company (local)**
  * Setting the contact scope to a particular company means that external contact will only be able to create and access work items for that particular company that the external contact has been associated to.
  * Users will also only be able to add a Contact to a Packet API if the Contact is in the same Company (or is in an umbrella Company).

{% hint style="info" %}
Please note:&#x20;

1. It is only possible to change the associated company of an external contact from All Companies/Global to a particular company (local) if the external contact is not associated with work items from multiple different companies. You can change this by reassigning the Contact on a work item.&#x20;
2. To scope external contacts to Global/All Companies the Company column in Bulk Upload file should be left blank so by default the contacts will be scoped to Global.
3. The company set to an auto-created contact will depend on the contact scope setting you have set. If it's set to 'Global', or 'Global and Local', the auto-created contact will have a Global scope, i.e. not linked to any specific company.  If it is set to 'Local', the auto-created contact will be created under the company that the related Work item exists under.
   {% endhint %}

### Impact of Global / Local Scoping on linking Contacts to a Work Item

{% hint style="warning" %}
Please note that if an External Contact is scoped locally (i.e. is linked a specific Company), you cannot add them as a contact for a work item which exists within another company.  This is also true for Agent accounts (which must *always* exist under a specific Company). ONLY Globally scoped External accounts have the flexibility to be linked as contacts to work items in any Customer.
{% endhint %}

## Editing a Contact

To edit a contact, go to the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) and double click on the contact to bring up the Edit Contact popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5KzvJfKILnLTcBggLbMR%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=96c83c98-057d-42f9-b311-93f2fdd41cf7)

You are also able to bulk edit the company, time zone, office location, preferred language and default tag of your contacts by selecting on the contacts' tick boxes - click on the Edit button which will appear to display the Bulk Edit popup. Set details as desired and hit Confirm to save bulk changes.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxKdZIM6sgHA9p4VcRwN9%2F7-Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=7c70b227-0e28-48a7-8735-0644bd1e0123)

## Deleting a Contact

To delete a contact, go to the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) and click on the contact's tick box and the delete button will appear. You are able to delete multiple contacts at once.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4jCq5IAIW63mMiAcyeke%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=9fad9700-bc29-4872-8f12-0b28e6f78c49)

## Contact Scope vs. Permissions

It is important to take your user permissions into account when understanding which Contact records you are able to see, depending on the Global / Local scope setting which has been made in Builder:

{% hint style="info" %}
**Please note:** \
**- Locally-scoped contacts are visible to you in if you have permissions specificallly on that contact's company, or parent companies. If you don't have such permissions, you will not be able to see the contact record.** \
**- Global contacts are visible to all users.**
{% endhint %}

## Creating Contacts in Test Mode

Enate supports the creation of separate Contact records in Test Mode, i.e. any contact records you create in Test mode will be accessible only to Test Mode users (and contacts created in live mode will be accessible only to Live mode users). This helps to ensure that emails from test work items are not accidentally sent to production users, and vice versa.

### Warning - Do Not Use Production Email Addresses when creating Test Contacts

{% hint style="warning" %}
**IMPORTANT:** Do NOT create Test Contact records using information (specifically email address) for people you will be using in normal production. **If you create a Contact record while you are in Test mode this will be created as a Test Contact, and ALL emails arriving into the system from that email address will create a Case/Ticket in Test Mode.** This would result in incoming production emails creating work test work items which would not be visible by production users.

If you have created a production Contact record as a Test Contract record in error, you should edit the Test contact by changing the email address, then switch back to normal production mode to create the desired normal Contact record.
{% endhint %}
