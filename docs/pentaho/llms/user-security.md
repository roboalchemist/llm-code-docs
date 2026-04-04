# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security.md

# User security

You can choose from two different user security options: Pentaho Security or advanced security providers (such as LDAP, Single Sign-On, or Microsoft Active Directory).

For the Pentaho User Console (PUC), your predefined users and roles can be used if you are already using a security provider such as Lightweight Directory Access Protocol (LDAP), Microsoft Active Directory (MSAD), or Single Sign-On (SSO). Pentaho Data Integration (PDI) can also be configured to use your implementation of these providers or Kerberos to authenticate users and authorize data access.

These articles guide you through the process of configuring third-party security frameworks for the Pentaho Server.

**Note:** If you are evaluating Pentaho or have a production environment with fewer than a hundred users, you may decide to use Pentaho default security. See the **Install Pentaho Data Integration and Analytics** document for details.

Before you can implement advanced security, you must have installed and configured the Pentaho Server. You should have administrative-level knowledge of the security provider you want to use, details about your user community, and a plan for the user roles to be used in PDI. You should also know how to use the command line to issue commands for Microsoft Windows or Linux.

PUC can be use to perform most security tasks pertaining to the console. For some cases with PDI, you will need a text editor to modify text files. Some of these security tasks also require that you work on the actual machine where the Pentaho Server is installed.

All of the tasks that use the Administration page in PUC require that you log on to the User Console with the Pentaho administrator user name and password.

For information on the two different user security options you can choose from, see the following topics:

* [Pentaho Server security](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security)
* [Advanced security providers](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers)
