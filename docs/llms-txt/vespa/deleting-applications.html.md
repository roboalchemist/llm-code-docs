# Source: https://docs.vespa.ai/en/operations/deleting-applications.html.md

# Deleting Applications

 

 **Warning:** Following these steps will remove production instances or regions and all data within them. Data will be unrecoverable.

## Deleting an application

To delete an application, use the console:

- navigate to the _application_ view at https://console.vespa-cloud.com/tenant/tenant-name/application where you can find the trash can icon to the far right, as an `ACTION`.
- navigate to the _deploy_ view at_https://console.vespa-cloud.com/tenant/tenant-name/application/app-name/prod/deploy_.

![delete production deployment](/assets/img/console/delete-production-deployment.png)

When the application deployments are deleted, delete the application in the [console](https://console.vespa-cloud.com). Remove the CI job that builds and deploys application packages, if any.

## Deleting an instance / region

To remove an instance or a deployment to a region from an application:

1. Remove the `region` from `prod`, or the `instance` from `deployment`in [deployment.xml](../reference/applications/deployment.html#instance):

2. Add or modify [validation-overrides.xml](../reference/applications/validation-overrides.html), allowing Vespa Cloud to remove production instances:

3. Build and deploy the application package.

 Copyright © 2026 - [Cookie Preferences](#)

