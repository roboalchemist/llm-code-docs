# Source: https://docs.jit.io/docs/introduction-2.md

# Security Plans Introduction

This section describes Jit's security plans and their components:

* For a full list of security plans supported by Jit, see [Security Plans](https://docs.jit.io/docs/security-plans).
* For a full list of available security controls, see [Security Controls](https://docs.jit.io/docs/plan-items)
* For a full list of security tools, see [Security Tools](https://docs.jit.io/docs/security-tools).

## Definition of a Jit Security Plan

A product Security plan is an outcome-driven blueprint that describes best practices and measures to protect and manage the different components of a company's tech stack.

It is designed to align with the organization's overall business objectives and security goals, with a continuous security approach of the company's product(s).

### Security Plan - From intent to implementation

* Captures security requirements as intent.
* Allows for velocity and extensibility, including addressing custom risks.
* Jit translates the abstract intent into a concrete implementation by running workflows and evaluating policies.
* Jit runs workflows:
  * Uses integration points along the SDLC and with third parties.
  * Can be triggered by various events such as pull requests, deployments, scheduled events, or external inputs.
  * Orchestrates security tools and manages automated processes like incident response, onboarding, and offboarding.