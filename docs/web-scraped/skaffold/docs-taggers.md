# Source: https://skaffold.dev/docs/taggers/

Title: Tag

URL Source: https://skaffold.dev/docs/taggers/

Markdown Content:
Skaffold supports multiple taggers or tag policies for tagging images:

*   the `gitCommit` tagger uses git commits/references.
*   the `inputDigest` tagger uses a digest of the artifact source files.
*   the `envTemplate` tagger uses environment variables.
*   the `dateTime` tagger uses current date and time, with a configurable pattern.
*   the `customTemplate` tagger uses a combination of the existing taggers as components in a template.
*   the `sha256` tagger uses `latest`.

The default tagger, if none is specified in the `skaffold.yaml`, is the `gitCommit` tagger.

The tags can be overridden with a fixed tag with the `--tag` option on the command-line.

### Configuration

The tag policy is specified in the `tagPolicy` field of the `build` section of the `skaffold.yaml` configuration file.

```
build:
  tagPolicy:
    gitCommit: {}
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

For a detailed discussion on Skaffold configuration, see [Skaffold Concepts](https://skaffold.dev/docs/design/config/) and [skaffold.yaml References](https://skaffold.dev/docs/references/yaml/).

### How tagging works

*   Image tags are computed before the images are built.
*   No matter the tagger, Skaffold always uses immutable references in Kubernetes manifests. Which reference is used depends on whether the images are pushed to a registry or loaded directly into the cluster (such as via the Docker daemon): 
    *   **When images are pushed**, their immutable digest is available. Skaffold then references images both by tag and digest. Something like `image:tag@sha256:abacabac...`. Using both the tag and the digest seems superfluous but it guarantees immutability and helps users quickly see which version of the image is used.
    *   **When images are loaded directly into the cluster**, such as loading into the cluster’s Docker daemon, digests are not available. We have the tags and the imageIDs. Since imageIDs can’t be used in Kubernetes manifests, Skaffold creates an additional immutable, local only, tag with the same name as the imageID and uses that in manifests. Something like `image:abecfabecfabecf...`.

*   Skaffold never references images just by their tags because those tags are mutable and can lead to cases where Kubernetes will use an outdated version of the image.

`gitCommit` is the default tag policy of Skaffold: if you do not specify the `tagPolicy` field in the `build` section, Skaffold will use Git information to tag artifacts.

The `gitCommit` tagger will look at the Git workspace that contains the artifact’s `context` directory and tag according to those rules:

*   If the workspace is on a Git tag, that tag is used to tag images
*   If the workspace is on a Git commit, the short commit is used
*   If the workspace has uncommitted changes, a `-dirty` suffix is appended to the image tag

### Example

The following `build` section instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `gitCommit` tag policy specified explicitly:

```
build:
  tagPolicy:
    gitCommit: {}
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

### Configuration

| Option | Description | Default |
| --- | --- | --- |
| `variant` | determines the behavior of the git tagger. Valid variants are: `Tags` (default): use git tags or fall back to abbreviated commit hash. `CommitSha`: use the full git commit sha. `AbbrevCommitSha`: use the abbreviated git commit sha. `TreeSha`: use the full tree hash of the artifact workingdir. `AbbrevTreeSha`: use the abbreviated tree hash of the artifact workingdir. |  |
| `prefix` | adds a fixed prefix to the tag. |  |
| `ignoreChanges` | specifies whether to omit the `-dirty` postfix if there are uncommitted changes. | `false` |

`inputDigest`: uses a digest of the artifact source to tag images
-----------------------------------------------------------------

The `inputDigest` tagger tags images with a digest of the artifact source files. The source files are the dependencies calculated by the configured builder.

### Example

The following `build` section instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `inputDigest` tag policy:

```
build:
  tagPolicy:
    inputDigest: {}
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

### Configuration

`inputDigest` tag policy features no options.

`envTemplate` allows you to use environment variables in tags. This policy requires that you specify a tag template, where part of template can be replaced with values of environment variables during the tagging process.

The following `build` section, for example, instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `envTemplate` tag policy. The tag template is `{{.FOO}}`; when Skaffold finishes building the image, it will check the list of available environment variables in the system for the variable `FOO`, and use its value to tag the image.

### Example

```
build:
  tagPolicy:
    envTemplate:
      template: "{{.FOO}}"
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

