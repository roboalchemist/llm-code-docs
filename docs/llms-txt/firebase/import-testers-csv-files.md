# Source: https://firebase.google.com/docs/app-distribution/import-testers-csv-files.md.txt

<br />

Importing testers from comma-separated values (CSV) files is useful when you want to grant release access to many testers. This feature saves you the effort of manually entering individual tester email addresses. You can use groups to share future releases with the group you created.

After you create a group, you upload a CSV file containing tester emails in the**Testers \& Groups** tab of the[App Distribution page](https://console.firebase.google.com/project/_/appdistribution)in the Firebase console. You then import the tester emails from the CSV file to the group. The CSV file must contain the testers' email addresses in the first column. All additional columns are ignored. For example:  

    ali@example.com
    bri@example.com,This is Ignored,This also
    cal@example.com,Cal Nguyen (ignored)

## Next steps

- To add and remove testers, see[Add and remove testers inApp Distribution](https://firebase.google.com/docs/app-distribution/add-remove-testers).

- Learn how to increase your internal testing base by[creating invite links](https://firebase.google.com/docs/app-distribution/create-invite-links).

- To register additional iOS devices manually or programmatically, see[Register additional iOS devices](https://firebase.google.com/docs/app-distribution/register-additional-devices).