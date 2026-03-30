# Source: https://zuul-ci.org/docs/zuul/latest/drivers/aws.html

Title: AWS — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/aws.html

Markdown Content:
Zuul can use AWS as a source for build nodes.

If using the AWS driver to upload images, see [VM Import/Export service role](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-role) for information on configuring the required permissions in AWS. You must also create an S3 Bucket for use by Zuul if uploading images (except when using the `ebs-direct` upload method).

A number of methods for configuration authentication are available:

*   Supplying values directly in `zuul.conf`

*   A shared credential file

*   [Environment variables](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-environment-variables%60)

Zuul will try to obtain credential information from those sources in that order.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#connection-configuration "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

The supported options in `zuul.conf` connections are:

<aws connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E "Link to this definition")

<aws connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.driver "Link to this definition")

aws[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-%3Caws%20connection%3E.driver.aws "Link to this definition")
The connection must set `driver=aws` for AWS connections.

<aws connection>.shared_credentials_file[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.shared_credentials_file "Link to this definition")

A path to a [configuration file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-a-configuration-file) with shared access credentials. If this is supplied, no other credential settings need to be present.

<aws connection>.access_key_id[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.access_key_id "Link to this definition")

The AWS access key id.

<aws connection>.secret_access_key[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.secret_access_key "Link to this definition")

The AWS secret access key.

<aws connection>.profile[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.profile "Link to this definition")

The AWS profile.

<aws connection>.role_arn[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.role_arn "Link to this definition")

When using a federated web identity token, this specifies the AWS IAM role that should be assumed. If this is specified, then [<aws connection>.web_identity_token_file](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.web_identity_token_file "attr-<aws connection>.web_identity_token_file") should be provided, and the access key settings should be omitted.

<aws connection>.web_identity_token_file[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.web_identity_token_file "Link to this definition")

The path to a file containing a federated web identity token. Generally created by a cloud or Kubernetes environment.

<aws connection>.rate[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-%3Caws%20connection%3E.rate "Link to this definition")

Default:`2`

The API rate limit (in requests per second) to use when performing API calls with AWS.

Provider Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#provider-configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

The `aws` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

provider[aws][](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws] "Link to this definition")

Type:_dict_

The attributes available for configuring an AWS provider are below.

provider[aws].abstract[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].abstract "Link to this definition")

Default:`False`

Type:_bool_

Whether a section is intended to be inherited by another [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") or a [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider"). This setting is currently unused (but may be used in the future). If a section is used to provide common values to other sections, set this to true. Otherwise, the default of false indicates that the section should be referenced directly by providers.

provider[aws].connection[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].connection "Link to this definition")

Type:_str_

The name of the [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) to use. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects and may not be changed via inheritance.

provider[aws].flavor-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any flavor used with this provider. Many attributes which may be set on an individual flavor may be set once in this section and used for all the flavors in this provider. Values set on individual flavors may still override the values set here.

provider[aws].flavor-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavor-defaults.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavor-defaults.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavor-defaults.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[aws].flavor-defaults.imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavor-defaults.imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavor-defaults.imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].flavor-defaults.iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].flavor-defaults.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[aws].flavor-defaults.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[aws].flavor-defaults.throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].flavor-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].flavor-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].flavor-defaults.volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavor-defaults.volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].flavors[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors "Link to this definition")

Type:_dict_

A list of flavors associated with this provider.

provider[aws].flavors.dedicated-host[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.dedicated-host "Link to this definition")

Default:`False`

Type:_bool_

If set to `true`, an AWS dedicated host will be allocated for the instance. The host may be used for one or more nodes depending on the settings of [provider[aws].labels.slots](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.slots "attr-provider[aws].labels.slots") and [provider[aws].labels.reuse](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.reuse "attr-provider[aws].labels.reuse").

If this option is set, the [spot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.market-type.spot "value-provider[aws].flavors.market-type.spot") option is not available, and [provider[aws].labels.az](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.az "attr-provider[aws].labels.az") option is required.

