# Package com.nimbusds.jose.jwk.source

---

package com.nimbusds.jose.jwk.source

JSON Web Key (JWK) sourcing interface and utilities. Typical sources can be
 a local text file containing a JWK set, a JWK set specified by URL, a Java
 keystore, or a database.

- 

Related Packages

Package
Description
com.nimbusds.jose.jwk

JSON Web Key (JWK) classes.

com.nimbusds.jose.jwk.gen

JSON Web Key (JWK) generation utilities.

- 

Class
Description
CachingJWKSetSource<C extends SecurityContext>

Caching JWKSetSource.

CachingJWKSetSource.RefreshCompletedEvent<C extends SecurityContext>

JWK set cache refresh completed event.

CachingJWKSetSource.RefreshInitiatedEvent<C extends SecurityContext>

JWK set cache refresh initiated event.

CachingJWKSetSource.RefreshTimedOutEvent<C extends SecurityContext>

JWK set cache refresh timed out event.

CachingJWKSetSource.UnableToRefreshEvent<C extends SecurityContext>

Unable to refresh the JWK set cache event.

CachingJWKSetSource.WaitingForRefreshEvent<C extends SecurityContext>

Waiting for a JWK set cache refresh to complete on another thread
 event.

DefaultJWKSetCache
Deprecated.
see RemoteJWKSet.

ImmutableJWKSet<C extends SecurityContext>

JSON Web Key (JWK) source backed by an immutable JWK set.

ImmutableSecret<C extends SecurityContext>

JSON Web Key (JWK) source backed by an immutable secret.

JWKSecurityContextJWKSet

A `JWKSource` backed by keys found in the `JWKSecurityContext`.

JWKSetBasedJWKSource<C extends SecurityContext>

JSON Web Key (JWK) set based JWK source.

JWKSetCache
Deprecated.
see RemoteJWKSet.

JWKSetCacheRefreshEvaluator

Evaluates whether a JWK set cache requires refreshing.

JWKSetParseException

JWK set parse exception, in the context of JWK set retrieval.

JWKSetRetrievalException

JWK set retrieval exception, due to a network issue or the remote server
 being unavailable.

JWKSetSource<C extends SecurityContext>

JSON Web Key (JWK) set source.

JWKSetSourceWithHealthStatusReporting<C extends SecurityContext>

Decorates a JWKSetSource with health status reporting.

JWKSetSourceWrapper<C extends SecurityContext>

Wraps a JWKSetSource to provide convenient decoration by means
 of subclassing.

JWKSetUnavailableException

JWK set unavailable exception.

JWKSetWithTimestamp
Deprecated.
see RemoteJWKSet.

JWKSource<C extends SecurityContext>

JSON Web Key (JWK) source.

JWKSourceBuilder<C extends SecurityContext>

JWKSource builder.

JWKSourceWithFailover<C extends SecurityContext>

JWK source with optional failover.

OutageTolerantJWKSetSource<C extends SecurityContext>

JWKSetSource with outage tolerance to handle temporary network
 issues and endpoint downtime, potentially running into minutes or hours.

OutageTolerantJWKSetSource.OutageEvent<C extends SecurityContext>

JWK set source outage event.

RateLimitedJWKSetSource<C extends SecurityContext>

JWKSetSource that limits the number of requests in a time
 period.

RateLimitedJWKSetSource.RateLimitedEvent<C extends SecurityContext>

Rate limited event.

RateLimitReachedException

Rate limit reached exception.

RefreshAheadCachingJWKSetSource<C extends SecurityContext>

Caching JWKSetSource that refreshes the JWK set prior to its
 expiration.

RefreshAheadCachingJWKSetSource.RefreshNotScheduledEvent<C extends SecurityContext>

JWK set refresh not scheduled event.

RefreshAheadCachingJWKSetSource.RefreshScheduledEvent<C extends SecurityContext>

New JWK set refresh scheduled event.

RefreshAheadCachingJWKSetSource.ScheduledRefreshCompletedEvent<C extends SecurityContext>

Scheduled JWK set cache refresh completed event.

RefreshAheadCachingJWKSetSource.ScheduledRefreshFailed<C extends SecurityContext>

Scheduled JWK refresh failed event.

RefreshAheadCachingJWKSetSource.ScheduledRefreshInitiatedEvent<C extends SecurityContext>

Scheduled JWK set cache refresh initiated event.

RefreshAheadCachingJWKSetSource.UnableToRefreshAheadOfExpirationEvent<C extends SecurityContext>

Unable to refresh the JWK set cache ahead of expiration event.

RemoteJWKSet<C extends SecurityContext>
Deprecated.
Construct a JWKSource using JWKSourceBuilder.

RetryingJWKSetSource<C extends SecurityContext>

JWKSetSource with with retry capability to work around
 transient network issues.

RetryingJWKSetSource.RetrialEvent<C extends SecurityContext>

Retrial event.

URLBasedJWKSetSource<C extends SecurityContext>

JWK set source that loads the keys from a `URL`, without health status
 reporting.