# Source: https://maven.apache.org/guides/introduction/introduction-to-profiles.html

Title: Introduction to Build Profiles – Maven

URL Source: https://maven.apache.org/guides/introduction/introduction-to-profiles.html

Markdown Content:
[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
*   [What are the different types of profile? Where is each defined?](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#What_are_the_different_types_of_profile.3F_Where_is_each_defined.3F)
*   [Profile Inheritance](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Profile_Inheritance)
*   [How can a profile be triggered? How does this vary according to the type of profile being used?](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#How_can_a_profile_be_triggered.3F_How_does_this_vary_according_to_the_type_of_profile_being_used.3F)
    *   [Details on profile activation](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Details_on_profile_activation)
        *   [Explicit profile activation](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Explicit_profile_activation)
        *   [Implicit profile activation](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Implicit_profile_activation)
            *   [Active by default](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Active_by_default)
            *   [JDK](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#JDK)
            *   [OS](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#OS)
            *   [Properties](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Properties)
                *   [System or CLI user property](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#System_or_CLI_user_property)
                *   [Packaging property](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Packaging_property)

            *   [Files](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Files)

        *   [Multiple conditions](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Multiple_conditions)

    *   [Deactivating a profile](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Deactivating_a_profile)

*   [Which areas of a POM can be customized by each type of profile? Why?](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Which_areas_of_a_POM_can_be_customized_by_each_type_of_profile.3F_Why.3F)
    *   [Profiles in external files](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Profiles_in_external_files)
    *   [Profiles in POMs](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Profiles_in_POMs)
        *   [Examples](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Examples)

    *   [POM elements outside <profiles>](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#POM_elements_outside_.3Cprofiles.3E)

*   [Profile Order](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Profile_Order)
*   [Profile Pitfalls](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Profile_Pitfalls)
    *   [External Properties](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#External_Properties)
    *   [Incomplete Specification of a Natural Profile Set](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Incomplete_Specification_of_a_Natural_Profile_Set)

*   [How can I tell which profiles are in effect during a build?](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#How_can_I_tell_which_profiles_are_in_effect_during_a_build.3F)
*   [Naming Conventions](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#Naming_Conventions)

Apache Maven goes to great lengths to ensure that builds are portable. Among other things, this means allowing build configuration inside the POM, avoiding **all** filesystem references (in inheritance, dependencies, and other places), and leaning much more heavily on the local repository to store the metadata needed to make this possible.

However, sometimes portability is not entirely possible. Under certain conditions, plugins may need to be configured with local filesystem paths. Under other circumstances, a slightly different dependency set will be required, and the project's artifact name may need to be adjusted slightly. And at still other times, you may even need to include a whole plugin in the build lifecycle depending on the detected build environment.

To address these circumstances, Maven supports build profiles. Profiles are specified using a subset of the elements available in the POM itself (plus one extra section), and are triggered in any of a variety of ways. They modify the POM at build time, and are meant to be used in complementary sets to give equivalent-but-different parameters for a set of target environments (providing, for example, the path of the appserver root in the development, testing, and production environments). As such, profiles can easily lead to differing build results from different members of your team. However, used properly, profiles can be used while still preserving project portability. This will also minimize the use of `-f` option of maven which allows user to create another POM with different parameters or configuration to build which makes it more maintainable since it is running with one POM only.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
What are the different types of profile? Where is each defined?[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#what-are-the-different-types-of-profile-where-is-each-defined)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Per Project

- Defined in the POM itself `(pom.xml)`.

*   Per User

- Defined in the [Maven-settings](https://maven.apache.org/ref/current/maven-settings/settings.html)`(%USER_HOME%/.m2/settings.xml)`.

*   Global

- Defined in the [global Maven-settings](https://maven.apache.org/ref/current/maven-settings/settings.html)`(${maven.home}/conf/settings.xml)`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
Profile Inheritance[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#profile-inheritance)
---------------------------------------------------------------------------------------------------------------------

The profiles are not inherited by child POMs. Instead, they are resolved very early by the [Maven Model Builder](https://maven.apache.org/ref/current/maven-model-builder/) and only the effects of active profiles are inherited (e.g. the plugins defined in the profile). Implicit profile activation only has an effect on the surrounding profile container but never on any other profile (even if it has the same id).

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
How can a profile be triggered? How does this vary according to the type of profile being used?[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#how-can-a-profile-be-triggered-how-does-this-vary-according-to-t)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A profile can be activated in several ways:

*   Explicitly
*   Implicitly, based on 
    *   JDK version
    *   Operating system
    *   system or CLI user properties
    *   packaging properties
    *   presence of files

Refer to the sections below for details.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### Details on profile activation[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#details-on-profile-activation)

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
#### Explicit profile activation[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#explicit-profile-activation)

Profiles can be explicitly specified using the `-P` command line flag.

This flag is followed by a comma-delimited list of profile IDs to use. The profile(s) specified in the option are activated in addition to any profiles which are activated by their activation configuration or the `<activeProfiles>` section in `settings.xml`. From Maven 4 onward, Maven will refuse to activate or deactivate a profile that cannot be resolved. To prevent this, prefix the profile identifier with an `?`, marking it as optional:

```
mvn groupId:artifactId:goal -P profile-1,profile-2,?profile-3
```

Profiles can be activated in the Maven settings, via the `<activeProfiles>` section. This section takes a list of `<activeProfile>` elements, each containing a profile-id inside.

1.   `<settings>`
2.   `...`
3.   `<activeProfiles>`
4.   `<activeProfile>profile-1</activeProfile>`
5.   `</activeProfiles>`
6.   `...`
7.   `</settings>`

Profiles listed in the `<activeProfiles>` tag would be activated by default every time a project use it.

Profiles can also be active by default using a configuration like the following in a POM:

1.   `<profiles>`
2.   `<profile>`
3.   `<id>profile-1</id>`
4.   `<activation>`
5.   `<activeByDefault>true</activeByDefault>`
6.   `</activation>`
7.   `...`
8.   `</profile>`
9.   `</profiles>`

This profile will automatically be active for all builds unless another profile in the same POM is activated using one of the previously described methods. All profiles that are active by default are automatically deactivated when a profile in the POM is activated on the command line or through its activation config.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
#### Implicit profile activation[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#implicit-profile-activation)

Profiles can be automatically triggered based on the state of the build environment. These triggers are specified via an `<activation>` section in the profile. The implicit profile activation only refers to the container profile (and not to profiles in other modules with the same id). The activation occurs when all the specified criteria have been met.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
##### Active by default[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#active-by-default)

Boolean flag which determines if the profile is active by default. Is `false` by default. This flag is only evaluated if no other profile is explicitly activated via command line, `settings.xml` or activated through some other activator. Otherwise, it has no effect.

Example to set a profile active by default.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<activeByDefault>true</activeByDefault>`
5.   `</activation>`
6.   `...`
7.   `</profile>`
8.   `</profiles>`

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
##### JDK[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#jdk)

The following configuration will trigger the profile when the JDK's version _starts with_`1.4` (for example `1.4.0_08`, `1.4.2_07`, `1.4`), in particular it _won't be active_ for **newer** versions like `1.8` or `11`:

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<jdk>1.4</jdk>`
5.   `</activation>`
6.   `...`
7.   `</profile>`
8.   `</profiles>`

[Ranges](https://maven.apache.org/enforcer/enforcer-rules/versionRanges.html) can also be used. Range values must start with either `[` or `(`. The following honours versions `1.3`, `1.4`, and `1.5`.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<jdk>[1.3,1.6)</jdk>`
5.   `</activation>`
6.   `...`
7.   `</profile>`
8.   `</profiles>`

_Note:_ The value ranges match if the JDK version used for running Maven is between the lower and upper bounds (either inclusive or exclusive). An upper bound such as `,1.5]` likely does not include most releases of 1.5, since they will have an additional “patch” release such as `_05` that is not taken into consideration in the above range.

If the range does not start with `[` or `(`, the value is interpreted as a vendor prefix. A prefix is negated if the value starts with `!`. (Negated) prefix values match if the JDK version used for running Maven starts/doesn't start with the given prefix (excluding the potentially leading `!`). The following profile would be active, when any `zulu64` JDK is used.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<jdk>zulu64</jdk>`
5.   `</activation>`
6.   `...`
7.   `</profile>`
8.   `</profiles>`

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
##### OS[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#os)

This next one will activate based on the detected operating system. See the [Maven Enforcer Plugin](https://maven.apache.org/enforcer/enforcer-rules/requireOS.html) for more details about OS values.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<os>`
5.   `<name>Windows XP</name>`
6.   `<family>Windows</family>`
7.   `<arch>x86</arch>`
8.   `<version>5.1.2600</version>`
9.   `</os>`
10.   `</activation>`
11.   `...`
12.   `</profile>`
13.   `</profiles>`

The values are interpreted as Strings and are matched against the [Java System properties](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html)`os.name`, `os.arch`, `os.version` and the family being derived from those.

Each value can be prefixed with `!` to negate the matching. The values match if they are (not) equal to the actual String value (**case insensitive**). All given OS conditions must match for the profile to be considered for activation.

Since [Maven 3.9.7](https://issues.apache.org/jira/browse/MNG-5726) the value for `version` may be prefixed with `regex:`. In that case [regular pattern matching](https://docs.oracle.com/javase/tutorial/essential/regex/) is applied for the version matching and applied against the **lower case**`os.version` value.

The actual OS values which need to match the given values are emitted when executing `mvn --version`. See the maven-enforcer-plugin's [Require OS Rule](https://maven.apache.org/enforcer/enforcer-rules/requireOS.html) for more details about OS values.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
##### Properties[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#properties)

The `profile` will activate if Maven detects a system property or CLI user property (a value which can be dereferenced within the POM by `${name}`) of the corresponding `name=value` pair, and it matches the given value (if given). Since Maven 3.9.0 one can also evaluate the `<packaging value>` of the pom via property name `packaging`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
###### System or CLI user property[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#system-or-cli-user-property)

The `profile` will activate if Maven detects a system property or CLI user property (a value which can be dereferenced within the POM by `${name}`) of the corresponding `name=value` pair, and it matches the given value (if given).

The profile below will be activated when the system property `debug` is specified with any value:

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>debug</name>`
6.   `</property>`
7.   `</activation>`
8.   `...`
9.   `</profile>`
10.   `</profiles>`

The following profile will be activated when the system property `debug` is not defined at all:

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>!debug</name>`
6.   `</property>`
7.   `</activation>`
8.   `...`
9.   `</profile>`
10.   `</profiles>`

The following profile will be activated when the system property `debug` is defined with no value, or is defined with the value `true`.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>debug</name>`
6.   `<value>true</value>`
7.   `</property>`
8.   `</activation>`
9.   `...`
10.   `</profile>`
11.   `</profiles>`

To activate this you would type one of those on the command line:

```
mvn groupId:artifactId:goal -Ddebug
mvn groupId:artifactId:goal -Ddebug=true
```

The following profile will be activated when the system property `debug` is not defined, or is defined with a value which is not `true`.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>debug</name>`
6.   `<value>!true</value>`
7.   `</property>`
8.   `</activation>`
9.   `...`
10.   `</profile>`
11.   `</profiles>`

To activate this you would type one of those on the command line:

```
mvn groupId:artifactId:goal
mvn groupId:artifactId:goal -Ddebug=false
```

The next example will trigger the profile when the system property `environment` is specified with the value `test`:

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>environment</name>`
6.   `<value>test</value>`
7.   `</property>`
8.   `</activation>`
9.   `...`
10.   `</profile>`
11.   `</profiles>`

To activate this you would type this on the command line:

```
mvn groupId:artifactId:goal -Denvironment=test
```

Profiles in the POM can also be activated based on properties from active profiles from the `settings.xml`.

**Note**: Environment variables like `FOO` are available as properties of the form `env.FOO`. Further note that environment variable names are normalized to all upper-case on Windows.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
###### Packaging property[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#packaging-property)

Since Maven 3.9.0 one can also evaluate the POM's packaging value by referencing property `packaging`. This is only useful where the profile activation is defined in a common parent POM which is reused among multiple Maven projects. The next example will trigger the profile when a project with packaging `war` is built:

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<property>`
5.   `<name>packaging</name>`
6.   `<value>war</value>`
7.   `</property>`
8.   `</activation>`
9.   `...`
10.   `</profile>`
11.   `</profiles>`

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
##### Files[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#files)

A given filename may activate the `profile` by the `existence` of a file, or if it is `missing`. **NOTE**: Interpolation for this element is limited to `${project.basedir}`, System properties, and request properties.

This example will trigger the profile when the generated file `target/generated-sources/axistools/wsdl2java/org/apache/maven` is missing.

1.   `<profiles>`
2.   `<profile>`
3.   `<activation>`
4.   `<file>`
5.   `<missing>target/generated-sources/axistools/wsdl2java/org/apache/maven</missing>`
6.   `</file>`
7.   `</activation>`
8.   `...`
9.   `</profile>`
10.   `</profiles>`

The tags `<exists>` and `<missing>` can be interpolated. Supported variables are system properties like `${user.home}` and environment variables like `${env.HOME}`. Please note that properties and values defined in the POM itself are not available for interpolation here, e.g. the above example activator cannot use `${project.build.directory}` but needs to hard-code the path `target`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
#### Multiple conditions[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#multiple-conditions)

Different implicit activation types can be combined in one profile. The profile is then only active if all conditions are met. Using the same type more than once in the same profile is not supported ([MNG-5909](https://issues.apache.org/jira/browse/MNG-5909), [MNG-3328](https://issues.apache.org/jira/browse/MNG-3328)).

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### Deactivating a profile[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#deactivating-a-profile)

One or more profiles can be deactivated using the command line by prefixing their identifier with either the character ‘!’ or ‘-’ as shown below.

**Note** that `!` needs to be escaped with `\` or quoted in Bash, ZSH and other shells as it has [a special meaning](https://www.gnu.org/software/bash/manual/html_node/Event-Designators.html). Also there is a known bug with command line option values starting with `-` ([CLI-309](https://issues.apache.org/jira/browse/CLI-309)), therefore it is recommended to use it with the syntax `-P=-profilename`.

```
mvn groupId:artifactId:goal -P !profile-1,!profile-2,!?profile-3
```

or

```
mvn groupId:artifactId:goal -P=-profile-1,-profile-2,-?profile-3
```

This can be used to deactivate profiles marked as activeByDefault or profiles that would otherwise be activated through their activation config.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
Which areas of a POM can be customized by each type of profile? Why?[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#which-areas-of-a-pom-can-be-customized-by-each-type-of-profile-w)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that we've talked about where to specify profiles, and how to activate them, it will be useful to talk about _what_ you can specify in a profile. As with the other aspects of profile configuration, this answer is not straightforward.

Depending on where you choose to configure your profile, you will have access to varying POM configuration options.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### Profiles in external files[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#profiles-in-external-files)

Profiles specified in external files (i.e in `settings.xml` or `profiles.xml`) are not portable in the strictest sense. Anything that seems to stand a high chance of changing the result of the build is restricted to the inline profiles in the POM. Things like repository lists could simply be a proprietary repository of approved artifacts, and won't change the outcome of the build. Therefore, you will only be able to modify the `<repositories>` and `<pluginRepositories>` sections, plus an extra `<properties>` section.

The `<properties>` section allows you to specify free-form key-value pairs which will be included in the interpolation process for the POM. This allows you to specify a plugin configuration in the form of `${profile.provided.path}`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### Profiles in POMs[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#profiles-in-poms)

On the other hand, if your profiles can be reasonably specified _inside_ the POM, you have many more options. The trade-off, of course, is that you can only modify _that_ project and its sub-modules. Since these profiles are specified inline, and therefore have a better chance of preserving portability, it's reasonable to say you can add more information to them without the risk of that information being unavailable to other users.

Profiles specified in the POM can modify [the following POM elements](https://maven.apache.org/ref/current/maven-model/maven.html):

*   `<repositories>`
*   `<pluginRepositories>`
*   `<dependencies>`
*   `<plugins>`
*   `<properties>`
*   `<modules>`
*   `<reports>`
*   `<reporting>`
*   `<dependencyManagement>`
*   `<distributionManagement>`
*   the following subset of the `<build>` element: 
    *   `<defaultGoal>`
    *   `<resources>`
    *   `<testResources>`
    *   `<directory>`
    *   `<finalName>`
    *   `<filters>`
    *   `<pluginManagement>`
    *   `<plugins>`

_Note_: A profile which tries to modify other elements of the `<build>` element is invalid and will fail the build with a “malformed POM” error.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
#### Examples[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#examples)

The following example defines a profile to execute the [Maven Invoker Plugin](https://maven.apache.org/plugins/maven-invoker-plugin/):

1.   `<profile>`
2.   `<id>run-its</id>`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-invoker-plugin</artifactId>`
8.   `<configuration>`
9.   `<goals>`
10.   `<goal>clean</goal>`
11.   `<goal>package</goal>`
12.   `</goals>`
13.   `</configuration>`
14.   `<executions>`
15.   `<execution>`
16.   `<id>integration-test</id>`
17.   `<goals>`
18.   `<goal>install</goal>`
19.   `<goal>integration-test</goal>`
20.   `</goals>`
21.   `</execution>`
22.   `</executions>`
23.   `</plugin>`
24.   `</plugins>`
25.   `</build>`
26.   `</profile>`

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### POM elements outside <profiles>[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#pom-elements-outside-profiles)

We don't allow modification of some POM elements outside of POM-profiles because these runtime modifications will not be distributed when the POM is deployed to the repository system, making that person's build of that project completely unique from others. While you can do this to some extent with the options given for external profiles, the danger is limited. Another reason is that this POM info is sometimes being reused from the parent POM.

External files such as `settings.xml` and `profiles.xml` also do not support elements outside the POM-profiles. Let us take this scenario for elaboration. When the effective POM is deployed to a remote repository, any person can pickup its info out of the repository and use it to build a Maven project directly. Now, imagine that if we can set profiles in dependencies, which is very important to a build, or in any other elements outside POM-profiles in `settings.xml` then most probably we cannot expect someone else to use that POM from the repository and be able to build it. And we have to also think about how to share the `settings.xml` with others. Note that too many files to configure are very confusing and very hard to maintain. Bottom line is that since this is build data, it should be in the POM.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
Profile Order[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#profile-order)
---------------------------------------------------------------------------------------------------------

All profile elements in a POM from active profiles overwrite the global elements with the same name of the POM or extend those in case of collections. In case multiple profiles are active in the same POM or external file, the ones which are defined **later** take precedence over the ones defined **earlier** (independent of their profile id and activation order).

Example:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<repositories>`
4.   `<repository>`
5.   `<id>global-repo</id>`
6.   `...`
7.   `</repository>`
8.   `</repositories>`
9.   `...`
10.   `<profiles>`
11.   `<profile>`
12.   `<id>profile-1</id>`
13.   `<activation>`
14.   `<activeByDefault>true</activeByDefault>`
15.   `</activation>`
16.   `<repositories>`
17.   `<repository>`
18.   `<id>profile-1-repo</id>`
19.   `...`
20.   `</repository>`
21.   `</repositories>`
22.   `</profile>`
23.   `<profile>`
24.   `<id>profile-2</id>`
25.   `<activation>`
26.   `<activeByDefault>true</activeByDefault>`
27.   `</activation>`
28.   `<repositories>`
29.   `<repository>`
30.   `<id>profile-2-repo</id>`
31.   `...`
32.   `</repository>`
33.   `</repositories>`
34.   `</profile>`
35.   `...`
36.   `</profiles>`
37.   `...`
38.   `</project>`

This leads to the repository list: `profile-2-repo, profile-1-repo, global-repo`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
Profile Pitfalls[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#profile-pitfalls)
---------------------------------------------------------------------------------------------------------------

We've already mentioned the fact that adding profiles to your build has the potential to break portability for your project. We've even gone so far as to highlight circumstances where profiles are likely to break project portability. However, it's worth reiterating those points as part of a more coherent discussion about some pitfalls to avoid when using profiles.

There are two main problem areas to keep in mind when using profiles. First are external properties, usually used in plugin configurations. These pose the risk of breaking portability in your project. The other, more subtle area is the incomplete specification of a natural set of profiles.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### External Properties[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#external-properties)

External property definition concerns any property value defined outside the `pom.xml` but not defined in a corresponding profile inside it. The most obvious usage of properties in the POM is in plugin configuration. While it is certainly possible to break project portability without properties, these critters can have subtle effects that cause builds to fail. For example, specifying appserver paths in a profile that is specified in the `settings.xml` may cause your integration test plugin to fail when another user on the team attempts to build without a similar `settings.xml`. Consider the following `pom.xml` snippet for a web application project:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.myco.plugins</groupId>`
7.   `<artifactId>spiffy-integrationTest-plugin</artifactId>`
8.   `<version>1.0</version>`
9.   `<configuration>`
10.   `<appserverHome>${appserver.home}</appserverHome>`
11.   `</configuration>`
12.   `</plugin>`
13.   `...`
14.   `</plugins>`
15.   `</build>`
16.   `...`
17.   `</project>`

Now, in your local `${user.home}/.m2/settings.xml`, you have:

1.   `<settings>`
2.   `...`
3.   `<profiles>`
4.   `<profile>`
5.   `<id>appserverConfig</id>`
6.   `<properties>`
7.   `<appserver.home>/path/to/appserver</appserver.home>`
8.   `</properties>`
9.   `</profile>`
10.   `</profiles>`

12.   `<activeProfiles>`
13.   `<activeProfile>appserverConfig</activeProfile>`
14.   `</activeProfiles>`
15.   `...`
16.   `</settings>`

When you build the **integration-test** lifecycle phase, your integration tests pass, since the path you've provided allows the test plugin to install and test this web application.

_However_, when your colleague attempts to build to **integration-test**, his build fails spectacularly, complaining that it cannot resolve the plugin configuration parameter `<appserverHome>`, or worse, that the value of that parameter - literally `${appserver.home}` - is invalid (if it warns you at all).

Congratulations, your project is now non-portable. Inlining this profile in your `pom.xml` can help alleviate this, with the obvious drawback that each project hierarchy (allowing for the effects of inheritance) now have to specify this information. Since Maven provides good support for project inheritance, it's possible to stick this sort of configuration in the `<pluginManagement>` section of a team-level POM or similar, and simply inherit the paths.

Another, less attractive answer might be standardization of development environments. However, this will tend to compromise the productivity gain that Maven is capable of providing.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
### Incomplete Specification of a Natural Profile Set[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#incomplete-specification-of-a-natural-profile-set)

In addition to the above portability-breaker, it's easy to fail to cover all cases with your profiles. When you do this, you're usually leaving one of your target environments high and dry. Let's take the example `pom.xml` snippet from above one more time:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.myco.plugins</groupId>`
7.   `<artifactId>spiffy-integrationTest-plugin</artifactId>`
8.   `<version>1.0</version>`
9.   `<configuration>`
10.   `<appserverHome>${appserver.home}</appserverHome>`
11.   `</configuration>`
12.   `</plugin>`
13.   `...`
14.   `</plugins>`
15.   `</build>`
16.   `...`
17.   `</project>`

Now, consider the following profile, which would be specified inline in the `pom.xml`:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<profiles>`
4.   `<profile>`
5.   `<id>appserverConfig-dev</id>`
6.   `<activation>`
7.   `<property>`
8.   `<name>env</name>`
9.   `<value>dev</value>`
10.   `</property>`
11.   `</activation>`
12.   `<properties>`
13.   `<appserver.home>/path/to/dev/appserver</appserver.home>`
14.   `</properties>`
15.   `</profile>`

17.   `<profile>`
18.   `<id>appserverConfig-dev-2</id>`
19.   `<activation>`
20.   `<property>`
21.   `<name>env</name>`
22.   `<value>dev-2</value>`
23.   `</property>`
24.   `</activation>`
25.   `<properties>`
26.   `<appserver.home>/path/to/another/dev/appserver2</appserver.home>`
27.   `</properties>`
28.   `</profile>`
29.   `</profiles>`
30.   `..`
31.   `</project>`

This profile looks quite similar to the one from the last example, with a few important exceptions: it's plainly geared toward a development environment, a new profile named `appserverConfig-dev-2` is added and it has an activation section that will trigger its inclusion when the system properties contain “env=dev” for a profile named `appserverConfig-dev` and “env=dev-2” for a profile named `appserverConfig-dev-2`. So, executing:

```
mvn -Denv=dev-2 integration-test
```

will result in a successful build, applying the properties given by profile named `appserverConfig-dev-2`. And when we execute

```
mvn -Denv=dev integration-test
```

it will result in a successful build applying the properties given by the profile named `appserverConfig-dev`. However, executing:

```
mvn -Denv=production integration-test
```

will not do a successful build. Why? Because, the resulting non-interpolated literal value of `${appserver.home}` will not be a valid path for deploying and testing your web application. We haven't considered the case for the production environment when writing our profiles. The “production” environment (env=production), along with “test” and possibly even “local” constitute a natural set of target environments for which we may want to build the integration-test lifecycle phase. The incomplete specification of this natural set means we have effectively limited our valid target environments to the development environment. Your teammates - and probably your manager - will not see the humor in this. When you construct profiles to handle cases such as these, be sure to address the entire set of target permutations.

As a quick aside, it's possible for user-specific profiles to act in a similar way. This means that profiles for handling different environments which are keyed to the user can act up when the team adds a new developer. While I suppose this _could_ act as useful training for the newbie, it just wouldn't be nice to throw them to the wolves in this way. Again, be sure to think of the _whole_ set of profiles.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
How can I tell which profiles are in effect during a build?[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#how-can-i-tell-which-profiles-are-in-effect-during-a-build)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Determining active profiles will help the user to know what particular profiles has been executed during a build. We can use the [Maven Help Plugin](https://maven.apache.org/plugins/maven-help-plugin/) to tell what profiles are in effect during a build.

```
mvn help:active-profiles
```

Let us have some small samples that will help us to understand more on the _active-profiles_ goal of that plugin.

From the last example of profiles in the `pom.xml`, you'll notice that there are two profiles named `appserverConfig-dev` and `appserverConfig-dev-2` which has been given different values for properties. If we go ahead and execute:

```
mvn help:active-profiles -Denv=dev
```

The result will be a bulleted list of the id of the profile with an activation property of “env=dev” together with the source where it was declared. See sample below.

```
The following profiles are active:

 - appserverConfig-dev (source: pom)
```

Now if we have a profile declared in `settings.xml` (refer to the sample of profile in `settings.xml`) and that have been set to be an active profile and execute:

```
mvn help:active-profiles
```

The result should be something like this

```
The following profiles are active:

 - appserverConfig (source: settings.xml)
```

Even though we don't have an activation property, a profile has been listed as active. Why? Like we mentioned before, a profile that has been set as an active profile in the `settings.xml` is automatically activated.

Now if we have something like a profile in the `settings.xml` that has been set as an active profile and also triggered a profile in the POM. Which profile do you think will have an effect on the build?

```
mvn help:active-profiles -P appserverConfig-dev
```

This will list the activated profiles:

```
The following profiles are active:

 - appserverConfig-dev (source: pom)
 - appserverConfig (source: settings.xml)
```

Even though it listed the two active profiles, we are not sure which one of them has been applied. To see the effect on the build execute:

```
mvn help:effective-pom -P appserverConfig-dev
```

This will print the effective POM for this build configuration out to the console. Take note that profiles in the `settings.xml` takes higher priority than profiles in the POM. So the profile that has been applied here is `appserverConfig` not `appserverConfig-dev`.

If you want to redirect the output from the plugin to a file called `effective-pom.xml`, use the command-line option `-Doutput=effective-pom.xml`.

[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
Naming Conventions[](https://maven.apache.org/guides/introduction/introduction-to-profiles.html#naming-conventions)
-------------------------------------------------------------------------------------------------------------------

By now you've noticed that profiles are a natural way of addressing the problem of different build configuration requirements for different target environments. Above, we discussed the concept of a “natural set” of profiles to address this situation, and the importance of considering the whole set of profiles that will be required.

However, the question of how to organize and manage the evolution of that set is non-trivial as well. Just as a good developer strives to write self-documenting code, it's important that your profile id's give a hint to their intended use. One good way to do this is to use the common system property trigger as part of the name for the profile. This might result in names like **env-dev**, **env-test**, and **env-prod** for profiles that are triggered by the system property **env**. Such a system leaves a highly intuitive hint on how to activate a build targeted at a particular environment. Thus, to activate a build for the test environment, you need to activate **env-test** by issuing:

```
mvn -Denv=test <phase>
```

The right command-line option can be had by simply substituting “=” for “-” in the profile id.
