# Source: https://docs.readthedocs.com/platform/latest/flyout-menu.html

# Flyout menu[](#flyout-menu "Link to this heading")

When you use a Read the Docs site, there is a flyout menu embedded on all the documentation pages. The flyout menu is a way to expose the functionality of Read the Docs on the page, without having to have the documentation theme integrate it directly.

Tip

The flyout menu is a default implementation that works for every site. You can access the full data used to construct the flyout, and use that to integrate the data directly into your documentation theme for a nicer user experience. See the [[Custom event integration]](#custom-event-integration) for more information.

## Addons flyout menu[](#addons-flyout-menu "Link to this heading")

The [[Read the Docs Addons]](addons.html) flyout provides a place for a number of Read the Docs features:

-   A [[version switcher]](versions.html) that shows users all of the active versions they have access to.

-   A [[translation switcher]](localization.html) that shows all the documentation languages provided.

-   A list of [[offline formats]](downloadable-documentation.html) for the current version, including HTML & PDF downloads.

-   Links to the Read the Docs dashboard for the project.

-   A search bar that gives users access to the [[Server side search]](server-side-search/index.html) of the current version.

<figure id="id1" class="align-center">
<img src="_images/flyout-addons.png" alt="_images/flyout-addons.png" />
<figcaption><p><span class="caption-text">The opened flyout menu</span><a href="#id1" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>

### Customizing the flyout menu[](#customizing-the-flyout-menu "Link to this heading")

In your dashboard, you can configure flyout menu options in [Settings \> Addons \> Flyout Menu].

#### Version sorting[](#version-sorting "Link to this heading")

The primary customization currently is the ability to sort versions. You can sort by:

-   [SemVer (Read the Docs)] - **Default**. Read the Docs custom implementation of semver.org.

-   [Python Packaging] - Sort by Python packaging sorting.

-   [CalVer] - Sort by calendar date.

-   [Alphabetically] - Only useful if you aren't using numeric versions.

-   Or you can define a custom pattern

You can also choose whether [`latest`] and [`stable`] should be sorted first, as those are special versions that Read the Docs uses.