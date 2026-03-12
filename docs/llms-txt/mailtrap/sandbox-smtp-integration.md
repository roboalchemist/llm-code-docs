# Source: https://docs.mailtrap.io/email-sandbox/setup/sandbox-smtp-integration.md

# Sandbox SMTP Integration

## Copy SMTP credentials

{% stepper %}
{% step %}
Go to **Email Testing** → **Sandboxes**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8f946da2c1074f0a2f0700dd00e0b4acc6a111cc%2Fsandbox-integration-navigate-to-sandboxes.png?alt=media" alt="Navigation menu showing Email Testing section with Sandboxes option" width="563"></div>
{% endstep %}

{% step %}
Open the sandbox (named **My Sandbox**) created by default.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-10b7e1b77daf3d2eead7469a7661bc0cbb978ce0%2Fsandbox-integration-open-my-sandbox.png?alt=media" alt="Sandboxes list displaying My Sandbox and other project sandboxes" width="563"></div>
{% endstep %}

{% step %}
Under the **Integration** tab, select **SMTP** and copy the credentials such as Host, Port, Username, and Password.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-72ef2089bec7b1a9ea41e9defb4c81d83a8464b2%2Fsandbox-integration-smtp-credentials.png?alt=media" alt="Integration tab showing SMTP credentials including Host, Port, Username, and Password" width="563"></div>
{% endstep %}

{% step %}
Paste them into your email-sending script, service, or MTA (any service that supports SMTP integration), and run it. The email will arrive in your sandbox in a few seconds.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d74cb92a9a7f2d35427ec74c02524115c91c018e%2Fsandbox-integration-email-received.png?alt=media" alt="Sandbox inbox displaying received test email message" width="563"></div>
{% endstep %}
{% endstepper %}

## Select your integration

Instead of copy-pasting the SMTP credentials, you can use the code samples already containing your credentials.

{% stepper %}
{% step %}
In the **Integration** tab of your sandbox, scroll down to **Code Samples** and select the programming language or framework you're working with.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58bb8ca2dd649b4b27dfcae7a8812a196b50d959%2Fsandbox-integration-code-samples.png?alt=media" alt="Code Samples section showing various programming language options for integration" width="563"></div>
{% endstep %}

{% step %}
Copy the configuration and paste it into your email-sending script. Then, run it. The email will arrive in the sandbox in a few seconds.
{% endstep %}
{% endstepper %}

{% hint style="success" %}
*Learn how exactly Mailtrap can help you streamline email testing processes from our* [*case study with The Software House*](https://mailtrap.io/case-studies/the-software-house/)*.*
{% endhint %}
