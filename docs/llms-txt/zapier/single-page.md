# Source: https://docs.zapier.com/platform/news/single-page.md

# Platform News (Single Page)

> Recent changelogs and tips on a single page

{/* To add an entry here, write a post in platform/news/<year> and run `pnpm run render-news` */}

## What's changed in v18.0.6

*Released: 2025-12-24*

The `zapier build` command was harcoded to use `npm install`. As alternate package managers gain adoption, the `zapier build` command will respect your app's package manager of choice.
It does this by checking the `packageManager` on the package.json file. If it is not defined, it will look for any relevant lock files. If still, none is defined, then will fallback to `npm`.

If you are familiar with using `zapier build` with the flag `--skip-npm-install`, this flag has been renamed to `--skip-dep-install`, but will continue to still work as an alias. In the future, we will remove the `--skip-npm-install` flag.

**cli**

* 💅 CLI build respects the integration's package manager ([#1216](https://github.com/zapier/zapier-platform/pull/1216))

**core**

None!

**schema**

None!

**misc**

* 🔨 Bump tmp from 0.2.4 to 0.2.5 ([#1207](https://github.com/zapier/zapier-platform/pull/1207))
* 🔨 Bump form-data from 4.0.4 to 4.0.5 ([#1208](https://github.com/zapier/zapier-platform/pull/1208))

***

## What's changed in v18.0.5

*Released: 2025-12-10*

<Info>We're releasing v18.0.5, skipping comprimised versions v18.0.2, v18.0.3, and v18.0.4, due to the prior [security incident](/platform/news/2025/npm-package-sec-inc).</Info>

This release fixes a potential security vulnerability in the `build` command related to zip file decompression.

**cli**

* 🐛 Remove problematic decompress-tar dependency ([#1202](https://github.com/zapier/zapier-platform/pull/1202))

**core**

None!

**schema**

None!

**misc**

* 🔨 Switch to pnpm as package manager and task runner ([#1204](https://github.com/zapier/zapier-platform/pull/1204))

***

## Incident: Unauthorized Access to Zapier NPM Packages

*Released: 2025-11-24*

**Unauthorized Access to Zapier npm Packages**

**Note: No action is needed from Zapier users**, only from Zapier developers using one of the NPM package versions listed [on this page](/platform/build-cli/inc-547). See that link for detailed mitigation recommendations.

All Zapier products are operating as expected and there is no indication of data loss or leak.

Please [see this link](https://status.zapier.com/incidents/01KAV9DDHMYT7R6MFHSB8C09E3#updates) for the most up-to-date information.

***

## What's changed in v18.0.1

*Released: 2025-11-05*

This release addresses an npx resolution issue introduced in v18.0.0 and fixes TypeScript typing for nested input fields when working with line items.

**cli**

* 🐛 Fix npx resolution issue with dual binary entries ([#1191](https://github.com/zapier/zapier-platform/pull/1191))

**core**

* 🐛 Fix children input types when line items are present ([#1188](https://github.com/zapier/zapier-platform/pull/1188))

**schema**

None!

**misc**

None!

***

## What's changed in v18.0.0

*Released: 2025-10-30*

Version 18.0.0 is a **BREAKING CHANGE** release that contains several important upgrades and changes. Here is a brief breakdown of the main changes (**❗ denotes a breaking change**):

**❗ Node.js 22 Support**

Zapier Platform v18 runs on Node.js 22 runtime. This is a breaking change as it may affect compatibility with older Node.js versions and dependencies.

**❗ Schema Changes**

The `skipCleanArrayInputData` experimental flag has been replaced with `cleanInputData`. This provides more consistent data cleaning behavior across the platform. This change is breaking **only if** you're using `skipCleanArrayInputData`.
See [cleanInputData flag documentation](/platform/build-cli/empty-values-in-input-data) for more details on how to configure this behavior.

**❗ New Throttling Middleware**

A new `throwForThrottling` middleware has been added to prevent `afterResponse` middleware from suppressing 429 (throttling) responses. This ensures proper handling of rate limiting scenarios. This change is breaking **if** you want to handle 429 responses in your `afterResponse`. See [v18.x and above: the built-in `throwForThrottling` middleware](/platform/build-cli/making-http-requests#v18-x-and-above%3A-the-built-in-throwforthrottling-middleware) for how to handle 429s yourself.

**New Executable Name `zapier-platform`**

The CLI now includes a new executable name `zapier-platform` while deprecating the old `zapier` command. Both will work for now, but `zapier-platform` is the recommended command going forward.

***

Apart from these major changes, here are the detailed release notes for this release (**note that ❗ denotes a breaking change**):

**cli**

* 🎉 Add executable name `zapier-platform` and deprecate `zapier` ([#1181](https://github.com/zapier/zapier-platform/pull/1181))
* 🔨 Update outdated dependencies with security vulnerabilities ([#1111](https://github.com/zapier/zapier-platform/pull/1111))
* 🔨 Apply prettier formatting to generated auth files since gen.fs.write bypasses transform streams
* 🔨 Add ESM wrapper improvements for better module support

**core**

* ❗ Add Node.js 22 support ([#1078](https://github.com/zapier/zapier-platform/pull/1078))
* 🎉 Add `throwForThrottling` middleware with backward-compatible default behavior ([#1151](https://github.com/zapier/zapier-platform/pull/1151))
* 🐛 Add better error message for 413 responses ([#1110](https://github.com/zapier/zapier-platform/pull/1110))

**schema**

* ❗ Replace `skipCleanArrayInputData` with `cleanInputData` ([#1183](https://github.com/zapier/zapier-platform/pull/1183))
* 🔨 Add global `cleanInputData` flag for consistent data cleaning behavior

**misc**

* ❗ Major dependency updates across all packages ([#1079](https://github.com/zapier/zapier-platform/pull/1079))
* 🔨 Update CI configuration for Node.js 22 support
* 🔨 Pin exact xmldom version for security

***

## What's changed in v17.9.1

*Released: 2025-10-28*

This release addresses a bug in the `zapier push` command and includes dependency updates.

**cli**

* 🐛 Fix issue where zapier push fail if the app wasn't built already (may have affected ESM builds) ([#1187](https://github.com/zapier/zapier-platform/pull/1187))

**core**

None!

**schema**

None!

**misc**

* 🔨 Bump vite from 6.3.6 to 6.4.1 ([#1185](https://github.com/zapier/zapier-platform/pull/1185))

***

## Self-serve static IP for private integrations

*Released: 2025-10-21*

**Self-serve static IP for private integrations**

* 🎉 [Static IP](https://docs.zapier.com/platform/build/static-ip) can now be enabled by team members for private integrations:
  * **Platform UI toggle**: Navigate to the Settings tab on the Advanced page to enable static IP addresses for your private integration without contacting support.
  * **Published integrations**: Continue to contact Zapier Support to enable static IP for published integrations.

***

## Labeled Versions now available in CLI and Platform UI

*Released: 2025-10-21*

**Labeled Versions**

* 🎉 [Labeled Versions](https://docs.zapier.com/platform/manage/labeled-versions) are now publicly available!
  * Versions like `2.0.0-beta` can be used for testing and avoiding version collisions during parallel development
  * More flexible "snapshot" versions like `0.0.0-my-feature` can be used to push integration updates without committing to a semantic version number

***

## What's changed in v17.9.0

*Released: 2025-10-20*

This release fixes an issue with validation for labeled versions, and improves failures on `zapier env:set`.

**cli**

* 🐛 Validate snapshot labels for 12 chars instead of 18 ([#1182](https://github.com/zapier/zapier-platform/pull/1182))
* 💅 Display failure reasons for env:set ([#1180](https://github.com/zapier/zapier-platform/pull/1180))

**core**

None!

**schema**

None!

***

## What's changed in v17.8.0

*Released: 2025-10-07*

Aside from some clean up work, this release adds support for natural snapshots to `zapier push`. This is currently only supported internally but look out for a public release soon!

**cli**

* 💅 `zapier push` supports natural snapshots ([#1172](https://github.com/zapier/zapier-platform/pull/1172))
* 🐛 Address `punycode` deprecation warning by removing `node-fetch` ([#1171](https://github.com/zapier/zapier-platform/pull/1171))
* 📜 Fix incorrect docs in `zapier migrate` ([#1169](https://github.com/zapier/zapier-platform/pull/1169))

**core**

* 🐛 Allow null and undefined values for `page_token` in `SearchResult` ([#1168](https://github.com/zapier/zapier-platform/pull/1168))
* 🐛 Allow undefined value for `paging_token` ([#1166](https://github.com/zapier/zapier-platform/pull/1166))

**misc**

* 📜 Direct developers to Platform News ([#1174](https://github.com/zapier/zapier-platform/pull/1174))

***

## Migration UI now supports individual and organization-level migrations

*Released: 2025-10-02*

**Migration via the Platform UI**

* 🎉 [Email-based migration](https://docs.zapier.com/platform/manage/migrate#migrate-users-to-new-version-with-platform-ui) now supports two scopes:
  * **Individual**: Migrates only private Zaps under the user's individual account (equivalent to the `--user` flag of the `zapier migrate` CLI command)
  * **Organization**: Migrates all Zaps including shared resources across organization accounts (equivalent to the `--account` flag of the `zapier migrate` CLI command)

***

## What's changed in v17.7.2

*Released: 2025-09-17*

**cli**

* 🐛 Allows deleting old non-semver versions and blocks pushes to non-semver versions ([#1160](https://github.com/zapier/zapier-platform/pull/1160))
* 🐛 Integration check displays failure icon if errors are present ([#1159](https://github.com/zapier/zapier-platform/pull/1159))

**core**

* 🐛 Adds paging\_token to bundle.meta types ([#1157](https://github.com/zapier/zapier-platform/pull/1157))

**misc**

* 🔨 Bump vite from 6.3.5 to 6.3.6 ([#1156](https://github.com/zapier/zapier-platform/pull/1156))
* 🔨 Improve types ([#1162](https://github.com/zapier/zapier-platform/pull/1162), [#1164](https://github.com/zapier/zapier-platform/pull/1164), [#1165](https://github.com/zapier/zapier-platform/pull/1165))

***

## What's changed in v17.7.1

*Released: 2025-09-10*

**cli**

* 🐛 Fix `zapier scaffold` failing when app object contains spread elements ([#1115](https://github.com/zapier/zapier-platform/pull/1115))
* 🐛 Fix `zapier invoke auth` may append to last line without a newline ([#1138](https://github.com/zapier/zapier-platform/pull/1138))
* 🐛 Fix `zapier scaffold` to use `.js` extension for TS imports ([#1123](https://github.com/zapier/zapier-platform/pull/1123))
* 🐛 Fix `zapier scaffold` to handle shorthand property syntax ([#1125](https://github.com/zapier/zapier-platform/pull/1125))
* 💅 `zapier validate` now runs `_zapier-build` before validation by default ([#1130](https://github.com/zapier/zapier-platform/pull/1130))
* 💅 Add `dev` script to `package.json` of typescript templates generated by `zapier init` ([#1128](https://github.com/zapier/zapier-platform/pull/1128))
* 💅 Improve `zapier init` to list only templates that support selected module and language ([#1146](https://github.com/zapier/zapier-platform/pull/1146))

**core**

* 🐛 Censor sensitive info in `ResponseError` ([#1147](https://github.com/zapier/zapier-platform/pull/1147))

**schema**

* 🐛 Fix `InputFieldGroupsSchema` to have its properties displayed ([#1143](https://github.com/zapier/zapier-platform/pull/1143))
* 🧪 Allow to skip cleaning arrays in `inputData` via `skipCleanArrayInputData` ([#1153](https://github.com/zapier/zapier-platform/pull/1153))
* 🔨 Support version with label (ongoing work) ([#1093](https://github.com/zapier/zapier-platform/pull/1093))

***

## No more manual handling of 4xx errors in refreshAccessToken

*Effective: 2025-09-08*

We made a change to how we handle error responses when refreshing OAuth2 access tokens.

**Old behavior**

When an app gives an error response (status code 4xx or 5xx) while refreshing the OAuth2 access token, Zapier keeps retrying the Zap step indefinitely or until it hits a certain limit, depending on the user's settings.

**New behavior**

When an app encounter a 4xx error response (except for the ones listed below) while refreshing the access token, Zapier will mark the connect as stale, and send an email telling the user to reconnect.

Exceptions: The following 4xx errors often indicate a temporary issue so they still have the same behavior as before:

* 408 (Request Timeout)
* 409 (Conflict)
* 423 (Locked)
* 425 (Too Early)
* 429 (Too Many Requests)

This is how Zapier handles a stale connection:

* If the stale connection is used by a trigger step, the trigger polling system will skip polling when the scheduled time comes.
* If the stale connection is used by an action step, the Zap run will be put on hold until the user reconnects and replays the run.

**What does it mean to you?**

You don't need to handle 4xx error responses in `refreshAccessToken` anymore. For example, you might have been catching 4xx errors in `refreshAccessToken` by enabling `skipThrowForStatus` and throwing `ExpiredAuthError`:

```js  theme={null}
const refreshAccessToken = async (z, bundle) => {
  const response = await z.request({
    url: "https://example.com/token/refresh",
    method: "POST",
    body: {
      refresh_token: bundle.authData.refresh_token,
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      grant_type: "refresh_token",
    },
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    skipThrowForStatus: true,
  });

  if (response.status >= 400 && response.status < 500) {
    throw new z.errors.ExpiredAuthError(
      "Authentication issue. Please reconnect.",
    );
  }

  return response.data;
};
```

This is no longer necessary. Now you can simplify your code as follows and let the platform handle it:

```js  theme={null}
const refreshAccessToken = async (z, bundle) => {
  const response = await z.request({
    url: "https://example.com/token/refresh",
    method: "POST",
    body: {
      refresh_token: bundle.authData.refresh_token,
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      grant_type: "refresh_token",
    },
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response.data;
};
```

No need to upgrade zapier-platform-core; this change is implemented in the Zapier backend.

***

## What's changed in v17.7.0

*Released: 2025-08-22*

**cli**

* 🐛 Fix `zapier pull` error "listFiles is not a function" ([#1113](https://github.com/zapier/zapier-platform/pull/1113))
* 🐛 Fix `zapier invoke auth` writing object values to `.env` as `[object Object]` ([#1107](https://github.com/zapier/zapier-platform/pull/1107))
* 💅 Add logic to `zapier build` to handle the case where the app directory has symlinks to files on a different drive ([#1106](https://github.com/zapier/zapier-platform/pull/1106))
* 🎉 `zapier invoke` supports testing Search Pagination with a `paging_token` flag ([#1082](https://github.com/zapier/zapier-platform/pull/1082))

**core**

* 🎉 Foundational support for Search Pagination ([#1082](https://github.com/zapier/zapier-platform/pull/1082))

**schema**

* 🎉 Schema support for Search Pagination ([#1082](https://github.com/zapier/zapier-platform/pull/1082))

**misc**

* 💅 Enable Windows in Github Actions CI ([#1106](https://github.com/zapier/zapier-platform/pull/1106))
* 💅 Add Claude, Copilot, and Cursor instructions/rules ([#1107](https://github.com/zapier/zapier-platform/pull/1107))
* 🔨 Bump `tmp` from 0.2.3 to 0.2.4 ([#1100](https://github.com/zapier/zapier-platform/pull/1100))
* 🔨 Bump `sha.js` from 2.4.11 to 2.4.12 ([#1116](https://github.com/zapier/zapier-platform/pull/1116))

***

## What's changed in v17.6.0

*Released: 2025-08-11*

**cli**

* 💅 Add user and account filters to canary ([#1066](https://github.com/zapier/zapier-platform/pull/1066))

**core**

* 💅 Export `console` from zapier-platform-core ([#1077](https://github.com/zapier/zapier-platform/pull/1077), [#1102](https://github.com/zapier/zapier-platform/pull/1102))
* 🐛 Allow safe `authData` keys to be logged uncensored ([#1097](https://github.com/zapier/zapier-platform/pull/1097))

**schema**

None!

***

## What's changed in v17.5.0

*Released: 2025-07-30*

**cli**

* 🐛 Fix missing `bundle.inputDataRaw` in invoke command ([#1072](https://github.com/zapier/zapier-platform/pull/1072))
* 🐛 Fix error `'No loader is configured for ".node" files'` on `zapier build` ([#1094](https://github.com/zapier/zapier-platform/pull/1094))
* 🔨 Refactor `zapier init` to move auth befores/afters into `middleware.js` instead of `authentication.js` ([#1073](https://github.com/zapier/zapier-platform/pull/1073))

**core**

* 💅 Export errors from `zapier-platform-core` ([#1075](https://github.com/zapier/zapier-platform/pull/1075))
* 🔨 Update `form-data` from `4.0.1` to `4.0.4` ([#1096](https://github.com/zapier/zapier-platform/pull/1096))

**schema**

* 💅 Expanded `AuthFieldSchema` with additional field types:
  * Added support for the `integer` type ([#1095](https://github.com/zapier/zapier-platform/pull/1095)).
  * Added support for the `text` type ([#1098](https://github.com/zapier/zapier-platform/pull/1098)).

***

## What's changed in v17.4.0

*Released: 2025-07-23*

**cli**

* 🐛 Fix regression bugs with `zapier build`, where it can fail with "'The "path" argument must be of type string'" when [dirent.parentPath](https://nodejs.org/docs/latest/api/fs.html#direntparentpath) property is missing ([#1087](https://github.com/zapier/zapier-platform/pull/1087))
* 🐛 Fixes a regression where `zapier build --skip-npm-install` fails when an app has a linked dependencies in its `node_modules` ([#1089](https://github.com/zapier/zapier-platform/pull/1089))
* 🐛 Remove empty array at the end of `zapier versions -f json` ([#1086](https://github.com/zapier/zapier-platform/pull/1086))
* 💅 Add additional Typescript auth options to `zapier init` ([#1067](https://github.com/zapier/zapier-platform/pull/1067))

**core**

* 💅 Support compression when stashing large input bundles ([#1085](https://github.com/zapier/zapier-platform/pull/1085))

**schema**

None!

***

## What's changed in v17.3.1

*Released: 2025-07-17*

**cli**

* 🐛 Fix regression bugs with `zapier build --skip-npm-install`, where:
  * it can miss local packages files when building in a Lerna monorepo ([#1068](https://github.com/zapier/zapier-platform/pull/1068))
  * it can fail with "Configuration property ... is not defined" when [config](https://www.npmjs.com/package/config) package is used ([#1071](https://github.com/zapier/zapier-platform/pull/1071))
* 💅 Improve some error messages in `zapier build` ([#1070](https://github.com/zapier/zapier-platform/pull/1070))

**core**

* 💅 Improve the error message when the app module fails to import ([#1070](https://github.com/zapier/zapier-platform/pull/1070))

**schema**

None!

***

## What's changed in v17.3.0

*Released: 2025-07-01*

This release introduces two major improvements: `zapier build` and input field grouping.

The `zapier build` command has been revamped to:

* Better support npm/yarn/pnpm workspaces
* Run faster when the `--skip-npm-install` flag is enabled
* Test the build.zip file to verify all load-time dependencies are included (not applicable on Windows)

Input Field Grouping:

* Grouping support, intended for visual purpose in products, has been added to the input fields.

**cli**

* 💅 `zapier build` supports npm/yarn/pnpm workspaces and runs faster ([#1052](https://github.com/zapier/zapier-platform/pull/1052))
* 🐛 Fix a bug where `zapier build` can select the wrong entry point of a dependency ([#1052](https://github.com/zapier/zapier-platform/pull/1052) - [c004298](https://github.com/zapier/zapier-platform/pull/1052/commits/c004298a1b61b7de777f3c8222949c7d38d8826f))
* :scroll: Update docs for new days before deprecation and sending emails ([#1056](https://github.com/zapier/zapier-platform/pull/1056))

**core**

* 🐛 Fix a bug where Fetch logger crashes when response doesn't have content-type ([#1062](https://github.com/zapier/zapier-platform/pull/1062))
* 🐛 Fix a bug where `text/xml` response content should be logged ([#1058](https://github.com/zapier/zapier-platform/pull/1058))
* 💅 Typing update: allow overriding `id` requirement in polling triggers ([#1059](https://github.com/zapier/zapier-platform/pull/1059))
* 💅 Typing update: allow test bundles to be recursively partial ([#1057](https://github.com/zapier/zapier-platform/pull/1057))
* 🔨 Bump fernet from 0.4.0 to 0.3.3 (latest) ([#1055](https://github.com/zapier/zapier-platform/pull/1055))

**schema**

* 🎉 Input fields now support visual grouping through the "group" property of the `/PlainInputFieldSchema` and the new `/InputFieldGroupsSchema` ([#1061](https://github.com/zapier/zapier-platform/pull/1061))

***

Looking for older news? [2025](/platform/news/2025), and [old changelogs prior to v17](https://github.com/zapier/zapier-platform/tree/main/changelog)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.zapier.com/llms.txt