# Source: https://www.apollographql.com/docs/graphos/platform/graph-management/transfers.md

# Transfer graphs

Transferring a graph between organizations in Apollo GraphOS Studio can be necessary for changes in project ownership.
To transfer graphs using the Studio UI, users need the [appropriate roles](https://www.apollographql.com/docs/graphos/platform/graph-management/transfers.md#required-roles) in both the source and destination graphs.

## Transfer graph ownership

If you want to transfer a graph from an organization with an expired plan or trial, please email [support@apollographql.com](mailto:support@apollographql.com).

### Required roles

To transfer a graph from one organization to another you need:

* At least the [graph admin role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) in the source organization
* At least the [contributor role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) in the destination organization

### Transfer steps

1. Open the graph you want to transfer in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).

2. In the left nav, open **Settings** and then the **This Graph** tab.

3. Under **Danger Zone**, next to **Graph owner**, click the **Transfer Graph** button.

   The **Transfer Graph button** isn't available if your user account isn't an Org Admin in multiple organizations.

4. In the modal that appears, select the organization you want to transfer the graph to. Click **Transfer**.

The graph will then be transferred to the selected organization.

## Effects of transferring a graph

After a graph is transferred, the following occurs:

* The new organization is responsible for paying costs incurred by the graph after the transfer.
* Graph variants and settings are maintained.
* [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are maintained.
* The new organization's members can interact with the graph according to their [organization-wide member roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles).
* All [graph-specific roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-specific-member-roles) from the previous organization are lost.
