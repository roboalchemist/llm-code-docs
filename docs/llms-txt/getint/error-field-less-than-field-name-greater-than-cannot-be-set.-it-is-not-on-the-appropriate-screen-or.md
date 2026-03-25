# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/error-field-less-than-field-name-greater-than-cannot-be-set.-it-is-not-on-the-appropriate-screen-or.md

# Error: Field '\<field-name>' cannot be set. It is not on the appropriate screen, or unknown

**Issue**: Field '\<field-name>' cannot be set. It is not on the appropriate screen, or unknown

**Description**: This error message will be displayed if the field in not available in the appropriate screen on **Jira**. For example, when a new ticket is being created in Jira from another App (during Sync), the mapped field should be available in the create screen on Jira. If the value is not available, the error message will be displayed

**Solution**:

There are 2 possible solutions

1. Add the relevant field to the appropriate screen. In the example above, the field should be added to the Create screen in Jira. Jira/Project adminstrators should be able to do this. Below link provides a detailed link to add default/custom fields to a Jira Screen\
   [![](https://wac-cdn.atlassian.com/assets/img/favicons/atlassian/favicon.png)Add, edit, and delete a field configuration | Atlassian Support](https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-a-field-configuration/)
2. Uncheck the field from ‘On Create’ and/or ‘On Update’ (if the field is not on the edit screen) in Getint mappings screen as follows

<br>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdD9RW3Lmo5WGrOiNM391%2Ferror%20field%20name%20cannot%20be%20set.png?alt=media&#x26;token=95b0470f-6992-4728-b681-64229a060efd" alt=""><figcaption></figcaption></figure>
