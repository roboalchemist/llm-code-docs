# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration.md

# Creating a ServiceNow User for Getint Integration

In general scenarios, Admin access is not provided to a ServiceNow instance. The best practice/recommendation is to create a dedicated user (with several different access controls) to connect a ServiceNow instance to Getint and sync the data.

### How to Create a ServiceNow User <a href="#how-to-create-a-servicenow-user" id="how-to-create-a-servicenow-user"></a>

#### **1. User Creation:** <a href="#id-1.-user-creation" id="id-1.-user-creation"></a>

* Log in to ServiceNow, click **All** at the top left corner, and navigate to the **Users** (under User Administration) section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJNoYfNVWX1B0d7Tp7ZUt%2FServiceNow%20Developer%20Instance.png?alt=media&#x26;token=f7fc9f83-5998-432b-8861-32956f3f5d80" alt=""><figcaption></figcaption></figure>

* Click on **New** to create a new user, and enter all relevant user details.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEkxDtQAojLSPVEHoVvO7%2FCreating%20a%20ServiceNow%20user.png?alt=media&#x26;token=45791963-98e7-49d4-83d6-40a7d0b9e3c9" alt=""><figcaption></figcaption></figure>

* Enter the User details, and click **Submit** to create the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjCcgh8MUWUpVl9RfkOTD%2FName%20your%20user%20and%20submit%20it.png?alt=media&#x26;token=988370e5-e99e-432f-9cb6-f9e2458d3448" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ensure that you untick **Password needs reset** when creating a new user. If you skip this step, the system will block the connection and display an error stating that you lack sufficient permissions. This message is misleading, as the issue isn’t related to permissions, but simply that the password is set to reset.
{% endhint %}

* After creating the user, you can now generate a password. Do so by clicking **Set Password** in the right corner of the screen. Save the password, and now you can use the full credentials to create a connection with Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMx64Idxe8ExBvSOBoUjV%2FSetting%20up%20a%20password.png?alt=media&#x26;token=f6f7ab84-3679-4ef3-a630-9283129bcb79" alt=""><figcaption></figcaption></figure>

#### **2. Create a Role:** <a href="#id-2.-create-a-role" id="id-2.-create-a-role"></a>

* Navigate to **System Security** > **Users and Groups** > **Roles.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHQCsYtcAEnnL47vyYI7s%2F82779d882a8ec1955b1c3feb980817f8%20(1).png?alt=media&#x26;token=5ffbf046-56df-43f8-9721-95d55ab83110" alt=""><figcaption></figcaption></figure>

* Click on **New** and enter relevant details for the new role.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft9ekcUQFBgMmVmdB8Tt8%2F0a524ce617cface009af137cdc1f88c0%20(1).png?alt=media&#x26;token=799238dd-d212-45a1-b109-e2ac0a3b0f93" alt=""><figcaption></figcaption></figure>

* Click **Submit** to create the role.

#### **3. Elevate System Admin to Security Admin:** <a href="#id-3.-elevate-system-admin-to-security-admin" id="id-3.-elevate-system-admin-to-security-admin"></a>

* Click on your profile image and select **Elevate Role.** In the pop-up, choose **security\_admin** and click **Update.** This step elevates the **System Admin** to **Security Admin** and will allow you to modify the **ACL** settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnpurKaVQ5j2cfS1sOdV3%2F3cbd2f8bd07344f83f0556c919121622%20(1).png?alt=media&#x26;token=5dbb5eb5-cfad-4c5a-a550-cd0d4088bc5a" alt=""><figcaption></figcaption></figure>

#### 4. Required ACLs for Getint Integration

As we are tailoring access for our users, some base ACLs are required so that the connection with the ServiceNow instance works properly, allowing users to create, edit, and read their fields.

Here is a list of the needed ACLs, as well as their respective purpose in this process:

* **Dictionary Entry \[sys\_dictionary]**\
  This is the ServiceNow Data Dictionary, which defines the structure and attributes of every field on every table.\
  The Getint user needs read access to this table to introspect the schema of the records being synchronized. By reading this table, Getint identifies a field's type (e.g., reference, string) and its properties (e.g., maximum length, required status). This information is crucial for accurately translating and mapping data types between ServiceNow and other software.
* **Field Class \[sys\_glide*****\_*****object]**\
  This table stores definitions for the fundamental data types (e.g., string, integer, reference) used by fields across the instance.

  The dedicated user requires read access to this table because it is closely related to sys\_dictionary. It provides the low-level, technical classification of the field types. This access helps Getint's logic correctly interpret and handle the data being pulled or pushed, ensuring that all synchronized fields adhere to their native ServiceNow data constraints.
* **Choice \[sys\_choice]**\
  This table contains all the predefined drop-down options (choices) for choice fields in the system, such as Incident State or Priority values.

  The Getint user must have read access to retrieve both the internal value (the numerical/system value) and the display label (the user-friendly name) for these choices. This is essential for the core integration function of status and value mapping, ensuring that a status correctly corresponds to the appropriate, valid choice value in ServiceNow.
