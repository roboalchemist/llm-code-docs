# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context/tenable.md

# Tenable

Tenable is a leading provider of vulnerability management solutions, offering comprehensive tools to identify, assess, and manage security vulnerabilities in IT environments.

It enables organizations to continuously monitor their networks, systems, and applications for potential weaknesses, providing critical insights to help mitigate security risks.

Tenable's platform, including products like Tenable.io and Tenable.sc, delivers real-time visibility into vulnerabilities and facilitates efficient remediation strategies.

By integrating with OX Security, Tenable helps enhance security teams' ability to proactively manage vulnerabilities and prioritize responses to potential threats, ensuring stronger protection across organizational systems.

Through this integration, OX Security can import vulnerability data from Tenable and correlate it with security issues found using the OX Security platform. This allows security teams to gain a broader view of vulnerabilities and manage them more effectively.

Seamless integration between the two platforms, allows continuous vulnerabilities monitoring and prioritization. It helps security teams streamline their workflows by centralizing data from multiple sources, improving the accuracy and efficiency of remediation efforts.

The integration supports automated reporting, enabling organizations to stay on top of security vulnerabilities across their environment.

The integration process includes the following steps:

1. [Generate Tenable API key.](#generating-a-tenable-vulnerability-management-api-key)
2. [Connect the OX platform to Tenable.](#connecting-to-tenable)

## Prerequisites

Tenable account.

## Generating a Tenable Vulnerability Management API Key

1. Log in to Tenable at [cloud.tenable.com](http://cloud.tenable.com/).
2. In the upper-right corner, click the user profile icon. The **My Account** page appears.
3. In the left navigation, click **API Keys**. The **API Keys** section appears.
4. In the bottom-left corner, click **Generate**. In the top-right corner, a dialog appears with a message that existing keys will be unauthorized.
5. Click **Continue**. Under **ACCESS KEY** and **SECRET KEY**, new keys appear.
6. Copy the keys to a safe location. After you close the **My Account page**, you cannot view the keys again.

## Connecting to Tenable

1. In the **OX app**, go to **Connectors** and search for Tenable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a95a2533dd31f5f665edc0c500a029cef8d7fa4c%2FTenable%20icon.png?alt=media" alt="" width="81"><figcaption></figcaption></figure>

1. Select **Tenable** and set the following parameters in the **Configure your Tenable credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0f927512d1ff44d861fcd7992a216db1f0eaf427%2FTenable_connect.png?alt=media" alt="" width="536"><figcaption></figcaption></figure>

| Parameter            | Description                                       |
| -------------------- | ------------------------------------------------- |
| **Tenable Host URL** | Add your Tenable organization account URL.        |
| **API Access Key**   | Paste the Tenable access key you have generated.  |
| **API Secret Key**   | Paste the Tenable secret key you have generated.. |

1. Select **CONNECT**. The success message appears.

\\
