# Source: https://zuul-ci.org/docs/zuul/latest/drivers/azure.html

Title: Azure — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/azure.html

Markdown Content:
Zuul can use Azure as a source for build nodes.

Before using the Azure driver, make sure you have created a service principal.

Two methods of authenticating the service principal are available: a shared secret or OIDC federation.

To use a shared secret: save the credential information in a JSON file. Follow the instructions at [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest) and use the `--sdk-auth` flag:

az ad sp create-for-rbac --name zuul --sdk-auth

There are two options for providing the information in this file to Zuul: place this file on the zuul-launcher and refer to it using [<azure connection>.shared_credentials_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "attr-<azure connection>.shared_credentials_file") or extract the information in the file and provide it directly with the configuration options below.

To use OIDC federation, the JWT must be available in a file on the zuul-launcher (for example, by way of Kubernetes secret projection). Set the [<azure connection>.subscription_id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.subscription_id "attr-<azure connection>.subscription_id"), [<azure connection>.tenant_id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.tenant_id "attr-<azure connection>.tenant_id"), [<azure connection>.client_id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.client_id "attr-<azure connection>.client_id"), and [<azure connection>.federated_token_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.federated_token_file "attr-<azure connection>.federated_token_file") fields.

You must also have created a network for Zuul to use. Be sure to enable IPv6 on the network if you plan to use it.

The Azure driver uses the “Standard” SKU for all public IP addresses. Standard IP addresses block all incoming traffic by default, therefore the use of a Network Security Group is required in order to allow incoming traffic. You will need to create one, add any required rules, and attach it to the subnet created above.

You may also need to register the Microsoft.Compute resource provider with your subscription.

The `azure` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#connection-configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

The supported options in `zuul.conf` connections are:

<azure connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E "Link to this definition")

<azure connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.driver "Link to this definition")

azure[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-%3Cazure%20connection%3E.driver.azure "Link to this definition")
The connection must set `driver=azure` for Azure connections.

<azure connection>.shared_credentials_file[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "Link to this definition")

A path to JSON file with shared access credentials. If this is supplied, no other credential settings need to be present.

<azure connection>.federated_token_file[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.federated_token_file "Link to this definition")

Path to the a file containing a JWT for use with OIDC federation.

<azure connection>.tenant_id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.tenant_id "Link to this definition")

The Microsoft Entra tenant ID for the account. Required unless [<azure connection>.shared_credentials_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "attr-<azure connection>.shared_credentials_file") is set.

<azure connection>.client_id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.client_id "Link to this definition")

The Microsoft Entra client ID for the account. Required unless [<azure connection>.shared_credentials_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "attr-<azure connection>.shared_credentials_file") is set.

<azure connection>.client_secret[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.client_secret "Link to this definition")

The shared secret for the principal. Required unless [<azure connection>.shared_credentials_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "attr-<azure connection>.shared_credentials_file") or [<azure connection>.federated_token_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.federated_token_file "attr-<azure connection>.federated_token_file") are set.

<azure connection>.subscription_id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.subscription_id "Link to this definition")

The Azure subscription to use. Required unless [<azure connection>.shared_credentials_file](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.shared_credentials_file "attr-<azure connection>.shared_credentials_file") is set.

<azure connection>.rate[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-%3Cazure%20connection%3E.rate "Link to this definition")

Default:`2`

The API rate limit (in requests per second) to use when performing API calls with Azure.

Provider Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#provider-configuration "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

The `azure` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

provider[azure][](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure] "Link to this definition")

Type:_dict_

The attributes available for configuring an Azure provider are below.

provider[azure].abstract[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].abstract "Link to this definition")

Default:`False`

Type:_bool_

Whether a section is intended to be inherited by another [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") or a [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider"). This setting is currently unused (but may be used in the future). If a section is used to provide common values to other sections, set this to true. Otherwise, the default of false indicates that the section should be referenced directly by providers.

provider[azure].connection[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].connection "Link to this definition")

Type:_str_

The name of the [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) to use. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects and may not be changed via inheritance.

provider[azure].flavor-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any flavor used with this provider. Many attributes which may be set on an individual flavor may be set once in this section and used for all the flavors in this provider. Values set on individual flavors may still override the values set here.

provider[azure].flavor-defaults.ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].flavor-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavor-defaults.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavor-defaults.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavor-defaults.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[azure].flavor-defaults.generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].flavor-defaults.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[azure].flavor-defaults.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[azure].flavor-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].flavor-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavor-defaults.volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].flavors[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors "Link to this definition")

Type:_dict_

A list of flavors associated with this provider.

provider[azure].flavors.description[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[azure].flavors.ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].flavors.final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavors.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavors.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavors.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[azure].flavors.generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].flavors.ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether to enable IPv4 networking. Defaults to true unless IPv6 is enabled. Enabling this will attach a private IPv4 address.

