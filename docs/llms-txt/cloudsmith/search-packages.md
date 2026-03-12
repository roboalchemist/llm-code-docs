# Source: https://help.cloudsmith.io/docs/search-packages.md

# Searching and Filtering

Searching for packages is simple and powerful with Cloudsmith. The search syntax is fully "boolean", in that you can combine queries together with `AND` (i.e. find this AND that), or `OR` (i.e. find this OR that), or `NOT` (i.e. find NOT this). This is optional, if you don't put any boolean operators (AND/OR) in, we'll just assume that you want `AND` by default.

***

## Search Terms

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Search By
      </th>

      <th>
        Search Terms Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Name (`name`)
      </td>

      <td>
        `name:my-package` (package name contains "my-package"; use anchors for exact match)
      </td>
    </tr>

    <tr>
      <td>
        Filename (`filename`)
      </td>

      <td>
        `filename:my-package.ext` (filename contains "my-package.ext"; use anchors for exact match)
      </td>
    </tr>

    <tr>
      <td>
        Tag (`tag`)
      </td>

      <td>
        `tag:latest` (a package tag contains "latest"; use anchors for exact match)
      </td>
    </tr>

    <tr>
      <td>
        Version - String-based (`version`)
      </td>

      <td>
        `version:^1.1.0$` (package version is exactly 1.1.0)\
        `version:1.1.0*post1` (package version contains 1.10 followed by post1).
      </td>
    </tr>

    <tr>
      <td>
        Version - Semantic (`version`)
      </td>

      <td>
        `version:1.1.0` (package version is "1.1.0")\
        `version:>1.1.0` (package version is greater than "1.1.0")\
        `version:<1.1.0` (package version is less than "1.1.0")\
        `version:~=1.1.0` (package version is greater or equal to 1.1.0, but less than 1.2.0)
      </td>
    </tr>

    <tr>
      <td>
        Prerelease (`prerelease`)
      </td>

      <td>
        `true` (packages are prerelease)\
        `false` (packages are not prerelease)
      </td>
    </tr>

    <tr>
      <td>
        Architecture (`architecture`)
      </td>

      <td>
        `architecture:x86_64` (architecture is "x86\_64")
      </td>
    </tr>

    <tr>
      <td>
        Distribution (`distribution`)
      </td>

      <td>
        `distribution:el/7` (distribution is "el", release is "7")
      </td>
    </tr>

    <tr>
      <td>
        Format (`format`)
      </td>

      <td>
        `format:deb` (format is "deb" le and p)
      </td>
    </tr>

    <tr>
      <td>
        Status (`status`)
      </td>

      <td>
        `status:in_progress` (status is "in\_progress")
      </td>
    </tr>

    <tr>
      <td>
        File Checksum (`checksum`)
      </td>

      <td>
        `checksum:5afba` (checksum contains "5afba")
      </td>
    </tr>

    <tr>
      <td>
        Downloads (`downloads`)
      </td>

      <td>
        `downloads:>8` (more than 8 downloads)\
        `downloads:<1000` (at least 1, but less than 1000 downloads)
      </td>
    </tr>

    <tr>
      <td>
        Package Type (`type`)
      </td>

      <td>
        `type:binary` (Binary Packages)\
        `type:source` (Source Packages)\
        `type:combined` (Binary and Source Packages)
      </td>
    </tr>

    <tr>
      <td>
        Size in Bytes (`size`)
      </td>

      <td>
        `size:>50000` (size is greater than 50000)\
        `size:<10000` (size is less than 10000)
      </td>
    </tr>

    <tr>
      <td>
        Uploaded Date (`uploaded`)
      </td>

      <td>
        `uploaded:’1 day ago’` (uploaded more than one day ago)\
        `uploaded:’August 14, 2019 EST’` (uploaded on Aug 14th)
      </td>
    </tr>

    <tr>
      <td>
        Entitlement Token Identifier (`token`)
      </td>

      <td>
        `token:3lKPVJPosCsY` (packages visible for specified token)
      </td>
    </tr>

    <tr>
      <td>
        Dependencies (`dependency`)
      </td>

      <td>
        `dependency:log4j` (search for packages that have a dependency with "log4j" in the name).\
        `dependency:log4j=1.2.17` (search for packages dependencies name including "log4j" & version matching 1.2.17).\
        `dependency:log4j<2.0.0` (search for packages dependencies with name including "log4j" & version less than 2.0.0).
      </td>
    </tr>

    <tr>
      <td>
        Repository (`repository`)
      </td>

      <td>
        `repository:repo-name` (Search for packages within the repository named "repo-name")
      </td>
    </tr>

    <tr>
      <td>
        * \*Debian:\*\* Component
      </td>

      <td>
        `deb_component:component-name` (Search for packages by Debian Component)
      </td>
    </tr>

    <tr>
      <td>
        * \*Docker:\*\* Image Digest
      </td>

      <td>
        `docker_image_digest:sha256:abcdef` (Search for packages by Docker Image Digest)
      </td>
    </tr>

    <tr>
      <td>
        * \*Docker:\*\* Layer Digest
      </td>

      <td>
        `docker_layer_digest:sha256:abcdef` (Search for packages by Docker Layer Digest)
      </td>
    </tr>

    <tr>
      <td>
        * *Maven:* \*GroupID
      </td>

      <td>
        `maven_group_id:io.cloudsmith` (Search for packages by Maven GroupID)
      </td>
    </tr>

    <tr>
      <td>
        Packages that have violated a policy (`policy_violated`)
      </td>

      <td>
        `true` (packages that have violated a policy)\
        `false` (packages have not violated a policy)
      </td>
    </tr>

    <tr>
      <td>
        Packages that have violated a vulnerability policy (`vulnerability_policy_violated`)
      </td>

      <td>
        `true` (packages that have violated a vulnerability policy)\
        `false` (packages have not violated a vulnerability policy)
      </td>
    </tr>

    <tr>
      <td>
        Packages that have violated a license policy (`license_policy_violated`)
      </td>

      <td>
        `true` (packages that have violated a license policy)\
        `false` (packages have not violated a license policy)
      </td>
    </tr>

    <tr>
      <td>
        Packages that have violated a deny list policy (`deny_policy_violated`)
      </td>

      <td>
        `true` (packages that have violated a deny list policy)\
        `false` (packages have not violated a deny list policy)
      </td>
    </tr>
  </tbody>