provider[aws].flavors.description[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[aws].flavors.ebs-optimized[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.ebs-optimized "Link to this definition")

Default:`False`

Type:_bool_

Indicates whether EBS optimization (additional, dedicated throughput between Amazon EC2 and Amazon EBS) should be enabled for the instance.

provider[aws].flavors.final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[aws].flavors.fleet[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.fleet "Link to this definition")

Type:_dict_

If specified, the EC2 Fleet API will be used for launching the instance. In this case, quota is not checked before launching the instance, but is taken into account after the instance is launched. Mutually exclusive with [provider[aws].flavors.instance-type](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.instance-type "attr-provider[aws].flavors.instance-type").

provider[aws].flavors.fleet.allocation-strategy[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.fleet.allocation-strategy "Link to this definition")

The allocation strategy to use when launching the instance.

prioritized[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.fleet.allocation-strategy.prioritized "Link to this definition")
The prioritized allocation strategy. Available for on-demand instances

price-capacity-optimized[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.fleet.allocation-strategy.price-capacity-optimized "Link to this definition")
The price-capacity-optimized allocation strategy. Available for spot instances

capacity-optimized[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.fleet.allocation-strategy.capacity-optimized "Link to this definition")
The capacity-optimized allocation strategy. Available for spot instances

diversified[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.fleet.allocation-strategy.diversified "Link to this definition")
The diversified allocation strategy. Available for spot instances

lowest-price[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.fleet.allocation-strategy.lowest-price "Link to this definition")
The lowest-price allocation strategy. Available for spot or on-demand instances

provider[aws].flavors.fleet.instance-types[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.fleet.instance-types "Link to this definition")

Type:_str_

A list of instance types from which AWS may select when launching the instance.

provider[aws].flavors.imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].flavors.instance-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.instance-type "Link to this definition")

Type:_str_

Name of the AWS instance type to use.. Mutually exclusive with [provider[aws].flavors.fleet](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.fleet "attr-provider[aws].flavors.fleet").

provider[aws].flavors.iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].flavors.market-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.market-type "Link to this definition")

Default:`on-demand`

Whether to request an on-demand or spot instance.

on-demand[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.market-type.on-demand "Link to this definition")
This is the typical EC2 instance where continued availability is guaranteed after allocation.

spot[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].flavors.market-type.spot "Link to this definition")
Request an Amazon EC2 Spot instance instead of an On-Demand instance. Spot instances take advantage of unused EC2 capacity at a discount, but if demand is high, instances may be unavailable. In addition, Amazon EC2 may interrupt Spot instances and reclaim them. Alternative nodesets with On-Demand instances configured as a fallback may be configured in order to mitigate this.

provider[aws].flavors.name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.name "Link to this definition")

Type:_str_

The name of the flavor. Used to refer to the flavor in Zuul configuration.

provider[aws].flavors.nested-virtualization[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.nested-virtualization "Link to this definition")

Type:_bool_

Whether nested-virtualization should be enabled for the instance.

provider[aws].flavors.public-ipv4[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.public-ipv4 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv4 address should be attached to nodes.

provider[aws].flavors.public-ipv6[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.public-ipv6 "Link to this definition")

Default:`False`

Type:_bool_

Whether a public IPv6 address should be attached to nodes.

provider[aws].flavors.throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].flavors.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].flavors.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].flavors.volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].flavors.volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].image-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any image used with this provider. Many attributes which may be set on an individual image may be set once in this section and used for all the images in this provider. Values set on individual images may still override the values set here.

provider[aws].image-defaults.architecture[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.architecture "Link to this definition")

Default:`x86_64`

Type:_str_

The architecture of the image. See the [AWS RegisterImage API documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html) for valid values.

provider[aws].image-defaults.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[aws].image-defaults.connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.connection-type.ssh "Link to this definition")
An ssh connection.

provider[aws].image-defaults.ena-support[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.ena-support "Link to this definition")

Default:`True`

Type:_bool_

