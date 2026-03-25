# Source: https://vincit.github.io/objection.js/release-notes/changelog.html

Title: Changelog | Objection.js

URL Source: https://vincit.github.io/objection.js/release-notes/changelog.html

Markdown Content:
[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-5) 3.1.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new) What's new

*   Types: Fix generic static `this`[#2533(opens new window)](https://github.com/Vincit/objection.js/pull/2533)
*   Types: Add `fromRaw` to `FromSelector regex [#2628(opens new window)](https://github.com/Vincit/objection.js/issues/2628)
*   Types: Fix argument types of `onConflict()`[#2635(opens new window)](https://github.com/Vincit/objection.js/pull/2635)
*   Types: Make `trx` optional for `Model.transaction(trx, cb)`[#2694(opens new window)](https://github.com/Vincit/objection.js/pull/2694)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-4) 3.1.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-2) What's new

*   Fix `upsertGraph()``$beforeUpdate()` calls on empty relates [#2605(opens new window)](https://github.com/Vincit/objection.js/issues/2605)
*   Don't call `onError()` with internal exceptions [#2603(opens new window)](https://github.com/Vincit/objection.js/issues/2603)
*   Remove docs and typings for nonexistent `$pick()`
*   Make `$omitFromJson()` + `$omitFromDatabaseJson()` compatible with old `$omit()` syntax

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-3) 3.1.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-3) What's new

*   Revert generic constructor type change [#2531(opens new window)](https://github.com/Vincit/objection.js/issues/2531), [#2399(opens new window)](https://github.com/Vincit/objection.js/pull/2399)

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-4) What's new

*   Patch Validator: Prevent recursion on inner properties [#2520(opens new window)](https://github.com/Vincit/objection.js/pull/2520)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-2) 3.1.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-5) What's new

*   Patch Validator: Prevent recursion on inner properties [#2520(opens new window)](https://github.com/Vincit/objection.js/pull/2520)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-1) 3.1.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-6) What's new

*   Only add Ajv formats if they weren't added in user-land already [#2482(opens new window)](https://github.com/Vincit/objection.js/pull/2482)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-1-0) 3.1.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-7) What's new

*   Support `$beforeUpdate()` mutations in `upsertGraph()`[#2233(opens new window)](https://github.com/Vincit/objection.js/issues/2233)
*   Remove deprecated `$afterGet()` hook [#2477(opens new window)](https://github.com/Vincit/objection.js/pull/2477)
*   Drop support for Node v12 [#2478(opens new window)](https://github.com/Vincit/objection.js/pull/2478)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-5) 3.0.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-8) What's new

*   Fixes [#2183(opens new window)](https://github.com/Vincit/objection.js/pull/2183)
*   Fixes [#2257(opens new window)](https://github.com/Vincit/objection.js/pull/2257)
*   Fixes [#2276(opens new window)](https://github.com/Vincit/objection.js/pull/2276)
*   Fixes [#2453(opens new window)](https://github.com/Vincit/objection.js/pull/2453)
*   Fixes [#2476(opens new window)](https://github.com/Vincit/objection.js/pull/2476)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-4) 3.0.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-9) What's new

*   Fixes [#2447(opens new window)](https://github.com/Vincit/objection.js/issues/2447)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-3) 3.0.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-10) What's new

*   Fixes [#1673(opens new window)](https://github.com/Vincit/objection.js/issues/1673)
*   Fixes [#1957(opens new window)](https://github.com/Vincit/objection.js/issues/1957)
*   Fixes [#2105(opens new window)](https://github.com/Vincit/objection.js/issues/2105)
*   Fixes [#2132(opens new window)](https://github.com/Vincit/objection.js/issues/2132)
*   Fixes [#2251(opens new window)](https://github.com/Vincit/objection.js/issues/2251)
*   Fixes [#2262(opens new window)](https://github.com/Vincit/objection.js/issues/2262)
*   Fixes [#2271(opens new window)](https://github.com/Vincit/objection.js/issues/2271)
*   Fixes [#2277(opens new window)](https://github.com/Vincit/objection.js/issues/2277)
*   Fixes [#2308(opens new window)](https://github.com/Vincit/objection.js/pull/2308)
*   Fixes [#2311(opens new window)](https://github.com/Vincit/objection.js/issues/2311)
*   Fixes [#2311(opens new window)](https://github.com/Vincit/objection.js/pull/2311)
*   Fixes [#2311(opens new window)](https://github.com/Vincit/objection.js/pull/2311)
*   Fixes [#2332(opens new window)](https://github.com/Vincit/objection.js/issues/2332)
*   Fixes [#2337(opens new window)](https://github.com/Vincit/objection.js/issues/2337)
*   Fixes [#2372(opens new window)](https://github.com/Vincit/objection.js/pull/2372)
*   Fixes [#2379(opens new window)](https://github.com/Vincit/objection.js/pull/2379)
*   Fixes [#2383(opens new window)](https://github.com/Vincit/objection.js/pull/2383)
*   Fixes [#2399(opens new window)](https://github.com/Vincit/objection.js/pull/2399)
*   Fixes [#2404(opens new window)](https://github.com/Vincit/objection.js/pull/2404)
*   Fixes [#2405(opens new window)](https://github.com/Vincit/objection.js/pull/2405)
*   Fixes [#2408(opens new window)](https://github.com/Vincit/objection.js/pull/2408)
*   Fixes [#2409(opens new window)](https://github.com/Vincit/objection.js/pull/2409)
*   Fixes [#2423(opens new window)](https://github.com/Vincit/objection.js/pull/2423)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-2) 3.0.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-11) What's new

*   Fixes [#1356(opens new window)](https://github.com/Vincit/objection.js/issues/1356)
*   Fixes [#1957(opens new window)](https://github.com/Vincit/objection.js/issues/1957)
*   Fixes [#2192(opens new window)](https://github.com/Vincit/objection.js/issues/2192)
*   Fixes [#2247(opens new window)](https://github.com/Vincit/objection.js/pull/2247)
*   Fixes [#2307(opens new window)](https://github.com/Vincit/objection.js/pull/2307)
*   Fixes [#2308(opens new window)](https://github.com/Vincit/objection.js/pull/2308)
*   Fixes [#2311(opens new window)](https://github.com/Vincit/objection.js/pull/2311)
*   Fixes [#2323(opens new window)](https://github.com/Vincit/objection.js/pull/2323)
*   Fixes [#2337(opens new window)](https://github.com/Vincit/objection.js/issues/2337)
*   Fixes [#2362(opens new window)](https://github.com/Vincit/objection.js/pull/2362)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-1) 3.0.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-12) What's new

*   Fixes [#2123(opens new window)](https://github.com/Vincit/objection.js/issues/2123)
*   Fixes [#2150(opens new window)](https://github.com/Vincit/objection.js/issues/2150)
*   Fixes [#2179(opens new window)](https://github.com/Vincit/objection.js/pull/2179)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_3-0-0) 3.0.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-13) What's new

*   Fixes [#1986(opens new window)](https://github.com/Vincit/objection.js/issues/1986)
*   Fixes [#1987(opens new window)](https://github.com/Vincit/objection.js/issues/1987)
*   Fixes [#1954(opens new window)](https://github.com/Vincit/objection.js/issues/1954)
*   Fixes [#1993(opens new window)](https://github.com/Vincit/objection.js/issues/1993)
*   Fixes [#1688(opens new window)](https://github.com/Vincit/objection.js/issues/1688)
*   Fixes [#1651(opens new window)](https://github.com/Vincit/objection.js/issues/1651)
*   Fixes [#2135(opens new window)](https://github.com/Vincit/objection.js/issues/2135)
*   Fixes [#1936(opens new window)](https://github.com/Vincit/objection.js/issues/1936)
*   Fixes [#1905(opens new window)](https://github.com/Vincit/objection.js/issues/1905)
*   Fixes [#1997(opens new window)](https://github.com/Vincit/objection.js/issues/1997)
*   Fixes [#2024(opens new window)](https://github.com/Vincit/objection.js/issues/2024)

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes) Breaking changes

See the [migration guide](https://vincit.github.io/objection.js/release-notes/migration.html).

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-10) 2.2.10
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-14) What's new

*   Add `modelClass` property for `ValidationError` and `NotFoundError`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-9) 2.2.9
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-15) What's new

*   Add `noWait` query builder method.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-8) 2.2.8
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-16) What's new

*   Fixes [#1982(opens new window)](https://github.com/Vincit/objection.js/issues/1982)
*   Fixes [#1983(opens new window)](https://github.com/Vincit/objection.js/issues/1983)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-7) 2.2.7
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-17) What's new

*   `QueryBuilder.castTo` can now be used to cast query results to any typescript type.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-6) 2.2.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-18) What's new

*   Fixes [#1964(opens new window)](https://github.com/Vincit/objection.js/issues/1964)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-5) 2.2.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-19) What's new

*   Fixes [#1855(opens new window)](https://github.com/Vincit/objection.js/issues/1855)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-4) 2.2.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-20) What's new

*   Add support for onConflict, merge and ignore knex methods.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-2) 2.2.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-21) What's new

*   [#1722(opens new window)](https://github.com/Vincit/objection.js/issues/1722)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-1) 2.2.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-22) What's new

*   Fixes [#1757(opens new window)](https://github.com/Vincit/objection.js/issues/1757)
*   Fixes [#1729(opens new window)](https://github.com/Vincit/objection.js/issues/1729)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-2-0) 2.2.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-23) What's new

*   Fixes [#1770(opens new window)](https://github.com/Vincit/objection.js/issues/1770)
*   Fixes [#1699(opens new window)](https://github.com/Vincit/objection.js/issues/1699)
*   Fixes [#1703(opens new window)](https://github.com/Vincit/objection.js/issues/1703)
*   Fixes [#1675(opens new window)](https://github.com/Vincit/objection.js/issues/1675)
*   Fixes [#1708(opens new window)](https://github.com/Vincit/objection.js/issues/1708)
*   Fixes [#1743(opens new window)](https://github.com/Vincit/objection.js/issues/1743)
*   Fixes [#1731(opens new window)](https://github.com/Vincit/objection.js/issues/1731)
*   Fixes [#1761(opens new window)](https://github.com/Vincit/objection.js/issues/1761)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-1-4) 2.1.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-24) What's new

*   Fixes [#1750(opens new window)](https://github.com/Vincit/objection.js/issues/1750)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-1-3) 2.1.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-25) What's new

*   Add `underscoreBetweenUppercaseLetters` option for snake case mappers. [#1676(opens new window)](https://github.com/Vincit/objection.js/issues/1676)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-1-2) 2.1.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-26) What's new

*   Fix `startTransaction` typings.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-1-1) 2.1.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-27) What's new

*   Fixes [#1489(opens new window)](https://github.com/Vincit/objection.js/issues/1489)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-1-0) 2.1.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-28) What's new

*   Fixes [#1638(opens new window)](https://github.com/Vincit/objection.js/issues/1638)
*   Fixes [#1636(opens new window)](https://github.com/Vincit/objection.js/issues/1636)
*   Fixes [#1615(opens new window)](https://github.com/Vincit/objection.js/issues/1615)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#changelog-2) Changelog
---------------------------------------------------------------------------------------------

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-10) 2.0.10
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-29) What's new

*   Fixes [#1630(opens new window)](https://github.com/Vincit/objection.js/issues/1630)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-9) 2.0.9
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-30) What's new

*   Fixes [#1606(opens new window)](https://github.com/Vincit/objection.js/issues/1606)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-8) 2.0.8
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-31) What's new

*   Fixes [#1627(opens new window)](https://github.com/Vincit/objection.js/issues/1627)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-7) 2.0.7
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-32) What's new

*   Fixes [#1607(opens new window)](https://github.com/Vincit/objection.js/issues/1607)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-6) 2.0.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-33) What's new

*   Fixes [#1603(opens new window)](https://github.com/Vincit/objection.js/issues/1603)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-5) 2.0.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-34) What's new

*   Fixes `upsertGraph` bug where composite keys were not selected correctly. See the fix [here(opens new window)](https://github.com/Vincit/objection.js/commit/0e58cf010348efc33e5459c055eea141f62f7561).

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-4) 2.0.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-35) What's new

*   New `skipFetched` option for `fetchGraph` and `$fetchGraph`

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-3) 2.0.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-36) What's new

*   Fixes [#1585(opens new window)](https://github.com/Vincit/objection.js/issues/1585)
*   Fixes [#1361(opens new window)](https://github.com/Vincit/objection.js/issues/1361)
*   Fixes [#1488(opens new window)](https://github.com/Vincit/objection.js/issues/1488)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_2-0-0) 2.0.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-37) What's new

*   Cleaner and more consistent API. A lot of methods have been renamed, removed combined and cleaned up. Most of the old methods still exist, but print a deprecation warning when first used. Some examples:

    *   `eager` ->`withGraphFetched`
    *   `joinEager` ->`withGraphJoined`
    *   removed `eagerAlgorithm` (you must explicitly use either `withGraphFetched` or `withGraphJoined`)
    *   merged `allowEager`, `allowInsert` and `allowUpsert` into one method `allowGraph`
    *   `$loadRelated` ->`$fetchGraph`
    *   `joinRelation` ->`joinRelated`
    *   `$relatedQuery` no longer mutates the receiving model instances

*   New [static hook API](https://vincit.github.io/objection.js/guide/hooks.html#static-query-hooks). The old instance hooks are still around.

*   `relatedQuery` can now be used for more than just subqueries. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#relation-queries).

*   modifiers can now take arguments and are a lot more useful. See [this recipe(opens new window)](https://vincit.github.io/objection.js/recipes/modifiers.html) for more info.

*   Objection now uses the [db-errors(opens new window)](https://github.com/Vincit/db-errors) library by default to wrap the database errors.

*   `insertMissing``upsertGraph` option now works as expected with `relate: true`: items that are not found in the database are inserted.

*   Brand new typings written from scratch with many improvements and finally a support for [custom query builders](https://vincit.github.io/objection.js/recipes/custom-query-builder.html#custom-query-builder)

*   A bunch of improvements and bug fixes for `upsertGraph`, including a huge speedup in some cases due to less data fetching.

*   A brand new [fn](https://vincit.github.io/objection.js/api/objection/#fn) helper for calling SQL functions.

*   Objection now uses native promises instead of bluebird.

*   Objection is now leaner as we dropped a bunch of dependencies like `bluebird` and `lodash`.

*   In addition to all of this, a huge number of bugs has been squashed!

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-2) Breaking changes

See the [migration guide](https://vincit.github.io/objection.js/release-notes/migration.html).

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-10) 1.6.10
--------------------------------------------------------------------------------------

*   Fixes [#1455(opens new window)](https://github.com/Vincit/objection.js/issues/1455)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-9) 1.6.9
------------------------------------------------------------------------------------

*   Revert fix for [#1089(opens new window)](https://github.com/Vincit/objection.js/issues/1089). It was causing more bugs than it fixed. #1089 will be addressed in 2.0.
*   Typings updates

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-8) 1.6.8
------------------------------------------------------------------------------------

*   Fix [#1287(opens new window)](https://github.com/Vincit/objection.js/issues/1287)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-7) 1.6.7
------------------------------------------------------------------------------------

*   A bunch of regression bug fixes.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-3) 1.6.3
------------------------------------------------------------------------------------

*   Fixes: [#1227(opens new window)](https://github.com/Vincit/objection.js/issues/1227)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-2) 1.6.2
------------------------------------------------------------------------------------

*   Add `as` method for `raw` making it possible to use `raw` expressions in `joinEager` modifiers (as long as you give names to your raw expressions using `as`).

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-1) 1.6.1
------------------------------------------------------------------------------------

*   Fix some very rare upsertGraph edge cases.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-6-0) 1.6.0
------------------------------------------------------------------------------------

*   Add `Model.traverseAsync` and `modelInstance.$traverseAsync` methods.

*   Fixes: [#842(opens new window)](https://github.com/Vincit/objection.js/issues/842) and [#1205(opens new window)](https://github.com/Vincit/objection.js/issues/1205). This bug is about subqueries "inheriting" parent query table name and alias. This bug has been around a long time and there is a small chance that people have started accidentally or on purpose use it as a feature. If you get weird reference errors from subqueries (relation not found, table not found etc.) you may need to explicitly give an alias or use `from` in your subqueries after this update. This is a borderline breaking change, but since 2.0 is still pretty far away, I wanted to get this out faster. If I'm wrong and people are heavily depending on this bug, I'll revert the change.

*   Fixes: [#1215(opens new window)](https://github.com/Vincit/objection.js/issues/1215)

*   Fixes: [#1206(opens new window)](https://github.com/Vincit/objection.js/issues/1206)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-5-3) 1.5.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-38) What's new

*   Fixes [#1204(opens new window)](https://github.com/Vincit/objection.js/issues/1204)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-5-1) 1.5.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-39) What's new

*   Relations are now loaded lazily [#1202(opens new window)](https://github.com/Vincit/objection.js/issues/1202)
*   `relationMappings.modelClass` can now be a function that returns a model class.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-5-0) 1.5.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-40) What's new

*   fix [#1131(opens new window)](https://github.com/Vincit/objection.js/issues/1131)
*   fix [#1114(opens new window)](https://github.com/Vincit/objection.js/issues/1114)
*   fix [#1185(opens new window)](https://github.com/Vincit/objection.js/issues/1185)
*   fix [#1109(opens new window)](https://github.com/Vincit/objection.js/issues/1109)
*   fix [#1110(opens new window)](https://github.com/Vincit/objection.js/issues/1110)
*   add eagerObject and eagerModifiers accessors to QueryBuilder.
*   complete rewrite of `insertGraph` and `upsertGraph` code. The rewrite brought a bunch of small performance optimizations and makes future development easier. No breaking changes.
*   Chaining `returning('*')` to `insertGraph` or `upsertGraph` now propagates the call to all insert, update and delete operations.
*   Code using objectio can now be transpilsed to ES5. No need to add babel workarounds anymore.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-4-0) 1.4.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-41) What's new

*   Add `modifierNotFound` hook [#1120(opens new window)](https://github.com/Vincit/objection.js/issues/1120)
*   fix [#1121(opens new window)](https://github.com/Vincit/objection.js/issues/1121)
*   fix [#1126(opens new window)](https://github.com/Vincit/objection.js/issues/1126)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-3-0) 1.3.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-42) What's new

*   Use `objection.raw` instead of `knex.raw` in `Model.raw`. [#1077(opens new window)](https://github.com/Vincit/objection.js/issues/1077)
*   Allow modifiers (namedFilters) to be used in `modifyEager` too.
*   Add `underscoreBeforeDigits` option for snake case converters. [#1025(opens new window)](https://github.com/Vincit/objection.js/issues/1025)
*   fix [#1074(opens new window)](https://github.com/Vincit/objection.js/issues/1074)
*   Typing fixes

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-2-3) 1.2.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-43) What's new

*   fix [#1007(opens new window)](https://github.com/Vincit/objection.js/issues/1007)
*   fix [#1008(opens new window)](https://github.com/Vincit/objection.js/issues/1008)
*   fix [#1047(opens new window)](https://github.com/Vincit/objection.js/issues/1047)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-2-2) 1.2.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-44) What's new

*   Improve reference cycle detection in `upsertGraph`

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-2-1) 1.2.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-45) What's new

*   fix [#1009(opens new window)](https://github.com/Vincit/objection.js/issues/1009)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-2-0) 1.2.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-46) What's new

*   fix [#919(opens new window)](https://github.com/Vincit/objection.js/issues/919)
*   fix [#964(opens new window)](https://github.com/Vincit/objection.js/issues/964)
*   Add `aliasFor` method to public API
*   Prevent bluebird warnings
*   UPPER_SNAKE_CASE support for `snakeCaseMappers` and `knexSnakeCaseMappers`

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-10) 1.1.10
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-47) What's new

*   Nothing! the npm release was somehow borked. This was just a rerelease of 1.1.9.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-9) 1.1.9
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-48) What's new

*   fix [#782(opens new window)](https://github.com/Vincit/objection.js/issues/782)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-8) 1.1.8
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-49) What's new

*   fix [#909(opens new window)](https://github.com/Vincit/objection.js/issues/909)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-7) 1.1.7
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-50) What's new

*   fix [#884(opens new window)](https://github.com/Vincit/objection.js/issues/884)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-6) 1.1.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-51) What's new

*   Add typings for fetchTableMetadata, tableMetadata and onbuildknex

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-5) 1.1.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-52) What's new

*   Make [Model.fetchTableMetadata](https://vincit.github.io/objection.js/release-notes/changelog.html#fetchtablemetadata) and [Model.tableMetadata](https://vincit.github.io/objection.js/release-notes/changelog.html#tablemetadata) methods public. [#871(opens new window)](https://github.com/Vincit/objection.js/issues/871)
*   Add [onBuildKnex](https://vincit.github.io/objection.js/release-notes/changelog.html#onbuildknex) query builder hook. [#807(opens new window)](https://github.com/Vincit/objection.js/issues/807)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-4) 1.1.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-53) What's new

*   fix subquery bug causing incompatibility with knex 0.14.5 and sqlite3

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-3) 1.1.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-54) What's new

*   fix regression in 1.1.2 (sorry about this) [#869(opens new window)](https://github.com/Vincit/objection.js/issues/869)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-2) 1.1.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-55) What's new

*   Add `virtuals` option for `toJSON` and `$toJson`[#866(opens new window)](https://github.com/Vincit/objection.js/issues/866)
*   fix [#868(opens new window)](https://github.com/Vincit/objection.js/issues/868)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-1) 1.1.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-56) What's new

*   fix [#865(opens new window)](https://github.com/Vincit/objection.js/issues/865)
*   fix bug where the static `Model.relatedQuery` didn't use the relation name as an alias for the table. This may break code if you have explicitly referenced the subquery table. [#859(opens new window)](https://github.com/Vincit/objection.js/issues/859)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-1-0) 1.1.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-57) What's new

*   Optional [object notation](https://vincit.github.io/objection.js/release-notes/changelog.html#relationexpression-object-notation) for relation expressions.
*   fix [#855(opens new window)](https://github.com/Vincit/objection.js/issues/855)
*   fix [#858(opens new window)](https://github.com/Vincit/objection.js/issues/858)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-0-1) 1.0.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-58) What's new

*   Added public [Relation.joinModelClass](https://vincit.github.io/objection.js/release-notes/changelog.html#relation) accessor
*   Don't call `returning` on sqlite (prevents a warning message added in knex 0.14.4)
*   fix [#844(opens new window)](https://github.com/Vincit/objection.js/issues/844)
*   Small documentation updates
*   Small typing fixes end updates

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_1-0-0-%F0%9F%8E%89) 1.0.0 🎉
----------------------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-59) What's new

*   The static [`relatedQuery`](https://vincit.github.io/objection.js/release-notes/changelog.html#relatedquery) method.
*   New reflection methods: [`isFind`](https://vincit.github.io/objection.js/release-notes/changelog.html#isfind), [`isInsert`](https://vincit.github.io/objection.js/release-notes/changelog.html#isinsert), [`isUpdate`](https://vincit.github.io/objection.js/release-notes/changelog.html#isupdate), [`isDelete`](https://vincit.github.io/objection.js/release-notes/changelog.html#isdelete), [`isRelate`](https://vincit.github.io/objection.js/release-notes/changelog.html#isrelate), [`isUnrelate`](https://vincit.github.io/objection.js/release-notes/changelog.html#isunrelate), [`hasWheres`](https://vincit.github.io/objection.js/release-notes/changelog.html#haswheres), [`hasSelects`](https://vincit.github.io/objection.js/release-notes/changelog.html#hasselects), [`hasEager`](https://vincit.github.io/objection.js/release-notes/changelog.html#haseager), [`has`](https://vincit.github.io/objection.js/release-notes/changelog.html#has). [`clear`](https://vincit.github.io/objection.js/release-notes/changelog.html#clear). [`columnNameToPropertyName`](https://vincit.github.io/objection.js/release-notes/changelog.html#columnnametopropertyname), [`propertyNameToColumnName`](https://vincit.github.io/objection.js/release-notes/changelog.html#propertynametocolumnname).
*   `ManyToMany` extras now work consistently in queries and filters. [#760(opens new window)](https://github.com/Vincit/objection.js/issues/760)

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-3) Breaking changes

*   `modelInstance.$query().delete().returning(something)` now returns a single instance instead of an array. [#659(opens new window)](https://github.com/Vincit/objection.js/issues/659)

*   Node 6.0.0 is now the minimum. Objection will not work on node < 6.0.0.

*   [`ValidationError`](https://vincit.github.io/objection.js/release-notes/changelog.html#validationerror) overhaul. This is a big one, so read this carefully! There are three things to check when you migrate to 1.0:

    1.   The [`createValidationError`](https://vincit.github.io/objection.js/release-notes/changelog.html#createvalidationerror) and [`ValidationError`](https://vincit.github.io/objection.js/release-notes/changelog.html#validationerror) interfaces have changed. If you have overridden the `createValidationError` method in your project, or you create custom `ValidationError` instances you need migrate to the interfaces.
    2.   The model validation errors (jsonSchema violations) have remained pretty much the same but there are couple of differences. Before, the keys of `error.data` were property names even when a nested object in a graph failed a validation. Now the keys for nested validation errors are key paths like `foo.bar[2].spam`. Another tiny difference is the order of validation errors for each key in `error.data`. Let's say a property `spam` failed for your model and `error.data.spam` contains an array of objects that describe the failures. Before, the first failed validation was the last item in the array, now it is the first item.
    3.   All [`ValidationErrors`](https://vincit.github.io/objection.js/release-notes/changelog.html#validationerror) now have a `type` field. Before all [`ValidationErrors`](https://vincit.github.io/objection.js/release-notes/changelog.html#validationerror) but the model validation errors (errors like "invalid relation expression", or "cyclic model graph") had no type, and could only be identified based on the existence of some weird key in `error.data`. The `error.data` is now removed from those errors and the `type` should be used instead. The message from the data is now stored in `error.message`.

*   Removed deprecated methods `whereRef`, `whereJsonField` and `whereJsonEquals`. The [`ref`](https://vincit.github.io/objection.js/release-notes/changelog.html#ref) helper can be used to replace the `whereRef` calls. [`ref`](https://vincit.github.io/objection.js/release-notes/changelog.html#ref) and [`lit`](https://vincit.github.io/objection.js/release-notes/changelog.html#lit) can be used to replace the removed json methods.

*   `ManyToMany` extras now work consistently in queries and filters. [#760(opens new window)](https://github.com/Vincit/objection.js/issues/760). This is not a breaking change per se, but can cause some queries to fail with a "ambiguous identifier" error because the join table is now joined in places where it previously wasn't. You need to explicitly specify the table for those failing columns using `Table.theColumn` syntax.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#changes) Changes

*   `isFindQuery` is renamed to [`isFind`(opens new window)](http://vincit.github.io/objection.js/#isfind) and deprecated.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-9-4) 0.9.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-60) What's new

*   Fixed [#627(opens new window)](https://github.com/Vincit/objection.js/issues/627)
*   Fixed [#671(opens new window)](https://github.com/Vincit/objection.js/issues/671)
*   Fixed [#672(opens new window)](https://github.com/Vincit/objection.js/issues/672)
*   Fixed [#674(opens new window)](https://github.com/Vincit/objection.js/issues/674)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-9-3) 0.9.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-61) What's new

*   Add beforeInsert hook for relations. [#649(opens new window)](https://github.com/Vincit/objection.js/issues/649)[#19(opens new window)](https://github.com/Vincit/objection.js/issues/19)
*   Add [`relatedFindQueryMutates`](https://vincit.github.io/objection.js/release-notes/changelog.html#relatedfindquerymutates) and [`relatedInsertQueryMutates`](https://vincit.github.io/objection.js/release-notes/changelog.html#relatedinsertquerymutates) configs as well as [`$setRelated`](https://vincit.github.io/objection.js/release-notes/changelog.html#_s_setrelated) and [`$appendRelated`](https://vincit.github.io/objection.js/release-notes/changelog.html#_s_appendrelated) helpers. [#599(opens new window)](https://github.com/Vincit/objection.js/issues/599)
*   Fixed [#648(opens new window)](https://github.com/Vincit/objection.js/issues/648)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-9-2) 0.9.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-62) What's new

*   Fix regression: `from` fails with a subquery.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-9-1) 0.9.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-63) What's new

*   [`castTo`(opens new window)](http://vincit.github.io/objection.js/#castto) method for setting the model class of query result rows.
*   [`onError`(opens new window)](http://vincit.github.io/objection.js/#onerror)`QueryBuilder` method.
*   [`knexSnakeCaseMappers`(opens new window)](http://vincit.github.io/objection.js/#objection-knexsnakecasemappers) and [`snakeCaseMappers`(opens new window)](http://vincit.github.io/objection.js/#objection-snakecasemappers) for snake_case to camelCase conversions.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-9-0) 0.9.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-64) What's new

*   Relations can now be defined using keys inside JSON columns. See the examples [here(opens new window)](http://vincit.github.io/objection.js/#relationmappings).
*   [`lit`(opens new window)](http://vincit.github.io/objection.js/#lit) helper function [#275(opens new window)](https://github.com/Vincit/objection.js/issues/275)
*   Fixes for [`upsertGraph`(opens new window)](http://vincit.github.io/objection.js/#upsertgraph) when using composite keys. [#517(opens new window)](https://github.com/Vincit/objection.js/issues/517)
*   Added `noDelete`, `noUpdate`, `noInsert`, `noRelate` and `noUnrelate` options for `upsertGraph`. See [UpsertGraphOptions docs](https://vincit.github.io/objection.js/release-notes/changelog.html#upsertgraphoptions) for more info.
*   `insertGraph` now accepts an options object just like `upsertGraph`. `relate` option can be used instead of `#dbRef`. [#586(opens new window)](https://github.com/Vincit/objection.js/issues/586)

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-4) Breaking changes

