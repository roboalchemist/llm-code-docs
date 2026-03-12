# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies.md

# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/companies.md

# Companies

This section provides details of the functionality and flexibility available to those who administer multiple company accounts.

Go to **Company > Companies** to access all of the options described below.

{% hint style="warning" %}
This page is valid only for users with a Reseller role.
{% endhint %}

## **Why Create Company Definitions?**

Unique definitions help resellers to provide the best service to multiple tenants sharing software. There is the opportunity to refine various elements according to the needs of each company and simplify management.

The platform provides the ability to view, add, edit, and delete customer companies and administer each as appropriate.

The authority to create and manage companies is only available to Resellers. Each customer will access the features of their company based on their license type.

## Listing Companies

The following details of all companies created can be viewed on the **Company > Companies** page.

<table><thead><tr><th width="151.1145874071177"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>Company Name</td><td>Name of the company</td></tr><tr><td>Reseller Name</td><td>The name of the Reseller company that manages the customer account.</td></tr><tr><td>Industry</td><td>Industry sector of the company</td></tr><tr><td>License Type</td><td>Information of the product license owned by the company</td></tr><tr><td>Target Users</td><td>The number of target users that are active on the customer account.</td></tr><tr><td>Inactive Users</td><td>The number of target users that are inactive on the customer account.</td></tr><tr><td>Deleted Users</td><td>The number of target users that are deleted on the customer account.</td></tr><tr><td>Monthly Users</td><td>The number of target users were added to the customer account during the selected month, regardless of whether they are currently Active, Inactive, or Deleted. You can change the month using the selector. Monthly Users data is available starting from December for all customers.</td></tr><tr><td>License Limit</td><td>The number of total target users permitted to be uploaded to the platform by the customer account.</td></tr><tr><td>Tags</td><td>The tags can be added to the companies for easier filtering or any other purposes.</td></tr><tr><td>Renewal Date</td><td>The date and time when the customer account’s license expires.</td></tr><tr><td>Date Created</td><td>Date the company was created</td></tr><tr><td>Action</td><td><p>The specifics of an existing company can be revised. Click on the the window that opens when the three-dot icon for the following options.</p><ul><li><strong>Add to a company group =</strong> Add the selected company to a previously created company groups</li><li><strong>Switch to company:</strong> Switch to this company to manage the company.</li><li><strong>Create a new company group with company =</strong> Create a new company group with the selected company</li><li><strong>Switch</strong> <strong>to</strong> <strong>company</strong> <strong>=</strong> Simulate the selected company to manage</li><li><strong>Delete</strong> <strong>=</strong> Delete the selected company</li></ul></td></tr></tbody></table>

### Exporting the company list

You can export the company list from **Company > Companies** to Excel or CSV. The exported file includes all columns visible in the list, including:

* **Inactive Users** — Number of target users who are inactive for that company.
* **Deleted Users** — Number of target users who have been deleted for that company.
* **Monthly Users** — Number of unique users added during the selected billing month (same as the Monthly Users column; the selected month applies to the export).

Use the export for billing reviews, capacity planning, and reporting across managed companies.

## **How to Create a New Company**

Go to the **Company > Companies** page and click on the **+ NEW** button to create a new company. The process of creating a new company consists of 4 stages which are explained below.

### Step 1: Company Info

Complete each field described below.

<table><thead><tr><th width="150"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>Company Name</td><td>Name of the company to be created</td></tr><tr><td>Description</td><td>Description of the company</td></tr><tr><td>Industry</td><td>The industry sector of the company</td></tr><tr><td>Country</td><td>Country location of the company. When you select a country, the platform automatically sets a default <strong>Date Format</strong> and <strong>Time Format</strong> based on that country's regional conventions. You can still change these formats manually in company settings if needed.</td></tr><tr><td>Address</td><td>Mailing address of the company</td></tr><tr><td>Website URL</td><td>Website address of the company</td></tr><tr><td>Company Logo</td><td><p>Option to upload a company logo. The aspect ratio is set automatically. For best results, the size should be 180px (w):60px (h).</p><p>The maximum disk image size is 2 MB. .Gif, .png, .jpg and .svg formats are supported.</p></td></tr><tr><td>Active</td><td>A company may be registered as inactive or active. Active status is required for the use of the platform.</td></tr><tr><td>Tags</td><td>Add tags to your company to easily search for it later using the Tags column.</td></tr></tbody></table>

Click **Next** to proceed to the License step.

### Step 2: License

Provide the following details of the company license.

<table><thead><tr><th width="151.1145874071177"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>License Type</td><td>Licensed product owned by the company or details of a custom license.</td></tr><tr><td>Expiry Period</td><td>License expiration date</td></tr><tr><td>Number of users</td><td><p>The number of licenses purchased by the company for adding unique email users to the platform.</p><p>Select the <strong>Make Unlimited</strong> option for an unrestricted number of licensed users.</p></td></tr></tbody></table>

Click **Next** to proceed to the Groups step.

### Step 3: Groups

Select groups relevant to this company and add this company to the relevant company groups. Please see more information about company groups from [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/companies/company-groups).