Whether the image has support for the AWS Enhanced Networking Adapter (ENA). Many newer operating systems include driver support as standard and some AWS instance types require it.

provider[aws].image-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[aws].image-defaults.image-format[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.image-format "Link to this definition")

Default:`raw`

The image format that should be used when building and uploading or importing the image.

ova[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.ova "Link to this definition")
The OVA image format.

vhd[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.vhd "Link to this definition")
The VHD image format.

vhdx[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.vhdx "Link to this definition")
The VHDX image format.

vmdk[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.vmdk "Link to this definition")
The VMDK image format.

raw[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.raw "Link to this definition")
A raw image.

snapshot[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.image-format.snapshot "Link to this definition")
Rather than producing an image artifact and uploading or importing it, this image is created by snapshotting a running instance.

provider[aws].image-defaults.imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].image-defaults.imds-support[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.imds-support "Link to this definition")

Default:`None`

Controls the usage of IMDSv2 on instances created from the image, This is only supported using the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

v2.0[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.imds-support.v2.0 "Link to this definition")
Enforces usage of IMDSv2 by default on instances created from the image.

null[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.imds-support.null "Link to this definition")
IMDSv2 is optional.

provider[aws].image-defaults.import-method[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.import-method "Link to this definition")

Default:`snapshot`

The method to use when importing the image.

snapshot[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.import-method.snapshot "Link to this definition")
This method uploads the image file to AWS as a snapshot and then registers an AMI directly from the snapshot. This is faster compared to the image method and may be used with operating systems and versions that AWS does not otherwise support. However, it is incompatible with some operating systems which require special licensing or other metadata in AWS.

image[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.import-method.image "Link to this definition")
This method uploads the image file to AWS and performs an “image import” on the file. This causes AWS to boot the image in a temporary VM and then take a snapshot of that VM which is then used as the basis of the AMI. This is slower compared to the snapshot method and may only be used with operating systems and versions which AWS already supports. This may be necessary in order to use Windows images.

ebs-direct[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.import-method.ebs-direct "Link to this definition")
This is similar to the snapshot method, but uses the [EBS direct API](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-accessing-snapshot.html) instead of S3. This may be faster and more efficient, but it may incur additional costs.

provider[aws].image-defaults.import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[aws].image-defaults.iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].image-defaults.python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[aws].image-defaults.shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[aws].image-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[aws].image-defaults.throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].image-defaults.upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].image-defaults.upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[aws].image-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].image-defaults.username[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[aws].image-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].image-defaults.volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].image-defaults.volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].images[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images "Link to this definition")

Type:_list_

A list of images associated with this provider.

provider[aws].images[cloud][](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud] "Link to this definition")

Type:_dict_

These are the attributes available for a cloud image.

provider[aws].images[cloud].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[aws].images[cloud].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].connection-type.ssh "Link to this definition")
An ssh connection.

provider[aws].images[cloud].description[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[aws].images[cloud].final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[aws].images[cloud].image-filters[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-filters "Link to this definition")

Type:_dict_

If provided, this is used to select an AMI by filters. If the filters provided match more than one image, the most recent will be returned. Either this field or [provider[aws].images[cloud].image-id](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-id "attr-provider[aws].images[cloud].image-id") must be provided.

This field may be provided as a dictionary, or a list of dictionaries with the following keys:

provider[aws].images[cloud].image-filters.name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-filters.name "Link to this definition")

Type:_str_

The filter name. See [Boto describe images](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_images) for a list of valid filters.

provider[aws].images[cloud].image-filters.values[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-filters.values "Link to this definition")

Type:_str_

A list of string values on which to filter.

provider[aws].images[cloud].image-id[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-id "Link to this definition")

Type:_str_

If this is provided, it is used to select the AMI from AWS by ID. Either this field or [provider[aws].images[cloud].image-filters](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].image-filters "attr-provider[aws].images[cloud].image-filters") must be provided.

