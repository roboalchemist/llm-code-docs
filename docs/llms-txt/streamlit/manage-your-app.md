# Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app

# Manage your app

You can manage your deployed app from your workspace at [share.streamlit.io](https://share.streamlit.io/) or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## Manage your app from your workspace

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to their repository's owner in GitHub. Your workspace is indicated in the upper-left corner. For more information, see [Switching workspaces](/deploy/streamlit-community-cloud/get-started/explore-your-workspace#switching-workspaces).

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

### Sort your apps

If you have many apps in your workspace, you can pin apps to the top by marking them as favorite (i.e., `star`).

### App overflow menus

Each app has a menu accessible from the overflow icon (i.e., `more_vert`) to the right.

- **Edit with Codespaces** — See [Edit your app with GitHub Codespaces](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces)
- **Reboot** — See [Reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
- **Delete** — See [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
- **Analytics** — See [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
- **Settings** — See [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings)

### Resource limits

All Community Cloud users have access to the same resources and are subject to the same limits. These limits may change at any time without notice. If your app meets or exceeds its limits, it may slow down from throttling or become nonfunctional. The limits as of February 2024 are approximately as follows:

- CPU: 0.078 cores minimum, 2 cores maximum
- Memory: 690MB minimum, 2.7GBs maximum
- Storage: No minimum, 50GB maximum

Symptoms that your app is running out of resources include the following:

- Your app is running slowly.
- Your app displays `🤯 This app has gone over its resource limits.`
- Your app displays `😦 Oh no.`

### Good for the world

Streamlit offers increased resources for apps with good-for-the-world use cases. Generally, these apps are used by an educational institution or nonprofit organization, are part of an open-source project, or benefit the world in some way. If your app is not primarily used by a for-profit company, you can [apply for increased resources](https://info.snowflake.com/streamlit-resource-increase-request.html).

### Optimizing your app

If your app is running slow or showing the error pages mentioned above, we first highly recommend going through and implementing the suggestions in the following blog posts to prevent your app from hitting the resource limits and to detect if your Streamlit app leaks memory:

- [Common app problems: Resource limits](https://blog.streamlit.io/common-app-problems-resource-limits/)
- [3 steps to fix app memory leaks](https://blog.streamlit.io/3-steps-to-fix-app-memory-leaks/)

If your app exceeds its resource limits, developers and viewers alike will see `😦 Oh no.`

### Developer view

All apps without traffic for 12 hours go to sleep. Community Cloud hibernates apps to conserve resources and allow the best communal use of the platform. To keep your app awake, simply visit your app.

When someone visits a sleeping app, they will see the sleeping page:

To wake the app up, click `Yes, get this app back up!` This can be done by anyone who has access to view the app, not just the app developer!

You can see which of your apps are asleep from your workspace. Sleeping apps have a moon icon (i.e., `bedtime`) to the right.

### App hibernation

All apps without traffic for 12 hours go to sleep. Community Cloud hibernates apps to conserve resources and allow the best communal use of the platform. To keep your app awake, simply visit your app.

When someone visits a sleeping app, they will see the sleeping page:

To wake the app up, click `Yes, get this app back up!` This can be done by anyone who has access to view the app, not just the app developer!

You can see which of your apps are asleep from your workspace. Sleeping apps have a moon icon (i.e., `bedtime`) to the right.