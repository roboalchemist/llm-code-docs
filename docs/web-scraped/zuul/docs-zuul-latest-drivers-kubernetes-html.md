# Source: https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html

Title: Kubernetes — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html

Markdown Content:
Zuul can use pods or namespaces from Kubernetes as a source for build nodes.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#connection-configuration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

The supported options in `zuul.conf` connections are:

<kubernetes connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-%3Ckubernetes%20connection%3E "Link to this definition")

<kubernetes connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-%3Ckubernetes%20connection%3E.driver "Link to this definition")

kubernetes[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-%3Ckubernetes%20connection%3E.driver.kubernetes "Link to this definition")
The connection must set `driver=kubernetes` for Kubernetes connections.

<kubernetes connection>.kubeconfig_file[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-%3Ckubernetes%20connection%3E.kubeconfig_file "Link to this definition")

A path to a kubeconfig file with credentials to access the Kubernetes cluster. If this is not present, Zuul will use the value of the KUBECONFIG environment variable. If neither this setting or the environment variable is present, then any credentials obtainable by the Kubernetes client library will be used.

<kubernetes connection>.context[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-%3Ckubernetes%20connection%3E.context "Link to this definition")

If the kubeconfig file has more than one context available, this option may be used to specify which one Zuul should use for this connection.

<kubernetes connection>.rate[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-%3Ckubernetes%20connection%3E.rate "Link to this definition")

Default:`2`

The API rate limit (in requests per second) to use when performing Kubernetes API calls.

Provider Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#provider-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The `kubernetes` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

provider[kubernetes][](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes] "Link to this definition")

Type:_dict_

The attributes available for configuring a Kubernetes provider are below.

provider[kubernetes].abstract[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].abstract "Link to this definition")

Default:`False`

Type:_bool_

Whether a section is intended to be inherited by another [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") or a [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider"). This setting is currently unused (but may be used in the future). If a section is used to provide common values to other sections, set this to true. Otherwise, the default of false indicates that the section should be referenced directly by providers.

provider[kubernetes].connection[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].connection "Link to this definition")

Type:_str_

The name of the [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) to use. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects and may not be changed via inheritance.

provider[kubernetes].flavor-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavor-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any flavor used with this provider. Many attributes which may be set on an individual flavor may be set once in this section and used for all the flavors in this provider. Values set on individual flavors may still override the values set here.

provider[kubernetes].flavor-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavor-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavor-defaults.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavor-defaults.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavor-defaults.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[kubernetes].flavors[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavors "Link to this definition")

Type:_dict_

A list of flavors associated with this provider.

provider[kubernetes].flavors.description[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavors.description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[kubernetes].flavors.final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavors.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavors.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavors.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].flavors.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[kubernetes].flavors.name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].flavors.name "Link to this definition")

Type:_str_

The name of the flavor. Used to refer to the flavor in Zuul configuration.

provider[kubernetes].image-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any image used with this provider. Many attributes which may be set on an individual image may be set once in this section and used for all the images in this provider. Values set on individual images may still override the values set here.

provider[kubernetes].image-defaults.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[kubernetes].image-defaults.connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.connection-type.ssh "Link to this definition")
An ssh connection.

provider[kubernetes].image-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[kubernetes].image-defaults.import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[kubernetes].image-defaults.python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[kubernetes].image-defaults.shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[kubernetes].image-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[kubernetes].image-defaults.upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].image-defaults.upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[kubernetes].image-defaults.username[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].image-defaults.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[kubernetes].images[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images "Link to this definition")

Type:_list_

A list of images associated with this provider.

provider[kubernetes].images[cloud][](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud] "Link to this definition")

Type:_dict_

These are the attributes available for a cloud image.

provider[kubernetes].images[cloud].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[kubernetes].images[cloud].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].connection-type.ssh "Link to this definition")
An ssh connection.

provider[kubernetes].images[cloud].description[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[kubernetes].images[cloud].final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[kubernetes].images[cloud].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[kubernetes].images[cloud].name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[kubernetes].images[cloud].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[kubernetes].images[cloud].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[kubernetes].images[cloud].type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].type "Link to this definition")

