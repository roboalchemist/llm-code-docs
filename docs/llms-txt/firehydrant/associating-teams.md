# Source: https://docs.firehydrant.com/docs/associating-teams.md

# Associating Teams

<Image alt="Teams settings in a Service or Functionality" align="center" width="650px" src="https://files.readme.io/8c03a4b-image.png">
  Teams settings in a Service or Functionality
</Image>

FireHydrant provides a few options in the catalog for leveraging teams for service ownership and responsibility. These team assignments help ensure the accuracy and completeness of the Catalog to help your teams resolve incidents quickly.

## Owning Teams

Setting an **Owning Team** limits access to editing or deleting a functionality or service to only members of that team, but with some exceptions:

* **Owners** will always be able to edit a Catalog entry regardless of Owning Team and team membership.
* **Viewers** and **Collaborators** will never be able to edit a Catalog entry regardless of Owning Team and team membership.
* Only **Members** will be restricted according to whether they are in a Catalog entry's Owning Team.

## Responding Teams

The **Responding Teams** respond to any incidents involving said functionalities or services. This allows you to understand which teams to call and [automatically pull them into the incident](/docs/adding-responders#automatically-via-service-catalog) if the **Auto-add responding team** setting is checked.

## Setting Teams on a Catalog Entry

Make sure you have FireHydrant Teams created. To learn more, read about [configuring your teams here](https://docs.firehydrant.com/docs/team-configuration).

To add an **Owning Team** or **Responding Teams**:

1. Click on **Catalog** in the navigation and then navigate to Services or Functionalities.
2. From here, select the Catalog entry you would like to edit, and on this screen, click **Edit Service** or \*\*Edit Function
3. Scroll down to the **Teams** section of the entry and select an owning team and/or responding team(s).
4. When you're done configuring, you can scroll to the top or bottom and click **Save edits**.

> 🚧 Note:
>
> If you set an Owning Team on an entry and you are not on that team or an **Owner** in the organization, then after clicking **Save edits**, you will no longer be able to edit that entry.

## Next Steps

Now that you've read about Owning and Responding Teams on Services:

* If you haven't, see how you can [link components](https://docs.firehydrant.com/docs/import-and-link-components) to other external providers to unlock even more capabilities
* For a primer on role-based access controls on FireHydrant, visit [the documentation page here](https://docs.firehydrant.com/docs/role-based-access-controls).