</Table>

**For all queries you can use:**\
`~` for negation.  (Example: `~foo`)

**For string queries you can use:**\
`^`   - to anchor to start of term.  (Example: `^foo`)\
`$` -  to anchor to end of term.  (Example: `foo$`)\
`*`  -  for fuzzy matching.  (Example: `foo*bar`)

**For number or date queries you can use:**\
`>`   -  for values greater than .  (Example: `>foo`)\
`>=` -  for values greater / equal .  (Example: `>=foo`)\
`<`   -  for values less than.  (Example: `<foo`)\
 `<=` -  for values less / equal.  (Example: `<=foo`)

Please note, when you use a query like `uploaded: >'1 month ago'`, that becomes `uploaded > dd/mm/yy` (i.e, within the last month).

**For version queries you can use:**\
`>`   -  for versions greater than .  (Example: `>1.2.3.`)\
`>=` -  for versions greater / equal .  (Example: `>=1.2.3`)\
`<`   -  for versions less than.  (Example: `<1.2.3`)\
 `<=` -  for versions less / equal.  (Example: `<=1.2.3`)\
`~=` -  for versions greater than or equal to, upto the next incompatible version. (Example: `~=1.2.0`)

> 📘
>
> Remember: You can use any combination of `AND`, `OR` and `NOT`. You can use parentheses to group terms if required, as `AND` has a higher precedence than `OR`, and it may change the meaning of queries without it.

***

## A Short Working Example

Suppose that you had the following packages:

* AlphaLib, Version: 1.0
* AlphaLib, Version: 1.1
* AlphaLib, Version: 2.0
* BetaLib: Version: 0.9

To find "AlphaLib" packages that are in the version 1.x series only, your query would be:\
`name:^AlphaLib$ AND version:~=1.0.`

Which would provide the following results:

* AlphaLib, Version: 1.0
* AlphaLib, Version: 1.1

To bring the query down, we added the following parts:

* `name:^AlphaLib$` - Find a package name that is **exactly** "AlphaLib". Without the `^` (starts-with) and `$` (ends-with), the query would be fuzzy, and potentially find packages called "AlphaLib2" or "FreeAlphaLib" too.
* `AND` - We want to search for both the name and version together. Both must match for the results.
* `version:~=1.0` - Find package versions that are at-least 1.0, upto the next incompatible version (2.0).

***

## Searching Packages via the Website UI

At the top of every page is the search box:

<Image alt="Search box in the Website UI" align="center" src="https://files.readme.io/97075343a9a33ef4bbc6957a18556c5b6cdd8e7b22ef88370bdd70f23d3e2902-package-search-6-edited.png">
  Search box in the Website UI
</Image>

Additional help and examples are available by hovering over the "? Search syntax" at the right side of the search box.

<Image alt="Search syntax displayed" align="center" src="https://files.readme.io/58be45141bb3dd355135c9535b94b4433d28a8a7b064b0d619157a717592a59b-package-search-3-edited.png">
  Search syntax displayed
</Image>

***

## Searching Packages via the Cloudsmith API

Please see the Cloudsmith API [interactive sandbox](https://api-prd.cloudsmith.io/v1/#!/packages/packages_list) and the full API [reference](https://help.cloudsmith.io/reference#packages_list).

***

## Searching Packages via the Cloudsmith CLI

To search packages using the Cloudsmith CLI, you use the `cloudsmith list packages` command in combination with the `-q` option:

```shell
cloudsmith list packages OWNER/REPOSITORY -q "SEARCH_TERMS"
```

**Example**\
To search for all debian packages:

```shell
cloudsmith list packages cloudsmith/examples -q "format:deb"
```

<Image title="search_pkgs_cli_format.png" alt={1120} align="center" src="https://files.readme.io/1aa0913-search_pkgs_cli_format.png">
  CLI search for format "deb"
</Image>

**Example**\
To search for the latest rpm and composer packages:

```shell
cloudsmith list packages cloudsmith/examples -q "tag:latest AND (format:rpm OR format:composer)"
```

<Image title="search_pkgs_cli_tag_and.png" alt={1223} align="center" src="https://files.readme.io/a2f0d45-search_pkgs_cli_tag_and.png">
  CLI search for tag "latest" and two formats
</Image>

**Example**\
To search for all python packages larger than 2KB with more than 50 downloads:

```shell
cloudsmith list packages cloudsmith/examples -q "format:python AND downloads:>50 AND size:>2048"
```

<Image title="search_pkgs_cli_size_dls.png" alt={1117} align="center" src="https://files.readme.io/ac51e3f-search_pkgs_cli_size_dls.png">
  CLI search for python packages larger than 2KB with more than 50 downloads
</Image>