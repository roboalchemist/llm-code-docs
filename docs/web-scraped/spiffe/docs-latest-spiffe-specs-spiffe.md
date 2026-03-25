# Source: https://spiffe.io/docs/latest/spiffe-specs/spiffe/

Title: Secure Production Identity Framework for Everyone

URL Source: https://spiffe.io/docs/latest/spiffe-specs/spiffe/

Markdown Content:
Secure Production Identity Framework for Everyone

Status of this Memo[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#status-of-this-memo)
---------------------------------------------------------------------------------------------

This document specifies an identity and identity issuance standard for the internet community, and requests discussion and suggestions for improvements. Distribution of this document is unlimited.

Abstract[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#abstract)
-----------------------------------------------------------------------

Distributed design patterns and practices such as microservices, container orchestrators, and cloud computing have led to production environments that are increasingly dynamic and heterogenous. Conventional security practices (such as network policies that only allow traffic between particular IP addresses) struggle to scale under this complexity. A first-class identity framework for workloads in an organization becomes necessary.

Further, modern developers are expected to understand and play a role in how applications are deployed and managed in production environments. Operations teams require deeper visibility into the applications they are managing. As we move to a more evolved security stance, we must offer better tools to both teams so they can play an active role in building secure, distributed applications.

The SPIFFE standard provides a specification for a framework capable of bootstrapping and issuing identity to services across heterogeneous environments and organizational boundaries.

Table of Contents[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#table-of-contents)
-----------------------------------------------------------------------------------------

1. [Introduction](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#1-introduction)

2. [The SPIFFE ID](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#2-the-spiffe-id)

3. [The SPIFFE Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#3-the-spiffe-verifiable-identity-document)

4. [The Workload API](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#4-the-workload-api)

5. [Conclusion](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#5-conclusion)

 Appendix A. [List of SPIFFE Specifications](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#appendix-a-list-of-spiffe-specifications)

1. Introduction[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#1-introduction)

------------------------------------------------------------------------------------

The SPIFFE standard comprises three major components - one which standardizes an identity namespace, one which dictates the manner in which an issued identity may be presented and verified, and another which specifies an API through which identity may be retrieved and/or issued. These components are known as the SPIFFE ID, the SPIFFE Verifiable Identity Document (SVID) and the Workload API, respectively.

While each of these components has a dedicated specification, the remainder of this document will explore them at a high level, and explain how they fit together.

1. The SPIFFE ID[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#2-the-spiffe-id)

--------------------------------------------------------------------------------------

A SPIFFE ID is a structured string (represented as a URI) which serves as the “name” of an entity. Although just a string, it is the component around which everything else is built. It is defined in the [SPIFFE Identity and Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/) specification.

1. The SPIFFE Verifiable Identity Document[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#3-the-spiffe-verifiable-identity-document)

------------------------------------------------------------------------------------------------------------------------------------------

A SPIFFE Verifiable Identity Document (SVID) is a document which carries the SPIFFE ID itself. It is the functional equivalent of a passport - a document which is presented that carries the identity of the presenter. Of course, similar to passports, they must be resistant to forgery, and it must be obvious that the document belongs to the presenter. In order to achieve this, an SVID includes cryptographic properties which allow it to be:

1. proven as authentic
2. proven to belong to the presenter

An SVID itself is not a document type. Instead, we define:

1. the properties required of an SVID
2. the method by which SVID information can be encoded and validated in various existing document types

The supported document types are an X.509 certificate or a JWT token.

The SPIFFE SVID is defined in the [SPIFFE Identity and Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/) specification. The X.509 SVID specification is defined in [The X.509 SPIFFE Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/x509-svid/). The JWT token SVID specification is defined in [The JWT SPIFFE Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/jwt-svid/).

1. The Workload API[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#4-the-workload-api)

--------------------------------------------------------------------------------------------

The SPIFFE Workload API is the method through which workloads, or compute processes, obtain their SVID(s). It is typically exposed locally (eg. via a Unix domain socket), and explicitly does not include an authentication handshake or authenticating token from the workload. Implementors can verify the authenticity of the caller to the Workload API via an out-of-band method, such as inspecting the properties of the process calling the Unix domain socket that are provided by the operating system.

In addition to providing a workload with its necessary SVIDs, the Workload API delivers the CA bundles which the workload should outwardly trust. These bundles are associated with trust domains outside of the issued SVID, and are used for federation.

The Workload API is defined in the [SPIFFE Workload API](https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_api/) specification, please see that document for more information.

1. Conclusion[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#5-conclusion)

--------------------------------------------------------------------------------

This document covered, at a high level, the various components that make up the SPIFFE specification as a whole. Together, these components solve many of the authentication and traffic security challenges presented in modern, heterogeneous environments, particularly those which are highly dynamic. For more detailed information, please see the specification(s) related to the component of interest.

Appendix A. List of SPIFFE Specifications[](https://spiffe.io/docs/latest/spiffe-specs/spiffe/#appendix-a-list-of-spiffe-specifications)
----------------------------------------------------------------------------------------------------------------------------------------

* [The SPIFFE Identity and Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/)
* [The X.509 SPIFFE Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/x509-svid/)
* [The JWT SPIFFE Verifiable Identity Document](https://spiffe.io/docs/latest/spiffe-specs/jwt-svid/)
* [The SPIFFE Workload Endpoint](https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_endpoint/)
* [The SPIFFE Workload API](https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_api/)
* [The SPIFFE Trust Domain and Bundle](https://spiffe.io/docs/latest/spiffe-specs/spiffe_trust_domain_and_bundle/)
* [SPIFFE Federation](https://spiffe.io/docs/latest/spiffe-specs/spiffe_federation/)
