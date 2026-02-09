# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/file-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/file-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/file-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/file-exclusions.md

# File exclusions

All versions of SonarQube for IDE will fetch file exclusions from SonarQube (Server, Cloud) or SonarQube Community Build when you bind a project while running in connected mode. Locally defined file exclusions will be ignored when running in connected mode. For more information about how SonarQube for Visual Studio settings are handled by the server, look at the server documentation on setting your analysis scope:

* See the [Setting analysis scope](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/project-administration/setting-analysis-scope "mention") pages in SonarQube Server.
* See the [Analysis scope](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/managing-your-projects/project-analysis/setting-analysis-scope "mention") pages in SonarQube Cloud.
* See the [Setting analysis scope](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/project-administration/adjusting-analysis/setting-analysis-scope "mention") pages in SonarQube Community Build.

### File exclusions in the IDE <a href="#file-exclusions-in-the-ide" id="file-exclusions-in-the-ide"></a>

When running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") with SonarQube (Server, Cloud) or SonarQube Community Build, SonarQube for IDE will ignore local exclusions and fetch file exclusions from the SonarQube (Server, Cloud) server.

Defining file exclusions locally in SonarQube for VS Code is possible in versions 3.22 and newer.

### Defining file exclusions <a href="#defining-file-exclusions" id="defining-file-exclusions"></a>

The `sonarlint.analysisExcludesStandalone` property is a simple way to locally exclude files from your analysis and can be used to configure wildcard patterns for files that *only SonarQube for IDE* will exclude. For example:

* The glob pattern `**/file[1-3].py`
* will exclude `file1.py`, `file2.py` and `file3.py`

Go to VS Code **Manage** > **Settings** > **Workspace** (or **Code** > **Settings…** > **Settings \[⌘,]** in macOS) and search `sonarlint.analysisExcludesStandalone` to add your exclusion patterns.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-e965e6a61464fe46e031d60f092c08c2814bf0f5%2F8cf25e50e4f476b4682bb701a51d58d696f9f02f.png?alt=media" alt="Check that you have selected &#x22;Sonarlint: Analysis Excludes Standalone&#x22; in your Workspace settings." width="375"><figcaption></figcaption></figure></div>

A second exclusion method configures VS Code to exclude files from your workspace; however, this may have unintended consequences such as *files disappearing from the VS Code* ***Explorer*** *view*.

To use VS Code’s file exclusions, go to VS Code **Manage** > **Settings** > **Workspace** (or **Code** > **Settings…** > **Settings \[⌘,]** in macOS), search `Files: Exclude` and select **Add Pattern**. The **Workspace** setting has information about how VS Code uses wildcard patterns to manage exclusions in the editor.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-cf5db8486e855650d2a477811cf17f2d28f31408%2Fd41c29b1518bf669ee44f8eb969291f409c44e8f.png?alt=media" alt="You can add exclusion patterns via the VS Code Workspace setting by searching for &#x22;Files: Exclude&#x22;" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that when running in connected mode, only the file exclusions defined on the server are respected.

When running a local analysis for security hotspots, which requires using connected mode, it is possible to omit some files and folders from the project analysis. Because you are in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"), a requirement to detect security hotspots in SonarQube for IDE, exclusions defined in VS Code will be ignored.

Check the documentation on [#reporting-security-hotspots-in-the-whole-folder](https://docs.sonarsource.com/sonarqube-for-vs-code/security-hotspots#reporting-security-hotspots-in-the-whole-folder "mention") for those details.
{% endhint %}

### Wildcard patterns <a href="#using-wildcards" id="using-wildcards"></a>

The recognized path-matching patterns are case-sensitive and defined using the following wildcards:

* `*` Match zero or more characters (not including the directory delimiter, `/` ).
* `**` Match zero or more directory segments or files within the path.
* `?` Match a single character (not including the directory delimiter, `/` ).

**Wildcard examples**

* The pattern `**/*.css`
  * matches `anyDirectory/anyFile.css`
  * doesn’t match `org/sonar.api/MyBean.java`
* The pattern `**/*Bean.java`
  * matches `org/sonar.api/MyBean.java`
  * doesn’t match `org/sonar.api/mybean.java` or `org/sonar/util/MyDTO.java`
* The pattern `**/*Bean?.java`
  * matches `org/sonar/util/MyOtherBean1.java`
  * doesn’t match `org/sonar/util/MyOtherBean.java`
* The pattern `org/sonar/*`
  * matches `org/sonar/MyClass.java`
  * doesn’t match `org/sonar/util/MyClassUtil.java`
* The pattern `org/sonar/**/*` is equivalent to `org/sonar/**` and
  * matches `org/sonar/anyDirectory/anyFile`
  * matches `org/sonar/MyClass.java`
  * doesn’t match `org/radar/MyClass.java`

The use of `?` to match a single character is available in SonarQube for VS Code v4.0+.
