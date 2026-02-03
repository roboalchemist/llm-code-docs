# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/setup-in-ping-identity.md

# Setup in Ping Identity

This page explains how to register SonarQube Server in PingOne. The procedure with PingFederate is similar as the properties and values to be configured are the same.

This is the first step of SAML authentication setup with Ping Identity. For an overview of the complete setup, see [introduction](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/introduction "mention").

### Step 1: Create the SAML application for SonarQube Server <a href="#create-saml-app" id="create-saml-app"></a>

1. In PingOne, go to **Applications > Applications**.
2. Select the **+** icon.

<figure><img src="broken-reference" alt="Create a new application in PingOne"><figcaption></figcaption></figure>

3. Enter the application name and description.

<figure><img src="broken-reference" alt="Enter the new application&#x27;s name in PingOne"><figcaption></figcaption></figure>

4. In **Choose Application Type**, select **SAML Application**.
5. Select **Configure**.
6. Select the **Manually Enter** option and set:
   * **ACS URL** (Assertion Consumer Service): Must be in the format: `<sqServerBaseUrl>/oauth2/callback/saml`\
     \
     \
     \
     \
     Example: `https://my-sonarqube.com/oauth2/callback/saml`
   * **Entity ID:** Identifier of the application for SonarQube Server in PingOne\
     Example: `sonarqube`
7. Select **Save**.

### Step 2: Configure the application <a href="#configure-app" id="configure-app"></a>

1. Go to the **Attribute mappings** tab of the application for SonarQube Server you created in step 1. To retrieve the application, go to **Applications > Applications** and open the application details page.

<figure><img src="broken-reference" alt="Configure the attribute mappings in PingOne"><figcaption></figcaption></figure>

2. Select the pencil icon and the **+Add** button to add an attribute mapping: select a PingOne user attribute and map it to an attribute in the application. See the example below.

<details>

<summary>SAML attribute mapping example</summary>

| SAML attribute in the application | PingOne user attribute | Description                                                                                |
| --------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------ |
| saml\_subject                     | User ID                |                                                                                            |
| login                             | Family Name            | A unique name to identify the user in SonarQube Server.                                    |
| name                              | Given Name             | User name.                                                                                 |
| email                             | Email Address          | User email address.                                                                        |
| group\_names                      | Group Names            | Required only if you use the group synchronization feature with Just-in-Time provisioning. |

</details>

3. Select **Save**.
4. Go to the **Configuration** tab and select the **Download Metadata** button to download the SAML metadata containing your X.509 certificate.

### Step 3: Enable the application <a href="#enable-app" id="enable-app"></a>

1. In PingOne, retrieve the application: go to **Applications > Applications** and open the application details page.
2. In the top right corner of the application, select the toggle button.

<figure><img src="broken-reference" alt="Enable the application in PingOne"><figcaption></figcaption></figure>

### Step 4: Assign users and groups to the application <a href="#assing-users" id="assing-users"></a>

1. To create users, go to **Identities > Users** and select **+ Add User**.
2. To create a group:
   * Go to **Identities > Groups.**
   * Select **+** to create and save a group.
   * On the page of the new group, open the **Users** tab, and add users to the group.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/overview "mention")
* [setup-in-sq](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/setup-in-sq "mention")
* [optional-security-features](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/optional-security-features "mention")
* [#justintime-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/overview#justintime-provisioning "mention")
