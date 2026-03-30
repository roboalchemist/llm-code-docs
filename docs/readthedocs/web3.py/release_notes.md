# Release Notes

v7 Breaking Changes Summary

See the v7 Migration Guide

## web3.py v8.0.0-beta.1 (2025-12-18)

### Breaking Changes

-

Drop support for Python 3.8 and 3.9 and upgrade syntax accordingly (#3774 [https://github.com/ethereum/web3.py/issues/3774])

-

Upgrade websockets requirement to >=14.0. (#3779 [https://github.com/ethereum/web3.py/issues/3779])

-

Bump eth-utils dependency to require >=5.3.0 (#3790 [https://github.com/ethereum/web3.py/issues/3790])

### Bugfixes

-

Fix tests flakiness due to slow data generation from hypothesis triggering a timeout. (#3730 [https://github.com/ethereum/web3.py/issues/3730])

-

Fix `topics` type for `LogsSubscription` to reflect AND / OR nested list conditions on log filters. (#3748 [https://github.com/ethereum/web3.py/issues/3748])

-

Make AsyncWeb3 with respect to the provider it is instantiated with, fixing static type issues. (#3761 [https://github.com/ethereum/web3.py/issues/3761])

-

Wrap timeout in ClientTimeout for AsyncBeacon post request (#3784 [https://github.com/ethereum/web3.py/issues/3784])

### Improved Documentation

-

Update a few broken links (#3746 [https://github.com/ethereum/web3.py/issues/3746])

-

Fix indentation in the code block in “An introduction to subscriptions” (#3752 [https://github.com/ethereum/web3.py/issues/3752])

### Features

-

Add the `TopicFilter` type to better describe the cases for filtering logs by topics. (#3748 [https://github.com/ethereum/web3.py/issues/3748])

-

Add support for Python 3.14 (#3779 [https://github.com/ethereum/web3.py/issues/3779])

-

Upgrade geth version in CI (#3787 [https://github.com/ethereum/web3.py/issues/3787])

### Internal Changes - for web3.py Contributors

-

Resolve the DeprecationWarning for the usage of datetime.datetime.utcnow() (#3751 [https://github.com/ethereum/web3.py/issues/3751])

-

Use latest Geth version `v1.16.5` for integration tests. (#3775 [https://github.com/ethereum/web3.py/issues/3775])

### Removals

-

Removal of the deprecated `LegacyWebSocketProvider`. (#3762 [https://github.com/ethereum/web3.py/issues/3762])

## web3.py v7.13.0 (2025-08-04)

### Bugfixes

-

Raise `BadResponseFormat` from within `FormattingMiddleware` if the raw response is not a dict. (#3735 [https://github.com/ethereum/web3.py/issues/3735])

### Improved Documentation

-

Fix broken link to external `eth_gasPrice` documentation. (#3717 [https://github.com/ethereum/web3.py/issues/3717])

### Features

-

Support parallelization of subscription handling globally via the subscription manager `parallelize` flag, and on a per-subscription basis via the `parallelize` flag on the subscription itself. (#3709 [https://github.com/ethereum/web3.py/issues/3709])

### Internal Changes - for web3.py Contributors

-

Update integration test suite fixture to test against geth `v1.16.2`. (#3738 [https://github.com/ethereum/web3.py/issues/3738])

-

Add missing async tests for `FormattingMiddleware` as a sanity check. (#3735 [https://github.com/ethereum/web3.py/issues/3735])

## web3.py v7.12.1 (2025-07-14)

### Bugfixes

-

Fix `AutoProvider` batching setup by adding a proxy batch request. (#3712 [https://github.com/ethereum/web3.py/issues/3712])

### Internal Changes - for web3.py Contributors

-

Update integrations tests to use geth `v1.16.0`. (#3727 [https://github.com/ethereum/web3.py/issues/3727])

### Miscellaneous Changes

-

# 3698 [https://github.com/ethereum/web3.py/issues/3698], #3710 [https://github.com/ethereum/web3.py/issues/3710]

## web3.py v7.12.0 (2025-05-22)

### Bugfixes

-

Thread safety for batching and better consistency with `PersistentConnectionProvider` implementations:

-

Make request batching threadsafe by using `contextvars.ContextVar` rather than a global flag for setting the batching state.

-

Deterministically match responses with request ids for `PersistentConnectionProvider` batch requests. (#3705 [https://github.com/ethereum/web3.py/issues/3705])
