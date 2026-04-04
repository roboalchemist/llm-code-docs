# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/webhooks.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/webhooks.md

# Webhooks

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

### Introduction to webhooks <a href="#introduction" id="introduction"></a>

Webhooks notify external services when:

* A project analysis is complete.\
  This is done regardless of the status of the background task or of the quality gate.
* An issue type, severity, or status is updated, and this update changes the quality gate status.\
  For example:
  * A user marks an issue as False Positive and the quality gate status turns green.
  * The severity of an issue is increased and the quality gate status turns red.

An HTTP(S) call including a JSON payload is sent to each configured URL. URLs may be specified at both the project and global levels. The project-level specification does not replace global-level webhooks. All hooks at both levels are called.

#### HTTP(S) call <a href="#https-call" id="https-call"></a>

The HTTP(S) call:

* Has an HTTP header `X-SonarQube-Project` with the project key to allow quick identification of the project involved.
* Includes a JSON document as payload, using the POST method. See below.
* Has a content type of `application/json`, with UTF-8 encoding.

#### Payload <a href="#payload" id="payload"></a>

The payload is a JSON document that includes:

* `analysedAt`: when the analysis was performed.
* `project`: the identification of the project analyzed.
* `qualityGate`: each quality gate criterion checked and its status.
* `qualityGate.status`: the quality gate status of the analysis.
* `status` and `taskID`: the status and the identifier of the background task.
* `properties`: user-specified properties.

{% hint style="info" %}
You can define project parameters to be added to the payload.
{% endhint %}

<details>

<summary>Payload example</summary>

```json
{
    "serverUrl": "<mySonarqubeURL>",
    "taskId": "AVh21JS2JepAEhwQ-b3u",
    "status": "SUCCESS",
    "analysedAt": "2016-11-18T10:46:28+0100",
    "revision": "c739069ec7105e01303e8b3065a81141aad9f129",
    "project": {
        "key": "myProject",
        "name": "My Project",
        "url": "https://mycompany.com/sonarqube/project/overview?id=myproject"
    },
    "properties": {
    },
    "qualityGate": {
        "conditions": [
            {
                "errorThreshold": "1",
                "metric": "new_security_rating",
                "onLeakPeriod": true,
                "operator": "GREATER_THAN",
                "status": "OK",
                "value": "1"
            },
            {
                "errorThreshold": "1",
                "metric": "new_reliability_rating",
                "onLeakPeriod": true,
                "operator": "GREATER_THAN",
                "status": "OK",
                "value": "1"
            },
            {
                "errorThreshold": "1",
                "metric": "new_maintainability_rating",
                "onLeakPeriod": true,
                "operator": "GREATER_THAN",
                "status": "OK",
                "value": "1"
            },
            {
                "errorThreshold": "80",
                "metric": "new_coverage",
                "onLeakPeriod": true,
                "operator": "LESS_THAN",
                "status": "NO_VALUE"
            }
        ],
        "name": "SonarQube way",
        "status": "OK"
    }
}
```

</details>

#### Webhook protection with HMAC <a href="#webhook-protection-with-hmac" id="webhook-protection-with-hmac"></a>

SonarQube can generate an HMAC to allow the third party service to verify the integrity and authenticity of the webhook they receive. To do so, it uses the HMAC-SHA256 algorithm and the secret stored in the webhook configuration.

### Configuring webhooks <a href="#configuration" id="configuration"></a>

