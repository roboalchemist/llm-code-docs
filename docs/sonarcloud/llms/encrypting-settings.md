# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/security/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/security/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/security/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/security/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/security/encrypting-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings.md

# Sensitive settings

You can encrypt any system property stored in `<sonarqubeHome>/conf/sonar.properties` or defined in SonarQube Server UI. The encryption algorithm used is AES with 256-bit keys.

In case of a Kubernetes deployment, see also [encrypting-helm-chart-sensitive-data](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data "mention").

You must have the Administer System permission in SonarQube Server.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

SonarQube Server must be up and running.

### Step 1: Create the encryption key <a href="#create-encryption-key" id="create-encryption-key"></a>

1. In SonarQube Server UI, go to **Administration > Configuration > Encryption**.
2. Select **Generate Secret Key**. An encryption key is generated.

You can use any other tool to generate the encryption key. It should be a Base64 Encoded AES-256 Key.

### Step 2: Store the encryption key in a secured file on disk <a href="#store-encryption-key" id="store-encryption-key"></a>

1. Copy the generated encryption key to a file on the machine hosting the SonarQube Server. The default location is `~/.sonar/sonar-secret.txt` .\
   If you want to store it somewhere else, set its path through the `sonar.secretKeyPath` system property. For more details about this setup, see [configuration-methods](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/configuration-methods "mention"). For more details about this system property, see [#general-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#general-properties "mention").
2. Restrict file permissions to the account running the SonarQube Server (ownership and read-access only).
3. Restart your SonarQube Server.

### Step 3: Encrypt the sensitive settings <a href="#encrypt-sensitive-settings" id="encrypt-sensitive-settings"></a>

To encrypt a property or setting:

1. In SonarQube Server UI, go to **Administration > Configuration > Encryption**.
2. Enter the value of the property in the form.

<figure><img src="broken-reference" alt="Enter the value of the sensitive property in the field and click Encrypt"><figcaption></figcaption></figure>

2. Select the **Encrypt** button. The encrypted value of the property is generated.
3. Select the copy tool to copy this value.
4. You can now:
   * In `<sonarqubeHome>/conf/sonar.properties`, replace the value of the property with the copied encrypted value.

```properties
sonar.jdbc.password={aes-gcm}CCGCFg4Xpm6r+PiJb1Swfg==  # Encrypted DB password
...
sonar.secretKeyPath=C:/path/to/my/secure/location/my_encryption_key.txt
```

* Or set the encrypted value in the corresponding SonarQuber Server UI’s field.
