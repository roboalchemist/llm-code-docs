# Source: https://docs.vespa.ai/en/applications/deployment.html.md

# Source: https://docs.vespa.ai/en/reference/applications/deployment.html.md

# deployment.xml reference

 

_deployment.xml_ controls how an application is deployed.

_deployment.xml_ is placed in the root of the [application package](../../basics/applications.html) and specifies which environments and regions the application is deployed to during [automated application deployment](../../operations/automated-deployments.html), as which application instances.

Deployment progresses through the `test` and `staging` environments to the `prod` environments listed in _deployment.xml_.

Simple example:

```
```
<deployment version="1.0">
    <prod>
        <region>aws-us-east-1c</region>
        <region>aws-us-west-2a</region>
    </prod>
</deployment>
```
```

More complex example:

```
```
<deployment version="1.0">
    <instance id="beta">
        <prod>
            <region>aws-us-east-1c</region>
        </prod>
    </instance>
    <instance id="default">
        <block-change revision="false"
                      days="mon,wed-fri"
                      hours="16-23"
                      time-zone="UTC" />
        <prod>
            <region>aws-us-east-1c</region>
            <delay hours="3" minutes="7" seconds="13" />
            <parallel>
                <region>aws-us-west-1c</region>
                <steps>
                    <region>aws-eu-west-1a</region>
                    <delay hours="3" />
                    <test>aws-us-west-2a</test>
                </steps>
            </parallel>
        </prod>
        <endpoints>
            <endpoint container-id="my-container-service">
                <region>aws-us-east-1c</region>
            </endpoint>
        </endpoints>
    </instance>
    <endpoints>
        <endpoint id="my-weighted-endpoint"
                  container-id="my-container-service"
                  region="aws-us-east-1c">
          <instance weight="1">beta</instance>
        </endpoint>
    </endpoints>
</deployment>
```
```

Some of the elements can be declared _either_ under the `<deployment>` root, **or**, if one or more `<instance>` tags are listed, under these. These have a bold **or** when listing where they may be present.

## deployment

The root element.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| version | Yes | 1.0 |
| major-version | No | The major version number this application is valid for. |
| cloud-account | No | Account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). |

## instance

In `<deployment>` or `<parallel>` (which must be a direct descendant of the root). An instance of the application; several of these may be simultaneously deployed in the same zone. If no `<instance>` is specified, all children of the root are implicitly children of an `<instance>` with `id="default"`, as in the simple example at the top.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| id | Yes | The unique name of the instance. |
| tags | No | Space-separated tags which can be referenced to make [deployment variants](../../operations/deployment-variants.html). |
| cloud-account | No | Account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. |

## block-change

In `<deployment>`, **or** `<instance>`. This blocks changes from being deployed to production in the matching time interval. Changes are nevertheless tested while blocked.

By default, both application revision changes and Vespa platform changes (upgrades) are blocked. It is possible to block just one kind of change using the `revision` and `version` attributes.

Any combination of the attributes below can be specified. Changes on a given date will be blocked if all conditions are met. Invalid `<block-change>` tags (i.e. that contains conditions that never match an actual date) are rejected by the system.

