# Source: https://docs.debricked.com/overview/language-support/python-pip-pipenv.md

# Python - Pip, Pipenv, UV, poetry

OpenText Core SCA now tracks Python dependencies through:

* Pip (using the older *requirements.txt* files)
* Pipenv (using the newer *Pipfile.lock* files)
* UV (using the newer *uv.lock* files)
* poetry (using the newer *poetry.lock* files)
* [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting), to find dependencies not defined in manifest-files

### Pip

To achieve the fastest and most accurate results, create a file containing the resolved dependency tree before scanning. This can be accomplished using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology in [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). By executing the *resolve* command, the CLI automatically identifies all manifest files that lack the recommended lock files and generates them as needed. The first part of the name is based on the name of the file it was generated from. The file naming format is as follows:

```
<FILE_NAME>.pip.debricked.lock
```

Example: *.requirements.txt.pip.debricked.lock*

If at least one of the supported files is committed to the repository, it will be automatically scanned for dependencies when integrated with OpenText Core SCA CI/CD pipeline.

### File fingerprinting

OpenText Core SCA supports scanning for Python dependencies not defined in manifest files through **file fingerprinting.** OpenText Core SCA database contains the hashes of .whl files as well as their unpacked contents (including .py files) for all packages in the Python package index (PyPI). This is used when comparing with the contents of your application, to ensure as accurate matches as possible.&#x20;

For more information on file fingerprinting and how to set it up, see [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting).

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th><th data-hidden data-type="checkbox">High Performance Scan</th></tr></thead><tbody><tr><td>Pip</td><td><em>requirements.txt</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td><td>true</td></tr><tr><td>Pipenv</td><td><em>Pipfile</em></td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td></td><td>false</td></tr><tr><td>Pipenv</td><td><em>Pipfile.lock</em></td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td><td>true</td></tr><tr><td>UV</td><td><em>pyproject.toml</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td><td>false</td></tr><tr><td>UV</td><td><em>uv.lock</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td><td>false</td></tr><tr><td>poetry</td><td><em>pyproject.toml</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td><td>false</td></tr><tr><td>poetry</td><td><em>poetry.lock</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td><td>false</td></tr><tr><td>-</td><td>fingerprinted files (.py, .txt, .sh, .c, .egg, .h and more**)</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>-</td><td>false</td></tr></tbody></table>

\**This is a native lock file format. Native lock file formats are the fastest formats to scan.*
