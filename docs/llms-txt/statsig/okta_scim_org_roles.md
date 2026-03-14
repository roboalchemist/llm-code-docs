# Source: https://docs.statsig.com/access-management/scim/okta_scim_org_roles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta SCIM Org Roles

## Update Okta User Org Role

For every user, Statsig surfaces a SCIM field named `statsigOrgRole`. Through this field, you can manage organization user roles.
Currently, Okta can only push role updates to Statsig. We currently support the following org roles: `Member` `Admin` `Owner`

### Step 1. Create the Custom Attribute in Okta

Navigate to `Directory > Profile Editor` and select the User (default) Okta profile. This represents all of the Okta users' attributes.
Scroll down and press `Add Attribute` and fill out the new attribute to have the variable name `statsigOrgRole`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step1.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=0c03263f1314761e8c0b53b63019376f" alt="Okta profile editor showing custom statsigOrgRole attribute being added" width="1396" height="1514" data-path="images/okta_scim_steps/org_steps/step1.png" />
</Frame>

### Step 2. Create the Custom Attribute in the Statsig SCIM Integration

Now Navigate to the `Statsig SCIM Integration's User Profile` in the `Profile Editor`.
Add an new attribute that matches the following format:

* Variable name: `statsigOrgRole`
* External namespace: `urn:ietf:params:scim:schemas:core:2.0:User`
* Attribute type: either `Personal` or `Group`, depending if using groups for app assignment

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step2.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=b2d6cd8e21a525a782ee1e849480971a" alt="Statsig SCIM integration user profile with statsigOrgRole attribute definition" width="1292" height="1954" data-path="images/okta_scim_steps/org_steps/step2.png" />
</Frame>

### Step 3. Create a Mapping from Statsig to Okta for the Custom Attribute

On the same Statsig SCIM profile editor, navigate to the `Mappings` button.
Scroll down to the new attribute `statsigOrgRole` and map `user.statsigOrgRole` to the Okta attribute `statsigOrgRole`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step3.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=7aa58de1925196152896db257dd619a0" alt="Okta mapping editor linking statsigOrgRole between Statsig and Okta profiles" width="2004" height="830" data-path="images/okta_scim_steps/org_steps/step3.png" />
</Frame>

### Step 4. Create a mapping from Okta to Statsig for the Custom Attribute

Now navigate to the Okta User to Statsig SCIM user mapping.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step4_1.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=e13c9eadf2b2ed62c5a50bee1c6c07c5" alt="Okta to Statsig user mapping screen for statsigOrgRole attribute" width="1930" height="614" data-path="images/okta_scim_steps/org_steps/step4_1.png" />
</Frame>

Scroll down to the `statsigOrgRole` attribute and map `user.statsigOrgRole` to the Okta attribute `statsigOrgRole`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step4_2.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=f4d6d88ecad2ad2d2d9587bea29fc95a" alt="statsigOrgRole attribute mapping row pointing from user field to Okta attribute" width="1822" height="522" data-path="images/okta_scim_steps/org_steps/step4_2.png" />
</Frame>

Now all users will be synced with their organization role. On the Statsig SCIM integration you can modify a user's role directly as well.

### Step 5. Modify Integration Mappings

Navigate to the Statsig SCIM integration provisioning section.
Under the "To App" tab, scroll down to the `statsigOrgRole` attribute.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step5_1.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=97f468aa63d8d644adbbcd6409f3235d" alt="Provisioning To App tab showing statsigOrgRole attribute settings" width="1394" height="480" data-path="images/okta_scim_steps/org_steps/step5_1.png" />
</Frame>

Set the attribute value to `Map from Okta Profile` and `statsigOrgRole`.
Set apply on `Create and update`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step5_2.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=0cf0bd278b9a42088036a2da9f697a98" alt="Set value dialog choosing Map from Okta Profile for statsigOrgRole" width="1548" height="622" data-path="images/okta_scim_steps/org_steps/step5_2.png" />
</Frame>

Navigate to the "To Okta" tab and scroll down to the `statsigOrgRole` attribute.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step5_3.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=b85acf794d0fbed936d25261cf7c149d" alt="Provisioning To Okta tab listing statsigOrgRole attribute" width="1386" height="456" data-path="images/okta_scim_steps/org_steps/step5_3.png" />
</Frame>

Set the attribute value to `Map from Statsig Profile` and `statsigOrgRole`.
Set apply on `Create`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/org_steps/step5_4.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=f72387f01b696779f3a772afa37b04b3" alt="Set value dialog mapping statsigOrgRole from Statsig profile back to Okta" width="1548" height="526" data-path="images/okta_scim_steps/org_steps/step5_4.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).