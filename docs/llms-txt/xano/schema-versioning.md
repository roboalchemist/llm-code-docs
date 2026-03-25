# Source: https://docs.xano.com/the-database/database-performance-and-maintenance/schema-versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Schema Versioning

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/93IHBZH01L0" title="Schema Versioning" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

You can leverage versioning to help you solve problems, see differences in your work, test ideas, and easily revert back to previous versions. It also tracks who from your team made a change, and when the change was made.

Schema versioning is for database tables, API groups, API endpoints, functions, Addons, and background tasks. It allows you to easily roll back to a previous version in case you make a mistake.

All paid plans have schema versioning enabled. The Essential plan retains 10 previous versions, and the Pro plan retains 20.

## **How to open schema version history**

<Frame caption="Open Version History by selecting Versions from the menu icon.">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7170bde4-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=03c36216c56c80fb725e06e92280ca22" width="960" height="540" data-path="images/7170bde4-image.jpeg" />
</Frame>

View your active (current) version, select from a previous one to roll-back, and see who made a change and when.

<Frame caption="Version History captures which is your active version, a history of previous versions with data on when the change was made and by who, and the ability to select a previous one.">
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/1538ea1c-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=a8ff851459b44f06c568ff2f77e4eda1" width="960" height="540" data-path="images/1538ea1c-image.jpeg" />
</Frame>

Version history will keep track of changes you make anywhere on a query, whether you make a change to a function or a filter. For API endpoints and functions, version history keeps a count of how many inputs, functions, and results were included in each version.

<Frame caption="Counts of each versions' inputs, functions, and results allow you to determine which version you may wish to roll-back to.">
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fc9b9bd1-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=62a9e8877d6b76aaa5a0d1897d6a5daa" width="626" height="675" data-path="images/fc9b9bd1-image.jpeg" />
</Frame>

Tasks will show how many functions and schedules there were for each version.

<Frame caption="Version history of a background task.">
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1a95a496-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=18632dc62e1dfb6ccf8c9339babd0a37" width="960" height="540" data-path="images/1a95a496-image.jpeg" />
</Frame>

Addons will show a count of how many inputs each version had.

<Frame caption="Version history of an Addon.">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/769124d1-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=e74b91e0d2df17cc559233b9ac91e931" width="960" height="540" data-path="images/769124d1-image.jpeg" />
</Frame>

## Compare Differences

When selecting a previous version, you can view a screenshot of the version and the differences compared to the active version. This gives you full context of the different versions to see exactly what changes were made and whether or not you indeed want to revert to the previous version.

### APIs

For example, here is the live version of an API endpoint:

<Frame caption="Example of a live version of a function stack.">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/ab2b9cc7-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=e68dace94b0de93fb1d00f45ea96850f" width="1225" height="907" data-path="images/ab2b9cc7-image.jpeg" />
</Frame>

After selecting Version History, we can see the different versions with some metadata and publish notes about each:

<Frame caption="The available versions of the API endpoint.">
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c70a79d1-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=fd32dd0e531d4f152d273b61f4340a2a" width="502" height="444" data-path="images/c70a79d1-image.jpeg" />
</Frame>

By clicking on a version, in this example we selected version #2, a modal opens showing the differences present in the current live version #4 as compared to the state of version #2.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/45576f73-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=e63c9ac7d3013187df235a7881aacb04" width="1555" height="901" data-path="images/45576f73-image.jpeg" />
</Frame>

The difference comparison tells us a few things.

* The live version (indicated at the top) and when it was created.
* The email of who created the version.
* What differences the live version has compared to the old version selected.
* When the old version was created.
* Indications of what's been changed from the old version compared to the state of things in the live version.

Lastly, you can easily navigate through the screenshots of the different old versions.

<Frame caption="Navigate through the previous versions.">
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/image%20(2).gif?s=700919c50257d88fb0111a3241998e01" width="768" height="490" data-path="images/image (2).gif" />
</Frame>

### Database

Difference comparison in schema versioning is also available on the database. In addition to information about the version number, created at time, and creator. Difference comparison on the database will include differences in:

* Schema (columns)
* Indexes
* View

<Frame caption="An example of comparing version differences of a database table.">
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d13c65ee-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=9a6c794d42d7f31e61a6addad66bcd69" width="1146" height="771" data-path="images/d13c65ee-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).