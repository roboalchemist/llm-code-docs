flatpak::source
# Struct FlatpakSource 
Source 

```
pub struct FlatpakSource {}
```

## Fields§
§`type: Option<FlatpakSourceType>`

Defines the type of the source description.
§`commands: Option<Vec<String>>`

An array of shell commands.
types: script, shell
§`dest_filename: Option<String>`

Filename to use inside the source dir.
types: script, archive, file
§`filename: Option<String>`

The name to use for the downloaded extra data
types: extra-data
§`url: Option<String>`

The url to the resource.
types: extra-data, svn, bzr, git, archive, file
§`mirror_urls: Option<Vec<String>>`

A list of alternative urls that are used if the main url fails.
types: archive, file
§`md5: Option<String>`

The md5 checksum of the file, verified after download
Note that md5 is no longer considered a safe checksum, we recommend you use at least sha256.
types: archive, file
§`sha1: Option<String>`

The sha1 checksum of the file, verified after download
Note that sha1 is no longer considered a safe checksum, we recommend you use at least sha256.
types: archive, file
§`sha256: Option<String>`

The sha256 of the resource.
types: extra-data, archive, file
§`sha512: Option<String>`

The sha512 checksum of the file, verified after download
types: archive, file
§`size: Option<i64>`

The size of the extra data in bytes.
types: extra-data
§`git_init: Option<bool>`

Whether to initialise the repository as a git repository.
types: archive
§`installed_size: Option<i64>`

The extra installed size this adds to the app (optional).
types: extra-data
§`revision: Option<String>`

A specific revision number to use
types: svn, bzr
§`branch: Option<String>`

The branch to use from the git repository
types: git
§`archive_type: Option<FlatpakArchiveType>`

The type of archive if it cannot be guessed from the path.
types: archive
§`commit: Option<String>`

The commit to use from the git repository.
If branch is also specified, then it is verified that the branch/tag is at this specific commit.
This is a readable way to document that you’re using a particular tag,
but verify that it does not change.
types: git
§`tag: Option<String>`

The tag to use from the git repository
types: git
§`path: Option<String>`

The path to associated with the resource.
types: git, archive, dir, patch, file
§`paths: Option<Vec<String>>`

An list of paths to a patch files that will be applied in the source dir, in order
types: patch
§`use_git: Option<bool>`

Whether to use “git apply” rather than “patch” to apply the patch, required when the
patch file contains binary diffs.
types: patch
§`use_git_am: Option<bool>`

Whether to use “git am” rather than “patch” to apply the patch, required when the patch
file contains binary diffs.
You cannot use this at the same time as use-git.
types: patch
§`options: Option<Vec<String>>`

Extra options to pass to the patch command.
types: patch
§`disable_fsckobjects: Option<bool>`

Don’t use transfer.fsckObjects=1 to mirror git repository. This may be needed for some
(broken) repositories.
types: git
§`disable_shallow_clone: Option<bool>`

Don’t optimize by making a shallow clone when downloading the git repo.
types: git
§`disable_submodules: Option<bool>`

Don’t checkout the git submodules when cloning the repository.
types: git
§`strip_components: Option<i64>`

The number of initial pathname components to strip.
defaults to 1.
types: archive, patch
§`skip: Option<Vec<String>>`

Source files to ignore in the directory.
types: dir
§`only_arches: Option<Vec<String>>`

If non-empty, only build the module on the arches listed.
types: all
§`skip_arches: Option<Vec<String>>`

Don’t build on any of the arches listed.
types: all
§`dest: Option<String>`

Directory inside the source dir where this source will be extracted.
types: all
§`x_checker_data: Option<FlatpakDataCheckerConfig>`
## Implementations§