# Source: https://docs.debricked.com/product/exporting-sbom/sbom-export/spdx-sbom-export.md

# SPDX SBOM export

{% hint style="info" %}
*This feature is only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)
{% endhint %}

### **What is SPDX?** <a href="#whatiscyclonedx" id="whatiscyclonedx"></a>

SPDX is an open standard for communicating software bill of material information, including provenance, license, security, and other related information. SPDX reduces redundant work by providing common formats for organizations and communities to share important data, thereby streamlining and improving compliance, security, and dependability.

{% hint style="info" %}
*Unlike the CycloneDX SBOM, the SPDX SBOM does not contain vulnerability information.*
{% endhint %}

#### Dependency relations <a href="#dependencyrelations" id="dependencyrelations"></a>

The relationships between components are presented in the relationships array. OpenText Core SCA SPDX SBOMs support following two types of relationship objects:

* DESCRIBES which is used for declaring each file and dependency component in the BOM.
* DEPENDENCY\_OF which denotes a direct relationship between two components.&#x20;

In the objects describing the direct dependencies of a file, the 'relatedSpdxElement' will contain the reference of that file. Relationships between dependencies will instead reference the parent dependency. By traversing the dependencies array, it is possible to build the entire dependency tree.

In the example below, you can see direct dependency *\`webpack-4.28.4\`* referenced as a dependency of a file. Component *\`terser-webpack-plugin-1.2.1\`* is in turn referenced as a dependency of *\`webpack-4.28.4\`* and lastly, *\`terser-3.14.1\`* is a dependency of *\`terser-webpack-plugin-1.2.1\`.*

```
"relationships": [
    {
        "spdxElementId": "SPDXRef-DOCUMENT",
        "relatedSpdxElement": "SPDXRef-bda845e38ee2becb214eaa4c995d4951d755faceb38a4ef6e7092699592d7efe",
        "relationshipType": "DESCRIBES"
    },
    {
        "spdxElementId": "SPDXRef-DOCUMENT",
        "relatedSpdxElement": "SPDXRef-pkg-npm-terser-3.14.1",
        "relationshipType": "DESCRIBES"
    },
    {
        "spdxElementId": "SPDXRef-DOCUMENT",
        "relatedSpdxElement": "SPDXRef-pkg-npm-terser-webpack-plugin-1.2.1",
        "relationshipType": "DESCRIBES"
    },
    {
        "spdxElementId": "SPDXRef-DOCUMENT",
        "relatedSpdxElement": "SPDXRef-pkg-npm-webpack-4.28.4",
        "relationshipType": "DESCRIBES"
    },
    {
        "spdxElementId": "SPDXRef-pkg-npm-terser-3.14.1",
        "relatedSpdxElement": "SPDXRef-pkg-npm-terser-webpack-plugin-1.2.1",
        "relationshipType": "DEPENDENCY_OF"
    },
    {
        "spdxElementId": "SPDXRef-pkg-npm-terser-webpack-plugin-1.2.1",
        "relatedSpdxElement": "SPDXRef-pkg-npm-webpack-4.28.4",
        "relationshipType": "DEPENDENCY_OF"
    },
    {
        "spdxElementId": "SPDXRef-pkg-npm-webpack-4.28.4",
        "relatedSpdxElement": "SPDXRef-bda845e38ee2becb214eaa4c995d4951d755faceb38a4ef6e7092699592d7efe",
        "relationshipType": "DEPENDENCY_OF"
    }
],
```

Here is how this would be visualised in the user interface:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FqrDvvGjgAf7Whbsy5hKm%2Fimage.png?alt=media&#x26;token=f0855415-c621-4d67-bf11-eb420de6deca" alt=""><figcaption></figcaption></figure>
