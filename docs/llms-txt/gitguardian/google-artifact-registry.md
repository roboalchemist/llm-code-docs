# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry.md

# Integrate Google Artifact Registry

> Integrate Google Artifact Registry with GitGuardian to scan container images for exposed secrets using a GCP service account.

Secure your containerized applications by monitoring Google Artifact Registry for exposed secrets in container images and build artifacts.

## Why Monitor Google Artifact Registry?

Google Artifact Registry is the central hub for your containerized applications running on Google Cloud Platform. Container images stored here typically contain service account keys, Cloud SQL credentials, and API tokens that grant access to Google Cloud services, making any secret exposure a direct pathway to compromising your entire GCP infrastructure.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Supported) | Analyze existing images and their layers |
| **Incremental Scanning** | â (Supported) | Regular scheduled scanning for new content |
| **Monitored Perimeter** | â (Supported) | Granular monitoring of your repos |
| **Team Perimeter** | â³ (Coming Soon) | Users must be in the "All-incidents" team to access incidents |
| **Presence Check** | â (Not Supported) | All occurrences considered present |
| **Source Visibility** | â (Not Supported) | All sources are considered as private |
| **File Attachments** | N/A | Not applicable for container registries |

**What we scan:**
- All container image layers
- Dockerfiles and build configurations
- Environment variables in image metadata

