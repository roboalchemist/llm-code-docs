# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/path-traversal-file-read.md

---
title: Potential path traversal from request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Potential path traversal from request
---

# Potential path traversal from request

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/path-traversal-file-read`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

The filename of the file being opened comes from an input parameter. If an unfiltered parameter is passed to the API, any location on the filesystem can be read.

#### Learn More{% #learn-more %}

- [Potential File Traversal](https://find-sec-bugs.github.io/bugs.htm#PATH_TRAVERSAL_IN)
- [CWE-22 - Improper Limitation of a Pathname to a Restricted Directory](https://cwe.mitre.org/data/definitions/22.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    @GET
    @Path("/images/{image}")
    @Produces("images/*")
    public Response getImage(@javax.ws.rs.PathParam("image") String image) {
        File file = new File("resources/images/", image); //Weak point

        if (!file.exists()) {
            return Response.status(Status.NOT_FOUND).build();
        }

        return Response.ok().entity(new FileInputStream(file)).build();
    }

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import org.apache.commons.io.FilenameUtils;

class MyClass {

    @GET
    @Path("/images/{image}")
    @Produces("images/*")
    public Response getImage(@javax.ws.rs.PathParam("image") String image) {
        File file = new File("resources/images/", FilenameUtils.getName(image)); //Fix

        if (!file.exists()) {
            return Response.status(Status.NOT_FOUND).build();
        }

        return Response.ok().entity(new FileInputStream(file)).build();
    }

    @GET
    @Path("/images/{image}")
    @Produces("images/*")
    public Response getImage(@javax.ws.rs.PathParam("image") String image) {
        File file = new File("resources/images/", image2); //Weak point

        if (!file.exists()) {
            return Response.status(Status.NOT_FOUND).build();
        }

        return Response.ok().entity(new FileInputStream(file)).build();
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
