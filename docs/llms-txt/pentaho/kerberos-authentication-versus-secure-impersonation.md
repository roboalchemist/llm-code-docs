# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation.md

# Kerberos authentication versus secure impersonation

Kerberos authentication occurs when Pentaho users connect to a cluster with a default Kerberos principal. All the Pentaho users connect to the cluster with the same Kerberos principal.

In secure impersonation, users connect to the cluster as a proxy user. The Pentaho user ID matches the cluster user ID in a one-on-one mapping. Resources are accessed and processes are executed as the cluster user.

Secure impersonation occurs if the following criteria are met:

1. Pre-defined credentials can authenticate to a Kerberos server before connecting to the cluster.
2. The Pentaho Server is configured for secure impersonation.
3. The cluster is secured.

For information on enabling secure impersonation and Kerberos authenticaion, see the following topics:&#x20;

* [Prerequisites](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/prerequisites)
* [Supported components](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/supported-components)
* [How to enable secure impersonation](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-secure-impersonation)
* [How to enable Kerberos authentication](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication)
