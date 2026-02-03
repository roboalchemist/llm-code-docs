# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/pli.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/pli.md

# PLI

*PLI* analysis is available starting in [*Enterprise Edition.*](https://www.sonarsource.com/plans-and-pricing/enterprise/)

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the PL/I-specific [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") in: **Administration** > **Configuration** > **General Settings** > **Languages** > **PL/I**

### Source code extraction <a href="#source-code-extraction" id="source-code-extraction"></a>

In order to analyze your source code with SonarQube Server, you need to first extract it onto a filesystem. You can use your own tool or an open-source tool. Sonar does not provide any connectors or source code extraction tools.

### Dealing with-includes <a href="#dealing-with-includes" id="dealing-with-includes"></a>

There are two possible ways to tell SonarQube Server where to retrieve the source code referenced by a `%INCLUDE` statement.

The following syntaxes are supported:

```css-79elbk
%INCLUDE 'C:/temp/myLib.pli'
%INCLUDE ddname(member);
%INCLUDE member; /* With member not enclosed within single or double quotes, i.e. a SYSLIB member */
```

Example:

If you want to interpret:

```css-79elbk
%INCLUDE O (XX02511) as %INCLUDE 'C:/temp/o/XX02511.99IPO';
%INCLUDE lib1 as %INCLUDE 'C:/temp/syslib/lib1.pli';
```

the Ddnames are defined as:

```css-79elbk
sonar.pli.includeDdnames=O,SYSLIB

sonar.pli.includeDdname.O.path=c:/temp/o
sonar.pli.includeDdname.O.suffix=.99IPO

sonar.pli.includeDdname.SYSLIB.path=c:/temp/syslib
sonar.pli.includeDdname.SYSLIB.suffix=.pli
```

Note that the following constructs, involving at least two members, are currently not supported:

```css-79elbk
%INCLUDE member1, member2;
%INCLUDE ddname1(member1), member2;
%INCLUDE member1, ddname1(member2);
%INCLUDE ddname1(member1), ddname2(member2);
```

### Related Pages <a href="#related-pages" id="related-pages"></a>

* [adding-coding-rules](https://docs.sonarsource.com/sonarqube-server/extension-guide/adding-coding-rules "mention")
