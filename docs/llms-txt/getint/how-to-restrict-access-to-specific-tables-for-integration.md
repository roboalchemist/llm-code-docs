# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/how-to-restrict-access-to-specific-tables-for-integration.md

# How to Restrict Access to Specific Tables for Integration

### Use Case

If you want to restrict full access to specific tables in ServiceNow for certain companies during integration, you can do this by adding Business Rules. This allows you to specify which tables you don't want to provide access to.

For example, if you only want to integrate **Incidents** and not **Change Requests**, you can restrict access to the **ChangeRequest** table.

**Scenario:**

Integrating **ChangeRequest** (ServiceNow) ↔︎ **Story** (Jira)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F89VjCIC2qnPTQ6ylF4UY%2FSample%20integration%20ChangeRequest%20(ServiceNow)%20%E2%86%94%EF%B8%8E%20Story%20(Jira).png?alt=media&#x26;token=795bdd75-187f-4992-938e-c29c50664614" alt=""><figcaption><p>Sample integration ChangeRequest (ServiceNow) ↔︎ Story (Jira)</p></figcaption></figure>

If you restrict access to the **ChangeRequest** table, attempting to create a Story in Jira will result in an error when trying to create a ChangeRequest in ServiceNow. This error will appear in the Getint integration logs.

### How to Deny Access to the ChangeRequest Table

* Go to **Administration > Business Rule**.
* Follow the steps shown in the images below to create a new Business Rule.
* Configure the fields as shown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgQUwb9bzErjDdpGYzXuM%2FCreating%20a%20new%20business%20rule.png?alt=media&#x26;token=98818c48-552c-4ca5-9755-f67eb6c12dc6" alt=""><figcaption><p>Create a new Business Rule</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F85nyiaXZWW6BfFi7xeBk%2FBusiness%20Rule%20configuration%20for%20SNOW%20getint%20integration.png?alt=media&#x26;token=f13134e0-8285-498a-9e9e-d34144ad28c6" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fpq5zipQLXyYG4vy4JimR%2FRestrict%20Change%20Request.png?alt=media&#x26;token=b226bb33-5047-42e3-8e24-4a9dc3b4fc0e" alt=""><figcaption><p>Go to the Advanced tab and paste the script shown below</p></figcaption></figure>

* In the **Advanced** tab, paste the following script to block access to the **ChangeRequest** table:

```
(function executeRule(current, previous) {
 // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        return; // Allow admins to proceed
    }
    // Abort any operation on the change_request table
    current.setAbortAction(true); // Prevent any operation from completing
    // Apply a query that results in no records being returned
    current.addQuery('number', "00000000000"); // An invalid query to ensure no records are returned
})(current, previous);
```

This script will prevent any operation (Insert, Update, Query, or Delete) from happening on the **ChangeRequest** table by aborting the action and returning no records.

### How to Restrict Access to Other Tables

To restrict access to other tables, simply repeat the steps described above for the **ChangeRequest** table.

The only change required is to select a different table in the **Table** field. You can restrict access to various tables such as:

* **Requested Item**
* **Incident**
* **Incident Task**
* **Problem**
* Other tables like **sys\_dictionary** or **journal\_field\_type** which we may have allowed access to in previous ACLs.

### Summary

By following this approach, you can ensure that companies only access the tables necessary for their integration and block unwanted access to other tables.

If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
