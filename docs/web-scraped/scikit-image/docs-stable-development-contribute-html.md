# Source: https://scikit-image.org/docs/stable/development/contribute.html

Title: How to contribute to scikit-image — skimage 0.26.0 documentation

URL Source: https://scikit-image.org/docs/stable/development/contribute.html

Markdown Content:
Developing open source software as part of a community is fun, and often quite educational!

We coordinate our work using GitHub, where you can find lists of [open issues](https://github.com/scikit-image/scikit-image/issues?q=is%3Aopen) and [new feature requests](https://github.com/scikit-image/scikit-image/labels/%3Apray%3A%20Feature%20request).

To follow along with discussions, or to get in touch with the developer team, please join us on the [scikit-image developer forum](https://discuss.scientific-python.org/c/contributor/skimage) and the [Zulip chat](https://skimage.zulipchat.com/).

Please post questions to these public forums (rather than contacting developers directly); that way, everyone can benefit from the answers, and developers can answer according to their availability. Don’t feel shy, the team is very friendly!

*   [Development process](https://scikit-image.org/docs/stable/development/contribute.html#development-process)

*   [Divergence between `upstream main` and your feature branch](https://scikit-image.org/docs/stable/development/contribute.html#divergence-between-upstream-main-and-your-feature-branch)

*   [Guidelines](https://scikit-image.org/docs/stable/development/contribute.html#guidelines)

*   [Stylistic Guidelines](https://scikit-image.org/docs/stable/development/contribute.html#stylistic-guidelines)

*   [Testing](https://scikit-image.org/docs/stable/development/contribute.html#testing)

    *   [Warnings during testing phase](https://scikit-image.org/docs/stable/development/contribute.html#warnings-during-testing-phase)

*   [Test coverage](https://scikit-image.org/docs/stable/development/contribute.html#test-coverage)

*   [Building docs](https://scikit-image.org/docs/stable/development/contribute.html#building-docs)

    *   [Gallery](https://scikit-image.org/docs/stable/development/contribute.html#gallery)

    *   [Fixing Warnings](https://scikit-image.org/docs/stable/development/contribute.html#fixing-warnings)

*   [Deprecation cycle (advanced)](https://scikit-image.org/docs/stable/development/contribute.html#deprecation-cycle-advanced)

    *   [Raising Warnings](https://scikit-image.org/docs/stable/development/contribute.html#raising-warnings)

    *   [Deprecating Keywords and Functions](https://scikit-image.org/docs/stable/development/contribute.html#deprecating-keywords-and-functions)

*   [Adding Data](https://scikit-image.org/docs/stable/development/contribute.html#adding-data)

*   [Benchmarks](https://scikit-image.org/docs/stable/development/contribute.html#benchmarks)

    *   [Prerequisites](https://scikit-image.org/docs/stable/development/contribute.html#prerequisites)

    *   [Writing a benchmark](https://scikit-image.org/docs/stable/development/contribute.html#writing-a-benchmark)

    *   [Testing the benchmarks locally](https://scikit-image.org/docs/stable/development/contribute.html#testing-the-benchmarks-locally)

    *   [Running your benchmark](https://scikit-image.org/docs/stable/development/contribute.html#running-your-benchmark)

    *   [Comparing results to main](https://scikit-image.org/docs/stable/development/contribute.html#comparing-results-to-main)

[Development process](https://scikit-image.org/docs/stable/development/contribute.html#id1)[#](https://scikit-image.org/docs/stable/development/contribute.html#development-process "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following is a brief overview about how changes to source code and documentation can be contributed to scikit-image.

1.   If you are a first-time contributor:

    *   Go to [scikit-image/scikit-image](https://github.com/scikit-image/scikit-image) and click the “fork” button to create your own copy of the project.

    *   [Set up GitHub SSH authentication](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

    *   Clone (download) the repository with the project source on your local computer:

git clone --origin upstream git@github.com:scikit-image/scikit-image 
    *   Change into the root directory of the cloned repository:

cd scikit-image 
    *   Add your fork as a [remote repository](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) that you will interact with.

Assuming a GitHub username of `codemonkey`:

git remote add codemonkey git@github.com:codemonkey/scikit-image
git fetch codemonkey 
    *   You now have two remote repositories:

        *   `upstream`, which refers to the `scikit-image` project repository, and

        *   `codemonkey`, which refers to your personal fork.

    *   Next, [set up your build environment](https://scikit-image.org/docs/stable/user_guide/install.html#build-env-setup).

    *   Finally, we recommend that you use our pre-commit hook, which runs code checkers and formatters each time you do a `git commit`:

pip install pre-commit
pre-commit install 

2.   Develop your contribution:

    *   Pull the latest changes from the project:

git switch main
git fetch upstream main
git merge upstream/main 
    *   Create a branch for the feature you want to work on. Use a sensible name, such as ‘transform-speedups’:

git switch -c transform-speedups 
    *   Commit locally as you progress (with `git add` and `git commit`). Please write [good commit messages](https://vxlabs.com/software-development-handbook/#good-commit-messages).

3.   To submit your contribution:

    *   Push your changes back to your fork on GitHub:

git push codemonkey transform-speedups 
A message will be displayed with a URL to open in your browser to create a pull request (PR). Open it and click the green button.

1.   Review process:

    *   Reviewers (the other developers and interested community members) will write inline and/or general comments on your pull request (PR) to help you improve its implementation, documentation, and style. Every single developer working on the project has their code reviewed, and we’ve come to see it as a friendly conversation from which we all learn and the overall code quality benefits. Therefore, please don’t let the review discourage you from contributing: its only aim is to improve the quality of the project, not to criticize (we are, after all, very grateful for the time you’re putting in!).

    *   To update your pull request, make your changes on your local repository and commit. As soon as those changes are pushed up (to the same branch as before) the pull request will update automatically.

    *   Continuous integration (CI) services are triggered after each pull request submission to build the package, run unit tests, and check the coding style and formatting of your branch. The tests must pass before your PR can be merged. If CI fails, you can find out why by clicking on the “failed” icon (red cross) and inspecting the build and test logs.

Note

PR labeling

CI will always fail on new PRs, until a maintainer adds a suitable category label. 
    *   A pull request must be approved by two core team members before merging.

1.   Document changes

If your change introduces a deprecation, add a reminder to `TODO.txt` for the team to remove the deprecated functionality in the future.

scikit-image uses [changelist](https://github.com/scientific-python/changelist) to generate a list of release notes automatically from pull requests. By default, changelist will use the title of a pull request and its GitHub labels to sort it into the appropriate section. However, for more complex changes, we encourage you to describe them in more detail using the `release-note` code block within the pull request description; e.g.:

```release-note
Remove the deprecated function `skimage.color.blue`. Blend
`skimage.color.cyan` and `skimage.color.magenta` instead.
``` 
You can refer to [Release notes](https://scikit-image.org/docs/stable/release_notes/index.html) for examples and to [changelist’s documentation](https://github.com/scientific-python/changelist) for more details.

Note

To reviewers: if it is not obvious from the PR description, make sure that the reason and context for a change are described in the merge message.

[Divergence between `upstream main` and your feature branch](https://scikit-image.org/docs/stable/development/contribute.html#id2)[#](https://scikit-image.org/docs/stable/development/contribute.html#divergence-between-upstream-main-and-your-feature-branch "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If GitHub indicates that the branch of your PR can no longer be merged automatically, merge the main branch into yours:

git fetch upstream main
git merge upstream/main

If any conflicts occur, they need to be [fixed before continuing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line).

[We recommend](https://github.com/stefanv/git-tools?tab=readme-ov-file#conflict-diff-display) setting:

git config --global merge.conflictstyle zdiff3

to make conflict markers easier to read.

An alternative to merging is to rebase your branch—but we squash and merge all PRs anyway, so we don’t mind merge commits.

[Guidelines](https://scikit-image.org/docs/stable/development/contribute.html#id3)[#](https://scikit-image.org/docs/stable/development/contribute.html#guidelines "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   All code should have tests (see [test coverage](https://scikit-image.org/docs/stable/development/contribute.html#test-coverage) below for more details).

*   All code should be documented, to the same [standard](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) as NumPy and SciPy.

*   For new functionality, always add an example to the gallery (see [Gallery](https://scikit-image.org/docs/stable/development/contribute.html#gallery) below for more details).

*   No changes are ever merged without review and approval by two core team members. There are two exceptions to this rule. First, pull requests which affect only the documentation require review and approval by only one core team member in most cases. If the maintainer feels the changes are large or likely to be controversial, two reviews should still be encouraged. The second case is that of minor fixes which restore CI to a working state, because these should be merged fairly quickly. Reach out on the [developer forum](https://discuss.scientific-python.org/c/contributor/skimage) if you get no response to your pull request. **Never merge your own pull request.**

[Stylistic Guidelines](https://scikit-image.org/docs/stable/development/contribute.html#id4)[#](https://scikit-image.org/docs/stable/development/contribute.html#stylistic-guidelines "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Use the following import conventions:

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import skimage as ski

sp.ndimage.label(...)
ski.measure.label(...) 
*   Use numpy data types instead of strings (`np.uint8` instead of `"uint8"`).

*   When documenting array parameters, use `image : (M, N) ndarray` and then refer to `M` and `N` in the docstring, if necessary.

*   Refer to array dimensions as (plane), row, column, not as x, y, z. See [Coordinate conventions](https://scikit-image.org/docs/stable/user_guide/numpy_images.html#numpy-images-coordinate-conventions) in the user guide for more information.

*   Functions should support all input image dtypes. Use utility functions such as `img_as_float` to help convert to an appropriate type. The output format can be whatever is most efficient. This allows us to string together several functions into a pipeline, e.g.:

hough(canny(my_image)) 
*   Use relative module imports, i.e. `from .._shared import xyz` rather than `from skimage._shared import xyz`.

*   For Cython functions:

    *   Release the GIL whenever possible, using `with nogil:`.

    *   Wrap Cython code in a pure Python function, which defines the API. This improves compatibility with code introspection tools, which are often not aware of Cython code.

*   Use `Py_ssize_t` as data type for all indexing, shape and size variables in C/C++ and Cython code.

[Testing](https://scikit-image.org/docs/stable/development/contribute.html#id5)[#](https://scikit-image.org/docs/stable/development/contribute.html#testing "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The test suite must pass before a pull request can be merged, and tests should be added to cover all modifications in behavior.

We use the [pytest](https://docs.pytest.org/en/latest/) testing framework, with tests located in the various `skimage/submodule/tests` folders.

Testing requirements are listed in `requirements/test.txt`. Run:

*   **All tests**: `spin test`

*   Tests for a **submodule**: `spin test src/skimage/morphology`

*   Run tests from a **specific file**: `spin test tests/skimage/morphology/tests/test_gray.py`

*   Run **a test inside a file**: `spin test tests/skimage/morphology/tests/test_gray.py::test_3d_fallback_black_tophat`

*   Run tests with **arbitrary ``pytest`` options**: `spin test -- any pytest args you want`.

*   Run tests **matching** a specific expression: `spin test -- -k threshold`

*   Run all tests and **doctests**: `spin test --with-doctest`

### [Warnings during testing phase](https://scikit-image.org/docs/stable/development/contribute.html#id6)[#](https://scikit-image.org/docs/stable/development/contribute.html#warnings-during-testing-phase "Link to this heading")

By default, warnings raised by the test suite result in errors. You can switch that behavior off by setting the environment variable `SKIMAGE_TEST_STRICT_WARNINGS` to `0`.

[Test coverage](https://scikit-image.org/docs/stable/development/contribute.html#id7)[#](https://scikit-image.org/docs/stable/development/contribute.html#test-coverage "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests for a module should ideally cover all code in that module, i.e., statement coverage should be at 100%.

To measure test coverage run:

$ spin test --coverage

This will run tests and print a report with one line for each file in [`skimage`](https://scikit-image.org/docs/stable/api/skimage.html#module-skimage "skimage"), detailing the test coverage:

Name                                             Stmts   Exec  Cover   Missing
------------------------------------------------------------------------------
skimage/color/colorconv                             77     77   100%
skimage/filter/ __init__                               1      1   100%
...

[Building docs](https://scikit-image.org/docs/stable/development/contribute.html#id8)[#](https://scikit-image.org/docs/stable/development/contribute.html#building-docs "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To build the HTML documentation, run:

spin docs

Output is in `scikit-image/doc/build/html/`. Add the `--clean` flag to build from scratch, deleting any cached output.

### [Gallery](https://scikit-image.org/docs/stable/development/contribute.html#id9)[#](https://scikit-image.org/docs/stable/development/contribute.html#gallery "Link to this heading")

The example gallery is built using [Sphinx-Gallery](https://sphinx-gallery.github.io/). Refer to their documentation for complete usage instructions, and also to existing examples in `doc/examples`.

Gallery examples should have a maximum figure width of 8 inches. You can also [change a gallery entry’s thumbnail](https://sphinx-gallery.github.io/stable/configuration.html#choosing-thumbnail).

### [Fixing Warnings](https://scikit-image.org/docs/stable/development/contribute.html#id10)[#](https://scikit-image.org/docs/stable/development/contribute.html#fixing-warnings "Link to this heading")

*   “citation not found: R###” There is probably an underscore after a reference in the first line of a docstring (e.g. [1]_). Use this method to find the source file: $ cd doc/build; grep -rin R####

*   “Duplicate citation R###, other instance in…”” There is probably a [2] without a [1] in one of the docstrings

*   Make sure to use pre-sphinxification paths to images (not the _images directory)

[Deprecation cycle (advanced)](https://scikit-image.org/docs/stable/development/contribute.html#id11)[#](https://scikit-image.org/docs/stable/development/contribute.html#deprecation-cycle-advanced "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the way a function is called has to be changed, a deprecation cycle must be followed to warn users.

A deprecation cycle is _not_ necessary when:

*   adding a new function, or

*   adding a new keyword argument to the _end_ of a function signature, or

*   fixing unexpected or incorrect behavior.

A deprecation cycle is necessary when:

*   renaming keyword arguments, or

*   changing the order of arguments or keywords, or

*   adding arguments to a function, or

*   changing a function’s name or location, or

*   changing the default value of function arguments or keywords.

Typically, deprecation warnings are in place for two releases, before a change is made.

For example, consider the modification of a default value in a function signature. In version N, we have:

def some_function(image, rescale=True):
 """Do something.

 Parameters
 ----------
 image : ndarray
 Input image.
 rescale : bool, optional
 Rescale the image unless ``False`` is given.

 Returns
 -------
 out : ndarray
 The resulting image.
 """
    out = do_something(image, rescale=rescale)
    return out

In version N+1, we will change this to:

def some_function(image, rescale=None):
 """Do something.

 Parameters
 ----------
 image : ndarray
 Input image.
 rescale : bool, optional
 Rescale the image unless ``False`` is given.

 .. warning:: The default value will change from ``True`` to
 ``False`` in skimage N+3.

 Returns
 -------
 out : ndarray
 The resulting image.
 """
    if rescale is None:
        warn('The default value of rescale will change '
             'to `False` in version N+3.', stacklevel=2)
        rescale = True
    out = do_something(image, rescale=rescale)
    return out

And, in version N+3:

def some_function(image, rescale=False):
 """Do something.

 Parameters
 ----------
 image : ndarray
 Input image.
 rescale : bool, optional
 Rescale the image if ``True`` is given.

 Returns
 -------
 out : ndarray
 The resulting image.
 """
    out = do_something(image, rescale=rescale)
    return out

Here is the process for a 3-release deprecation cycle:

*   Set the default to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), and modify the docstring to specify that the default is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)").

*   In the function, _if_ rescale is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), set it to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)") and warn that the default will change to [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)") in version N+3.

*   In `doc/release/release_dev.rst`, under deprecations, add “In `some_function`, the `rescale` argument will default to [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)") in N+3.”

*   In `TODO.txt`, create an item in the section related to version N+3 and write “change rescale default to False in some_function”.

Note that the 3-release deprecation cycle is not a strict rule and, in some cases, developers can agree on a different procedure.

### [Raising Warnings](https://scikit-image.org/docs/stable/development/contribute.html#id12)[#](https://scikit-image.org/docs/stable/development/contribute.html#raising-warnings "Link to this heading")

`skimage` raises `FutureWarning`s to highlight changes in its API, e.g.:

from warnings import warn
warn(
    "Automatic detection of the color channel was deprecated in "
    "v0.19, and `channel_axis=None` will be the new default in "
    "v0.22. Set `channel_axis=-1` explicitly to silence this "
    "warning.",
    FutureWarning,
    stacklevel=2,
)

The [stacklevel](https://docs.python.org/3/library/warnings.html#warnings.warn) is a bit of a technicality, but ensures that the warning points to the user-called function, and not to a utility function within.

In most cases, set the `stacklevel` to `2`. When warnings originate from helper routines internal to the scikit-image library, set it to `3`.

To test if your warning is being emitted correctly, try calling the function from an IPython console. It should point you to the console input itself instead of being emitted by files in the scikit-image library:

*   **Good**: `ipython:1: UserWarning: ...`

*   **Bad**: `scikit-image/skimage/measure/_structural_similarity.py:155: UserWarning:`

### [Deprecating Keywords and Functions](https://scikit-image.org/docs/stable/development/contribute.html#id13)[#](https://scikit-image.org/docs/stable/development/contribute.html#deprecating-keywords-and-functions "Link to this heading")

When removing keywords or entire functions, the `skimage._shared.utils.deprecate_parameter` and `skimage._shared.utils.deprecate_func` utility functions can be used to perform the above procedure.

[Adding Data](https://scikit-image.org/docs/stable/development/contribute.html#id14)[#](https://scikit-image.org/docs/stable/development/contribute.html#adding-data "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While code is hosted on [github](https://github.com/scikit-image/), example datasets are on [gitlab](https://gitlab.com/scikit-image/data). These are fetched with [pooch](https://github.com/fatiando/pooch) when accessing `skimage.data.*`.

New datasets are submitted on gitlab and, once merged, the data registry `skimage/data/_registry.py` in the main GitHub repository can be updated.

[Benchmarks](https://scikit-image.org/docs/stable/development/contribute.html#id15)[#](https://scikit-image.org/docs/stable/development/contribute.html#benchmarks "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While not mandatory for most pull requests, we ask that performance-related PRs include a benchmark in order to clearly depict the use case that is being optimized for.

In this section we will review how to setup the benchmarks, and three commands `spin asv -- dev`, `spin asv -- run` and `spin asv -- continuous`.

### [Prerequisites](https://scikit-image.org/docs/stable/development/contribute.html#id16)[#](https://scikit-image.org/docs/stable/development/contribute.html#prerequisites "Link to this heading")

Begin by installing [airspeed velocity](https://asv.readthedocs.io/en/stable/) in your development environment. Prior to installation, be sure to activate your development environment, then if using `venv` you may install the requirement with:

source skimage-dev/bin/activate
pip install asv

If you are using conda, then the command:

conda activate skimage-dev
conda install asv

is more appropriate. Once installed, it is useful to run the command:

spin asv -- machine

To let airspeed velocity know more information about your machine.

### [Writing a benchmark](https://scikit-image.org/docs/stable/development/contribute.html#id17)[#](https://scikit-image.org/docs/stable/development/contribute.html#writing-a-benchmark "Link to this heading")

To write benchmark, add a file in the `benchmarks` directory which contains a a class with one `setup` method and at least one method prefixed with `time_`.

The `time_` method should only contain code you wish to benchmark. Therefore it is useful to move everything that prepares the benchmark scenario into the `setup` method. This function is called before calling a `time_` method and its execution time is not factored into the benchmarks.

Take for example the `TransformSuite` benchmark:

import numpy as np
from skimage import transform

class TransformSuite:
 """Benchmark for transform routines in scikit-image."""

    def setup(self):
        self.image = np.zeros((2000, 2000))
        idx = np.arange(500, 1500)
        self.image[idx[::-1], idx] = 255
        self.image[idx, idx] = 255

    def time_hough_line(self):
        result1, result2, result3 = transform.hough_line(self.image)

Here, the creation of the image is completed in the `setup` method, and not included in the reported time of the benchmark.

It is also possible to benchmark features such as peak memory usage. To learn more about the features, please refer to the official [airspeed velocity documentation](https://asv.readthedocs.io/en/latest/writing_benchmarks.html).

Also, the benchmark files need to be importable when benchmarking old versions of scikit-image. So if anything from scikit-image is imported at the top level, it should be done as:

try:
    from skimage import metrics
except ImportError:
    pass

The benchmarks themselves don’t need any guarding against missing features, only the top-level imports.

To allow tests of newer functions to be marked as “n/a” (not available) rather than “failed” for older versions, the setup method itself can raise a NotImplemented error. See the following example for the registration module:

try:
    from skimage import registration
except ImportError:
    raise NotImplementedError("registration module not available")

### [Testing the benchmarks locally](https://scikit-image.org/docs/stable/development/contribute.html#id18)[#](https://scikit-image.org/docs/stable/development/contribute.html#testing-the-benchmarks-locally "Link to this heading")

Prior to running the true benchmark, it is often worthwhile to test that the code is free of typos. To do so, you may use the command:

spin asv -- dev -b TransformSuite

Where the `TransformSuite` above will be run once in your current environment to test that everything is in order.

### [Running your benchmark](https://scikit-image.org/docs/stable/development/contribute.html#id19)[#](https://scikit-image.org/docs/stable/development/contribute.html#running-your-benchmark "Link to this heading")

The command above is fast, but doesn’t test the performance of the code adequately. To do that you may want to run the benchmark in your current environment to see the performance of your change as you are developing new features. The command `asv run -E existing` will specify that you wish to run the benchmark in your existing environment. This will save a significant amount of time since building scikit-image can be a time consuming task:

spin asv -- run -E existing -b TransformSuite

### [Comparing results to main](https://scikit-image.org/docs/stable/development/contribute.html#id20)[#](https://scikit-image.org/docs/stable/development/contribute.html#comparing-results-to-main "Link to this heading")

Often, the goal of a PR is to compare the results of the modifications in terms speed to a snapshot of the code that is in the main branch of the `scikit-image` repository. The command `asv continuous` is of help here:

spin asv -- continuous main -b TransformSuite

This call will build out the environments specified in the `asv.conf.json` file and compare the performance of the benchmark between your current commit and the code in the main branch.

The output may look something like:

$ spin asv -- continuous main -b TransformSuite
· Creating environments
· Discovering benchmarks
·· Uninstalling from conda-py3.7-cython-numpy1.15-scipy
·· Installing 544c0fe3 <benchmark_docs> into conda-py3.7-cython-numpy1.15-scipy.
· Running 4 total benchmarks (2 commits * 2 environments * 1 benchmarks)
[  0.00%] · For scikit-image commit 37c764cb <benchmark_docs~1> (round 1/2):
[...]
[100.00%] ··· ...ansform.TransformSuite.time_hough_line           33.2±2ms

BENCHMARKS NOT SIGNIFICANTLY CHANGED.

In this case, the differences between HEAD and main are not significant enough for airspeed velocity to report.

It is also possible to get a comparison of results for two specific revisions for which benchmark results have previously been run via the `asv compare` command:

spin asv -- compare v0.14.5 v0.17.2

Finally, one can also run ASV benchmarks only for a specific commit hash or release tag by appending `^!` to the commit or tag name. For example to run the skimage.filter module benchmarks on release v0.17.2:

spin asv -- run -b Filter v0.17.2^!
