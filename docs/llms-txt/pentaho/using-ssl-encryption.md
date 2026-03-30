# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster/using-ssl-encryption.md

# Using SSL encryption

Complete the following steps to set up SSL connections for the PDI client and the Pentaho Server:

1. Set up SSL security by enabling SSL in the Pentaho Server with a certificate authority.

   See **Administer Pentaho Data Integration and Analytics** document for details.
2. Import your certificate to the Java keystore on the machine where the PDI client is installed. If the Pentaho Server is installed on a different machine, import the certificate to the Java keystore on that machine.
3. At the following prompts, enter a new password and enter `Y`:

   ```
   Enter keystore password: 
   Trust this certificate?
   ```

The certificate is now trusted by the PDI client and the Pentaho Server.