:::info
This integration automatically scans your monitored repositories, downloading artifacts which may incur [bandwidth costs](https://cloud.google.com/vpc/network-pricing). To optimize costs and reduce false positives, carefully select the sources to monitor and use our [filepath exclusion feature](../../../secrets-detection/customize-detection/exclusion-rules#filepath-exclusions).
:::

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::

## Setup your Google Artifact Registry integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Google Cloud admin permissions** to create Service Accounts in your GCP project

GitGuardian integrates with Google Artifact Registry via a **Service Account** with **read-only access** to your repositories.

You can install GitGuardian on multiple Google Artifact Registry instances to monitor your repositories.

1. Make sure you're logged as an administrator in your Google Cloud Console
2. Click **Select a project** and select the project you want to integrate
    ![Google Artifact Registry Project](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-project.png)
3. Open the ![platform icon](/img/icons/three-dots-menu.svg) menu and go to the **Project settings**
    ![Google Artifact Registry Project Settings](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-project-settings.png)
4. Go to the **Service Accounts** section
5. Click **CREATE SERVICE ACCOUNT**
    ![Google Artifact Registry Create Service Account](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-create-service-account.png)
6. Type a **Service account name** and click **CREATE AND CONTINUE**
    ![Google Artifact Registry Service Account Name](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-service-account-name.png)
7. Select `Artifact Registry Reader` as a role and click **CONTINUE**
    ![Google Artifact Registry Service Account Role](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-service-account-role.png)
8. You can skip the 3rd step and click **DONE**
9. Click the ![platform icon](/img/icons/three-dots-menu.svg) menu next to the new service account and select **Manage keys**
    ![Google Artifact Registry Manage Keys](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-manage-keys.png)
10. Click the **ADD KEY** menu and select **Create new key**
    ![Google Artifact Registry Create New Key](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-create-news-key.png)
11. Select **JSON** as a key type and click **CREATE**
    ![Google Artifact Registry Download JSON File](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-download-json-file.png)
   This will create your new key and download it locally in a JSON file
12. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
13. Click **Install** next to **Google Artifact Registry** in the **Container registries** section
    ![Google Artifact Registry install](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-install.png)
14. Click **Install** on the [Google Artifact Registry integration](https://dashboard.gitguardian.com/settings/integrations/google_artifact) page
15. Type your **Region** (e.g.: `us-west2`)
16. Paste your **Service Account Key** in JSON format
17. Click **Add**
    ![Google Artifact Registry integration](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-integration.png)
18. Customize your monitored perimeter:
    - **Monitor specific Google Artifact Registry repositories** (Recommended)
        - No repositories are monitored by default, you will have to select them manually.
        - Newly created repositories will not be monitored by default. You can adjust this setting at any time.
        - Recommended to optimize your [bandwidth costs](https://cloud.google.com/vpc/network-pricing).
    - **Monitor the entire Google Artifact Registry instance**
        - All repositories are monitored by default with a full historical scan automatically triggered.
        - Newly created repositories will be monitored by default. You can adjust this setting at any time.

    ![Google Artifact Registry Default Monitored Perimeter](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-default-perimeter.png)

That's it! Your Google Artifact Registry instance is now installed, and GitGuardian is monitoring all Docker images of your selected repositories for secrets.

## Customize your monitored perimeter

To customize the monitored repositories, navigate to your [Google Artifact Registry settings](https://dashboard.gitguardian.com/settings/integrations/google_artifact).
1. Select/Unselect repositories to include or exclude them from monitoring
2. Confirm by clicking **Update monitored perimeter**
    ![Google Artifact Registry Custom Monitored Perimeter](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-custom-perimeter.png)

## Automatic repository monitoring

You can enable or disable the automatic addition of newly created repositories to your monitored perimeter by switching the option in your [Google Artifact Registry settings](https://dashboard.gitguardian.com/settings/integrations/google_artifact).
    ![Google Artifact Registry Automatic Repository Monitoring](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-automatic-monitoring.png)

## Uninstall your Google Artifact Registry instance

To uninstall a Google Artifact Registry instance:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Google Artifact Registry** in the **Container registries** section
3. Click the bin icon next to the Google Artifact Registry instance to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
    ![Google Artifact Registry uninstall](/img/internal-monitoring/integrate-sources/container-registries-integrations/google-artifact-registry/google-artifact-registry-uninstall.png)

That's it! Your Google Artifact Registry instance is now uninstalled.

## Excluded paths

GitGuardian automatically excludes files from scanning if their paths contain any of these regular expressions:

```
/__pypackages__/
/\.venv/
/\.tox/
/site-packages/
/venv/
distutils/command/register\.py
python.*/awscli/examples/
python.*/dulwich/(tests|contrib/test_)
python.*/hgext/bugzilla\.py
python.*/mercurial/util\.py
python.*/test/certdata/
python.*/urllib/request\.py
python.*/pygments/lexers/
/cryptography.+/tests/.+(fixtures|test)_.+\.py
/python.+pygpgme.+/tests/
botocore/data/.+/(examples|service)-.+\.json
usr(/local)?/lib/python.+/dist-packages
/libevent.+/info/test/test/
/conda-.+-py.+/info/test/tests.+/test_.+\.py
/python[^/]+/test/
/man/man5/kdc\.conf\.5
erlang.*(inets|ssl).*/examples/
/gems/.*httpclient.*/(test|sample)/
/gems/.*faraday.*/
/vendor/bundle/
/\.gem/
ruby-[^/]+/test/openssl/
/(g|G)o/src/cmd/go/internal/.*_test\.go
/(g|G)o/src/cmd/go/internal/.*/testdata/
/(g|G)o/src/cmd/go/testdata/
/(g|G)o/src/crypto/x509/platform_root_key\.pem
/(G|g)o/src/crypto/(tls|x509)/.*_test\.go
/(g|G)o/src/net/(url|http)/.*_test\.go
src/github.com/DataDog/datadog-agent/.*test.*\.go
google/internal/.*_test\.go
golang.org.*oauth2@.*/.*\.go
/flutter/.*/packages/flutter_tools/test/data/
/flutter/.*/examples/image_list/lib
/\.pub-cache
etc/ssl/private/ssl-cert-snakeoil\.key
perl.*Cwd\.pm
ansible/.*/tests/(integration|unit)/
ansible/.*/test/awx
ansible/collections/ansible_collections/.*/plugins/
/curl/.*/(tests|docs|lib/url\.c)
/doc/wget.+/NEWS
dist/awscli/examples/
usr(/local)?/lib/aws-cli/examples/
/google-cloud-sdk/(lib|platform)/
\.git/modules/third[-_]?party/
\.git/modules/external/
/\.npm/_cacache
/node_modules/
/\.parcel-cache/
/\.yarn/cache/
/\.m2/
/\.ivy2/cache/
/\.mix/
/\.hex/
/composer/cache/
/\.nuget/packages/
/libgpg-error/errorref\.txt
/Homebrew/Library/Taps/
/tcl[^/]+/http-.+\.tm
/tcl[^/]+/[^/]+/http-.+\.tm
usr/share/lua/[^/]+/posix/init\.lua
openssl/openssl-[^/]+/test/recipes/
usr/share/doc/libssl-doc/demos/
boringssl/src/third_party/[^/]+test[^/]+/[^/]+_test\.json
```

## Additional Self-Hosted considerations

For GitGuardian Self-Hosted instances, scan frequency can be configured in the [Admin Area](../../../self-hosting/management/application-management/admin-area):
- Time interval unit: **seconds**
- Default value: **86400** (1 day)
- Minimum value: **1800** (30 minutes)

## Privacy

Country-specific laws and regulations may require you to inform your users that your repositories are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans its repositories for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> *Please note that only repositories relating to the companyâs activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the repositoryâs purpose.*
