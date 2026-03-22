# Source: https://docs.rootly.com/configuration/playbooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Create and manage response playbooks that automatically attach to incidents based on conditions like severity, service, or team to guide resolution efforts.

## Overview

Playbooks are a great way to create a document that can help speed incident resolution. We can see them as a collection of simple instructions to empower someone to resolve a particular incident (even if they have minimal experience).

Playbooks are **automatically attached** to incidents when they **match a configured condition** (for example: severity, service, functionality, team impacted ). You can see these fields in the screenshot below. If you have Playbooks or supported documentation hosted internally, you can link to them in the "External URL" field and provide detailed instructions in the content field.

<Frame>
    <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/misc/playbooks-1.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=3c564bf928301c1d215f31ae4d2e2642" alt="Document image" width="910" height="590" data-path="images/misc/playbooks-1.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/misc/playbooks-2.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=5aa05a3c23ca425453add642606a330c" alt="Document image" width="910" height="617" data-path="images/misc/playbooks-2.webp" />
</Frame>

On the above example, the **Database outage playbook** will be attached to any incident with the **SEV2 severity or the** **customers-postgresql-db** **microservices.** Please note that this is all OR logic currently, meaning this playbook will be attached to an incident that has just one of those matching condition, such as SEV2 severity for example.

Additionally, at the bottom of the Playbook details page you have the ability to append any relevant tasking that needs to be done during the incident.

<Frame>
    <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/misc/playbooks-3.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=fcb3a477c5d4c37f7947d6581331f679" alt="Document image" width="908" height="393" data-path="images/misc/playbooks-3.webp" />
</Frame>

Playbooks are a great way to prevent a single person from becoming the de facto expert on how to resolve a particular problem. We don't want one person on the team to be the only one to know how to bring a critical system back online.


Built with [Mintlify](https://mintlify.com).