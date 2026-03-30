# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry.md

# Registry

Registry connectors connect OX to container registries that store and distribute your container images.

OX imports data from these tools through APIs, enriches it with OX context (application mapping, ownership, workflows, and compliance), and presents it alongside findings from other scanners and tools in a unified view.

## What OX adds

* **Context and correlation:** OX maps findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Where data appears in OX

* **Active Issues:** Filter by **Source tool** to focus on findings from a specific connector.
* **Issue details:** Tabs show scanner evidence, asset data, and OX correlations such as application and repository mapping.
* **Assets and applications:** Imported assets appear in asset views, application context, and dashboards.
* **Risk prioritization:** Findings are ranked using combined development, pipeline, and runtime signals.

## **Supported connectors**

* [Amazon ECR](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/amazon-ecr)
* [Azure Container Registry](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry)
* [Docker Hub](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/docker-hub)
* [GitLab Container Registry](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/gitlab-container-registry)
* [Google Artifact Registry](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/google)
* [Harbor](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/harbor)
* [JFrog Artifactory](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/jfrog-artifactory)
* [Nexus Container Registry](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/nexus-container-registry)
* [Red Hat Quay](https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/red-hat-quay)
