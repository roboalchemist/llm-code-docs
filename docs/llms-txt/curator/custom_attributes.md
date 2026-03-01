# Source: https://docs.curator.interworks.com/users_groups/user_management/custom_attributes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Attributes 

> Define and manage custom user attributes for enhanced user profiling and personalized content delivery.

With Tableau Cloud, and Tableau versions 2023.1 and above, you can now pass through User Attributes from Curator or your
SAML IdP (e.g. Okta, Azure AD) seamlessly through to your Tableau Dashboards.  This will allow you to use a new calculated
field `USERATTRIBUTE()` in your Dashboard to retrieve the value of the User Attribute and filter your data accordingly.

Note: When a conflict arises due to the same attribute being found in multiple locations, the User attributes will take
highest precedence, followed by Group attributes and then SAML attributes.

## View User's Attributes

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user you would like to see from the list using the search options.
4. Expand the "Custom Attributes" section.  At the top you will see the "Resolved Attributes" that take into account
   inheritance from all sources.

## Enabling SAML Attribute Retrieval on Login

(/setup/authentication/overview)
\***NOTE:** [SAML Authentication](/setup/authentication/overview)
**must be enabled to retrieve these user details from an external source.**

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Expand the "SAML Attributes" section, and enter User Attributes you would like Curator to detect from the user's SAML
   profile on login.
4. Click the "Save" button.

## Assigning User Attributes to a Group on Curator

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Group** section from the left-hand menu.
3. Find a user group and click on the group to edit details, or click the "New Frontend Group" button to create a new
   group on Curator.
4. Expand the "Custom Attributes" section, and enter the attribute and value you would like to assign to all users that
   belong to this group.
5. Click the "Save" button.

## Assigning User Attributes to a User on Curator

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user you would like to assign an attribute to and click on their name to view the edit-user page.
4. Expand the "Custom Attributes" section, and find the "User Custom Attributes" fields.  Enter the attribute and value
   you would like to assign to the user.
5. Click the "Save" button.
