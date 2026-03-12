# Source: https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html

Title: OpenStack — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html

Markdown Content:
Zuul can use OpenStack clouds as a source for build nodes.

Information about OpenStack clouds, including authentication information, may be provided via a configuration file (e.g., `clouds.yaml`) or environment variables. See the [OpenStack SDK](https://docs.openstack.org/openstacksdk/latest/user/config/index.html) for more information.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#connection-configuration "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The supported options in `zuul.conf` connections are:

<openstack connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-%3Copenstack%20connection%3E "Link to this definition")

<openstack connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-%3Copenstack%20connection%3E.driver "Link to this definition")

openstack[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-%3Copenstack%20connection%3E.driver.openstack "Link to this definition")
The connection must set `driver=openstack` for OpenStack connections.

<openstack connection>.client_config_file[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-%3Copenstack%20connection%3E.client_config_file "Link to this definition")

A path to a configuration file (e.g., `clouds.yaml`) with connection information for one or more OpenStack clouds.

<openstack connection>.cloud(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-%3Copenstack%20connection%3E.cloud "Link to this definition")

The name of the OpenStack cloud (as it appears in the client config file).

<openstack connection>.rate[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-%3Copenstack%20connection%3E.rate "Link to this definition")

Default:`2`

The API rate limit (in requests per second) to use when performing API calls with this OpenStack cloud.

Provider Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#provider-configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

The `openstack` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

provider[openstack][](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack] "Link to this definition")

Type:_dict_

The attributes available for configuring an OpenStack provider are below.

provider[openstack].abstract[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].abstract "Link to this definition")

Default:`False`

Type:_bool_

Whether a section is intended to be inherited by another [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") or a [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider"). This setting is currently unused (but may be used in the future). If a section is used to provide common values to other sections, set this to true. Otherwise, the default of false indicates that the section should be referenced directly by providers.

provider[openstack].connection[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].connection "Link to this definition")

Type:_str_

The name of the [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) to use. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects and may not be changed via inheritance.

provider[openstack].flavor-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any flavor used with this provider. Many attributes which may be set on an individual flavor may be set once in this section and used for all the flavors in this provider. Values set on individual flavors may still override the values set here.

provider[openstack].flavor-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavor-defaults.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavor-defaults.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavor-defaults.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[openstack].flavor-defaults.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[openstack].flavor-defaults.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[openstack].flavor-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].flavor-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavor-defaults.volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].flavors[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors "Link to this definition")

Type:_dict_

A list of flavors associated with this provider.

provider[openstack].flavors.description[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[openstack].flavors.final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavors.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavors.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].flavors.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[openstack].flavors.flavor-name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.flavor-name "Link to this definition")

Type:_str_

Name or id of the OpenStack flavor to use.

provider[openstack].flavors.name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.name "Link to this definition")

Type:_str_

The name of the flavor. Used to refer to the flavor in Zuul configuration.

provider[openstack].flavors.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[openstack].flavors.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[openstack].flavors.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].flavors.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].flavors.volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].floating-ip-cleanup[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].floating-ip-cleanup "Link to this definition")

Default:`False`

Type:_bool_

If set to `true`, Zuul will behave as if it is the only user of the OpenStack project and will attempt to clean unattached floating IPs that may have leaked.

provider[openstack].image-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any image used with this provider. Many attributes which may be set on an individual image may be set once in this section and used for all the images in this provider. Values set on individual images may still override the values set here.

provider[openstack].image-defaults.config-drive[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.config-drive "Link to this definition")

Default:`True`

Type:_bool_

Whether config drive should be used for the cloud image.

provider[openstack].image-defaults.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[openstack].image-defaults.connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.connection-type.ssh "Link to this definition")
An ssh connection.

provider[openstack].image-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[openstack].image-defaults.import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[openstack].image-defaults.python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[openstack].image-defaults.shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[openstack].image-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[openstack].image-defaults.upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].image-defaults.upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[openstack].image-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].image-defaults.username[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[openstack].image-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].image-defaults.volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].images[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images "Link to this definition")

