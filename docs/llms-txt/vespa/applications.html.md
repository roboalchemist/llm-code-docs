# Source: https://docs.vespa.ai/en/basics/applications.html.md

# Vespa applications

 

You use Vespa by deploying an _application_ to it. Why applications? Because Vespa handles both data and the computations you do over them - together an application.

An application is specified by an _application package_ - a directory with some files. The application package contains _everything_ that is needed to run your application: Config, schemas, components, ML models, and so on.

The _only_ way to change an application is to make the change in the application package and then deploy it again. Vespa will then safely change the running system to match the new application package revision, without impacting queries, writes, or data.

## A minimal application package

You can create a complete application package with just a single file: services.xml. This file specifies the clusters that your application should run. It could just be a single stateless cluster - what's called _container_ - like this:

```
```
<services version="1.0">
    <container version="1.0" id="default">
        <nodes count="2">
            <resources vcpu="4" memory="16Gb" disk="50Gb"/>
        </nodes>
    </container>
</services>
```
```

Put this in a file called services.xml, and you have created the world's smallest application package. However, this won't do much, usually you want to have a `content` cluster which can store data, maintain indexes, and run the distributed part of queries. You'll also want your container cluster to load the necessary middleware for this. With that we get a services file like this:

```
```
<services version="1.0">
    <container version="1.0" id="queryfeedendpoint">
        <search/>
        <document-api/>
        <nodes count="2">
            <resources vcpu="4" memory="16Gb" disk="50Gb"/>
        </nodes>
    </container>
    <content id="mydocs" version="1.0">
        <min-redundancy>2</min-redundancy>
        <nodes count="2">
            <resources vcpu="8" memory="64Gb" disk="200Gb"/>
        </nodes>
        <documents>
            <document type="myschema" mode="index"/>
        </documents>
    </content>
</services>
```
```

This specifies a pretty normal simple Vespa application, but now we need another file: The schema of the document type we'll use. This goes into the directory `schemas/`, so our application package now looks like this:

```
services.xml
schemas/myschema.sd
```

The schema file describes a kind of data and the computations (such as ranking/scoring) you want to do over it. At minimum it just lists the fields of that data type and if and each field should be indexed:

```
schema myschema {

    document myschema {

        field text type string {
            indexing: summary | index
        }

        field embedding type tensor<bfloat16>(x[384]) {
            indexing: attribute | index
        }

        field popularity type double {
            indexing: summary | attribute
        }

    }

}
```

With these two files we have specified a fully functional application that can do text, vector and hybrid search with filtering.

Rather than creating applications from scratch like this, you can also clone one of our sample applications as a starting point like we did in [getting started](deploy-an-application.html).

To read more on schemas, see the [schemas](schemas.html) guide. To see everything an application package can contain, see the[application package reference](../reference/applications/application-packages.html).

## Deploying applications

To create running instances of an application, or make the changes to one take effect, you _deploy_ it. Deployments to the dev zone and to self-managed clusters sets up a single instance, while deployments to production can set up multiple instances in one or more regions.

To deploy an application package you use the [deploy command](../clients/vespa-cli.html#deployment) in Vespa CLI:

```
```
$ vespa deploy .
```
```

This will deploy the application package at the current dir to the current target and the default dev zone (use `vespa deploy -h` to see other options).

Deployment to production zones use a separate command:

```
```
$ vespa prod deploy .
```
```

Production deployments also require an additional file in the application package to specify where it should be deployed: deployment.xml. See [production deployment](../operations/production-deployment.html). The recommended way to deploy to production is by setting up a continuous deployment job, see[automated deployments](../operations/automated-deployments.html).

Deploying a change to an application package is generally safe to do at any time. It does not disrupt queries and writes, and invalid or destructive changes are rejected before taking effect. You can also add tests that verifies the application before deployment to production zones.

  

#### Next: [Schemas](schemas.html)

 Copyright © 2025 - [Cookie Preferences](#)