* **Journal Entry \[sys\_journal\_field]**\
  This table is where Journal-type field entries are stored, specifically, records like Additional comments and Work notes from synchronized tickets.

  The dedicated user requires read and create/write access to this table to manage bi-directional communication. This access allows Getint to extract comments from a ServiceNow record to sync to the integrated software, and conversely, to write comments back into the correct ServiceNow journal field, maintaining a full communication history.

#### 5. Granting User Access: Create Permission Records in ServiceNow

* Go to **System Security** > **Access Control (ACL).** Now, in the **ACL**, create **six new records** as follows:

**Record 1:**

* Click **New** to create a new record.
* Select **Read** from the **Operation** dropdown.
* In the **Name** field, select **Dictionary Entry \[sys\_dictionary]** in the first dropdown and **\*** in the second dropdown.
* Provide a **Description.**
* In the **Requires Role** section, add the role created in **Step 2** above.
* Click **Submit** at the top right corner, and **Continue** to create the new ACL record.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSr1If8WIDWKiapmX7tOE%2Fa2ce5cb001b4863e64efcaf97a15ca92%20(1).png?alt=media&#x26;token=e4ab8ba7-20ec-49be-8f10-10968d7ab2d6" alt=""><figcaption></figcaption></figure>

**Record 2:**

* Repeat the steps as **Record 1,** but this time select **None** in the second dropdown instead of the **\* (asterisk).**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVpXOCtJdpY2sTvo2CtL2%2F3ec142a61b16bda4734f6bf41b378436%20(1).png?alt=media&#x26;token=1a0e6b27-f0ba-47bd-a4e6-f4fb7fffafeb" alt=""><figcaption></figcaption></figure>

**Record 3:**

* Repeat the previous steps, but in the **Name** field, choose **Field class \[sys\_glide*****\_*****object]** in the first dropdown and **\*** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiDR8pcyfYMhxVayudaeC%2Fb833a4169923482038ca2173f14065d0%20(1).png?alt=media&#x26;token=30ac4e3b-d617-4a78-bfc6-da1f23199474" alt=""><figcaption></figcaption></figure>

**Record 4:**

* Repeat the previous steps, but in the **Name** field, choose **Choice \[sys\_choice]** in the first dropdown and **\*** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fxa5dXkCd7W4o9sRDY8mm%2F0265b1df0503d18b78dcb86ef65ff561%20(1).png?alt=media&#x26;token=20787949-f5e3-4486-bbc6-386480155dec" alt=""><figcaption></figcaption></figure>

**Record 5:**

* Repeat the previous steps, but in the **Name** field, choose **Field class \[sys\_glide*****\_*****object]** in the first dropdown and **None** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fw68TScwvjkjicPiYAgRJ%2F433d73b97a2b9a532f77673f4de2e335%20(1).png?alt=media&#x26;token=6fecc870-c555-49fd-9fa2-4012f370e604" alt=""><figcaption></figcaption></figure>

**Record 6:**

* Repeat the previous steps, but in the **Name** field, choose **Journal Entry \[sys\_journal\_field]** and **None** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FECqA6YFJYTFYniI2CXE9%2F4ae64ae1bdc9f5e58d85347ba492d6ce.png?alt=media&#x26;token=c37f5e74-2c8b-448a-a471-042873133ce5" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Do not forget to add the **getint role** in the **Requires role** section for all six records.
{% endhint %}

#### **6. Configure User Permissions:** <a href="#id-4.-configure-user-permissions" id="id-4.-configure-user-permissions"></a>

* Go to **Users Administration** > **Users.**
* Search for the user created in **Step 1.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFYEkZJrtoJf3EINUMeCj%2F13732d07421f4c47cacf87f6d6b928b9%20(1).png?alt=media&#x26;token=d4511f78-c821-445e-ac12-a101576bf72c" alt=""><figcaption></figcaption></figure>

* Click on the user ID and navigate to the **Entitled Custom Tables** section.
* In the **Roles** tab, click **Edit.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2kfgUBj3uVbODjOqbYPF%2Ff92234b9c098f8319e4fe4c2030bdfa1%20(1).png?alt=media&#x26;token=d92b7e43-7e17-4d08-b0e6-788145becd08" alt=""><figcaption></figcaption></figure>

* In the **Collections** section:
  * Search for **itil** and move it to the **Roles list.**
  * Also, search for the role created in **Step 2** and add it to the **Roles list.**
* Click **Save** and then **Update** to finalize the changes for the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzF8hXfkotOln5fSXChs5%2Fcc28d7fb4a0878eb6d68c2058dae5007%20(1).png?alt=media&#x26;token=7a055e10-f9a2-46fa-8972-9fcd5fe955d4" alt=""><figcaption></figcaption></figure>

With these steps, all permissions are now configured for this ServiceNow user, allowing to establish a connection between Getint and ServiceNow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