Type:_list_

A list of images associated with this provider.

provider[openstack].images[cloud][](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud] "Link to this definition")

Type:_dict_

These are the attributes available for a cloud image.

provider[openstack].images[cloud].config-drive[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].config-drive "Link to this definition")

Default:`True`

Type:_bool_

Whether config drive should be used for the cloud image.

provider[openstack].images[cloud].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[openstack].images[cloud].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].connection-type.ssh "Link to this definition")
An ssh connection.

provider[openstack].images[cloud].description[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[openstack].images[cloud].final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[openstack].images[cloud].image-id[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].image-id "Link to this definition")

Type:_str_

The ID of the cloud provider’s image.

provider[openstack].images[cloud].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[openstack].images[cloud].name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[openstack].images[cloud].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[openstack].images[cloud].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[openstack].images[cloud].type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].type "Link to this definition")

The type of image.

cloud[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[cloud].type.cloud "Link to this definition")
An existing image available in the cloud.

provider[openstack].images[cloud].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].images[cloud].username[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[openstack].images[cloud].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[cloud].volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].images[zuul][](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul] "Link to this definition")

Type:_dict_

These are the attributes available for a Zuul image.

provider[openstack].images[zuul].config-drive[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].config-drive "Link to this definition")

Default:`True`

Type:_bool_

Whether config drive should be used for the cloud image.

provider[openstack].images[zuul].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[openstack].images[zuul].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].connection-type.ssh "Link to this definition")
An ssh connection.

provider[openstack].images[zuul].description[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[openstack].images[zuul].final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[openstack].images[zuul].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[openstack].images[zuul].name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[openstack].images[zuul].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[openstack].images[zuul].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[openstack].images[zuul].tags[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[openstack].images[zuul].type[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].type "Link to this definition")

The type of image.

zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].type.zuul "Link to this definition")
An image managed by Zuul.

provider[openstack].images[zuul].upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].images[zuul].upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[openstack].images[zuul].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].images[zuul].username[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[openstack].images[zuul].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].images[zuul].volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].label-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any label used with this provider. Many attributes which may be set on an individual label may be set once in this section and used for all the labels in this provider. Values set on individual labels may still override the values set here.

provider[openstack].label-defaults.auto-floating-ip[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.auto-floating-ip "Link to this definition")

Default:`True`

Type:_bool_

Whether to automatically allocate and assign a floating IP for each node.

provider[openstack].label-defaults.az[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.az "Link to this definition")

Type:_str_

Servers will be assigned to the specified availibility zone. If omitted, one will be chosen at random.

provider[openstack].label-defaults.boot-from-volume[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.boot-from-volume "Link to this definition")

Default:`False`

Type:_bool_

Whether to create a volume from the image and boot the node from it.

provider[openstack].label-defaults.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[openstack].label-defaults.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[openstack].label-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].label-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].label-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].label-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[openstack].label-defaults.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[openstack].label-defaults.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[openstack].label-defaults.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[openstack].label-defaults.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[openstack].label-defaults.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[openstack].label-defaults.networks[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.networks "Link to this definition")

Type:_str_

The OpenStack networks to associate with the node.

provider[openstack].label-defaults.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[openstack].label-defaults.security-groups[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.security-groups "Link to this definition")

Type:_str_

Specify custom networks to be attached to each node. Specify the name or id of the network as a string.

provider[openstack].label-defaults.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[openstack].label-defaults.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[openstack].label-defaults.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[openstack].label-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[openstack].label-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].label-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].label-defaults.volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].labels[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels "Link to this definition")

Type:_dict_

A list of labels associated with this provider.

provider[openstack].labels.auto-floating-ip[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.auto-floating-ip "Link to this definition")

Default:`True`

Type:_bool_

