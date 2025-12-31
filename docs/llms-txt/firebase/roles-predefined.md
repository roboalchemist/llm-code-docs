# Source: https://firebase.google.com/docs/projects/iam/roles-predefined.md.txt

**Firebase predefined roles**are the curated Firebase-specific roles that enable more granular access control than the basic roles (formerly called "primitive" roles). You can assign more than one role to each project member.

By using predefined roles, you can grant different*access levels* (Admin versus Viewer) as well as*breadth of access*(individual products versus groups of products).

- [**Firebase-level roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products): Roles which grant full read/write or read-only access to*all* the Firebase products.  
  You can assign the Firebase-level roles using the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/iam).

- [**Product-category roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-category): Roles which grant full read/write or read-only access to groups of products. They are structured aroundGoogle Analyticsand general product categories.  
  You can assign the Firebase product-category roles using the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/iam).

- [**Product-level roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-product): Roles which grant full read/write or read-only access to*specific* Firebase products.  
  You can assign the Firebase product-level roles using the[Google Cloudconsole](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

Note that, when needed, predefined roles automatically include permissions which are:

- [Required to use any Firebase product or service.](https://firebase.google.com/docs/projects/iam/permissions#required_all_roles)

- [Required to perform some Firebase service-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_service)

- [Required to perform some Firebase management-specific actions.](https://firebase.google.com/docs/projects/iam/permissions#required_firebase_management)