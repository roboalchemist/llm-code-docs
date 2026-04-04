# Source: https://help.cloudsmith.io/docs/signing-keys.md

# Signing Keys

Cloudsmith uses GPG or RSA signatures (where applicable) in addition to package checksums to detect tampering.

We calculate a signature for every file that is uploaded, but only some of the package formats make it available or use it. Only some of the formats also offer metadata signing.

For increased trust, you can also provide your own [GPG key](https://help.cloudsmith.io/docs/repository-settings#custom-gpg-signing-key) or [RSA key](https://help.cloudsmith.io/docs/repository-settings#custom-rsa-signing-key) for signing.

## Key Support by Package Format

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Package Format
      </th>

      <th>
        Key Type
      </th>

      <th>
        Key Use
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Alpine](https://help.cloudsmith.io/docs/alpine-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-red">RSA</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span>
      </td>
    </tr>

    <tr>
      <td>
        [Cargo](https://help.cloudsmith.io/docs/cargo-registry)
      </td>

      <td />

      <td>
        <span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>
      </td>
    </tr>

    <tr>
      <td>
        [CocoaPods](https://help.cloudsmith.io/docs/cocoapods-repository)
      </td>

      <td />

      <td>
        <span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>
      </td>
    </tr>

    <tr>
      <td>
        [Composer](https://help.cloudsmith.io/docs/composer-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Conan](https://help.cloudsmith.io/docs/conan-repository)
      </td>

      <td />

      <td>
        <span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>
      </td>
    </tr>

    <tr>
      <td>
        [CRAN](https://help.cloudsmith.io/docs/cran-repository)
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        [Dart](https://help.cloudsmith.io/docs/dart-repository)
      </td>

      <td />

      <td>
        <span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>
      </td>
    </tr>

    <tr>
      <td>
        [Debian](https://help.cloudsmith.io/docs/debian-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span>
      </td>
    </tr>

    <tr>
      <td>
        [Docker](https://help.cloudsmith.io/docs/docker-registry)
      </td>

      <td>
        <span class="cs-tag cs-tag-red">RSA</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span>
      </td>
    </tr>

    <tr>
      <td>
        [Go](https://help.cloudsmith.io/docs/go-registry)
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        [Gradle](https://help.cloudsmith.io/docs/gradle-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span> <span class="cs-tag cs-tag-midnight-blue">Packages</span>
      </td>
    </tr>

    <tr>
      <td>
        [Helm Charts](https://help.cloudsmith.io/docs/helm-chart-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [LuaRocks](https://help.cloudsmith.io/docs/luarocks-repository)
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        [Maven](https://help.cloudsmith.io/docs/maven-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span> <span class="cs-tag cs-tag-midnight-blue">Packages</span>
      </td>
    </tr>

    <tr>
      <td>
        [npm](https://help.cloudsmith.io/docs/npm-registry)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [NuGet](https://help.cloudsmith.io/docs/nuget-feed)
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        [Python](https://help.cloudsmith.io/docs/python-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Raw](https://help.cloudsmith.io/docs/raw-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [RPM](https://help.cloudsmith.io/docs/redhat-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span> <span class="cs-tag cs-tag-midnight-blue">Packages</span>
      </td>
    </tr>

    <tr>
      <td>
        [Ruby](https://help.cloudsmith.io/docs/ruby-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [sbt](https://help.cloudsmith.io/docs/sbt-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td>
        <span class="cs-tag cs-tag-purple">Index</span> <span class="cs-tag cs-tag-midnight-blue">Packages</span>
      </td>
    </tr>

    <tr>
      <td>
        [Terraform Modules](https://help.cloudsmith.io/docs/terraform-modules-repository)
      </td>

      <td />

      <td>
        <span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>
      </td>
    </tr>

    <tr>
      <td>
        [Unity Registry](https://help.cloudsmith.io/docs/unity-registry)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Vagrant](https://help.cloudsmith.io/docs/vagrant-repository)
      </td>

      <td>
        <span class="cs-tag cs-tag-blue">GPG</span>
      </td>

      <td />
    </tr>
  </tbody>
</Table>

## Docker and Cosign

> 📘 Early Access
>
> Automatic signing of Docker images on image upload is currently in early Access. If you would like to enable this feature please [Contact Us](https://help.cloudsmith.io/docs/contact-us).

When a Docker image is uploaded to a repository, Cloudsmith automatically generates a Cosign signature using the repository’s ECDSA private key. Customers can download the corresponding ECDSA public key to verify the specific image, as below:

```text
docker push docker.cloudsmith.io/<org>/<repo>/alpine:<sha256-checksum>

cosign verify --private-infrastructure=true --key public-ecdsa-key.key docker.cloudsmith.io/<org>/<repo>/alpine:<sha256-checksum>
```

> 📘 Docker image verification
>
> Cloudsmith does not log to [Rekor](https://docs.sigstore.dev/logging/overview/) when generating signatures on image upload. When verifying these using `cosign verify` pass `--private-infrastructure=true`to prevent cosign querying the Rekor log.

As docker images within Cloudsmith are predominantly private, when a cosign signature is automatically generated on image upload, Cloudsmith does not add any data to the [Rekor](https://docs.sigstore.dev/logging/overview/) log . The Rekor log contains a record of image names and corresponding public keys, and is used to enable software maintainers to record signed metadata, and for verifiers to monitor and query the log for an appropriate identity. When using `cosign verify` to verify cosign signatures generated by Cloudsmith, pass `--private-infrastructure=true` to ensure cosign does not query the Rekor log. If this parameter is not passed, the following warning will be displayed:

```text
WARNING: "docker.cloudsmith.io/<org>/<repo>/alpine:<sha256-checksum> appears to be a private repository, please confirm uploading to the transparency log at "https://rekor.sigstore.dev"
```

Please note customers who create their own signatures using the `cosign sign` command, will be asked if they wish to upload a transparency log to Rekor.

> 🚧 Supported Keys
>
> If a key is used which is not supported by Cosign, it will not be possible to generate the associated OCI image signature.

Cosign supports the following ECDSA curves:

* NIST P-224 (secp224r1)
* NIST P-256 (secp256r1, prime256v1)
* NIST P-384 (secp384r1)
* NIST P-521 (secp521r1)

If a key is used which is not supported by Cosign, Cloudsmith will not be able to generate the associated OCI image signature.