# Source: https://typescript-eslint.io/users/releases

On this page# Releases## Latest[​](#latest)
[](https://www.npmjs.com/package/@typescript-eslint/parser)
We release a latest version every Monday at 17:00 UTC (5:00 PM UTC) using the latest commit to `main` at that time. This release is performed automatically by a Github action located in a private repository. This release goes to the standard `latest` tag on npm.
See [Versioning](/users/versioning) for how the version number is calculated.
If there have been no commits that impact public-facing packages then a patch-level release shall be released.
Latest releases shall only ever be "minor" or "patch" releases.
### Release Notes[​](#release-notes)
Every release is documented on the [Github Release page](https://github.com/typescript-eslint/typescript-eslint/releases).
These release notes will list the PRs included in the release.
## Canary[​](#canary)
[](https://www.npmjs.com/package/@typescript-eslint/parser)
We release a canary version for each commit to `main` that passes all required checks. This release is performed automatically by the [`publish_canary_version` step](https://github.com/typescript-eslint/typescript-eslint/blob/5feb2dba9da2bd5e233451b7b0f1c99414b5aef9/.github/workflows/ci.yml#L234-L263). So **you never need to wait for a new stable version to make use of any updates**.
This release goes to the `canary` tag on npm and it is versioned as an incremental canary patch release on top of the current `latest` version. I.e. if the current version is `5.6.1`, then the first canary version will be `5.6.2-alpha.0`, the second `5.6.2-alpha.1`, and so on.
noteThe only exception to the automated publishes described above is when we are in the final phases of creating the next major version of the libraries - e.g. going from `1.x.x` to `2.x.x`.
During these periods, we manually publish `canary` releases until we are happy with the release and promote it to `latest`.
### Installing Canary Versions[​](#installing-canary-versions)
To try out the latest canary versions of typescript-eslint, install `@typescript-eslint/eslint-plugin@canary` and `@typescript-eslint/parser@canary`.
Note that npm may need a `--force` to override version requirements.
- npm- Yarn- pnpm```
npm i @typescript-eslint/eslint-plugin@canary @typescript-eslint/parser@canary --save-dev --force
``````
yarn add @typescript-eslint/eslint-plugin@canary @typescript-eslint/parser@canary --dev --force
``````
pnpm add @typescript-eslint/eslint-plugin@canary @typescript-eslint/parser@canary --save-dev --force
```
## Major Releases[​](#major-releases)
We currently do not have a set schedule around when major releases shall be performed; instead they are done as the need arises.
We keep a backlog of breaking issues as a milestone on GitHub that is named in the form `${major}.0.0`.
When we do do a major release, we release a release candidate version to the `rc-v${major}` tag on npm for each commit to the major branch.
See [Maintenance > Releases](/maintenance/releases#major-releases) for steps to perform a major release.
## Out-of-Band Releases[​](#out-of-band-releases)
We will do releases "out-of-band" (outside the [latest](#latest) schedule) for rare emergencies.
We assess need on a case-by-case basis though generally an emergency is defined as a critical regression specifically introduced in the latest release.
These releases are done manually by a maintainer with the required access privileges.
## Older Versions[​](#older-versions)
Older major versions of typescript-eslint are never maintained or supported.
They may crash with the latest versions of TypeScript.
Using the latest version of typescript-eslint is strongly recommended for getting the latest rule features and fixes, supporting the latest TypeScript features and syntax, and continuous performance and stability improvements.
### Back-Porting Releases[​](#back-porting-releases)
We ***do not*** back port releases to previously released major/minor versions.
We only ever release forward.
### Old Release Documentation[​](#old-release-documentation)
You can find the last version of some older major versions under their dedicated branch deploys:
- v7: [v7--typescript-eslint.netlify.app](https://v7--typescript-eslint.netlify.app)
- v6: [v6--typescript-eslint.netlify.app](https://v6--typescript-eslint.netlify.app)
Note that older documentation pages may contain outdated information and links.
We strongly recommend using the latest version of typescript-eslint and its documentation.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/users/Releases.mdx)- [Latest](#latest)[Release Notes](#release-notes)- [Canary](#canary)[Installing Canary Versions](#installing-canary-versions)- [Major Releases](#major-releases)- [Out-of-Band Releases](#out-of-band-releases)- [Older Versions](#older-versions)[Back-Porting Releases](#back-porting-releases)- [Old Release Documentation](#old-release-documentation)