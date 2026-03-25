# Source: https://help.cloudsmith.io/docs/migration-to-cloudsmith.md

# Migrating to Cloudsmith

This help doc will walk you through the steps involved in migrating packages, artifacts, binaries, images, or zip files into Cloudsmith. If you have any trouble migrating, contact us, and we will be happy to assist in the process.

Migrating from another package repository requires the following:

* Export the packages from your old repositories like JFrog's Artifactory or Sonatype Nexus.
* Importing to Cloudsmith
* Optional setup requirements

## Exporting from another repository

If you have been running another repository manager, such as Artifactory, Nexus, MyGet or ProGet and you want to migrate your package hosted on this repository to Cloudsmith, the first step is exporting the packages out of your old repository.

Depending on your package repository and/or package format, you will have to use different approaches to exporting your packages. We have the following documentation on how to:

* [Export any package from JFrog Artifactory](https://help.cloudsmith.io/docs/export-from-jfrog-artifactory)
* [Export from Nexus Sonatype](https://help.cloudsmith.io/docs/export-from-nexus-sonatype)
* [Export NuGet packages from any package repository](https://help.cloudsmith.io/docs/exporting-nuget)

> 📘
>
> Export details not here? Contact us and we'll help!

## Import into Cloudsmith

After the export, you can import the packages into your new Cloudsmith repository - Yay!\
We will assume you have exported all your packages/artifacts/binaries into a folder or a shared location (e.g. S3 bucket).

Importing your packages into Cloudsmith should be a stress-free process; you will need to:

* Create an [organization](https://help.cloudsmith.io/docs/organisations) and at least one [repository](https://help.cloudsmith.io/docs/manage-a-repository) on your Cloudsmith account. [it should only take 60 seconds](https://www.youtube.com/watch?v=Rqlc5o0r3cg\&ab_channel=Cloudsmith)
* Install the [Cloudsmith CLI](https://help.cloudsmith.io/docs/cli) and export your API token.
* Do a bulk import of your packages per package format using the Cloudsmith CLI. For a build import from a folder, follow the instructions [here](https://help.cloudsmith.io/docs/import-files-from-a-folder).
* We have specific instructions for certain package types:
  * [Import Maven](https://help.cloudsmith.io/docs/import-maven)
  * [Import npm](https://help.cloudsmith.io/docs/import-npm)
  * [Import NuGet](https://help.cloudsmith.io/docs/import-nuget)
  * [Import Docker](https://help.cloudsmith.io/docs/import-docker)
  * [Import Python](https://help.cloudsmith.io/docs/import-python)

> 📘
>
> Import details not here? Contact us and we'll help!

## Other settings to consider

If you are migrating packages and setting up Cloudsmith for the first time, you may need to consider other tasks when getting started, including:

* Update your build tools and configurations to push/pull to the new Cloudsmith endpoints. You may have a configuration file for every package format in your code base, you will find information on how to set up Cloudsmith for each format [here](https://help.cloudsmith.io/docs/supported-formats).
* Setup your [Single Sign-On](https://help.cloudsmith.io/docs/single-sign-on) and [Group Mapping](https://help.cloudsmith.io/docs/single-sign-on#saml-group-sync) instructions if this is your preferred way to log in to your users.
* Setup your [upstreams](https://help.cloudsmith.io/docs/upstream-proxying-caching), which will set up Cloudsmith to fetch and cache your 3rd party dependencies hosted on public repositories like NuGet Gallery, RubyGems.org or Maven Central.
* Setup [signing keys](https://help.cloudsmith.io/docs/signing-keys).
* Setup your [service accounts](https://help.cloudsmith.io/docs/service-accounts).
* Setup your [logs export to s3](https://help.cloudsmith.io/docs/access-log-exports-to-s3).
* If you are a distributor, you may want to set up [Entitlement tokens](https://help.cloudsmith.io/docs/entitlements) to distribute to 3rd parties
* Setup [Custom Domains](https://help.cloudsmith.io/docs/custom-domains), which allow you to present your brand and domain when distributing from Cloudsmith.