This tag must be placed after any `<test>` and `<staging>` tags, and before `<prod>`. It can be declared multiple times.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| revision | No, default `true` | Set to `false` to allow application deployments |
| version | No, default `true` | Set to `false` to allow Vespa platform upgrades |
| days | No, default `mon-sun` | List of days this block is effective - a comma-separated list of single days or day intervals where the start and end day are separated by a dash and are inclusive. Each day is identified by its english name or three-letter abbreviation. |
| hours | No, default `0-23` | List of hours this block is effective - a comma-separated list of single hours or hour intervals where the start and end hour are separated by a dash and are inclusive. Each hour is identified by a number in the range 0 to 23. |
| time-zone | No, default UTC | The name of the time zone used to interpret the hours attribute. Time zones are full names or short forms, when the latter is unambiguous. See [ZoneId.of](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html#of-java.lang.String-) for the full spec of acceptable values. |
| from-date | No | The inclusive starting date of this block (ISO-8601, `YYYY-MM-DD`). |
| to-date | No | The inclusive ending date of this block (ISO-8601, `YYYY-MM-DD`). |

The below example blocks all changes on weekends, and blocks revisions outside working hours, in the PST time zone:

```
```
<block-change days="sat-sun"
              hours="0-23"
              time-zone="America/Los_Angeles"/>
<block-change revision="false"
              days="mon-fri,sat,sun"
              hours="0-8,16-23"
              time-zone="America/Los_Angeles"/>
```
```

The below example blocks:

- all changes on Sundays starting on 2022-03-01
- all changes in the hours 16-23 between 2022-02-10 and 2022-02-15
- all changes until 2022-01-05

```
```
<block-change days="sun"
              from-date="2022-03-01"
              time-zone="America/Los_Angeles"/>
<block-change hours="16-23"
              from-date="2022-02-10"
              to-date="2022-02-15"
              time-zone="America/Los_Angeles"/>
<block-change to-date="2022-01-05"
              time-zone="America/Los_Angeles"/>
```
```

## upgrade

In `<deployment>`, or `<instance>`. Determines the strategy for upgrading the application, or one of its instances. By default, application revision changes and Vespa platform changes are deployed separately. The exception is when an upgrade fails; then, the latest application revision is deployed together with the upgrade, as these may be necessary to fix the upgrade failure.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| rollout | No, default `separate` | 
- `separate` is the default. When a revision catches up to a platform upgrade, it stays behind, unless the upgrade alone fails.
- `simultaneous` favors revision roll-out. When a revision catches up to a platform upgrade, it joins, and then passes the upgrade.

 |
| revision-target | No, default `latest` | 
- `latest` is the default. When rolling out a new revision to an instance, the latest available revision is chosen.
- `next` trades speed for smaller changes. When rolling out a new revision to an instance, the next available revision is chosen.

 The available revisions for an instance are revisions which are not yet deployed, or revisions which have rolled out in previous instances. |
| revision-change | No, default `when-failing` | 
- `always` is the most aggressive setting. A new, available revision may always replace the one which is currently rolling out.
- `when-failing` is the default. A new, available revision may replace the one which is currently rolling out if this is failing.
- `when-clear` is the most conservative setting. A new, available revision may never replace one which is currently rolling out.

 Revision targets will never automatically change inside [revision block window](#block-change), but may be set by manual intervention at any time. |
| max-risk | No, default `0` | May only be used with `revision-change="when-clear"` and `revision-target="next"`. The maximum amount of _risk_ to roll out per new revision target. The default of `0` results in the next build always being chosen, while a higher value allows skipping intermediate builds, as long as the cumulative risk does not exceed what is configured here. |
| min-risk | No, default `0` | Must be less than or equal to the configured `max-risk`. The minimum amount of _risk_ to start rolling out a new revision. The default of `0` results in a new revision rolling out as soon as anything is ready, while a higher value lets the system wait until enough cumulative risk is available. This can be used to avoid blocking a lengthy deployment process with trivial changes. |
| max-idle-hours | No, default `8` | May only be used when `min-risk` is specified, and greater than `0`. The maximum number of hours to wait for enough cumulative risk to be available, before rolling out a new revision. |

## test

Meaning depends on where it is located:

| Parent | Description |
| --- | --- |
| `<deployment>` `<instance>` | If present, the application is deployed to the [`test`](../../operations/environments.html#test) environment, and system tested there, even if no prod zones are deployed to. Also, when specified, system tests _must_ be present in the application test package. See guides for [getting to production](../../operations/production-deployment.html).  
 If present in an `<instance>` element, system tests are run for that specific instance before any production deployments of the instance may proceed — otherwise, previous system tests for any instance are acceptable. |
| `<prod>` `<parallel>` `<steps>` | If present, production tests are run against the production region with id contained in this element. A test must be _after_ a corresponding [region](#region) element. When specified, production tests _must_ be preset in the application test package. See guides for [getting to production](../../operations/production-deployment.html). |

| Attribute | Mandatory | Values |
| --- | --- | --- |
| cloud-account | No | For [system tests](../../operations/automated-deployments.html#system-tests) only: account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. Cloud account _must not_ be specified for [production tests](../../operations/automated-deployments.html#production-tests), which always run in the account of the corresponding deployment. |

## staging

In `<deployment>`, or `<instance>`. If present, the application is deployed to the[`staging`](../../operations/environments.html#staging) environment, and tested there, even if no prod zones are deployed to. If present in an `<instance>` element, staging tests are run for that specific instance before any production deployments of the instance may proceed — otherwise, previous staging tests for any instance are acceptable. When specified, staging tests _must_ be preset in the application test package. See guides for [getting to production](../../operations/production-deployment.html).

| Attribute | Mandatory | Values |
| --- | --- | --- |
| cloud-account | No | Account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. |

## prod

In `<deployment>`, **or** in `<instance>`. If present, the application is deployed to the production regions listed inside this element, under the specified instance, after deployments and tests in the `test` and `staging` environments.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| cloud-account | No | Account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. |

## region

In `<prod>`, `<parallel>`, `<steps>`, or `<group>`. The application is deployed to the production[region](../../operations/zones.html) with id contained in this element.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| fraction | No | Only when this region is inside a group: The fractional membership in the group. |
| cloud-account | No | Account to deploy to with [Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. |

## dev

In `<deployment>`. Optionally used to control deployment settings for the [dev environment](../../operations/environments.html). This can be used specify a different cloud account, tags, and private endpoints.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| tags | No | Space-separated tags which can be referenced to make [deployment variants](../../operations/deployment-variants.html). |
| cloud-account | No | Account to deploy to with [Vespa Cloud Enclave](../../operations/enclave/enclave). Overrides parent's use of cloud-account. |

## delay

In `<deployment>`, `<instance>`, `<prod>`, `<parallel>`, or `<steps>`. Introduces a delay which must pass after completion of all previous steps, before subsequent steps may proceed. This may be useful to allow some grace time to discover errors before deploying a change in additional zones, or to gather higher-level metrics for a production deployment for a while, before evaluating these in a production test. The maximum total delay for the whole deployment spec is 48 hours. The delay is specified by any combination of the `hours`, `minutes` and `seconds` attributes.

## parallel

In `<deployment>`, `<prod>`, or `<steps>`. Runs the contained steps in parallel: instances if in `<deployment>`, or primitive steps (deployments, tests or delays) or a series of these (see [steps](#steps)) otherwise. Multiple `<parallel>` elements are permitted. The following example will deploy to `us-west-1` first, then to `us-east-3` and `us-central-1`simultaneously, and, finally to `eu-west-1`, once both parallel deployments have completed:

```
```
<region>us-west-1</region>
<parallel>
    <region>us-east-3</region>
    <region>us-central-1</region>
</parallel>
<region>eu-west-1</region>
```
```

## steps

In `<parallel>`. Runs the contained parallel or primitive steps (deployments, tests or delays) serially. The following example will in parallel:

1. deploy to `us-east-3`,
2. deploy to `us-west-1`, then delay 1 hour, and run tests for `us-west-1`, and
3. delay for two hours.

Thus, the parallel block is complete when both deployments are complete, tests are successful for the second deployment, and at least two hours have passed since the block began executing.

```
```
<parallel>
    <region>us-east-3</region>
    <steps>
        <region>us-west-1</region>
        <delay hours="1" />
        <test>us-west-1</test>
    </steps>
    <delay hours="2" />
</parallel>
```
```

## tester

In `<test>`, `<staging>` and `<prod>`. Specifies container settings for the tester application container, which is used to run system, staging and production verification tests.

The allowed elements inside this are [`<nodes>`](../applications/services/services.html#nodes).

```
```
<staging>
    <tester>
        <nodes count="1">
            <resources vcpu="8" memory="32Gb" disk="30Gb" />
        </nodes>
    </tester>
</staging>
```
```

## endpoints (global)

In `<deployment>`, without any `<instance>`declared **or** in `<instance>`: This allows_global_ endpoints, via one or more [`<endpoint>`](#endpoint-global) elements; and [zone endpoint](#endpoint-zone) and [private endpoint](#endpoint-private)elements for cloud-native private network configuration.

## endpoints (dev)

In `<dev>`. This allows[zone endpoint](#endpoint-zone) elements for cloud-native private network configuration for[dev](../../operations/environments.html#dev) deployments. Note that [private endpoints](#endpoint-private) are only supported in `prod`.

## endpoint (global)

In `<endpoints>` or `<group>`. Specifies a global endpoint for this application. Each endpoint will point to the regions that are declared in the endpoint. If no regions are specified, the endpoint defaults to the regions declared in the `<prod>` element. The following example creates a default endpoint to all regions, and a _us_ endpoint pointing only to US regions.

```
```
<endpoints>
    <endpoint container-id="my-container-service"/>
    <endpoint id="us" container-id="my-container-service">
        <region>aws-us-east-1c</region>
        <region>aws-us-west-2a</region>
    </endpoint>
</endpoints>
```
```

| Attribute | Mandatory | Values |
| --- | --- | --- |
| id | No | The identifier for the endpoint. This will be part of the endpoint name that is generated. If not specified, the endpoint will be the default global endpoint for the application. |
| container-id | Yes | The id of the [container cluster](/en/reference/applications/services/container.html) to which requests to the global endpoint is forwarded. |

Global endpoints are implemented using Route 53 and healthchecks, to keep active zones in rotation. See [BCP](#bcp) for advanced configurations.

## endpoint (zone)

In `<endpoints>` or `<group>`, with `type='zone'`. Used to disable public zone endpoints. _Non-public endpoints can not be used in global endpoints, which require that all constituent endpoints are public._The example disables the public zone endpoint for the `my-container`container cluster in all regions, except where it is explicitly enabled, in `region-1`. Changing endpoint visibility will make the service unavailable for a short period of time.

```
```
<endpoints>
    <endpoint type='zone' container-id='my-container' enabled='false' />
    <endpoint type='zone' container-id='my-container' enabled='true'>
        <region>region-1</region>
    </endpoint>
</endpoints>
```
```

| Attribute | Mandatory | Values |
| --- | --- | --- |
| type | Yes | Private endpoints are specified with `type='zone'`. |
| container-id | Yes | The id of the [container cluster](/en/reference/applications/services/container.html) to disable public endpoints for. |
| enabled | No | Whether a public endpoint for this container cluster should be enabled; default `true`. |

## endpoint (private)

In `<endpoints>` or `<group>`, with `type='private'`. Specifies a private endpoint service for this application. Each service will be launched in the regions that are declared in the endpoint. If no regions are specified, the service is launched in all regions declared in the`<prod>` element, that support any of the declared [access types](#allow). The following example creates a private endpoint in two specific regions.

```
```
<endpoints>
    <endpoint type='private' container-id='my-container'>
        <region>aws-us-east-1c</region>
        <allow with='aws-private-link' arn='arn:aws:iam::123123123123:root' />
    </endpoint>
    <endpoint type='private' container-id='my-container'>
        <region>gcp-us-central1-f</region>
        <allow with='gcp-service-connect' project='user-project' />
    </endpoint>
</endpoints>
```
```

| Attribute | Mandatory | Values |
| --- | --- | --- |
| type | Yes | Private endpoints are specified with `type='private'`. |
| container-id | Yes | The id of the [container cluster](/en/reference/applications/services/container.html) to which requests to the private endpoint service is forwarded. |
| auth-method | No | The authentication method to use with this [private endpoint](/en/operations/private-endpoints.html).   
 Must be either `mtls` or `token`. Defaults to mTLS if not included. |

## allow

In `<endpoint type='private'>`. Allows a principal identified by the URN to set up a connection to the declared private endpoint service. This element must be repeated for each additional URN. An endpoint service will only consider allowed URNs of a compatible type, and will only be created if at least one compatible access type-and-URN is given:

- For AWS deployments, specify `aws-private-link`, and an _ARN_.
- For GCP deployments, specify `gcp-service-connect`, and a _project ID_

```
```
<endpoint type='private' container-id="my-container">
    <allow with='aws-private-link' arn='arn:aws:iam::123123123123:root' />
    <allow with='aws-private-link' arn='arn:aws:iam::321321321321:role/my-role' />
    <allow with='aws-private-link' arn='arn:aws:iam::321321321321:user/my-user' />
    <allow with='gcp-service-connect' project='my-project' />
</endpoint>
```
```

| Attribute | Mandatory | Values |
| --- | --- | --- |
| with | Yes | The private endpoint access type; must be `aws-private-link` or `gcp-service-connect`. |
| arn | Maybe | Must be specified with `aws-private-link`. See [AWS documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html) for more details. |
| project | Maybe | Must be specified with `gcp-service-connect`. See [GCP documentation](https://cloud.google.com/vpc/docs/configure-private-service-connect-services) for more details. |

## bcp

In `<instance>` or `<deployment>`. Defines the BCP (Business Continuity Planning) structure of this instance: Which zones should take over for which others during the outage of a zone and how fast they must have the capacity ready. Autoscaling uses this information to decide the ideal cpu load of a zone. If this element is not defined, it is assumed that all regions covers for an equal share of the traffic of all other regions and must have that capacity ready at all times.

If a bcp element is specified at the root, and explicit instances are used, that bcp element becomes the default for all instances that does not contain a bcp element themselves. If a BCP element contains no group elements it will implicitly define a single group of all the regions of the instance in which it is used.

See [BCP test](https://cloud.vespa.ai/en/reference/bcp-test.html) for a procedure to verify that your BCP configuration is correct.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| deadline | No | 

The max time after a region becomes unreachable until the other regions in its BCP group must be able to handle the traffic of it, given as a number of minutes followed by 'm', 'h' or 'd' (for minutes, hours or days). The default deadline is 0: Regions must at all times have capacity to handle BCP traffic immediately.

By providing a deadline, autoscaling can avoid the cost of provisioning additional resources for BCP capacity if it predicts that it can grow to handle the traffic faster than the deadline in a given cluster.

This is the default deadline to be used for all groups that don't specify one themselves.

 |

Example:

```
```
<bcp>
    <group deadline="15m">
        <endpoint id="foo" container-id="bar"/>
        <region>us-east1</region>
        <region>us-east2</region>
        <region fraction="0.5">us-central1</region>
    </group>
    <group>
        <region>us-west1</region>
        <region>us-west2</region>
        <region fraction="0.5">us-central1</region>
    </group>
</bcp>
```
```

## group

In `<bcp>`. Defines a bcp group: A set of regions whose members cover for each other during a regional outage.

Each region in a group will (as allowed, when autoscaling ranges are configured) provision resources sufficient to handle that any other single region in the group goes down. The traffic of the region is assumed to be rerouted in equal amount to the remaining regions in the group. That is, if a group has one member, no resources will be provisioned to handle an outage in that member. If a group has two members, each will aim to provision sufficient resources to handle the actual traffic of the other. If a group has three members, each will provision to handle half of the traffic observed in the region among the two others which receives the most traffic.

A region may have fractional membership in multiple groups, meaning it will handle just that fraction of the traffic of the remaining members, and vice versa. A regions total membership among groups must always sum to exactly 1.

A group may also define global endpoints for the region members in the group. This is exactly the same as defining the endpoint separately and repeating the regions of the group under the endpoint. Endpoints under a group cannot contain explicit region sub-elements.

| Attribute | Mandatory | Values |
| --- | --- | --- |
| deadline | No | 

The deadline of this BCP group. See deadline on the BCP element.

 |

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [deployment](#deployment)
- [instance](#instance)
- [block-change](#block-change)
- [upgrade](#upgrade)
- [test](#test)
- [staging](#staging)
- [prod](#prod)
- [region](#region)
- [dev](#dev)
- [delay](#delay)
- [parallel](#parallel)
- [steps](#steps)
- [tester](#tester)
- [endpoints (global)](#endpoints-global)
- [endpoints (dev)](#endpoints-dev)
- [endpoint (global)](#endpoint-global)
- [endpoint (zone)](#endpoint-zone)
- [endpoint (private)](#endpoint-private)
- [allow](#allow)
- [bcp](#bcp)
- [group](#group)

