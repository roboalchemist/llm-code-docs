# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/getting-started-with-scim.md

# Getting Started with SCIM

You can create a SCIM setting by following the steps below and then authenticate your identity provider with the platform over the SCIM endpoint and token to synchronize users.

1. Go to **Company > Company Settings > SCIM Settings** page.
2. Click the **‘+ NEW’** button to create a SCIM setting.
3. Enter a **name** for the SCIM setting.
4. **Map a field** if you want to synchronize unique information. You **may skip** this step if you're not interested to synchronize different information rather than "email, first name, last name, department, phone number" information.
   1. If you want to create a mapping to synchronize a piece of unique information.
   2. First, go to the **Target Users** page, and on the top right side, click the **Settings** button and then click **Edit Fields** to create one field, and then you can map it on SCIM settings.
   3. To map the unique piece of information to the created column, select the attribute and column by following the steps.
      1. Go to **Company > Company Settings > SCIM Settings > + NEW > Map Fields** to map the attribute you wish to synchronize to that column.
5. Click the **Next** button to go to the second page.
6. Choose a target group that you want to synchronize users to.
   1. If you don’t have a target group, please create one.
   2. If a group is not chosen, the users will be synchronized as a **single user** under the **People** tab in the target users menu.
7. **Group By** is a feature that allows you to synchronize users by their **Department** or **Custom Mapped Field.**
   1. If you enable this feature, all users won’t be synchronized to **only one group** but instead, everyone will be assigned to their own mapped target group.
   2. The users who don’t have mapped information will be synchronized to the target group that is chosen.
   3. Please **leave it empty** if you want to synchronize users to **only one group.**
8. Click **Save** and make sure to copy the **unique token** information.

You can now switch to Identity Provider to set up the rest of the SCIM settings.
