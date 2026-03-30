# Source: https://firebase.google.com/docs/projects/iam/overview.md.txt

# Manage project access with Firebase IAM

Identity and Access Management (IAM) lets you grant granular access to specific
Firebase and Google resources and prevents unwanted access to other resources.
IAM lets you adopt the
[security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege),
so you grant only the necessary access to your resources.

For a detailed description of IAM, read the
[Google Cloud IAM documentation](https://cloud.google.com/iam/docs/).

## Overview of Firebase IAM

Firebase offers additional IAM options that are specific for Firebase projects
and your project members.

When an authenticated [**project member**](https://firebase.google.com/docs/projects/iam/overview#members) requests an action in
Firebase, IAM makes an authorization decision about whether the project member
has [**permission**](https://firebase.google.com/docs/projects/iam/permissions) to perform the requested
operation on the **resource** . Whether the project member is allowed to perform
the request depends on the project member's assigned [**role**](https://firebase.google.com/docs/projects/iam/overview#roles).
Each role is a collection of permissions, and when you assign a role to a
project member, you are granting that project member all the permissions for
that role.

## Project members

Using Firebase IAM, you assign roles (and their inherent permissions) to your
project members. Project members can be of the following
[types](https://cloud.google.com/iam/docs/overview#concepts_related_identity):

- Google account
- Service account
- Google group

> [!NOTE]
> **Note:** In the Google Cloud console and Google Cloud IAM documentation, project members are called *principals*.

## Roles

**Permissions are granted to your project members via
[*roles*](https://firebase.google.com/docs/projects/iam/roles).** A role is a collection of
[*permissions*](https://firebase.google.com/docs/projects/iam/permissions). When you assign a role to a
project member, you grant that project member all the permissions that the role
contains.

Firebase IAM supports the following types of roles:

- **[Basic roles](https://firebase.google.com/docs/projects/iam/roles-basic)** :
  Fundamental **Owner** , **Editor** , and **Viewer** roles (formerly called
  "primitive" roles).

- **[Predefined roles](https://firebase.google.com/docs/projects/iam/roles-predefined)**:
  Curated Firebase-specific roles that enable more granular access control than
  the basic roles. Firebase offers:

  - [**Firebase-level roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products):
    Roles which grant full read/write or read-only access to *all* the
    Firebase products.

  - [**Product-category roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-category):
    Roles which grant full read/write or read-only access to groups of
    products. They are structured around Google Analytics and general
    product categories.

  - [**Product-level roles**](https://firebase.google.com/docs/projects/iam/roles-predefined-product):
    Roles which grant full read/write or read-only access to *specific*
    Firebase products.

- **[Custom roles](https://firebase.google.com/docs/projects/iam/roles-custom)**: Fully customized
  roles that you create to tailor a set of permissions that meet the specific
  requirements of your organization.

## Manage project members and their roles

> [!NOTE]
> **Note** : Access changes, such as assigning a role or denying a permission, may take several minutes to take effect across all systems. For details, see [Access change propagation](https://cloud.google.com/iam/docs/access-change-propagation) in the Google Cloud documentation.

### View project members and their roles

You can view many of your project members and their roles in the [*Users and permissions* tab](https://console.firebase.google.com/project/_/settings/iam) of \> **Project settings** in the Firebase console. Note the following:

- The Firebase console only lists project members assigned a [basic role](https://firebase.google.com/docs/projects/iam/roles-basic) (Owner, Editor, Viewer) or a [Firebase predefined role](https://firebase.google.com/docs/projects/iam/roles-predefined). The project members listed in this tab are the only project members who have access to the Firebase project in the Firebase console.
- The Firebase console does not list project members that are service accounts. View these project members in the [*IAM* page](https://console.cloud.google.com/iam-admin/iam) of the Google Cloud console.

Alternatively, you can view *all* of your project members and their roles in the [*IAM* page](https://console.cloud.google.com/iam-admin/iam) of the Google Cloud console.

### Assign a role to a project member

To manage the role(s) assigned to each project member, you must be an Owner of the Firebase
project (or be assigned a role with the permission
`resourcemanager.projects.setIamPolicy`).

Here are the places where you can assign and manage roles:

- The Firebase console offers a simplified way to assign roles to project members in the [*Users and permissions* tab](https://console.firebase.google.com/project/_/settings/iam) of \> **Project settings** . In the Firebase console, you can assign any of the [basic roles](https://firebase.google.com/docs/projects/iam/roles-basic) (Owner, Editor, Viewer), the [Firebase Admin/Viewer roles](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), or any of the [Firebase predefined product-category
  roles](https://firebase.google.com/docs/projects/iam/roles-predefined-category).
- The Google Cloud console offers an expansive set of tools to assign roles to project members in the [*IAM* page](https://console.cloud.google.com/iam-admin/iam). In the Cloud console, you can also create and manage [custom roles](https://firebase.google.com/docs/projects/iam/roles-custom), as well as give service accounts access to your project.

  Note that in the Google Cloud console, project members are called *principals*.

If the Owner of your project can no longer perform the tasks of an Owner (for example, the person
left your company) and your project isn't managed via a Google Cloud organization (see next
paragraph), you can
[contact Firebase Support](https://firebase.google.com/support/troubleshooter/contact)
and check with them about how to request access to the Firebase project.

Note that if a Firebase project is part of a Google Cloud organization, it may not have an Owner.
If you're unable to find an Owner for your Firebase project, contact the person who manages your
Google Cloud organization to assign an Owner for the project.