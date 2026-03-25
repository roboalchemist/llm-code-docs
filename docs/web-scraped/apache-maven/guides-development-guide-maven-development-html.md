# Source: https://maven.apache.org/guides/development/guide-maven-development.html

Title: Developing Maven – Maven

URL Source: https://maven.apache.org/guides/development/guide-maven-development.html

Markdown Content:
[](https://maven.apache.org/guides/development/guide-maven-development.html)
This document describes how to get started developing Maven itself. There is a separate page describing how to [build Maven](https://maven.apache.org/guides/development/guide-building-maven.html).

*   [Finding some work to do](https://maven.apache.org/guides/development/guide-maven-development.html#Finding_some_work_to_do)
*   [Where's the source?](https://maven.apache.org/guides/development/guide-maven-development.html#Where.27s_the_source.3F)
*   [Don't forget tests!](https://maven.apache.org/guides/development/guide-maven-development.html#Don.27t_forget_tests.21)
*   [Creating and submitting a patch](https://maven.apache.org/guides/development/guide-maven-development.html#Creating_and_submitting_a_patch)
    *   [Small amendments of the documentation](https://maven.apache.org/guides/development/guide-maven-development.html#Small_amendments_of_the_documentation)

*   [Pull request acceptance criteria](https://maven.apache.org/guides/development/guide-maven-development.html#Pull_request_acceptance_criteria)
*   [Related Projects](https://maven.apache.org/guides/development/guide-maven-development.html#Related_Projects)
*   [Sub Projects](https://maven.apache.org/guides/development/guide-maven-development.html#Sub_Projects)

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Finding some work to do[](https://maven.apache.org/guides/development/guide-maven-development.html#finding-some-work-to-do)
---------------------------------------------------------------------------------------------------------------------------

First of all you need something to work on. Issues can be found on each GitHub repo issues.

When you find an issue you would like to work on, add a comment in the issue log so the core developers and other people looking for work know that someone is already working on it.

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Where's the source?[](https://maven.apache.org/guides/development/guide-maven-development.html#wheres-the-source)
-----------------------------------------------------------------------------------------------------------------

See [https://maven.apache.org/scm.html](https://maven.apache.org/scm.html) for information. The Maven project uses the Apache GitBox Repositories, and all of them are dual-mirrored to [GitHub](https://github.com/apache/).

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Don't forget tests![](https://maven.apache.org/guides/development/guide-maven-development.html#dont-forget-tests)
-----------------------------------------------------------------------------------------------------------------

You will find many unit tests. If at all possible, create or modify a unit test to demonstrate the problem, and then validate your fix.

If you need to mock a class to write a test, use the Mockito framework. Parts of the Maven codebase predate Mockito so you will encounter existing tests that use EasyMock, PowerMock, and JMock. However, all newly written mocks should use Mockito, even if this means a module or a single class uses multiple mocking frameworks. If an existing test class has complicated legacy mock setup, you can add new Mockito based tests in a new test class. There is no requirement that all tests for a single model class must be in the same test class. It is OK to have multiple test classes per model class.

If the problem case can't be set up in the unit tests, add an integration test. Before submitting a patch, in any case, you should run all integration tests. The tests require an empty local repository. See [Core IT Suite documentation](https://maven.apache.org/core-its/core-it-suite/) for more details.

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Creating and submitting a patch[](https://maven.apache.org/guides/development/guide-maven-development.html#creating-and-submitting-a-patch)
-------------------------------------------------------------------------------------------------------------------------------------------

The most convenient way is to create a GitHub fork from the Git repository you are working with. When you have either completed an issue or just want some feedback on the work you have done, create a pull request. We have a couple of guidelines when submitting contributions:

*   Verify the status of the `master` branch on [Maven CI](https://ci-maven.apache.org/job/Maven/job/maven-box/job/maven-dist-tool/job/master/site/dist-tool-master-jobs.html).
*   If it is not `SUCCESS`, then first try to figure out the problem. Don't start with your own issue yet. You can use `git bisect` to figure out the problematic commit and help with that committer to solve the problem.
*   Create your branch from `master`, not from a tag. Otherwise, your patch is outdated the moment you create it and might not be applicable to the development head.
*   Name the branch after the issue number; the branch name would start with `-<ticket-id>`.
*   Push your branch with the commit(s) to your fork.
*   Create a [pull request](https://help.github.com/en/articles/about-pull-requests) to submit your contribution. Someone will review the pull request and give you feedback on it.
*   Make sure that you follow our [Maven Code Style And Code Convention](https://maven.apache.org/developers/conventions/code.html).

[](https://maven.apache.org/guides/development/guide-maven-development.html)
### Small amendments of the documentation[](https://maven.apache.org/guides/development/guide-maven-development.html#small-amendments-of-the-documentation)

If you want to submit small site amendments, for example correct a spelling mistake, you don't have to do the full setup described before. You can simply hit the “Edit” button after the page's title in the breadcrumb section on the top of the page. This will open the page's source file on GitHub, where you can edit it and easily open a pull request containing your change.

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Pull request acceptance criteria[](https://maven.apache.org/guides/development/guide-maven-development.html#pull-request-acceptance-criteria)
---------------------------------------------------------------------------------------------------------------------------------------------

There are a number of criteria that a pull request will be judged on:

*   Whether it works and does what is intended. This one is probably obvious!
*   Whether it fits the spirit of the project. Some pull requests may be rejected as they take the project in a different direction than the current development community has chosen. This is usually discussed on an issue well before a pull request is contributed, so if you are unsure, discuss it there or on the mailing lists first. Feel free to continue discussing it (with new justification) if you disagree, or appeal to a wider audience on the mailing lists.
*   Whether it contains tests. It is expected that any pull request relating to functionality will be accompanied by unit tests and/or integration tests. It is strongly desired (and will be requested) for bug fixes too, but will not be the basis for not applying it. At a bare minimum, the change should not decrease the amount of automated test coverage. As a community, we are focusing on increasing the current coverage, as there are several areas that do not receive automated testing.
*   Whether it contains documentation. All new functionality needs to be documented for users, even if it is very rough for someone to expand on later. While rough is acceptable, incomplete is not. As with automated testing, as a community we are striving to increase the current coverage of documentation.

Above all, don't be discouraged. These are the same requirements the current committers should hold each other to as well. And remember, your contributions are always welcome!

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Maven has a few dependencies on other projects:

*   **Plexus**

Plexus is a full-fledged container supporting different kinds of component lifecycles. Its native lifecycle is like any other modern IoC container, using field injection of both requirements and configuration. All core Maven functionality are Plexus components.

You can [read more about Plexus](https://codehaus-plexus.github.io/).

*   **Modello**

Modello is a simple tool for representing an object model and generating code and resources from the model. Maven uses Modello to generate all Java objects, XML readers and writers, XML Schema, and HTML documentation.

You can [read more about Modello](https://codehaus-plexus.github.io/modello/).

*   **Mojo**

“Mojo” is really two things when it comes to Maven: it is both [Maven's plug-in API](https://maven.apache.org/ref/current/maven-plugin-api/) and also [a separate Mojohaus project](http://www.mojohaus.org/) hosting a lot of plugins.

[The MojoHaus Project](http://www.mojohaus.org/) is a plugin forge for non-core Maven plugins. There is also a lower bar for becoming a part of the project.

[](https://maven.apache.org/guides/development/guide-maven-development.html)
Sub Projects[](https://maven.apache.org/guides/development/guide-maven-development.html#sub-projects)
-----------------------------------------------------------------------------------------------------

*   **Maven Surefire**

Surefire is a testing framework. It can run regular JUnit tests so you won't have to change anything in your code to use it. It supports scripting tests in BeanShell and Jython and has special “batteries” for writing acceptance and functional tests for the web and for testing XML-RPC code.

You can [read more about Surefire](https://maven.apache.org/surefire/).

*   **Maven Doxia**

Doxia is Maven's documentation engine. It has a sink and parser API that can be used to plug in support for input and output documents.

You can read more about [Doxia](https://maven.apache.org/doxia/) and the currently supported [document formats](https://maven.apache.org/doxia/references/index.html).

*   **Maven SCM**

Maven SCM (Source Control Management) is a reusable API which is independent of Maven itself. It is used by the SCM related Maven Plugins. The core part of Maven doesn't depend on Maven SCM.

You can [read more about Scm](https://maven.apache.org/scm/).

*   **Maven Wagon**

Maven Wagon is a standalone API that dealt with transporting files and directories in Maven 2.x. Maven Core today uses the Resolver Transport API, that among other implementations, contains a wrapper for Wagon as well. Also, the site plugin uses it to publish the site.

You can [read more about Wagon](https://maven.apache.org/wagon/).
