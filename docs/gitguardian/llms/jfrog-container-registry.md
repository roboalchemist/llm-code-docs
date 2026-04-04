# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry.md

# Integrate JFrog Container Registry

> Integrate JFrog Container Registry with GitGuardian to scan container images and build artifacts for exposed secrets.

Secure your containerized applications by monitoring JFrog Container Registry for exposed secrets in container images and build artifacts.

:::tip
Looking to scan non-container artifacts such as npm, Maven, or PyPI packages? Check out the [JFrog Package Registries](../package-registries-integrations/jfrog-package-registry) integration.
:::

## Why Monitor JFrog Container Registry?

JFrog Container Registry serves as the enterprise-grade repository for your organization's production-ready container images. 
These images often contain production database credentials, enterprise API keys, and internal service tokens that, when exposed, can compromise critical business applications and provide unauthorized access to proprietary systems and sensitive customer data.

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
This integration automatically scans your monitored repositories, downloading container images which may incur [bandwidth costs](https://jfrog.com/pricing/). To optimize costs and reduce false positives, carefully select the sources to monitor and use our [filepath exclusion feature](../../../secrets-detection/customize-detection/exclusion-rules#filepath-exclusions).
:::

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::

## Setup your JFrog Container Registry integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **JFrog admin permissions** to create Access Tokens in your JFrog instance
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian integrates with JFrog Container Registry via an **Access Token** with **read-only access** to your repositories.

You can install GitGuardian on multiple JFrog Container Registry instances to monitor your repositories.

1. Make sure you're logged as an administrator in your JFrog Platform
2. Go to **Administration** > **User Management** > **Access Tokens**
3. Click **Generate Token**
    ![JFrog Platform Access Tokens page](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-access-tokens.png)
4. Type a Description (e.g.: `GitGuardian`)
5. Select `Group` as **Token scope**
6. Select `readers` as **Groups**
7. Uncheck **All** and select `Artifactory` as **Service**
8. Click **Generate**
    ![JFrog Platform Generate Token modal](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-generate-token.png)
9. Get the **Username** and copy the **Token**
    ![JFrog Platform Token value modal](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-copy-token.png)
10. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
11. Click **Install** next to **JFrog Container Registry** in the **Container registries** section
    ![JFrog Container Registry install button](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-install.png)
12. Click **Install** on the [JFrog Container Registry integration](https://dashboard.gitguardian.com/settings/integrations/jfrog_artifact) page
13. Type your **JFrog Container Registry instance URL** (e.g.: `https://acme.jfrog.io/`)
14. Paste your **Personal access token**
15. Type the associated **Username** (e.g.: `admin@acme.com`)
16. Click **Add**
    ![JFrog Container Registry integration](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-integration.png)
17. Customize your monitored perimeter:
    - **Monitor specific JFrog Container Registry repositories** (Recommended)
        - No repositories are monitored by default, you will have to select them manually.
        - Newly created repositories will not be monitored by default. You can adjust this setting at any time.
        - Recommended to optimize your [bandwidth costs](https://jfrog.com/pricing/).
    - **Monitor the entire JFrog Container Registry instance**
        - All repositories are monitored by default with a full historical scan automatically triggered.
        - Newly created repositories will be monitored by default. You can adjust this setting at any time.

    ![JFrog Container Registry Default Monitored Perimeter](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-default-perimeter.png)

That's it! Your JFrog Container Registry instance is now installed, and GitGuardian is monitoring all Docker images of your selected repositories for secrets.

## Customize your monitored perimeter

To customize the monitored repositories, navigate to your [JFrog Container Registry settings](https://dashboard.gitguardian.com/settings/integrations/jfrog_artifact).
1. Select/Unselect repositories to include or exclude them from monitoring
2. Confirm by clicking **Update monitored perimeter**
    ![JFrog Container Registry Custom Monitored Perimeter](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-custom-perimeter.png)

## Automatic repository monitoring

You can enable or disable the automatic addition of newly created repositories to your monitored perimeter by switching the option in your [JFrog Container Registry settings](https://dashboard.gitguardian.com/settings/integrations/jfrog_artifact).
    ![JFrog Artifactory Automatic Repository Monitoring](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-automatic-monitoring.png)

## Uninstall your JFrog Container Registry instance

To uninstall a JFrog Container Registry instance:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **JFrog Container Registry** in the **Container registries** section
3. Click the bin icon next to the JFrog Container Registry instance to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
    ![JFrog Container Registry uninstall](/img/internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry/jfrog-container-registry-uninstall.png)

That's it! Your JFrog Container Registry instance is now uninstalled.

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
