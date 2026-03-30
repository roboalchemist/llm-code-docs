# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server.md

# Install and manage a local license server

If you cannot access the cloud license server that is included with Pentaho to verify Pentaho product licenses, you can install a local license server behind your firewall to use for verifying licenses.

The local license server is a command line tool that is used to manage Pentaho licenses and perform various administrative tasks.

You can install a local license server on either Linux or Windows operating systems.

During the process of installing a local license server, you are provided with a URL for the product to connect to the license server (example: `http://<server_ip_address>:7070/api/1.0/instances/~`).

Users can also enter a URL to request a license from the local license server (example: `http://<server_ip_address>:7070/request`). The local license server communicates which licenses are available and the proper components are unlocked and made available to that user.

As part of your deployment, you might want to consider redundancy to prevent disruptions in application access due to local license server failures. For more information, see [Revenera License Server Failover](https://docs.revenera.com/fne/2022_02/adminguide/Content/helplibrary/License_Server_Failover.htm#lagfunctionality_2657120275_1032675) for details.
