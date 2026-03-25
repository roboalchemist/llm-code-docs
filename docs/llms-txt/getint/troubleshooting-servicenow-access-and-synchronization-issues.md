# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/troubleshooting-servicenow-access-and-synchronization-issues.md

# Troubleshooting ServiceNow Access and Synchronization Issues

### Use Case

When integrating with ServiceNow, you may choose to restrict your dedicated user’s access to specific tables to enforce boundaries. However, overly strict limitations can lead to insufficient permissions, preventing Getint from retrieving data correctly and disrupting synchronization.

Out-of-the-box (OOB) modules installed via the Application Manager may require specific ACLs to be assigned to the dedicated user's role to access necessary tables and ensure proper syncing.

This guide walks you through how to grant the required permissions or troubleshoot common access issues that may appear during setup.

### Assign OOB Roles for Easier Setup

Base OOB roles can be assigned to your dedicated user to grant read, write, and create access to the **Incident**, **Problem**, and **Change** tables.

If you’re encountering access errors when syncing these work items and prefer not to assign the more extensive **ITIL** role, consider using OOB roles customized to your needs.

#### Understanding Roles in ServiceNow

Roles in ServiceNow can inherit other roles, which helps with permission management. You can view these associations by navigating to:

**System Security** > **Users and Groups** > **Roles**

Locate a specific role and click to see inherited roles in the **Contains Roles** tab.

Additionally, roles can include specific ACLs to grant change permissions and access to various tables.

### Role Access Breakdown

#### Incident

* **sn\_incident\_read** Grants read access to Incident records.
* **sn\_incident\_write** Enables creation and editing of Incident records.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdG1osNSJGgfe9z1ZYINE%2FRole%20SN%20Incident%20Read.png?alt=media&#x26;token=a84984be-42cf-4664-959a-8f171fb99bc1" alt=""><figcaption><p>sn_incident_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQZCU26wpSPbA9Kv1H9xl%2FSN%20Incident%20Write%20ServiceNow.png?alt=media&#x26;token=84ca24d0-228d-4c60-ba51-431e0b2bd2ba" alt=""><figcaption><p>sn_incident_write role</p></figcaption></figure>

#### Change

* **sn\_change\_read** Provides read access to Change records.
* **sn\_change\_write** Allows creation and modification of Change records.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsBI4499sccBcEdNtAwKE%2FSN%20Change%20Read%20ServiceNow.png?alt=media&#x26;token=34a8787d-2afc-42ee-a750-978e491fb182" alt=""><figcaption><p>sn_change_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLUZjENnCQdQKFuACqNEP%2FSN%20Change%20Write%20ServiceNOW.png?alt=media&#x26;token=5db1fec6-b93b-41e5-b4be-7f03391d0552" alt=""><figcaption><p>sn_change_write role</p></figcaption></figure>

#### Problem

* **sn\_problem\_read** Enables reading of Problem records.
* **sn\_problem\_write** Supports creating and editing of Problem records.

Each role displays inherited permissions in the **Contains Roles** tab at the bottom.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbetaceNpEjkuGs2U49Ri%2FSN%20Problem%20Read.png?alt=media&#x26;token=4d4f5330-8b28-4679-a472-5d122fef81bf" alt=""><figcaption><p>sn_problem_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrvyOY6KaHnB3cORocivx%2FSN%20Problem%20Write%20ServiceNow.png?alt=media&#x26;token=7cc9bcc5-0c5f-4925-82a0-0e2f24d63452" alt=""><figcaption><p>sn_problem_write role</p></figcaption></figure>

### Removing Unwanted ACLs from OOB Roles

If you're concerned about assigning OOB roles that may include excessive permissions, you can query ACLs and trim them to fit your integration scope.

#### Steps to Query ACLs

1. In the **Application Navigator**, type `sys_security_acl_role_list.do` and press **Enter**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdz3yRL7ADNHYZM0zmLNR%2FSys%20Security%20role.png?alt=media&#x26;token=7f54ddc2-07d5-46de-aba0-093065b37a87" alt=""><figcaption></figcaption></figure>

1. It will lead you to a page that lists all ACLs within your ServiceNow workspace. You can then filter the ACLs by role.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj5n6epvskNOOYkvquMkr%2FACL%20Roles.png?alt=media&#x26;token=0ba3de90-c0cf-4319-b541-f637ab66ae5b" alt=""><figcaption></figcaption></figure>

1. Running the filter with conditions **ROLE - IS - \[yourRoleName]** will output all ACLs associated with the specified role. You can then customize all ACLs assigned to the specified role (you can also add tags to each ACL, so you can track their operation type, as you won’t be able to see it through this screen).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdDFOK3q3uFWdoEeJZegh%2Fimage-20250705-000707.png?alt=media&#x26;token=3e04f673-d81c-4aac-8fbf-b24e1fc56946" alt=""><figcaption></figcaption></figure>

### Adding ACLs for Vendor and Scoped Applications

For integrations involving modules like **Customer Service Management (CSM)** or **Project Portfolio Management (PPM)**, dedicated users must have ACLs aligned with corresponding work item tables.