*   Instance update/patch with `returning` now return a single object instead of an array. [#423(opens new window)](https://github.com/Vincit/objection.js/issues/423)

*   Because of the support for JSON relations [the `Relation` class(opens new window)](http://vincit.github.io/objection.js/#relation) has changed a bit.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-8) 0.8.8
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-65) What's new

*   Typing updates: [#489(opens new window)](https://github.com/Vincit/objection.js/issues/489)[#487(opens new window)](https://github.com/Vincit/objection.js/issues/487)
*   Improve `resultSize` method. [#213(opens new window)](https://github.com/Vincit/objection.js/issues/213)
*   Avoid unnecessary updates in upsertGraph [#480(opens new window)](https://github.com/Vincit/objection.js/issues/480)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-7) 0.8.7
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-66) What's new

*   `throwIfNotFound` now also throws when update or delete doesn't change any rows.
*   [`mixin`](https://vincit.github.io/objection.js/release-notes/changelog.html#mixin) and [`compose`](https://vincit.github.io/objection.js/release-notes/changelog.html#compose) helpers for applying multiple plugins. [#475(opens new window)](https://github.com/Vincit/objection.js/issues/475)[#473(opens new window)](https://github.com/Vincit/objection.js/issues/473)
*   Typing updates [#474(opens new window)](https://github.com/Vincit/objection.js/issues/474)[#479(opens new window)](https://github.com/Vincit/objection.js/issues/479)
*   `upsertGraph` now validates patched models correctly. [#477(opens new window)](https://github.com/Vincit/objection.js/issues/477)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-6) 0.8.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-67) What's new

*   Finally: the first version of [`upsertGraph`](https://vincit.github.io/objection.js/release-notes/changelog.html#graph-upserts) method! Please open issues about bugs, WTFs and missing features.
*   Strip readonly virtual properties in fromJson & friends [#432(opens new window)](https://github.com/Vincit/objection.js/issues/432)
*   Fixed [#439(opens new window)](https://github.com/Vincit/objection.js/issues/439)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-5) 0.8.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-68) What's new

*   Add [`Model.useLimitInFirst`(opens new window)](http://vincit.github.io/objection.js/#uselimitinfirst) configuration flag.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-4) 0.8.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-69) What's new

*   New shorthand methods [`joinEager`(opens new window)](http://vincit.github.io/objection.js/#joineager), [`naiveEager`(opens new window)](http://vincit.github.io/objection.js/#naiveeager), [`mergeJoinEager`(opens new window)](http://vincit.github.io/objection.js/#mergejoineager) and [`mergeNaiveEager`(opens new window)](http://vincit.github.io/objection.js/#mergenaiveeager).
*   New shorthand method [`findOne`(opens new window)](http://vincit.github.io/objection.js/#findone)
*   New reflection method [`isFindQuery`(opens new window)](http://vincit.github.io/objection.js/#isfind)
*   ManyToMany extra properties can now be updated [#413(opens new window)](https://github.com/Vincit/objection.js/issues/413)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-3) 0.8.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-70) What's new

*   [`NaiveEagerAlogrithm`(opens new window)](http://vincit.github.io/objection.js/#eager)
*   [Aliases in relation expressions(opens new window)](http://vincit.github.io/objection.js/#relationexpression)[#402(opens new window)](https://github.com/Vincit/objection.js/issues/402)
*   New lazily evaluated `raw` function. [#275(opens new window)](https://github.com/Vincit/objection.js/issues/275)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-2) 0.8.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-71) What's new

*   [`Model.namedFilters`(opens new window)](http://vincit.github.io/objection.js/#namedfilters) object for defining shared filters that can be used by name in eager expressions.
*   Full support for views and table aliases in eager, join, joinRelation etc. [#181(opens new window)](https://github.com/Vincit/objection.js/issues/181)
*   Fix `bindTransaction` bug with `ManyToManyRelation` junction tables [#395(opens new window)](https://github.com/Vincit/objection.js/issues/395)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-1) 0.8.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-72) What's new

*   [`throwIfNotFound`(opens new window)](http://vincit.github.io/objection.js/#throwifnotfound) method for making empty query results throw an exception.
*   fix error when passing model instance to a `where` method. [#387(opens new window)](https://github.com/Vincit/objection.js/issues/387)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-8-0) 0.8.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-73) What's new

*   All query methods now call `Model.query` to create a `QueryBuilder` instance [#346(opens new window)](https://github.com/Vincit/objection.js/issues/346)
*   Objection is no longer transpiled. One of the implications is that you can use a github link in package.json to test experimental versions.
*   `count` can now be called without arguments [#364(opens new window)](https://github.com/Vincit/objection.js/issues/364)
*   A new [`getRelations`](https://vincit.github.io/objection.js/release-notes/changelog.html#getrelations) method for plugin development and other reflection greatness.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-5) Breaking changes

> Old model definition

```
function Person() {
  Model.apply(this, arguments);
}

Model.extend(Person);

Person.tableName = 'Person';

Person.prototype.fullName = function () {
  return this.firstName + ' ' + this.lastName;
};

// More static and prototype methods.
```

> Easiest way to migrate to `class` and `extends` keywords

```
class Person extends Model {}

Person.tableName = 'Person';

Person.prototype.fullName = function () {
  return this.firstName + ' ' + this.lastName;
};

// More static and prototype methods.
```

*   Support for node versions below 4.0.0 has been removed. With it the support for legacy class inheritance using `Model.extend` method has also been removed. This means that you need to change your model definitions to use the `class` and `extends` keywords. To achieve this with the minimum amount of changes you can simply swap the constructor function and `Model.extend` to a class definition. You can still define all static and prototype methods and properties the old way. See the example on the right -->

Note that this also affects Babel transpilation. You cannot (or need to) use `babel-plugin-transform-es2015-classes` anymore. See the [ESNext example project(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/express-es7) as an example of how to setup babel.

*   The default value of [`pickJsonSchemaProperties`](https://vincit.github.io/objection.js/release-notes/changelog.html#pickjsonschemaproperties) was changed to `false`. Before, all properties that were not listed in `jsonSchema` were removed before `insert`, `patch` or `update` (if `jsonSchma` was defined). Starting from this version you need to explicitly set the value to `true`. You may have been used this feature by accident. If you have weird problems after the update, try setting `objection.Model.pickJsonSchemaProperties = true;` to see if it helps.

*   [`relate`](https://vincit.github.io/objection.js/release-notes/changelog.html#pickjsonschemaproperties) and [`unrelate`](https://vincit.github.io/objection.js/release-notes/changelog.html#pickjsonschemaproperties) methods now return the result of the underlying query (`patch` in case of `HasManyRelation`, `HasOneRelation`, and `BelongsToOneRelation`. `insert` otherwise). Before the method input was always returned.

*   `Model.RelatedQueryBuilder` is removed. `Model.QueryBuilder` is now used to create all query builders for the model. This only affects you if you have defined custom query builders.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-12) 0.7.12
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-74) What's new

*   fix [#345(opens new window)](https://github.com/Vincit/objection.js/issues/345)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-11) 0.7.11
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-75) What's new

*   fix [#339(opens new window)](https://github.com/Vincit/objection.js/issues/339)
*   fix [#341(opens new window)](https://github.com/Vincit/objection.js/issues/341)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-10) 0.7.10
--------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-76) What's new

*   fix bugs that prevented using `$relatedQuery` and `eager` together with `JoinEagerAlgorithm`
*   typing updates

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-9) 0.7.9
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-77) What's new

*   [`joinRelation`(opens new window)](http://vincit.github.io/objection.js/#joinrelation) now accepts [`RelationExpressions`(opens new window)](http://vincit.github.io/objection.js/#relationexpression) and can join multiple and nested relations.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-6) 0.7.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-78) What's new

*   `range` and `page` methods now use a window function and only generate one query on postgresql [#62(opens new window)](https://github.com/Vincit/objection.js/issues/62)
*   fix MSSQL 2100 parameter limit in eager queries [#311(opens new window)](https://github.com/Vincit/objection.js/issues/311)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-5) 0.7.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-79) What's new

*   fix [#327(opens new window)](https://github.com/Vincit/objection.js/issues/327)
*   fix [#256(opens new window)](https://github.com/Vincit/objection.js/issues/256)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-4) 0.7.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-80) What's new

*   automatically select columns needed for relations [#309(opens new window)](https://github.com/Vincit/objection.js/issues/309)
*   fix an issue where `$formatJson` was called inside `insertGraph`[#326(opens new window)](https://github.com/Vincit/objection.js/issues/326)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-3) 0.7.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-81) What's new

*   fix [#325(opens new window)](https://github.com/Vincit/objection.js/issues/325)
*   fix an issue where `select` had to be used in addition to `distinct` in some cases

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-2) 0.7.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-82) What's new

*   `HasOneThroughRelation` relation type.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-1) 0.7.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-83) What's new

*   fix `JoinEagerAlgorithm` NPE bug

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-7-0) 0.7.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-84) What's new

*   `jsonSchema` without `properties` now works. [#205(opens new window)](https://github.com/Vincit/objection.js/issues/205)
*   `relationMappings` can now be a function. [#227(opens new window)](https://github.com/Vincit/objection.js/issues/227)
*   many to many extras can now be aliased. [#223(opens new window)](https://github.com/Vincit/objection.js/issues/223)
*   zero values are now allowed in relation columns. [#228(opens new window)](https://github.com/Vincit/objection.js/issues/228)
*   active transaction can now be accessed in `$before/$after` hooks through `queryContext.transaction` property.
*   Validation can now be easily modified through a new [`Validator`](https://vincit.github.io/objection.js/release-notes/changelog.html#validator) interface. [#241(opens new window)](https://github.com/Vincit/objection.js/issues/241)[#199(opens new window)](https://github.com/Vincit/objection.js/issues/199)
*   fix a `JoinEager` problem where an empty result for a relation caused the following relations to be empty. [#292(opens new window)](https://github.com/Vincit/objection.js/issues/292)
*   `ref(fieldExpression)` syntax to reduce need for knex.raw and updating single attribute inside JSON column. [#270(opens new window)](https://github.com/Vincit/objection.js/issues/270)
*   [mergeEager(opens new window)](http://vincit.github.io/objection.js/#mergeeager) method.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-6) Breaking changes

*   `$relatedQuery` now returns a single model instead of an array for belongsToOne and hasOne relations. [#155(opens new window)](https://github.com/Vincit/objection.js/issues/155)
*   identifier of a model can now be updated. Be careful with this one! Before if you forgot a wrong id in an `update`/`patch` operation, it would simply get ignored. Now the id is also updated just like any other column [#100(opens new window)](https://github.com/Vincit/objection.js/issues/100)
*   `Table.*` is now selected by default in all queries instead of `*`. This will break some join queries that don't have an explicit select clause. [#161(opens new window)](https://github.com/Vincit/objection.js/issues/161)
*   `ValidationError.data` is now an object including, for each key, a list of errors with context info. [#283(opens new window)](https://github.com/Vincit/objection.js/issues/283)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-6-2) 0.6.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-85) What's new

*   `relationMappings` can now be a function [#227(opens new window)](https://github.com/Vincit/objection.js/issues/227)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-6-1) 0.6.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-86) What's new

*   fix bug [#205(opens new window)](https://github.com/Vincit/objection.js/issues/205)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-6-0) 0.6.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-87) What's new

*   Eager loading can now be done using joins and zero extra queries. See [`eagerAlgorithm`](https://vincit.github.io/objection.js/release-notes/changelog.html#eageralgorithm), [`defaultEagerAlgorithm`](https://vincit.github.io/objection.js/release-notes/changelog.html#defaulteageralgorithm) and [`eager`](https://vincit.github.io/objection.js/release-notes/changelog.html#eager) for more info.
*   `#ref` in graph inserts can now contain extra properties for many-to-many relations [#156(opens new window)](https://github.com/Vincit/objection.js/issues/156)
*   `#dbRef` can now be used to refer to existing rows from a `insertWithRelated` graph.
*   [`modelPaths`](https://vincit.github.io/objection.js/release-notes/changelog.html#modelpaths) attribute for cleaner way to point to models in relationMappings.
*   [`pickJsonSchemaProperties`](https://vincit.github.io/objection.js/release-notes/changelog.html#pickjsonschemaproperties) config parameter [#110(opens new window)](https://github.com/Vincit/objection.js/issues/110)
*   [`insertGraphAndFetch`](https://vincit.github.io/objection.js/release-notes/changelog.html#insertgraphandfetch) with `insertWithRelatedAndFetch` alias. [#172(opens new window)](https://github.com/Vincit/objection.js/issues/172)
*   Added [`$beforeDelete`](https://vincit.github.io/objection.js/release-notes/changelog.html#_s_beforedelete) and [`$afterDelete`](https://vincit.github.io/objection.js/release-notes/changelog.html#_s_afterdelete) hooks [#112(opens new window)](https://github.com/Vincit/objection.js/issues/112)
*   Old values can now be accessed from `$beforeUpdate`, `$afterUpdate`, `$beforeValidate` and `$afterValidate` hooks [#185(opens new window)](https://github.com/Vincit/objection.js/issues/185)
*   Support length property [#168(opens new window)](https://github.com/Vincit/objection.js/issues/168)
*   Make sure operations are executed in the order they are called [#180(opens new window)](https://github.com/Vincit/objection.js/issues/180)
*   Fetch nothing if the `where` clauses hit no rows in `update/patchAndFetchById` methods [#189(opens new window)](https://github.com/Vincit/objection.js/issues/189)
*   Lots of performance tweaks.
*   `$loadRelated` and `loadRelated` now return a `QueryBuilder`.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-7) Breaking changes

*   Undefined values as query method arguments now throw an exception. Before they were just silently ignored and for example `delete().where('id', undefined)` caused the entire table to be deleted. [skipUndefined(opens new window)](http://vincit.github.io/objection.js/#skipundefined) method can be called for a query builder to handle the undefined values the old way.

*   Deprecated method `dumpSql` is now removed.

*   `$loadRelated` and `loadRelated` now return a `QueryBuilder`. This may break your code is some rare cases where you have called a non-standard promise method like `reflect` for the return value of these functions.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-5-5) 0.5.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-88) What's new

*   [Virtual attributes](https://vincit.github.io/objection.js/release-notes/changelog.html#virtualattributes)

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-5-4) 0.5.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-89) What's new

*   bugfix: insertWithRelated now works with `additionalProperties = false` in `jsonSchema`
*   Add updateAndFetch and patchAndFetch methods for `$query`
*   bugfix: afterGet was not called for nested models in eager query
*   Use ajv instad of tv4 for json schema validation

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-5-3) 0.5.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-90) What's new

*   ES6 promise compatibility fixes.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-5-1) 0.5.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-91) What's new

*   [$afterGet](https://vincit.github.io/objection.js/release-notes/changelog.html#afterget) hook.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-5-0) 0.5.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-92) What's new

*   [joinRelation](https://vincit.github.io/objection.js/release-notes/changelog.html#joinrelation) family of query builder methods.
*   `HasOneRelation` for creating inverse one-to-one relations.
*   Relations have been renamed `OneToOneRelation` -->`BelongsToOneRelation`, `OneToManyRelation` -->`HasManyRelation`. The old names work, but have been deprecated.
*   [withSchema](https://vincit.github.io/objection.js/release-notes/changelog.html#withschema) now works as expected and sets the schema of all queries executed by the query builder the method is called for.
*   [filterEager](https://vincit.github.io/objection.js/release-notes/changelog.html#filtereager) method for better eager query filtering.
*   [extra properties](https://vincit.github.io/objection.js/release-notes/changelog.html#relationmappings) feature for selecting/inserting columns from/to the join table in many-to-many relations.
*   Eager query recursion depth can be controlled like so: `parent.^5`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-4-0) 0.4.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-93) What's new

*   Query context feature. See [#51(opens new window)](https://github.com/Vincit/objection.js/issues/51) and [these docs](https://vincit.github.io/objection.js/release-notes/changelog.html#context) for more info.
*   Composite key support.
*   [findById](https://vincit.github.io/objection.js/release-notes/changelog.html#findbyid), [deleteById](https://vincit.github.io/objection.js/release-notes/changelog.html#deletebyid), [whereComposite](https://vincit.github.io/objection.js/release-notes/changelog.html#wherecomposite) and [whereInComposite](https://vincit.github.io/objection.js/release-notes/changelog.html#whereincomposite) query builder methods.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-8) Breaking changes

There shouldn't be any major breaking changes. We moved from ES5 to ES7 + babel in this version so there are big changes in the codebase. If something comes up, please open an issue.

There are a few known corner cases that may break:

*   You can now define a model for the join table of `ManyToMany` relations in `relationMappings`. This is optional, but may be needed if you already have a model for a `ManyToMany` relation _and_ you use `snake_case` to `camelCase` conversion for the column names. See the documentation on the [through](https://vincit.github.io/objection.js/release-notes/changelog.html#relationthrough) property of [relationMappings](https://vincit.github.io/objection.js/release-notes/changelog.html#relationmappings).

*   The repo no longer contains the actual built javascript. Only the ES7 code that is transpiled when the code is published to npm. Therefore you can no longer specify a git hash to package.json to use for example the HEAD version. We will start to publish alpha and RC versions to npm when something new and experimental is added to the library.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-3-3) 0.3.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-94) What's new

*   fix regression: QueryBuilder.from is broken.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-3-2) 0.3.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-95) What's new

*   Improved relation expression whitespace handling.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-3-1) 0.3.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-96) What's new

*   `whereJson*` methods can now be used inside functions given to `where` methods.
*   Added multiple missing knex methods to `QueryBuilder`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-3-0) 0.3.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-97) What's new

*   [insertWithRelated(opens new window)](http://vincit.github.io/objection.js/QueryBuilder.html#insertWithRelated) method for inserting model trees
*   [insertAndFetch(opens new window)](http://vincit.github.io/objection.js/QueryBuilder.html#insertAndFetch), [updateAndFetchById(opens new window)](http://vincit.github.io/objection.js/QueryBuilder.html#updateAndFetchById) and [patchAndFetchById(opens new window)](http://vincit.github.io/objection.js/QueryBuilder.html#patchAndFetchById) helper methods
*   Filters for [eager expressions](https://vincit.github.io/objection.js/release-notes/changelog.html#eager-queries)
*   [New alternative way to use transactions](https://vincit.github.io/objection.js/release-notes/changelog.html#transaction-object)
*   Many performance updates related to cloning, serializing and deserializing model trees.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-9) Breaking changes

*   QueryBuilder methods `update`, `patch` and `delete` now return the number of affected rows. The new methods `updateAndFetchById` and `patchAndFetchById` may help with the migration
*   `modelInstance.$query()` instance method now returns a single model instead of an array
*   Removed `Model.generateId()` method. `$beforeInsert` can be used instead

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-8) 0.2.8
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-98) What's new

*   ES6 inheritance support
*   generator function support for transactions
*   traverse,pick and omit methods for Model and QueryBuilder
*   bugfix: issue #38

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-7) 0.2.7
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-99) What's new

*   bugfix: fix #37 also for `$query()`.
*   Significant `toJson`/`fromJson` performance boost.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-6) 0.2.6
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-100) What's new

*   bugfix: fix regression bug that broke dumpSql.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-5) 0.2.5
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-101) What's new

*   bugfix: fix regression bug that prevented values assigned to `this` in `$before` callbacks from getting into the actual database query

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-4) 0.2.4
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-102) What's new

*   bugfix: many-to-many relations didn't work correctly with a snake_case to camelCase conversion in the related model class.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-3) 0.2.3
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-103) What's new

*   Promise constructor is now exposed through `require('objection').Promise`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-2) 0.2.2
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-104) What's new

*   $beforeUpdate, $afterUpdate, $beforeInsert etc. are now asynchronous and you can return promises from them.
*   Added `Model.fn()` shortcut to `knex.fn`.
*   Added missing `asCallback` and `nodeify` methods for `QueryBuilder`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-1) 0.2.1
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-105) What's new

*   bugfix: Chaining `insert` with `returning` now returns all listed columns.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-2-0) 0.2.0
------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#what-s-new-106) What's new

*   New name `objection.js`.
*   `$beforeInsert`, `$afterInsert`, `$beforeUpdate` and `$afterUpdate` hooks for `Model`.
*   Postgres jsonb query methods: `whereJsonEquals`, `whereJsonSupersetOf`, `whereJsonSubsetOf` and friends.
*   `whereRef` query method.
*   Expose `knex.raw()` through `Model.raw()`.
*   Expose `knex.client.formatter()` through `Model.formatter()`.
*   `QueryBuilder` can be used to make sub queries just like knex's `QueryBuilder`.
*   Possibility to use a custom `QueryBuilder` subclass by overriding `Model.QueryBuilder`.
*   Filter queries/objects for relations.
*   A pile of bug fixes.

### [#](https://vincit.github.io/objection.js/release-notes/changelog.html#breaking-changes-10) Breaking changes

*   Project was renamed to objection.js. Migrate simply by replacing `moron` with `objection`.

[#](https://vincit.github.io/objection.js/release-notes/changelog.html#_0-1-0) 0.1.0
------------------------------------------------------------------------------------

First release.
