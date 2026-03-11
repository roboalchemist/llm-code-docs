# Source: https://docs.flux.ai/reference/stability-and-updates.md

# Stability and updates

This section is about:

- How new API updates are released.
- How the Flux team provides stability to **published** models.

One of our top priorities for the API is stability. It's important for our users that models don't break all the time. This is especially true given that Flux is a fast-moving product with weekly new releases.

On the other hand, we also want to strike the right balance between providing new functionality quickly and maintaining backwards compatibility. Below is how we intend to do that.

## API Versioning

Changes to the plugins API are identified as "Version X, Update Y". The first number "X" represents the major version number, and the second number "Y" represents minor updates.

### Minor updates

New **additive** APIs and minor bug fixes will be provided as minor **updates**. These new APIs will become automatically available to plugins, as long as the plugin is using the latest version. This may mean you need to upgrade the plugin major version to get an update.

You will still need to get the latest typings file manually by downloading it or creating a new project and copying the typings file from there.

If an API has a bug, we may ship the bug fix as a minor update upon our discretion. It depends on whether we feel like there's a risk that some may plugins break as a result of _fixing_ the bug. While any change in the behavior of an API could theoretically make a plugin work or not work, it's extra overhead for both plugin authors and for us to consider every bug fix to be a breaking change.

**TypeScript**: We may change the _typings_ of the API in breaking ways during minor updates too. In the TypeScript world that, typings and code are two separate things. As such, changes to typings don't affect existing code and don't cause published plugins to break. Having typings that accurately represent the latest state of the API is more important than having perfect backwards compatibility since types are easy to update. Generally, typings change only involve renaming some types.

### Major versions

Changes to existing APIs will be provided as major **versions**. These are changes that are likely to have a visible effect on plugins and require plugin authors to update their code.

This includes both changes to the API itself (e.g. removing a deprecated function) or changes to the behavior of the API (e.g. suppose we decided that all `create<NodeType>` functions no longer parent to the canvas by default).

Models will not be automatically upgraded to these changes. The `api` field in the manifest specifies the major version. To keep existing plugins working, the Flux team commits to support old major versions as long as practically possible.