For example, syncing the **Project** work item from **PPM** requires read, write, and create ACLs for the **Project** table. Without these, syncing will fail even if mappings exist in Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjjfPFyL58siajBOlPKm5%2FProject%20portfolio%20management.png?alt=media&#x26;token=d43c6cf9-2944-41e9-b8c3-aae0d27f766a" alt=""><figcaption><p>View of the Project Portfolio Management, through the Application Manager.</p></figcaption></figure>

#### Example Error

```
{"message":"Insufficient rights to query records","detail":"Field(s) present in the query do not have permission to be read"}
```

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZywdFyBv6yV5Q0jyYSkO%2FError%20with%20missing%20permissions.png?alt=media&#x26;token=6dc8cf7a-86b5-410d-b61a-bbce17d2f725" alt=""><figcaption><p>Dedicated user doesn’t have read ACL for the Project table.</p></figcaption></figure>

After installing a vendor application, you must create ACLs corresponding to the table and work item that you’d like to synchronize. Make sure to assign the ACLs to the dedicated user’s role:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMy7Xy85yOG2BK1a3CfEJ%2Fimage-20250705-032322.png?alt=media&#x26;token=e3d5464a-742f-4a55-8f1d-7fac0d0aa3c0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
In this case, we installed Project Portfolio Management. Searching for **Project** in the name dropdown of the ACL creation screen fetches the right table for the work item Project that we are looking to sync.
{% endhint %}

After assigning the **Read** ACL for the Project table to the dedicated user's role, Getint successfully retrieved items from the Project table. However, because the **Create** ACL was still missing, the integration was unable to generate new Project work items in ServiceNow.

To ensure smooth data synchronization, confirm that the dedicated user's role includes all required ACLs. These typically include **Read**, **Write**, and **Create** permissions for the relevant tables.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYIfYmAIU2SZovJxAamX6%2Fimage-20250705-032709%20(1).png?alt=media&#x26;token=f1f2d112-d864-40b8-9509-0842ce9ec220" alt=""><figcaption><p>Ensure to add Read, Write, and Create ACLs to the dedicated user’s role for the integration to run smoothly.</p></figcaption></figure>

#### Working with Scoped Applications

* Scoped applications like **CSM** operate in isolated environments. You cannot use the `.*` ACL operator unless you change the **global scope**. This ACL operator is required for Getint to synchronize data, and without the ACLs with this operator you might experience access issues.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVt00ddfF9lwk6cYTNixr%2Fimage-20250705-033327.png?alt=media&#x26;token=34389ce2-63a3-4415-9fe1-4563c2206eab" alt=""><figcaption><p>.* ACL is missing from the dropdown, as we are not in the scope of the application.</p></figcaption></figure>

* To change your current scope, click the **Application Scope** icon, and then click on the first option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrGJVFfX7SpMHRcGa44VE%2Fimage-20250705-035437.png?alt=media&#x26;token=99e48636-1bb4-431e-b31f-9f6af8615e74" alt=""><figcaption></figcaption></figure>

* Filter the application by name, then click it. When the application is selected, your ServiceNow tab should refresh, and the global scope will change the one selected:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfVBjPJWW6Ty5prfug599%2FCustomer%20Service%20Scope%20ServiceNOW.png?alt=media&#x26;token=3aafbac2-56d2-4bc8-8af6-eff3e272862f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FykO0njJRSiQ0MjzJK6oq%2FApplication%20scope.png?alt=media&#x26;token=f2901c71-ec36-40d0-b2bf-b54ce340d014" alt=""><figcaption><p>You can confirm that you are within the scope of the application by hovering your mouse over the application scope icon.</p></figcaption></figure>

* You should now be able to create ACLs of the scoped application’s tables with the .\* operator:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJfbY2e4hriotaQ5hMeJx%2Fimage-20250705-040522.png?alt=media&#x26;token=754c1004-f232-4283-bbda-10e30767f05a" alt=""><figcaption><p>The <strong>.*</strong> operator for ACL can now be selected, as we are within the application’s scope.</p></figcaption></figure>

### Debugging Field-Level ACLs

You can debug individual work item fields to uncover their ACLs, identify missing permissions, and assign only those needed for syncing. This lets you control which fields Getint can access while excluding any restricted data.

#### How to Debug Fields

1. Type **Debug Security** in the navigator,  and select **Debug Security Rules** under System Security.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkCjMdoq0Vl1TBeXkLdLj%2Fimage-20250706-021722.png?alt=media&#x26;token=912813d1-f08d-482d-be04-287ce637f1c7" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Avoid impersonating before opening the Debug application. Doing so will prevent access, even if the user has the **script\_debugger** role. Instead, open the Debug application first and impersonate after the debug window is active.
{% endhint %}

1. The Debug application window will appear. Impersonate the user, minimize the window, and navigate to the work item you want to debug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6hHwDuUsmM3olEl6HmJl%2Fimage-20250706-022644.png?alt=media&#x26;token=29fea761-21cd-40b9-b6a0-948230c2f17b" alt=""><figcaption><p>Debug application window.</p></figcaption></figure>

