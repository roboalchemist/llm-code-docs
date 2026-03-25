# The PGPainless Ecosystem

PGPainless consists of an ecosystem of different libraries and projects.

The diagram below shows, how the different projects relate to one another.

## Libraries and Tools

- 

PGPainless [https://codeberg.org/pgpainless/pgpainless]

The main repository contains the following components:

  - 

`pgpainless-core` - core implementation - powerful, yet easy to use OpenPGP API

  - 

`pgpainless-sop` - super simple OpenPGP implementation. Drop-in for `sop-java`

  - 

`pgpainless-cli` - SOP CLI implementation using PGPainless

- 

SOP-Java [https://codeberg.org/pgpainless/sop-java]

An API definition and CLI implementation of the Stateless OpenPGP Protocol [https://datatracker.ietf.org/doc/draft-dkg-openpgp-stateless-cli/] (SOP).
Consumers of the SOP API can simply depend on `sop-java` and then switch out the backend as they wish.
Read more about the SOP protocol here.

  - 

`sop-java` - generic OpenPGP API definition

  - 

`sop-java-picocli` - CLI frontend for `sop-java`

- 

WKD-Java [https://codeberg.org/pgpainless/wkd-java]

Implementation of the Web Key Directory [https://www.ietf.org/archive/id/draft-koch-openpgp-webkey-service-13.html].

  - 

`wkd-java` - generic WKD discovery implementation

  - 

`wkd-java-cli` - CLI frontend for WKD discovery using PGPainless

  - 

`wkd-test-suite` - Generator for test vectors for testing WKD implementations

- 

VKS-Java [https://codeberg.org/pgpainless/vks-java]

Client-side API for communicating with Verifying Key Servers, such as https://keys.openpgp.org/.

  - 

`vks-java` - VKS client implementation

  - 

`vks-java-cli` - CLI frontend for `vks-java`

- 

Cert-D-Java [https://codeberg.org/pgpainless/cert-d-java]

Implementations of the Shared OpenPGP Certificate Directory specification [https://sequoia-pgp.gitlab.io/pgp-cert-d/].

  - 

`pgp-certificate-store` - abstract definitions of OpenPGP certificate stores

  - 

`pgp-cert-d-java` - implementation of `pgp-certificate-store` following the PGP-CERT-D spec

  - 

`pgp-cert-d-java-jdbc-sqlite-lookup` - subkey lookup using sqlite database

- 

Cert-D-PGPainless [https://codeberg.org/pgpainless/cert-d-pgpainless]

Implementation of the Shared OpenPGP Certificate Directory specification [https://sequoia-pgp.gitlab.io/pgp-cert-d/] using PGPainless.

  - 

`pgpainless-cert-d` - PGPainless-based implementation of `pgp-cert-d-java`

  - 

`pgpainless-cert-d-cli` - CLI frontend for `pgpainless-cert-d`

- 

PGPainless-WOT [https://codeberg.org/pgpainless/pgpainless-wot]

Implementation of the OpenPGP Web of Trust specification [https://sequoia-pgp.gitlab.io/sequoia-wot/] using PGPainless.

  - 

`pgpainless-wot` - Parse OpenPGP keyrings into a generic `Network` object

  - 

`wot-dijkstra` - Perform queries to find paths inside a `Network` object

  - 

`pgpainless-wot-cli` - CLI frontend for `pgpainless-wot` and `wot-dijkstra`

  - 

`wot-test-suite` - Test vectors ported from Sequoia-PGPs WoT implementation [https://gitlab.com/sequoia-pgp/sequoia-wot/-/tree/main/tests/data]

- 

PGPeasy [https://codeberg.org/pgpainless/pgpeasy]

Prototypical, comprehensive OpenPGP CLI application

  - 

`pgpeasy` - CLI application