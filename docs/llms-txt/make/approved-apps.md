# Source: https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app/approved-apps.md

# Approved apps

Once an app is approved by Make, the code is locked and it starts to be versioned. When a new change is made in the code of the app, it automatically creates Diff files, which contain detailed information about the changes.

Every change made to the app is visible only to you unless we commit it. You can safely add and test new functions and when they are stable, you must follow our guidelines to have the changes checked and released to users.

You should always make sure the [changes will not break](https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app/approved-apps/managing-breaking-changes) existing scenarios.

{% hint style="info" %}
The changes you make will become available only after triggering your scenario in your web browser. This can be done by clicking the **Run once** button, or by selecting the **Run this module only** option after right-clicking on a module with your mouse.

To make the changes available to all users in Make, you must request [approval of the changes](https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app/approved-apps/approval-of-changes-in-approved-app). Once approved, the changes will be available to all users. Additionally, you will have the ability to schedule your scenario with the updated modules that were previously run in "run-once" mode.
{% endhint %}

We recommend you create a new version of the app when there are major changes in the current API and/or there is a new API version available and it is not possible to update the current app without breaking changes.