1. When debugging is active, a small **Bug** <img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNXvTrtIrW8H0TfXCR6d8%2Fimage.png?alt=media&#x26;token=fe642c8b-eba8-4cc7-b908-2416ce4de9e7" alt="" data-size="line"> icon appears beside fields governed by ACL rules. Clicking it reveals the applicable ACLs and their evaluation results.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSw5le2sY72jCjAcJQxDO%2FDebug%20icon%20next%20to%20fields.png?alt=media&#x26;token=81415305-6f83-4f53-96fb-fd8342da26af" alt=""><figcaption></figcaption></figure>

1. The fields appear greyed out, indicating the dedicated user lacks Write permissions, even though they have access to the Incidents application and table.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqNpp0d0fZJwzH9CfvLdr%2FFields%20with%20ACL%20rules.png?alt=media&#x26;token=a5c23f10-cd37-48ce-bfd6-a2792becd00b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
A **True** result for a Read ACL means the dedicated user has a role with Read access to the field.

A **False** result for a Write ACL means the user lacks Write permission for the field.
{% endhint %}

1. Granting Write ACL for the Urgency field to the dedicated user’s role enables editing of that field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0CtDTLgmeq0KnoT9GLyH%2Fimage-20250706-024345.png?alt=media&#x26;token=02f4364a-d5e6-419f-8988-2b1f10a7d349" alt=""><figcaption><p>Write ACL for the Incident's Urgency field has been added to the <strong>getint_integration</strong> role assigned to the dedicated user.</p></figcaption></figure>

1. The field is no longer greyed out, and its values are now editable.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq645bJxKDkcEBeXQqlrv%2Fimage-20250706-024528.png?alt=media&#x26;token=a26ae33a-73cc-4665-a8c8-ed1e2bbe3649" alt=""><figcaption><p>Getint can now sync the Urgency field, while leaving the data of other unwanted fields out of access.</p></figcaption></figure>

### Fields Not Visible Due to Business Rule <a href="#fields-not-visible-due-to-business-rule" id="fields-not-visible-due-to-business-rule"></a>

When reducing the access of the dedicated user, or when limiting its ACLs/roles, you may notice some fields missing from the work item:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwqCw2UWXacQvfmHCYdD2%2FMissing%20fields%20in%20ServiceNow%20Incident.png?alt=media&#x26;token=633a0607-1804-441c-b3b8-c93f9eee19dc" alt=""><figcaption><p>Fields such as Assignee and Assignment Group are missing from the view.</p></figcaption></figure>

If the dedicated user doesn't have **ITIL** or **snc\_incident\_read** roles, trying to switch the view from Self-Service to Default to display those missing fields will always switch it back to Self-Service.\
\
This happens due to a Business Rule in place. You can add the dedicated user role to the list of roles allowed to switch the view to default with the following process:

* Type **Business Rules** in the application navigator, and select the option under **System Definition**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNWoI5MeJlTpL9tm8SfC%2FBusiness%20Rules.png?alt=media&#x26;token=d9a9c248-13f6-4df0-acad-1bff4aed6b3c" alt=""><figcaption></figcaption></figure>

* Type **incident** in the search bar, and click on the **Incident Functions** option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fy8fGYHQ9d4zHWdoLixDq%2FLooking%20for%20incidents.png?alt=media&#x26;token=5ebba8d0-66f2-4105-831e-cf68626b2c29" alt=""><figcaption></figcaption></figure>

* Switch to the Advanced tab, and copy this text (from the first space until the penultimate parenthesis):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAXognwbe4AbXMqneGA3b%2FSwitch%20to%20the%20Advanced%20tab.png?alt=media&#x26;token=9d575dd4-6c07-4040-ba7d-850232b2eead" alt=""><figcaption></figcaption></figure>

* Paste the text right after the penultimate parenthesis, and change the "sn\_incident\_read“ role for the role you have created for your dedicated user (in my case, it’s getint\_integration):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeTM9dXDf4pRas84HJ8iQ%2FLook%20for%20the%20incident%20read%20role.png?alt=media&#x26;token=b61d7ee9-d348-4cb9-9e21-e790832b8ad5" alt=""><figcaption></figcaption></figure>

* Now the dedicated user should be able to switch views to Default, without it switching back to Self-Service, allowing you to visualize the fields from the work item properly while logged in through the dedicated user (or while impersonating it):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJpfpv5YicXRd19CPraYC%2Fdefault%20view%20for%20the%20dedicated%20user.png?alt=media&#x26;token=1cb5fcc7-34cf-4e85-864e-596be21ee6bc" alt=""><figcaption><p>Default View can now be selected, and the fields previously not visible are now displayed.</p></figcaption></figure>

### Summary

Use these steps to control what Getint can access and sync from ServiceNow.

* For a straightforward setup, assign OOB roles.
* To limit permissions, query ACLs, remove excess, and customize the role.
* Vendor applications like PPM or scoped apps like CSM require targeted ACLs. Make sure to switch scopes and add `. *` ACLs as needed.
* Debug field-level permissions to ensure the user can read and write the intended fields.

If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
