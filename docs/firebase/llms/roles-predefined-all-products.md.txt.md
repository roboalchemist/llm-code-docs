# Source: https://firebase.google.com/docs/projects/iam/roles-predefined-all-products.md.txt

# Firebase-level predefined roles

These roles grant full read/write or read-only access to *all* Firebase
products.

Assign these Firebase-level roles to project members using the
[Firebase console](https://console.firebase.google.com/project/_/settings/iam)
or the
[Google Cloud console](https://console.cloud.google.com/iam-admin/iam).

> [!NOTE]
> **Note:** If you want more granular predefined roles for your project members, you can assign [product-category roles](https://firebase.google.com/docs/projects/iam/roles-predefined-category) or [product-level roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).

| Role | Description | Permissions |
|---|---|---|
| **Firebase Admin** `roles/firebase.admin` | Full read/write access to all Firebase services | **Firebase Admin** permissions All the permissions included with: - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#analytics_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#develop_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#grow_roles` - `https://firebase.google.com/docs/projects/iam/permissions#test-lab` - `https://firebase.google.com/docs/projects/iam/permissions#test-lab` Additional permissions: - clientauthconfig.clients.create - clientauthconfig.clients.delete - clientauthconfig.clients.update - firebase.billingPlans.update - firebase.clients.create - firebase.clients.delete - firebase.clients.undelete - firebase.clients.update - firebase.links.create - firebase.links.delete - firebase.links.update - firebase.playLinks.update - firebase.projects.delete - firebase.projects.update Additional access: Install and manage Firebase Extensions |
| **Firebase Viewer** `roles/firebase.viewer` | Read-only access to all Firebase services | **Firebase Viewer** permissions All the permissions included with: - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#analytics_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#develop_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles` - `https://firebase.google.com/docs/projects/iam/roles-predefined-category#grow_roles` - `https://firebase.google.com/docs/projects/iam/permissions#test-lab` Additional access: View installed Firebase Extensions |

> [!IMPORTANT]
> **Important:** The `FirebaseAdmin` and `FirebaseViewer` roles are applicable for projects that are already set up as Firebase projects. Note that to call the [`AddFirebase` endpoint](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase), a project member must be an Editor or Owner for the existing Google Cloud project.