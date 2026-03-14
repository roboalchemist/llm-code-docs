# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/defect-parties.md

# Defect Parties

As part of [system-level settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings) you can add and edit defect parties, so that when a work item goes wrong, service agents can add defects against the parties at fault.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq25-LnWlv1WFp-ufq%2F-MWq36bHsjxir93ByUER%2Fimage.png?alt=media\&token=b66695a3-5d71-49d6-bbd0-71962edd99d1)

### **Configuring Defects** <a href="#configuring-defects" id="configuring-defects"></a>

To configure new or edit the migrated defects click the edit link on a Service Line and expand the new advanced settings.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq25-LnWlv1WFp-ufq%2F-MWq3C7clxrFTvZlHEIz%2Fimage.png?alt=media\&token=e058e232-9294-42de-9c8d-3c3f46b390d8)

Here you can configure up to three levels of defect categories, and you can even mix-and-match some that are only a single level while others have multiple levels.

The defects applied to a Work Item is shared with any related Cases/Tickets and Actions (just like Custom Data, Files, Contacts, etc). So a defect added to an Action will also show on its parent Case. If that Case was launched by a Ticket then they would also show on that Ticket. Likewise if a Defect is added to a Ticket then it shows on the Case if one is launched from it.

When editing a defect category, you are also able to see its activity history by clicking on the Show Activity button. You can see when the defect category was created and by who, as well as if any edits have been made to the defect category, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq25-LnWlv1WFp-ufq%2F-MWq3GtQvTsvLGsjPH4C%2Fimage.png?alt=media\&token=59e110dd-4ee3-426d-abbc-9ffd6ebe70ed)

Defect Parties can be localised and managed in the [Localisations page](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations).

### **Warehouse aspects of the Defects changes:** <a href="#warehouse-aspects-of-the-defects-changes" id="warehouse-aspects-of-the-defects-changes"></a>

* In the data warehouse only the ‘hidden’ value was exposed with no way of getting the Display Value. Now there is just a single value defined.
* The warehouse contains the Defect Categories even if they are not referenced by a Work Item yet.
* The warehouse contains the localised Display Values in the usual Localisations table
* See separate “Breaking Changes” document for technical details of the new Warehouse database structure.

### **Migration of Defects data** <a href="#migration-of-defects-data" id="migration-of-defects-data"></a>

* Defect Categories that are on a Case OR Ticket are migrated to a single list on the Service Line – **this should be validated manually after the migration has been completed**.
* Note for customers migrating from version prior to v2019.4: Some customers may have some misconfigured Defect Categories created in older versions of the product. For example, it may be that they have have a Defect Categories of ‘(Select)’ which incorrectly does not have a value defined ending in ‘.Blank’ (perhaps a typo of ‘,Blank’) – as such this would be considered a valid category for the user to select in 2019.3 and below, and so this will be migrated over to later versions as a valid defect category. Customers may wish to correct or delete such unwanted defect values, something which can easily be achieved in Enate Builder.
