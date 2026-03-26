# Source: https://docs.debricked.com/product/exporting-sbom/sbom-export/cyclonedx-sbom-export.md

# CycloneDX SBOM export

{% hint style="info" %}
*This feature is only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)
{% endhint %}

### **What is CycloneDX?** <a href="#whatiscyclonedx" id="whatiscyclonedx"></a>

CycloneDX, developed by the Open Web Application Security Project (OWASP), is an open common standard for communicating SBOM information, a data format.

#### Dependency relations <a href="#dependencyrelations" id="dependencyrelations"></a>

In the dependencies array, you can find a reference number (ref) for each component and an array of each direct dependency of that dependency (depends\_on). The roots of the relational trees will reference to the files in the project, together with the direct dependencies that it contains. By traversing the dependencies array, it is possible to build the entire dependency tree.

In example below, you can see the direct dependency *\`webpack:4.28.4\`* depending on *\`terser-webpack-plugin:1.2.1\`* which in turn depends on *\`terser:3.14.1\`.*

```

    "dependencies": [
    {
        "ref": "e771afadf654cc12c324a0dd716518dd",
        "depends_on": ["cpe:2.3::~:webpack:4.28.4:~:~:~:~:~:~:~"]
    },
    {
        "ref": "cpe:2.3::~:webpack:4.28.4:~:~:~:~:~:~:~",
        "depends_on": ["cpe:2.3::~:terser-webpack-plugin:1.2.1:~:~:~:~:~:~:~"]
    },
    {
        "ref": "cpe:2.3::~:terser-webpack-plugin:1.2.1:~:~:~:~:~:~:~",
        "depends_on": ["cpe:2.3::~:terser:3.14.1:~:~:~:~:~:~:~"]
    },
    {
        "ref": "cpe:2.3::~:terser:3.14.1:~:~:~:~:~:~:~",
        "depends_on": []
    }
    ]
```

Here is how this would be visualised in the user interface:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FqrDvvGjgAf7Whbsy5hKm%2Fimage.png?alt=media&#x26;token=f0855415-c621-4d67-bf11-eb420de6deca" alt=""><figcaption></figcaption></figure>

#### Root fixes <a href="#rootfixes" id="rootfixes"></a>

Under **Recommendation,** you can find information about the first version of the specific vulnerable dependency that is safe, as well as the first version of the root or direct dependency that does not contain a vulnerable version of the indirect dependency. See example below:

```
"recommendation": "Multiple components are affected by this vulnerability.
Component: pkg:npm/async@3.2.0
Safe version: 3.2.2.
Root fixes: Update root dependency pkg:npm/htmlhint@0.14.2 to 0.16.2.
---------
Component: pkg:npm/async@2.6.0
Safe version: 2.6.4.
Root fixes: Update root dependency pkg:npm/gelf-pro@1.2.2 to 1.3.4.",
      "created": "2022-04-06T17:15:00+00:00",
      "published": "2022-04-06T17:15:00+00:00",
      "updated": "2022-04-06T17:15:00+00:00",
      "affects": [
        {
          "ref": "pkg:npm/async@3.2.0"
        },
        {
          "ref": "pkg:npm/async@2.6.0"
        }
      ],
      "references": [
        {
          "id": "GHSA-fwr7-v2mv-hh25",
          "source": {
            "url": "https://github.com/advisories/GHSA-fwr7-v2mv-hh25",
            "name": "GitHub"
          }
        }
```