provider[aws].images[cloud].imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].images[cloud].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[aws].images[cloud].iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].images[cloud].name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[aws].images[cloud].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[aws].images[cloud].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[aws].images[cloud].throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].images[cloud].type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].type "Link to this definition")

The type of image.

cloud[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[cloud].type.cloud "Link to this definition")
An existing image available in the cloud.

provider[aws].images[cloud].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].images[cloud].username[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[aws].images[cloud].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].images[cloud].volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[cloud].volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].images[zuul][](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul] "Link to this definition")

Type:_dict_

These are the attributes available for a Zuul image.

provider[aws].images[zuul].architecture[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].architecture "Link to this definition")

Default:`x86_64`

Type:_str_

The architecture of the image. See the [AWS RegisterImage API documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html) for valid values.

provider[aws].images[zuul].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[aws].images[zuul].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].connection-type.ssh "Link to this definition")
An ssh connection.

provider[aws].images[zuul].description[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[aws].images[zuul].ena-support[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].ena-support "Link to this definition")

Default:`True`

Type:_bool_

Whether the image has support for the AWS Enhanced Networking Adapter (ENA). Many newer operating systems include driver support as standard and some AWS instance types require it.

provider[aws].images[zuul].final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[aws].images[zuul].image-format[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].image-format "Link to this definition")

Default:`raw`

The image format that should be used when building and uploading or importing the image.

ova[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.ova "Link to this definition")
The OVA image format.

vhd[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.vhd "Link to this definition")
The VHD image format.

vhdx[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.vhdx "Link to this definition")
The VHDX image format.

vmdk[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.vmdk "Link to this definition")
The VMDK image format.

raw[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.raw "Link to this definition")
A raw image.

snapshot[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].image-format.snapshot "Link to this definition")
Rather than producing an image artifact and uploading or importing it, this image is created by snapshotting a running instance.

provider[aws].images[zuul].imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].images[zuul].imds-support[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].imds-support "Link to this definition")

Default:`None`

Controls the usage of IMDSv2 on instances created from the image, This is only supported using the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

v2.0[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].imds-support.v2.0 "Link to this definition")
Enforces usage of IMDSv2 by default on instances created from the image.

null[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].imds-support.null "Link to this definition")
IMDSv2 is optional.

provider[aws].images[zuul].import-method[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].import-method "Link to this definition")

Default:`snapshot`

The method to use when importing the image.

snapshot[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "Link to this definition")
This method uploads the image file to AWS as a snapshot and then registers an AMI directly from the snapshot. This is faster compared to the image method and may be used with operating systems and versions that AWS does not otherwise support. However, it is incompatible with some operating systems which require special licensing or other metadata in AWS.

image[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.image "Link to this definition")
This method uploads the image file to AWS and performs an “image import” on the file. This causes AWS to boot the image in a temporary VM and then take a snapshot of that VM which is then used as the basis of the AMI. This is slower compared to the snapshot method and may only be used with operating systems and versions which AWS already supports. This may be necessary in order to use Windows images.

ebs-direct[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "Link to this definition")
This is similar to the snapshot method, but uses the [EBS direct API](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-accessing-snapshot.html) instead of S3. This may be faster and more efficient, but it may incur additional costs.

provider[aws].images[zuul].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[aws].images[zuul].iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].images[zuul].name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[aws].images[zuul].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[aws].images[zuul].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[aws].images[zuul].tags[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[aws].images[zuul].throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].images[zuul].type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].type "Link to this definition")

The type of image.

zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].type.zuul "Link to this definition")
An image managed by Zuul.

provider[aws].images[zuul].upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[aws].images[zuul].userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].images[zuul].username[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[aws].images[zuul].volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].images[zuul].volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].images[zuul].volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].label-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any label used with this provider. Many attributes which may be set on an individual label may be set once in this section and used for all the labels in this provider. Values set on individual labels may still override the values set here.

provider[aws].label-defaults.az[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.az "Link to this definition")

Type:_str_

Instances will be assigned to the specified availibility zone. If omitted, AWS will select from the available zones.

