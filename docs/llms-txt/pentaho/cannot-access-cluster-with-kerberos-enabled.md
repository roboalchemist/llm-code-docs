# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/cannot-access-cluster-with-kerberos-enabled.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/cannot-access-cluster-with-kerberos-enabled.md

# Cannot access cluster with Kerberos enabled

If a step or entry cannot access a Kerberos authenticated cluster, review the steps in **Set up Kerberos for Pentaho** in the **Administer Pentaho Data Integration and Analytics** document.

If this issue persists, verify that the username, password, UID, and GID for each impersonated or spoofed user is the same on each node. When a user is deleted and recreated, it may then have different UIDs and GIDs causing this issue.
