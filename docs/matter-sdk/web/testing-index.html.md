# Source: https://project-chip.github.io/connectedhomeip-doc/testing/index.html

# Testing Guides

## Contents

# Testing Guides

The following guide provide an introduction to the testing mechanisms available in the SDK.

## Integration and Certification tests

Integration tests test the entire software stack using the same mechanisms as a standard controller.

The certification tests are all integration tests, since they run against the product as a black box.

* [Integration and Certification tests](integration_tests.html)

* [YAML](yaml.html)

* [Python testing framework](python.html)

* [Enabling tests in the CI](ci_testing.html)

* [Integration test utilities](integration_test_utilities.html)

## Unit testing

Unit tests run on small pieces (“units”) of business logic. They do not use an external controller and instead test at the public interface of the class or function. For clusters, this requires an API that separates the cluster logic from the global ember and message delivery layers.

* [Unit tests](unit_testing.html)

## PICS and PIXIT

* [PICS and PIXIT](pics_and_pixit.html)

## Testing in the CI

* [CI testing](ci_testing.html)
