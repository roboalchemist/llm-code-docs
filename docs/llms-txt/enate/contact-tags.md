# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags.md

# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-tags.md

# Contact Tags

Contact tags are used to link contacts to work items.

## System-Default Tags

The system-default Contacts Tags that are available are:

* **Primary Contact** – the main person you are dealing with for this query. There can only ever be one Primary Contact for a work item. This is mandatory for a Ticket. Depending on Case configuration in Builder, this may or may not be mandatory for a Case (if set as mandatory for Case type, is also mandatory for that Case’s Actions).
* **Original Requester** - the person who initially raised the request. There can only ever be one Original Requester for a work item, and it is independent to the 'Requester' tag. The original requester will be either automatically set in the situation where a valid contact sent in the email that started the work item, or the first person who gets manually set as the ‘requester’ will be promoted to ‘original requester’. The Original Requester tag cannot be changed once it has been set and you cannot remove the contact tagged as the original requester from the work item.
* **Requester** – the person requesting the query. There can only ever be one Requester for a work item. This is mandatory for a Ticket. Depending on Case configuration in Builder, this may or may not be mandatory for a Case (if set as mandatory for Case type, is also mandatory for that Case’s Actions).
* **Subject** – who the work item is about (this may be neither of the above). There can only ever be one Subject for a work item.

Very often all three will be the same person. If you tag another contact as any of these system-default relationship types, the tag will be removed from the previous contact - as there can be only one holder of the system-default contacts in one work item.

When you manually add the first contact to a work item they will be set as the Primary Contact, Requester and Subject by default. You can manually reassign these tags to other users afterwards.

* CCs – any further contacts which can be copied on any correspondence. When a contact is tagged only as ‘CC’, it will be displayed in the separate CCs section (hidden until any CC-only contacts exist on the work item.

## Setting additional Default Tags on a Contact Record

In addition to the system-default Contact Tags (Primary Contact, Subject, CC, Requester), you can add a further default contact tag to a contact record to make using contact tags on work items faster and easier.&#x20;

Example: If you know that 'Jane Smith' is always going to be the Broker or any work item you add them to as a contact, you can give Jane's Contact record a default tag of 'Broker' so it gets auto-populated for her in the work item - rather than you having to manually set this tag value each time.

The Default Tags list available to choose from is set in Builder in the [General Settings >> Contact Tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags) section. &#x20;

You can set this Default Tag whenever you add a new contact into the system.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcIJqqZIZBtMkAQf7AMzo%2Fimage.png?alt=media\&token=f611c6da-530a-4210-a855-2cb31d205937)

You can also add the tag to existing contacts and edit the Default Tag set to a contact via the Contacts page.

The Default Tag attribute is also available to edit in bulk, i.e. you can set this for multiple contacts at one time - simply select a number of contact records from the Contacts page grid and click on the Edit button to access the Bulk Edit popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1vGyg20nHkJq744dxTq2%2Fimage.png?alt=media\&token=e6094bcc-5d65-4af9-98a7-9f8c7c40785c)

### Default Contact Tag behaviour if set not to 'Allow Multiple'

If a specific tag value has not been set to 'Allow Multiple', only one contact in a Work Item is allowed to have the value. Example: it may be that there can be only a single 'Broker' contact for Ticket. This obviously impacts default tagging if two contacts with the same 'must be unique' Default Tag get added to a work item, either manually or automatically. In this scenario the system will allocate the Default Tag to only one contact (and therefore remove the Default Tag for the other contacts). The system will allocate to the Contact already tagged with an existing *other* tag value, in the following priority order.

* Primary Contact
* Requester
* Subject
* CC
* Any other contact on the work item

### **Additional notes about Supplier Company mismatches with Contact Tags:**&#x20;

* You will not be able to add a Default Tag to a contact if the company they are assigned to has a different Supplier Company to the Default Tag.&#x20;
* You will not be able to submit a work item with a contact whose Default Tag is set to a different Supplier Company than the work item.

## Auto-tagging of Contacts in Work Items <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

### Contacts populated from an initial email <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

#### Known Contacts

When an email arrives from an address which is associated with a contact that is already in the system and the contact:

* has a Global scope setting, or&#x20;
* they have a Local scope setting but belong to the same company that the work item will belong to based on email routing rules

then their details are automatically populated into the Contacts Card when the work item is created by the system and they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. Additionally, if they have a default tag assigned to them, they will also be tagged as that. However do note that you can always go in and manually edit the tags yourself once the work item has been created.

When an email arrives from an address which is associated with a contact that is already in the system, but they have a Local scope setting and belong to a *different* company than the one the work item will belong to based on email routing rules, their details will NOT be automatically populated into the Contacts Card when the work item is created by the system, (and therefore they cannot be automatically tagged to the work item). Note that you can always go in and manually edit the contact and tags yourself once the work item has been created.

#### Unknown Contacts

*Default 'Global' or 'Global & Local' Scope*

When an email arrives from an unknown address and:

* &#x20;the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) and&#x20;
* your system has been configured to set the scope of your external contacts to '**Global**', or '**Global and Local**',&#x20;

then the contact will be auto-created, have a Global scope (i.e. the won't be  linked to any specific company) and their details will be automatically populated into the Contacts Card when the work item is created by the system. Additionally, they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. As they were previously unknown to the system, they will have no default tag set. Note that you can always go in and manually edit the tags yourself once the work item has been created.

*Default 'Local' Scope*

When an email arrives from an unknown address and

* the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) and&#x20;
* your system has been configured to set the scope of your external contacts to '**Local**',&#x20;

then the contact will be auto-created, have a Local scope (i.e. they will be  linked to a specific company) and they will be created under the company that the work item exists under. Their details will be automatically populated into the Contacts Card when the work item is created by the system and they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. As they were previously unknown to the system, they will have no default tag set. Note that you can always go in and manually edit the tags yourself once the work item has been created.

*Automatic Contact Creation OFF*

When an email arrives from an unknown address and&#x20;

* the ['Enable Automatic Contact Creation' setting is set to OFF in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation),&#x20;

then the work item will be created based on the email routing rules, but the email sender's details will NOT be automatically populated into the Contacts Card when the work item is created by the system, (and therefore they cannot be automatically tagged to the work item). Note that you can always go in and manually edit the contacts and tags yourself once the work item has been created.

### Contact tags populated from the Contact Activity Page <a href="#contacts-populated-from-contact-activity-call-handling-page" id="contacts-populated-from-contact-activity-call-handling-page"></a>

When a work item is created from the 'Start work item' button on the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of a contact, that contact will be auto-tagged as the Original Requester, Requester, Subject and Primary Contact of the work item, and their Default Tag will be added too (if they have one).
