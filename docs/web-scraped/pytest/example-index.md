# Source: https://docs.pytest.org/en/stable/example/index.html

[]

# Examples and customization tricks[¶](#examples-and-customization-tricks "Link to this heading")

Here is a (growing) list of examples. [[Contact]](../contact.html#contact) us if you need more examples or have questions. Also take a look at the [[comprehensive documentation]](../contents.html#toc) which contains many example snippets as well. Also, [pytest on stackoverflow.com](http://stackoverflow.com/search?q=pytest) often comes with example answers.

For basic examples, see

-   [[Get Started]](../getting-started.html#get-started) for basic introductory examples

-   [[How to write and report assertions in tests]](../how-to/assert.html#assert) for basic assertion examples

-   [[Fixtures]](../reference/fixtures.html#fixtures) for basic fixture/setup examples

-   [[How to parametrize fixtures and test functions]](../how-to/parametrize.html#parametrize) for basic test function parametrization

-   [[How to use unittest-based tests with pytest]](../how-to/unittest.html#unittest) for basic unittest integration

The following examples aim at various use cases you might encounter.

-   [Demo of Python failure reports with pytest](reportingdemo.html)
-   [Basic patterns and examples](simple.html)
    -   [How to change command line options defaults](simple.html#how-to-change-command-line-options-defaults)
    -   [Pass different values to a test function, depending on command line options](simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options)
    -   [Dynamically adding command line options](simple.html#dynamically-adding-command-line-options)
    -   [Control skipping of tests according to command line option](simple.html#control-skipping-of-tests-according-to-command-line-option)
    -   [Writing well integrated assertion helpers](simple.html#writing-well-integrated-assertion-helpers)
    -   [Detect if running from within a pytest run](simple.html#detect-if-running-from-within-a-pytest-run)
    -   [Adding info to test report header](simple.html#adding-info-to-test-report-header)
    -   [Profiling test duration](simple.html#profiling-test-duration)
    -   [Incremental testing - test steps](simple.html#incremental-testing-test-steps)
    -   [Package/Directory-level fixtures (setups)](simple.html#package-directory-level-fixtures-setups)
    -   [Post-process test reports / failures](simple.html#post-process-test-reports-failures)
    -   [Making test result information available in fixtures](simple.html#making-test-result-information-available-in-fixtures)
    -   [[`PYTEST_CURRENT_TEST`] environment variable](simple.html#pytest-current-test-environment-variable)
    -   [Freezing pytest](simple.html#freezing-pytest)
-   [Parametrizing tests](parametrize.html)
    -   [Generating parameters combinations, depending on command line](parametrize.html#generating-parameters-combinations-depending-on-command-line)
    -   [Different options for test IDs](parametrize.html#different-options-for-test-ids)
    -   [A quick port of "testscenarios"](parametrize.html#a-quick-port-of-testscenarios)
    -   [Deferring the setup of parametrized resources](parametrize.html#deferring-the-setup-of-parametrized-resources)
    -   [Indirect parametrization](parametrize.html#indirect-parametrization)
    -   [Apply indirect on particular arguments](parametrize.html#apply-indirect-on-particular-arguments)
    -   [Parametrizing test methods through per-class configuration](parametrize.html#parametrizing-test-methods-through-per-class-configuration)
    -   [Parametrization with multiple fixtures](parametrize.html#parametrization-with-multiple-fixtures)
    -   [Parametrization of optional implementations/imports](parametrize.html#parametrization-of-optional-implementations-imports)
    -   [Set marks or test ID for individual parametrized test](parametrize.html#set-marks-or-test-id-for-individual-parametrized-test)
    -   [Parametrizing conditional raising](parametrize.html#parametrizing-conditional-raising)
-   [Working with custom markers](markers.html)
    -   [Marking test functions and selecting them for a run](markers.html#marking-test-functions-and-selecting-them-for-a-run)
    -   [Selecting tests based on their node ID](markers.html#selecting-tests-based-on-their-node-id)
    -   [Using [`-k`]` `[`expr`] to select tests based on their name](markers.html#using-k-expr-to-select-tests-based-on-their-name)
    -   [Registering markers](markers.html#registering-markers)
    -   [Marking whole classes or modules](markers.html#marking-whole-classes-or-modules)
    -   [Marking individual tests when using parametrize](markers.html#marking-individual-tests-when-using-parametrize)
    -   [Custom marker and command line option to control test runs](markers.html#custom-marker-and-command-line-option-to-control-test-runs)
    -   [Passing a callable to custom markers](markers.html#passing-a-callable-to-custom-markers)
    -   [Reading markers which were set from multiple places](markers.html#reading-markers-which-were-set-from-multiple-places)
    -   [Marking platform specific tests with pytest](markers.html#marking-platform-specific-tests-with-pytest)
    -   [Automatically adding markers based on test names](markers.html#automatically-adding-markers-based-on-test-names)
-   [A session-fixture which can look at all collected tests](special.html)
-   [Changing standard (Python) test discovery](pythoncollection.html)
    -   [Ignore paths during test collection](pythoncollection.html#ignore-paths-during-test-collection)
    -   [Deselect tests during test collection](pythoncollection.html#deselect-tests-during-test-collection)
    -   [Keeping duplicate paths specified from command line](pythoncollection.html#keeping-duplicate-paths-specified-from-command-line)
    -   [Changing directory recursion](pythoncollection.html#changing-directory-recursion)
    -   [Changing naming conventions](pythoncollection.html#changing-naming-conventions)
    -   [Interpreting cmdline arguments as Python packages](pythoncollection.html#interpreting-cmdline-arguments-as-python-packages)
    -   [Finding out what is collected](pythoncollection.html#finding-out-what-is-collected)
    -   [Customizing test collection](pythoncollection.html#customizing-test-collection)
-   [Working with non-python tests](nonpython.html)
    -   [A basic example for specifying tests in Yaml files](nonpython.html#a-basic-example-for-specifying-tests-in-yaml-files)
-   [Using a custom directory collector](customdirectory.html)
    -   [A basic example for a directory manifest file](customdirectory.html#a-basic-example-for-a-directory-manifest-file)