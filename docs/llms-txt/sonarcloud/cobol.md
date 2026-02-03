# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/cobol.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/cobol.md

# COBOL

This language is available only in the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention").

### Language-Specific Properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the COBOL-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Cobol**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Source code extraction <a href="#source-code-extraction" id="source-code-extraction"></a>

In order to analyze your source code with SonarQube Cloud, you need to first extract it onto a filesystem. You can use your own tool or an open-source tool; Sonar does not provide any connectors or source code extraction tools.

### Advanced Configuration <a href="#advanced-configuration" id="advanced-configuration"></a>

#### Defining Source Code Format <a href="#defining-source-code-format" id="defining-source-code-format"></a>

The supported source code formats are:

* Fixed format
* Free format
* Variable format

To set the format, go to Project **Administration** > **General Settings** > **Languages** > **Cobol** and set the **Source format** property.

The fixed format has three main areas:

```cobol
Area1 | Area2                                           | Area3
000100* MY COMMENT
000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. HELLOWORLD.                          *xxx
100000 PROCEDURE DIVISION.                              *yyy
100100
100200 START.
100400 DISPLAY "HELLO COBOL !" LINE 42 POSITION 12.
100500 STOP RUN.
```

Areas #1 and #3 contain non-significant characters. Area #2 contains the source code. The first character of Area #2 is the Indicator Area, which has a special meaning (for example, `*` means that the line is a comment line, `D` means that the line is only taken into account in debug mode, etc.).

The free format:

```cobol
Area1 | Area2
     * MY COMMENT
      IDENTIFICATION DIVISION.
        PROGRAM-ID. HELLOWORLD.
      PROCEDURE DIVISION.
        DISPLAY "HELLO COBOL !" LINE 42 POSITION 12.
        STOP RUN.
```

The Indicator Area that has a special meaning (for instance `*` means that the line is a comment line, `D` means that the line in only taken into account in debug mode, etc.) is located at column 0. The size of the source code area is not limited.

The variable format is also supported: it’s similar to the fixed format but without Area #3.

#### Defining COBOL Dialect <a href="#defining-cobol-dialect" id="defining-cobol-dialect"></a>

Go to Project **Administration** > **General Settings** > **Languages** > **Cobol** and set the **Dialect** property.

COBOL analysis supports the following dialects:

* `bull-gcos-cobol`
* `hp-tandem-cobol`
* `ibm-os/vs-cobol`
* `ibm-ile-cobol`
* `ibm-cobol/ii`
* `ibm-cobol/400`
* `ibm-enterprise-cobol`
* `microfocus-cobol`
* `microfocus-acucobol-gt-cobol`
* `opencobol/cobol-it`

#### Making Copybooks Available to the Analysis <a href="#making-copybooks-available-to-the-analysis" id="making-copybooks-available-to-the-analysis"></a>

Copybooks are, by definition, COBOL files that are not syntactically valid by themselves. However, copybooks are usually needed to properly parse COBOL programs. Thus, paths to the copybooks must be listed through the `sonar.cobol.copy.directories` property.

#### Raising Issues Against Copybooks <a href="#raising-issues-against-copybooks" id="raising-issues-against-copybooks"></a>

To have copybooks imported into a project, and issues logged against them, the copybook directories must be added to `sonar.sources` AND the copybook file suffixes must be added to `sonar.cobol.file.suffixes`. E.G.:

```properties
sonar.sources=cobol,copy1,commonCopy
sonar.cobol.file.suffixes=cbl,cpy
sonar.cobol.copy.suffixes=cpy
sonar.cobol.copy.directories=copy1,commonCopy
```

In the case where a number of projects share a common set of copybooks, it may not be desirable to increment each project’s technical debt with the issues from the common copybooks. In such cases, the directory holding the common copybooks should be listed in `sonar.cobol.copy.directories` (as before) but left out of `sonar.sources`, for example:

```properties
sonar.sources=cobol,copy1
sonar.cobol.file.suffixes=cbl,cpy
sonar.cobol.copy.suffixes=cpy
sonar.cobol.copy.directories=copy1,commonCopy
```

#### Analyzing without file suffixes <a href="#analyzing-without-file-suffixes" id="analyzing-without-file-suffixes"></a>

Note that it is possible to analyze a COBOL project without file suffixes. To do this, remove the two suffix-related properties from your configuration and substitute the following setting:

`sonar.lang.patterns.cobol=**/*`

#### Switching Off Issues <a href="#switching-off-issues" id="switching-off-issues"></a>

There are three ways to switch off issues:

