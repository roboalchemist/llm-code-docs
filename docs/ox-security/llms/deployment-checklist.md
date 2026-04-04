# Source: https://docs.ox.security/get-started/deployment-checklist.md

# Deployment Checklist

Use this checklist to guide the core steps required to deploy OX in your environment.

The list helps ensure that your setup is complete, your environment is connected, and your workflows and pipeline logic are properly configured.

Although onboarding technically ends once source control is connected and initial scans run, this checklist continues into the full deployment lifecycle, allowing you to fine-tune the platform and gradually automate your security processes.

| Area                        | Task                                                                                        | Status |
| --------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| **Login**                   | Add users manually or invite them to your organization                                      | ☐      |
|                             | Configure SSO                                                                               | ☐      |
|                             | Create scopes using tags or owners                                                          | ☐      |
| **Connect the Environment** | Connect core systems: SCM (required), Registry, Cloud, Kubernetes, Ticketing, Messaging     | ☐      |
|                             | Validate that all required resources are selected for scanning                              | ☐      |
| **Review Results**          | Verify that scans are running and results appear in the Dashboard, Applications, and Issues | ☐      |
|                             | Confirm that the initial code scan completed successfully                                   | ☐      |
| **Platform Fine-Tuning**    | Review Business Priority Score and adjust as needed                                         | ☐      |
| **Workflows**               | Review issues and design workflows according to your organizational processes               | ☐      |
|                             | Configure workflow logic and test automation paths                                          | ☐      |
| **Pipeline Integration**    | Configure pipeline workflows                                                                | ☐      |
|                             | Connect pipeline integration(s) and run in monitor mode                                     | ☐      |
| **Policies**                | Review policies and fine-tune configurations                                                | ☐      |
