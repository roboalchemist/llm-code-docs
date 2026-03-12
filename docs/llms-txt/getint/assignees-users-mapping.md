# Source: https://docs.getint.io/getintio-platform/workflows/assignees-users-mapping.md

# Assignees (Users) Mapping

Mapping users across different IDs is crucial for synchronizing Assignee fields accurately. For instance, in Jira Cloud, a user might be identified by an account ID hash, while in Jira Server, it could be a username. Similarly, in Asana, users may have different IDs. To properly synchronize these fields, we manually identify which user represents the same person. For example, James Farrell might be named James in Jira and James F in Asana. Without proper mapping, Getint cannot automatically interpret that these are the same user.

{% embed url="<https://www.loom.com/share/6a3ea8422fef448d950de983358afe02?sid=ffedae49-cb9e-4d71-94fa-561b91de6e34>" %}
Mapping assigness / users
{% endembed %}

### How to Map Assignees <a href="#how-to-map-assignees" id="how-to-map-assignees"></a>

1. Go to your integration and open your type mapping.
2. Click on "+ Add Field Mapping" and select the corresponding option for Assignees in every app.
3. Click on your new Assignees mapping, and scroll down to "Map available options." Make sure to select the options that represent the same user. Click on "Apply" to save your mapping configuration. Then, click on "Save" to persist with your changes.

If a user was not found on the mapped options list, please verify you’re selecting the correct field for Assignees, depending on your app, and confirm that the users exist for both instances. For example, other apps have the Assignee named "Assigned to or Owner."

### How to Set Default Users <a href="#how-to-set-default-users" id="how-to-set-default-users"></a>

With "Default mapping," you can designate a specific user or value as the primary assignee for both instances. For example, when synchronizing tasks through your integration, you can ensure that all tickets from Asana are assigned to Carlos in Jira, and all tickets from Jira are assigned to Julian in Asana.

### Copying Mapped Users from One Type Mapping to Another  <a href="#copying-mapped-users-from-one-type-mapping-to-another" id="copying-mapped-users-from-one-type-mapping-to-another"></a>

This feature allows users to effortlessly transfer mapped users from one type of mapping to another within the integration settings. Easily replicate user assignments from one app to another, streamlining your workflow and ensuring consistency across platforms.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