provider[azure].flavors.ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether to enable IPv6 networking. Enabling this will attach a private IPv6 address.

provider[azure].flavors.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.name "Link to this definition")

Type:_str_

The name of the flavor. Used to refer to the flavor in Zuul configuration.

provider[azure].flavors.priority[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.priority "Link to this definition")

Default:`regular`

Whether to create regular or spot instances.

regular[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavors.priority.regular "Link to this definition")
A regular instance.

spot[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].flavors.priority.spot "Link to this definition")
A spot instance.

provider[azure].flavors.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[azure].flavors.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[azure].flavors.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].flavors.vm-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.vm-size "Link to this definition")

Type:_str_

Size of the VM to use in Azure. See the [List of VM sizes](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=virtual-machines) for the list of sizes availabile in each region.

provider[azure].flavors.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].flavors.volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].image-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any image used with this provider. Many attributes which may be set on an individual image may be set once in this section and used for all the images in this provider. Values set on individual images may still override the values set here.

provider[azure].image-defaults.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[azure].image-defaults.connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.connection-type.ssh "Link to this definition")
An ssh connection.

provider[azure].image-defaults.ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].image-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[azure].image-defaults.generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].image-defaults.import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[azure].image-defaults.python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[azure].image-defaults.shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[azure].image-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[azure].image-defaults.upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].image-defaults.upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[azure].image-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].image-defaults.username[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[azure].image-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].image-defaults.volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].images[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images "Link to this definition")

Type:_list_

A list of images associated with this provider.

provider[azure].images[cloud][](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud] "Link to this definition")

Type:_dict_

These are the attributes available for a cloud image.

Specifies a community gallery image to use. Either this field, [provider[azure].images[cloud].shared-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image "attr-provider[azure].images[cloud].shared-gallery-image"), [provider[azure].images[cloud].image-reference](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference "attr-provider[azure].images[cloud].image-reference"), [provider[azure].images[cloud].image-id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-id "attr-provider[azure].images[cloud].image-id"), or [provider[azure].images[cloud].image-filter](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter "attr-provider[azure].images[cloud].image-filter") must be provided.

The image gallery name.

The image name.

The image version. Omit to use the latest version.

provider[azure].images[cloud].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[azure].images[cloud].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].connection-type.ssh "Link to this definition")
An ssh connection.

provider[azure].images[cloud].description[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[azure].images[cloud].ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].images[cloud].final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[azure].images[cloud].generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].images[cloud].image-filter[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter "Link to this definition")

Type:_dict_

Specifies a private image to use via filters. Either this field, [provider[azure].images[cloud].shared-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image "attr-provider[azure].images[cloud].shared-gallery-image"), [provider[azure].images[cloud].community-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].community-gallery-image "attr-provider[azure].images[cloud].community-gallery-image"), [provider[azure].images[cloud].image-reference](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference "attr-provider[azure].images[cloud].image-reference"), or [provider[azure].images[cloud].image-id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-id "attr-provider[azure].images[cloud].image-id") must be provided.

If a filter is provided, Zuul will list all of the images in the provider’s resource group and reduce the list using the supplied filter. All items specified in the filter must match in order for an image to match. If more than one image matches, the images are sorted by name and the last one matches.

The following filters are available:

provider[azure].images[cloud].image-filter.location[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter.location "Link to this definition")

Type:_str_

The image location.

provider[azure].images[cloud].image-filter.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter.name "Link to this definition")

Type:_str_

The image name.

provider[azure].images[cloud].image-filter.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter.tags "Link to this definition")

Type:_dict_

The image tags.

provider[azure].images[cloud].image-id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-id "Link to this definition")

Type:_str_

Specifies a private image to use by ID. Either this field, [provider[azure].images[cloud].shared-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image "attr-provider[azure].images[cloud].shared-gallery-image"), [provider[azure].images[cloud].community-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].community-gallery-image "attr-provider[azure].images[cloud].community-gallery-image"), [provider[azure].images[cloud].image-reference](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference "attr-provider[azure].images[cloud].image-reference"), or [provider[azure].images[cloud].image-filter](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter "attr-provider[azure].images[cloud].image-filter") must be provided.

provider[azure].images[cloud].image-reference[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference "Link to this definition")

Type:_dict_

Specifies a public image to use by reference. Either this field, [provider[azure].images[cloud].shared-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image "attr-provider[azure].images[cloud].shared-gallery-image"), [provider[azure].images[cloud].community-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].community-gallery-image "attr-provider[azure].images[cloud].community-gallery-image"), [provider[azure].images[cloud].image-id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-id "attr-provider[azure].images[cloud].image-id"), or [provider[azure].images[cloud].image-filter](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter "attr-provider[azure].images[cloud].image-filter") must be provided.

