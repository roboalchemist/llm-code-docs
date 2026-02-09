# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md

# Encrypting sensitive data

You can encrypt any Sonar property stored in the `values.yaml` file and some Helm parameters, such as `jdbcPassword`, that will be managed as sonar properties. The encryption algorithm used is AES with 256-bit keys.

You must have the Administer System permission in SonarQube Server to perform this procedure.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

SonarQube Server must be up and running.

### Step 1: Create the encryption key <a href="#create-encryption-key" id="create-encryption-key"></a>

1. In SonarQube Server UI, go to **Administration > Configuration > Encryption**.
2. Select **Generate Secret Key**. An encryption key is generated.
3. Store the generated key in a safe location.

### Step 2: Create a Kubernetes secret to store the encryption key <a href="#create-kubernetes-secret" id="create-kubernetes-secret"></a>

Use the command below:

```sh
kubectl create secret generic --from-literal sonar-secret.txt=<encryptionKeyValue> <encryptionKeySecretName>
```

Example:

```sh
kubectl create secret generic --from-literal sonar-secret.txt=EgycYJc4Ek4uj2pH39e3+bnnk15IrVu4dxtfjDyN1y8= myEncryptionKeySecret
```

### Step 3: Enable the encryption in the Helm chart <a href="#enable-encryption-in-chart" id="enable-encryption-in-chart"></a>

Install the encryption key secret as follows:

1\. Add the following to the `values.yaml` file:

```yaml
sonarSecretKey: <encryptionKeySecretName>
```

2\. Use the helm upgrade command.

### Step 4: Encrypt the sensitive data <a href="#encrypt-data" id="encrypt-data"></a>

To encrypt a sensitive property in `values.yaml`:

1\. In SonarQube Server UI, go to **Administration > Configuration > Encryption**.

<figure><img src="broken-reference" alt="Enter the value of the sensitive property in the field and click Encrypt"><figcaption></figcaption></figure>

2\. Enter the value of the property.

3\. Select the **Encrypt** button. The encrypted value of the property is generated.

4\. Select the copy tool.

5\. In the `values.yaml` file, replace the value of the property with the copied encrypted value.

6\. Use the helm upgrade command.