* See [#false-positive](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/editing#false-positive "mention")
* Using [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention") to ignore issues.
* Using the `NOSONAR` tag. To switch off an issue, place the `NOSONAR` tag in a comment line located right before the line containing the issue. Example:

`* NOSONAR, in such case call to GO TO is tolerated, blabla...`\
`GO TO MY_PARAGRAPH.`

#### ACUCOBOL-GT Source Code Control Directives <a href="#acucobolgt-source-code-control-directives" id="acucobolgt-source-code-control-directives"></a>

COBOL analysis supports the ACUCOBOL-GT’s Source Code Control directives. This mechanism allows you to conditionally modify the program at compile time by excluding or including lines. This can be used to maintain different versions of the program, perhaps to support different machine environments.

The `-Si` (include) flag controls the actions of the source code control system. It must be followed by an argument that specifies a pattern that the compiler will search for in the Identification Area of each source line. If the pattern is found, then the line will be included in the source program, even if it is a comment line. However, if the pattern is immediately preceded by an exclamation point, then the line will be excluded from the source (i.e., commented out).

The `-Sx` (exclude) flag works the same way, except that its meaning is reversed (lines with the pattern will be commented out and lines with a preceding exclamation point will be included).

For example, suppose a program is being maintained for both the UNIX and VMS environments. The following piece of code is in the program:

```cobol
MOVE "SYS$HELP:HELPFILE" TO FILE-NAME.  VMS
*MOVE "/etc/helpfile" TO FILE-NAME.     UNX
OPEN INPUT HELP-FILE.
```

This program fragment is ready to be compiled for the VMS system. If a UNIX version is desired, then the following flags will correct the source during compilation:

```bash
-Si UNX -Sx VMS
```

Please consult the ACUCOBOL-GT documentation for more on the mechanism.

There are two ways in SonarQube Cloud to specify the list of ACUCOBOL-GT flags to be used in order to preprocess the source code. The first option is to define a list of global flags which will be used to preprocess all source files. This can be done in the **Administration** > **General Settings** > **Languages** > **Cobol** > **Preprocessor**.

The second option is to provide a list of relative paths (with help of the `sonar.cobol.acucobol.preprocessor.directives.directories` property) which contain the list of flags to be used for each COBOL source file. Let’s take a simple example. If a file `MY_PROGRAM.CBL` is going to be processed, the SonarQube ACUCOBOL-GT preprocessor will try to find a file `MY_PROGRAM.CMD`. If this file is found, then the flags contained in this file are used to preprocess the program `MY_PROGRAM.CBL`. If the file `MY_PROGRAM.CMD` doesn’t exist, then the preprocessor will use the content of the file `DEFAULT.CMD`, if it exists.

#### Microfocus Compiler Constants <a href="#microfocus-compiler-constants" id="microfocus-compiler-constants"></a>

If your code takes advantage of conditional compilation features provided by Microfocus, you may have to configure compiler constants for your analysis.

For example, if your COBOL code looks like this:

```cobol
       IDENTIFICATION DIVISION.
      $IF myconstant DEFINED
       PROGRAM-ID. x.
      $END
      $IF otherconstant DEFINED
       PROGRAM-ID. y.
      $END
```

Go to Project **Administration** > **General Settings** > **Languages** > **Cobol** and declare each constant by name with an associated value.

Defining the constant via `sonar.cobol.compilationConstant.[constant name here]` in `sonar-project.properties` is deprecated since version 4.5 of the COBOL analyzer.

### Database Catalog (DB2) <a href="#database-catalog-db2" id="database-catalog-db2"></a>

COBOL analysis offers rules which target embedded SQL statements and require the analyzer to have knowledge of the database catalog (for example, the primary key column(s) of a given table). These rules will raise issues only if the database catalog is provided for the analysis. For the moment, this is available only for IBM DB2 (z/OS) catalogs, and the catalog must be provided via a set of CSV ("Comma Separated Values") files.

These rules rely on two analysis properties:

| **Key**                                 | **Description**                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| `sonar.cobol.sql.catalog.csv.path`      | relative path of the directory containing CSV files for the database catalog     |
| `sonar.cobol.sql.catalog.defaultSchema` | comma-separated list of default database schemas used in embedded SQL statements |

`sonar.cobol.sql.catalog.csv.path` should define a directory that contains 8 CSV files. Each of these CSV files contains data for a specific DB2 catalog table and is named after it. The following table lists the required files and their respective mandatory columns. Additional columns may be listed, but will be ignored:

| **Table**              | **File name**       | **Required Columns**                                                                   |
| ---------------------- | ------------------- | -------------------------------------------------------------------------------------- |
| `SYSIBM.SYSCOLUMNS`    | `SYSCOLUMNS.csv`    | `TBNAME`,`TBCREATOR`,`NAME`,`PARTKEY_COLSEQ`,`DEFAULT`,`NULLS`,`DEFAULTVALUE`          |
| `SYSIBM.SYSINDEXES`    | `SYSINDEXES.csv`    | `NAME`,`CREATOR`,`TBNAME`,`TBCREATOR`,`UNIQUERULE`,`INDEXTYPE`                         |
| `SYSIBM.SYSINDEXPART`  | `SYSINDEXPART.csv`  | `IXNAME`,`IXCREATOR`,`PARTITION`                                                       |
| `SYSIBM.SYSKEYS`       | `SYSKEYS.csv`       | `IXNAME`,`IXCREATOR`,`COLNAME`,`COLSEQ`                                                |
| `SYSIBM.SYSSYNONYMS`   | `SYSSYNONYMS.csv`   | `NAME`,`CREATOR`,`TBNAME`,`TBCREATOR`                                                  |
| `SYSIBM.SYSTABLES`     | `SYSTABLES.csv`     | `NAME`,`CREATOR`,`TYPE`,`PARTKEYCOLNUM`,`TSNAME`,`DBNAME`,`TBNAME`,`TBCREATOR`,`CARDF` |
| `SYSIBM.SYSTABLESPACE` | `SYSTABLESPACE.csv` | `NAME`,`DBNAME`,`PARTITIONS`                                                           |
| `SYSIBM.SYSVIEWS`      | `SYSVIEWS.csv`      | `NAME`,`CREATOR`,`STATEMENT`                                                           |

The CSV format is the following:

* Each file must be named for the table it represents.
* The first line must contain the names of the columns.
* The order of the columns is not meaningful.
* Fields are comma-delimited.
* If a field contains a comma, then its value must be surrounded by double quotes (").
* If a field that is surrounded by double quotes contains a double quote character ("), then this character must be doubled ("").

Example for `SYSVIEWS.csv`:

```csv
CREATOR,NAME,STATEMENT
USER1,VIEW1,select x from table1
USER1,VIEW2,"select x, y from table1"
USER1,VIEW3,"select x, ""y"" from table1"
```

The `UNLOAD` DB2 utility with the `DELIMITED` option should produce the required files except for the column names on the first line.
