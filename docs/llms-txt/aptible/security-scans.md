# Source: https://www.aptible.com/docs/core-concepts/security-compliance/security-scans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Scans

> Learn about application vulnerability scanning provided by Aptible

Aptible can scan the packages in your Docker images for known vulnerabilities [Clair](https://github.com/coreos/clair) on demand.

# What is scanned?

Docker image security scans look for vulnerable OS packages installed in your Docker images on supported Linux distributions:

* **Debian / Ubuntu**: packages installed using `dpkg` or its `apt-get` frontend.
* **CentOS / Red Hat / Amazon Linux**: packages installed using `rpm` or its frontends `yum` and `dnf`.
* **Alpine Linux**: packages installed using `apk`.

Docker image security scans do **not** scan for:

* packages installed from source (e.g., using `make && make install`).
* packages installed by language-level package managers, such as `bundler`, `npm`, `pip`, `yarn`, `composer`, `go install`, etc. (third-party vulnerability analysis providers support those, and you can incorporate them using a CI process, for example).

# FAQ

<AccordionGroup>
  <Accordion title="How do I access security scans?">
    Access Docker image security scans in the Aptible Dashboard by navigating to the respective app and selecting "Security Scan."
    <img src="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=068dd69243844b3ba9fa5eedf336bb84" alt="" data-og-width="1000" width="1000" data-og-height="500" height="500" data-path="images/Security-Scans.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=280&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=b355dd37c100e3e992ddb1973b3af6bb 280w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=560&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=716d204dc972ad6d886fdca6d961ccd7 560w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=840&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=5c855d982d5c9c7072656d91294f4d3e 840w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=1100&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=34029ff452235228821e40720add236c 1100w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=1650&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=4ce6aac80b9345dff5be2c4f5a237579 1650w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/Security-Scans.png?w=2500&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=b4ac80a6bb805cf6463e58ad9fc4a819 2500w" />
  </Accordion>

  <Accordion title="What OSes are supported?">
    **Ubuntu, Debian, RHEL, Oracle, Alpine, and AWS Linux** are currently supported.

    Some operating systems, like CentOS, are not supported because the OS maintainers do not publish any kind of security database of package vulnerabilities.
    You will see an error message like "No OS detected by Clair" if this is the case.
  </Accordion>

  <Accordion title="What does it mean if my scan returns no vulnerabilities?">
    In the best case, this means that Aptible was able to identify packages installed in your container, and none of those packages have any "known" vulnerabilities.

    In the worst case, Aptible is unable to correlate any vulnerabilities to packages in your container.

    Vulnerability detection relies on your OS maintainers to publicly publish vulnerability information and keep it up to date.
    The most common reason for there being no vulnerabilities detected is if you're using an unsupported (e.g., End of Life) OS version, like Debian 9 or older, for which there is no longer any publicly maintained vulnerability database.
  </Accordion>

  <Accordion title="How do I handle the vulnerabilities found in security scans?">
    ## Read the guide

    <Card title="How to handle vulnerabilities found in security scans" icon="book-open-reader" href="https://www.aptible.com/docs/how-to-handle-vulnerabilities-found-in-security-scans" />
  </Accordion>
</AccordionGroup>