provider[aws].label-defaults.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[aws].label-defaults.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[aws].label-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].label-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].label-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].label-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[aws].label-defaults.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[aws].label-defaults.iam-instance-profile[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.iam-instance-profile "Link to this definition")

Type:_dict_

Used to attach an IAM instance profile. Useful for giving access to services without needing any secrets.

provider[aws].label-defaults.iam-instance-profile.arn[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.iam-instance-profile.arn "Link to this definition")

Type:_str_

ARN identifier of the profile. Mutually exclusive with [provider[aws].labels.iam-instance-profile.name](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.name "attr-provider[aws].labels.iam-instance-profile.name")

provider[aws].label-defaults.iam-instance-profile.name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.iam-instance-profile.name "Link to this definition")

Type:_str_

Name of the instance profile. Mutually exclusive with [provider[aws].labels.iam-instance-profile.arn](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.arn "attr-provider[aws].labels.iam-instance-profile.arn")

provider[aws].label-defaults.imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].label-defaults.imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].label-defaults.imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].label-defaults.iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].label-defaults.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[aws].label-defaults.kms-key-id[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.kms-key-id "Link to this definition")

Type:_str_

The KMS key id to use when launching instances from an encrypted image. Typically only necessary when using images shared from a different AWS account.

provider[aws].label-defaults.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[aws].label-defaults.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[aws].label-defaults.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[aws].label-defaults.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[aws].label-defaults.security-group-ids[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.security-group-ids "Link to this definition")

Type:_str_

Specifies the security group IDs to assign to the node’s network interfaces.

provider[aws].label-defaults.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[aws].label-defaults.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[aws].label-defaults.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[aws].label-defaults.subnet-ids[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.subnet-ids "Link to this definition")

Type:_str_

Specifies the subnets to assign to the node’s network interfaces.

provider[aws].label-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[aws].label-defaults.throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].label-defaults.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].label-defaults.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].label-defaults.volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].label-defaults.volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].labels[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels "Link to this definition")

Type:_dict_

A list of labels associated with this provider.

provider[aws].labels.az[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.az "Link to this definition")

Type:_str_

Instances will be assigned to the specified availibility zone. If omitted, AWS will select from the available zones.

provider[aws].labels.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[aws].labels.description[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.description "Link to this definition")

Type:_str_

A textual description of the label for reference purposes.

provider[aws].labels.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[aws].labels.final[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].labels.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].labels.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].labels.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[aws].labels.flavor[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.flavor "Link to this definition")

Type:_str_

The flavor to use with this label.

provider[aws].labels.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[aws].labels.iam-instance-profile[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile "Link to this definition")

Type:_dict_

Used to attach an IAM instance profile. Useful for giving access to services without needing any secrets.

provider[aws].labels.iam-instance-profile.arn[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.arn "Link to this definition")

Type:_str_

ARN identifier of the profile. Mutually exclusive with [provider[aws].labels.iam-instance-profile.name](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.name "attr-provider[aws].labels.iam-instance-profile.name")

provider[aws].labels.iam-instance-profile.name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.name "Link to this definition")

Type:_str_

Name of the instance profile. Mutually exclusive with [provider[aws].labels.iam-instance-profile.arn](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iam-instance-profile.arn "attr-provider[aws].labels.iam-instance-profile.arn")

provider[aws].labels.image[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.image "Link to this definition")

Type:_str_

The image to use with this label.

provider[aws].labels.imds-http-tokens[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.imds-http-tokens "Link to this definition")

Specify whether IMDSv2 is required. If this is omitted, then AWS defaults are used (usually equivalent to `optional` but may be influenced by the image used).

optional[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].labels.imds-http-tokens.optional "Link to this definition")
Allows usage of IMDSv2 but do not require it. This sets the following metadata options:

*   HttpTokens is optional

*   HttpEndpoint is enabled

required[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].labels.imds-http-tokens.required "Link to this definition")
Require IMDSv2. This sets the following metadata options:

*   HttpTokens is required

