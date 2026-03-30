# Source: https://help.aikido.dev/getting-started/general-information/enhancing-security-with-access-control-checks.md

# Access Control Checks

Aikido's checks on Access Controls offers robust security by informing about critical access control practices. This way, you can ensure that only authorized and verified changes are made to your codebase. Some examples of checks are multi-factor authentication, restricting default access rights, and requiring mandatory code reviews.

> All Access Controls checks [can be found here](https://app.aikido.dev/repositories/access_control).

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* Only available for GitHub & GitLab connected workspaces.

### Access Control Setup for GitHub <a href="#access-control-setup-for-github" id="access-control-setup-for-github"></a>

> For GitLab, no extra authorisation steps need to be taken.

**Step 1.** In the Main Feed, filter on **Access Controls.** Click **Authorise on GitHub** in order to allow Aikido scan for configurations related the access controls.

![Access controls filter active; Aikido requests extra GitHub permissions for analysis.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2f1deb6c6f469d2084befeb5497820727f0152a3%2Fenhancing-security-with-access-control-checks_a13fd024-3a98-4ee5-9e3f-9f4c50f66760.png?alt=media)

**Step 2.** In GitHub, grant permissions to **install** the Aikido GitHub Config Scanner. It is recommended to select **All Repositories**.

![Installing Aikido GitHub Config Scanner with repository and organization read access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b735d8126097d001d8e70d1870b922357baee7fd%2Fenhancing-security-with-access-control-checks_f8ad227e-3483-4118-9dcd-a32af3acf7ca.png?alt=media)

**Step 3.** After connecting, Aikido will do a scan for [checks mentioned here. ](https://app.aikido.dev/repositories/access_control)After a couple of minutes, you will be able to view them in the Aikido feed. The sidebar will give more information about which repos need configuration adjustments.

![Access control security issues listed by severity and estimated fix time.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f154d3154b9be3c3e7b263b2d75062e97284a749%2Fenhancing-security-with-access-control-checks_6b6bed8d-ee13-4d87-b0bb-47e2ac5dfe74.png?alt=media)
