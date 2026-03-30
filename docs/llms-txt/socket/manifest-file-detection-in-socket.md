# Source: https://docs.socket.dev/docs/manifest-file-detection-in-socket.md

# Manifest File Detection

Socket's file detection system is designed to identify and analyze key manifest files and specific patterns across various programming languages and package managers. These manifest files are crucial for dependency management and security auditing, allowing Socket to provide comprehensive security insights and alerts. Here’s how Socket detects and recognizes these files:

#### Supported Manifest Files

Socket automatically scans for a variety of manifest file types. The primary file types it looks for include:

* **Python (PyPI):**
  * `requirements.txt`
  * `requirements/*.txt` (when placed in a `requirements` folder)
  * `pipfile`
  * `pyproject.toml`
  * `setup.py`
  * `poetry.lock`

* **JavaScript (NPM, Yarn, PNPM):**
  * `package.json`
  * `package-lock.json`
  * `npm-shrinkwrap.json`
  * `yarn.lock`
  * `pnpm-lock.yaml`
  * `pnpm-workspace.yaml`

* **Java (Maven):**
  * `pom.xml`

* **Go (GoLang):**
  * `go.mod`
  * `go.sum`

* **Ruby (Gem):**
  * `Gemfile.lock`
  * `*.gemspec`

* **Gradle (SPDX or CycloneDX):**
  * `*spdx.json`
  * `*cdx.json`

<br />

#### Malicious Package Alerts

If you have included known malicious packages in your project but are not receiving alerts, it may be due to the folder structure or the naming conventions of your manifest files. Ensuring that your manifest files follow the supported patterns should resolve these issues. Additionally, make sure that the malicious packages are correctly installed or referenced within these recognized manifest files.

#### Ensuring Effective Detection

To ensure that Socket can properly detect and analyze all relevant files:

* Follow the recommended file naming conventions.
* Place custom manifest files within expected directories.
* Regularly update your manifest files to reflect any changes in dependencies.

This will help maximize the effectiveness of Socket’s security features and ensure that your project is fully protected against vulnerabilities and malicious dependencies.

For more detailed information on supported files and patterns, you can refer to the [Socket API documentation](https://docs.socket.dev/reference/getreportsupportedfiles).