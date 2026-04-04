# Source: https://help.cloudsmith.io/docs/helm-chart-repository.md

# Helm Chart Repository

Cloudsmith provides public & private repositories for Helm Charts

![](https://files.readme.io/974fd7d-banner_helm_hd.jpg "banner_helm_hd.jpg")

> 🚧 Support for OCI and non-OCI Helm Registries
>
> While Cloudsmith supports both OCI and non-OCI Helm registries, please note that for Helm OCI support the endpoint is: [helm.oci.cloudsmith.io](helm.oci.cloudsmith.io).
>
> For support on OCI Helm Charts, please refer to our OCI Repository documentation [here](https://help.cloudsmith.io/docs/oci-repository).

[Helm](https://helm.sh) is a package manager for Kubernetes that allows development and operations teams to easily manage and deploy these increasingly complex cloud native applications to their Kubernetes clusters. Helm allows you to manage applications on your Kubernetes cluster in much the same way as you’d manage applications on your Linux server with `apt` or `yum`.

Helm works by packaging up a set of YAML definitions along with the necessary configuration to quickly stand up all components of an application in a repeatable way. A single chart can be as simple or complex as necessary, deploying anything from a single container to a full distributed application. Helm combines these application definitions with user-provided configuration to allow simple overriding of configuration where needed, allowing users to concentrate on shipping software and not on the nitty-gritty of configuring every application they need to run.

Helm packages are known as “Charts” and are stored in a “Chart Repository”. By default, Helm comes bundled with the “stable” chart repository, hosted for free by Google. Most public charts are hosted here, mostly provided by vendors packaging their own software for use by others.

For more information on Helm, please see:

* [Helm](https://helm.sh/): The official website for Helm
* [Helm Hub](https://hub.helm.sh): The official public repository for Helm Charts
* [Helm Documentation](https://helm.sh/docs): Helm Documentation
* [Kubernetes Documentation](https://kubernetes.io/docs): Kubernetes Documentation

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo/rsa-key pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
      <a href="https://youtu.be/2yFGdeaYU9Y" target="_blank">
        <img src="https://files.readme.io/c9f2ced-cloudsmith-youtube-play-helm-small.png" /></a>
    </div>
  </div>
  `}
</HTMLBlock>

In the following examples:

| Identifier     | Description                                                                               |
| :------------- | :---------------------------------------------------------------------------------------- |
| OWNER          | Your Cloudsmith account name or organization name (namespace)                             |
| REPOSITORY     | Your Cloudsmith Repository name (also called "slug")                                      |
| TOKEN          | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME       | Your Cloudsmith username                                                                  |
| PASSWORD       | Your Cloudsmith password                                                                  |
| API-KEY        | Your Cloudsmith API Key                                                                   |
| NAME           | A name for your repository in your helm configuration                                     |
| CHART\_NAME    | The name of your chart                                                                    |
| CHART\_VERSION | The version number of your chart                                                          |

## Upload a Chart

To upload, you will need to generate your chart first. You can do this with the [helm CLI](https://helm.sh/docs/helm/#helm-package):

```shell
helm package .
```

This generates a chart package file (.tgz) like `CHART_NAME-CHART_VERSION.tgz` that you can upload.

> 📘
>
> Please see the [official Chart development](https://helm.sh/docs/developing_charts/) guide for more information on building your own Charts for distribution.

### Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/cli).

The command to upload a Helm chart via the Cloudsmith CLI is:

```shell
cloudsmith push helm OWNER/REPOSITORY CHART_NAME-CHART_VERSION.tgz
```

Example:

```shell
cloudsmith push helm org/repo your-chart-1.0.0.tgz
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

***

### Example Project

For examples of what your project should look like for packaging and publishing/uploading, please have a look at our [examples repository](http://github.com/cloudsmith-io/cloudsmith-examples) (on GitHub). We'll supplement these with more detailed guidance later but otherwise, just ask! - we're here to help.

***

## Download / Install a Chart

### Setup

Assuming you have helm already installed, it is straight-forward to add a Cloudsmith-based chart repository. You use the `helm repo add` and `helm repo update` commands as follows:

#### Public Repositories

```shell
helm repo add NAME \
  'https://dl.cloudsmith.io/public/OWNER/REPOSITORY/helm/charts/' 
helm repo update
```

#### Private Repositories

```shell Entitlement Token Auth
helm repo add NAME \
  'https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/helm/charts/' 
helm repo update
```

```shell HTTP Basic Auth (User & Pass)
helm repo add NAME \
  'https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/helm/charts/'  \
  --username USERNAME \
  --password PASSWORD
helm repo update
```

```shell HTTP Basic Auth (API-Key)
helm repo add NAME \
  'https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/helm/charts/'  \
  --username USERNAME \
  --password API-KEY
helm repo update
```

```shell HTTP Basic Auth (Token)
helm repo add NAME \
  'https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/helm/charts/'  \
  --username token \
  --password TOKEN
helm repo update
```

> 📘
>
> Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.
>
> The setup method will differ depending on what authentication type you choose to use.

> 🚧
>
> Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs

***

### Installing a Chart

To install/use a specific version of a chart:

```shell Shell - Classic Repository
helm install NAME/CHART_NAME --version CHART_VERSION
```

To install the latest version of a chart:

```shell Shell - Classic Repository
helm install NAME/CHART_NAME
```

Or you can upgrade to the most recent version of a chart if you've already installed:

```shell Shell - Classic Repository
helm upgrade NAME/CHART_NAME
```

If you've got a `requirements.yaml` file in your chart, you can specify this as a dependency:

```yaml
dependencies:
  - name: CHART_NAME
    version: CHART_VERSION
    repository: NAME
```

***

### Removing Setup

Helm provides a very clean method of removing a chart repository, simply run the following command:

```shell
helm repo remove NAME
```

### Logging out of Registry

Helm provides a command to logout of registries

```shell
helm registry logout docker.cloudsmith.io
```

## Provenance

Provenance files allow for verification of both the integrity and source of a Helm chart. Cloudsmith fully supports both verification and generation of Helm provenance files.

### Building Provenance Files

Provenance files can be built whilst packaging helm charts, by passing in the `--sign` and `--key` switches:

```Text Shell
helm package --sign --key "Your Key Name" .
```

The Helm client will prompt for the secret key used to sign your Chart. One complete, a `.prov` file will coexist alongside your chart tarball.

### Uploading Provenance Files

Provenance files may be uploaded on the UI as above.

### Upload via the Cloudsmith CLI

Provenance files can be passed to the Cloudsmith CLI during a `push`. Please note this requires version `2.0.4` (or later) of the `cloudsmith-api` Python package:

```Text Shell
cloudsmith push helm OWNER/REPOSITORY --provenance-file CHART_NAME-CHART_VERSION.tgz.prov CHART_NAME-CHART_VERSION.tgz
```

### Automated Generation of Provenance Files

Where a provenance file has not been provided at upload, Cloudsmith will automatically generate one during synchronization. Generated provenance files will be signed using the current repository GPG signing key.

### Verifying a Chart

Charts and provenance files may verified by passing the `--verify` switch to `helm install`:

```Text Shell
helm install --verify NAME/CHART_NAME
```

Note that this will require the GPG public key of the repository to be installed to the keyring of the target system.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>

You can configure upstream Helm repositories that you wish to use for charts that are not available in your Cloudsmith repository. In addition, you can also choose to cache any requested charts for future use.

Please see our [Upstream Proxying](https://help.cloudsmith.io/docs/proxying) documentation for further instructions.

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span> <span class="cs-tag cs-tag-purple">Packages</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.