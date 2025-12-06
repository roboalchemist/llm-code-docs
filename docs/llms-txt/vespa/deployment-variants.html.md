# Source: https://docs.vespa.ai/en/operations/deployment-variants.html.md

# Instance, region, cloud and environment variants

 

Sometimes it is useful to create configuration that varies depending on properties of the deployment, for example to set region specific endpoints of services used by [Searchers](/en/applications/searchers.html), or use smaller clusters for a "beta" instance.

This is supported both for [services.xml](#services.xml-variants) and [query profiles](#query-profile-variants).

## services.xml variants

[services.xml](../reference/applications/services/services.html) files support different configuration settings for different _tags_, _instances_, _environments_, _clouds_ and _regions_. To use this, import the _deploy_ namespace:

```
```
<services version="1.0" xmlns:deploy="vespa">
```
```

Deploy directives are used to specify with which tags, and in which instance, environment, cloud and/or [region](https://cloud.vespa.ai/en/reference/zones) an XML element should be included:

```
```
<content version="1.0">
    <min-redundancy>2</min-redundancy>
    <documents>
        <document type="music.sd" mode="index" />
    </documents>
    <nodes deploy:environment="dev"
           count="1" />
    <nodes deploy:environment="prod"
           deploy:region="aws-us-east-1c"
           count="20">
        <resources vcpu="16.0" memory="128Gb" disk="3750Gb"/>
    </nodes>
    <nodes deploy:cloud="gcp" count="10" />
    <nodes deploy:environment="prod"
           deploy:region="aws-us-west-2a"
           count="40">
        <resources vcpu="8.0" memory="64Gb" disk="3750Gb"/>
    </nodes>
    <nodes deploy:environment="prod"
           deploy:region="aws-ap-northeast-1a"
           deploy:instance="alpha"
           count="4">
        <resources vcpu="16.0" memory="256Gb" disk="3750Gb"/>
    </nodes>
    <nodes deploy:tags="myTag1 myTag2" count="8" />
</content>
```
```

The example above configures different node counts/configurations depending on the deployment target. Deploying the application in the _dev_ environment gives:

```
```
<content version="1.0">
    <min-redundancy>2</min-redundancy>
    <documents>
        <document type="music.sd" mode="index" />
    </documents>
    <nodes count="1" />
</content>
```
```

Whereas in `aws-us-west-2a` it is:

```
```
<content version="1.0">
    <min-redundancy>2</min-redundancy>
    <documents>
        <document type="music.sd" mode="index" />
    </documents>
    <nodes count="40">
        <resources vcpu="8.0" memory="64Gb" disk="3750Gb"/>
    </nodes>
</content>
```
```

This can be used to modify any config by deployment target.

The `deploy` directives have a set of override rules:

- A directive specifying more conditions will override one specifying fewer.
- Directives are inherited in child elements.
- When multiple XML elements with the same name is specified (e.g. when specifying search or docproc chains), the _id_ attribute or the _idref_ attribute of the element is used together with the element name when applying directives. 

Some overrides are applied by default in some environments, see [environments](/en/operations/environments.html). Any override made explicitly for an environment will override the defaults for it.

### Specifying multiple targets

More than one tag, instance, region or environment can be specified in the attribute, separated by space.

Note that `tags` by default only apply in production instances, and are matched whenever the tags of the element and the tags of the instance intersect. To match tags in other environments, an explicit `deploy:environment` directive for that environment must also match. Use tags if you have a complex instance structure which you want config to vary by.

The namespace can be applied to any element. Example:

```
```
<container id="default" version="1.0" deploy:environment="test staging prod">
    <search>
        <chain id="default" inherits="vespa">
            <searcher bundle="basic-application" id="vespa.ai.ExampleSearcher">
                <config name="example.message">
                    <message>Hello from application config</message>
                    <message deploy:region="aws-us-east-1c">Hello from east colo!</message>
                </config>
            </searcher>
        </chain>
    </search>
</container>
```
```

Above, the `container` element is configured for the 3 environments only (it will not apply to `dev`) - and in region `aws-us-east-1c`, the config is different.

## Query profile variants

[Query profiles](/en/querying/query-profiles.html) support different configuration settings for different _instances_, _environments_ and _regions_ through [query profile variants](/en/querying/query-profiles.html#query-profile-variants). This allows you to set different query parameters for a query type depending on these deployment attributes.

To use this feature, create a regular query profile variant with any of `instance`, `environment` and `region` as dimension names and let your query profile vary by that. For example:

```
```
<query-profile id="default">

    <dimensions>instance, environment, region</dimensions>

    <field name="a">My default value</field>

    <!-- Value for (any deployment of) the beta instance -->
    <query-profile for="beta">
        <field name="a">My beta value</field>
    </query-profile>

    <!-- Value for (any) dev deployment -->
    <query-profile for="*, dev">
        <field name="a">My dev value</field>
    </query-profile>

    <!-- Value for the default instance in prod -->
    <query-profile for="default, prod">
        <field name="a">My main instance prod value</field>
    </query-profile>

</query-profile>
```
```

You can pick and combine these dimensions in any way you want with other dimensions sent as query parameters, e.g:

```
```
<dimensions>device, instance, usecase</dimensions>
```
```

 Copyright © 2025 - [Cookie Preferences](#)

