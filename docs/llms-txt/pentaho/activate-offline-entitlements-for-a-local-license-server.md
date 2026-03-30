# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/activate-offline-entitlements-for-a-local-license-server.md

# Activate offline entitlements for a local license server

If your environment has a security restriction that prevents the license server from reaching the back office URL, you can use this procedure to activate your offline entitlements.

1. Obtain the activation ID from the sales support team.
2. Create a request file (`capabilityRequest.bin`) to activate granted entitlements by executing the following command on your local license server:

   ```
   cd /<destination_folder>/enterprise-local-license-server/enterprise

   # Linux:
   ./flexnetlsadmin.sh -server http://<license_server_ip_address>:7070/api/1.0/instances/~ -authorize admin Password!01 -activate -id <activation_id> -count <no_of_entitlements_you_want_to_activate> -o capabilityRequest.bin 

   # Windows:
   ./flexnetlsadmin.bat -server http://<license_server_ip_address>:7070/api/1.0/instances/~ -authorize admin Password!01 -activate -id <activation_id> -count <no_of_entitlements_you_want_to_activate> -o capabilityRequest.bin
   ```

   A `capabilityRequest.bin` file is generated in the directory where you ran the command.
3. Send the `capabilityRequest.bin` file to Pentaho customer support.

   Customer support generates a `capabilityResponse.bin` file and sends it to you.
4. Load the `capabilityResponse.bin` file to the local license server using the following command:

   Linux:

   ```
   ./flexnetlsadmin.sh -server http://<license_server_ip_address>:7070/api/1.0/instances/~ -authorize admin Password\!01 -activate -load capabilityResponse.bin
   ```

   Windows:

   ```
   ./flexnetlsadmin.bat -server http://<license_server_ip_address>:7070/api/1.0/instances/~ -authorize admin Password\!01 -activate -load capabilityResponse.bin
   ```
5. Check which licenses have been activated using the following command:

   ```
   ./flexnetlsadmin.sh -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -licenses -verbose
   ```

Your entitlements are now activated on the local license server.
