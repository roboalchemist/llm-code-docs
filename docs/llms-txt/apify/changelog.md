# Source: https://docs.apify.com/cli/docs/changelog.md

# Source: https://docs.apify.com/sdk/python/docs/changelog.md

# Source: https://docs.apify.com/sdk/js/reference/changelog.md

# Source: https://docs.apify.com/sdk/js/docs/changelog.md

# Source: https://docs.apify.com/api/client/python/docs/changelog.md

# Source: https://docs.apify.com/api/client/js/docs/changelog.md

# Source: https://docs.apify.com/cli/docs/changelog.md

# Source: https://docs.apify.com/sdk/python/docs/changelog.md

# Source: https://docs.apify.com/sdk/js/reference/changelog.md

# Source: https://docs.apify.com/sdk/js/docs/changelog.md

# Source: https://docs.apify.com/api/client/python/docs/changelog.md

# Source: https://docs.apify.com/api/client/js/docs/changelog.md

# Changelog

### [2.19.0](https://github.com/apify/apify-client-js/releases/tag/v2.19.0)[](#2190)

##### [2.19.0](https://github.com/apify/apify-client-js/releases/tag/v2.19.0) (2025-10-20)[](#2190-2025-10-20)

###### 🚀 Features[](#-features)

* Move restartOnError from Actor to Run options ([#760](https://github.com/apify/apify-client-js/pull/760)) ([8f80f82](https://github.com/apify/apify-client-js/commit/8f80f82c22128fd3378ba00ad29766cf4cc8e3c0)) by [@DaveHanns](https://github.com/DaveHanns)

### [2.18.0](https://github.com/apify/apify-client-js/releases/tag/v2.18.0)[](#2180)

##### [2.18.0](https://github.com/apify/apify-client-js/releases/tag/v2.18.0) (2025-10-09)[](#2180-2025-10-09)

###### 🚀 Features[](#-features-1)

* Allowed signature to be passed in kv-store/datasets ([#761](https://github.com/apify/apify-client-js/pull/761)) ([a31e36d](https://github.com/apify/apify-client-js/commit/a31e36d6201f90136da362af2aa10b29efb80bad)) by [@gippy](https://github.com/gippy)
* Add startedBefore and startedAfter to run list ([#763](https://github.com/apify/apify-client-js/pull/763)) ([2345999](https://github.com/apify/apify-client-js/commit/23459990598ba01833a21bfe969a1c64f775be00)) by [@danpoletaev](https://github.com/danpoletaev)

###### 🐛 Bug Fixes[](#-bug-fixes)

* Export missing symbols from env vars and version client ([#756](https://github.com/apify/apify-client-js/pull/756)) ([86b591f](https://github.com/apify/apify-client-js/commit/86b591fe8d2f07b4e746561ee9e055fca6639e1d)) by [@B4nan](https://github.com/B4nan)

### [2.17.0](https://github.com/apify/apify-client-js/releases/tag/v2.17.0)[](#2170)

##### [2.17.0](https://github.com/apify/apify-client-js/releases/tag/v2.17.0) (2025-09-11)[](#2170-2025-09-11)

###### 🚀 Features[](#-features-2)

* Add forcePermissionLevel run option ([#743](https://github.com/apify/apify-client-js/pull/743)) ([693808c](https://github.com/apify/apify-client-js/commit/693808c6dbbf24542f8f86f3d49673b75309e9f6)) by [@tobice](https://github.com/tobice)

###### 🐛 Bug Fixes[](#-bug-fixes-1)

* Signed storage URLs avoid adding expiresInSecs to query params ([#734](https://github.com/apify/apify-client-js/pull/734)) ([70aff4f](https://github.com/apify/apify-client-js/commit/70aff4fedefc02a1c8c6e5155057e213a8ad6c81)) by [@danpoletaev](https://github.com/danpoletaev)
* Presigned resource urls shouldn't follow `baseUrl` ([#745](https://github.com/apify/apify-client-js/pull/745)) ([07b36fb](https://github.com/apify/apify-client-js/commit/07b36fbd46ed74e9c4ad3977cac883af55ad525d)) by [@barjin](https://github.com/barjin)

### [2.16.0](https://github.com/apify/apify-client-js/releases/tag/v2.16.0)[](#2160)

##### [2.16.0](https://github.com/apify/apify-client-js/releases/tag/v2.16.0) (2025-08-26)[](#2160-2025-08-26)

###### Refactor[](#refactor)

* \[**breaking**] Rename expiresInMillis to expiresInSecs in create storage content URL ([#733](https://github.com/apify/apify-client-js/pull/733)) ([a190b72](https://github.com/apify/apify-client-js/commit/a190b72f6f62ffb54898fd74c80981a6967d573f)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.15.1](https://github.com/apify/apify-client-js/releases/tag/v2.15.1)[](#2151)

##### [2.15.1](https://github.com/apify/apify-client-js/releases/tag/v2.15.1) (2025-08-20)[](#2151-2025-08-20)

###### 🐛 Bug Fixes[](#-bug-fixes-2)

* Add recordPublicUrl to KeyValueListItem type ([#730](https://github.com/apify/apify-client-js/pull/730)) ([42dfe64](https://github.com/apify/apify-client-js/commit/42dfe6484e3504aaf46c516bade3d7ff989782ea)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.15.0](https://github.com/apify/apify-client-js/releases/tag/v2.15.0)[](#2150)

##### [2.15.0](https://github.com/apify/apify-client-js/releases/tag/v2.15.0) (2025-08-12)[](#2150-2025-08-12)

###### 🚀 Features[](#-features-3)

* Extend status parameter to an array of possible statuses ([#723](https://github.com/apify/apify-client-js/pull/723)) ([0be893f](https://github.com/apify/apify-client-js/commit/0be893f2401a652908aff1ed305736068ee0b421)) by [@JanHranicky](https://github.com/JanHranicky)

### [2.14.0](https://github.com/apify/apify-client-js/releases/tag/v2.14.0)[](#2140)

##### [2.14.0](https://github.com/apify/apify-client-js/releases/tag/v2.14.0) (2025-08-11)[](#2140-2025-08-11)

###### 🚀 Features[](#-features-4)

* Add keyValueStore.getRecordPublicUrl ([#725](https://github.com/apify/apify-client-js/pull/725)) ([d84a03a](https://github.com/apify/apify-client-js/commit/d84a03afe6fd49e38d4ca9a6821681e852c73a2a)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.13.0](https://github.com/apify/apify-client-js/releases/tag/v2.13.0)[](#2130)

##### [2.13.0](https://github.com/apify/apify-client-js/releases/tag/v2.13.0) (2025-08-06)[](#2130-2025-08-06)

###### 🚀 Features[](#-features-5)

* Add new methods Dataset.createItemsPublicUrl & KeyValueStore.createKeysPublicUrl ([#720](https://github.com/apify/apify-client-js/pull/720)) ([62554e4](https://github.com/apify/apify-client-js/commit/62554e48a8bf6bf1853f356ac84f046fed5945c1)) by [@danpoletaev](https://github.com/danpoletaev)

###### 🐛 Bug Fixes[](#-bug-fixes-3)

* Add `eventData` to `WebhookDispatch` type ([#714](https://github.com/apify/apify-client-js/pull/714)) ([351f11f](https://github.com/apify/apify-client-js/commit/351f11f268a54532c7003ab099bc0d7d8d9c9ad7)) by [@valekjo](https://github.com/valekjo)
* KV store createKeysPublicUrl wrong URL ([#724](https://github.com/apify/apify-client-js/pull/724)) ([a48ec58](https://github.com/apify/apify-client-js/commit/a48ec58e16a36cc8aa188524e4a738c40f5b74e9)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.12.6](https://github.com/apify/apify-client-js/releases/tag/v2.12.6)[](#2126)

##### [2.12.6](https://github.com/apify/apify-client-js/releases/tag/v2.12.6) (2025-06-30)[](#2126-2025-06-30)

###### 🚀 Features[](#-features-6)

* Allow sorting of Actors collection ([#708](https://github.com/apify/apify-client-js/pull/708)) ([562a193](https://github.com/apify/apify-client-js/commit/562a193b90ce4f2b05bf166da8fe2dddaa87eb6b)) by [@protoss70](https://github.com/protoss70)

###### 🐛 Bug Fixes[](#-bug-fixes-4)

* Use appropriate timeouts ([#704](https://github.com/apify/apify-client-js/pull/704)) ([b896bf2](https://github.com/apify/apify-client-js/commit/b896bf2e653e0766ef297f29a35304c1a5f27598)) by [@janbuchar](https://github.com/janbuchar)
* Rename option for new sortBy parameter ([#711](https://github.com/apify/apify-client-js/pull/711)) ([f45dd03](https://github.com/apify/apify-client-js/commit/f45dd037c581a6c0e27fd8c036033b99cec1ba89)) by [@protoss70](https://github.com/protoss70)

### [2.12.5](https://github.com/apify/apify-client-js/releases/tag/v2.12.5)[](#2125)

##### [2.12.5](https://github.com/apify/apify-client-js/releases/tag/v2.12.5) (2025-05-28)[](#2125-2025-05-28)

###### 🚀 Features[](#-features-7)

* List kv store keys by collection of prefix ([#688](https://github.com/apify/apify-client-js/pull/688)) ([be25137](https://github.com/apify/apify-client-js/commit/be25137575435547aaf2c3849fc772daf0537450)) by [@MFori](https://github.com/MFori)
* Add unlockRequests endpoint to RequestQueue client ([#700](https://github.com/apify/apify-client-js/pull/700)) ([7c52c64](https://github.com/apify/apify-client-js/commit/7c52c645e2eb66ad97c8daa9791b080bfc747288)) by [@drobnikj](https://github.com/drobnikj)

###### 🐛 Bug Fixes[](#-bug-fixes-5)

* Add missing 'effectivePlatformFeatures', 'createdAt', 'isPaying' to User interface ([#691](https://github.com/apify/apify-client-js/pull/691)) ([e138093](https://github.com/apify/apify-client-js/commit/e1380933476e5336469e5da083d2017147518f88)) by [@metalwarrior665](https://github.com/metalwarrior665)
* Move prettier into `devDependencies` ([#695](https://github.com/apify/apify-client-js/pull/695)) ([1ba903a](https://github.com/apify/apify-client-js/commit/1ba903a1bfa7a95a8c54ef53951db502dfa4b276)) by [@hudson-worden](https://github.com/hudson-worden)

### [2.12.4](https://github.com/apify/apify-client-js/releases/tag/v2.12.4)[](#2124)

##### [2.12.4](https://github.com/apify/apify-client-js/releases/tag/v2.12.4) (2025-05-13)[](#2124-2025-05-13)

###### 🚀 Features[](#-features-8)

* Allow overriding timeout of `KVS.setRecord` calls ([#692](https://github.com/apify/apify-client-js/pull/692)) ([105bd68](https://github.com/apify/apify-client-js/commit/105bd6888117a6c64b21a725c536d4992dff099c)) by [@B4nan](https://github.com/B4nan)

###### 🐛 Bug Fixes[](#-bug-fixes-6)

* Fix `RunCollectionListOptions` status type ([#681](https://github.com/apify/apify-client-js/pull/681)) ([8fbcf82](https://github.com/apify/apify-client-js/commit/8fbcf82bfaca57d087719cf079fc850c6d31daa5)) by [@MatousMarik](https://github.com/MatousMarik)
* **actor:** Add missing 'pricingInfos' field to Actor object ([#683](https://github.com/apify/apify-client-js/pull/683)) ([4bd4853](https://github.com/apify/apify-client-js/commit/4bd485369ac42d0b72597638c0316a6ca60f9847)) by [@metalwarrior665](https://github.com/metalwarrior665)

### [2.12.3](https://github.com/apify/apify-client-js/releases/tag/v2.12.3)[](#2123)

##### [2.12.3](https://github.com/apify/apify-client-js/releases/tag/v2.12.3) (2025-04-24)[](#2123-2025-04-24)

###### 🐛 Bug Fixes[](#-bug-fixes-7)

* DefaultBuild() returns BuildClient ([#677](https://github.com/apify/apify-client-js/pull/677)) ([8ce72a4](https://github.com/apify/apify-client-js/commit/8ce72a4c90aac421281d14ad0ff25fdecba1d094)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.12.2](https://github.com/apify/apify-client-js/releases/tag/v2.12.2)[](#2122)

##### [2.12.2](https://github.com/apify/apify-client-js/releases/tag/v2.12.2) (2025-04-14)[](#2122-2025-04-14)

###### 🚀 Features[](#-features-9)

* Add support for general resource access ([#669](https://github.com/apify/apify-client-js/pull/669)) ([7deba52](https://github.com/apify/apify-client-js/commit/7deba52a5ff96c990254687d6b965fc1a5bf3467)) by [@tobice](https://github.com/tobice)
* Add defaultBuild method ([#668](https://github.com/apify/apify-client-js/pull/668)) ([c494b3b](https://github.com/apify/apify-client-js/commit/c494b3b8b664a88620e9f41c902acba533d636cf)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.12.1](https://github.com/apify/apify-client-js/releases/tag/v2.12.1)[](#2121)

##### [2.12.1](https://github.com/apify/apify-client-js/releases/tag/v2.12.1) (2025-03-11)[](#2121-2025-03-11)

###### 🚀 Features[](#-features-10)

* Add maxItems and maxTotalChargeUsd to resurrect ([#652](https://github.com/apify/apify-client-js/pull/652)) ([5fb9c9a](https://github.com/apify/apify-client-js/commit/5fb9c9a35d6ccb7313c5cbbd7d09b19a64d70d8e)) by [@novotnyj](https://github.com/novotnyj)

### [2.11.2](https://github.com/apify/apify-client-js/releases/tag/v2.11.2)[](#2112)

##### [2.11.2](https://github.com/apify/apify-client-js/releases/tag/v2.11.2) (2025-02-03)[](#2112-2025-02-03)

###### 🚀 Features[](#-features-11)

* Add dataset.statistics ([#621](https://github.com/apify/apify-client-js/pull/621)) ([6aeb2b7](https://github.com/apify/apify-client-js/commit/6aeb2b7fae041468d125a0c8bbb00804e290143a)) by [@MFori](https://github.com/MFori)
* Added getOpenApiSpecification() to BuildClient ([#626](https://github.com/apify/apify-client-js/pull/626)) ([6248b28](https://github.com/apify/apify-client-js/commit/6248b2844796f93e22404ddea85ee77c1a5b7d50)) by [@danpoletaev](https://github.com/danpoletaev)

### [2.11.1](https://github.com/apify/apify-client-js/releases/tag/v2.11.1)[](#2111)

##### [2.11.1](https://github.com/apify/apify-client-js/releases/tag/v2.11.1) (2025-01-10)[](#2111-2025-01-10)

###### 🐛 Bug Fixes[](#-bug-fixes-8)

* Change type `Build.actorDefinitions` to `Build.actorDefinition` ([#624](https://github.com/apify/apify-client-js/pull/624)) ([611f313](https://github.com/apify/apify-client-js/commit/611f31365727e70f58d899009ff5a05c6b888253)) by [@jirispilka](https://github.com/jirispilka)
* Add ActorRunPricingInfo type ([#623](https://github.com/apify/apify-client-js/pull/623)) ([8880295](https://github.com/apify/apify-client-js/commit/8880295f13c1664ab6ae0b8b3f171025317ea011)) by [@janbuchar](https://github.com/janbuchar)

### [2.11.0](https://github.com/apify/apify-client-js/releases/tag/v2.11.0)[](#2110)

##### [2.11.0](https://github.com/apify/apify-client-js/releases/tag/v2.11.0) (2024-12-16)[](#2110-2024-12-16)

###### 🚀 Features[](#-features-12)

* **actor-build:** Add actorDefinition type for actor build detail, deprecate inputSchema and readme. ([#611](https://github.com/apify/apify-client-js/pull/611)) ([123c2b8](https://github.com/apify/apify-client-js/commit/123c2b81c945a0ca6922221598aa73c42cc298d6)) by [@drobnikj](https://github.com/drobnikj)
* Add `charge` method to the run client for "pay per event" ([#613](https://github.com/apify/apify-client-js/pull/613)) ([3d9c64d](https://github.com/apify/apify-client-js/commit/3d9c64d5442b4f8f27c2b19dd98dd3b758944287)) by [@Jkuzz](https://github.com/Jkuzz)
* **request-queue:** Add queueHasLockedRequests and clientKey into RequestQueueClientListAndLockHeadResult ([#617](https://github.com/apify/apify-client-js/pull/617)) ([f58ce98](https://github.com/apify/apify-client-js/commit/f58ce989e431de54eb673e561e407a7066ea2b64)) by [@drobnikj](https://github.com/drobnikj)

###### 🐛 Bug Fixes[](#-bug-fixes-9)

* **actor:** Correctly set type for ActorTaggedBuilds ([#612](https://github.com/apify/apify-client-js/pull/612)) ([3bda7ee](https://github.com/apify/apify-client-js/commit/3bda7ee741caf2ccfea249a42ed7512cda36bf0b)) by [@metalwarrior665](https://github.com/metalwarrior665)

### [2.10.0](https://github.com/apify/apify-client-js/releases/tag/v2.10.0)[](#2100)

##### [2.10.0](https://github.com/apify/apify-client-js/releases/tag/v2.10.0) (2024-11-01)[](#2100-2024-11-01)

###### 🚀 Features[](#-features-13)

* Add user.updateLimits ([#595](https://github.com/apify/apify-client-js/pull/595)) ([bf97c0f](https://github.com/apify/apify-client-js/commit/bf97c0f5bf8d0cbd8decb60382f0605243b00dd5)) by [@MFori](https://github.com/MFori)
* Allow appending custom parts to the user agent ([#602](https://github.com/apify/apify-client-js/pull/602)) ([d07452b](https://github.com/apify/apify-client-js/commit/d07452b7bff83d16b48bf3cfba5b88aa564ffe2b)) by [@B4nan](https://github.com/B4nan)

###### 🐛 Bug Fixes[](#-bug-fixes-10)

* Allow `null` when updating dataset/kvs/rq `name` ([#604](https://github.com/apify/apify-client-js/pull/604)) ([0034c2e](https://github.com/apify/apify-client-js/commit/0034c2ee63d6d1c6856c4e7786da43d86a3d63ce)) by [@B4nan](https://github.com/B4nan)

### [v2.9.7](https://github.com/apify/apify-client-js/releases/tag/v2.9.7)[](#v297)

##### What's Changed[](#whats-changed)

* feat: Rename maxCostPerRunUsd to maxTotalChargeUsd by [@novotnyj](https://github.com/novotnyj) in [#592](https://github.com/apify/apify-client-js/pull/592)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.6...v2.9.7>

### [v2.9.6](https://github.com/apify/apify-client-js/releases/tag/v2.9.6)[](#v296)

##### What's Changed[](#whats-changed-1)

* fix: Rename maxCostPerRun by [@novotnyj](https://github.com/novotnyj) in [#589](https://github.com/apify/apify-client-js/pull/589)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.5...v2.9.6>

### [v2.9.5](https://github.com/apify/apify-client-js/releases/tag/v2.9.5)[](#v295)

##### What's Changed[](#whats-changed-2)

* fix: add `isDeprecated` to actor update type by [@Jkuzz](https://github.com/Jkuzz) in [#566](https://github.com/apify/apify-client-js/pull/566)
* feat: add Actor Standby types by [@jirimoravcik](https://github.com/jirimoravcik) in [#569](https://github.com/apify/apify-client-js/pull/569)
* feat: allow `unwind` param to `DatasetClient.listItems()` to be an array by [@fnesveda](https://github.com/fnesveda) in [#576](https://github.com/apify/apify-client-js/pull/576)
* feat: add maxCostPerRun param by [@stetizu1](https://github.com/stetizu1) in [#578](https://github.com/apify/apify-client-js/pull/578)

##### New Contributors[](#new-contributors)

* [@stetizu1](https://github.com/stetizu1) made their first contribution in [#578](https://github.com/apify/apify-client-js/pull/578)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.4...v2.9.5>

### [v2.9.4](https://github.com/apify/apify-client-js/releases/tag/v2.9.4)[](#v294)

##### What's Changed[](#whats-changed-3)

* fix: add missing `isApifyIntegration` field to `Webhook` type by [@omikader](https://github.com/omikader) in [#523](https://github.com/apify/apify-client-js/pull/523)
* feat: add notifications field to Schedule by [@m-murasovs](https://github.com/m-murasovs) in [#545](https://github.com/apify/apify-client-js/pull/545)
* feat: added data property to API error object by [@gippy](https://github.com/gippy) in [#559](https://github.com/apify/apify-client-js/pull/559)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.3...v2.9.4>

### [v2.9.3](https://github.com/apify/apify-client-js/releases/tag/v2.9.3)[](#v293)

##### What's Changed[](#whats-changed-4)

* chore: remove warning when parseDateFields reaches depth limit by [@tobice](https://github.com/tobice) in [#521](https://github.com/apify/apify-client-js/pull/521)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.2...v2.9.3>

### [v2.9.2](https://github.com/apify/apify-client-js/releases/tag/v2.9.2)[](#v292)

##### What's Changed[](#whats-changed-5)

* feat: add monthlyUsage() and limits() endpoints to UserClients by [@tobice](https://github.com/tobice) in [#517](https://github.com/apify/apify-client-js/pull/517)
* feat: parse monthlyUsage.dailyServiceUsages\[].date as Date by [@tobice](https://github.com/tobice) in [#519](https://github.com/apify/apify-client-js/pull/519)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.1...v2.9.2>

### [v2.9.1](https://github.com/apify/apify-client-js/releases/tag/v2.9.1)[](#v291)

##### What's Changed[](#whats-changed-6)

* fix: ensure axios headers are instance of AxiosHeaders via interceptor by [@B4nan](https://github.com/B4nan) in [#515](https://github.com/apify/apify-client-js/pull/515)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.9.0...v2.9.1>

### [v2.9.0](https://github.com/apify/apify-client-js/releases/tag/v2.9.0)[](#v290)

##### What's Changed[](#whats-changed-7)

* fix: publish browser bundle by [@B4nan](https://github.com/B4nan) in [#506](https://github.com/apify/apify-client-js/pull/506)
* fix: update axios to v1.6 by [@B4nan](https://github.com/B4nan) in [#505](https://github.com/apify/apify-client-js/pull/505)
* feat: add `KeyValueStore.recordExists()` method by [@barjin](https://github.com/barjin) in [#510](https://github.com/apify/apify-client-js/pull/510)
* feat: add `log()` method to BuildClient by [@tobice](https://github.com/tobice) in [#509](https://github.com/apify/apify-client-js/pull/509)
* feat: add `runs()` and `builds()` top level endpoints by [@foxt451](https://github.com/foxt451) in [#468](https://github.com/apify/apify-client-js/pull/468)

##### New Contributors[](#new-contributors-1)

* [@tobice](https://github.com/tobice) made their first contribution in [#509](https://github.com/apify/apify-client-js/pull/509)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.8.6...v2.9.0>

### [v2.8.6](https://github.com/apify/apify-client-js/releases/tag/v2.8.6)[](#v286)

##### What's Changed[](#whats-changed-8)

* fix: replace ReadableStream with Readable by [@foxt451](https://github.com/foxt451) in [#463](https://github.com/apify/apify-client-js/pull/463)
* fix: add missing properties to `ActorCollectionCreateOptions` type by [@jirimoravcik](https://github.com/jirimoravcik) in [#486](https://github.com/apify/apify-client-js/pull/486)
* feat(request-queue): Limit payload size for batchAddRequests() by [@drobnikj](https://github.com/drobnikj) in [#489](https://github.com/apify/apify-client-js/pull/489)
* docs: add code owner for documentation by [@TC-MO](https://github.com/TC-MO) in [#488](https://github.com/apify/apify-client-js/pull/488)

##### New Contributors[](#new-contributors-2)

* [@foxt451](https://github.com/foxt451) made their first contribution in [#463](https://github.com/apify/apify-client-js/pull/463)
* [@TC-MO](https://github.com/TC-MO) made their first contribution in [#488](https://github.com/apify/apify-client-js/pull/488)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.8.4...v2.8.6>

### [v2.8.4](https://github.com/apify/apify-client-js/releases/tag/v2.8.4)[](#v284)

##### What's Changed[](#whats-changed-9)

* fix(schedule): expose other fields when id optional by [@omikader](https://github.com/omikader) in [#451](https://github.com/apify/apify-client-js/pull/451)

##### New Contributors[](#new-contributors-3)

* [@omikader](https://github.com/omikader) made their first contribution in [#451](https://github.com/apify/apify-client-js/pull/451)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.8.2...v2.8.4>

### [v.2.8.2](https://github.com/apify/apify-client-js/releases/tag/v2.8.2)[](#v282)

##### What's Changed[](#whats-changed-10)

* ci: test on node 20 + improve tests workflow by [@B4nan](https://github.com/B4nan) in [#430](https://github.com/apify/apify-client-js/pull/430)
* feat: Add how to install javascript Apify client by [@webrdaniel](https://github.com/webrdaniel) in [#440](https://github.com/apify/apify-client-js/pull/440)
* fix: ScheduleUpdateData type by [@magne4000](https://github.com/magne4000) in [#276](https://github.com/apify/apify-client-js/pull/276)

##### New Contributors[](#new-contributors-4)

* [@webrdaniel](https://github.com/webrdaniel) made their first contribution in [#440](https://github.com/apify/apify-client-js/pull/440)
* [@magne4000](https://github.com/magne4000) made their first contribution in [#276](https://github.com/apify/apify-client-js/pull/276)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.8.1...v2.8.2>

### [v2.8.1](https://github.com/apify/apify-client-js/releases/tag/v2.8.1)[](#v281)

##### What's Changed[](#whats-changed-11)

* fix: don't parse non-date strings by [@barjin](https://github.com/barjin) in [#412](https://github.com/apify/apify-client-js/pull/412)
* chore: Removed references to issuesEnabled by [@Jkuzz](https://github.com/Jkuzz) in [#416](https://github.com/apify/apify-client-js/pull/416)
* feat: add new webhook fields by [@m-murasovs](https://github.com/m-murasovs) in [#426](https://github.com/apify/apify-client-js/pull/426)
* feat: Add delete to runs and builds by [@Jkuzz](https://github.com/Jkuzz) in [#428](https://github.com/apify/apify-client-js/pull/428)

##### New Contributors[](#new-contributors-5)

* [@Jkuzz](https://github.com/Jkuzz) made their first contribution in [#416](https://github.com/apify/apify-client-js/pull/416)

**Full Changelog**: <https://github.com/apify/apify-client-js/compare/v2.8.0...v2.8.1>
