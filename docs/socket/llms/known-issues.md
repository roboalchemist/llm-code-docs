# Source: https://docs.socket.dev/docs/known-issues.md

# Known issues

Known issues with the Socket product, and workarounds when available.

# Socket for GitHub does not analyze private npm packages

Socket skips dependencies which are private npm packages, since we never read customer source code. This means that we do not analyze the transitive dependencies contained therein.

**Workaround:** To analyze private npm package dependencies, you must ensure that Socket for GitHub is enabled on the private package's GitHub repository. Then Socket for GitHub will be able access the dependency manifests (e.g. `package.json`, etc.) for the repository.

**Alternative Workaround:** Add the npm private package as a workspace within your main project.

Please [Contact support](https://docs.socket.dev/docs/contact-support) if you need help with either of these workarounds.