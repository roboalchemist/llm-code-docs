# Source: https://firebase.google.com/docs/extensions/permissions-granted-to-extension.md.txt

<br />

For aFirebase Extensionto perform its specified actions, Firebase grants each instance of an installed extension limited access to your project and data via a***service account***.

## What's a service account?

**A[service account](https://cloud.google.com/iam/docs/understanding-service-accounts)is a special type of Google user account. It represents a non-human user that's authorized to access data using Google APIs.**

During installation of an extension, Firebase creates a service account in your project. Each installed instance of an extension has its own service account.

Firebase limits access to your project and data by assigning an extension's service account specific[***roles***(bundles of permissions)](https://firebase.google.com/docs/projects/iam/roles). The roles that an extension requires to operate are determined by Firebase during extension development. At installation, Firebase assigns these roles to an extension's service account, and you shouldn't modify, add to, or delete any of these assigned roles (otherwise your installed extension won't work as expected). You can, though,[uninstall the extension](https://firebase.google.com/docs/extensions/permissions-granted-to-extension#uninstall-extension), which deletes the service account (and its access) altogether.

Service accounts created for extensions are in the format:**ext-** <var translate="no">extension-instance-id</var>***@*** <var translate="no">project-id</var>**.iam.gserviceaccount.com**.

You can view all the service accounts associated with your Firebase project in the[*Service accounts*](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)tab of yoursettings*Project settings*.

## Permissions and roles

During development of an extension, Firebase determines the level of access that an extension requires to operate.

Firebase defines this level of access by explicitly listing the***roles*** (bundles of permissions) that Firebase should assign to the extension's[service account](https://firebase.google.com/docs/extensions/permissions-granted-to-extension#service-account)during installation of the extension.

Each role (and its inherent permissions) is based on a specific product or service. Examples of roles are`firebasehosting.admin`,`bigquery.dataEditor`, and`firebasedatabase.admin`. Firebase lists the required roles for an extension in the extension's specification file (the[`extension.yaml`file](https://firebase.google.com/docs/extensions/overview-use-extensions#view-source-code)).

For officialFirebaseextensions, Firebase thoroughly reviews this list of roles to ensure that an extension's access is strictly limited to the scope of the extension's tasks. You can also review and confirm for yourself the access granted to an extension by viewing the extension's details page in the[Firebase Extensionsdashboard](https://console.firebase.google.com/project/_/extensions/)or viewing its[`README`file](https://firebase.google.com/docs/extensions/overview-use-extensions#view-source-code).

Learn about the permissions included in each role:

- [Firebase product-level roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product)
- [Google Cloudroles](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles)

## What happens when I uninstall an extension?

When you[uninstall an extension](https://firebase.google.com/docs/extensions/manage-installed-extensions#uninstall)from your project, Firebase deletes the[service account](https://firebase.google.com/docs/extensions/permissions-granted-to-extension#service-account)created for that instance of the extension. After this deletion of the service account, the extension cannot run in your project because it no longer has any access rights to your project or data.