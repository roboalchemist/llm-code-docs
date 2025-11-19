# Source: https://docs.apify.com/platform/actors/development/builds-and-runs/builds.md

# Builds

**Learn about Actor build numbers, versioning, and how to use specific Actor version in runs. Understand an Actor's lifecycle and manage its cache.**

***

## Understand Actor builds

Before an Actor can be run, it needs to be built. The build process creates a snapshot of a specific version of the Actor's settings, including its https://docs.apify.com/platform/actors/development/actor-definition/source-code.md and https://docs.apify.com/platform/actors/development/programming-interface/environment-variables.md. This snapshot is then used to create a Docker image containing everything the Actor needs for its run, such as `npm` packages, web browsers, etc.

### Build numbers

Each build is assigned a unique build number in the format *MAJOR.MINOR.BUILD* (e.g. *1.2.345*):

* *MAJOR.MINOR* corresponds to the Actor version number
* *BUILD* is an automatically incremented number starting at **1**.

### Build resources

By default, builds have the following resource allocations:

* Timeout: *1800* seconds
* Memory: `4096 MB`

Check out the https://docs.apify.com/platform/actors/running.md section for more details.

## Versioning

To support active development, Actors can have multiple versions of source code and associated settings, such as the base image and environment. Each version is denoted by a version number of the form *MAJOR.MINOR*, following https://semver.org/ principles.

For example, an Actor might have:

* Production version *1.1*
* Beta version *1.2* that contains new features but is still backward compatible
* Development version *2.0* that contains breaking changes.

## Tags

Tags simplify the process of specifying which build to use when running an Actor. Instead of using a version number, you can use a tag such as *latest* or *beta*. Tags are unique, meaning only one build can be associated with a specific tag.

To set a tag for builds of a specific Actor version:

1. Set the `Build tag` property.
2. When a new build of that version is successfully finished, it's automatically assigned the tag.

By default, the builds are set to the *latest* tag.

## Cache

To speed up builds triggered via API, you can use the `useCache=1` parameter. This instructs the build process to use cached Docker images and layers instead of pulling the latest copies and building each layer from scratch. Note that the cached images and layers might not always be available on the server building the image, the `useCache` parameter only functions on a best-effort basis.

Clean builds

Running builds from the Console By default, the Console uses cached data when starting a build. You can also run a clean build without using the cache. To run a clean build:

1. Go to your Actor page.
2. Select **Source** > **Code**.
3. Locate the **Start** button. Next to it, click on the arrow & choose **Clean build**
