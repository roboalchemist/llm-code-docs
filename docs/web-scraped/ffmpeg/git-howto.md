# Source: https://ffmpeg.org/git-howto.html

-   [![FFmpeg](img/ffmpeg3d_white_20.png) FFmpeg](.)
-   [About](about.html)
-   [News](index.html#news)
-   [Download](download.html)
-   [Documentation](documentation.html)
-   [Community](community.html)
    -   [Code of Conduct](community.html#CodeOfConduct)
    -   [Mailing Lists](contact.html#MailingLists)
    -   [IRC](contact.html#IRCChannels)
    -   [Forums](contact.html#Forums)
    -   [Bug Reports](bugreports.html)
    -   [Wiki](https://trac.ffmpeg.org)
    -   [Conferences](https://trac.ffmpeg.org/wiki/Conferences)
-   [Developers](developer.html)
    -   [Source Code](download.html#get-sources)
    -   [Contribute](developer.html#Introduction)
    -   [FATE](http://fate.ffmpeg.org)
    -   [Code Coverage](http://coverage.ffmpeg.org)
    -   [Funding through SPI](spi.html)
-   [More](#)
    -   [Donate[]](donations.html)
    -   [Hire Developers](consulting.html)
    -   [Contact](contact.html)
    -   [Security](security.html)
    -   [Legal](legal.html)

# [](#) Using Git to develop FFmpeg

[] []

## Table of Contents 

-   [1 Introduction](#Introduction)
-   [2 Basics Usage](#Basics-Usage)
    -   [2.1 Get Git](#Get-Git)
    -   [2.2 Cloning the source tree](#Cloning-the-source-tree)
    -   [2.3 Updating the source tree to the latest revision](#Updating-the-source-tree-to-the-latest-revision-1)
    -   [2.4 Rebasing your local branches](#Rebasing-your-local-branches)
    -   [2.5 Adding/removing files/directories](#Adding_002fremoving-files_002fdirectories)
    -   [2.6 Showing modifications](#Showing-modifications)
    -   [2.7 Inspecting the changelog](#Inspecting-the-changelog)
    -   [2.8 Checking source tree status](#Checking-source-tree-status)
    -   [2.9 Committing](#Committing)
    -   [2.10 Writing a commit message](#Writing-a-commit-message)
    -   [2.11 Preparing a patchset](#Preparing-a-patchset)
    -   [2.12 Sending patches for review](#Sending-patches-for-review)
    -   [2.13 Renaming/moving/copying files or contents of files](#Renaming_002fmoving_002fcopying-files-or-contents-of-files)
-   [3 Git configuration](#Git-configuration)
    -   [3.1 Personal Git installation](#Personal-Git-installation)
    -   [3.2 Repository configuration](#Repository-configuration)
-   [4 FFmpeg specific](#FFmpeg-specific)
    -   [4.1 Reverting broken commits](#Reverting-broken-commits)
    -   [4.2 Pushing changes to remote trees](#Pushing-changes-to-remote-trees)
    -   [4.3 Finding a specific svn revision](#Finding-a-specific-svn-revision)
-   [5 gpg key generation](#gpg-key-generation)
-   [6 Pre-push checklist](#Pre_002dpush-checklist)
-   [7 Server Issues](#Server-Issues)

[]

## [1 Introduction](#toc-Introduction) 

This document aims in giving some quick references on a set of useful Git commands. You should always use the extensive and detailed documentation provided directly by Git:

``` example
git --help
man git
```

shows you the available subcommands,

``` example
git <command> --help
man git-<command>
```

shows information about the subcommand \<command\>.

Additional information could be found on the [Git Reference](http://gitref.org) website.

For more information about the Git project, visit the [Git website](http://git-scm.com/).

Consult these resources whenever you have problems, they are quite exhaustive.

What follows now is a basic introduction to Git and some FFmpeg-specific guidelines to ease the contribution to the project.

[]

## [2 Basics Usage](#toc-Basics-Usage) 

[]

### [2.1 Get Git](#toc-Get-Git) 

You can get Git from <http://git-scm.com/> Most distribution and operating system provide a package for it.

[]

### [2.2 Cloning the source tree](#toc-Cloning-the-source-tree) 

``` example
git clone https://git.ffmpeg.org/ffmpeg.git <target>
```

This will put the FFmpeg sources into the directory `<target>`.

``` example
git clone git@source.ffmpeg.org:ffmpeg <target>
```

This will put the FFmpeg sources into the directory `<target>` and let you push back your changes to the remote repository.

``` example
git clone git@ffmpeg.org:ffmpeg-web <target>
```

This will put the source of the FFmpeg website into the directory `<target>` and let you push back your changes to the remote repository.

If you don't have write-access to the ffmpeg-web repository, you can create patches after making a read-only ffmpeg-web clone:

``` example
git clone git://ffmpeg.org/ffmpeg-web <target>
```

Make sure that you do not have Windows line endings in your checkouts, otherwise you may experience spurious compilation failures. One way to achieve this is to run

``` example
git config --global core.autocrlf false
```

[][]

### [2.3 Updating the source tree to the latest revision](#toc-Updating-the-source-tree-to-the-latest-revision-1) 

``` example
git pull (--rebase)
```

pulls in the latest changes from the tracked branch. The tracked branch can be remote. By default the master branch tracks the branch master in the remote origin.

`--rebase` (see below) is recommended.

[]

### [2.4 Rebasing your local branches](#toc-Rebasing-your-local-branches) 

``` example
git pull --rebase
```

fetches the changes from the main repository and replays your local commits over it. This is required to keep all your local changes at the top of FFmpeg's master tree. The master tree will reject pushes with merge commits.

[]

### [2.5 Adding/removing files/directories](#toc-Adding_002fremoving-files_002fdirectories) 

``` example
git add [-A] <filename/dirname>
git rm [-r] <filename/dirname>
```

Git needs to get notified of all changes you make to your working directory that makes files appear or disappear. Line moves across files are automatically tracked.

[]

### [2.6 Showing modifications](#toc-Showing-modifications) 

``` example
git diff <filename(s)>
```

will show all local modifications in your working directory as unified diff.

[]

### [2.7 Inspecting the changelog](#toc-Inspecting-the-changelog) 

``` example
git log <filename(s)>
```

You may also use the graphical tools like `gitview` or `gitk` or the web interface available at <https://git.ffmpeg.org/ffmpeg.git>.

[]

### [2.8 Checking source tree status](#toc-Checking-source-tree-status) 

``` example
git status
```

detects all the changes you made and lists what actions will be taken in case of a commit (additions, modifications, deletions, etc.).

[]

### [2.9 Committing](#toc-Committing) 

``` example
git diff --check
```

to double check your changes before committing them to avoid trouble later on. All experienced developers do this on each and every commit, no matter how small.

Every one of them has been saved from looking like a fool by this many times. It's very easy for stray debug output or cosmetic modifications to slip in, please avoid problems through this extra level of scrutiny.

For cosmetics-only commits you should get (almost) empty output from

``` example
git diff -w -b <filename(s)>
```

Also check the output of

``` example
git status
```

to make sure you don't have untracked files or deletions.

``` example
git add [-i|-p|-A] <filenames/dirnames>
```

Make sure you have told Git your name, email address and GPG key

``` example
git config --global user.name "My Name"
git config --global user.email my@email.invalid
git config --global user.signingkey ABCDEF0123245
```

Enable signing all commits or use -S

``` example
git config --global commit.gpgsign true
```

Use `--global` to set the global configuration for all your Git checkouts.

Git will select the changes to the files for commit. Optionally you can use the interactive or the patch mode to select hunk by hunk what should be added to the commit.

``` example
git commit
```

Git will commit the selected changes to your current local branch.

You will be prompted for a log message in an editor, which is either set in your personal configuration file through

``` example
git config --global core.editor
```

or set by one of the following environment variables: `GIT_EDITOR`, `VISUAL` or `EDITOR`.

[]

### [2.10 Writing a commit message](#toc-Writing-a-commit-message) 

Log messages should be concise but descriptive.

The first line must contain the context, a colon and a very short summary of what the commit does. Details can be added, if necessary, separated by an empty line. These details should not exceed 60-72 characters per line, except when containing code.

Example of a good commit message:

``` example
avcodec/cbs: add a helper to read extradata within packet side data

Using ff_cbs_read() on the raw buffer will not parse it as extradata,
resulting in parsing errors for example when handling ISOBMFF avcC.
This helper works around that.
```

``` example
ptr might be NULL
```

If the summary on the first line is not enough, in the body of the message, explain why you made a change, what you did will be obvious from the changes themselves most of the time. Saying just \"bug fix\" or \"10l\" is bad. Remember that people of varying skill levels look at and educate themselves while reading through your code. Don't include filenames in log messages except in the context, Git provides that information.

If the commit fixes a registered issue, state it in a separate line of the body: `Fix Trac ticket #42.`

The first line will be used to name the patch by `git format-patch`.

Common mistakes for the first line, as seen in `git log --oneline` include: missing context at the beginning; description of what the code did before the patch; line too long or wrapped to the second line.

[]

### [2.11 Preparing a patchset](#toc-Preparing-a-patchset) 

``` example
git format-patch <commit> [-o directory]
```

will generate a set of patches for each commit between `<commit>` and current `HEAD`. E.g.

``` example
git format-patch origin/master
```

will generate patches for all commits on current branch which are not present in upstream. A useful shortcut is also

``` example
git format-patch -n
```

which will generate patches from last `n` commits. By default the patches are created in the current directory.

[]

### [2.12 Sending patches for review](#toc-Sending-patches-for-review) 

``` example
git send-email <commit list|directory>
```

will send the patches created by `git format-patch` or directly generates them. All the email fields can be configured in the global/local configuration or overridden by command line. Note that this tool must often be installed separately (e.g. `git-email` package on Debian-based distros).

[]

### [2.13 Renaming/moving/copying files or contents of files](#toc-Renaming_002fmoving_002fcopying-files-or-contents-of-files) 

Git automatically tracks such changes, making those normal commits.

``` example
mv/cp path/file otherpath/otherfile
git add [-A] .
git commit
```

[]

## [3 Git configuration](#toc-Git-configuration) 

In order to simplify a few workflows, it is advisable to configure both your personal Git installation and your local FFmpeg repository.

[]

### [3.1 Personal Git installation](#toc-Personal-Git-installation) 

Add the following to your `~/.gitconfig` to help `git send-email` and `git format-patch` detect renames:

``` example
[diff]
        renames = copy
```

[]

### [3.2 Repository configuration](#toc-Repository-configuration) 

In order to have `git send-email` automatically send patches to the ffmpeg-devel mailing list, add the following stanza to `/path/to/ffmpeg/repository/.git/config`:

``` example
[sendemail]
        to = ffmpeg-devel@ffmpeg.org
```

[]

## [4 FFmpeg specific](#toc-FFmpeg-specific) 

[]

### [4.1 Reverting broken commits](#toc-Reverting-broken-commits) 

``` example
git reset <commit>
```

`git reset` will uncommit the changes till `<commit>` rewriting the current branch history.

``` example
git commit --amend
```

allows one to amend the last commit details quickly.

``` example
git rebase -i origin/master
```

will replay local commits over the main repository allowing to edit, merge or remove some of them in the process.

`git reset`, `git commit --amend` and `git rebase` rewrite history, so you should use them ONLY on your local or topic branches. The main repository will reject those changes.

``` example
git revert <commit>
```

`git revert` will generate a revert commit. This will not make the faulty commit disappear from the history.

[]

### [4.2 Pushing changes to remote trees](#toc-Pushing-changes-to-remote-trees) 

``` example
git push origin master --dry-run
```

Will simulate a push of the local master branch to the default remote (`origin`). And list which branches and ranges or commits would have been pushed. Git will prevent you from pushing changes if the local and remote trees are out of sync. Refer to [Updating the source tree to the latest revision](#Updating-the-source-tree-to-the-latest-revision).

``` example
git remote add <name> <url>
```

Will add additional remote with a name reference, it is useful if you want to push your local branch for review on a remote host.

``` example
git push <remote> <refspec>
```

Will push the changes to the `<remote>` repository. Omitting `<refspec>` makes `git push` update all the remote branches matching the local ones.

[]

### [4.3 Finding a specific svn revision](#toc-Finding-a-specific-svn-revision) 

Since version 1.7.1 Git supports '`:/foo`' syntax for specifying commits based on a regular expression. see man gitrevisions

``` example
git show :/'as revision 23456'
```

will show the svn changeset '`r23456`'. With older Git versions searching in the `git log` output is the easiest option (especially if a pager with search capabilities is used).

This commit can be checked out with

``` example
git checkout -b svn_23456 :/'as revision 23456'
```

or for Git \< 1.7.1 with

``` example
git checkout -b svn_23456 $SHA1
```

where `$SHA1` is the commit hash from the `git log` output.

[]

## [5 gpg key generation](#toc-gpg-key-generation) 

If you have no gpg key yet, we recommend that you create a ed25519 based key as it is small, fast and secure. Especially it results in small signatures in git.

``` example
gpg --default-new-key-algo "ed25519/cert,sign+cv25519/encr" --quick-generate-key "human@server.com"
```

When generating a key, make sure the email specified matches the email used in git as some sites like github consider mismatches a reason to declare such commits unverified. After generating a key you can add it to the MAINTAINER file and upload it to a keyserver.

[]

## [6 Pre-push checklist](#toc-Pre_002dpush-checklist) 

Once you have a set of commits that you feel are ready for pushing, work through the following checklist to doublecheck everything is in proper order. This list tries to be exhaustive. In case you are just pushing a typo in a comment, some of the steps may be unnecessary. Apply your common sense, but if in doubt, err on the side of caution.

First, make sure that the commits and branches you are going to push match what you want pushed and that nothing is missing, extraneous or wrong. You can see what will be pushed by running the git push command with `--dry-run` first. And then inspecting the commits listed with `git log -p 1234567..987654`. The `git status` command may help in finding local changes that have been forgotten to be added.

Next let the code pass through a full run of our test suite.

-   `make distclean`
-   `/path/to/ffmpeg/configure`
-   `make fate`
-   if fate fails due to missing samples run `make fate-rsync` and retry

Make sure all your changes have been checked before pushing them, the test suite only checks against regressions and that only to some extend. It does obviously not check newly added features/code to be working unless you have added a test for that (which is recommended).

Also note that every single commit should pass the test suite, not just the result of a series of patches.

Once everything passed, push the changes to your public ffmpeg clone and post a merge request to ffmpeg-devel. You can also push them directly but this is not recommended.

[]

## [7 Server Issues](#toc-Server-Issues) 

Contact the project admins at <root@ffmpeg.org> if you have technical problems with the Git server.

This document was generated on *December 27, 2025* using [*makeinfo*](http://www.gnu.org/software/texinfo/).

[Hosting provided by [telepoint.bg](https://telepoint.bg)]