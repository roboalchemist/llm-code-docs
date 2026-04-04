# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/handle-vulnerabilities-security-scans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to handle vulnerabilities found in security scans

[Security Scans](/core-concepts/security-compliance/security-scans) look for vulnerable OS packages installed in your Docker images by your Operating System’s package manager, so the solutions suggested below highlight the various ways you can manipulate these packages to mitigate the vulnerabilities.

## Mitigate by updating packages

## Rebuild your image

Since any found vulnerabilities were installed by the OS Package manager, we recommend first that you try the simplest approach possible and update all the packages in your Image. Rebuilding your image will often solve any vulnerabilities marked “Fix available”, as these are vulnerabilities for which the scanner has identified a newer version this package is available which remediates this vulnerability.

If you deploying via Git, you can use the command `aptible rebuild` to rebuild and deploy the new image:

```sql  theme={null}
aptible rebuild --app $HANDLE
```

If you are deploying via Docker Image, you will need to follow your established process to build, publish, and deploy the new image.

## Packages included in your parent image

The broadest thing you can try, assuming it does not introduce any compatibility issues for your application, is to update the parent image of your App: this is the one specified as the first line in your Dockerfile, for example:

```sql  theme={null}
FROM debian:8.2
```

Debian version 8.2 is no longer the latest revision of Debian 8, and may not have a specific newer package version available. You could update to `FROM debian:8.11` to get the latest version of this image, which may have upgraded packages in it, but by the time you read this FAQ there will be a newer still version available. So, you should prefer to use `FROM debian:8`, which is maintained to always be the latest Debian 8 image, as documented on the Docker Hub. This version tagging pattern is common on many images, so check the documentation of your parent image in order to choose the appropriate tag.

Finally, the vulnerability details might indicate a newer OS, eg Debian 10, includes a version with the vulnerability remediated. This change may be more impactful than those suggested above, given the types of changes that may occur between major versions of an operating system.

## Packages explicitly installed in your Dockerfile

You might also find that you have pinned a specific version of a package in your Dockerfile, either for compatibility or to prevent a regression of another vulnerability. For example:

```ruby  theme={null}
FROM debian: 8

RUN apt - get update &&\
apt - get - y install exim4 = 4.84.2 - 2 + deb8u5 exim4 - base=4.84.2 - 2 + deb8u5 &&\
rm - rf /var/lib/apt / lists/*
```

There exists a vulnerability (CVE-2020-1283) that is fixed in the newer `4.84.2-2+deb8u7` release of `exim4` . So, you would either want to test the newer version and specify it explicitly in your Dockerfile, or simply remove the explicit request for a particular version to be sure that exim4 is always kept up to date.

## Packages implicitly installed in your Dockerfile

Some packages will appear in the vulnerability scan that you don’t immediately recognize a reason they are installed. It is possible those are installed as a dependency of another package, and most package managers include tools for looking up reverse dependencies which you can use to determine which package(s) require the vulnerable package. For example, on Debian, you can use `apt-cache rdepends --installed $PACKAGE` .

## Mitigate by Removing Packages

If the scan lists a vulnerability in a package you do not require, you can simply remove it.

First, we suggest, as a best practice, to identify any packages that you have installed as a build-time dependency and remove them at the end of your Dockerfile when building is complete.

In your Dockerfile, you can track which packages are installed as a build dependency and simply uninstall them when you have completed that task:

```ruby  theme={null}
FROM debian:8

# Declare your build-time dependencies
ENV DEPS "make build-essential python-pip python-dev"

# Install them
RUN apt-get update &&\
    apt-get -y install ${DEPS}= &&\
    rm -rf /var/lib/apt/lists/*

# Build your application
RUN make build

# Remove the build dependencies now that you no longer need them
RUN apt-get -y --autoremove ${DEPS}
```

The above would potentially mitigate a vulnerability identified in `libmpc3`, which you only need as a dependency of `build-essential`. You would still need to determine if the vulnerability discovered affected your app through the use of `libmpc3`, even if you have later uninstalled it.

Finally, many parent images will include many unnecessary packages by default. Try the `-slim` tag to get an image with less software installed by default, for example, `python:3` contains a large number of packages that `python:3-slim` does not. Not all images have this option, and you will likely have to add specific dependencies back in your Dockerfile to keep your App working, but this can greatly reduce the surface area for vulnerability by reducing the number of installed packages.

## What next?

If there are no fixes available, and you can’t remove the package, you will need to analyze the vulnerability itself.

Does the package you have installed actually include the vulnerability? If the CVE information lists “not-affected” or “DNE” for your specific OS, there is likely no issue. For example, Ubuntu back ports security fixes in OpenSSL yet maintains a 1.0.x version number. This means a vulnerability that says it affects “OpenSSL versions before 1.1.0” does not automatically mean the `1.0.2g-1ubuntu4.6` version you likely have installed is actually vulnerable.

Does the vulnerability actually impact your use of the package? The vulnerability may be present in a function you do not use or in a service, your image is not actually running.

Is the vulnerability otherwise mitigated by your security posture? Many vulnerabilities can be remediated with simple steps like sanitizing input to your application or by not running or exposing unnecessary services.

If you’ve reached this point and the scanner has helped you identify a real vulnerability in your application, it’s time to decide on another mitigation strategy!
