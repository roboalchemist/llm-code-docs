# Source: https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html

Title: Release Process — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html

Markdown Content:
*   The _release process_ is optimized when using Gitflow branching, as detailed here: [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). It’s important to note that the Ocelot team does not utilize [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow), which, despite being quicker, does not align with the efficiency required for Ocelot’s delivery.

*   Contributors are free to manage their pull requests and feature branches as they see fit to contribute to the ‘[develop](https://github.com/ThreeMammals/Ocelot/tree/develop)’ branch.

*   Maintainers have the autonomy to handle pull requests and merges. Any merges to the ‘[main](https://github.com/ThreeMammals/Ocelot/tree/main)’ branch will trigger the release of packages to GitHub and NuGet.

*   In conclusion, while users should adhere to the guidelines in [Development Process](https://ocelot.readthedocs.io/en/latest/building/devprocess.html), maintainers should follow the procedures outlined in [Release Process](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#).

Stages[¶](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#stages "Link to this heading")
-------------------------------------------------------------------------------------------------------------

Ocelot project follows this _release process_ to incorporate work into NuGet packages:

1.   As a code reviewers, maintainers review pull requests and, if satisfactory, merge them; otherwise, they provide feedback for the contributor to address. Contributors are supported through continuous [Pair Programming](https://www.bing.com/search?q=Pair+Programming) sessions, which include multiple code reviews, resolving code review issues, and problem-solving.

2.   As a release engineers, maintainers must adhere to Semantic Versioning ([SemVer](https://semver.org/)) supported by [GitVersion](https://gitversion.net/docs/). For breaking changes, maintainers should use the correct commit message (containing _“+semver: breaking|major|minor|patch”_) to ensure [GitVersion](https://gitversion.net/docs/) applies the appropriate [SemVer](https://semver.org/) tags. Manual tagging of the Ocelot repository should be avoided to prevent disruptions.

3.   Once a pull request is merged into the ‘[develop](https://github.com/ThreeMammals/Ocelot/tree/develop)’ branch, the [Ocelot NuGet packages](https://www.nuget.org/profiles/ThreeMammals) remain unchanged until a release is initiated. When sufficient work warrants a new release, the ‘[develop](https://github.com/ThreeMammals/Ocelot/tree/develop)’ branch is merged into ‘[main](https://github.com/ThreeMammals/Ocelot/tree/main)’ as a `release/X.Y` branch, triggering the [Release](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml) workflow that builds the code, assigns versions, and pushes artifacts to GitHub and packages to NuGet.

4.   The release engineer, who holds the integration tokens in GitHub [Environments](https://github.com/ThreeMammals/Ocelot/settings/environments), automates each release build using the primary build script, ‘[build.cake](https://github.com/ThreeMammals/Ocelot/blob/main/build.cake)’. Automated or manual [Building](https://ocelot.readthedocs.io/en/latest/building/building.html) can be performed [In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-terminal) or [With CI/CD](https://ocelot.readthedocs.io/en/latest/building/building.html#b-with-ci-cd). The release engineer is also responsible for DevOps within the [ThreeMammals](https://github.com/ThreeMammals) organization, across all (sub)repositories, supporting the primary build script, and scripting for other repositories.

5.   The release engineer drafts the `ReleaseNotes.md` template file, informing the community about key aspects of the release, including new or updated features, bug fixes, documentation updates, breaking changes, contributor acknowledgments, version upgrade guidelines, and more.

6.   The final stage of the _release process_ involves returning to GitHub to close the current [milestone](https://github.com/ThreeMammals/Ocelot/milestones), ensuring that:

    *   All issues within the [milestone](https://github.com/ThreeMammals/Ocelot/milestones) are closed; any remaining work from open issues should be transferred to the next [milestone](https://github.com/ThreeMammals/Ocelot/milestones).

    *   All pull requests associated with the [milestone](https://github.com/ThreeMammals/Ocelot/milestones) are either closed or reassigned to the upcoming release [milestone](https://github.com/ThreeMammals/Ocelot/milestones).

    *   Release Notes are published on GitHub [releases](https://github.com/ThreeMammals/Ocelot/releases), with an additional review of the text.

    *   The published release is designated as the latest, provided the corresponding [Ocelot NuGet packages](https://www.nuget.org/profiles/ThreeMammals) have been successfully uploaded to the [ThreeMammals](https://www.nuget.org/profiles/ThreeMammals) account.

7.   Optional support for the major version `X.Y.0` should be available in cases such as Microsoft official patches and critical Ocelot defects of that major version. Maintainers should release patched versions `X.Y.1-z` as hot-fix patch versions.

Notes[¶](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#notes "Link to this heading")
-----------------------------------------------------------------------------------------------------------

**Note 1**: All NuGet package builds and releases are conducted through the [GitHub Actions](https://docs.github.com/en/actions) CI/CD provider. For details, refer to the dedicated [Actions](https://github.com/ThreeMammals/Ocelot/actions) dashboard, which should be used to monitor the current status of three workflows.

**Note 2**: Currently, only [Tom Pallister](https://github.com/TomPallister), [Raman Maksimchuk](https://github.com/raman-m), the owners—along with the [Ocelot Team](https://github.com/orgs/ThreeMammals/teams) maintainers—have the authority to merge releases into the ‘[main](https://github.com/ThreeMammals/Ocelot/tree/main)’ branch of the Ocelot repository. This policy ensures that final [Quality Gates](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#quality-gates) are in place. The maintainers’ primary focus during the final merge is to identify any security issues, as outlined in Stage 7 of the process.

Quality Gates[¶](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#quality-gates "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

**Gate 1**: Static code analysis. The Ocelot repository includes the following integrated style analyzers:

*   In-built IDE (.NET SDK): The [code analysis rule set](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20%3CCodeAnalysisRuleSet%3E&type=code) is defined in the ‘[codeanalysis.ruleset](https://github.com/ThreeMammals/Ocelot/blob/main/codeanalysis.ruleset)’ file, with configuration instructions available [here](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-options). For comprehensive documentation, refer to the following article:

    *   Microsoft Learn: [Overview of .NET source code analysis](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview?tabs=net-9)

*   [StyleCop.Analyzers](https://www.nuget.org/packages/StyleCop.Analyzers): The package is somewhat outdated with slow support, but Ocelot projects still [reference](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20StyleCop.Analyzers&type=code) it because it has remained functional since 2015/16 as an older style analyzer. The Ocelot team plans to replace this library with a more advanced tool in upcoming releases.
