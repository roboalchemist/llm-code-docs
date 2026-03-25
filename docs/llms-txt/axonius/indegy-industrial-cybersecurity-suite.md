# Source: https://docs.axonius.com/docs/indegy-industrial-cybersecurity-suite.md

# Tenable.OT (Indegy)

Tenable.OT (Indegy) (previously Indegy Industrial Cybersecurity Suite) protects industrial networks from cyber threats, malicious insiders, and human error.

<Callout icon="📘" theme="info">
  Note

  Axonius uses the Indegy API to fetch data from Tenable.OT.  Authenticating APIs calls require a private key, public (cert) key and a "robot" user. You need to create those before configuring the Tenable.OT adapter connection. For details, see [Creating a Private Key Public Cert Key and a Robot User for authenticating API Calls to Indegy](/docs/indegy-industrial-cybersecurity-suite#creating-a-private-key-public-cert-key-and-a-robot-user-for-authenticating-api-calls-to-indegy).
</Callout>

<Callout icon="📘" theme="info">
  Note

  Axonius uses the Indegy API to fetch data from Tenable.OT.  Authenticating APIs calls require a private key, public (cert) key and a "robot" user. You need to create those before configuring the Tenable.OT adapter connection. For details, see \[/docs/indegy-industrial-cybersecurity-suite#creating-a-private-key-public-cert-key-and-a-robot-user-for-authenticating-api-calls-to-indegy]\(/docs/indegy-industrial-cybersecurity-suite#creating-a-private-key-public-cert-key-and-a-robot-user-for-authenticating-api-calls-to-indegy.
</Callout>

## Parameters:

1. **Indegy Domain** - Use your Indegy domain.
2. **Robot Name** - Specify the logical name for the robot you have created by using the robot name.
3. **Certificate file** - Upload the public key (cert) you have generated, which is a cert.pem file.
4. **Private key file** -  Upload the private key you have generated, which is a key.pem file.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server.
6. **HTTPS Proxy** *(optional)* - Enter details if the connection to the API requires a proxy.

<Image alt="TenableOTINdgy" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableOTINdgy.png" />

### Creating a Private Key, Public (Cert) Key and a "Robot" User for Authenticating API Calls to Indegy

The Indegy API Robots endpoint is used to facilitate the authentication and authorization process through the use of TLC Client Certificate. Instead of managing complicated tokens and sessions, Indegy enables the creation of a "Robot" user that serves as an intermediary, while supporting the use of TLC certificates as the authentication method for API calls.

**To create a private key, public (cert) key and a "robot" user**

1. Obtain a Token from Tenable Support.
2. Connect to your Indegy domain and run the following command to create a cert and private key.
   For example:
   ```
   openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
   ```
3. Save the generates files: the private key (key.pem) and the public key (cert.pem).
4. Issue a **Robots (POST)** API call with the body and token as specified below. This API call will associate the token with key.pem, so Axonius will not need to use the token for future API calls.

   In the request, specify the following mandatory parameters:

   * IP - The IP of your Indegy domain. Replace *\<IP>* in the script below.

   * Token - The token you have obtained from Indegy support. Replace *\<TOKEN>* in the script below.

   * Name (string) - A logical name for the robot (*"robot1"*  in the example script below).

   * Role (string) - The type of user role that is being created: "AdminRole" or "ReaderRole" (*"AdminRole"*  in the example script below).

   * Cert - The content of your cert.pem file. Use *"\n"*  to reflect new rows. Replace *\<CERT>*  in the script below.

   For example:

   ```
   curl -k -H 'Authorization: Bearer <TOKEN>' -XPOST https://<IP>/v1/robots --data '{"name": "robot1", "role": "AdminRole","cert": "<CERT>"}'
   ```

<Callout icon="📘" theme="info">
  Note

  For more details, see the Indegy Security Platform API Guide, provided by Tenable support.
</Callout>