The type of image.

cloud[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[cloud].type.cloud "Link to this definition")
An existing image available in the cloud.

provider[kubernetes].images[cloud].username[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[cloud].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[kubernetes].images[zuul][](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul] "Link to this definition")

Type:_dict_

These are the attributes available for a Zuul image.

provider[kubernetes].images[zuul].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[kubernetes].images[zuul].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].connection-type.ssh "Link to this definition")
An ssh connection.

provider[kubernetes].images[zuul].description[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[kubernetes].images[zuul].final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[kubernetes].images[zuul].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[kubernetes].images[zuul].name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[kubernetes].images[zuul].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[kubernetes].images[zuul].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[kubernetes].images[zuul].tags[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[kubernetes].images[zuul].type[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].type "Link to this definition")

The type of image.

zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].type.zuul "Link to this definition")
An image managed by Zuul.

provider[kubernetes].images[zuul].upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].images[zuul].upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[kubernetes].images[zuul].username[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].images[zuul].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[kubernetes].label-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any label used with this provider. Many attributes which may be set on an individual label may be set once in this section and used for all the labels in this provider. Values set on individual labels may still override the values set here.

provider[kubernetes].label-defaults.annotations[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.annotations "Link to this definition")

Type:_dict_

A dictionary of additional values to be added to the pod metadata. The value of this field is added to the metadata.annotations field in Kubernetes. This field contains arbitrary key/value pairs that can be accessed by tools and libraries.

provider[kubernetes].label-defaults.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[kubernetes].label-defaults.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[kubernetes].label-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].label-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].label-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].label-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[kubernetes].label-defaults.image-pull-secrets[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.image-pull-secrets "Link to this definition")

Type:_dict_

The imagePullSecrets needed to pull container images from a private registry. Because Zuul creates pods in a new namespace, and image pull secrets must exist in the namespace of the pods that use them, the referenced secrets will be copied into the temporary namespace that Zuul creates before creating the pod. The new secrets will have the same name as the old secrets.

Each entry is a dictionary with the following keys:

provider[kubernetes].label-defaults.image-pull-secrets.name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.image-pull-secrets.name "Link to this definition")

Type:_str_

Identifier for this secret. The referenced secret must already exist under this name so that Nodepool may copy it. It will be copied into the new namespace with the same name, therefore, if multiple entries are provided, they must have distinct names.

provider[kubernetes].label-defaults.image-pull-secrets.namespace[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.image-pull-secrets.namespace "Link to this definition")

Default:`default`

Type:_str_

The namespace of the existing secret to copy.

provider[kubernetes].label-defaults.kind[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.kind "Link to this definition")

The Kubernetes driver supports two types of labels:

pod[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].label-defaults.kind.pod "Link to this definition")
Pod labels provide a dedicated namespace with a single pod and a service account that can exec and get the logs of the pod.

namespace[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].label-defaults.kind.namespace "Link to this definition")
Namespace labels provide an empty namespace configured with a service account that can create pods, services, configmaps, etc.

provider[kubernetes].label-defaults.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[kubernetes].label-defaults.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[kubernetes].label-defaults.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[kubernetes].label-defaults.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[kubernetes].label-defaults.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[kubernetes].label-defaults.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[kubernetes].label-defaults.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[kubernetes].label-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].label-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[kubernetes].labels[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels "Link to this definition")

Type:_dict_

A list of labels associated with this provider.

provider[kubernetes].labels.annotations[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.annotations "Link to this definition")

Type:_dict_

A dictionary of additional values to be added to the pod metadata. The value of this field is added to the metadata.annotations field in Kubernetes. This field contains arbitrary key/value pairs that can be accessed by tools and libraries.

provider[kubernetes].labels.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[kubernetes].labels.description[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.description "Link to this definition")

Type:_str_

A textual description of the label for reference purposes.

provider[kubernetes].labels.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[kubernetes].labels.final[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].labels.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].labels.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].labels.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[kubernetes].labels.flavor[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.flavor "Link to this definition")

Type:_str_

