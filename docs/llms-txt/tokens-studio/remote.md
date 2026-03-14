# Source: https://docs.tokens.studio/token-storage/remote.md

# Remote Token Storage Integrations

## Remote Token Storage

By default, Tokens Studio will store your [Design Tokens locally](https://docs.tokens.studio/token-storage/local) in the Figma file you are working in, but their true power is unleashed when they can be stored outside of a design tool and synced with code.

This synchronization creates a shared source of truth, fostering collaboration and alignment between design and development teams.

You can manage version control in Tokens Studio without ever having the Figma to keep your changes in sync with engineers in code, and other designers working in multiple Figma files.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFyXpvOHIPhzSlIrCFS0M%2Fsync-header-infographic-v2.png?alt=media&#x26;token=8766a6c6-1941-4593-a76a-349d97986dd4" alt=""><figcaption></figcaption></figure>

### Sync providers

Tokens Studio offers out-of-the-box integrations with several third-party providers to sync your Design Tokens with code and store them externally for safekeeping outside of your local design files.

We support:

* [Git providers](#git-providers)
  * Connected to a code repository for remote Token storage that is version-controlled.
* [Cloud-based code storage providers](#cloud-storage-providers)
  * Syncing your Token files with design data platforms.
* [Locally hosted server Token storage.](#server-storage-providers)

Once your sync provider is active, the Plugin will detect changes in real time, and indicate when you need to sync changes with the Tokens in remote storage.&#x20;

Pro licence holders working with a Git sync provider can also create and switch between branches from within the plugin.&#x20;

{% content-ref url="remote-branch-switch" %}
[remote-branch-switch](https://docs.tokens.studio/token-storage/remote-branch-switch)
{% endcontent-ref %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fn1cTuEdZjVKY4IUF12qG%2Fsync-overview-plugin-v2-0.png?alt=media&#x26;token=0ad330ac-3b5d-47bc-8449-d03c1aa24942" alt=""><figcaption></figcaption></figure>

***

### Git providers

Git is an open-source system that tracks changes in code files.

Syncing your Tokens with a Git provider allows you to store your Design Tokens as code files in a repository. Tokens Studio has native features to push and pull Token changes easily and version-control your design decisions using the branching feature.

This allows you to explore design decisions before deploying them to a production environment.

*Select any of the Git providers below to read its Sync Setup Guide*

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>GitHub is the most popular Git provider for hosting your code and design decisions in the same location, and it's free to get started!</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPQX5WYH7zZUsIvcoDu3S%2Fgithub-card-header-sync-provider.png?alt=media&#x26;token=1bd8963c-cabf-4bc9-9409-040d28adab40">github-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-github">sync-git-github</a></td></tr><tr><td>Gitlab is a popular Git provider for projects that benefit from its enhanced security features.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FpRqNTyIaZapd1SqRohSz%2Fgitlab-card-header-sync-provider.png?alt=media&#x26;token=4cc49ccd-8a17-48cb-9167-093cd60287d0">gitlab-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-gitlab">sync-git-gitlab</a></td></tr><tr><td>Azure DevOps is a Microsoft-owned suite of development tools and services you can use to create a Git-based source code repository.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2OYQvS12rKDRw2RxZeos%2Fado-card-header-sync-provider.png?alt=media&#x26;token=568ad820-6e59-4db3-b16e-479e4ad7a6d0">ado-card-header-sync-provider.png</a></td><td></td></tr><tr><td>Bitbucket is a Git-based source code repository hosting service popular among teams using Atlassian tools.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FewmX1Q0F9XnNSRbYyksO%2Fbitbucket-card-header-sync-provider.png?alt=media&#x26;token=23434d72-e1b1-49d2-824a-7ea31deb1aaf">bitbucket-card-header-sync-provider.png</a></td><td></td></tr></tbody></table>

***

### Cloud storage providers

Cloud storage providers offer a platform to store, manage, and retrieve your Design Token data via an API.

*Select any of the cloud storage providers below to read its Sync Setup Guide*

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>JSONBin provides a simple REST interface to store &#x26; retrieve your JSON data from the cloud.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FASrFKEtxsqtYlq5xX2NL%2FJSONBIN-card-header-sync-provider.png?alt=media&#x26;token=731d0f95-1c37-4f6b-9ce3-9b13834bba92">JSONBIN-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-jsonbin">sync-cloud-jsonbin</a></td></tr><tr><td>Supernova is a design data platform popular for documenting design systems.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FsbhdiY2yFHg9Dgv20a1c%2FSUPERNOVA-card-header-sync-provider.png?alt=media&#x26;token=e162c759-26d8-4165-8f14-0e5c10e41e63">SUPERNOVA-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-supernova">sync-cloud-supernova</a></td></tr><tr><td>Tokens Studio has a standalone web-based platform for dynamic creation and management of design decisions.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDlVTT6lCDHtCxHltCRwZ%2FSTUDIO-card-header-sync-provider.png?alt=media&#x26;token=ca22b02a-4e2a-4293-a1b1-7453ed22990b">STUDIO-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-studio-platform">sync-cloud-studio-platform</a></td></tr></tbody></table>

***

### Locally hosted Token storage providers

Locally hosted Token storage providers offer an alternative to Git providers for projects that benefit from storing their Tokens on the same servers as the rest of their code.

*Select any of the local hosted below below to read its Sync Setup Guide*

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td>Generic Versioned Storage is a way to host your Design Tokens on a local or remote server, which supports read-only, read/write, and read/write/create workflows.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FvOdY6AksQcUtuMUY42AT%2FGENERICVERSION-card-header-sync-provider.png?alt=media&#x26;token=ec54fe57-e05b-4690-8567-dbd45b97e675">GENERICVERSION-card-header-sync-provider.png</a></td></tr><tr><td>When you host your Design Token JSON files on a web server or static hosting service, the plugin can access the Tokens (read-only) by syncing to the URL where your Token files are stored.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F4i5dEQKmUjLeSAYIUi2M%2FURL-card-header-sync-provider.png?alt=media&#x26;token=3a7d114e-6f2e-4d87-8e19-1ffb3935a661">URL-card-header-sync-provider.png</a></td></tr></tbody></table>

***

### Sync Provider Guides

When you are ready to sync your Tokens to a remote storage provider, check out these guides:

{% content-ref url="manage-sync-provider" %}
[manage-sync-provider](https://docs.tokens.studio/token-storage/manage-sync-provider)
{% endcontent-ref %}

{% content-ref url="remote-multi-file-sync" %}
[remote-multi-file-sync](https://docs.tokens.studio/token-storage/remote-multi-file-sync)
{% endcontent-ref %}

{% content-ref url="remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

{% content-ref url="remote-branch-switch" %}
[remote-branch-switch](https://docs.tokens.studio/token-storage/remote-branch-switch)
{% endcontent-ref %}

{% content-ref url="manage-sync-provider/edit" %}
[edit](https://docs.tokens.studio/token-storage/manage-sync-provider/edit)
{% endcontent-ref %}

{% content-ref url="manage-sync-provider/change" %}
[change](https://docs.tokens.studio/token-storage/manage-sync-provider/change)
{% endcontent-ref %}

{% content-ref url="local" %}
[local](https://docs.tokens.studio/token-storage/local)
{% endcontent-ref %}

{% content-ref url="manage-sync-provider/remove" %}
[remove](https://docs.tokens.studio/token-storage/manage-sync-provider/remove)
{% endcontent-ref %}

***
