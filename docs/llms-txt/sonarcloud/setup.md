# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/setup.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/setup.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/setup.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/notifications/slack/setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/setup.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/setup.md

# Setting up the connection to Slack

{% stepper %}
{% step %}

#### **Log in to SonarQube Cloud** [**through this page**](https://sonarcloud.io/login?return_to=%2Foauth-callback%2Fslack%3Fredirect_uri%3Dhttps%253A%252F%252Fslack.com%252Foauth%252Fv2%252Fauthorize%253Fclient_id%253D3702920631.9467182584262%2526redirect_uri%253Dhttps%253A%252F%252Fslack.com%252Foauth%252Fv2%252Fauthorize%253Fclient_id%253D3702920631.9467182584262%2526scope%253Dchannels%253Aread%252Cchat%253Awrite%252Ccommands%252Cgroups%253Aread%252Cmpim%253Aread%252Cchat%253Awrite.public%2526user_scope%253D%2526redirect_uri%253Dhttps%253A%252F%252Fsonarcloud.io%252Foauth-callback%252Fslack%26_gl%3D1*10nfome*_gcl_au*MTg4ODI3Nzk5Mi4xNzYyNTEzNTE3*_ga*MTMxMzk4MzAwMi4xNzU0NDc5Nzgz*_ga_9JZ0GZ5TC6*czE3NjMzODA3OTkkbzg3JGcxJHQxNzYzMzgxNjgxJGo1NCRsMCRoMA\&error=authentication\&skipRegionSelection=true)

This will allow SonarQube Cloud to connect your SonarQube Cloud account to your Slack account.\
Once you've successfully logged in to SonarQube Cloud, you'll be redirected to the Slack app installation page as illustrated below.&#x20;

<figure><img src="broken-reference" alt="To install the SonarQube Cloud app for Slack, select your Slack workspace and select the Install SonarQube button."><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Finish the installation

1. In **Workspace**, select your Slack workspace. You must be an admin of the workspace.
2. Review the app permissions in the right section.
3. Select **Install SonarQube**.
   {% endstep %}

{% step %}

#### Users can now subscribe to notifications&#x20;

Users can subscribe to SonarQube Cloud notifications directly within their Slack account: see [subscribing-to-slack-notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/subscribing-to-slack-notifications "mention").
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Check out this video on how to benefit from the Slack integration.

{% embed url="<https://www.youtube.com/watch?v=oW-pp4LN9r0>" %}
{% endhint %}

### Related pages

* [integration-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/connecting-to-slack/integration-overview "mention")
* [subscribing-to-slack-notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/subscribing-to-slack-notifications "mention")
