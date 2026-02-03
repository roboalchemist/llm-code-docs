# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/pl-i.md

# PL/I

This language is available only in the SonarQube Cloud Enterprise plan. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more details.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the PL/I-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **PL/I**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Source code extraction <a href="#source-code-extraction" id="source-code-extraction"></a>

In order to analyze your source code with SonarQube Cloud you need to first extract it onto a file system. You can use your own tool or an open-source tool. Sonar does not provide any connectors or source code extraction tools.

### Dealing with-includes <a href="#dealing-with-includes" id="dealing-with-includes"></a>

There are two possible ways to tell SonarQube Cloud where to retrieve the source code referenced by an `%INCLUDE` statement.

The following syntaxes are supported:

```php
%INCLUDE 'C:/temp/myLib.pli'
%INCLUDE ddname(member);
%INCLUDE member; 
  /* With member not enclosed within single or double quotes, i.e. a SYSLIB member */
```

Example:

If you want to interpret:

```php
%INCLUDE O (XX02511) as %INCLUDE 'C:/temp/o/XX02511.99IPO';
%INCLUDE lib1 as %INCLUDE 'C:/temp/syslib/lib1.pli';
```

the Ddnames are defined as:

```php
  sonar.pli.includeDdnames=O,SYSLIB

  sonar.pli.includeDdname.O.path=c:/temp/o
  sonar.pli.includeDdname.O.suffix=.99IPO

  sonar.pli.includeDdname.SYSLIB.path=c:/temp/syslib
  sonar.pli.includeDdname.SYSLIB.suffix=.pli
```

Note that the following constructs, involving at least two members, are currently not supported:

```php
%INCLUDE member1, member2;
%INCLUDE ddname1(member1), member2;
%INCLUDE member1, ddname1(member2);
%INCLUDE ddname1(member1), ddname2(member2);
```
