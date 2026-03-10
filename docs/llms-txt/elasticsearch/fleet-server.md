# Source: https://www.elastic.co/docs/release-notes/fleet-server

﻿---
title: Fleet Server release notes
description: Review the changes, fixes, and more in each version of Fleet Server. To check for security updates, go to Security announcements for the Elastic Stack...
url: https://www.elastic.co/docs/release-notes/fleet-server
products:
  - Elastic Agent
  - Fleet
  - Fleet Server
applies_to:
  - Elastic Stack: Generally available
---

# Fleet Server release notes
Review the changes, fixes, and more in each version of Fleet Server.
To check for security updates, go to [Security announcements for the Elastic Stack](https://discuss.elastic.co/c/announcements/security-announcements/31).
<admonition title="Related release notes">
  Elastic Agent integrates and manages Beats for data collection, and Beats changes may impact Elastic Agent functionality. To check for Elastic Agent changes in Beats, go to [Beats release notes](https://www.elastic.co/docs/release-notes/beats).
</admonition>


## 9.3.1


### Features and enhancements

- Update Go to v1.25.7. [#6322](https://github.com/elastic/fleet-server/pull/6322)


## 9.3.0


### Features and enhancements

- Support secrets in agent.download section of policy. [#5837](https://github.com/elastic/fleet-server/pull/5837)
- Support secrets in fleet section of policy. [#5997](https://github.com/elastic/fleet-server/pull/5997)
- Make file storage size configurable. [#5478](https://github.com/elastic/fleet-server/pull/5478)
- Accept secret references in policies in either inline or path formats. [#5852](https://github.com/elastic/fleet-server/pull/5852)
  Elastic Agent policies can contain secret references in one of two formats: inline or path.
  With the inline format, the reference looks like this: `&lt;path&gt;: $co.elastic.secret{&lt;secret ref&gt;}`.
  With the path format, the reference looks like this: `secrets.&lt;path&gt;.id:&lt;secret ref&gt;`.
  This change ensures that Fleet Server accepts secret references in policies in either format.
- Improve file upload performance for large files. [#6048](https://github.com/elastic/fleet-server/pull/6048)


### Fixes

- Make action optional when upgrade details are provided. [#5609](https://github.com/elastic/fleet-server/pull/5609)


## 9.2.6


### Features and enhancements

- Update Go to v1.25.7. [#6322](https://github.com/elastic/fleet-server/pull/6322)


## 9.2.5


### Fixes

- Enforce maximum limits on UploadBegin and UploadComplete request body sizes. [#6159](https://github.com/elastic/fleet-server/pull/6159)


## 9.2.4


### Fixes

- Make action optional when upgrade details are provided. [#5609](https://github.com/elastic/fleet-server/pull/5609)


## 9.2.3

_No new features, enhancements, or fixes._

## 9.2.2

_No new features, enhancements, or fixes._

## 9.2.1


### Fixes

- Fix issue that was preventing checkin local_metadata from being updated. [#5824](https://github.com/elastic/fleet-server/pull/5824)
  Once an Elastic Agent is marked with audit unenrolled Fleet Server fails to update the document in
  Elasticsearch when it checks in. This fixes that issue an now the Fleet Server will be able to update the
  document in Elasticsearch reflecting the actual status of the Elastic Agent.
- Fix issue where malformed components field prevents agent authentication. [#5858](https://github.com/elastic/fleet-server/pull/5858)


## 9.2.0


### Features and enhancements

- Add OTel collector properties to policy schema. [#5169](https://github.com/elastic/fleet-server/pull/5169) [#5241](https://github.com/elastic/fleet-server/issues/5241)
  Add OTel collector properties to the policy schema. This way policies defined in Fleet that include
  this data are forwarded to agents.
- Add agent_policy_id and policy_revision_idx to checkin requests. [#5501](https://github.com/elastic/fleet-server/pull/5501) [#6446](https://github.com/elastic/elastic-agent/issues/6446)
  Add the agent_policy_id and policy_revision_idx attributes to checkin
  request bodies so an agent is able to inform fleet-server of its exact
  policy. These details will replace the need for an ack on
  policy_change actions, and will be used to determine when to send a
  policy change when there is a new revision available, or when the
  agent is reassigned to a different policy. Add a server setting under
  feature_flags.ignore_checkin_policy_id that disables this behavour and
  restores the previous approach.
- Refactor bulk checkin handler. [#5493](https://github.com/elastic/fleet-server/pull/5493)
  Refactor the bulk checkin handler to allow for future extensions
- Add credentials to OTel Elasticsearch exporters. [#5469](https://github.com/elastic/fleet-server/pull/5469)
  When a policy includes OTel configuration with Elasticsearch exporters, it configures their credentials using the credentials in the Elasticsearch output.
- Update Golang version to v1.25.1. [#5562](https://github.com/elastic/fleet-server/pull/5562)


## 9.1.10

_No new features, enhancements, or fixes._

## 9.1.9

_No new features, enhancements, or fixes._

## 9.1.8

_No new features, enhancements, or fixes._

## 9.1.7


### Fixes

- Fix issue that was preventing checkin local_metadata from being updated. [#5824](https://github.com/elastic/fleet-server/pull/5824)

After an Elastic Agent was marked with audit unenrolled, Fleet Server failed to update the document in
Elasticsearch when it checked in. This fixes that issue, and now the Fleet Server can update the
document in Elasticsearch, reflecting the actual status of the Elastic Agent.
- Fix issue where malformed components field prevents agent authentication. [#5858](https://github.com/elastic/fleet-server/pull/5858)


## 9.1.6

_No new features, enhancements, or fixes._

## 9.1.5


### Features and enhancements

- Update Go version to v1.25.1. [#5562](https://github.com/elastic/fleet-server/pull/5562)


## 9.1.4


### Fixes

- Reset trace links on bulk items when returning to pool. [#5317](https://github.com/elastic/fleet-server/pull/5317)
- Restore connection limiter. [#5372](https://github.com/elastic/fleet-server/pull/5372)
  Restore connection level limiter to prevent OOM incidents.
  This limiter is used in addition to the request-level throttle so that when
  our in-flight requests reaches max_connections, a 429 is returned. If the
  total connections the server uses is over max_connections*1.1 the server drops
  the connection before the TLS handshake.
- Build fleet-server as fully static binary to restore OS matrix compatibility. [#5392](https://github.com/elastic/fleet-server/pull/5392) [#5262](https://github.com/elastic/fleet-server/issues/5262)


## 9.1.3


### Fixes

- Fix 503 handling in enrollment. [#5232](https://github.com/elastic/fleet-server/pull/5232) [#5197](https://github.com/elastic/fleet-server/issues/5197)
- Remove extra ES search when preparing agent policy. [#5283](https://github.com/elastic/fleet-server/pull/5283)


## 9.1.2

_No new features, enhancements, or fixes._

## 9.1.1


### Fixes

- Fix upgrade details download_rate as string handling. [#5198](https://github.com/elastic/fleet-server/pull/5198) [#5214](https://github.com/elastic/fleet-server/pull/5214) [#5183](https://github.com/elastic/fleet-server/pull/5183) [#5176](https://github.com/elastic/fleet-server/pull/5176) [#5164](https://github.com/elastic/fleet-server/issues/5164)


## 9.1.0


### Features and enhancements

- Add ability for enrollment to take an agent ID. [#4290](https://github.com/elastic/fleet-server/pull/4290) [#4226](https://github.com/elastic/fleet-server/issues/4226)
- Clear `agent.upgrade_attempts` when upgrade is complete. [#4528](https://github.com/elastic/fleet-server/pull/4528)
  The new AutomaticAgentUpgradeTask Kibana task sets the upgrade_attempts property in agents it upgrades.
  This property is used to track upgrade retries and should therefore be cleared when the upgrade is complete.
- Make pbkdf2 settings validation FIPS compliant. [#4542](https://github.com/elastic/fleet-server/pull/4542)
- Update Go to v1.24.3. [#4891](https://github.com/elastic/fleet-server/pull/4891)
- Add version metadata to version command output. [#4820](https://github.com/elastic/fleet-server/pull/4820)
  Add commit, buildtime, and FIPS distribution indicators to output of version command.
  Add fips-distribution attribute to initial startup log.
- Add rollback attribute to upgrade actions in preparation for enabling upgrade rollbacks in a future release. [#4838](https://github.com/elastic/fleet-server/issues/4838)


### Fixes

- Upgrade golang.org/x/net to v0.34.0 and golang.org/x/crypto to v0.32.0. [#4405](https://github.com/elastic/fleet-server/pull/4405)
- Fix host parsing in Elasticsearch output diagnostics. [#4765](https://github.com/elastic/fleet-server/pull/4765)
- Redact output in bootstrap config logs. [#4775](https://github.com/elastic/fleet-server/pull/4775)
- Mutex protection for remote bulker config. [#4776](https://github.com/elastic/fleet-server/pull/4776)
  Use existing remote bulker mutex to control access to remote bulker configs.
- Enable dead code elimination. [#4784](https://github.com/elastic/fleet-server/pull/4784)
  Add grpcnotrace build tags and ensure DCE (dead code elimination) is enabled.
  Reduce binary size by 34%
- Include the base error for json decode error responses. [#5069](https://github.com/elastic/fleet-server/pull/5069)


## 9.0.8


### Features and enhancements

- Update Go version to v1.25.1. [#5562](https://github.com/elastic/fleet-server/pull/5562)


## 9.0.7


### Fixes

- Reset trace links on bulk items when returning to pool. [#5317](https://github.com/elastic/fleet-server/pull/5317)
- Restore connection limiter. [#5372](https://github.com/elastic/fleet-server/pull/5372)
  Restore connection level limiter to prevent OOM incidents.
  This limiter is used in addition to the request-level throttle so that once
  our in-flight requests reaches max_connections a 429 is returned, but if the
  total connections the server uses is over max_connections*1.1 the server drops
  the connection before the TLS handshake.
- Build fleet-server as fully static binary to restore OS matrix compatibility. [#5392](https://github.com/elastic/fleet-server/pull/5392) [#5262](https://github.com/elastic/fleet-server/issues/5262)


## 9.0.6


### Fixes

- Fix 503 handling in enrollment. [#5232](https://github.com/elastic/fleet-server/pull/5232) [#5197](https://github.com/elastic/fleet-server/issues/5197)
- Remove extra ES search when preparing agent policy. [#5283](https://github.com/elastic/fleet-server/pull/5283)


## 9.0.5


### Fixes

- Fix upgrade details download_rate as string handling. [#5217](https://github.com/elastic/fleet-server/pull/5217) [#5227](https://github.com/elastic/fleet-server/pull/5227) [#5176](https://github.com/elastic/fleet-server/pull/5176) [#5164](https://github.com/elastic/fleet-server/issues/5164)


## 9.0.4


### Fixes

- Include the base error for JSON decode error responses. [#5069](https://github.com/elastic/fleet-server/pull/5069)


## 9.0.3


### Features and enhancements

- Update Go version to v1.24.4. [#5025](https://github.com/elastic/fleet-server/pull/5025)


## 9.0.2


### Features and enhancements

- Update Go version to v1.24.3. [#4891](https://github.com/elastic/fleet-server/pull/4891)


## 9.0.1


### Fixes

- Fix host parsing in Elasticsearch output diagnostics. [#4765](https://github.com/elastic/fleet-server/pull/4765)
- Redact output in bootstrap config logs. [#4775](https://github.com/elastic/fleet-server/pull/4775)
- Mutex protection for remote bulker config. [#4776](https://github.com/elastic/fleet-server/pull/4776)
  Use existing remote bulker mutex to control access to remote bulker configs.
- Enable dead code elimination. [#4784](https://github.com/elastic/fleet-server/pull/4784)
  Add grpcnotrace build tags and ensure DCE (dead code elimination) is enabled.
  Reduce binary size by 34%


## 9.0.0


### Features and enhancements

- New setting allowing automatic deletion of unenrolled agents in Fleet settings. [#195544](https://github.com/elastic/kibana/pull/195544)
- Improves filtering and visibility of Uninstalled and Orphaned agents in Fleet, by differentiating them from Offline agents. [#205815](https://github.com/elastic/kibana/pull/205815)
- Introduces air-gapped configuration for bundled packages in Fleet. [#202435](https://github.com/elastic/kibana/pull/202435)
- Updates removed parameters of the Fleet -> Logstash output configurations. [#210115](https://github.com/elastic/kibana/pull/210115)
- Updates the maximum supported package version in Fleet. [#196675](https://github.com/elastic/kibana/pull/196675)
- Replaces the use of context.TODO and context.Background in logger function calls for most Fleet Server use cases. [#4168](https://github.com/elastic/fleet-server/pull/4168) and [#3087](https://github.com/elastic/fleet-server/issues/3087)
- Refactor the Fleet Server API constructor to use functional opts instead of a long list of pointers. [#4169](https://github.com/elastic/fleet-server/pull/4169) and [#3823](https://github.com/elastic/fleet-server/issues/3823)
- Removes the deprecated policy_throttle configuration setting in favour of the newer policy-limit for Fleet Server. [#4288](https://github.com/elastic/fleet-server/pull/4288)
- Removes old bundled.yaml from oas, fixed tags. [#194788](https://github.com/elastic/kibana/pull/194788)
- Adds the ability for Elastic Agent to enroll using a specific ID. [#4290](https://github.com/elastic/fleet-server/pull/4290) and [#4226](https://github.com/elastic/fleet-server/issues/4226)


### Fixes

- Fixes a validation error that occurs on multi-text input fields in Fleet. [#205768](https://github.com/elastic/kibana/pull/205768)
- Adds a context timeout to the bulker flush in Fleet Server so it times out if it takes more time than the deadline. [#3986](https://github.com/elastic/fleet-server/pull/3986)
- Removes a race condition that may occur when remote Elasticsearch outputs are used in Fleet Server. [#4171](https://github.com/elastic/fleet-server/pull/4171)
- Uses the chi/middleware.Throttle package to track in-flight requests and return a 429 response when the limit is reached in Fleet Server. [#4402](https://github.com/elastic/fleet-server/pull/4402) and [#4400](https://github.com/elastic/fleet-server/issues/4400)