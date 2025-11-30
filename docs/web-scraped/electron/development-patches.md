# Source: https://www.electronjs.org/docs/latest/development/patches

On this page

# Patches in Electron

Electron is built on two major upstream projects: Chromium and Node.js. Each of these projects has several of their own dependencies, too. We try our best to use these dependencies exactly as they are but sometimes we can\'t achieve our goals without patching those upstream dependencies to fit our use cases.

## Patch justification[â€‹](#patch-justification "Direct link to Patch justification") 

Every patch in Electron is a maintenance burden. When upstream code changes, patches can breakâ€"sometimes without even a patch conflict or a compilation error. It\'s an ongoing effort to keep our patch set up-to-date and effective. So we strive to keep our patch count at a minimum. To that end, every patch must describe its reason for existence in its commit message. That reason must be one of the following:

1.  The patch is temporary, and is intended to be (or has been) committed upstream or otherwise eventually removed. Include a link to an upstream PR or code review if available, or a procedure for verifying whether the patch is still needed at a later date.
2.  The patch allows the code to compile in the Electron environment, but cannot be upstreamed because it\'s Electron-specific (e.g. patching out references to Chrome\'s `Profile`). Include reasoning about why the change cannot be implemented without a patch (e.g. by subclassing or copying the code).
3.  The patch makes Electron-specific changes in functionality which are fundamentally incompatible with upstream.

In general, all the upstream projects we work with are friendly folks and are often happy to accept refactorings that allow the code in question to be compatible with both Electron and the upstream project. (See e.g. [this](https://chromium-review.googlesource.com/c/chromium/src/+/1637040) change in Chromium, which allowed us to remove a patch that did the same thing, or [this](https://github.com/nodejs/node/pull/22110) change in Node, which was a no-op for Node but fixed a bug in Electron.) **We should aim to upstream changes whenever we can, and avoid indefinite-lifetime patches**.

## Patch system[â€‹](#patch-system "Direct link to Patch system") 

If you find yourself in the unfortunate position of having to make a change which can only be made through patching an upstream project, you\'ll need to know how to manage patches in Electron.

All patches to upstream projects in Electron are contained in the `patches/` directory. Each subdirectory of `patches/` contains several patch files, along with a `.patches` file which lists the order in which the patches should be applied. Think of these files as making up a series of git commits that are applied on top of the upstream project after we check it out.

``` 
patches
âââ config.json   <-- this describes which patchset directory is applied to what project
âââ chromium
âÂ Â  âââ .patches
âÂ Â  âââ accelerator.patch
âÂ Â  âââ add_contentgpuclient_precreatemessageloop_callback.patch
â   â®
âââ node
âÂ Â  âââ .patches
âÂ Â  âââ add_openssl_is_boringssl_guard_to_oaep_hash_check.patch
âÂ Â  âââ build_add_gn_build_files.patch
âÂ Â  â®
â®
```

To help manage these patch sets, we provide two tools: `git-import-patches` and `git-export-patches`. `git-import-patches` imports a set of patch files into a git repository by applying each patch in the correct order and creating a commit for each one. `git-export-patches` does the reverse; it exports a series of git commits in a repository into a set of files in a directory and an accompanying `.patches` file.

> Side note: the reason we use a `.patches` file to maintain the order of applied patches, rather than prepending a number like `001-` to each file, is because it reduces conflicts related to patch ordering. It prevents the situation where two PRs both add a patch at the end of the series with the same numbering and end up both getting merged resulting in a duplicate identifier, and it also reduces churn when a patch is added or deleted in the middle of the series.

### Usage[â€‹](#usage "Direct link to Usage") 

#### Adding a new patch[â€‹](#adding-a-new-patch "Direct link to Adding a new patch") 

``` 
$ cd src/third_party/electron_node
$ vim some/code/file.cc
$ git commit
$ ../../electron/script/git-export-patches -o ../../electron/patches/node
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`git-export-patches` ignores any uncommitted files, so you must create a commit if you want your changes to be exported. The subject line of the commit message will be used to derive the patch file name, and the body of the commit message should include the reason for the patch\'s existence.

Re-exporting patches will sometimes cause shasums in unrelated patches to change. This is generally harmless and can be ignored (but go ahead and add those changes to your PR, it\'ll stop them from showing up for other people).

#### Editing an existing patch[â€‹](#editing-an-existing-patch "Direct link to Editing an existing patch") 

``` 
$ cd src/v8
$ vim some/code/file.cc
$ git log
# Find the commit sha of the patch you want to edit.
$ git commit --fixup [COMMIT_SHA]
$ git rebase --autosquash -i [COMMIT_SHA]^
$ ../electron/script/git-export-patches -o ../electron/patches/v8
```

Note that the `^` symbol [can cause trouble on Windows](https://stackoverflow.com/questions/14203952/git-reset-asks-more/14204318#14204318). The workaround is to either quote it `"[COMMIT_SHA]^"` or avoid it `[COMMIT_SHA]~1`.

#### Removing a patch[â€‹](#removing-a-patch "Direct link to Removing a patch") 

``` 
$ vim src/electron/patches/node/.patches
# Delete the line with the name of the patch you want to remove
$ cd src/third_party/electron_node
$ git reset --hard refs/patches/upstream-head
$ ../../electron/script/git-import-patches ../../electron/patches/node
$ ../../electron/script/git-export-patches -o ../../electron/patches/node
```

Note that `git-import-patches` will mark the commit that was `HEAD` when it was run as `refs/patches/upstream-head`. This lets you keep track of which commits are from Electron patches (those that come after `refs/patches/upstream-head`) and which commits are in upstream (those before `refs/patches/upstream-head`).

#### Resolving conflicts[â€‹](#resolving-conflicts "Direct link to Resolving conflicts") 

When updating an upstream dependency, patches may fail to apply cleanly. Often, the conflict can be resolved automatically by git with a 3-way merge. You can instruct `git-import-patches` to use the 3-way merge algorithm by passing the `-3` argument:

``` 
$ cd src/third_party/electron_node
# If the patch application failed midway through, you can reset it with:
$ git am --abort
# And then retry with 3-way merge:
$ ../../electron/script/git-import-patches -3 ../../electron/patches/node
```

If `git-import-patches -3` encounters a merge conflict that it can\'t resolve automatically, it will pause and allow you to resolve the conflict manually. Once you have resolved the conflict, `git add` the resolved files and continue to apply the rest of the patches by running `git am --continue`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/patches.md)