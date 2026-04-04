# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client/configure-cdp-public-cloud-cluster-with-the-pdi-client-connecting-to-a-hadoop-cluster-with-the-pdi-c.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client/configure-cdp-public-cloud-cluster-with-the-pdi-client-connecting-to-a-hadoop-cluster-with-the-pdi-c.md

# Configure CDP Public Cloud cluster with the PDI client

If you are working with a CDP Public Cloud cluster in the PDI client, you must perform some additional configuration steps.

CDP Public Cloud’s datahub cluster offerings have gateway nodes for installing any third-party applications that need access to those clusters. Before you begin, install gateway nodes for running Pentaho. Use CentOS to deploy these gateway nodes.

For additional information about how to connect to the Cloudera Data Platform (CDP), see the advanced settings section in the **Install Pentaho Data Integration and Analytics** document.

Perform the following steps to configure the CDP Public Cloud cluster to work with the PDI client:

1. Use `sudo su` to log in as a `root` user and add users to `sudoers` list, as shown in the following example code:

   ```
   usermod -a -G wheel username
   ```

   **Note:** To install packages, we need `sudo` access. To attain that access, log (SSH) into the cluster gateway node as the `cloudbreak` user.
2. Install `tigervnc-server` to access the gateway node with the user interface, as shown in the following example:

   ```
   sudo yum install tigervnc-server
   vncpasswd
   vncserver
   ```

   The `vncpasswd` command is used to set a password for the VNC login and the `vncserver` command is used to start the VNC viewer.
3. Install `libwebkitgtk-1.0.0` in the gateway node. As this module is deprecated and not present in CentOS repository, you must install `webkitgtk` using a third-party RPM called `nux-dextop`, as shown in the following example commands:

   ```
   sudo rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
   sudo yum -y install epel-release && sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-05.el7.nux.noarch.rpm
   sudo yum install webkitgtk
   ```
4. Verify Kerberos is pre-installed and set up on the cluster:
   1. Download the keytab for the Cloudera Management Console.
   2. Upload the keytab to the gateway node.
   3. Run either one of the following commands:
      * ```
        ```

kinit

````

        -   ```
kinit -kt <keytab_location> username
````
