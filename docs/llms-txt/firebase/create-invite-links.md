# Source: https://firebase.google.com/docs/app-distribution/create-invite-links.md.txt

<br />

Invite links are an optional way to increase your internal testing base by letting users add themselves to your list of app testers. An*invite link*is a unique URL that lets testers enter their email addresses to sign up to test an app.

There are two types of invite links:

- Invite link to an app, with no group selected
- Invite link to a group

If you use an invite link with a group attached, testers are added to all releases across all apps that the group has access to. If you use an invite link without a group, testers are only added to the latest distributed release of the app which they are invited to test. To learn more about groups, see[Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-group).

You create an invite link in the**Invite links** tab of the[App Distribution page](https://console.firebase.google.com/project/_/appdistribution)of theFirebaseconsole. You can enable the**Restrict invitation acceptance to recipient's email** toggle in the**Testers \& Groups**tab to add a restriction on which emails your testers can use to accept testing invitations.

The toggle will require testers to accept invitations using the Google Account with the same email address that they received the invitation. By default, this toggle is disabled.
| **Note:** If account restrictions are enabled, invite links require that domain restrictions are also enabled.

## Next steps

- To add and remove testers, see[Add and remove testers inApp Distribution](https://firebase.google.com/docs/app-distribution/add-remove-testers).

- [Import testers from CSV files](https://firebase.google.com/docs/app-distribution/import-testers-csv-files).

- To register additional iOS devices manually or programmatically, see[Register additional iOS devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).