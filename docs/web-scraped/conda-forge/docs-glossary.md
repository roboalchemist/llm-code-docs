# Source: https://conda-forge.org/docs/glossary/

Title: Glossary | conda-forge | community-driven packaging for conda

URL Source: https://conda-forge.org/docs/glossary/

Published Time: Wed, 11 Mar 2026 09:21:59 GMT

Markdown Content:
List of frequently used terms and acronyms.

ABI[​](https://conda-forge.org/docs/glossary/#abi "Direct link to ABI")
-----------------------------------------------------------------------

Application Binary Interface. ABI is a document that comprehensively defines the binary system interface between applications and the operating system on which they run.

Learn More at [Wikipedia](https://en.wikipedia.org/wiki/Application_binary_interface) or [pypackaging-native](https://pypackaging-native.github.io/background/binary_interface).

CDN[​](https://conda-forge.org/docs/glossary/#cdn "Direct link to CDN")
-----------------------------------------------------------------------

**C**ontent **D**elivery **N**etwork. CDNs are geographically distributed networks of servers that mirror contents of a primary source. Having multiple servers offering the same content increases performance (reduced latency, higher download speeds) and availability.

[Learn more](https://en.wikipedia.org/wiki/Content_delivery_network).

CDT[​](https://conda-forge.org/docs/glossary/#cdt "Direct link to CDT")
-----------------------------------------------------------------------

Core Dependency Tree. Core Dependency Tree packages take care of the dependencies that are so close to the system that they are not packaged with conda-forge. For example, in conda-forge, we have used repackaged CentOS 6 or 7 binaries for some time.

[Learn more](https://conda-forge.org/docs/maintainer/knowledge_base.html#core-dependency-tree-packages-cdts).

CFEP[​](https://conda-forge.org/docs/glossary/#cfep "Direct link to CFEP")
--------------------------------------------------------------------------

Conda Forge Enhancement Proposal. A CFEP is a document that outlines a suggested change to how the conda-forge project operates, from a technical standpoint as well as to address social topics such as governance and expected conduct.

[Learn More](https://github.com/conda-forge/cfep/blob/main/cfep-01.md/).

CI[​](https://conda-forge.org/docs/glossary/#ci "Direct link to CI")
--------------------------------------------------------------------

Continuous Integration. Continuous integration is the practice of automating the integration of code changes from multiple contributors into a single software project.

[Learn More](https://en.wikipedia.org/wiki/Continuous_integration).

CLI[​](https://conda-forge.org/docs/glossary/#cli "Direct link to CLI")
-----------------------------------------------------------------------

Command Line Interface. A textual interface of a program that allows the user to control the program with a single command line, which is entered in a command-line environment, such as the Miniforge Prompt on Windows, or a terminal on MacOS and Linux. An example of a program offering a CLI is `conda`.

[Learn More](https://en.wikipedia.org/wiki/Command-line_interface).

Conda channel[​](https://conda-forge.org/docs/glossary/#conda-channel "Direct link to Conda channel")
-----------------------------------------------------------------------------------------------------

Conda channels are the locations where packages are stored. They serve as the base for hosting and managing packages. `conda-forge` is one example of a conda channel.

[Learn More](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html).

Conda package[​](https://conda-forge.org/docs/glossary/#conda-package "Direct link to Conda package")
-----------------------------------------------------------------------------------------------------

A conda package is a `.tar.bz2` or `.conda` archive that contains libraries, executable programs, data files and other components, as well as metadata under the `info/` directory. Its contents are unpacked in the installation prefix.

[Learn More](https://en.wikipedia.org/wiki/Conda_%28package_manager%29).

CRAN[​](https://conda-forge.org/docs/glossary/#cran "Direct link to CRAN")
--------------------------------------------------------------------------

Comprehensive R Archive Network. CRAN is a network of FTP and web servers around the world that store identical, up-to-date versions of code and documentation for R.

[Learn More](https://cran.r-project.org/).

Environment[​](https://conda-forge.org/docs/glossary/#environment "Direct link to Environment")
-----------------------------------------------------------------------------------------------

An environment is a tool that helps to keep dependencies required by different projects separate by creating isolated spaces where these dependencies are installed.

[Learn More](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html).

ICU[​](https://conda-forge.org/docs/glossary/#icu "Direct link to ICU")
-----------------------------------------------------------------------

International Components for Unicode. ICU is an open-source project of mature C/C++ and Java libraries for Unicode support, software internationalization, and software globalization.

[Learn More](https://icu.unicode.org/).

PR[​](https://conda-forge.org/docs/glossary/#pr "Direct link to PR")
--------------------------------------------------------------------

Pull Request. A Pull Request is a workflow method to submit contributions to an open development project in which the developer asks for changes committed to an external repository to be considered for inclusion in a project's main repository.

[Learn More](https://help.github.com/articles/about-pull-requests/).

Recipe[​](https://conda-forge.org/docs/glossary/#recipe "Direct link to Recipe")
--------------------------------------------------------------------------------

A recipe is a collection of files required to build a conda package. This includes, at minimum, a [`meta.yaml`](https://conda-forge.org/docs/maintainer/adding_pkgs/#the-recipe-recipeyaml-or-metayaml) file, but can also include license files, patches, build scripts, test scripts etc.

[Learn More](https://docs.conda.io/projects/conda-build/en/stable/resources/define-metadata.html).

Virtual package[​](https://conda-forge.org/docs/glossary/#virtual-package "Direct link to Virtual package")
-----------------------------------------------------------------------------------------------------------

Virtual packages are not real packages that can be downloaded. They are injected by the conda clients at runtime so the solver can consider that metadata as part of the constraints of the problem. By convention, they always start with a double underscore (`__`). Some examples include the type of operating system (Linux, Windows, macOS), or the CUDA version supported by the system (if any).

[Learn More](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-virtual.html).
