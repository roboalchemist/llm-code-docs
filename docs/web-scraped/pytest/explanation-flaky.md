# Source: https://docs.pytest.org/en/stable/explanation/flaky.html

# Flaky tests[¶](#flaky-tests "Link to this heading")

A "flaky" test is one that exhibits intermittent or sporadic failure, that seems to have non-deterministic behaviour. Sometimes it passes, sometimes it fails, and it's not clear why. This page discusses pytest features that can help and other general strategies for identifying, fixing or mitigating them.

## Why flaky tests are a problem[¶](#why-flaky-tests-are-a-problem "Link to this heading")

Flaky tests are particularly troublesome when a continuous integration (CI) server is being used, so that all tests must pass before a new code change can be merged. If the test result is not a reliable signal -- that a test failure means the code change broke the test -- developers can become mistrustful of the test results, which can lead to overlooking genuine failures. It is also a source of wasted time as developers must re-run test suites and investigate spurious failures.

## Potential root causes[¶](#potential-root-causes "Link to this heading")

### System state[¶](#system-state "Link to this heading")

Broadly speaking, a flaky test indicates that the test relies on some system state that is not being appropriately controlled - the test environment is not sufficiently isolated. Higher level tests are more likely to be flaky as they rely on more state.

Flaky tests sometimes appear when a test suite is run in parallel (such as use of [pytest-xdist](https://github.com/pytest-dev/pytest-xdist)). This can indicate a test is reliant on test ordering.

-   Perhaps a different test is failing to clean up after itself and leaving behind data which causes the flaky test to fail.

-   The flaky test is reliant on data from a previous test that doesn't clean up after itself, and in parallel runs that previous test is not always present

-   Tests that modify global state typically cannot be run in parallel.

### Overly strict assertion[¶](#overly-strict-assertion "Link to this heading")

Overly strict assertions can cause problems with floating point comparison as well as timing issues. [[`pytest.approx()`]](../reference/reference.html#pytest.approx "pytest.approx") is useful here.

### Thread safety[¶](#thread-safety "Link to this heading")

pytest is single-threaded, executing its tests always in the same thread, sequentially, never spawning any threads itself.

Even in case of plugins which run tests in parallel, for example [pytest-xdist](https://github.com/pytest-dev/pytest-xdist), usually work by spawning multiple *processes* and running tests in batches, without using multiple threads.

It is of course possible (and common) for tests and fixtures to spawn threads themselves as part of their testing workflow (for example, a fixture that starts a server thread in the background, or a test which executes production code that spawns threads), but some care must be taken:

-   Make sure to eventually wait on any spawned threads -- for example at the end of a test, or during the teardown of a fixture.

-   Avoid using primitives provided by pytest ([[`pytest.warns()`]](../reference/reference.html#pytest.warns "pytest.warns"), [[`pytest.raises()`]](../reference/reference.html#pytest.raises "pytest.raises"), etc) from multiple threads, as they are not thread-safe.

If your test suite uses threads and your are seeing flaky test results, do not discount the possibility that the test is implicitly using global state in pytest itself.

## Related features[¶](#related-features "Link to this heading")

### Xfail strict[¶](#xfail-strict "Link to this heading")

[[pytest.mark.xfail]](../reference/reference.html#pytest-mark-xfail-ref) with [`strict=False`] can be used to mark a test so that its failure does not cause the whole build to break. This could be considered like a manual quarantine, and is rather dangerous to use permanently.

### PYTEST_CURRENT_TEST[¶](#pytest-current-test "Link to this heading")

[][[`PYTEST_CURRENT_TEST`]](../reference/reference.html#envvar-PYTEST_CURRENT_TEST) may be useful for figuring out "which test got stuck". See [[PYTEST_CURRENT_TEST environment variable]](../example/simple.html#pytest-current-test-env) for more details.

### Plugins[¶](#plugins "Link to this heading")

Rerunning any failed tests can mitigate the negative effects of flaky tests by giving them additional chances to pass, so that the overall build does not fail. Several pytest plugins support this:

-   [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)

-   [pytest-replay](https://github.com/ESSS/pytest-replay): This plugin helps to reproduce locally crashes or flaky tests observed during CI runs.

-   [pytest-flakefinder](https://github.com/dropbox/pytest-flakefinder) - [blog post](https://blogs.dropbox.com/tech/2016/03/open-sourcing-pytest-tools/)

Plugins to deliberately randomize tests can help expose tests with state problems:

-   [pytest-random-order](https://github.com/jbasko/pytest-random-order)

-   [pytest-randomly](https://github.com/pytest-dev/pytest-randomly)

## Other general strategies[¶](#other-general-strategies "Link to this heading")

### Split up test suites[¶](#split-up-test-suites "Link to this heading")

It can be common to split a single test suite into two, such as unit vs integration, and only use the unit test suite as a CI gate. This also helps keep build times manageable as high level tests tend to be slower. However, it means it does become possible for code that breaks the build to be merged, so extra vigilance is needed for monitoring the integration test results.

### Video/screenshot on failure[¶](#video-screenshot-on-failure "Link to this heading")

For UI tests these are important for understanding what the state of the UI was when the test failed. pytest-splinter can be used with plugins like pytest-bdd and can [save a screenshot on test failure](https://pytest-splinter.readthedocs.io/en/latest/#automatic-screenshots-on-test-failure), which can help to isolate the cause.

### Delete or rewrite the test[¶](#delete-or-rewrite-the-test "Link to this heading")

If the functionality is covered by other tests, perhaps the test can be removed. If not, perhaps it can be rewritten at a lower level which will remove the flakiness or make its source more apparent.

### Quarantine[¶](#quarantine "Link to this heading")

Mark Lapierre discusses the [Pros and Cons of Quarantined Tests](https://dev.to/mlapierre/pros-and-cons-of-quarantined-tests-2emj) in a post from 2018.

### CI tools that rerun on failure[¶](#ci-tools-that-rerun-on-failure "Link to this heading")

Azure Pipelines (the Azure cloud CI/CD tool, formerly Visual Studio Team Services or VSTS) has a feature to [identify flaky tests](https://docs.microsoft.com/en-us/previous-versions/azure/devops/2017/dec-11-vsts?view=tfs-2017#identify-flaky-tests) and rerun failed tests.

## Research[¶](#research "Link to this heading")

This is a limited list, please submit an issue or pull request to expand it!

-   Gao, Zebao, Yalan Liang, Myra B. Cohen, Atif M. Memon, and Zhen Wang. "Making system user interactive tests repeatable: When and what should we control?." In *Software Engineering (ICSE), 2015 IEEE/ACM 37th IEEE International Conference on*, vol. 1, pp. 55-65. IEEE, 2015. [PDF](http://www.cs.umd.edu/~atif/pubs/gao-icse15.pdf)

-   Palomba, Fabio, and Andy Zaidman. "Does refactoring of test smells induce fixing flaky tests?." In *Software Maintenance and Evolution (ICSME), 2017 IEEE International Conference on*, pp. 1-12. IEEE, 2017. [PDF in Google Drive](https://drive.google.com/file/d/10HdcCQiuQVgW3yYUJD-TSTq1NbYEprl0/view)

-   Bell, Jonathan, Owolabi Legunsen, Michael Hilton, Lamyaa Eloussi, Tifany Yung, and Darko Marinov. "DeFlaker: Automatically detecting flaky tests." In *Proceedings of the 2018 International Conference on Software Engineering*. 2018. [PDF](https://www.jonbell.net/icse18-deflaker.pdf#section-Research)

-   Dutta, Saikat and Shi, August and Choudhary, Rutvik and Zhang, Zhekun and Jain, Aryaman and Misailovic, Sasa. "Detecting flaky tests in probabilistic and machine learning applications." In *Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA)*, pp. 211-224. ACM, 2020. [PDF](https://www.cs.cornell.edu/~saikatd/papers/flash-issta20.pdf)

-   Habchi, Sarra and Haben, Guillaume and Sohn, Jeongju and Franci, Adriano and Papadakis, Mike and Cordy, Maxime and Le Traon, Yves. "What Made This Test Flake? Pinpointing Classes Responsible for Test Flakiness." In Proceedings of the 38th IEEE International Conference on Software Maintenance and Evolution (ICSME), IEEE, 2022. [PDF](https://arxiv.org/abs/2207.10143)

-   Lamprou, Sokrates. "Non-deterministic tests and where to find them: Empirically investigating the relationship between flaky tests and test smells by examining test order dependency." Bachelor thesis, Department of Computer and Information Science, Linköping University, 2022. LIU-IDA/LITH-EX-G--19/056--SE. [PDF](https://www.diva-portal.org/smash/get/diva2:1713691/FULLTEXT01.pdf)

-   Leinen, Fabian and Elsner, Daniel and Pretschner, Alexander and Stahlbauer, Andreas and Sailer, Michael and Jürgens, Elmar. "Cost of Flaky Tests in Continuous Integration: An Industrial Case Study." Technical University of Munich and CQSE GmbH, Munich, Germany, 2023. [PDF](https://mediatum.ub.tum.de/doc/1730194/1730194.pdf)

## Resources[¶](#resources "Link to this heading")

-   [Eradicating Non-Determinism in Tests](https://martinfowler.com/articles/nonDeterminism.html) by Martin Fowler, 2011

-   [No more flaky tests on the Go team](https://www.thoughtworks.com/insights/blog/no-more-flaky-tests-go-team) by Pavan Sudarshan, 2012

-   [The Build That Cried Broken: Building Trust in your Continuous Integration Tests](https://www.youtube.com/embed/VotJqV4n8ig) talk (video) by [Angie Jones](https://angiejones.tech/) at SeleniumConf Austin 2017

-   [Test and Code Podcast: Flaky Tests and How to Deal with Them](https://testandcode.com/50) by Brian Okken and Anthony Shaw, 2018

-   Microsoft:

    -   [How we approach testing VSTS to enable continuous delivery](https://blogs.msdn.microsoft.com/bharry/2017/06/28/testing-in-a-cloud-delivery-cadence/) by Brian Harry MS, 2017

    -   [Eliminating Flaky Tests](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/eliminating-flaky-tests) blog and talk (video) by Munil Shah, 2017

-   Google:

    -   [Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) by John Micco, 2016

    -   [Where do Google's flaky tests come from?](https://testing.googleblog.com/2017/04/where-do-our-flaky-tests-come-from.html) by Jeff Listfield, 2017

-   Dropbox: \* [Athena: Our automated build health management system](https://dropbox.tech/infrastructure/athena-our-automated-build-health-management-system) by Utsav Shah, 2019 \* [How To Manage Flaky Tests in your CI Workflows](https://mill-build.org/blog/4-flaky-tests.html) by Li Haoyi, 2025

-   Uber: \* [Handling Flaky Unit Tests in Java](https://www.uber.com/blog/handling-flaky-tests-java/) by Uber Engineering, 2021 \* [Flaky Tests Overhaul at Uber](https://www.uber.com/blog/flaky-tests-overhaul/) by Uber Engineering, 2024