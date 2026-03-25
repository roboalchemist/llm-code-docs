# Source: https://help.aikido.dev/container-image-scanning/hardened-images-extended-lifetime-support.md

# Hardened images / Extended lifetime support

Updating to the latest version of a base image can be a difficult task as it might required changes to your application. When updating to a newer base image is not a viable option, you can stay secure by using Aikido Extended Lifetime Support (i.e. hardened images).

Aikido maintains a registry of base images containing patched versions of libraries with reported **CRITICAL** or **HIGH** severity security issues.&#x20;

For example [CVE-2025-4373](https://security-tracker.debian.org/tracker/CVE-2025-4373) is fixed by Debian in Trixie and Sid but not in Bookworm. Our ELS `debian:bookworm` image contains a patched version of `glib2.0` that fixes this vulnerability. Using this image avoids breaking changes while maintaining a good security posture.

## Extended Lifetime Support image availability <a href="#extended-lifetime-support-image-availability" id="extended-lifetime-support-image-availability"></a>

In Aikido, you can view which base images have supported ELS versions from the **AutoFix** > **Containers** page.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXFtlxuCcAnL7t8fiYFTO%2FAutoFix_Container_overview_-_Roland_Demo_Org_-_Aikido_Security_%E2%80%94_Aikido.png?alt=media&#x26;token=9d7352b5-763b-4dce-a45d-0080a7e33af1" alt=""><figcaption></figcaption></figure>

## Autofix

{% content-ref url="../aikido-autofix/autofix-for-containers-using-hardened-images" %}
[autofix-for-containers-using-hardened-images](https://help.aikido.dev/aikido-autofix/autofix-for-containers-using-hardened-images)
{% endcontent-ref %}
