# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/advanced-security/best-practices-for-managing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/advanced-security/best-practices-for-managing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/advanced-security/best-practices-for-managing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/advanced-security/best-practices-for-managing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/advanced-security/best-practices-for-managing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-security/best-practices-for-managing-dependency-risks.md

# Best practices for managing dependency risks

Advanced Security is an add-on that requires a separate subscription to your SonarQube Cloud's [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

Managing dependency risks from SCA is differs from fixing issues in first-party code in a number of ways. Here are some recommendations.

### How dependency risks differ from issues <a href="#how-dependency-risks-differ-from-issues" id="how-dependency-risks-differ-from-issues"></a>

First-party code issues can be fixed entirely by your developers. Even where they may require some internal refactoring, 95% of the time a developer can fix a first-party Sonar code without leaving their codebase, and without having to adjust other code in their application.

That isn’t the case with dependency risks. Dependency risks require updating your open source dependencies to new versions. Moving to a new version of a dependency could require any or all of the following larger changes:

* Adjusting code throughout your application to call new or changed APIs.
* Data migration to new file formats if the new dependency version requires it.
* Moving to entirely an entirely new version of your language runtime (such as Java 21) if the new version of the dependency requires it.

Because of this, the typical dependency risk takes significantly longer to fix than a typical Sonar code issue. Oftentimes development teams will need to schedule explicit technical debt work to perform needed dependency upgrades.

#### Some risks require replacing the entire package <a href="#some-risks-require-replacing-the-entire-package" id="some-risks-require-replacing-the-entire-package"></a>

Open source packages do not change licenses often. If a risk is found where you are using a third-party dependency with a license that is unfit for your organization, in the overwhelming majority of cases, the only available fix is to move to a different dependency entirely. This can be an effort of hours, weeks, or even months in the case of major framework migrations.

#### The initial work can be large <a href="#the-initial-work-can-be-large" id="the-initial-work-can-be-large"></a>

If you have not previously had good dependency management practices, you may be surprised by the number of direct and transitive issues that are discovered for your projects. The scope of burning down this initial backlog of risk is usually larger than can be added to your developers’ plates to be handled in an ad-hoc manner while they do their normal day-to-day work.

Because of the differences in how dependency risks are resolved by developers, Sonar recommends the following practices for successful onboarding of the SCA features of Advanced Security in a large organization.

### Best practices <a href="#best-practices" id="best-practices"></a>

#### Start small <a href="#start-small" id="start-small"></a>

The initial [SCA analyses](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca) will likely create a backlog of issues that need to be triaged and addressed, especially if you had no prior SCA process in place.

* Start with one developer team to refine rollout processes.
* Choose a team committed to refining the process and willing to be a reference.
* The team should have time to spend working through a backlog of initially discovered risks.

#### Determine how you want to handle license compliance <a href="#determine-how-you-want-to-handle-license-compliance" id="determine-how-you-want-to-handle-license-compliance"></a>

The appropriate [license policy](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies) for a piece of software in your organization can depend on:

* what the license of your own code is
* where and how the application is deployed (internal only, network facing, delivered as an artifact to customers)
* how it uses and invokes those dependencies
* your own organization’s level of risk tolerance

There is no one-size-fits-all approach to license compliance. Work with your legal contact to create an appropriate license profile for the applications produced by your first developer team. Create multiple profiles as necessary based on the characteristics of your applications.

#### Only enforce a quality gate on new code <a href="#only-enforce-a-quality-gate-on-new-code" id="only-enforce-a-quality-gate-on-new-code"></a>

To avoid shutting down ongoing development due to a tightly configured [quality gate](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates) when tackling dependency risks, start enforcement by only enforcing quality on [newly added code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code) / on pull requests.

To ensures no new, real, risk is added to your codebase, a good first start is by adding the “Severity of a dependency risk is greater than Info” condition for new code.

#### Begin reducing existing risk outside of a quality gate <a href="#begin-reducing-existing-risk-outside-of-a-quality-gate" id="begin-reducing-existing-risk-outside-of-a-quality-gate"></a>

Once you are no longer bringing in new risks into your codebase, you can then address the backlog of initial risks.

Start by addressing the most severe (any Blocker or High risks). Work with your development team to:

* evaluate how the risk applies to your code. You may be able to mark them as safe as you research how it affects your environment.
* perform any necessary dependency upgrades or implement any workarounds.

Once you have worked with your development team to understand how quickly they can remediate these risks and perform these upgrades, you can then determine how strict of a quality gate is appropriate for overall code.

#### When ready, enforce a quality gate on overall code <a href="#when-ready-enforce-a-quality-gate-on-overall-code" id="when-ready-enforce-a-quality-gate-on-overall-code"></a>

A quality gate on overall code means that *merging of new code will be broken for any new publicly disclosed vulnerability*. Before you enable such a quality gate, you need to ensure that your development team is able to handle these risks when they arise.

Once you are comfortable that your development team is able to quickly remediate new public issues, you can add a quality gate condition such as “Severity of a dependency risk is greater than Medium”

This ensures that production code drops will stop whenever a newly discovered High or Blocker issue, forcing the development team to address it.

#### Track your work <a href="#track-your-work" id="track-your-work"></a>

You can measure your success in dependency risk management by tracking the risk over time in your applications.

Track how over time the number of risks, and their severity, drops across your applications. This shows you how your developers are reducing risk in your organization, and how fast they are eliminating risks as they appear.

#### Expand the circle <a href="#expand-the-circle" id="expand-the-circle"></a>

Once you have gone through these steps with one development team in your organization, you can expand the circle. Take your notes and processes that you have developed, and repeat the steps with another team. Use your first team as a reference to help onboard subsequent teams. As you expand, you will be able to build a culture of dependency management practices throughout your organization.