*   HttpEndpoint is enabled

provider[aws].labels.iops[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.iops "Link to this definition")

Type:_int_

The number of I/O operations per second to be provisioned for the volume. The default varies based on the volume type; see the documentation under [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the specific volume type for details.

provider[aws].labels.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[aws].labels.kms-key-id[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.kms-key-id "Link to this definition")

Type:_str_

The KMS key id to use when launching instances from an encrypted image. Typically only necessary when using images shared from a different AWS account.

provider[aws].labels.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[aws].labels.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[aws].labels.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[aws].labels.name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.name "Link to this definition")

Type:_str_

The name of the label. Used to refer to the label in Zuul configuration.

provider[aws].labels.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[aws].labels.security-group-ids[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.security-group-ids "Link to this definition")

Type:_str_

Specifies the security group IDs to assign to the node’s network interfaces.

provider[aws].labels.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[aws].labels.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[aws].labels.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[aws].labels.subnet-ids[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.subnet-ids "Link to this definition")

Type:_str_

Specifies the subnets to assign to the node’s network interfaces.

provider[aws].labels.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[aws].labels.throughput[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.throughput "Link to this definition")

Type:_int_

The throughput of the volume in MiB/s. This is only valid for `gp3` volumes.

provider[aws].labels.userdata[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.userdata "Link to this definition")

Type:_str_

A string of userdata for a node. Systems such as “cloud-init” may use this to configure the node on boot.

provider[aws].labels.volume-size[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.volume-size "Link to this definition")

Type:_int_

The size of the root EBS volume, in GiB, for the image. If omitted, the volume size reported for the imported snapshot will be used. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].labels.volume-type[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].labels.volume-type "Link to this definition")

Default:`gp3`

Type:_str_

The root [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) for the image. Only used with the [snapshot](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.snapshot "value-provider[aws].images[zuul].import-method.snapshot") or [ebs-direct](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#value-provider[aws].images[zuul].import-method.ebs-direct "value-provider[aws].images[zuul].import-method.ebs-direct") import methods.

provider[aws].launch-attempts[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].launch-attempts "Link to this definition")

Default:`3`

Type:_int_

The number of times to attempt launching a node before considering the request failed.

provider[aws].launch-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].launch-timeout "Link to this definition")

Type:_int_

The time to wait from issuing the command to create a new node until the node is reporting as running. If the timeout is exceeded, the node launch is aborted and the node deleted.

provider[aws].name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].name "Link to this definition")

Type:_str_

The name of the provider. Used to refer to the provider in Zuul configuration.

provider[aws].object-storage[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].object-storage "Link to this definition")

Type:_dict_

Configuration options related to object storage used for image management.

provider[aws].object-storage.bucket-name[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].object-storage.bucket-name "Link to this definition")

Type:_str_

The name of the S3 bucket that should be used when importing Zuul images.

provider[aws].parent[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].parent "Link to this definition")

Type:_str_

The name of the parent section from which to inherit. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects. To indicate which section a provider should be attached to, use [provider[aws].section](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].section "attr-provider[aws].section")

provider[aws].region[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].region "Link to this definition")

Type:_str_

The name of the [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html) to interact with.

provider[aws].resource-limits[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].resource-limits "Link to this definition")

Type:_dict_

Resource limits for this provider. Configure these values to cause Zuul to attempt to limit the resource usage. This can be used to limit Zuul’s usage to a level below the cloud quota.

In addition to the options listed below, it is possible to configure a limit for any of the quota codes supported by AWS.

provider[aws].resource-limits.cores[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].resource-limits.cores "Link to this definition")

Type:_int_

The number of cores.

provider[aws].resource-limits.instances[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].resource-limits.instances "Link to this definition")

Type:_int_

The number of instances.

provider[aws].resource-limits.ram[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].resource-limits.ram "Link to this definition")

Type:_int_

The amount of ram, in MiB.

provider[aws].section[](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#attr-provider[aws].section "Link to this definition")

Type:_str_

The name of the [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") from which to inherit.
