# Source: https://render.com/docs/shared-responsibility-model.md

# Shared Responsibility Model — Understand how Render and our customers work together to keep applications secure.

Render's security controls are predicated on the assumption that customers maintain robust internal controls. The effective use of the Render system relies heavily on customers actively managing their assigned security responsibilities. This includes safeguarding user data, controlling access, and upholding security protocols.

This document delineates Render's specific responsibilities alongside the customer's obligations and identifies areas of shared responsibility. It aims to guide customers in establishing comprehensive security practices.

Note that the procedures and controls listed here serve as foundational guidance. They are not exhaustive. Customers are encouraged to implement additional controls that align with their specific security needs and compliance requirements.

## Customer responsibilities

*Customer is responsible for:*

- Protecting all secrets within their organization
- Managing and reviewing user access to the Render system
- Implementing and enforcing data policies regarding the types of data entered into the Render system, ensuring data is transmitted securely and encrypted as necessary
- Keeping informed about communications from Render that affect system security, user obligations, or service availability
- Establishing and maintaining security controls for system-generated outputs and reports
- Compliance with relevant legal and regulatory requirements
- Security of application-level configurations
- Regular security assessments of their applications
- Endpoint protection of workstations used to access the Render system
- Developing and maintaining their own business continuity and disaster recovery plans
- Deleting their data from the Render system upon termination of services

## Render responsibilities

*Render is responsible for:*

- Making sure all underlying operating systems are patched and up to date
- All internal networking between services and databases
- Securing the infrastructure that hosts all hardware, software, networking, and facilities
- Managing the underlying servers, networks, and storage
- Ensuring that the runtime environments for supported programming languages and frameworks are secure and up to date
- Transparency about their operational status and any security breaches
- Securing the platform, which includes middleware and other integrated services that it provides
- Providing detailed documentation and guidelines on the security features of their platform.

## Shared responsibilities

*Customer and Render share responsibility for:*

- Monitoring and responding to incidents, depending on the nature of the incident and where it occurs in the stack
- Security training
- Data privacy management—both parties should cooperate to ensure that data privacy is maintained according to best practices and compliance requirements.
- Conducting regular reviews of their security practices