<table><thead><tr><th width="150"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>Company Groups</td><td>Companies added to a company group have access to the shared contents such as SMTP settings, notification templates or other settings defined for that company group.</td></tr></tbody></table>

Click **Next** to proceed to the Content Management step.

### Step 4: Content Management

Select the content and settings to be made available to the company.

<table><thead><tr><th width="150"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>Notification Templates</td><td><p>There are 3 options:</p><p><strong>All Notification Templates =</strong> The company has access to all of the notification templates on the platform including yours that has been shared with the company.</p><p><strong>Only System Notification Templates =</strong> The company only has access to system notification templates.</p><p><strong>Only Reseller's Custom Templates =</strong> The company only has access to the custom notification templates shared by the reseller.</p></td></tr><tr><td>Training Contents</td><td><p>There are 3 options:</p><p><strong>All Training Content =</strong> The company has access to all training content shared by the platform or reseller.</p><p><strong>Only System Training Contents =</strong> The company only has access to system training content.</p><p><strong>Only Reseller's Custom Training Content =</strong> The company only has access to the customized reseller training content.</p></td></tr><tr><td>SMTP Configurations</td><td><p>There are 3 options:</p><p><strong>All SMTP Configurations =</strong> The company has access to all SMTP settings provided by the platform or reseller.</p><p><strong>Only System SMTP Configurations =</strong> The company only has access to SMTP configurations of type SYSTEM which is shared by the platform.</p><p><strong>Only Reseller's Custom SMTP Configurations =</strong> The company only has access to the customized SMTP configurations customized by the Reseller.</p></td></tr></tbody></table>

After clicking the **Save** button at the bottom right of the screen, you will be presented with a choice of how to proceed. In response to “Would you like to configure settings for the company you just created?” You can click **Yes** **configure**, and complete the process, or delay the application of the settings with the **Skip** option.

### Step 5: Quick Setup

The **New Company Quick Setup** page has 3 steps to a simple configuration. Each component is explained in detail below.

#### Step 1: White Labeling

This option gives you the opportunity to customize the interface of the platform for any brand. Additional details about white labeling are provided here.

Move on to the **First System User** page by clicking **Save** **and** **Continue**, or you can go directly to the subsequent page by clicking the **Skip** button. The **Cancel** option allows you to rescind the configuration.

#### Step 2: First System User

The system user is the authorized account used to manage all activities on the platform. The following elements must be defined to create first system user.

<table><thead><tr><th width="151.1145874071177"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>First name</td><td>First name of the system user</td></tr><tr><td>Last name</td><td>Surname of the system user</td></tr><tr><td>Email Address</td><td>Email address of the system user</td></tr><tr><td>Phone Number</td><td>Phone number of the system user (This information is required in multiple authentication steps; accuracy is important.)</td></tr><tr><td>Status</td><td>The account may be designated as inactive if the account is no longer needed to log in to the platform.</td></tr><tr><td>Role</td><td>It is the area where the priveleges of the system user is determined.</td></tr></tbody></table>

Move on to the **Next** **Steps** page by clicking **Save** **and** **Continue**. You can return to the White Labeling page with the **Back** button or you can go directly to the next page by clicking the **Skip** button. The **Cancel** option allows you to rescind the configuration.

#### Step 3: Next Steps

Once a company has been created, you can edit the specific settings described below.

<table><thead><tr><th width="151.1145874071177"></th><th width="580.5714285714286"></th></tr></thead><tbody><tr><td>Customize Notification Templates</td><td>To create and edit company email notification templates, use the path <strong>Company > Company Settings > Notification Templates</strong>.</td></tr><tr><td>Create Target Users</td><td>To create a target user group, use the path <strong>Visit Company > Target Users</strong>.</td></tr><tr><td>Mail Configurations</td><td>To define the email services for the most effective use of the Phishing Reporter and Incident Responder, use the path <strong>Incident Responder > Mail configurations</strong>.</td></tr><tr><td>Create Tenant Companies</td><td>To designate a new company that you manage, use the path <strong>Company > Companies</strong>.</td></tr><tr><td>Configure Phishing Reporter</td><td>To configure the Phishing Reporter plugin settings, use the path <strong>Phishing Reporter > Settings</strong>.</td></tr></tbody></table>

You can complete the process with the **Close** button, return to the **First System User** page with the **Back** button, or select **Cancel** to rescind the configuration.

## FAQs

### Q: I created a company account, can I delete it at any time?

A: Yes. You have the ability to edit and delete company accounts as desired from the **Company > Companies** page.

### Q: Can I increase the number of license users of a company at any time?

A: Yes. You can update the license information of a company as needed by editing the company from the **Company > Companies** page.

### Q: Can I manage the companies I created on the platform?

A: Yes. You have the ability to manage and simulate the companies you created from the **Company > Companies** page.

### Q: Can I manage a company created by someone else?

A: Yes, you can see and manage if the company is created by another Reseller under your management. Details of the **Switch** **Company** feature are available [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/user-profile).

### **Q:** How can I filter companies that have exceeded their user limits?

A: Go to the **Companies** menu, then click **"Exceeding User Limit"** button from the filter options to see companies that have exceeded their user limits.
