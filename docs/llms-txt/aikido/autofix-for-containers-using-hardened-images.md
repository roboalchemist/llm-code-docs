# Source: https://help.aikido.dev/aikido-autofix/autofix-for-containers-using-hardened-images.md

# AutoFix for Containers: Using Aikido Hardened Images

Updating to the latest version of a base image can be a difficult task as it might required changes to your application. When updating to a newer base image is not a viable option, you can stay secure by using Aikido Extended Lifetime Support (i.e. hardened images).

Aikido maintains a registry of base images containing patched versions of libraries with reported **CRITICAL** or **HIGH** severity security issues. When you accept an AutoFix suggestion to use a hardened (or **ELS** - Extended Lifecycle Support) image, the hardened image from the Aikido registry replaces the existing base image in your Dockerfile.

For example [CVE-2025-4373](https://security-tracker.debian.org/tracker/CVE-2025-4373) is fixed by Debian in Trixie and Sid but not in Bookworm. Our ELS `debian:bookworm` image contains a patched version of `glib2.0` that fixes this vulnerability. Using this image avoids breaking changes while maintaining a good security posture.

The Aikido-maintained ELS images are created by Root ([root.io](https://root.io/)). Root eliminates vulnerabilities in container images by automatically remediating issues and patching affected packages. That means the ELS images you use are continuously kept up to date, with AutoFix suggesting updates as appropriate.

## Using Hardened/ELS images with AutoFix

1. In Aikido, navigate to **Containers**. For a container with security issues, select the kebab menu for that entry and click **Preview AutoFix** (if AutoFix is available for that issue).
   1. **Note:** You can alternatively navigate to **AutoFix > Containers** and click **View Fix** under the **Status** column for that issue.
2. Aikido AutoFix for containers will automatically propose an ELS image when available. The image is hosted on `docker.aikido.io` .&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FWUpigVzAZcGbF2YQiCbS%2Fimage.png?alt=media&#x26;token=766d754a-02cf-481c-a7a0-9a495a8a86fb" alt=""><figcaption></figcaption></figure>

In this example we see a Dockerfile using a `debian:bookworm` base image. Updating the base image to the ELS version solves 75 issues present in that version of the base image that were not remediated by the Debian maintainers.

3. Select **Create PR** to open a pull request in your SCM to apply the fix. You can also click **Copy fixed file** to manually apply the change to your Dockerfile.&#x20;

## Extended Lifetime Support image availability

In Aikido, you can view which base images have supported ELS versions from the **AutoFix** > **Containers** page >&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXFtlxuCcAnL7t8fiYFTO%2FAutoFix_Container_overview_-_Roland_Demo_Org_-_Aikido_Security_%E2%80%94_Aikido.png?alt=media&#x26;token=9d7352b5-763b-4dce-a45d-0080a7e33af1" alt=""><figcaption></figcaption></figure>

All image are available for both `amd64` and `arm64` architectures.
