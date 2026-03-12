# Source: https://docs.getint.io/guides/integration-synchronization/jira-gitlab/attachments-sync-in-gitlab-integration.md

# Attachments Sync in GitLab Integration

As of now, there’s a limitation to syncing attachments from GitLab. It doesn’t support attachments natively, but it is possible to sync them with a workaround by providing a cookie header.

### How to sync attachments <a href="#how-to-sync-attachments" id="how-to-sync-attachments"></a>

1. Please open your type mappings in your Jira Gitlab integration and go to the **Comments & Attachments** tab. Enable **Synchronize attachments:**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTbP65Hl6wgOkZuPrhKhD%2F01e799325071a6493e9cf4555d7671f2%20(1).png?alt=media&#x26;token=478c466f-4802-4a4d-8ae2-59f066f0c02c" alt=""><figcaption></figcaption></figure>

1. Get the **Cookie header** from your GitLab account. Use the developer's tool (F12 on Windows) within your GitLab’s groups page and go to **Network** > **Groups** > Click on **Headers** and scroll down to **Cookie**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frlx18fnugpG1uezmyBX5%2F65e501727ccb3c3cf44c6c24119aee27%20(1).png?alt=media&#x26;token=e9237911-2d9f-4ed7-abbd-c02738169908" alt=""><figcaption></figcaption></figure>

1. Copy the information and paste it into the **GitLab Cookie Header** field in Getint. Click **Apply,** to submit the changes and save your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQHD2reVbQ81Ohf1kHytN%2F1cbc24fe9b3e6f2df72ee82a896e5a6a%20(1).png?alt=media&#x26;token=ed698052-6fae-495a-a119-b6c6d4e141ef" alt=""><figcaption></figcaption></figure>

1. Make sure to test the attachments after enabling the feature.

{% hint style="warning" %}
Currently, attachments are only supported one way from GitLab to the other app in the integration. Also, no API is available to download and upload attachments through a Gitlab integration. As a result, this alternative remains the only option for downloading attachments from synced comments as long as they come from GitLab.
{% endhint %}
