::: redirect-from
/devel/gitwash/development_workflow
:::

::: redirect-from
/devel/gitwash/maintainer_workflow
:::

# Development workflow

## Workflow summary

To keep your work well organized, with readable history, and in turn
make it easier for project maintainers (that might be you) to see what
you\'ve done, and why you did it, we recommend the following:

-   Don\'t make changes in your local `main` branch!
-   Before starting a new set of changes, fetch all changes from
    `upstream/main`, and start a new *feature branch* from that.
-   Make a new branch for each feature or bug fix --- \"one task, one
    branch\".
-   Name your branch for the purpose of the changes - e.g.
    `bugfix-for-issue-14` or `refactor-database-code`.
-   If you get stuck, reach out on Gitter or
    [discourse](https://discourse.matplotlib.org).
-   When you\'re ready or need feedback on your code, open a pull
    request so that the Matplotlib developers can give feedback and
    eventually include your suggested code into the `main` branch.

### Overview

After
`setting up a development environment <installing_for_devs>`{.interpreted-text
role="ref"}, the typical workflow is:

1.  Fetch all changes from `upstream/main`:

    ``` bash
    git fetch upstream
    ```

2.  Start a new *feature branch* from `upstream/main`:

    ``` bash
    git checkout -b my-feature upstream/main
    ```

3.  When you\'re done editing, e.g., `lib/matplotlib/collections.py`,
    record your changes in Git:

    ``` bash
    git add lib/matplotlib/collections.py
    git commit -m 'a commit message'
    ```

4.  Push the changes to your GitHub fork:

    ``` bash
    git push -u origin my-feature
    ```

## Update the `main` branch {#update-mirror-main}

First make sure you have followed
`installing_for_devs`{.interpreted-text role="ref"}.

From time to time you should fetch the upstream changes from GitHub:

``` bash
git fetch upstream
```

This will pull down any commits you don\'t have, and set the remote
branches to point to the right commit.

## Make a new feature branch {#make-feature-branch}

When you are ready to make some changes to the code, you should start a
new branch. Branches that are for a collection of related edits are
often called \'feature branches\'. Making a new branch for each set of
related changes will make it easier for someone reviewing your branch to
see what you are doing.

Choose an informative name for the branch to remind yourself and the
rest of us what the changes in the branch are for. For example
`add-ability-to-fly`, or `bugfix-for-issue-42`.

The process for creating a new feature branch is:

``` bash
# Update the main branch
git fetch upstream
# Make new feature branch starting at current main
git branch my-new-feature upstream/main
git checkout my-new-feature
```

If you started making changes on your local `main` branch, you can
convert the branch to a feature branch by renaming it:

``` bash
git branch -m <newname>
```

Generally, you will want to keep your feature branches on your public
GitHub fork of Matplotlib. To do this, you `git push` this new branch up
to your GitHub repo. Generally, if you followed the instructions in
these pages, and by default, git will have a link to your fork of the
GitHub repo, called `origin`. You push up to your own fork with:

``` bash
git push origin my-new-feature
```

## The editing workflow {#edit-flow}

1.  Make some changes

2.  Save the changes

3.  See which files have changed with `git status`. You\'ll see a
    listing like this one:

    ``` none
    # On branch ny-new-feature
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #  modified:   README
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #  INSTALL
    no changes added to commit (use "git add" and/or "git commit -a")
    ```

4.  Check what the actual changes are with `git diff`.

5.  Add any new files to version control `git add new_file_name`.

6.  To commit **all** modified files into the local copy of your repo,
    type:

    ``` bash
    git commit -am 'A commit message'
    ```

    Note the `-am` options to `commit`. The `m` flag signals that you
    are going to type a message on the command line. The `a` flag stages
    every file that has been modified, except files listed in
    `.gitignore`. For more information, see the [git
    commit](https://git-scm.com/docs/git-commit) manual page.

7.  To push the changes up to your forked repo on GitHub, do a
    `git push`.

## Verify your changes

Check that your change does what you intend. For code changes:

-   If the issue you are working on provided a code example, run that
    example against your branch and check that you now get the desired
    result. Note that adapting the issue example is often a good way to
    create a new test.
-   Run the tests to check that your change has not had unintended
    consequences on existing functionality. See
    `run_tests`{.interpreted-text role="ref"}.

For documentation changes, build the documentation locally to check that
it renders how you intended and that any new links work correctly. See
`build_docs`{.interpreted-text role="ref"}.

This is also a good time to look through the
`pr-author-guidelines`{.interpreted-text role="ref"} and address as many
of the relevant points as you can.

## Open a pull request {#open-pull-request}

When you are ready to ask for someone to review your code and consider a
merge, [submit your Pull Request
(PR)](https://docs.github.com/pull-requests).

Go to the web page of *your fork* of the Matplotlib repo, and click
`Compare & pull request` to send your changes to the maintainers for
review. The base repository is `matplotlib/matplotlib` and the base
branch is generally `main`.

Enter a title for the set of changes with some explanation of what
you\'ve done. Mention anything you\'d like particular attention for -
such as a complicated change or some code you are not happy with.

If you don\'t think your request is ready to be merged, make a
`draft pull request <draft-pr>`{.interpreted-text role="ref"} and state
what aspects you want to have feedback on. This is a good way of getting
some preliminary code review.

For more guidance on the mechanics of making a pull request, see
GitHub\'s [pull request
tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

## Update a pull request {#update-pull-request}

When updating your pull request after making revisions, instead of
adding new commits, please consider amending your initial commit(s) to
keep the commit history clean.

You can achieve this by using

``` bash
git commit -a --amend --no-edit
git push [your-remote-repo] [your-branch] --force-with-lease
```

::: tip
::: title
Tip
:::

Instead of typing your branch name every time, you only need to type the
following once to link the remote branch to the local branch:

git push \--set-upstream origin my-new-feature

From now on git will know that `my-new-feature` is related to the
`my-new-feature` branch in the GitHub repo. After this, you will be able
to push your changes with:

git push
:::

## Manage commit history

### Explore your repository

To see a graphical representation of the repository branches and
commits:

``` bash
gitk --all
```

To see a linear list of commits for this branch:

``` bash
git log
```

### Recover from mistakes {#recovering-from-mess-up}

Sometimes, you mess up merges or rebases. Luckily, in git it is
relatively straightforward to recover from such mistakes.

If you mess up during a rebase:

``` bash
git rebase --abort
```

If you notice you messed up after the rebase:

``` bash
# reset branch back to the saved point
git reset --hard tmp
```

If you forgot to make a backup branch:

``` bash
# look at the reflog of the branch
git reflog show cool-feature

8630830 cool-feature@{0}: commit: BUG: io: close file handles immediately
278dd2a cool-feature@{1}: rebase finished: refs/heads/my-feature-branch onto 11ee694744f2552d
26aa21a cool-feature@{2}: commit: BUG: lib: make seek_gzip_factory not leak gzip obj
...

# reset the branch to where it was before the botched rebase
git reset --hard cool-feature@{2}
```

### Rewrite commit history {#rewriting-commit-history}

::: note
::: title
Note
:::

Do this only for your own feature branches.
:::

Is there an embarrassing typo in a commit you made? Or perhaps you made
several false starts you don\'t want posterity to see.

This can be done via *interactive rebasing*.

Suppose that the commit history looks like this:

``` bash
git log --oneline
eadc391 Fix some remaining bugs
a815645 Modify it so that it works
2dec1ac Fix a few bugs + disable
13d7934 First implementation
6ad92e5 * masked is now an instance of a new object, MaskedConstant
29001ed Add pre-nep for a copule of structured_array_extensions.
...
```

and `6ad92e5` is the last commit in the `cool-feature` branch. Suppose
we want to make the following changes:

-   Rewrite the commit message for `13d7934` to something more sensible.
-   Combine the commits `2dec1ac`, `a815645`, `eadc391` into a single
    one.

We do as follows:

``` bash
# make a backup of the current state
git branch tmp HEAD
# interactive rebase
git rebase -i 6ad92e5
```

This will open an editor with the following text in it:

``` bash
pick 13d7934 First implementation
pick 2dec1ac Fix a few bugs + disable
pick a815645 Modify it so that it works
pick eadc391 Fix some remaining bugs

# Rebase 6ad92e5..eadc391 onto 6ad92e5
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#
# If you remove a line here THAT COMMIT WILL BE LOST.
# However, if you remove everything, the rebase will be aborted.
#
```

To achieve what we want, we will make the following changes to it:

``` bash
r 13d7934 First implementation
pick 2dec1ac Fix a few bugs + disable
f a815645 Modify it so that it works
f eadc391 Fix some remaining bugs
```

This means that (i) we want to edit the commit message for `13d7934`,
and (ii) collapse the last three commits into one. Now we save and quit
the editor.

Git will then immediately bring up an editor for editing the commit
message. After revising it, we get the output:

``` bash
[detached HEAD 721fc64] FOO: First implementation
 2 files changed, 199 insertions(+), 66 deletions(-)
[detached HEAD 0f22701] Fix a few bugs + disable
 1 files changed, 79 insertions(+), 61 deletions(-)
Successfully rebased and updated refs/heads/my-feature-branch.
```

and now, the history looks like this:

``` bash
0f22701 Fix a few bugs + disable
721fc64 ENH: Sophisticated feature
6ad92e5 * masked is now an instance of a new object, MaskedConstant
```

If it went wrong, recovery is again possible as explained `above
<recovering-from-mess-up>`{.interpreted-text role="ref"}.

If you have not yet pushed this branch to github, you can carry on as
normal, however if you *have* already pushed this commit see
`force-push`{.interpreted-text role="ref"} for how to replace your
already published commits with the new ones.

### Rebase onto `upstream/main` {#rebase-on-main}

Let\'s say you thought of some work you\'d like to do. You
`update-mirror-main`{.interpreted-text role="ref"} and
`make-feature-branch`{.interpreted-text role="ref"} called
`cool-feature`. At this stage, `main` is at some commit, let\'s call it
E. Now you make some new commits on your `cool-feature` branch, let\'s
call them A, B, C. Maybe your changes take a while, or you come back to
them after a while. In the meantime, `main` has progressed from commit E
to commit (say) G:

``` none
A---B---C cool-feature
/
D---E---F---G main
```

At this stage you consider merging `main` into your feature branch, and
you remember that this page sternly advises you not to do that, because
the history will get messy. Most of the time, you can just ask for a
review without worrying about whether `main` has got a little ahead;
however sometimes, the changes in `main` might affect your changes, and
you need to harmonize them. In this situation you may prefer to do a
rebase.

`rebase` takes your changes (A, B, C) and replays them as if they had
been made to the current state of `main`. In other words, in this case,
it takes the changes represented by A, B, C and replays them on top of
G. After the rebase, your history will look like this:

``` none
A'--B'--C' cool-feature
/
D---E---F---G main
```

See [rebase without
tears](https://matthew-brett.github.io/pydagogue/rebase_without_tears.html)
for more detail.

To do a rebase on `upstream/main`:

``` bash
# Fetch changes from upstream/main
git fetch upstream
# go to the feature branch
git checkout cool-feature
# make a backup in case you mess up
git branch tmp cool-feature
# rebase cool-feature onto main
git rebase --onto upstream/main upstream/main cool-feature
```

In this situation, where you are already on branch `cool-feature`, the
last command can be written more succinctly as:

``` bash
git rebase upstream/main
```

When all looks good, you can delete your backup branch:

``` bash
git branch -D tmp
```

If it doesn\'t look good you may need to have a look at
`recovering-from-mess-up`{.interpreted-text role="ref"}.

If you have made changes to files that have also changed in `main`, this
may generate merge conflicts that you need to resolve - see the [git
rebase](https://git-scm.com/docs/git-rebase) man page for some
instructions at the end of the \"Description\" section. There is some
related help on merging in the git user manual - see [resolving a
merge](https://schacon.github.io/git/user-manual.html#resolving-a-merge).

If you have not yet pushed this branch to github, you can carry on as
normal, however if you *have* already pushed this commit see
`force-push`{.interpreted-text role="ref"} for how to replace your
already published commits with the new ones.

### Push with force {#force-push}

If you have in some way re-written already pushed history (e.g. via
`rewriting-commit-history`{.interpreted-text role="ref"} or
`rebase-on-main`{.interpreted-text role="ref"}) leaving you with a git
history that looks something like

``` none
A'--E cool-feature
/
D---A---B---C origin/cool-feature
```

where you have pushed the commits `A,B,C` to your fork on GitHub (under
the remote name *origin*) but now have the commits `A'` and `E` on your
local branch *cool-feature*. If you try to push the new commits to
GitHub, it will fail and show an error that looks like :

``` bash
$ git push
Pushing to github.com:origin/matplotlib.git
To github.com:origin/matplotlib.git
 ! [rejected]              cool_feature -> cool_feature (non-fast-forward)
error: failed to push some refs to 'github.com:origin/matplotlib.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

If this push had succeeded, the commits `A`, `B`, and `C` would no
longer be referenced by any branch and they would be discarded:

``` none
D---A'---E cool-feature, origin/cool-feature
```

By default `git push` helpfully tries to protect you from accidentally
discarding commits by rejecting the push to the remote. When this
happens, GitHub also adds the helpful suggestion to pull the remote
changes and then try pushing again. In some cases, such as if you and a
colleague are both committing and pushing to the same branch, this is a
correct course of action.

However, in the case of having intentionally re-written history, we
*want* to discard the commits on the remote and replace them with the
new-and-improved versions from our local branch. In this case, what we
want to do is :

``` bash
$ git push --force-with-lease
```

which tells git you are aware of the risks and want to do the push
anyway. We recommend using `--force-with-lease` over the `--force` flag.
The `--force` will do the push no matter what, whereas
`--force-with-lease` will only do the push if the remote branch is where
the local `git` client thought it was.

Be judicious with force-pushing. It is effectively re-writing published
history, and if anyone has fetched the old commits, it will have a
different view of history which can cause confusion.

## Automated tests

Whenever a pull request is created or updated, various automated test
tools will run on all supported platforms and versions of Python.

-   [tox]() is not used in the automated testing. It is supported for
    testing locally.
-   Codecov and CodeQL are currently for information only. Their failure
    is not necessarily a blocker.

Make sure the Linting, GitHub Actions, AppVeyor, CircleCI, and Azure
pipelines are passing before merging. All checks are listed at the
bottom of the GitHub page of your pull request.

+-------------+-------------+------------------------------------------+
| Name        | Check       | Tips for finding cause of failure        |
+=============+=============+==========================================+
| Linting     | `code styl  | Errors are displayed as annotations on   |
|             | e <code-sty | the pull request diff.                   |
|             | le>`{.inter |                                          |
|             | preted-text |                                          |
|             | role="ref"} |                                          |
+-------------+-------------+------------------------------------------+
| | Mypy      | `stati      | Errors are displayed as annotations on   |
| | Stubtest  | c type hint | the pull request diff.                   |
|             | s <type-hin |                                          |
|             | ts>`{.inter |                                          |
|             | preted-text |                                          |
|             | role="ref"} |                                          |
+-------------+-------------+------------------------------------------+
| CircleCI    | `docu       | Search the CircleCI log for `WARNING`.   |
|             | mentation b |                                          |
|             | uild <writi |                                          |
|             | ng-rest-pag |                                          |
|             | es>`{.inter |                                          |
|             | preted-text |                                          |
|             | role="ref"} |                                          |
+-------------+-------------+------------------------------------------+
| | GitHub    | `t          | | Search the log for `FAILURES`.         |
|   Actions   | ests <testi |   Subsequent section should contain      |
| | AppVeyor  | ng>`{.inter |   information on failed tests.           |
| | Azure     | preted-text | |                                        |
|   pipelines | role="ref"} | | On Azure, find the images as           |
|             |             |   *artifacts* of the Azure job:          |
|             |             | | 1. Click *Details* on the check on the |
|             |             |   GitHub PR page.                        |
|             |             | | 2. Click *View more details on Azure   |
|             |             |   Pipelines* to go to Azure.             |
|             |             | | 3. On the overview page *artifacts*    |
|             |             |   are listed in the section *Related*.   |
+-------------+-------------+------------------------------------------+

### Skip CI checks

If you know only a subset of CI checks need to be run, you can skip
unneeded CI checks on individual commits by including the following
strings in the commit message:

+-----------------+-------------+--------------------------------------+
| String          | Effect      | Notes                                |
+=================+=============+======================================+
| `[ci doc]`      | Only run    | | For when you have only changed     |
|                 | do          |   documentation.                     |
|                 | cumentation | | `[ci doc]` is applied              |
|                 | checks.     |   automatically when the changes are |
|                 |             |   only to files in `doc/**/` or      |
|                 |             |   `galleries/**/`                    |
+-----------------+-------------+--------------------------------------+
| `[skip doc]`    | Skip        | For when you didn\'t change          |
|                 | do          | documentation.                       |
|                 | cumentation |                                      |
|                 | checks.     |                                      |
+-----------------+-------------+--------------------------------------+
| `[              | Skip        | Substring must be in first line of   |
| skip appveyor]` | AppVeyor    | commit message.                      |
|                 | run.        |                                      |
+-----------------+-------------+--------------------------------------+
| `[skip azp]`    | Skip Azure  |                                      |
|                 | Pipelines.  |                                      |
+-----------------+-------------+--------------------------------------+
| `               | Skip GitHub |                                      |
| [skip actions]` | Actions.    |                                      |
+-----------------+-------------+--------------------------------------+
| `[skip ci]`     | Skip all CI | Use only for changes where           |
|                 | checks.     | documentation checks and unit tests  |
|                 |             | do not apply.                        |
+-----------------+-------------+--------------------------------------+

`[skip actions]` and `[skip ci]` only skip Github Actions CI workflows
that are triggered on `on: push` and `on: pull_request` events. For more
information, see [Skipping workflow
runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs).
