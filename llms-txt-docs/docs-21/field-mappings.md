# Source: https://docs.unifygtm.com/reference/integrations/salesforce/field-mappings.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/field-mappings.md

# Field Mappings

> Understand how to configure and use HubSpot field mappings in Unify.

# Overview

Unify can sync data between HubSpot objects and Unify objects. However, the
exact fields in HubSpot differ from Unify, so Unify needs to understand how to
sync data between the two systems. This is done using *field mappings*.

# Setup

### Change field mappings

When you first connect your HubSpot instance, Unify will automatically prepare
the field mappings for you. If you use any custom properties in place of
default HubSpot properties, you may want to update the mappings before Unify
starts syncing data.

In the [HubSpot integration settings](https://app.unifygtm.com/dashboard/settings/integrations/hubspot),
look for the **Company**, **Person**, and **Email Message** field mappings at
the bottom of the page. Select one to view and edit the field configuration.

<Frame caption="Customize which fields are synced to and from HubSpot.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ac67ac0a544b106dc1dc157b1c65f21e" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/company-field-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e0e5a21f398d430674ff089354662e25 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1dd74350c864f98fa2eecbb025a130bd 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2564067d541a2e16a8af2b797d3ebb4 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=95da33ae2b2935818aaa2e745bf8b7a4 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ba22a3e6a3cdba653fe401c8dd386aea 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=692ab57c15caa7b4dc11082a3c919650 2500w" />
</Frame>

You can return to update these mappings any time in the future, so you don't
need to worry about getting them perfect right off the bat!

### (Optional) Create custom properties

You can write values to default properties and custom properties. In order to
write to custom properties, they must already exist in HubSpot.

While some of the fields Unify can write exist as standard properties in
HubSpot, many of them do not. In particular, Unify-specific fields (like the
name of the Sequence a person was enrolled in) do not exist in HubSpot by
default. In order to write these values to HubSpot, you will need to create
custom properties before mapping them.

<Note>
  Here's what the process looks like for adding **Contact** properties. First, in
  HubSpot, navigate to **CRM -> Contacts**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bcc0b056e9ca14a99f444d9de2ae07f7" alt="HubSpot Home" data-og-width="3626" width="3626" data-og-height="1690" height="1690" data-path="images/hubspot-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=82a9120918278b8e6350bf7da19f3475 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e657714152d25702d61d971c63e492c1 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=edb8c0622a7233009af44f28f6b1e04f 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=52f7714574c3cf485621d2f2864a4e83 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d177efe241afc4b91b6cf6494c0c0989 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=936f43f82639054fcab46b88ed2e89eb 2500w" /></Frame>

  Select **Actions -> Edit properties**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ce62a906f1697fa03aa461fbf8352de9" alt="HubSpot Contacts" data-og-width="3634" width="3634" data-og-height="1688" height="1688" data-path="images/hubspot-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=16f5d32d0827f6fb0bedede76ccd262c 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=74c1d1cf0af3adedbb62fba8a60fa843 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=67a3420481cf392ed34e6190e73873c0 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d3912c8a76ec048296af86c08d2b3f7f 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=42af62484900fb5da5b08b73670ce5eb 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fde74d0f80dfccc586c127374148936c 2500w" /></Frame>

  Navigate to **Groups -> Create group**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b219405e8e5bc293f4e443a9387628bd" alt="HubSpot Contact Property Groups" data-og-width="3628" width="3628" data-og-height="1686" height="1686" data-path="images/hubspot-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=98e87d67d6a782471fb0e2ea9863c334 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5285e69071a189046008b3cd1898b084 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d2fffbed30b7f26fe22b2a6e95a7458a 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=29e326dd7fca3f1dbbadb64a3a3d07eb 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=620a28ca8b6c4079a0a1ee78d047a038 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5fbc70114fdcf74ae29bce180d0ae375 2500w" /></Frame>

  Type in the name of the group (recommended title "Unify information") and click
  **Create**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=df07eed5693cf547cebc6a00c84d45e0" alt="HubSpot Contact Create Property Group" data-og-width="3626" width="3626" data-og-height="1678" height="1678" data-path="images/hubspot-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2b055d160606f353ba121c583faf56ff 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=098fd2f6be5d78c49a1f24be4374b635 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2008ceeb0d75c6ad2428e3761a51b39b 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9bda2be9897274817bf910a2a9dda4da 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0837ff32041c5c06543a023520fc3624 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2c7d01028d50244fb4cfd43c90f91401 2500w" /></Frame>

  Navigate to **Properties -> Create property**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=829423a8d2b2402434a2db732ac9118f" alt="HubSpot Contact Properties" data-og-width="3628" width="3628" data-og-height="1686" height="1686" data-path="images/hubspot-11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=00564d38f28cd6a719d1e7ff4600f7ee 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1d30aa1d153d152c5b23d56adb27894c 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e64fdba91fe6bc3a8b4644e47492a496 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=864dfbde6ac3cdc2bff508d9c6cc1500 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c0b8a3309db92d23b7987a12e374675b 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e55593cb76d3c4480e77d3e96fa7f26f 2500w" /></Frame>

  When editing the property details, make sure the **Object type** is set properly
  (in this case, to **Contact**) and the **Group** is set to the group you
  created earlier. You can fill in the **Label** and **Description** as desired.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=176a486a4bc99e29f4b12f1b864418e7" alt="HubSpot Contact Create Property" data-og-width="3630" width="3630" data-og-height="1764" height="1764" data-path="images/hubspot-12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5406599c54ae95bc1f0183c6cd7cc63b 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bff618afc94938ace22c020cd86ac483 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8b240ce98e6293570259a67d461334bc 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=70a13b2233b5fd7568d8d5b7e4cdf28e 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9281935ca33a61c437c6149e66a4b65e 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=65169ae5b6fb350ea4c400003d922606 2500w" /></Frame>

  Lastly, select the **Field type** and click **Create**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=48ac7a78694a745bbfbe0d04cdc75077" alt="HubSpot Contact Select Property Type" data-og-width="3628" width="3628" data-og-height="1766" height="1766" data-path="images/hubspot-13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0eb6e01b65c82d53b71a5c98d1551ef7 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=3d78ee498385afd451dcb0184caabf76 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aaf15f9d8f6c7c9d0e2479792a757747 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=17179480eb1fbcb2c7efc868d5545433 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6aac265a632464b4152e4349a49a91dc 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aa129f35c0d782c0dea63dce3d53663c 2500w" /></Frame>

  This is what your **Contact** properties filtered to your new group might look
  like after you've added them:

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ab7f38574fd82ed1a8015ebedfba3c72" alt="HubSpot Contact New Properties" data-og-width="3626" width="3626" data-og-height="1762" height="1762" data-path="images/hubspot-14.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a0263c59aeee4984f01a6f1f24d38c39 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=95124d0a0b28d9d27df5d17004f50bb7 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4b7436649d97bca731c47709d46ee06a 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=010a11b95995e0d3a23ca840889adafc 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7e848f087f2e6ac2838881ca4d3b3b05 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=93fa187b24b20474165bfe69ee68b495 2500w" /></Frame>

  You can then repeat this process for **Company** properties as well.
</Note>

# Available fields

Below is a full list of the values that can be configured in the field mappings
for each object type. Some of these are standard properties, while others
provide Unify-specific information, such as the name of the Sequence that a
person was enrolled in.

<AccordionGroup>
  <Accordion title="Companies">
    | Field                                  | Description                                                                                                                                                       |
    | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Company Name**<br />*Text*           | Name of the company.                                                                                                                                              |
    | **Domain**<br />*Text*                 | Web domain of the company.                                                                                                                                        |
    | **Address**<br />*Text*                | Physical address of the company.                                                                                                                                  |
    | **State or Province**<br />*Text*      | State, province, region, or territory the company is located in.                                                                                                  |
    | **Country**<br />*Country*             | Country the address is located in.                                                                                                                                |
    | **City**<br />*Text*                   | City, town, or village the company is located in.                                                                                                                 |
    | **Postal Code**<br />*Text*            | Postal code for the company.                                                                                                                                      |
    | **Time Zone**<br />*Text*              | Time zone the company is located in.                                                                                                                              |
    | **Corporate Phone**<br />*Text*        | Corporate phone number for the company.                                                                                                                           |
    | **Status**<br />*Text*                 | Status of the company in the sales lifecycle.                                                                                                                     |
    | **LinkedIn URL**<br />*Text*           | URL to the company's LinkedIn page.                                                                                                                               |
    | **Description**<br />*Text*            | Description of the company.                                                                                                                                       |
    | **Do Not Contact**<br />*Boolean*      | Flag indicating that the company should not be contacted.                                                                                                         |
    | **Founded**<br />*Date*                | Date the company was founded.                                                                                                                                     |
    | **Industry**<br />*Text*               | Industry the company is in.                                                                                                                                       |
    | **Employee Count**<br />*Number*       | Approximate number of employees at the company.                                                                                                                   |
    | **Revenue**<br />*Number*              | Estimated annual revenue of the company.                                                                                                                          |
    | **Revenue Currency**<br />*Text*       | Three-letter ISO 4217 code indicating the revenue value currency type.                                                                                            |
    | **Account Source**<br />*Text*         | Channel this Company record was sourced from.                                                                                                                     |
    | **Unify Metadata**<br />*Text*         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date* | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text* | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Intent Level**<br />*Text*     | Intent level of the company (either **High**, **Medium**, **Low**, or **None**).                                                                                  |
  </Accordion>

  <Accordion title="People">
    | Field                                                  | Description                                                                                                                                                       |
    | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Email**<br />*Text*                                  | Contact email address.                                                                                                                                            |
    | **Address**<br />*Text*                                | Physical address of the person.                                                                                                                                   |
    | **Country**<br />*Country*                             | Country the address is located in.                                                                                                                                |
    | **Postal Code**<br />*Text*                            | Postal code for the person.                                                                                                                                       |
    | **Email Opt Out**<br />*Boolean*                       | Indicates whether the person has opted out of receiving emails.                                                                                                   |
    | **Status**<br />*Text*                                 | Status of the person in the sales lifecycle.                                                                                                                      |
    | **First Name**<br />*Text*                             | First name of the contact.                                                                                                                                        |
    | **First Name Suffix**<br />*Text*                      | Suffix of the first name of the contact.                                                                                                                          |
    | **Last Name**<br />*Text*                              | Last name of the contact.                                                                                                                                         |
    | **Title**<br />*Text*                                  | Job title or position of the contact.                                                                                                                             |
    | **Mobile Phone**<br />*Text*                           | Mobile phone number of the contact.                                                                                                                               |
    | **Work Phone**<br />*Text*                             | Work phone number of the contact.                                                                                                                                 |
    | **Corporate Phone**<br />*Text*                        | Corporate phone number of the contact.                                                                                                                            |
    | **LinkedIn URL**<br />*Text*                           | LinkedIn profile URL of the contact.                                                                                                                              |
    | **Do Not Call**<br />*Boolean*                         | Indicates whether the contact should receive phone calls or not.                                                                                                  |
    | **Do Not Email**<br />*Boolean*                        | Indicates whether the contact should receive emails or not.                                                                                                       |
    | **EU Resident**<br />*Boolean*                         | Indicates whether the contact is a resident of the European Union.                                                                                                |
    | **Lead Source**<br />*Text*                            | Channel this Person record was sourced from.                                                                                                                      |
    | **Last Activity Date**<br />*Date*                     | Date of the last activity or engagement with the contact.                                                                                                         |
    | **Unify Metadata**<br />*Text*                         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*                       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*                       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date*                 | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*                     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*                  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text*                 | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Most Recent Play At**<br />*Date*              | Date and time the most recent Unify Play ran on this record.                                                                                                      |
    | **Unify Initial Sequence**<br />*Text*                 | Name of the first Unify Sequence this person was enrolled in.                                                                                                     |
    | **Unify Initial Sequence At**<br />*Date*              | Date and time this person was first enrolled in a Unify Sequence.                                                                                                 |
    | **Unify Initial Sequence Step At**<br />*Date*         | Date and time this person first completed a step in a Unify Sequence.                                                                                             |
    | **Unify Most Recent Sequence**<br />*Text*             | Name of the most recent Unify Sequence this person was enrolled in.                                                                                               |
    | **Unify Most Recent Sequence At**<br />*Date*          | Date and time this person was most recently enrolled in a Unify Sequence.                                                                                         |
    | **Unify Most Recent Sequence Step At**<br />*Date*     | Date and time this person most recently completed a step in a Unify Sequence.                                                                                     |
    | **Unify Most Recent Sequence Status**<br />*Text*      | Status of the most recent enrollment for this person. The statuses shown on enrollments in Unify are the same values that will be written to HubSpot.             |
    | **Unify Initial Reply Classification**<br />*Text*     | High-level classification of the initial reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".          |
    | **Unify Most Recent Reply Classification**<br />*Text* | High-level classification of the most recent reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".      |
    | **Unify Initial Reply Tags**<br />*Text*               | Comma-separated list of classification tags of the initial reply received from a person. For example, "Ready to meet, Needs more information".                    |
    | **Unify Most Recent Reply Tags**<br />*Text*           | Comma-separated list of classification tags of the most recent reply received from a person. For example, "Ready to meet, Needs more information".                |
  </Accordion>

  <Accordion title="Email Messages">
    | Field                                | Description                                                    |
    | ------------------------------------ | -------------------------------------------------------------- |
    | **Universal Message ID**<br />*Text* | Globally unique identifier that exists for all email messages. |
    | **Subject**<br />*Text*              | Subject of the email.                                          |
    | **HTML Content**<br />*Text*         | Body of the email.                                             |
    | **Sent At**<br />*Date*              | Date and time the email was sent.                              |
  </Accordion>
</AccordionGroup>
