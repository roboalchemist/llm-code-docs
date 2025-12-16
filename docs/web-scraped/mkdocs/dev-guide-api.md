# Source: https://www.mkdocs.org/dev-guide/api/

[MkDocs](../..)

[]

-   [Home](../..)
-   [Getting Started](../../getting-started/)
-   [User Guide ](#)
    -   [User Guide](../../user-guide/)
    -   [Installation](../../user-guide/installation/)
    -   [Writing Your Docs](../../user-guide/writing-your-docs/)
    -   [Choosing Your Theme](../../user-guide/choosing-your-theme/)
    -   [Customizing Your Theme](../../user-guide/customizing-your-theme/)
    -   [Localizing Your Theme](../../user-guide/localizing-your-theme/)
    -   [Configuration](../../user-guide/configuration/)
    -   [Command Line Interface](../../user-guide/cli/)
    -   [Deploying Your Docs](../../user-guide/deploying-your-docs/)
-   [Developer Guide ](#)
    -   [Developer Guide](../)
    -   [Themes](../themes/)
    -   [Translations](../translations/)
    -   [Plugins](../plugins/)
    -   [API Reference](./)
-   [About ](#)
    -   [Release Notes](../../about/release-notes/)
    -   [Contributing](../../about/contributing/)
    -   [License](../../about/license/)

```
<!-- -->
```
-   [ Search](#)
-   [ Previous](../plugins/)
-   [Next ](../../about/release-notes/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/dev-guide/api.md)

[]

-   [API reference](#api-reference)
    -   [Files](#mkdocs.structure.files.Files)
    -   [File](#mkdocs.structure.files.File)
    -   [Config](#mkdocs.config.base.Config)
    -   [TemplateContext](#mkdocs.utils.templates.TemplateContext)
    -   [LiveReloadServer](#mkdocs.livereload.LiveReloadServer)

# API reference[](#api-reference "Permanent link")

Note

The main entry point to the API is through [Events](../plugins/#events) that are received by plugins. These events\' descriptions link back to this page.

## `mkdocs.structure.files.Files` [](#mkdocs.structure.files.Files "Permanent link") 

A collection of [File](#mkdocs.structure.files.File) objects.

### `src_paths: dict[str, File]` [ [`property`] ] [](#mkdocs.structure.files.Files.src_paths "Permanent link") 

Soft-deprecated, prefer `src_uris`.

### `src_uris: Mapping[str, File]` [ [`property`] ] [](#mkdocs.structure.files.Files.src_uris "Permanent link") 

A mapping containing every file, with the keys being their [`src_uri`](#mkdocs.structure.files.File.src_uri).

### `__iter__() -> Iterator[File]` [](#mkdocs.structure.files.Files.__iter__ "Permanent link") 

Iterate over the files within.

### `__len__() -> int` [](#mkdocs.structure.files.Files.__len__ "Permanent link") 

The number of files within.

### `__contains__(path: str) -> bool` [](#mkdocs.structure.files.Files.__contains__ "Permanent link") 

Soft-deprecated, prefer `get_file_from_path(path) is not None`.

### `get_file_from_path(path: str) -> File | None` [](#mkdocs.structure.files.Files.get_file_from_path "Permanent link") 

Return a File instance with File.src_uri equal to path.

### `append(file: File) -> None` [](#mkdocs.structure.files.Files.append "Permanent link") 

Add file to the Files collection.

### `remove(file: File) -> None` [](#mkdocs.structure.files.Files.remove "Permanent link") 

Remove file from Files collection.

### `copy_static_files(dirty: bool = False, *, inclusion: Callable[[InclusionLevel], bool] = InclusionLevel.is_included) -> None` [](#mkdocs.structure.files.Files.copy_static_files "Permanent link") 

Copy static files from source to destination.

### `documentation_pages(*, inclusion: Callable[[InclusionLevel], bool] = InclusionLevel.is_included) -> Sequence[File]` [](#mkdocs.structure.files.Files.documentation_pages "Permanent link") 

Return iterable of all Markdown page file objects.

### `static_pages() -> Sequence[File]` [](#mkdocs.structure.files.Files.static_pages "Permanent link") 

Return iterable of all static page file objects.

### `media_files() -> Sequence[File]` [](#mkdocs.structure.files.Files.media_files "Permanent link") 

Return iterable of all file objects which are not documentation or static pages.

### `javascript_files() -> Sequence[File]` [](#mkdocs.structure.files.Files.javascript_files "Permanent link") 

Return iterable of all javascript file objects.

### `css_files() -> Sequence[File]` [](#mkdocs.structure.files.Files.css_files "Permanent link") 

Return iterable of all CSS file objects.

### `add_files_from_theme(env: jinja2.Environment, config: MkDocsConfig) -> None` [](#mkdocs.structure.files.Files.add_files_from_theme "Permanent link") 

Retrieve static files from Jinja environment and add to collection.

## `mkdocs.structure.files.File` [](#mkdocs.structure.files.File "Permanent link") 

A MkDocs File object.

It represents how the contents of one file should be populated in the destination site.

A file always has its `abs_dest_path` (obtained by joining `dest_dir` and `dest_path`), where the `dest_dir` is understood to be the *site* directory.

`content_bytes`/`content_string` (new in MkDocs 1.6) can always be used to obtain the file\'s content. But it may be backed by one of the two sources:

-   A physical source file at `abs_src_path` (by default obtained by joining `src_dir` and `src_uri`). `src_dir` is understood to be the *docs* directory.

    Then `content_bytes`/`content_string` will read the file at `abs_src_path`.

    `src_dir` *should* be populated for real files and should be `None` for generated files.

-   Since MkDocs 1.6 a file may alternatively be stored in memory - `content_string`/`content_bytes`.

    Then `src_dir` and `abs_src_path` will remain `None`. `content_bytes`/`content_string` need to be written to, or populated through the `content` argument in the constructor.

    But `src_uri` is still populated for such files as well! The virtual file pretends as if it originated from that path in the `docs` directory, and other values are derived.

For static files the file is just copied to the destination, and `dest_uri` equals `src_uri`.

For Markdown files (determined by the file extension in `src_uri`) the destination content will be the rendered content, and `dest_uri` will have the `.html` extension and some additional transformations to the path, based on `use_directory_urls`.

### `src_uri: str` [ [`instance-attribute`] ] [](#mkdocs.structure.files.File.src_uri "Permanent link") 

The pure path (always \'/\'-separated) of the source file relative to the source directory.

### `generated_by: str | None = None` [ [`class-attribute`] [`instance-attribute`] ] [](#mkdocs.structure.files.File.generated_by "Permanent link") 

If not None, indicates that a plugin generated this file on the fly.

The value is the plugin\'s entrypoint name and can be used to find the plugin by key in the PluginCollection.

### `dest_path: str` [ [`property`] [`writable`] ] [](#mkdocs.structure.files.File.dest_path "Permanent link") 

Same as `dest_uri` (and synchronized with it) but will use backslashes on Windows. Discouraged.

### `src_path: str = path` [ [`instance-attribute`] [`property`] [`writable`] ] [](#mkdocs.structure.files.File.src_path "Permanent link") 

Same as `src_uri` (and synchronized with it) but will use backslashes on Windows. Discouraged.

### `src_dir: str | None = src_dir` [ [`instance-attribute`] ] [](#mkdocs.structure.files.File.src_dir "Permanent link") 

The OS path of the top-level directory that the source file originates from.

Assumed to be the *docs_dir*; not populated for generated files.

### `dest_dir: str = dest_dir` [ [`instance-attribute`] ] [](#mkdocs.structure.files.File.dest_dir "Permanent link") 

The OS path of the destination directory (top-level site_dir) that the file should be copied to.

### `use_directory_urls: bool = use_directory_urls` [ [`instance-attribute`] ] [](#mkdocs.structure.files.File.use_directory_urls "Permanent link") 

Whether directory URLs (\'foo/\') should be used or not (\'foo.html\').

If `False`, a Markdown file is mapped to an HTML file of the same name (the file extension is changed to `.html`). If True, a Markdown file is mapped to an HTML index file (`index.html`) nested in a directory using the \"name\" of the file in `path`. Non-Markdown files retain their original path.

### `inclusion: InclusionLevel = inclusion` [ [`class-attribute`] [`instance-attribute`] ] [](#mkdocs.structure.files.File.inclusion "Permanent link") 

Whether the file will be excluded from the built site.

### `name = cached_property(_get_stem)` [ [`class-attribute`] [`instance-attribute`] ] [](#mkdocs.structure.files.File.name "Permanent link") 

Return the name of the file without its extension.

### `dest_uri = cached_property(_get_dest_path)` [ [`class-attribute`] [`instance-attribute`] ] [](#mkdocs.structure.files.File.dest_uri "Permanent link") 

The pure path (always \'/\'-separated) of the destination file relative to the destination directory.

### `url = cached_property(_get_url)` [ [`class-attribute`] [`instance-attribute`] ] [](#mkdocs.structure.files.File.url "Permanent link") 

The URI of the destination file relative to the destination directory as a string.

### `abs_src_path: str | None` [ [`cached`] [`property`] ] [](#mkdocs.structure.files.File.abs_src_path "Permanent link") 

The absolute concrete path of the source file. Will use backslashes on Windows.

Note: do not use this path to read the file, prefer `content_bytes`/`content_string`.

### `abs_dest_path: str` [ [`cached`] [`property`] ] [](#mkdocs.structure.files.File.abs_dest_path "Permanent link") 

The absolute concrete path of the destination file. Will use backslashes on Windows.

### `content_bytes: bytes` [ [`property`] [`writable`] ] [](#mkdocs.structure.files.File.content_bytes "Permanent link") 

Get the content of this file as a bytestring.

May raise if backed by a real file (`abs_src_path`) if it cannot be read.

If used as a setter, it defines the content of the file, and `abs_src_path` becomes unset.

### `content_string: str` [ [`property`] [`writable`] ] [](#mkdocs.structure.files.File.content_string "Permanent link") 

Get the content of this file as a string. Assumes UTF-8 encoding, may raise.

May also raise if backed by a real file (`abs_src_path`) if it cannot be read.

If used as a setter, it defines the content of the file, and `abs_src_path` becomes unset.

### `generated(config: MkDocsConfig, src_uri: str, *, content: str | bytes | None = None, abs_src_path: str | None = None, inclusion: InclusionLevel = InclusionLevel.UNDEFINED) -> File` [ [`classmethod`] ] [](#mkdocs.structure.files.File.generated "Permanent link") 

Create a virtual file, backed either by in-memory `content` or by a file at `abs_src_path`.

It will pretend to be a file in the docs dir at `src_uri`.

### `edit_uri() -> str | None` [](#mkdocs.structure.files.File.edit_uri "Permanent link") 

A path relative to the source repository to use for the \"edit\" button.

Defaults to `src_uri` and can be overwritten. For generated files this should be set to `None`.

### `url_relative_to(other: File | str) -> str` [](#mkdocs.structure.files.File.url_relative_to "Permanent link") 

Return url for file relative to other file.

### `copy_file(dirty: bool = False) -> None` [](#mkdocs.structure.files.File.copy_file "Permanent link") 

Copy source file to destination, ensuring parent directories exist.

### `is_documentation_page() -> bool` [](#mkdocs.structure.files.File.is_documentation_page "Permanent link") 

Return True if file is a Markdown page.

### `is_static_page() -> bool` [](#mkdocs.structure.files.File.is_static_page "Permanent link") 

Return True if file is a static page (HTML, XML, JSON).

### `is_media_file() -> bool` [](#mkdocs.structure.files.File.is_media_file "Permanent link") 

Return True if file is not a documentation or static page.

### `is_javascript() -> bool` [](#mkdocs.structure.files.File.is_javascript "Permanent link") 

Return True if file is a JavaScript file.

### `is_css() -> bool` [](#mkdocs.structure.files.File.is_css "Permanent link") 

Return True if file is a CSS file.

## `mkdocs.config.base.Config` [](#mkdocs.config.base.Config "Permanent link") 

Bases: [`UserDict`]

Base class for MkDocs configuration, plugin configuration (and sub-configuration) objects.

It should be subclassed and have `ConfigOption`s defined as attributes. For examples, see mkdocs/contrib/search/**init**.py and mkdocs/config/defaults.py.

Behavior as it was prior to MkDocs 1.4 is now handled by LegacyConfig.

### `__new__(*args, **kwargs) -> Config` [](#mkdocs.config.base.Config.__new__ "Permanent link") 

Compatibility: allow referring to `LegacyConfig(...)` constructor as `Config(...)`.

### `set_defaults() -> None` [](#mkdocs.config.base.Config.set_defaults "Permanent link") 

Set the base config by going through each validator and getting the default if it has one.

### `load_dict(patch: dict) -> None` [](#mkdocs.config.base.Config.load_dict "Permanent link") 

Load config options from a dictionary.

### `load_file(config_file: IO) -> None` [](#mkdocs.config.base.Config.load_file "Permanent link") 

Load config options from the open file descriptor of a YAML file.

## `mkdocs.utils.templates.TemplateContext` [](#mkdocs.utils.templates.TemplateContext "Permanent link") 

Bases: [`TypedDict`]

### `nav: Navigation` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.nav "Permanent link") 

### `pages: Sequence[File]` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.pages "Permanent link") 

### `base_url: str` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.base_url "Permanent link") 

### `extra_css: Sequence[str]` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.extra_css "Permanent link") 

### `extra_javascript: Sequence[str]` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.extra_javascript "Permanent link") 

### `mkdocs_version: str` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.mkdocs_version "Permanent link") 

### `build_date_utc: datetime.datetime` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.build_date_utc "Permanent link") 

### `config: MkDocsConfig` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.config "Permanent link") 

### `page: Page | None` [ [`instance-attribute`] ] [](#mkdocs.utils.templates.TemplateContext.page "Permanent link") 

## `mkdocs.livereload.LiveReloadServer` [](#mkdocs.livereload.LiveReloadServer "Permanent link") 

Bases: [`ThreadingMixIn`], [`WSGIServer`]

### `watch(path: str, func: None = None, *, recursive: bool = True) -> None` [](#mkdocs.livereload.LiveReloadServer.watch "Permanent link") 

Add the \'path\' to watched paths, call the function and reload when any file changes under it.

### `unwatch(path: str) -> None` [](#mkdocs.livereload.LiveReloadServer.unwatch "Permanent link") 

Stop watching file changes for path. Raises if there was no corresponding `watch` call.

------------------------------------------------------------------------

Copyright © 2014 [Tom Christie](https://twitter.com/starletdreaming), Maintained by the [MkDocs Team](/about/release-notes/#maintenance-team).

Documentation built with [MkDocs](https://www.mkdocs.org/).

#### Search 

[×][Close]

From here you can search these documents. Enter your search terms below.

#### Keyboard Shortcuts 

[×][Close]

  Keys        Action
  ----------- ----------------
  [?]   Open this help
  [n]   Next page
  [p]   Previous page
  [s]   Search