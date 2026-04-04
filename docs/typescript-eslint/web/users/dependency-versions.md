# Source: https://typescript-eslint.io/users/dependency-versions

On this page# Dependency Versions## ESLint[​](#eslint)
The version range of ESLint currently supported is
`^8.57.0 || ^9.0.0`.
We generally support at least the latest two major versions of ESLint; though sometimes we may restrict this if the APIs change too much between major releases.
## Node[​](#node)
The version range of NodeJS currently supported is
`^18.18.0 || ^20.9.0 || >=21.1.0`.
We make an effort to support Active LTS and Maintenance LTS release statuses of Node according to [Node&#x27;s release document](https://github.com/nodejs/release#release-schedule).
Support for specific Current status releases are considered periodically.
## TypeScript[​](#typescript)
The version range of TypeScript currently supported is
`>=4.8.4 <6.0.0`.
We mirror [DefinitelyTyped&#x27;s version support window](https://github.com/DefinitelyTyped/DefinitelyTyped/#support-window) - meaning we only support versions of TypeScript less than 2 years old.
You may find that our tooling works on older TypeScript versions however we provide no guarantees and ***we will not accept issues against unsupported versions***.
We will always endeavor to support the latest stable version of TypeScript.
Sometimes, but not always, changes in TypeScript will not require breaking changes in this project, and so we are able to support more than one version of TypeScript.
In some cases, we may even be able to support additional pre-releases (i.e. betas and release candidates) of TypeScript, but only if doing so does not require us to compromise on support for the latest stable version.
### Supporting New TypeScript Releases[​](#supporting-new-typescript-releases)
With each new TypeScript release we file an issue to track the changes in the new version. The issue should always be pinned, and you can also [find the issues by searching for issues tagged with "New TypeScript Version"](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+label%3A%22New+TypeScript+Version%22+sort%3Acreated-desc). If the issue is open, we do not have official support yet - please be patient.
In terms of what versions we support:
- We do not support the `beta` releases.
- We *generally* do not officially support the `rc` releases.
- We endeavor to support the latest stable TypeScript versions as soon as possible after the release.
Generally we will begin working on supporting the next release when the `rc` version is released.
### Version Warning Logs[​](#version-warning-logs)
Note that our packages have an open `peerDependency` requirement in order to allow for experimentation on newer/beta versions of TypeScript.
If you use a non-supported version of TypeScript, the parser will log a warning to the console.
If you want to disable this warning, you can configure this in your `parserOptions`.
See: [Packages > Parser > `warnOnUnsupportedTypeScriptVersion`](/packages/parser#warnonunsupportedtypescriptversion).
## Dependant Version Upgrades[​](#dependant-version-upgrades)
See [Maintenance > Dependent Version Upgrades](/maintenance/pull-requests/dependency-version-upgrades) for maintenance steps to update these versions.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/users/Dependency_Versions.mdx)- [ESLint](#eslint)- [Node](#node)- [TypeScript](#typescript)[Supporting New TypeScript Releases](#supporting-new-typescript-releases)- [Version Warning Logs](#version-warning-logs)- [Dependant Version Upgrades](#dependant-version-upgrades)