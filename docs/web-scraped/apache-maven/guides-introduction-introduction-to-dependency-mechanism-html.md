# Source: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

Title: Introduction to the Dependency Mechanism – Maven

URL Source: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

Markdown Content:
[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
Dependency management is a core feature of Maven. Managing dependencies for a single project is easy. Managing dependencies for multi-module projects and applications that consist of hundreds of modules is possible. Maven helps a great deal in defining, creating, and maintaining reproducible builds with well-defined classpaths and library versions.

Learn more about:

*   [Transitive Dependencies](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Transitive_Dependencies)
*   [Dependency Scope](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Scope)
*   [Dependency Management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Management)
    *   [Importing Dependencies](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Importing_Dependencies)
    *   [Bill of Materials (BOM) POMs](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Bill_of_Materials_.28BOM.29_POMs)

*   [System Dependencies](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#System_Dependencies)
    *   [Historical usage: Java EE (javax) libraries of the JDK](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Historical_usage.3A_Java_EE_.28javax.29_libraries_of_the_JDK)

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
Transitive Dependencies[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#transitive-dependencies)
-----------------------------------------------------------------------------------------------------------------------------------------

Maven avoids the need to discover and specify the libraries that your own dependencies require by including transitive dependencies automatically.

This feature is facilitated by reading the project files of your dependencies from the remote repositories specified. In general, all dependencies of those projects are used in your project, as are any that the project inherits from its parents, or from its dependencies, and so on.

There is no limit to the number of levels that dependencies can be gathered from. A problem arises only if a cyclic dependency is discovered.

With transitive dependencies, the graph of included libraries can quickly grow quite large. For this reason, there are additional features that limit which dependencies are included:

*   _Dependency mediation_ - this determines what version of an artifact will be chosen when multiple versions are encountered as dependencies. Maven picks the “nearest definition”. That is, it uses the version of the closest dependency to your project in the tree of dependencies. You can always guarantee a version by declaring it explicitly in your project's POM. Note that if two dependency versions are at the same depth in the dependency tree, the first declaration wins. 
    *   “nearest definition” means that the version used will be the closest one to your project in the tree of dependencies. Consider this tree of dependencies:

```
A
  ├── B
  │   └── C
  │       └── D 2.0
  └── E
      └── D 1.0
```

In text, dependencies for A, B, and C are defined as A -> B -> C -> D 2.0 and A -> E -> D 1.0, then D 1.0 will be used when building A because the path from A to D through E is shorter. You could explicitly add a dependency to D 2.0 in A to force the use of D 2.0, as shown here:

```
A
  ├── B
  │   └── C
  │       └── D 2.0
  ├── E
  │   └── D 1.0
  │
  └── D 2.0
```

*   _Dependency management_ - this allows project authors to directly specify the versions of artifacts to be used when they are encountered in transitive dependencies or in dependencies where no version has been specified. In the example in the preceding section a dependency was directly added to A even though it is not directly used by A. Instead, A can include D as a dependency in its dependencyManagement section and directly control which version of D is used when, or if, it is ever referenced.
*   _Dependency scope_ - this allows you to only include dependencies appropriate for the current stage of the build. This is described in more detail below.
*   _Excluded dependencies_ - If project X depends on project Y, and project Y depends on project Z, the owner of project X can explicitly exclude project Z as a dependency, using the “exclusion” element.
*   _Optional dependencies_ - If project Y depends on project Z, the owner of project Y can mark project Z as an optional dependency, using the “optional” element. When project X depends on project Y, X will depend only on Y and not on Y's optional dependency Z. The owner of project X may then explicitly add a dependency on Z, at her option. (It may be helpful to think of optional dependencies as “excluded by default.”)

Although transitive dependencies can implicitly include desired dependencies, it is a good practice to explicitly specify the dependencies your source code uses directly. This best practice proves its value especially when the dependencies of your project change their dependencies.

For example, assume that your project A specifies a dependency on another project B, and project B specifies a dependency on project C. If you are directly using components in project C, and you don't specify project C in your project A, it may cause build failure when project B suddenly updates/removes its dependency on project C.

Another reason to directly specify dependencies is that it provides better documentation for your project: one can learn more information by just reading the POM file in your project, or by executing **mvn dependency:tree**.

Maven also provides [dependency:analyze](https://maven.apache.org/plugins/maven-dependency-plugin/analyze-mojo.html) plugin goal for analyzing the dependencies: it helps making this best practice more achievable.

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
Dependency Scope[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#dependency-scope)
---------------------------------------------------------------------------------------------------------------------------

Dependency scope is used to limit the transitivity of a dependency and to determine when a dependency is included in a classpath.

There are 6 scopes:

*   **compile**

 This is the default scope, used if none is specified. Compile dependencies are available in all classpaths of a project. Furthermore, those dependencies are propagated to dependent projects.
*   **provided**

 This is much like `compile`, but indicates you expect the JDK or a container to provide the dependency at runtime. For example, when building a web application for the Java Enterprise Edition, you would set the dependency on the Servlet API and related Java EE APIs to scope `provided` because the web container provides those classes. A dependency with this scope is added to the classpath used for compilation and test, but not the runtime classpath. It is not transitive.
*   **runtime**

 This scope indicates that the dependency is not required for compilation, but is for execution. Maven includes a dependency with this scope in the runtime and test classpaths, but not the compile classpath.
*   **test**

 This scope indicates that the dependency is not required for normal use of the application, and is only available for the test compilation and execution phases. This scope is not transitive. Typically, this scope is used for test libraries such as JUnit and Mockito. It is also used for non-test libraries such as Apache Commons IO if those libraries are used in unit tests (src/test/java) but not in the model code (src/main/java).
*   **system**

 This scope indicates that the dependency is required for compilation and execution. However, Maven will not download the dependency from the repository system. Instead, it looks for a jar in the local file system at a specified path.
*   **import**

 This scope is only supported on a dependency of type `pom` in the `<dependencyManagement>` section. It indicates the dependency is to be replaced with the effective list of dependencies in the specified POM's `<dependencyManagement>` section. Since they are replaced, dependencies with a scope of `import` do not actually participate in limiting the transitivity of a dependency.

Each of the scopes (except for `import`) affects transitive dependencies in a different way. For a dependency A, declared in the project (left column), and its transitive dependency B (top row), the table below shows the resulting scope of B based on both initial scope declarations. If the cell is empty, it means the dependency is omitted during the build of the project.

Examples:

*   If dependency A is declared as “compile” and its transitive dependency B is declared as “runtime”, then the resulting scope of B will be “runtime”.
*   If dependency A is declared as “compile” and its transitive dependency B is declared as “provided”, then B will be omitted.

|  | Scope of B (transitive dependency of A) |
| --- | --- |
| compile | provided | runtime | test |
| Scope of A (Project dependency) | compile | compile | - | runtime | - |
| provided | provided | - | provided | - |
| runtime | runtime | - | runtime | - |
| test | test | - | test | - |

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
Dependency Management[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#dependency-management)
-------------------------------------------------------------------------------------------------------------------------------------

The dependency management section is a mechanism for centralizing dependency information. When you have a set of projects that inherit from a common parent, it's possible to put all information about the dependency in the common POM and have simpler references to the artifacts in the child POMs. The mechanism is best illustrated through some examples. Given these two POMs which extend the same parent:

Project A:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `...`
4.   `<dependencies>`
5.   `<dependency>`
6.   `<groupId>group-a</groupId>`
7.   `<artifactId>artifact-a</artifactId>`
8.   `<version>1.0</version>`
9.   `<exclusions>`
10.   `<exclusion>`
11.   `<groupId>group-c</groupId>`
12.   `<artifactId>excluded-artifact</artifactId>`
13.   `</exclusion>`
14.   `</exclusions>`
15.   `</dependency>`
16.   `<dependency>`
17.   `<groupId>group-a</groupId>`
18.   `<artifactId>artifact-b</artifactId>`
19.   `<version>1.0</version>`
20.   `<type>bar</type>`
21.   `<scope>runtime</scope>`
22.   `</dependency>`
23.   `</dependencies>`
24.   `</project>`

Project B:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `...`
4.   `<dependencies>`
5.   `<dependency>`
6.   `<groupId>group-c</groupId>`
7.   `<artifactId>artifact-b</artifactId>`
8.   `<version>1.0</version>`
9.   `<type>war</type>`
10.   `<scope>runtime</scope>`
11.   `</dependency>`
12.   `<dependency>`
13.   `<groupId>group-a</groupId>`
14.   `<artifactId>artifact-b</artifactId>`
15.   `<version>1.0</version>`
16.   `<type>bar</type>`
17.   `<scope>runtime</scope>`
18.   `</dependency>`
19.   `</dependencies>`
20.   `</project>`

These two example POMs share a common dependency and each has one non-trivial dependency. This information can be put in the parent POM like this:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `...`
4.   `<dependencyManagement>`
5.   `<dependencies>`
6.   `<dependency>`
7.   `<groupId>group-a</groupId>`
8.   `<artifactId>artifact-a</artifactId>`
9.   `<version>1.0</version>`

11.   `<exclusions>`
12.   `<exclusion>`
13.   `<groupId>group-c</groupId>`
14.   `<artifactId>excluded-artifact</artifactId>`
15.   `</exclusion>`
16.   `</exclusions>`

18.   `</dependency>`

20.   `<dependency>`
21.   `<groupId>group-c</groupId>`
22.   `<artifactId>artifact-b</artifactId>`
23.   `<version>1.0</version>`
24.   `<type>war</type>`
25.   `<scope>runtime</scope>`
26.   `</dependency>`

28.   `<dependency>`
29.   `<groupId>group-a</groupId>`
30.   `<artifactId>artifact-b</artifactId>`
31.   `<version>1.0</version>`
32.   `<type>bar</type>`
33.   `<scope>runtime</scope>`
34.   `</dependency>`
35.   `</dependencies>`
36.   `</dependencyManagement>`
37.   `</project>`

Then the two child POMs become much simpler:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `...`
4.   `<dependencies>`
5.   `<dependency>`
6.   `<groupId>group-a</groupId>`
7.   `<artifactId>artifact-a</artifactId>`
8.   `</dependency>`

10.   `<dependency>`
11.   `<groupId>group-a</groupId>`
12.   `<artifactId>artifact-b</artifactId>`
13.   `<!-- This is not a jar dependency, so we must specify type. -->`
14.   `<type>bar</type>`
15.   `</dependency>`
16.   `</dependencies>`
17.   `</project>`

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `...`
4.   `<dependencies>`
5.   `<dependency>`
6.   `<groupId>group-c</groupId>`
7.   `<artifactId>artifact-b</artifactId>`
8.   `<!-- This is not a jar dependency, so we must specify type. -->`
9.   `<type>war</type>`
10.   `</dependency>`

12.   `<dependency>`
13.   `<groupId>group-a</groupId>`
14.   `<artifactId>artifact-b</artifactId>`
15.   `<!-- This is not a jar dependency, so we must specify type. -->`
16.   `<type>bar</type>`
17.   `</dependency>`
18.   `</dependencies>`
19.   `</project>`

**NOTE:** In two of these dependency references, we had to specify the <type/> element. This is because the minimal set of information for matching a dependency reference against a dependencyManagement section is actually **{groupId, artifactId, type, classifier}**. In many cases, these dependencies will refer to jar artifacts with no classifier. This allows us to shorthand the identity set to **{groupId, artifactId}**, since the default for the type field is `jar`, and the default classifier is null.

A second, and very important use of the dependency management section is to control the versions of artifacts used in transitive dependencies. As an example consider these projects:

Project A:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>maven</groupId>`
5.   `<artifactId>A</artifactId>`
6.   `<packaging>pom</packaging>`
7.   `<name>A</name>`
8.   `<version>1.0</version>`
9.   `<dependencyManagement>`
10.   `<dependencies>`
11.   `<dependency>`
12.   `<groupId>test</groupId>`
13.   `<artifactId>a</artifactId>`
14.   `<version>1.2</version>`
15.   `</dependency>`
16.   `<dependency>`
17.   `<groupId>test</groupId>`
18.   `<artifactId>b</artifactId>`
19.   `<version>1.0</version>`
20.   `<scope>compile</scope>`
21.   `</dependency>`
22.   `<dependency>`
23.   `<groupId>test</groupId>`
24.   `<artifactId>c</artifactId>`
25.   `<version>1.0</version>`
26.   `<scope>compile</scope>`
27.   `</dependency>`
28.   `<dependency>`
29.   `<groupId>test</groupId>`
30.   `<artifactId>d</artifactId>`
31.   `<version>1.2</version>`
32.   `</dependency>`
33.   `</dependencies>`
34.   `</dependencyManagement>`
35.   `</project>`

Project B:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<parent>`
4.   `<artifactId>A</artifactId>`
5.   `<groupId>maven</groupId>`
6.   `<version>1.0</version>`
7.   `</parent>`
8.   `<modelVersion>4.0.0</modelVersion>`
9.   `<groupId>maven</groupId>`
10.   `<artifactId>B</artifactId>`
11.   `<packaging>pom</packaging>`
12.   `<name>B</name>`
13.   `<version>1.0</version>`

15.   `<dependencyManagement>`
16.   `<dependencies>`
17.   `<dependency>`
18.   `<groupId>test</groupId>`
19.   `<artifactId>d</artifactId>`
20.   `<version>1.0</version>`
21.   `</dependency>`
22.   `</dependencies>`
23.   `</dependencyManagement>`

25.   `<dependencies>`
26.   `<dependency>`
27.   `<groupId>test</groupId>`
28.   `<artifactId>a</artifactId>`
29.   `<version>1.0</version>`
30.   `<scope>runtime</scope>`
31.   `</dependency>`
32.   `<dependency>`
33.   `<groupId>test</groupId>`
34.   `<artifactId>c</artifactId>`
35.   `<scope>runtime</scope>`
36.   `</dependency>`
37.   `</dependencies>`
38.   `</project>`

When maven is run on project B, version 1.0 of artifacts a, b, c, and d will be used regardless of the version specified in their POM.

*   a and c both are declared as dependencies of the project so version 1.0 is used due to dependency mediation. Both also have runtime scope since it is directly specified.
*   b is defined in B's parent's dependency management section and since dependency management takes precedence over dependency mediation for transitive dependencies, version 1.0 will be selected should it be referenced in a or c's POM. b will also have compile scope.
*   Finally, since d is specified in B's dependency management section, should d be a dependency (or transitive dependency) of a or c, version 1.0 will be chosen - again because dependency management takes precedence over dependency mediation and also because the current POM's declaration takes precedence over its parent's declaration.

**NOTE:** The dependency management won't affect the (transitive) dependencies of any _plugins_ used in the same effective POM but only the (transitive) project dependencies.

The reference information about the dependency management tags is available from the [project descriptor reference](https://maven.apache.org/ref/current/maven-model/maven.html#class_DependencyManagement).

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
### Importing Dependencies[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#importing-dependencies)

The examples in the previous section describe how to specify managed dependencies through inheritance. However, in larger projects it may be impossible to accomplish this since a project can only inherit from a single parent. To accommodate this, projects can import managed dependencies from other projects. This is accomplished by declaring a POM artifact as a dependency with a scope of “import”.

Project B:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>maven</groupId>`
5.   `<artifactId>B</artifactId>`
6.   `<packaging>pom</packaging>`
7.   `<name>B</name>`
8.   `<version>1.0</version>`

10.   `<dependencyManagement>`
11.   `<dependencies>`
12.   `<dependency>`
13.   `<groupId>maven</groupId>`
14.   `<artifactId>A</artifactId>`
15.   `<version>1.0</version>`
16.   `<type>pom</type>`
17.   `<scope>import</scope>`
18.   `</dependency>`
19.   `<dependency>`
20.   `<groupId>test</groupId>`
21.   `<artifactId>d</artifactId>`
22.   `<version>1.0</version>`
23.   `</dependency>`
24.   `</dependencies>`
25.   `</dependencyManagement>`

27.   `<dependencies>`
28.   `<dependency>`
29.   `<groupId>test</groupId>`
30.   `<artifactId>a</artifactId>`
31.   `<version>1.0</version>`
32.   `<scope>runtime</scope>`
33.   `</dependency>`
34.   `<dependency>`
35.   `<groupId>test</groupId>`
36.   `<artifactId>c</artifactId>`
37.   `<scope>runtime</scope>`
38.   `</dependency>`
39.   `</dependencies>`
40.   `</project>`

Assuming A is the POM defined in the preceding example, the end result would be the same. All of A's managed dependencies would be incorporated into B except for d since it is defined in this POM.

Project X:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>maven</groupId>`
5.   `<artifactId>X</artifactId>`
6.   `<packaging>pom</packaging>`
7.   `<name>X</name>`
8.   `<version>1.0</version>`

10.   `<dependencyManagement>`
11.   `<dependencies>`
12.   `<dependency>`
13.   `<groupId>test</groupId>`
14.   `<artifactId>a</artifactId>`
15.   `<version>1.1</version>`
16.   `</dependency>`
17.   `<dependency>`
18.   `<groupId>test</groupId>`
19.   `<artifactId>b</artifactId>`
20.   `<version>1.0</version>`
21.   `<scope>compile</scope>`
22.   `</dependency>`
23.   `</dependencies>`
24.   `</dependencyManagement>`
25.   `</project>`

Project Y:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>maven</groupId>`
5.   `<artifactId>Y</artifactId>`
6.   `<packaging>pom</packaging>`
7.   `<name>Y</name>`
8.   `<version>1.0</version>`

10.   `<dependencyManagement>`
11.   `<dependencies>`
12.   `<dependency>`
13.   `<groupId>test</groupId>`
14.   `<artifactId>a</artifactId>`
15.   `<version>1.2</version>`
16.   `</dependency>`
17.   `<dependency>`
18.   `<groupId>test</groupId>`
19.   `<artifactId>c</artifactId>`
20.   `<version>1.0</version>`
21.   `<scope>compile</scope>`
22.   `</dependency>`
23.   `</dependencies>`
24.   `</dependencyManagement>`
25.   `</project>`

Project Z:

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>maven</groupId>`
5.   `<artifactId>Z</artifactId>`
6.   `<packaging>pom</packaging>`
7.   `<name>Z</name>`
8.   `<version>1.0</version>`
9.   ``
10.   `<dependencyManagement>`
11.   `<dependencies>`
12.   `<dependency>`
13.   `<groupId>maven</groupId>`
14.   `<artifactId>X</artifactId>`
15.   `<version>1.0</version>`
16.   `<type>pom</type>`
17.   `<scope>import</scope>`
18.   `</dependency>`
19.   `<dependency>`
20.   `<groupId>maven</groupId>`
21.   `<artifactId>Y</artifactId>`
22.   `<version>1.0</version>`
23.   `<type>pom</type>`
24.   `<scope>import</scope>`
25.   `</dependency>`
26.   `</dependencies>`
27.   `</dependencyManagement>`
28.   `</project>`

In the example above Z imports the managed dependencies from both X and Y. However, both X and Y contain dependency a. Here, version 1.1 of a would be used since X is declared first and a is not declared in Z's dependencyManagement.

This process is recursive. For example, if X imports another POM, Q, when Z is processed it will simply appear that all of Q's managed dependencies are defined in X.

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
### Bill of Materials (BOM) POMs[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#bill-of-materials-bom-poms)

Imports are most effective when used for defining a “library” of related artifacts that are generally part of a multiproject build. It is fairly common for one project to use one or more artifacts from these libraries. However, it has sometimes been difficult to keep the versions in the project using the artifacts in synch with the versions distributed in the library. The pattern below illustrates how a “bill of materials” (BOM) can be created for use by other projects.

The root of the project is the BOM POM. It defines the versions of all the artifacts that will be created in the library. Other projects that wish to use the library should import this POM into the dependencyManagement section of their POM.

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">`
4.   `<modelVersion>4.0.0</modelVersion>`
5.   `<groupId>com.test</groupId>`
6.   `<artifactId>bom</artifactId>`
7.   `<version>1.0.0</version>`
8.   `<packaging>pom</packaging>`
9.   `<properties>`
10.   `<project1Version>1.0.0</project1Version>`
11.   `<project2Version>1.0.0</project2Version>`
12.   `</properties>`
13.   ``
14.   `<dependencyManagement>`
15.   `<dependencies>`
16.   `<dependency>`
17.   `<groupId>com.test</groupId>`
18.   `<artifactId>project1</artifactId>`
19.   `<version>${project1Version}</version>`
20.   `</dependency>`
21.   `<dependency>`
22.   `<groupId>com.test</groupId>`
23.   `<artifactId>project2</artifactId>`
24.   `<version>${project2Version}</version>`
25.   `</dependency>`
26.   `</dependencies>`
27.   `</dependencyManagement>`
28.   ``
29.   `<modules>`
30.   `<module>parent</module>`
31.   `</modules>`
32.   `</project>`

The parent subproject has the BOM POM as its parent. It is a normal multiproject pom.

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">`
4.   `<modelVersion>4.0.0</modelVersion>`
5.   `<parent>`
6.   `<groupId>com.test</groupId>`
7.   `<version>1.0.0</version>`
8.   `<artifactId>bom</artifactId>`
9.   `</parent>`

11.   `<groupId>com.test</groupId>`
12.   `<artifactId>parent</artifactId>`
13.   `<version>1.0.0</version>`
14.   `<packaging>pom</packaging>`

16.   `<dependencyManagement>`
17.   `<dependencies>`
18.   `<dependency>`
19.   `<groupId>log4j</groupId>`
20.   `<artifactId>log4j</artifactId>`
21.   `<version>1.2.12</version>`
22.   `</dependency>`
23.   `<dependency>`
24.   `<groupId>commons-logging</groupId>`
25.   `<artifactId>commons-logging</artifactId>`
26.   `<version>1.1.1</version>`
27.   `</dependency>`
28.   `</dependencies>`
29.   `</dependencyManagement>`
30.   `<modules>`
31.   `<module>project1</module>`
32.   `<module>project2</module>`
33.   `</modules>`
34.   `</project>`

Next are the actual project POMs.

2.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">`
4.   `<modelVersion>4.0.0</modelVersion>`
5.   `<parent>`
6.   `<groupId>com.test</groupId>`
7.   `<version>1.0.0</version>`
8.   `<artifactId>parent</artifactId>`
9.   `</parent>`
10.   `<groupId>com.test</groupId>`
11.   `<artifactId>project1</artifactId>`
12.   `<version>${project1Version}</version>`
13.   `<packaging>jar</packaging>`

15.   `<dependencies>`
16.   `<dependency>`
17.   `<groupId>log4j</groupId>`
18.   `<artifactId>log4j</artifactId>`
19.   `</dependency>`
20.   `</dependencies>`
21.   `</project>`

23.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
24.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">`
25.   `<modelVersion>4.0.0</modelVersion>`
26.   `<parent>`
27.   `<groupId>com.test</groupId>`
28.   `<version>1.0.0</version>`
29.   `<artifactId>parent</artifactId>`
30.   `</parent>`
31.   `<groupId>com.test</groupId>`
32.   `<artifactId>project2</artifactId>`
33.   `<version>${project2Version}</version>`
34.   `<packaging>jar</packaging>`

36.   `<dependencies>`
37.   `<dependency>`
38.   `<groupId>commons-logging</groupId>`
39.   `<artifactId>commons-logging</artifactId>`
40.   `</dependency>`
41.   `</dependencies>`
42.   `</project>`

The project that follows shows how the library can now be used in another project without having to specify the dependent project's versions.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">`
3.   `<modelVersion>4.0.0</modelVersion>`
4.   `<groupId>com.test</groupId>`
5.   `<artifactId>use</artifactId>`
6.   `<version>1.0.0</version>`
7.   `<packaging>jar</packaging>`

9.   `<dependencyManagement>`
10.   `<dependencies>`
11.   `<dependency>`
12.   `<groupId>com.test</groupId>`
13.   `<artifactId>bom</artifactId>`
14.   `<version>1.0.0</version>`
15.   `<type>pom</type>`
16.   `<scope>import</scope>`
17.   `</dependency>`
18.   `</dependencies>`
19.   `</dependencyManagement>`
20.   `<dependencies>`
21.   `<dependency>`
22.   `<groupId>com.test</groupId>`
23.   `<artifactId>project1</artifactId>`
24.   `</dependency>`
25.   `<dependency>`
26.   `<groupId>com.test</groupId>`
27.   `<artifactId>project2</artifactId>`
28.   `</dependency>`
29.   `</dependencies>`
30.   `</project>`

Finally, when creating projects that import dependencies, beware of the following:

*   Do not attempt to import a POM that is defined in a submodule of the current POM. Attempting to do that will result in the build failing since it won't be able to locate the POM.
*   Never declare the POM importing a POM as the parent (or grandparent, etc) of the target POM. There is no way to resolve the circularity and an exception will be thrown.
*   When referring to artifacts whose POMs have transitive dependencies, the project needs to specify versions of those artifacts as managed dependencies. Not doing so results in a build failure since the artifact may not have a version specified. (This should be considered a best practice in any case as it keeps the versions of artifacts from changing from one build to the next).

Starting from Maven 4.0, a new specific BOM packaging has been introduced. It allows defining a BOM which is not used as a parent in a project leveraging the newer 4.1.0 model, while still providing full compatibility with Maven 3.X clients and projects. This BOM packaging is translated into a more usual POM packaging at installation / deployment time, leveraging the build/consumer POM feature from Maven 4. This thus provides full compatibility with Maven 3.x.

2.   `<project xmlns="http://maven.apache.org/POM/4.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/POM/4.1.0 https://maven.apache.org/xsd/maven-4.1.0.xsd">`
4.   `<parent>`
5.   `<groupId>com.test</groupId>`
6.   `<version>1.0.0</version>`
7.   `<artifactId>parent</artifactId>`
8.   `</parent>`
9.   `<groupId>com.test</groupId>`
10.   `<artifactId>bom</artifactId>`
11.   `<version>1.0.0</version>`
12.   `<packaging>bom</packaging>`
13.   `<properties>`
14.   `<project1Version>1.0.0</project1Version>`
15.   `<project2Version>1.0.0</project2Version>`
16.   `</properties>`
17.   `<dependencyManagement>`
18.   `<dependencies>`
19.   `<dependency>`
20.   `<groupId>com.test</groupId>`
21.   `<artifactId>project1</artifactId>`
22.   `<version>${project1Version}</version>`
23.   `</dependency>`
24.   `<dependency>`
25.   `<groupId>com.test</groupId>`
26.   `<artifactId>project2</artifactId>`
27.   `<version>${project2Version}</version>`
28.   `</dependency>`
29.   `</dependencies>`
30.   `</dependencyManagement>`
31.   `</project>`

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
System Dependencies[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#system-dependencies)
---------------------------------------------------------------------------------------------------------------------------------

In rare occurrences it's necessary to use a dependency which is not available in any repository, but only on local machine; For example, a jar of some commercial application. To include such a dependency in the build, the _system_ scope can be used. Dependencies with the scope _system_ are not looked up in the Maven repository system. Instead, the `dependency` element contains a `systemPath` pointing to a jar on the local file system.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<dependencies>`
4.   `<dependency>`
5.   `<groupId>some.company</groupId>`
6.   `<artifactId>the-artifact</artifactId>`
7.   `<version>1.0.0</version>`
8.   `<scope>system</scope>`
9.   `<systemPath>path/to/lib/the.jar</systemPath>`
10.   `</dependency>`
11.   `</dependencies>`
12.   `...`
13.   `</project>`

While the _system_ scope is supported, its usage is **not recommended**! The dependency is only looked up on this specific file path, which binds the build to individual machines. The recommended approach is to upload the dependency to a [private hosted repository](https://maven.apache.org/repository-management.html) accessible within the organization. This also allows differentiation between dependencies needed for compile/execution and those only needed for testing, by using _compile_ or _test_ scope.

[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)
### Historical usage: Java EE (`javax`) libraries of the JDK[](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#historical-usage-java-ee-javax-libraries-of-the-jdk)

In the past, the system scope was commonly used to tell Maven about Java EE (`javax` package) dependencies provided by the JDK that were available as separate downloads earlier. A typical examples is the Java Authentication and Authorization Service (JAAS):

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<dependencies>`
4.   `<dependency>`
5.   `<groupId>javax.security</groupId>`
6.   `<artifactId>jaas</artifactId>`
7.   `<version>1.0.01</version>`
8.   `<scope>system</scope>`
9.   `<systemPath>${java.home}/lib/rt.jar</systemPath>`
10.   `</dependency>`
11.   `</dependencies>`
12.   `...`
13.   `</project>`

Most of those dependencies are available on Maven central nowadays. In general, you should never add any explicit dependencies for classes which are part of the JDK.
