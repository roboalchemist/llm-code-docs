# Source: https://docs.port.io/solutions/security/security-champions-initiatives.md

# Security champions & initiatives

Scale security culture

**Port empowers organizations to scale security culture by making secure development measurable, actionable, and rewarding.**

## Introduction[â](#introduction "Direct link to Introduction")

The most successful security programs are **not built by security teams alone**âthey are built by empowering every developer to take part in protecting the business.

Traditional approaches rely on:

* Mandatory training sessions.
* Security checklists.
* Penalty-driven compliance.

These often create friction between security and engineering teams and fail to build sustainable engagement.

The reality: most developers **want** to build secure software but are overwhelmed by:

* Conflicting security requirements.
* Unclear guidance.
* Tools that slow them down.

The solution is to **make security the easy and rewarding choice** through:

* Clear standards and expectations.
* Automated guardrails.
* Recognition and motivation for security-positive behaviors.

Port provides the foundation to scale these efforts by connecting **people, processes, and technology** in one platform.

## Why many security champion programs fail[â](#why-many-security-champion-programs-fail "Direct link to Why many security champion programs fail")

Most security champion programs start with enthusiasm but fizzle out due to poor execution.

| Common Failure             | Impact on the Program                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Unclear expectations**   | Champions are unsure of their role beyond vague directives like "promote security."                        |
| **No measurable outcomes** | Progress is tracked by activity (training hours) rather than meaningful results (vulnerabilities reduced). |
| **Tool friction**          | Security tools create extra work without providing developers clear value or context.                      |
| **Recognition gaps**       | Champions take on extra responsibilities without career incentives or visibility.                          |
| **Unsustainable model**    | Programs rely on a few motivated individuals who eventually burn out.                                      |

## Port's approach: measurable, sustainable, scalable[â](#ports-approach-measurable-sustainable-scalable "Direct link to Port's approach: measurable, sustainable, scalable")

Port turns security champions programs from volunteer-driven efforts into **systematic, measurable cultural transformation initiatives**.

It does this through three pillars:

1. **Scorecards** â to set clear standards and expectations.
2. **Initiatives** â to create momentum and shared goals.
3. **Guardrails & Automation** â to make secure development frictionless.

## 1. Scorecards: defining security success[â](#1-scorecards-defining-security-success "Direct link to 1. Scorecards: defining security success")

Scorecards in Port translate abstract security principles into **concrete, trackable practices** for teams and services.<br /><!-- -->Each scorecard contains criteria that teams can directly influence.

### Application security scorecard[â](#application-security-scorecard "Direct link to Application security scorecard")

Track practices that prevent vulnerabilities from reaching production:

* **Dependency management** â Vulnerable dependencies are updated promptly.
* **Secure coding practices** â Security linters and SAST integrated into CI/CD.
* **Access controls** â Proper authentication and authorization in place.
* **Data protection** â Sensitive data handled according to policy.
* **Security testing** â Security tests included in CI/CD pipelines.

Portâs **Scorecards** make Application security success concrete. Scorecards can turn the OWASP Top-10 into tiered, measurable targetsâ**Basic â Bronze â Silver â Gold**. This helps teams see exactly what âgoodâ looks like and how far theyâve progressed.

* **Risk-aligned tiers:** Bronze (exploit blockers), Silver (crypto/logging integrity), Gold (design & config hardening) map effort to impact.
* **Clear pass criteria:** Each OWASP control has an explicit check; green checks show whatâs met (e.g., A01, A07, A03, A10 at Bronze; A08, A02, A09 at Silver; A06, A04, A05 at Gold).
* **Instant posture view:** The horizontal progress bar shows portfolio maturity at a glanceâno hunting through scans.
* **Ownership built-in:** Scorecards can be filtered by service/team, turning standards into accountable goals.
* **Automation hooks:** Fail a control â open ticket/notify/optionally gate deploys; pass â record evidence for audits.
* **Continuous improvement:** Teams climb tiers over time, moving from break-fix to secure-by-design, tracked in one place.

![OWASP Top 10 Chart showing Gold, Silver and Basic tier distribution](/img/guides/owasp/chart.png) ![Application security](/img/guides/security-solution/owasp-scorecard.png)

### Infrastructure security scorecard[â](#infrastructure-security-scorecard "Direct link to Infrastructure security scorecard")

Ensure infrastructure is deployed and maintained securely:

* **Network security** â Proper segmentation and firewall rules.
* **IAM hygiene** â Enforcing least-privilege principles.
* **Encryption standards** â Data encryption at rest and in transit.
* **Configuration management** â Systems hardened consistently.
* **Logging & monitoring** â Security events captured and monitored.

### Operational security scorecard[â](#operational-security-scorecard "Direct link to Operational security scorecard")

Measure preparedness and response capabilities:

* **Incident response readiness** â Runbooks updated and teams trained.
* **Vulnerability management** â Vulnerabilities triaged and remediated within SLA.
* **Access reviews** â Regular audits of permissions and roles.
* **Backup and recovery** â Recovery processes tested regularly.
* **Compliance tracking** â Audit trails maintained and up-to-date.

Start small and iterate

Focus scorecards on practices that teams directly control to ensure quick wins and early adoption.

## 2. Initiatives: driving momentum and engagement[â](#2-initiatives-driving-momentum-and-engagement "Direct link to 2. Initiatives: driving momentum and engagement")

Scorecards define **what good looks like**.<br />**Initiatives** provide the **why and when**, turning goals into campaigns that drive real change.

### Progressive improvement campaigns[â](#progressive-improvement-campaigns "Direct link to Progressive improvement campaigns")

