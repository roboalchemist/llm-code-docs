# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-keycloak.md

# With Keycloak

To integrate Keycloak (the identity provider) with SonarQube Server (the service provider), both sides need to be configured.

{% hint style="warning" %}
Make sure the SonarQube Server URL is correctly set in SonarQube Server. See [server-base-url](https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url "mention") for more details.
{% endhint %}

### Keycloak server configuration <a href="#keycloak-server-configuration" id="keycloak-server-configuration"></a>

#### Create a new SAML client <a href="#create-a-new-saml-client" id="create-a-new-saml-client"></a>

1. Create your **Client ID.** Define it as something like `sonarqube`. It must not contain whitespace.
2. Define your **Client Protocol** as *saml*.
3. The **Client SAML Endpoint** can be left empty.

#### Configure the new SAML client <a href="#configure-the-new-saml-client" id="configure-the-new-saml-client"></a>

1. Under **Settings**:
   1. **Client Signature Required:** *ON* (only if request signature is active in the SonarQube Server SAML configuration).
   2. **Encrypt Assertions**: *ON* (if the responses from the IdP are to be encrypted).
   3. **Valid Redirect URLs**: `<Your SonarQube Server URL>/oauth2/callback/saml`. For example, [`https://sonarqube.mycompany.com/oauth2/callback/saml`](https://sonarqube.mycompany.com/oauth2/callback/saml).
2. Under **Keys**:
   1. **Signing Key** (optional): Add the service provider private key and the certificate if the signature of the requests is enabled on the SonarQube Server side (Keycloak generated keys can be used). This private key will have to be provided in PKCS8 format in SonarQube Server.
   2. **Encryption Key** (optional): Add the service provider certificate if you want to activate the encryption of Keycloak responses. If a request signature is used, you must use the same certificate for the encryption.
3. In **Client Scopes** > **Default Client Scopes**, remove `role_list` from **Assigned Default Client Scopes** (to prevent the error `com.onelogin.saml2.exception.ValidationError: Found an Attribute element with duplicated Name` during authentication)
4. Under **Mappers**, create a mapper for each user attribute:
   1. Create a mapper for the login:
      * **Name**: `Login`
      * **Mapper Type**: *User property*.
      * **Property**: `Username` (Note that this value should not contain any special characters other than `.-_@`, to meet SonarQube Server restrictions.)
      * **SAML Attribute Name**: `login`
   2. Create a mapper for the name:
      * **Name**: `Name`
      * **Mapper Type**: *User property*.
      * **Property**: `Username` (This can also be another attribute that you previously specified for the users.)
      * **SAML Attribute Name**: `name`
      * (Optional) Create a mapper for the email:
        1. **Name**: `Email`
        2. **Mapper Type**: *User property*.
        3. **Property**: `Email`
        4. **SAML Attribute Name**: `email`
   3. (Optional) Create a mapper for the groups (if you rely on a list of roles defined in **Roles** of the realm, not in **Roles** of the client):
      * **Name**: `Groups`
      * **Mapper Type**: *Role list*.
      * **Role Attribute Name**: `groups`
      * **Single Role Attribute**: *ON*
   4. If you rely on a list of groups defined in "Groups":
      * **Name**: `Groups`
      * **Mapper Type**: *Group list*.
      * **Role Attribute Name**: `groups`
      * **Single Role Attribute**: *ON*
      * **Full Group Path**: *OFF*
5. In **Realm Settings** > **General** > **Endpoints**, click on **SAML 2.0 Identify Provider Metadata** to obtain the XML configuration file from Keycloak.

### SonarQube Server configuration <a href="#sonarqube-configuration" id="sonarqube-configuration"></a>

Navigate to **Administration** > **Authentication** > **SAML** and click **Create configuration**, it will open a popup window with all the fields that you need to provide.

Configure the SAML authentication: **Administration** > **Configuration** > **General Settings** > **Authentication** > **SAML**:

* **Application ID**: The value of the **Client ID** you set in Keycloak (for example, `sonarqube`)
* **Provider ID**: The value of the `EntityDescriptor > entityID` attribute in the XML configuration file (for example, [`http://keycloak:8080/auth/realms/sonarqube`](http://keycloak:8080/auth/realms/sonarqube%22)).
* **SAML login URL**: The value of `SingleSignOnService > Location` attribute in the XML configuration file (for example, [`http://keycloak:8080/auth/realms/sonarqube/protocol/saml`](http://keycloak:8080/auth/realms/sonarqube/protocol/saml%22)).
* **Identity provider certificate**: The value you get from **Realm Settings > Keys > RS256**. Click on **Certificate**.
* **SAML user login attribute**: `login` (or whatever you configured above when doing the mapping)
* **SAML user name attribute**: `name` (or whatever you configured above when doing the mapping)
* (Optional) **SAML user email attribute**: `email` (or whatever you configured above when doing the mapping)
* **Sign requests**: Set to true to activate the signature of the SAML requests. It needs both the service provider private key and certificate to be set.
* **Service provider private key**: The service provider private key shared with the identity provider. This key is required for both request signature and response encryption, which can be activated individually. The key should be provided for SonarQube Server in PKCS8 format without password protection.
* **Service provider certificate**: The service provider certificate shared with the identity provider in order to activate the request signature and response encryption.

You can find some instructions to convert different key formats [here](https://manpages.ubuntu.com/manpages/focal/man1/pkcs8.1ssl.html).

### Enabling and testing SAML authentication <a href="#enabling-and-testing-saml-authentication" id="enabling-and-testing-saml-authentication"></a>

1. Save the SAML configuration by clicking **Save configuration.**
2. Before enabling the SAML authentication on SonarQube Server, you can verify that the configuration is correct by clicking **Test Configuration**. This will initiate a SAML login and return useful information about the SAML response obtained from the identity provider.
3. Click **Enable configuration**.
4. In the login form, the new button **Log in with Keycloak** (or a custom name specified in the **Provider Name** field) allows users to connect with their SAML account.

<div align="left"><figure><img src="broken-reference" alt="SonarQube login form with Keycloak login button"><figcaption></figcaption></figure></div>

### Group synchronization <a href="#group-synchronization" id="group-synchronization"></a>

To use the group synchronization feature:

1. Create and/or verify the user groups in SonarQube Server so that the automatic group synchronization can take place properly. See *Group synchronization* in [#justintime-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/overview#justintime-provisioning "mention").
2. Configure a `groups` attribute in Keycload (see the Keycloak server configuration section).
3. Enable group synchronization in SonarQube Server as follows:\
   Under **SAML** > **Provisioning,** enter `groups`, or whatever name you gave to this attribute, in the **SAML group attribute** field. If no value is entered in this field, users are assigned to the default sonar-users group only.

Group synchronization is only compatible with the **Just-in-Time user and group provisioning (default)** option.

<figure><img src="broken-reference" alt="The just-in-time provisioning option is selected"><figcaption></figcaption></figure>