This paragraph explains how to configure webhooks in the UI. You can also use the [Web API](https://sonarcloud.io/web_api/api/webhooks).

You can configure up to 10 webhooks at the project level and at the organization level. If configured, all 20 webhooks will be executed.

#### Configuring webhooks for your project <a href="#configuring-webhooks-for-your-project" id="configuring-webhooks-for-your-project"></a>

You must be a project admin.

Proceed as follows:

1. [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention").
2. Go to **Administration** > **Webhooks**.
3. Select **Create**. The **Create Webhook** dialog is displayed.
4. Enter the webhook name.
5. Enter the URL to which the webhook is to be delivered.
6. Enter a secret if you want to protect the webhook with HMAC. See **Securing your webhooks** below.
7. To update or delete a webhook, select the corresponding command in the three-dot menu at the far right of the webhook row.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e3b1a7f04c0789e4dc92355e739ee0714f6bb4cf%2F23747c77ca5d4b96d0adc9d9fa451157e3b1d386.png?alt=media" alt="The Webhooks page offers a Create button to build a new webhook to notify external services about the status of your project."><figcaption></figcaption></figure></div>

#### Configuring webhooks for your organization <a href="#configuring-webhooks-for-your-organization" id="configuring-webhooks-for-your-organization"></a>

You must be an organization admin.

Proceed as follows:

1. [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention").
2. Go to **Administration** > **Configuration** > **Webhooks**.
3. Select **Create**. The **Create Webhook** dialog is displayed.
4. Enter the webhook name.
5. Enter the URL to which the webhook is to be delivered. You can provide user/password in the URL as described in **Securing your webhooks** below.
6. Enter a secret if you want to protect the webhook with HMAC. See **Securing your webhooks** below.
7. To update or delete a webhook, select the corresponding command in the three-dot menu at the far right of the webhook row.

#### Testing the webhooks <a href="#testing-the-webhooks" id="testing-the-webhooks"></a>

It’s important that you test your configured webhooks. To do so, you can use various webhook testing/debugging tools.

### Monitoring the webhook delivery <a href="#monitoring-delivery" id="monitoring-delivery"></a>

You can monitor the delivery of your webhooks configured at the project or organization level in the SonarQube UI. You can also use the [Web API](https://sonarcloud.io/web_api/api/webhooks) to retrieve the webhook deliveries.

Each webhook’s delivery status is indicated. A delivery is marked as failed if the URL doesn’t respond within 10 seconds. Response records are purged after 30 days.

{% hint style="info" %}
SonarQube Cloud doesn’t retry to deliver failed webhook deliveries. You may use the Web API to implement an automatic redelivering mechanism.
{% endhint %}

{% hint style="info" %}
If you downgraded your organization to the Free plan, existing webhooks are still visible on the UI but won’t be invoked by SonarQube Cloud. If you upgrade your organization, you regain access to them.
{% endhint %}

#### Monitoring your project’s webhooks <a href="#monitoring-your-projects-webhooks" id="monitoring-your-projects-webhooks"></a>

You must be a project admin.

Proceed as follows:

1. Retrieve your project (see the[retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") page for instructions).
2. Go to **Administration** > **Webhooks**. The page shows the result and timestamp of each webhook’s most recent delivery.
3. To view the payload of the last delivery, select the three-dot menu at the far right of the webhook row.
4. To view the results and payloads of earlier deliveries, select the three-dot menu at the far right of the webhook row.

#### Monitoring your organization’s webhooks <a href="#monitoring-your-organizations-webhooks" id="monitoring-your-organizations-webhooks"></a>

You must be an organization admin.

Proceed as follows:

1. Retrieve your organization ( see the [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") page for instructions).
2. Go to **Administration** > **Configuration** > **Webhooks**. The page shows the result and timestamp of each webhook’s most recent delivery.
3. To view the payload of the last delivery, select the three-dot menu at the far right of the webhook row.
4. To view the results and payloads of earlier deliveries, select the three-dot menu at the far right of the webhook row.

### Securing webhooks <a href="#securing-webhooks" id="securing-webhooks"></a>

After you’ve configured your server to receive payloads, you want to be sure that the payloads you receive are initiated by SonarQube Cloud and not by attackers. You can do this by validating a hash signature that ensures that requests originate from SonarQube Cloud.

{% hint style="info" %}
A basic authentication mechanism is supported by providing user/password in the URL of the Webhook such as `https://myLogin:myPassword@my_server/foo`.
{% endhint %}

#### Setting your secret <a href="#setting-your-secret" id="setting-your-secret"></a>

To set your secret in SonarQube Cloud:

1. From the project or organization where you’re securing your webhooks, navigate to the webhooks settings at **Administration** > **Webhooks**
2. You can either select **Create** to create a new webhook or click an existing webhook’s settings drop-down and select **Update**.
3. Enter a random string in the **Secret** text box. This is used as the key to generate the HMAC hex digest value in the `X-Sonar-Webhook-HMAC-SHA256` header.
4. Select **Update**.

#### Validating the received payload <a href="#validating-the-received-payload" id="validating-the-received-payload"></a>

After setting your secret, it’s used by SonarQube Cloud to create a hash signature with each payload that’s passed using the `X-Sonar-Webhook-HMAC-SHA256` HTTP header. The header value needs to match the signature you are expecting to receive. SonarQube Cloud uses a HMAC lower-case SHA256 digest to compute the signature of the request body. Below is some sample Java code for your server. In this example, we are using the lib from [apache commons-codec HmacUtils class](https://commons.apache.org/proper/commons-codec/apidocs/org/apache/commons/codec/digest/HmacUtils.html).

```java
private static boolean isValidSignature(YourHttpRequest request) {
  String receivedSignature = request.getHeader("X-Sonar-Webhook-HMAC-SHA256");
  // See Apache commons-codec
  String expectedSignature = new HmacUtils(HmacAlgorithms.HMAC_SHA_256, "your_secret").hmacHex(request.getBody())
  return Objects.equals(expectedSignature, receivedSignature);
}
```

If the signatures don’t match, then the payload should be ignored.

### Adding parameters to the webhook payload <a href="#additional-parameters" id="additional-parameters"></a>

If you provide additional properties to your SonarScanner using the pattern `sonar.analysis.*`, these properties will be automatically added to the section `"properties"` of the payload.

For example these additional parameters:

```properties
sonar-scanner -Dsonar.analysis.buildNumber=12345
```

would add this to the payload:

```properties
"properties": {
  "sonar.analysis.buildNumber": "12345"
}
```