Suppose the value of the `FOO` environment variable is `v1`, the image built will be `gcr.io/k8s-skaffold/example:v1`.

### Configuration

The tag template uses the [Go Programming Language Syntax](https://golang.org/pkg/text/template/). As showcased in the example, `envTemplate` tag policy features one **required** parameter, `template`, which is the tag template to use. To learn more about templating support in Skaffold.yaml see [Templated fields](https://skaffold.dev/docs/environment/templating/)

`dateTime` uses the time when Skaffold starts building artifacts as the tag. You can choose which format and timezone Skaffold should use. By default, Skaffold uses the time format `2006-01-02_15-04-05.999_MST` and the local timezone.

### Example

The following `build` section, for example, instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `dateTime` tag policy:

```
build:
  tagPolicy:
    dateTime:
      format: "2006-01-02_15-04-05.999_MST"
      timezone: "Local"
  artifacts:
  - image: gcr.io/k8s-skaffold/example
# The tagPolicy section above is equal to
# tagPolicy:
#   dateTime: {}
```

Suppose current time is `15:04:09.999 January 2nd, 2006` and current time zone is `MST` (`US Mountain Standard Time`), the image built will be `gcr.io/k8s-skaffold/example:2006-01-02_15-04-05.999_MST`.

### Configuration

You can learn more about what time format and time zone you can use in [Go Programming Language Documentation: Time package/Format Function](https://golang.org/pkg/time#Time.Format) and [Go Programming Language Documentation: Time package/LoadLocation Function](https://golang.org/pkg/time#LoadLocation) respectively. As showcased in the example, `dateTime` tag policy features two optional parameters: `format` and `timezone`.

`customTemplate`: uses a combination of the existing taggers as components in a template
----------------------------------------------------------------------------------------

`customTemplate` allows you to combine all existing taggers to create a custom tagging policy. This policy requires that you specify a tag template, using a combination of plaintext and references to other tagging strategies which will be evaluated at runtime. We refer to these individual parts as “components”, which can be any of the other existing supported tagging strategies. Nested `customTemplate` components are not supported.

The following `build` section, for example, instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `customTemplate` tag policy. The tag template is `{{.FOO}}_{{.BAR}}`. The components are a `dateTime` tagger named `FOO` and a `gitCommit` tagger named `BAR`. When Skaffold finishes building the image, it will evaluate `FOO` and `BAR` and use their values to tag the image.

### Example

```
build:
  tagPolicy:
    customTemplate:
      template: "{{.FOO}}_{{.BAR}}"
      components:
      - name: FOO
        dateTime:
          format: "2006-01-02"
          timezone: "UTC"
      - name: BAR
        gitCommit:
          variant: AbbrevCommitSha
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

Suppose the current time is `15:04:09.999 January 2nd, 2006` and the abbreviated commit sha is `25c65e0`, the image built will be `gcr.io/k8s-skaffold/example:2006-01-02_25c65e0`.

### Configuration

The tag template uses the [Golang Templating Syntax](https://golang.org/pkg/text/template/). As showcased in the example, `customTemplate` tag policy features one **required** parameter, `template`, which is the tag template to use. To learn more about templating support in the skaffold.yaml, see [Templated fields](https://skaffold.dev/docs/environment/templating/)

`sha256`: uses `latest` to tag images
-------------------------------------

`sha256` is a misleading name. It is named like that because, in the end, when Skaffold deploys to a remote cluster, the image’s `sha256` digest is used in addition to `:latest` in order to create an immutable image reference.

### Example

The following `build` section instructs Skaffold to build a Docker image `gcr.io/k8s-skaffold/example` with the `sha256` tag policy:

```
build:
  tagPolicy:
    sha256: {}
  artifacts:
  - image: gcr.io/k8s-skaffold/example
```

### Configuration

`sha256` tag policy features no options.
