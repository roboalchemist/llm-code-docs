# Source: https://docs.ox.security/inventory-with-ox-bom/bom.md

# BOM Dashboard

A Bill of Materials (BOM) is a complete, always-current inventory of what your software and environments contain. In OX, BOMs provide you a single view across code, build artifacts, and cloud so you can trace any risk from runtime back to its source and owner.

OX builds these BOMs by ingesting data from source control, CI/CD, registries, and cloud providers, then correlates it with vulnerabilities, policies, ownership, and SLAs. The result powers search, impact analysis, compliance reports, and attestation workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-098735a2e31176b4f234101e02e36923ce5048c1%2FBOM_intro.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| BOM option                                                                  | What it inventories and why use it                                                                                                                              |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [API BOM](https://docs.ox.security/inventory-with-ox-bom/api-bom)           | Catalogs your APIs by framework and type, shows issues exposed by endpoints. Use it to see API coverage, hot spots, and drill into risky services.              |
| [SBOM](https://docs.ox.security/inventory-with-ox-bom/sbom)                 | Lists libraries, packages, and versions inside apps and images. Use it for vulnerability and license governance, and to answer “where is this component used?”. |
| [SaaS BOM](https://docs.ox.security/inventory-with-ox-bom/saas-bom)         | Detects SaaS applications in use across the organization. Use it to track adoption, reduce shadow IT, and review data-exposure risk.                            |
| [Artifact BOM](https://docs.ox.security/inventory-with-ox-bom/artifact-bom) | Tracks build outputs such as container images, packages, and charts with provenance. Use it for release readiness, signatures, and supply-chain traceability.   |
| [Cloud BOM](https://docs.ox.security/inventory-with-ox-bom/cloud-bom)       | Maps cloud assets and running workloads. Use it to see runtime exposure, drift, and how deployed resources relate to images, repos, and owners.                 |