provider[azure].images[cloud].image-reference.offer[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference.offer "Link to this definition")

Type:_str_

The image offer.

provider[azure].images[cloud].image-reference.publisher[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference.publisher "Link to this definition")

Type:_str_

The image Publisher.

provider[azure].images[cloud].image-reference.sku[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference.sku "Link to this definition")

Type:_str_

The image SKU.

provider[azure].images[cloud].image-reference.version[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference.version "Link to this definition")

Type:_str_

The image version.

provider[azure].images[cloud].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[azure].images[cloud].name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[azure].images[cloud].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[azure].images[cloud].shared-gallery-image[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image "Link to this definition")

Type:_dict_

Specifies a shared gallery image to use. Either this field, [provider[azure].images[cloud].community-gallery-image](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].community-gallery-image "attr-provider[azure].images[cloud].community-gallery-image"), [provider[azure].images[cloud].image-reference](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-reference "attr-provider[azure].images[cloud].image-reference"), [provider[azure].images[cloud].image-id](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-id "attr-provider[azure].images[cloud].image-id"), or [provider[azure].images[cloud].image-filter](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].image-filter "attr-provider[azure].images[cloud].image-filter") must be provided.

provider[azure].images[cloud].shared-gallery-image.gallery-name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image.gallery-name "Link to this definition")

Type:_str_

The image gallery name.

provider[azure].images[cloud].shared-gallery-image.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image.name "Link to this definition")

Type:_str_

The image name.

provider[azure].images[cloud].shared-gallery-image.version[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shared-gallery-image.version "Link to this definition")

Type:_str_

The image version. Omit to use the latest version.

provider[azure].images[cloud].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[azure].images[cloud].type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].type "Link to this definition")

The type of image.

cloud[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[cloud].type.cloud "Link to this definition")
An existing image available in the cloud.

provider[azure].images[cloud].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].images[cloud].username[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[azure].images[cloud].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[cloud].volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].images[zuul][](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul] "Link to this definition")

Type:_dict_

These are the attributes available for a Zuul image.

provider[azure].images[zuul].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[azure].images[zuul].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].connection-type.ssh "Link to this definition")
An ssh connection.

provider[azure].images[zuul].description[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[azure].images[zuul].ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].images[zuul].final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[azure].images[zuul].generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].images[zuul].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[azure].images[zuul].name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[azure].images[zuul].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[azure].images[zuul].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[azure].images[zuul].tags[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[azure].images[zuul].type[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].type "Link to this definition")

The type of image.

zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].type.zuul "Link to this definition")
An image managed by Zuul.

provider[azure].images[zuul].upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].images[zuul].upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[azure].images[zuul].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].images[zuul].username[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[azure].images[zuul].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].images[zuul].volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].label-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any label used with this provider. Many attributes which may be set on an individual label may be set once in this section and used for all the labels in this provider. Values set on individual labels may still override the values set here.

provider[azure].label-defaults.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[azure].label-defaults.ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].label-defaults.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[azure].label-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].label-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].label-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].label-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[azure].label-defaults.generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].label-defaults.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[azure].label-defaults.key-data[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.key-data "Link to this definition")

Type:_str_

The SSH public key that should be installed on the node.

provider[azure].label-defaults.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[azure].label-defaults.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[azure].label-defaults.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[azure].label-defaults.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[azure].label-defaults.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[azure].label-defaults.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[azure].label-defaults.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[azure].label-defaults.subnet-id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.subnet-id "Link to this definition")

Type:_str_

Specifies the subnet to use by ID.

provider[azure].label-defaults.subnet-reference[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.subnet-reference "Link to this definition")

Type:_dict_

Specifies the subnet to use by reference

provider[azure].label-defaults.subnet-reference.network[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.subnet-reference.network "Link to this definition")

Type:_str_

The name of the subnet’s network.

provider[azure].label-defaults.subnet-reference.resource-group[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.subnet-reference.resource-group "Link to this definition")

Type:_str_

The resource group that contains the subnet.

provider[azure].label-defaults.subnet-reference.subnet[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.subnet-reference.subnet "Link to this definition")

Default:`default`

Type:_str_

The name of the subnet.

provider[azure].label-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[azure].label-defaults.user-assigned-identities[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.user-assigned-identities "Link to this definition")

Type:_dict_

provider[azure].label-defaults.user-assigned-identities.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.user-assigned-identities.name "Link to this definition")

Type:_str_

The name of the identity.

provider[azure].label-defaults.user-assigned-identities.resource-group[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.user-assigned-identities.resource-group "Link to this definition")

