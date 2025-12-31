# Source: https://docs.upsun.com/create-apps/multi-app.md

# Set up multiple apps in a single project


You can create multiple apps within a single project so they can share data.
This can be useful if you have several apps that are closely related,
such as a backend-only CMS and a frontend system for content delivery and display.

No matter how many apps you have in one project, they're all served by a single [router for the project](https://docs.upsun.com/create-apps/multi-app/routes.md).
To allow your apps to communicate with each other, [create relationships](https://docs.upsun.com/create-apps/multi-app/relationships.md).
Each app separately defines its relationships to [services](https://docs.upsun.com/add-services.md),
so apps can share services or have their own.

