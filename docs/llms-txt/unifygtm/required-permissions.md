# Source: https://docs.unifygtm.com/reference/integrations/salesforce/required-permissions.md

# Required Permissions and Settings

> Ensure your Salesforce user has the required permissions for Unify.

# Overview

The permissions that Unify requires fall into two categories:

1. **System Permissions**: These are permissions that apply to the entire
   Salesforce instance and are required for Unify to function properly.
2. **Object Permissions**: These are permissions that apply to specific objects
   (e.g., Account, Contact, etc.) and are required for Unify to read and write
   data.

The exact permissions that Unify needs are detailed below along with
instructions on assigning these permissions to your integration user.

# Required Permissions

<Info>
  Access can be restricted as desired for sensitive records or fields that you
  do not want Unify to access. However, Unify needs access to any records or
  fields that you want to use for exclusions.

  For example, to prevent Unify from engaging with current customers, Unify will
  require access to the records that indicate current customers to evaluate the
  exclusion rule.
</Info>

<Tabs>
  <Tab title="System Permissions">
    | Permission                       | Reason                                                      |
    | -------------------------------- | ----------------------------------------------------------- |
    | **API Enabled**                  | Allows Unify to communicate with Salesforce via the API     |
    | **View All Users**               | Enables Unify to link Salesforce users to Unify users       |
    | **View Setup and Configuration** | Enables Unify to provide details about missing permissions  |
    | **Edit Tasks**                   | Enables Unify to create and update tasks and email messages |
  </Tab>

  <Tab title="Object Permissions">
    | Object            | Permissions          | Reason                                                     |
    | ----------------- | -------------------- | ---------------------------------------------------------- |
    | **Account**       | *Read, Create, Edit* | Enables Unify to sync companies bidirectionally            |
    | **Contact**       | *Read, Create, Edit* | Enables Unify to sync people bidirectionally               |
    | **Lead**          | *Read, Create, Edit* | Enables Unify to sync companies and people bidirectionally |
    | **Opportunity**   | *Read*               | Enables Unify to use and filter based on opportunities     |
    | **Email Message** | *Read, Create, Edit* | Enables Unify to write outbound emails and replies         |
  </Tab>
</Tabs>

# Setup

### Assign required permissions

Depending on whether you are using profiles or permission sets, the steps to
assign the required permissions will differ slightly. Follow the instructions
below based on your setup.

<Tabs>
  <Tab title="Profiles">
    If you're using a **Profile** to manage permissions, follow these steps:

    1. Navigate to the **Setup** page in Salesforce by clicking the gear icon in
       the top-right corner.

    2. Go to **Users > Profiles**.

    3. Choose the Profile assigned to your integration user.

    4. Click **Edit**.

    5. In the **Administrative Permissions** section, enable the following
       options:

       * **API Enabled**
       * **View All Users**
       * **View Setup and Configuration**

    6. In the **General User Permissions** section, enable the following
       options:

       * **Access Activities**

    7. In the **Standard Object Permissions** section, enable the following
       options for each object:

       * **Account**: Read, Create, Edit
       * **Contact**: Read, Create, Edit
       * **Lead**: Read, Create, Edit
       * **Opportunity**: Read
       * **Email Message**: Read, Create, Edit

    8. Click **Save**.
  </Tab>

  <Tab title="Permission Sets">
    If you're using a **Permission Set** to manage permissions, follow these steps:

    1. Navigate to **Setup > Permission Sets**.

    2. Create a new permission set (or modify an existing one).

    3. Assign the permission set to your integration user.

    4. Under **System Permissions**, enable the following options:

       * **API Enabled**
       * **View All Users**
       * **View Setup and Configuration**

    5. Under **App Permissions**, enable the following options:

       * **Access Activities**

    6. Under **Object Settings**, select each object and enable the following
       options:

       * **Account**: Read, Create, Edit
       * **Contact**: Read, Create, Edit
       * **Lead**: Read, Create, Edit
       * **Opportunity**: Read
       * **Email Message**: Read, Create, Edit

    7. Click **Save**.

    8. If you created a new permission set, assign it to your integration user.
  </Tab>
</Tabs>

Once you've assigned these permissions, you can verify they are correctly set up
by checking the **Permissions** widget in Unify. Navigate to
[Settings -> Integrations -> Salesforce](https://app.unifygtm.com/dashboard/settings/integrations/salesforce)
and look for the **Permissions** widget.

<Frame caption="The permissions widget will indicate if permissions are missing.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c1b2160778cc25bdc9df55963c4aaf2d" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/missing-permissions-settings-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9631cd5ef28ffff5689c1085891693c6 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4a84c5360df3a158222835feabe72bef 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dd4cf8a57312a23e4e1c74b267d25a7b 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=87345249c0860e92219f92f29b00e37c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=19dd4a89adeb4e369843aa7eebedbcbd 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a520595c950078a6de3e237f2ca33928 2500w" />
</Frame>

<Frame caption="The specific missing permissions are displayed in the details view.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bf9161fd9b568ae58178b8258f884f10" data-og-width="2880" width="2880" data-og-height="2050" height="2050" data-path="images/reference/integrations/salesforce/view-missing-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4f4df5d4bc9a4a0b1c5e0a00b774020a 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e40f8e2272fdabac8e63e17658c6481a 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8666941f6b10bf8e23621922468672e8 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=307bd20f36c0b0ab360bec5246d9df37 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bf678cbcc71d2d27747cfe2685968b80 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=60477b55b55c7dcc593fd96ac8f1e508 2500w" />
</Frame>

### Enable Enhanced Emails

To ensure Unify can write emails to Salesforce, the **Enhanced Email** feature
must be enabled. This allows Unify to write sent emails using the **Email Message**
object.

In most orgs, Enhanced Email is enabled by default. If you don’t see the
**Email Message** object, review the following guide to enable it.

<Card icon="envelope" title="Set Up Enhanced Email" href="https://help.salesforce.com/s/articleView?id=sf.enable_enhanced_email.htm&type=5">
  Salesforce support article explaining how to enable Enhanced Email.
</Card>

For more information:

* [Use Enhanced Email for More Email Functionality](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_overview.htm\&type=5)
* [Considerations for Using Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm\&type=5)