Type:_str_

The resource group that contains the identity.

provider[azure].label-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].label-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].label-defaults.volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].labels[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels "Link to this definition")

Type:_dict_

A list of labels associated with this provider.

provider[azure].labels.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[azure].labels.description[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.description "Link to this definition")

Type:_str_

A textual description of the label for reference purposes.

provider[azure].labels.ephemeral-disk[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.ephemeral-disk "Link to this definition")

Type:_bool_

If set to `true`, Azure will create an ephemeral OS disk instead of a managed disk.

provider[azure].labels.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[azure].labels.final[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].labels.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].labels.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#value-provider[azure].labels.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[azure].labels.flavor[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.flavor "Link to this definition")

Type:_str_

The flavor to use with this label.

provider[azure].labels.generate-password[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.generate-password "Link to this definition")

Type:_bool_

If booting a Windows image, an administrative password is required. If the password is not actually used (e.g., the image has key-based authentication enabled), a random password can be provided by enabling this option. The password is not stored anywhere and is not retrievable.

provider[azure].labels.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[azure].labels.image[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.image "Link to this definition")

Type:_str_

The image to use with this label.

provider[azure].labels.key-data[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.key-data "Link to this definition")

Type:_str_

The SSH public key that should be installed on the node.

provider[azure].labels.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[azure].labels.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[azure].labels.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[azure].labels.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.name "Link to this definition")

Type:_str_

The name of the label. Used to refer to the label in Zuul configuration.

provider[azure].labels.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[azure].labels.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[azure].labels.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[azure].labels.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[azure].labels.subnet-id[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.subnet-id "Link to this definition")

Type:_str_

Specifies the subnet to use by ID.

provider[azure].labels.subnet-reference[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.subnet-reference "Link to this definition")

Type:_dict_

Specifies the subnet to use by reference

provider[azure].labels.subnet-reference.network[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.subnet-reference.network "Link to this definition")

Type:_str_

The name of the subnet’s network.

provider[azure].labels.subnet-reference.resource-group[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.subnet-reference.resource-group "Link to this definition")

Type:_str_

The resource group that contains the subnet.

provider[azure].labels.subnet-reference.subnet[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.subnet-reference.subnet "Link to this definition")

Default:`default`

Type:_str_

The name of the subnet.

provider[azure].labels.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[azure].labels.user-assigned-identities[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.user-assigned-identities "Link to this definition")

Type:_dict_

provider[azure].labels.user-assigned-identities.name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.user-assigned-identities.name "Link to this definition")

Type:_str_

The name of the identity.

provider[azure].labels.user-assigned-identities.resource-group[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.user-assigned-identities.resource-group "Link to this definition")

Type:_str_

The resource group that contains the identity.

provider[azure].labels.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[azure].labels.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].labels.volume-size "Link to this definition")

Type:_int_

The size of the operating system disk, in GiB.

provider[azure].launch-attempts[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].launch-attempts "Link to this definition")

Default:`3`

Type:_int_

The number of times to attempt launching a node before considering the request failed.

provider[azure].launch-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].launch-timeout "Link to this definition")

Type:_int_

The time to wait from issuing the command to create a new node until the node is reporting as running. If the timeout is exceeded, the node launch is aborted and the node deleted.

provider[azure].name[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].name "Link to this definition")

Type:_str_

The name of the provider. Used to refer to the provider in Zuul configuration.

provider[azure].parent[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].parent "Link to this definition")

Type:_str_

The name of the parent section from which to inherit. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects. To indicate which section a provider should be attached to, use [provider[azure].section](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].section "attr-provider[azure].section")

provider[azure].region[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].region "Link to this definition")

Type:_str_

Name of the Azure region to use.

provider[azure].resource-group[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-group "Link to this definition")

Type:_str_

Name of the resource group in which to place nodes.

provider[azure].resource-limits[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-limits "Link to this definition")

Type:_dict_

Resource limits for this provider. Configure these values to cause Zuul to attempt to limit the resource usage. This can be used to limit Zuul’s usage to a level below the cloud quota.

provider[azure].resource-limits.cores[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-limits.cores "Link to this definition")

Type:_int_

The number of cores used by regular instances.

provider[azure].resource-limits.instances[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-limits.instances "Link to this definition")

Type:_int_

The number of instances.

provider[azure].resource-limits.lowPriorityCores[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-limits.lowprioritycores "Link to this definition")

Type:_int_

The number of low priority cores (including spot instances).

provider[azure].resource-limits.ram[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].resource-limits.ram "Link to this definition")

Type:_int_

The amount of ram, in MiB.

provider[azure].section[](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#attr-provider[azure].section "Link to this definition")

Type:_str_

The name of the [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") from which to inherit.
