# Source: https://github.com/TigerVNC/tigervnc/wiki/Development:-Making-a-Release

Quick guide to how we make releases.

# Creating a new branch 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#creating-a-new-branch)

1.  Update the translation template file:

    ::: 
        $ make translations_update
    :::

2.  Go through the changes, and see if there is anything that looks strange, or should be adjusted:

    ::: 
        $ git diff -I '^#' po/tigervnc.pot
    :::

3.  Commit the new template file:

    ::: 
        $ git commit -m "Update translation template file" po/tigervnc.pot
    :::

4.  Create the release branch:

    ::: 
        $ git branch 1.2-branch master
    :::

5.  Check out the master branch:

    ::: 
        $ git checkout master
    :::

6.  Update the version number in these files:

    -   `CMakeLists.txt`
    -   `java/CMakeLists.txt`
    -   `unix/xserver/hw/vnc/xvnc.c`

    If the release is 1.2.0 then the master branch should have 1.2.80 as the version number.

7.  Commit the version change:

    ::: 
        $ git commit -m "Change development version to 1.2.80" \
        CMakeLists.txt java/CMakeLists.txt unix/xserver/hw/vnc/xvnc.c
    :::

8.  Push the master branch to GitHub:

    ::: 
        $ git push --dry-run git@github.com:TigerVNC/tigervnc.git master

        (check that everything looks sane)

        $ git push git@github.com:TigerVNC/tigervnc.git master
    :::

# Beta 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#beta)

1.  Check out the release branch:

    ::: 
        $ git checkout 1.2-branch
    :::

2.  Update the version number in these files:

    -   `CMakeLists.txt`
    -   `java/CMakeLists.txt`
    -   `unix/xserver/hw/vnc/xvnc.c`

3.  Commit the version change:

    ::: 
        $ git commit -m "TigerVNC 1.1.90 (1.2.0 beta)" \
        CMakeLists.txt java/CMakeLists.txt unix/xserver/hw/vnc/xvnc.c
    :::

4.  Tag the beta:

    ::: 
        $ git tag -a -m "TigerVNC 1.1.90 (1.2.0 beta)" v1.1.90 1.2-branch
    :::

5.  Push everything to GitHub:

    ::: 
        $ git push --dry-run git@github.com:TigerVNC/tigervnc.git v1.1.90 1.2-branch

        (check that everything looks sane)

        $ git push git@github.com:TigerVNC/tigervnc.git v1.1.90 1.2-branch
    :::

6.  Create a build (only Brian can do this right now)

7.  Create a release entry on SourceForge. Use the `beta` folder.

8.  Upload all the built files.

9.  Grab `README.rst` from a previous release and upload an adjusted version for this new release.

10. Fill out the GitHub release using this template as a base:

    ::: 
        A beta of TigerVNC 1.2.0 is now available. Lots of changes have been made since
        the last release, but the highlights are:

          - Something
          - Something else
          - Something more

        Binaries are available from SourceForge:

        https://sourceforge.net/projects/tigervnc/files/beta/1.2beta

        Regards
        The TigerVNC Developers
    :::

11. Use the same template as above and send an annoucement to the `tigervnc-announce` mailing list.

12. Inform the translation project that a new release needs translation.

# Proper release 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#proper-release)

This follows the same steps as the beta, except for these changes:

-   Don\'t inform the translation project about the new release.

-   Use the simple \"TigerVNC 1.2.0\" as the version commit and tag message.

-   Update the HTML version of the man pages on the main web page. You can generate them using groff:

    ::: 
        $ groff -mandoc -Thtml -P-l Xvnc.man > Xvnc.html
    :::

-   Use the `stable` folder on SourceForge.

-   Mark the binaries as the default downloads for each platform

# Bug fix releases 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#bug-fix-releases)

No beta is done for bug fix releases, and commits should be added to the already existing release branch (e.g. 1.14-branch when creating bug fix release 1.14.1). See instructions below:

1.  Check out the release branch:

    ::: 
        $ git checkout 1.14-branch
    :::

2.  Cherry-pick the commits that should be included in the new release. Remember to use `git cherry-pick -x` to get a reference to the original commit.

    -   A tip is to push a small number of commits at a time, to simplify troubleshooting if the GitHub checks do not pass.

3.  Update the version number in these files:

    -   `CMakeLists.txt`
    -   `java/CMakeLists.txt`
    -   `unix/xserver/hw/vnc/xvnc.c`

4.  Commit the version change:

    ::: 
        $ git commit -m "TigerVNC 1.14.1" \
        CMakeLists.txt java/CMakeLists.txt unix/xserver/hw/vnc/xvnc.c
    :::

5.  Tag the beta:

    ::: 
        $ git tag -a -m "TigerVNC 1.14.1" v1.14.1 1.14-branch
    :::

6.  Push everything to GitHub:

    ::: 
        $ git push --dry-run git@github.com:TigerVNC/tigervnc.git v1.14.1 1.14-branch

        (check that everything looks sane)

        $ git push git@github.com:TigerVNC/tigervnc.git v1.14.1 1.14-branch
    :::

7.  Create a build (only Brian can do this right now)

8.  Create a release entry on SourceForge. Use the `stable` folder.

9.  Upload all the built files.

10. Grab `README.rst` from a previous release and upload an adjusted version for this new release.

11. Update the HTML version of the man pages on the main web page. You can generate them using groff:

    ::: 
        $ groff -mandoc -Thtml -P-l Xvnc.man > Xvnc.html
    :::

12. Fill out the GitHub release using this template as a base:

    ::: 
        The bugfix release TigerVNC 1.14.1 is now available. This release fixes a number
        of regressions, the most prominent being:

          - Something
          - Something else
          - Something more

        Binaries are available from SourceForge:

        https://sourceforge.net/projects/tigervnc/files/stable/1.14.1

        Regards
        The TigerVNC Developers
    :::

13. Use the same template as above and send an announcement to the `tigervnc-announce` mailing list.

The wiki is read-only because of malware spam that GitHub refuses to provide protection agains. Contact the maintainers directly with changes you\'d like to make.