Whether to automatically allocate and assign a floating IP for each node.

provider[openstack].labels.az[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.az "Link to this definition")

Type:_str_

Servers will be assigned to the specified availibility zone. If omitted, one will be chosen at random.

provider[openstack].labels.boot-from-volume[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.boot-from-volume "Link to this definition")

Default:`False`

Type:_bool_

Whether to create a volume from the image and boot the node from it.

provider[openstack].labels.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[openstack].labels.description[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.description "Link to this definition")

Type:_str_

A textual description of the label for reference purposes.

provider[openstack].labels.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[openstack].labels.final[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].labels.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].labels.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#value-provider[openstack].labels.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[openstack].labels.flavor[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.flavor "Link to this definition")

Type:_str_

The flavor to use with this label.

provider[openstack].labels.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[openstack].labels.image[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.image "Link to this definition")

Type:_str_

The image to use with this label.

provider[openstack].labels.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[openstack].labels.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[openstack].labels.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[openstack].labels.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[openstack].labels.name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.name "Link to this definition")

Type:_str_

The name of the label. Used to refer to the label in Zuul configuration.

provider[openstack].labels.networks[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.networks "Link to this definition")

Type:_str_

The OpenStack networks to associate with the node.

provider[openstack].labels.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[openstack].labels.security-groups[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.security-groups "Link to this definition")

Type:_str_

Specify custom networks to be attached to each node. Specify the name or id of the network as a string.

provider[openstack].labels.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[openstack].labels.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[openstack].labels.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[openstack].labels.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[openstack].labels.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[openstack].labels.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].labels.volume-size "Link to this definition")

Type:_int_

When booting an image from volume, this indicates the size of the created volume, in GB.

provider[openstack].launch-attempts[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].launch-attempts "Link to this definition")

Default:`3`

Type:_int_

The number of times to attempt launching a node before considering the request failed.

provider[openstack].launch-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].launch-timeout "Link to this definition")

Type:_int_

The time to wait from issuing the command to create a new node until the node is reporting as running. If the timeout is exceeded, the node launch is aborted and the node deleted.

provider[openstack].name[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].name "Link to this definition")

Type:_str_

The name of the provider. Used to refer to the provider in Zuul configuration.

provider[openstack].parent[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].parent "Link to this definition")

Type:_str_

The name of the parent section from which to inherit. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects. To indicate which section a provider should be attached to, use [provider[openstack].section](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].section "attr-provider[openstack].section")

provider[openstack].port-cleanup-interval[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].port-cleanup-interval "Link to this definition")

Default:`600`

Type:_int_

If greater than 0, Zuul will behave as if it is the only user of the OpenStack project and will attempt to clean ports in `DOWN` state after the cleanup interval has elapsed. This value may be reduced if the instance spawn time on the provider is reliably quicker.

provider[openstack].region[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].region "Link to this definition")

Type:_str_

The region name if the provider cloud has multiple regions.

provider[openstack].resource-limits[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits "Link to this definition")

Type:_dict_

Resource limits for this provider. Configure these values to cause Zuul to attempt to limit the resource usage. This can be used to limit Zuul’s usage to a level below the cloud quota.

provider[openstack].resource-limits.cores[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits.cores "Link to this definition")

Type:_int_

The number of cores.

provider[openstack].resource-limits.instances[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits.instances "Link to this definition")

Type:_int_

The number of instances.

provider[openstack].resource-limits.ram[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits.ram "Link to this definition")

Type:_int_

The amount of ram, in MiB.

provider[openstack].resource-limits.volume-gb[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits.volume-gb "Link to this definition")

Type:_int_

The amount of volume storage in GB.

provider[openstack].resource-limits.volumes[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].resource-limits.volumes "Link to this definition")

Type:_int_

The number of volumes.

provider[openstack].section[](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#attr-provider[openstack].section "Link to this definition")

Type:_str_

The name of the [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") from which to inherit.
