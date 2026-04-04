# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-your-docker-containers-with-clusters-docker-deployment/use-the-docker-command-tool-with-a-kerberos-secured-cluster-docker-deployment.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-your-docker-containers-with-clusters-docker-deployment/use-the-docker-command-tool-with-a-kerberos-secured-cluster-docker-deployment.md

# Use the Docker command tool with a Kerberos secured cluster

Adding a Kerberos secure cluster connection requires additional changes to the `generatedFiles` directory. You must change the `dockerfile` file to bring in the additional dependencies and install SSL keys. For this example, the cluster is defined to use a username and password rather than a keytab. Using a keytab requires an additional ADD command to add the keytab file.

Perform the steps to prepare a container to work with a Kerberos secured cluster:

1. Run `DockMaker` without the `-X` parameter to prepare the `generatedFiles` directory but not build the image or compose the container.
2. Copy the resulting not executed `docker build` and `docker compose` commands from the output to another (different) location for later use.
3. Copy your `krb5.conf` and `cacerts.pem` files to the `generatedFiles` directory.

   Any files copied to the container must be in the `generatedFiles` context to be available, which is a restriction imposed by Docker.
4. Edit the `generatedFiles/dockerfile` file to add the following lines close to the bottom of the file but make sure they appear above the `USER ${PENTAHO_USER}` line as that root must be defined to execute this additional code:

   ```
   RUN apt-get install -y krb5-user
   ADD krb5.conf /etc/krb5.conf
   ADD cacerts.pem /tmp/cacerts.pem
   RUN /usr/bin/keytool -import -noprompt -alias clustername -keystore /etc/ssl/certs/java/cacerts -file /tmp/cacerts.pem -storepass changeit;

   ```

   where *clustername* is the name of your cluster.
5. Run the `docker build` command you previously copied.
6. Run the `docker compose` command you previously copied.

You now have a running instance with Kerberos support. You can update your template `dockerfile` files to make sure these lines are always added to the `dockerfile` when `generatedFiles` is first created. The template `dockerfiles` are in the following locations:

* **Server**

  `containers\pentaho-server\pentaho-server-auto\Dockerfile`
* **PDI**

  `containers\pentaho-data-integration\pdi-client-auto\Dockerfile`
* **Carte**

  `containers\pentaho-data-integration\pdi-client-auto\Dockerfile`
