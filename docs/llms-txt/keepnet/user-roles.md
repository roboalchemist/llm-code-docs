# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles.md

# User Roles

This section describes how to create custom roles to restrict platform access usage for system users. The platform provides default roles such as Company Admin and Reseller for system users to use on the platform. The admin has the option to restrict system users’ activities on the platform.

### **Roles Home Page**

Go to **Company > System Users > User Roles** menu. This menu will list all the default roles and custom roles. The admin can create, view, edit or delete the roles.

The fields of the roles page are explained below.

<table><thead><tr><th width="183"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Role Name</td><td>Name of the role</td><td></td></tr><tr><td>Users</td><td>Number of users assigned to the role</td><td></td></tr><tr><td>Tenant Users</td><td>Number of different tenant's users assigned to the role</td><td></td></tr><tr><td>Type</td><td>The type of the custom role, it can be Custom or System. The Custom is created by the company and the System is provided by the Platform or Reseller.</td><td></td></tr><tr><td>Date Created</td><td>The date that the role was first created</td><td></td></tr><tr><td>Actions > Edit</td><td>Edit the role to customize</td><td></td></tr><tr><td>Action > Delete</td><td>Delete the role. The users must be unassigned from this role for an admin to delete the role successfully.</td><td></td></tr></tbody></table>

### **How to Create a New Role**

Go to **Company Settings > System Users > User Roles** then click the **New** button. This will bring you to the page where you will define the role name, descriptions, and permissions with the following fields.

<table data-header-hidden><thead><tr><th width="203"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Role Title</td><td>The name of the custom role</td><td></td></tr><tr><td>Description</td><td>A brief description of the role</td><td></td></tr><tr><td>Make available For</td><td>Choose the companies and/or company groups that will have this role available. This option is only available to Reseller accounts.</td><td></td></tr><tr><td>Privileges</td><td>Search permissions to assign to the role.</td><td></td></tr><tr><td>Permissions</td><td>Select the permissions to make available. You can see the permissions available in the table below.</td><td></td></tr></tbody></table>

### **Permissions Available**

For each permission, you can select the full field or specific sub-fields within the permission to the platform.

<table data-header-hidden><thead><tr><th width="138"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Permission Field</strong></td><td><strong>Sub Field(s)</strong></td><td></td></tr><tr><td>Threat Sharing</td><td><ul><li>Communities</li><li>Incidents</li></ul></td><td></td></tr><tr><td>Phishing Simulation</td><td><ul><li>Email Templates</li><li>DNS Services</li><li>Domain Records</li><li>Landing Page</li><li>Templates</li><li>Phishing Scenario</li><li>Phishing Campaign</li><li>Phishing Campaign Job</li><li>Phishing Campaign Report</li><li>Exclude IP Address</li></ul></td><td></td></tr><tr><td>Smishing Simulator</td><td><ul><li>Smishing Scenario</li><li>Text Template</li><li>Smishing Campaign</li><li>Smishing Campaign Job</li><li>Smishing Campaign Report</li><li>Smishing Domain Records</li><li>Smishing Exclude IP Address</li><li>Smishing Dns Services</li><li>Smishing Landing Page Template</li></ul></td><td></td></tr><tr><td>Awareness Educator</td><td><ul><li>Certificates</li><li>Enrollments</li><li>Training List</li><li>Training Reports</li></ul></td><td></td></tr><tr><td>Incident Responder</td><td><ul><li><p>Integrations</p><ul><li>Cross Company Integration</li></ul></li><li>Investigations</li><li><p>Incident Responder</p><ul><li>Reported Emails</li></ul></li><li>Playbook</li><li>Mail Configurations</li></ul></td><td></td></tr><tr><td>Phishing Reporter Add in</td><td><ul><li><p>Phishing Reporter</p><ul><li>Settings</li><li>User</li></ul></li></ul></td><td></td></tr><tr><td>Email Threat Simulator</td><td><ul><li>Attack Vector</li><li>Quick Scan</li></ul></td><td></td></tr><tr><td>Company Settings</td><td><ul><li>Audit Log</li><li>Companies</li><li><p>Widget</p><ul><li>ROI Settings</li></ul></li><li>Company Groups</li><li><p>System Users</p><ul><li>User Roles</li><li>People</li><li>Account</li></ul></li><li>Target Users</li><li><p>Company Settings</p><ul><li>SMTP Settings</li><li>Notification Templates</li><li>Rest API</li><li>White Labeling</li><li>Proxy Settings</li><li>SAML Settings</li><li>Tag Management</li><li>Company Settings</li><li>SCIM</li><li>SIEM Integrations</li><li>LDAP Settings</li><li>Allow List</li><li>Direct Email Creation</li><li>Privacy</li></ul></li></ul></td><td></td></tr><tr><td>Vishing Simulator</td><td><ul><li>Vishing Template</li><li>Vishing Campaign</li></ul></td><td></td></tr><tr><td>Quishing Simulator</td><td><ul><li>Quishing Scenario</li><li>Quishing Domain Records</li><li>Quishing Exclude IP Address</li><li>Quishing Dns Services</li><li>Quishing Landing Page Template</li><li>Quishing Campaign</li><li>Quishing Campaign Job</li><li>Quishing Campaign Report</li><li>Email Templates</li><li>Quishing Template</li></ul></td><td></td></tr><tr><td>Threat Intelligence</td><td><ul><li>Search Leak</li><li>Get Leak Report</li></ul></td><td></td></tr><tr><td>Callback Simulator</td><td><ul><li>Callback Template</li><li>Callback EmailTemplate</li><li>Callback Scenario</li><li>Callback Campaign</li><li>Callback Campaign Job</li><li>Callback Settings</li><li>Callback Campaign Job Report</li></ul></td><td></td></tr></tbody></table>

Once you select the permissions for your new role, click **Save** button and the new role will populate on the **Roles** page.

### **How to Add a User to a Role**

Go to the **Company > System Users** page to assign the custom role to the system users, simply by editing the system users and updating the role. The system user will have a custom role and depending on the custom role permissions, the system user can manage the platform.
