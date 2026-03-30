# Source: https://docs.bugbug.io/creating-tests/independent-tests.md

# Independent tests

## Why create atomic, independent tests?

A good practice in automation testing is that every test is completely independent of other tests.

**Atomic tests:**

* do not rely on their order&#x20;
* have no dependencies between them, no shared variables
* do not require any additional manual preparation
* they are small, they should verify just one feature

**Benefits of independent end-to-end test cases:**

* Easier debugging
* Can be run in[ parallel](https://docs.bugbug.io/running-tests/parallel-mode)
* Easier team collaboration

## Can I order tests?

Ordering tests it's not recommended practice, because end-to-end tests should be atomic (see [above](#why-create-atomic-independent-tests)).

**Example test case:** \
[register a new user](https://docs.bugbug.io/editing-tests/variables#test-user-registration-and-login-using-variables) --> login to an admin panel --> check if the user exists --> delete the user&#x20;

You might be tempted to create one test for user registration and one for checking if the user is created. **But all of these steps should be in one test only.** You can't split it because one of the tests would need to wait until the first is finished. You won't be able to run the second test without running the first one, it will just lead to problems and so-called *spaghetti* between the tests.&#x20;

Solution: simply create a single test with all of these steps, no dependencies, no problems :smile:

That's why BugBug doesn't allow you to order tests and combine them or create separate "before & after" steps, even in a [test suite](https://docs.bugbug.io/organizing-tests/suites). It's better to [duplicate the tests](https://docs.bugbug.io/creating-tests/duplicating-tests) and use [components to share steps between tests](https://docs.bugbug.io/editing-tests/components).

Here's an e
