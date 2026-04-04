# Source: https://firebase.google.com/docs/app-distribution/add-remove-testers.md.txt

<br />

iOS+Android  

<br />

This document describes how to add and remove testers in App Distribution, including the following tasks:

- [Add and remove testers from a Firebase project](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-project)
- [Add and remove testers with the Firebase App Distribution API](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-api)
- [Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-group)

## Add and remove testers from a Firebase project

You add and remove testers in the**Testers \& Groups** tab of the[App Distribution page](https://console.firebase.google.com/project/_/appdistribution)in the Firebase console.

If you have a large number of testers, you can use groups to more easily manage tester access to releases. To learn more, see[Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-group).

### Tester limits

Firebase App Distributionhas the following tester limits:

- Add a maximum of 500 testers to a Firebase project

- Add a maximum of 200 testers to anApp Distributiongroup

To add more testers, request a no-cost[limit increase](https://console.firebase.google.com/project/_/appdistribution/limits).

## Add and remove testers with the Firebase App Distribution API

You can use the`testers.batchAdd`and`testers.batchRemove`endpoints in the[Firebase App Distribution API](https://firebase.google.com/docs/reference/app-distribution/rest)to add or remove testers from App Distribution using an HTTP request to the App Distribution API.

## Add and remove testers from a group

You can add and remove testers from groups in the**Testers \& Groups** tab of the[App Distribution page](https://console.firebase.google.com/project/_/appdistribution)in the Firebase console. Groups are useful for managing access to releases for a large number of testers. For example, you could create a group to grant a small group of testers access to an early release of an app. Once you implement feedback from the initial tester group, you can create a group for a larger number of testers.

When you add or remove testers from a group, those testers gain or lose access to*all of the releases*which were distributed to that group.

### Remove a tester from a group

When you remove a tester from a group:

- The tester is removed from*all* releases that they had access to*exclusively*via the group from which they were removed.
- If the tester is a member of a different group which also has access to a release, the tester retains access to that release.

### Delete a group

When you delete a group, all of the testers in that group are removed from all releases that they had access to exclusively via that group. In most cases, group deletion occurs almost immediately; but if you have a large number of testers and releases, the group delete can take longer. After you delete a group, it is no longer listed in the App Distribution page of the Firebase console.

Deleting a group may not take effect immediately; after you delete a group you might temporarily see individual testers from the deleted group listed as having access to a specific release.

## Next steps

- [Import testers from CSV files](https://firebase.google.com/docs/app-distribution/import-testers-csv-files).

- To learn how to increase your internal testing base, see[Create invite links](https://firebase.google.com/docs/app-distribution/create-invite-links).

- To register additional iOS devices manually or programmatically, see[Register additional iOS devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).