The flavor to use with this label.

provider[kubernetes].labels.image[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.image "Link to this definition")

Type:_str_

The image to use with this label.

provider[kubernetes].labels.image-pull-secrets[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.image-pull-secrets "Link to this definition")

Type:_dict_

The imagePullSecrets needed to pull container images from a private registry. Because Zuul creates pods in a new namespace, and image pull secrets must exist in the namespace of the pods that use them, the referenced secrets will be copied into the temporary namespace that Zuul creates before creating the pod. The new secrets will have the same name as the old secrets.

Each entry is a dictionary with the following keys:

provider[kubernetes].labels.image-pull-secrets.name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.image-pull-secrets.name "Link to this definition")

Type:_str_

Identifier for this secret. The referenced secret must already exist under this name so that Nodepool may copy it. It will be copied into the new namespace with the same name, therefore, if multiple entries are provided, they must have distinct names.

provider[kubernetes].labels.image-pull-secrets.namespace[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.image-pull-secrets.namespace "Link to this definition")

Default:`default`

Type:_str_

The namespace of the existing secret to copy.

provider[kubernetes].labels.kind[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.kind "Link to this definition")

The Kubernetes driver supports two types of labels:

pod[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].labels.kind.pod "Link to this definition")
Pod labels provide a dedicated namespace with a single pod and a service account that can exec and get the logs of the pod.

namespace[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#value-provider[kubernetes].labels.kind.namespace "Link to this definition")
Namespace labels provide an empty namespace configured with a service account that can create pods, services, configmaps, etc.

provider[kubernetes].labels.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[kubernetes].labels.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[kubernetes].labels.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[kubernetes].labels.name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.name "Link to this definition")

Type:_str_

The name of the label. Used to refer to the label in Zuul configuration.

provider[kubernetes].labels.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[kubernetes].labels.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[kubernetes].labels.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[kubernetes].labels.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[kubernetes].labels.spec[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.spec "Link to this definition")

Type:_dict_

Zuul will supply the contents of this value verbatim to Kubernetes as the `spec` attribute of the Kubernetes `Pod` definition.

This attribute allows for the creation of arbitrary complex pod definitions but the user is responsible for ensuring that they are suitable. The first container in the pod is expected to be a long-running container that hosts a shell environment for running commands. The following minimal definition is recommended as a starting point:

labels:
 - name: custom-pod
 kind: pod
 spec:
 containers:
 - name: custom-pod
 image: ubuntu:jammy
 imagePullPolicy: IfNotPresent
 command: ["/bin/sh", "-c"]
 args: ["sleep infinity"]

provider[kubernetes].labels.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].labels.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[kubernetes].launch-attempts[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].launch-attempts "Link to this definition")

Default:`3`

Type:_int_

The number of times to attempt launching a node before considering the request failed.

provider[kubernetes].launch-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].launch-timeout "Link to this definition")

Type:_int_

The time to wait from issuing the command to create a new node until the node is reporting as running. If the timeout is exceeded, the node launch is aborted and the node deleted.

provider[kubernetes].name[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].name "Link to this definition")

Type:_str_

The name of the provider. Used to refer to the provider in Zuul configuration.

provider[kubernetes].parent[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].parent "Link to this definition")

Type:_str_

The name of the parent section from which to inherit. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects. To indicate which section a provider should be attached to, use [provider[kubernetes].section](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].section "attr-provider[kubernetes].section")

provider[kubernetes].resource-limits[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].resource-limits "Link to this definition")

Type:_dict_

Resource limits for this provider. Configure these values to cause Zuul to attempt to limit the resource usage. This can be used to limit Zuul’s usage to a level below the cloud quota.

provider[kubernetes].resource-limits.namespaces[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].resource-limits.namespaces "Link to this definition")

Type:_int_

The number of pods.

provider[kubernetes].resource-limits.pods[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].resource-limits.pods "Link to this definition")

Type:_int_

The number of pods.

provider[kubernetes].section[](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#attr-provider[kubernetes].section "Link to this definition")

Type:_str_

The name of the [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") from which to inherit.