Rather than demanding 100% compliance immediately, focus on specific, achievable improvements.

Examples:

* **Zero critical vulnerabilities** â Eliminate critical vulnerabilities in production systems.
* **Secrets management adoption** â Drive adoption of secure secrets storage practices.
* **Branch protection compliance** â Ensure all production repos enforce branch protection rules.

These campaigns can be **tracked in Port** through:

* Dashboards that visualize campaign progress.
* Automated alerts when thresholds are reached.
* Scorecard metrics tied to completion targets.

### Recognition and gamification[â](#recognition-and-gamification "Direct link to Recognition and gamification")

Security is a team sport.<br /><!-- -->Recognizing and rewarding improvements encourages ongoing participation.

Examples:

* **Leaderboards** â Rank teams by their improvement scores.
* **Achievement badges** â Reward milestones like "90% scorecard compliance.
* **Improvement showcases** â Share success stories at company all-hands.
* **Cross-team learning sessions** â High-performing teams teach others.

## 3. Guardrails and automation: secure by default[â](#3-guardrails-and-automation-secure-by-default "Direct link to 3. Guardrails and automation: secure by default")

Secure practices must be **built into the development workflow** so teams donât rely solely on manual checks.

### Automated policy enforcement[â](#automated-policy-enforcement "Direct link to Automated policy enforcement")

Use Port automations to **enforce policies automatically**, reducing human error:

* Auto-enable **branch protection rules** on new repos ([Setup branch protection rules](/guides/all/setup-branch-protection-rules.md)).
* Block deployments with **critical vulnerabilities** detected by scanners like Trivy or Wiz.
* Prevent commits with **hardcoded secrets**.
* Require **security scan gates** to pass before production deployments.

### Self-service security actions[â](#self-service-security-actions "Direct link to Self-service security actions")

Make security tools and processes easily accessible through **self-service actions**:

* Trigger security scans on-demand.
* Submit vulnerability exception requests.
* Request consultations with security teams.
* Check compliance status before releases.

By making security **self-service and embedded**, teams fix issues faster without waiting on central security bottlenecks.

## Putting security champions into practice[â](#putting-security-champions-into-practice "Direct link to Putting security champions into practice")

### Step 1: identify and empower champions[â](#step-1-identify-and-empower-champions "Direct link to Step 1: identify and empower champions")

* **Selection** â Choose respected developers with influence and interest in security.
* **Time allocation** â Dedicate 10â20% of their role to security initiatives.
* **Training** â Provide certifications and ongoing education.
* **Career growth** â Recognize champion contributions in performance reviews and promotions.

### Step 2: define clear expectations[â](#step-2-define-clear-expectations "Direct link to Step 2: define clear expectations")

Champions should have **specific, measurable responsibilities**:

* Review code for security issues.
* Lead team-level security training.
* Drive scorecard improvements.
* Report vulnerabilities and guide remediation.

Success is tracked through:

* Team scorecard performance.
* Remediation timelines.
* Training engagement rates.

### Step 3: implement scorecards[â](#step-3-implement-scorecards "Direct link to Step 3: implement scorecards")

Start small with key security practices:

* [Track GitLab project maturity](/guides/all/track-gitlab-project-maturity-with-scorecards.md).
* Add service-level scorecards for application, infrastructure, and operational practices.
* Gradually expand to advanced metrics like incident response and compliance readiness.

### Step 4: establish continuous improvement[â](#step-4-establish-continuous-improvement "Direct link to Step 4: establish continuous improvement")

Create a cycle of **review, plan, and improve**:

* **Monthly reviews** â Assess scorecard performance.
* **Quarterly planning** â Launch new improvement campaigns.
* **Retrospectives** â Analyze incidents to identify systemic fixes.
* **Cross-team forums** â Share practices and lessons learned.

caution

**Balance automation and human judgment:**<br /><!-- -->Automation accelerates security, but always provide clear escalation paths for exceptions and edge cases.

## Measuring cultural change[â](#measuring-cultural-change "Direct link to Measuring cultural change")

Track cultural indicators to understand program health:

| Metric                        | What It Shows                                                              |
| ----------------------------- | -------------------------------------------------------------------------- |
| **Proactive issue reporting** | Teams are finding and reporting issues before external discovery.          |
| **Training engagement**       | Developers are participating actively in security education.               |
| **Cross-team collaboration**  | Security knowledge is being shared across teams.                           |
| **Tool adoption**             | Teams are adopting security tools voluntarily, not just out of compliance. |

## Success metrics for security champion programs[â](#success-metrics-for-security-champion-programs "Direct link to Success metrics for security champion programs")

Youâll know the program is working when:

* Champions are seen as **trusted technical leaders** by their peers.
* Teams **compete to improve scorecard scores** instead of seeing compliance as a burden.
* Security improvements happen **organically**, not only through mandates.
* Security incidents are treated as **learning opportunities**, not blame games.
* New developers are mentored on security by their teams, **not just the central security group**.

## Outcomes with Port[â](#outcomes-with-port "Direct link to Outcomes with Port")

Organizations using Port to power their champions program have achieved:

* **Fewer vulnerabilities reaching production** thanks to proactive team ownership.
* **Faster remediation times** due to automated triage and self-service fixes.
* **Reduced deployment delays** by integrating security earlier in workflows.
* **Improved training completion** driven by peer-to-peer champion-led programs.

Security champions bridge the gap between **security strategy** and **engineering execution**.<br /><!-- -->With Port, you can:

* Define clear expectations through scorecards.
* Drive progress with initiatives and campaigns.
* Automate guardrails to make security seamless.
* Measure cultural change with actionable metrics.
