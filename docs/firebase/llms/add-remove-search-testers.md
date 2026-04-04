# Source: https://firebase.google.com/docs/app-distribution/add-remove-search-testers.md.txt

<br />

iOS+Android  

<br />

This document describes how to add and remove testers inApp Distribution, including the following tasks:

- [Add, remove, and search for testers in a Firebase project](https://firebase.google.com/docs/app-distribution/add-remove-search-testers#add-remove-search-testers-project)
- [Add testers using invitation restrictions](https://firebase.google.com/docs/app-distribution/add-remove-search-testers#add-using-invitation-restrictions)
- [Add and remove testers with theFirebase App DistributionAPI](https://firebase.google.com/docs/app-distribution/add-remove-search-testers#add-remove-testers-api)
- [Add, remove, and search for testers in a group](https://firebase.google.com/docs/app-distribution/add-remove-search-testers#add-remove-search-testers-group)

## Add, remove, and search for testers in a Firebase project

The search function lets you check for specific testers that you have added to your Firebase project. If you have a large number of testers, you can quickly search for individual testers, by their email address or name, using the search bar at the top of the group's page. Note that the search function requires that you know the email address or name of the tester that you are searching for.

You can add, remove, and search for testers in the**Testers \& Groups** tab of the[App Distributionpage](https://console.firebase.google.com/project/_/appdistribution)in the Firebase console.

To add a tester from the**Testers \& Groups**tab to your Firebase project:

1. Click the**Add tester**button next to the search bar.
2. Enter the tester's email address.
3. Click**Add tester**.

Your tester is now added to your Firebase project. To give the tester access to a release, add the individual tester to a release or add the tester to a group that has access to a release.

### Tester limits

Firebase App Distributionhas the following tester limits:

- Add a maximum of 500 testers to a Firebase project

- Add a maximum of 200 testers to anApp Distributiongroup

To add more testers, request a no-cost[limit increase](https://console.firebase.google.com/project/_/appdistribution/limits).

## Add testers using invitation restrictions

You can use the**Restrict invitation acceptance to recipient's email** toggle in the**Testers \& Groups**tab to add a restriction on which emails your testers can use to accept testing invitations.

This toggle will require testers to accept invitations using the Google Account with the same email address that they received the invitation. By default, this toggle is disabled.

## Add and remove testers with theFirebase App DistributionAPI

You can use the`testers.batchAdd`and`testers.batchRemove`endpoints in the[Firebase App DistributionAPI](https://firebase.google.com/docs/reference/app-distribution/rest)to add or remove testers from App Distribution using an HTTP request to the App Distribution API.

## Add, remove, and search for testers from a group

The search function lets you check for specific testers that you have added to a group. If you have a large number of groups, you can quickly search for individual testers, by their email address or name, using the search bar at the top of the group's page. Note that the search function requires that you know the email address or name of the tester that you are searching for.

You can add, remove, and search for testers from groups in the**Testers \& Groups** tab of the[App Distributionpage](https://console.firebase.google.com/project/_/appdistribution)in the Firebase console. Groups are useful for managing access to releases for a large number of testers. For example, you could create a group to grant a small group of testers access to an early release of an app. Once you implement feedback from the initial tester group, you can create a group for a larger number of testers.

To add a tester to a specific group, follow these steps:

1. Click the group's name.
2. Click the**Add testers**button next to the search bar.
3. Enter the tester's email address.
4. Click**Add tester**.

When you add or remove testers from a group, those testers gain or lose access to*all of the releases*which were distributed to that group.

### Remove a tester from a group

When you remove a tester from a group:

- The tester is removed from*all* releases that they had access to*exclusively*via the group from which they were removed.
- If the tester is a member of a different group which also has access to a release, the tester retains access to that release.

### Delete a group

When you delete a group, all of the testers in that group are removed from all releases that they had access to exclusively via that group. In most cases, group deletion occurs almost immediately; but if you have a large number of testers and releases, the group delete can take longer. After you delete a group, it is no longer listed in theApp Distributionpage of the Firebase console.

Deleting a group may not take effect immediately; after you delete a group you might temporarily see individual testers from the deleted group listed as having access to a specific release.

## Next steps

- [Import testers from CSV files](https://firebase.google.com/docs/app-distribution/import-testers-csv-files).

- To learn how to increase your internal testing base, see[Create invite links](https://firebase.google.com/docs/app-distribution/create-invite-links).

- To register additional iOS devices manually or programmatically, see[Register additional iOS devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).