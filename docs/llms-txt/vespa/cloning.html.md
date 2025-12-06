# Source: https://docs.vespa.ai/en/operations/cloning.html.md

# Cloning applications and data

 

This is a guide on how to replicate a Vespa application in different environments, with or without data. Use cases for cloning include:

- Get a copy of the application and (some) data on a laptop to work offline, or attach a debugger.
- Deploy local experiments to the `dev` environment to easily cooperate and share.
- Set up a copy of the application and (some) data to test a new major version of Vespa.
- Replicate a bug report in a non-production environment.
- Set up a copy of the application and (some) data in a `prod` environment to experiment with a CI/CD pipeline, without touching the current production serving.
- Onboard a new team member by setting up a copy of the application and test data in a `dev` environment.
- Clone to a `dev` environment for load testing.

This guide uses _applications_. One can also use _instances_, but that will not work across Vespa major versions on Vespa Cloud - refer to [tenant, applications, instances](../learn/tenant-apps-instances) for details.

Vespa Cloud has different environments `dev` and `prod`, with different characteristics -[details](environments.html). Clone to `dev` for short-lived experiments/development/benchmarking, use `prod` for serving applications with a [CI/CD pipeline](automated-deployments.html).

As some steps are similar, it is a good idea to read through all, as details are added only the first time for brevity. Examples are based on the[album-recommendation](https://github.com/vespa-engine/sample-apps/tree/master/album-recommendation) sample application.

 **Note:** When done, it is easy to tear down resources in Vespa Cloud. E.g., _https://console.vespa-cloud.com/tenant/mytenant/application/myapp/prod/deploy_ or_https://console.vespa-cloud.com/tenant/mytenant/application/myapp/dev/instance/default_ to find a delete-link. Instances in `dev` environments are auto-expired ([details](environments.html)), so application cloning is a safe way to work with Vespa. Find more information in [deleting applications](deleting-applications).

## Cloning - self-hosted to Vespa Cloud

**Source setup:**

```
$ docker run --detach --name vespa1 --hostname vespa-container1 \
  --publish 8080:8080 --publish 19071:19071 \
  vespaengine/vespa

$ vespa deploy -t http://localhost:19071
```

**Target setup:**

[Create a tenant](../basics/deploy-an-application.html) in the Vespa Cloud console, in this guide using "mytenant".

**Export source application package:**

This gets the application package and copies it out of the container to local file system:

```
$ vespa fetch -t http://localhost:19071 && \
  unzip application.zip -x application.zip
```

**Deploy target application package**

The procedure differs a little whether deploying to dev or prod [environment](environments.html). The `mvn -U clean package` step is only needed for applications with custom code. Configure application name and create data plane credentials:

```
$ vespa config set target cloud && \
  vespa config set application mytenant.myapp

$ vespa auth login

$ vespa auth cert -f

$ mvn -U clean package
```

 **Note:** When deploying to a new app, one will often want to generate a new data plane cert/key pair. To do this, use `vespa auth cert -f`. If reusing a cert/key pair, drop `-f` and make sure to put the pair in _.vespa_, to avoid errors like`Error: open /Users/me/.vespa/mytenant.myapp.default/data-plane-public-cert.pem: no such file or directory`in the subsequent deploy step.

Then deploy the application. Depending on the use case, deploy to `dev` or `prod`:

- `dev`:
```
$ vespa deploy
```
 Expect something like:
```
Uploading application package ... done

Success: Triggered deployment of . with run ID 1

Use vespa status for deployment status, or follow this deployment at
https://console.vespa-cloud.com/tenant/mytenant/application/myapp/dev/instance/default/job/dev-aws-us-east-1c/run/1
```
- Deployments to the `prod` environment requires [deployment.xml](/en/reference/applications/deployment.html) - select which [zone](https://cloud.vespa.ai/en/reference/zones) to deploy to:
```
$ cat <<EOF > deployment.xml
<deployment version="1.0">
    <prod>
        <region>aws-us-east-1c</region>
    </prod>
</deployment>
EOF
```
`prod` deployments also require `resources` specifications in [services.xml](https://cloud.vespa.ai/en/reference/services) - use [vespa-documentation-search](https://github.com/vespa-cloud/vespa-documentation-search/blob/main/src/main/application/services.xml) as an example and add/replace `nodes` elements for `container` and `content` clusters. If in doubt, just add a small config to start with, and change later:
```
<nodes count="2">
    <resources vcpu="2" memory="8Gb" disk="10Gb" />
</nodes>
```
 Deploy the application package:
```
$ vespa prod deploy
```
 Expect something like:
```
Hint: See[production deployment](production-deployment.html)Success: Deployed .
See https://console.vespa-cloud.com/tenant/mytenant/application/myapp/prod/deployment for deployment progress
```
 A proper deployment to a `prod` zone should have automated tests, read more in [automated deployments](automated-deployments.html)

**Data copy**

Export documents from the local instance and feed to the Vespa Cloud instance:

```
$ vespa visit -t http://localhost:8080 | vespa feed -
```

Add more parameters as needed to `vespa feed` for other endpoints.

**Get access log from source:**

```
$ docker exec vespa1 cat /opt/vespa/logs/vespa/access/JsonAccessLog.default
```

## Cloning - Vespa Cloud to self-hosted

**Download application from Vespa Cloud**

Validate the endpoint, and fetch the application package:

```
$ vespa config get application
application = mytenant.myapp.default

$ vespa fetch
Downloading application package... done
Success: Application package written to application.zip
```

The application package can also be downloaded from the Vespa Cloud Console:

- dev: Navigate to _https://console.vespa-cloud.com/tenant/mytenant/application/myapp/dev/instance/default_, click _Application_ to download: 

- prod: Navigate to _https://console.vespa-cloud.com/tenant/mytenant1/application/myapp/prod/deployment?tab=builds_ and select the version of the application to download: 

**Target setup:**

Note the name of the application package .zip-file just downloaded. If changes are needed, unzip it and use `vespa deploy -t http://localhost:19071 `to deploy from current directory:

```
$ docker run --detach --name vespa1 --hostname vespa-container1 \
  --publish 8080:8080 --publish 19071:19071 \
  vespaengine/vespa

$ vespa config set target local

$ vespa deploy -t http://localhost:19071 mytenant.myapp.default.dev.aws-us-east-1c.zip
```

**Data copy**

Set config target cloud for `vespa visit` and pipe the jsonl output into `vespa feed` to the local instance:

```
$ vespa config set target cloud

$ vespa visit | vespa feed - -t http://localhost:8080
```

**data copy - minimal**

For use cases requiring a few documents, visit just a few documents:

```
$ vespa visit --chunk-count 10
```

**Get access log from source:**

Use the Vespa Cloud Console to get access logs

## Cloning - Vespa Cloud to Vespa Cloud

This is a combination of the procedures above. Download the application package from dev or prod, make note of the source name, like mytenant.myapp.default. Then use `vespa deploy` or `vespa prod deploy` as above to deploy to dev or prod.

If cloning from `dev` to `prod`, pay attention to changes in _deployment.xml_ and _services.xml_as in [cloning to Vespa Cloud](#cloning---self-hosted-to-vespa-cloud).

**Data copy**

Set the feed endpoint name / paths, e.g. mytenant.myapp-new.default:

```
$ vespa config set target cloud

$ vespa visit | vespa feed - -t https://default.myapp-new.mytenant.aws-us-east-1c.dev.z.vespa-app.cloud
```

**Data copy 5%**Set the –selection argument to `vespa visit` to select a subset of the documents.

## Cloning - self-hosted to self-hosted

Creating a copy from one self-hosted application to another. Self-hosted means running [Vespa](https://vespa.ai/) on a laptop or a [multinode system](self-managed/multinode-systems.html).

This example sets up a source app and deploys the [application package](../basics/applications.html) - use [album-recommendation](https://github.com/vespa-engine/sample-apps/tree/master/album-recommendation)as an example. The application package is then exported from the source and deployed to a new target app. Steps:

**Source setup:**

```
$ vespa config set target local

$ docker run --detach --name vespa1 --hostname vespa-container1 \
  --publish 8080:8080 --publish 19071:19071 \
  vespaengine/vespa

$ vespa deploy -t http://localhost:19071
```

**Target setup:**

```
$ docker run --detach --name vespa2 --hostname vespa-container2 \
  --publish 8081:8080 --publish 19072:19071 \
  vespaengine/vespa
```

**Export source application package**

Export files:

```
$ vespa fetch -t http://localhost:19071
```

**Deploy application package to target**

Before deploying, one can make changes to the application package files as needed. Deploy to target:

```
$ vespa deploy -t http://localhost:19072 application.zip
```

**Data copy from source to target**

This pipes the source data directly into `vespa feed` - another option is to save the data to files temporarily and feed these individually:

```
$ vespa visit -t http://localhost:8080 | vespa feed - -t http://localhost:8081
```

**Data copy 5%**

This is an example on how to use a [selection](../reference/writing/document-selector-language.html)to specify a subset of the documents - here a "random" 5% selection:

```
$ vespa visit -t http://localhost:8080 --selection 'id.hash().abs() % 20 = 0' | \
  vespa feed - -t http://localhost:8081
```

**Get access log from source**

Get the current query access log from the source application (there might be more files there):

```
$ docker exec vespa1 cat /opt/vespa/logs/vespa/access/JsonAccessLog.default
```

 Copyright © 2025 - [Cookie Preferences](#)

