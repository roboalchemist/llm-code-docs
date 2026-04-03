# Source: https://firebase.google.com/docs/projects/dev-workflows/general-best-practices.md.txt

This page provides general, high-level best practices for setting up Firebase projects and registering your apps with a project so that you have a clear[development workflow](https://firebase.google.com/docs/projects/dev-workflows/overview-environments)that use distinct environments. Once you're familiar with the best practices on this page, check out our[general security guidelines](https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines).
| **Key Point:** We recommend reading our guides thoroughly, but here's the top takeaway about development workflows:  
| **Firebase recommends using a*separate* Firebase project for*each*environment in your development workflow.**

## Understanding the hierarchy of Firebase projects

![Diagram showing the basic hierarchy of a Firebase project, including the project, its registered apps, and its provisioned resources and services](https://firebase.google.com/docs/projects/images/firebase-projects-hierarchy_projects-apps-resources.png)This diagram shows the basic hierarchy of a Firebase project. Here are the key relationships:

- A**Firebase project**is like a container for all your apps and any resources and services provisioned for the project.

- A Firebase project can have one or more**Firebase Apps**registered to it (for example, both the iOS and Android versions of an app, or both the free and paid versions of an app).

- All Firebase Apps registered to the same Firebase project**share and have access to all the same resources and services provisioned for the project**. Here are some examples:

  - All the Firebase Apps registered to the same Firebase project share the same backends, likeFirebase Hosting,Authentication,Realtime Database,Cloud Firestore,Cloud Storage, andCloud Functions.

  - All Firebase Apps registered to the same Firebase project are associated with the same Google Analytics property, where each Firebase App is a separate data stream in that property.

### Where does aGoogle Cloudproject fit into this hierarchy?

One aspect of the Firebase project hierarchy that's not shown in the diagram above is the relationship with aGoogle Cloudproject.**A Firebase project is actually just aGoogle Cloudproject that has additional*Firebase-specific*configurations and services enabled for it.** Note that all the apps registered to the same Firebase project also share and have access to all the sameGoogle Cloudresources and services, too.

Learn more about the Firebase andGoogle Cloudrelationship in[Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)

## Registering app variants with Firebase projects

| **Key Point:** All the apps registered to a Firebase project share and can access the same data as well as the resources and services provisioned for the project, which includes database instances, storage buckets, functions, etc.

Here are some important tips for registering your app variants with a Firebase project:

- Ensure that all apps registered to a Firebase project are**platform variants of the same application** from an end-user perspective. Register the iOS, Android, and web versions of the same app or game with the*same*Firebase project.

- If you have**multiple build variants that could*share the same Firebase resources*** , register the variants with the*same*Firebase project. Some examples are a blog and a web app in the same project, or both the free and paid versions of the same app in the same project.

- If you have**multiple build variants that are*based on release status*** (rather than on common end-user activity or access, like above), register each variant with a*separate*Firebase project. An example is your debug vs release build -- register each of these builds in its own Firebase project.

  - Builds based on release status should not share the same Firebase resources because that risks your debug data polluting or even overriding your prod data.

  - The*platform* -variants of each of these build variants should be in the*same*Firebase project. For example, register both the iOS and the Android debug builds in a "dev" Firebase project because they can both interact with the same non-prod data and resources.

| **Note:** For each Android app, if you provide a SHA-1 key for the app, you need to provide a package name and SHA-1 key combination that is globally unique across all ofGoogle Cloud.

### Avoiding multi-tenancy

| **Key Point:** Connecting several different logically independent apps and/or web sites to a single Firebase project (often called "multi-tenancy") is not recommended.

Multi-tenancy can lead to serious configuration and data privacy concerns, including unintended issues with analytics aggregation, shared authentication, overly-complex database structures, and difficulties with security rules.

Generally,**if a set of apps don't share the same data and configurations, strongly consider registering each app with a different Firebase project.**

For example, if you develop a white-label application, each independently labeled app should have its own Firebase project, and the iOS and Android versions of that label should be in the same Firebase project. Each independently labeled app shouldn't (for privacy reasons) share data with the others.

## Next steps

- Review the[general security guidelines](https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines)for different environments. You want to make sure each environment and its data are secure.

- Review the[Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).