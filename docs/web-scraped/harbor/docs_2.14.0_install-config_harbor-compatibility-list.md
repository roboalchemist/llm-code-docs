# Harbor docs | Harbor Compatibility List

**Source:** https://goharbor.io/docs/2.14.0/install-config/harbor-compatibility-list/

Harbor Compatibility List

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

This document provides compatibility information for all Harbor components.

## Replication Adapters

|  | Registries | Pull Mode | Push Mode | Proxy Cache | Introduced in Release | Automated Pipeline Covered |
| --- | --- | --- | --- | --- | --- | --- |
| [Harbor](https://goharbor.io/) | Harbor  Harbor | Y  Y | Y  Y | Y  Y | V1.8 | Y  Y |
| [distribution](https://github.com/distribution/distribution) | distribution  distribution | Y  Y | Y  Y | Y  Y | V1.8 | Y  Y |
| [docker hub](https://hub.docker.com/) | docker hub  docker hub | Y  Y | Y  Y | Y  Y | V1.8 | Y  Y |
| [Huawei SWR](https://www.huaweicloud.com/en-us/product/swr.html) | Huawei SWR  Huawei SWR | Y  Y | Y  Y | N  N | V1.8 | N  N |
| [GCR](https://cloud.google.com/container-registry/) | GCR  GCR | Y  Y | Y  Y | Y  Y | V1.9 | Y  Y |
| [ECR](https://aws.amazon.com/ecr/) | ECR  ECR | Y  Y | Y  Y | Y  Y | V1.9 | Y  Y |
| [ACR](https://azure.microsoft.com/en-us/services/container-registry/) | ACR  ACR | Y  Y | Y  Y | Y  Y | V1.9 | N  N |
| [AliCR](https://www.alibabacloud.com/product/container-registry) | AliCR  AliCR | Y  Y | Y  Y | N  N | V1.9 | N  N |
| [Artifact Hub](https://artifacthub.io/) | Artifact Hub  Artifact Hub | Y  Y | N  N | N  N | V2.2 | N  N |
| [Artifactory](https://jfrog.com/artifactory/) | Artifactory  Artifactory | Y  Y | Y  Y | Y  Y | V1.10 | N  N |
| [Quay](https://github.com/quay/quay) | Quay  Quay | Y  Y | Y  Y | Y  Y | V1.10 | N  N |
| [GitLab Registry](https://docs.gitlab.com/ee/user/packages/container_registry/) | GitLab Registry  GitLab Registry | Y  Y | Y  Y | N  N | V1.10 | N  N |

* `Pull` mode replicates artifacts from the specified source registries into Harbor.
* `Push` mode replicates artifacts from Harbor to the specified target registries.
* `Proxy Cache` means the replication adapter can be used as a proxy cache registry.

## OIDC Adapters

|  | OIDC Providers | Officially Verified | End User Verified | Verified in Release |
| --- | --- | --- | --- | --- |
| [Google Identity](https://developers.google.com/identity/protocols/OpenIDConnect) | google identity  google identity | Y  Y |  | V1.9 |
| [Dex](https://github.com/dexidp/dex) | dex  dex | Y  Y |  | V1.9 |
| [Ping Identity](https://www.pingidentity.com) | ping identity  ping identity |  | Y  Y | V1.9 |
| [Keycloak](https://www.keycloak.org/) | Keycloak  Keycloak | Y  Y |  | V1.10 |
| [Auth0](https://auth0.com/) | Auth0  Auth0 | Y  Y |  | V1.10 |

## Scanner Adapters

|  | Scanners | Providers | Evaluated | As Default | Onboard in Release |
| --- | --- | --- | --- | --- | --- |
| [Clair](https://github.com/goharbor/harbor-scanner-clair) | Clair  Clair | CentOS | Y  Y | (removed as default in v2.2) | v1.10 |
| [Anchore](https://github.com/anchore/harbor-scanner-adapter) | Anchore  Anchore | Anchore | Y  Y |  | v1.10 |
| [Trivy](https://github.com/aquasecurity/harbor-scanner-trivy) | Trivy  Trivy | Aqua | Y  Y | Y  Y | v1.10 |
| [CSP](https://github.com/aquasecurity/harbor-scanner-aqua) | Aqua  Aqua | Aqua | Y  Y |  | v1.10 |
| [DoSec](https://github.com/dosec-cn/harbor-scanner/blob/master/README_en.md) | DoSec  DoSec | DoSec | Y  Y |  | v1.10 |
| [Sysdig Secure](https://github.com/sysdiglabs/harbor-scanner-sysdig-secure) | Sysdig  Sysdig | Sysdig | Y  Y |  | v2.1.0 |
| [TensorSecurity](https://github.com/tensorsecurity/harbor-scanner) | TensorSecurity  TensorSecurity | TensorSecurity | Y  Y |  | v2.2.0 |
| [ArksecScanner](https://github.com/arksec-cn) | Arksec  Arksec | Arksec | Y  Y |  | v2.4.0 |
| [Cyberwatch](https://github.com/Cyberwatch) | Cyberwatch  Cyberwatch | [Cyberwatch](https://cyberwatch.fr/integrate-with-harbor-scans) | Y  Y |  | v2.8.0 |

* `Evaluated` means that the scanner implementation has been officially tested and verified.
* `As Default` means that the scanner is provided as a default option and can be deployed together with the main Harbor components by providing extra options during installation. You must install other scanners manually.

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/harbor-compatibility-list.md)
[Create issue](https://github.com/goharbor/harbor/issues)