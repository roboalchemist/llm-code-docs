# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/set-up-a-google-compute-engine-instance-for-pdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/set-up-a-google-compute-engine-instance-for-pdi.md

# Set up a Google Compute Engine instance for PDI

The PDI client must be run from within the Google Compute Engine (GCE). Users must be able to connect remotely to the instance using a Virtual Network Connection (VNC) service to see the Gnome desktop and run the PDI client. Because VM instances running on the GCE do not publicly expose the ports required to establish a remote desktop connection, you must also create an SSH (Secure Shell) tunnel between the remote PDI client and the local machine.

Perform the following procedures to set up a PDI client instance in the Google Compute Engine and use it as a client instance for Dataproc.

1. In the GCP platform dashboard, navigate to the Compute Engine console.
2. Navigate from the menu to **Compute Engine** > **VM Instances**.
   1. Click **Create Instance**.
   2. Click **Advanced options** > **Networking tab**.
   3. In the **Network Tags** text box, enter `vnc-server`.
3. Install and update a working VNC service for the remote user interface.
4. Log in to the instance using SSH.
   1. Use a locally installed SSH client command line to access the remote client instance using its external IP address.

      **Note:** The console displays the external IP.
   2. Use the Compute Engine list of active virtual machines and select SSH from the list next to the virtual machine you want to use.
5. Update the operating system on the virtual machine.
6. Install Gnome and VNC.
7. Create an SSH tunnel from your VNC client machine.
8. Connect to the VNC.
9. (Optional) Configure and log in to Kerberos on your client instance.

   If you are using Kerberos, the VM instance running PDI in GCE must be configured with Kerberos to work with a Kerberos-enabled Dataproc cluster. Kerberos must be properly configured and the client machine must be authenticated with the Kerberos controller.

When successful, you can see a remote desktop with PDI running in the compute engine. You can use PDI to design and launch jobs and transformations on a cluster created in Google Dataproc.
