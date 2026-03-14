# Source: https://assertj.github.io/doc/

Title: AssertJ - fluent assertions java library

URL Source: https://assertj.github.io/doc/

Markdown Content:
AssertJ - fluent assertions java library
Version 1.0
Table of Contents
1. AssertJ Overview
2. AssertJ Core
2.1. What is AssertJ Core?
2.2. Getting Help
2.3. Contributing to this guide
2.4. Quick start
2.4.1. Supported Java Versions
Kotlin Support
Android Support
2.4.2. Get AssertJ Core
Maven
Gradle
Other build tools
Spring Boot
2.4.3. Use Assertions class entry point
Alternative entry points
IDE configuration
2.4.4. Use code completion
2.4.5. Javadoc
2.5. Core assertions guide
2.5.1. A simple example
2.5.2. Supported type assertions
Common types
Primitive types
Java 8 Temporal types
Atomic types
2.5.3. Assertion description
Printing or consuming description
2.5.4. Overriding error message
Lazy error message overriding
2.5.5. Avoiding incorrect usage
Forgetting to call an assertion
Calling as() after the assertion
Calling withFailMessage/overridingErrorMessage after the assertion
Setting a comparator after the assertion
2.5.6. Configuring AssertJ
Configuring single properties
AssertJ Configuration
Automagic configuration discovery
2.5.7. Controlling type formatting
Creating a custom Representation
Changing the default global scope custom representation
Per assertion scope custom representation
Registering multiple fine-grained representations
2.5.8. Common assertions
2.5.9. Object assertions
2.5.10. String/CharSequence assertions
2.5.11. Iterable and array assertions
Reference
Checking iterables/arrays content
Verify assertions on some elements
Navigating to a given element
Filtering elements
Extracting elements values
Comparing elements with a specific comparator
2.5.12. Exception assertions
Reference
Checking exception message
Checking the cause and root cause
BDD style
assertThatThrownBy
assertThatExceptionOfType
Testing that no exception is thrown
With Java 7 (AssertJ 2.x)
2.5.13. Field by field recursive comparison
Basic usage
How field values are resolved
Breaking changes
isNotEqualTo
Strict or lenient comparison
Ignoring fields in the comparison
Using overridden equals
Ignoring all expected null fields
Ignoring all actual empty optional fields
Specifying how to compare specific types or fields in the comparison
Overriding error messages for specific fields or types
Recursive comparison for iterable assertions
Specifying how to introspect the objects to compare
2.5.14. Recursive assertions
2.5.15. Soft assertions
BDD Soft assertions
JUnit 4 Soft assertions rule
JUnit 5 soft assertions extension
Auto Closeable Soft assertions
Soft assertions with assertSoftly
Combining soft assertions entry points
Reacting to collected soft assertions
2.5.16. Assumptions
2.5.17. Javadoc
2.6. Extending assertions
2.6.1. Conditions
Creating a Condition
Using Conditions
Combining Conditions
2.6.2. Custom Assertions
Creating your own assertion class
Using our custom assertion class
Providing an entry point for all custom assertions
2.7. Migrating assertions
2.7.1. Migration Scripts
Usage
Script output
2.7.2. OpenRewrite
2.7.3. Migration Regexes
Converting assertEquals(0, myList.size()) to assertThat(myList).isEmpty()
Converting assertEquals(size, myList.size()) to assertThat(myList).hasSize(size)
Converting assertEquals(expected, actual) to assertThat(actual).isEqualTo(expected)
Converting assertNull(objectUnderTest) to assertThat(objectUnderTest).isNull()
Converting assertNotNull(objectUnderTest) to assertThat(objectUnderTest).isNotNull()
Converting assertFalse(logicalCondition) to assertThat(logicalCondition).isFalse()
2.8. AssertJ Sample Projects
2.9. Release Notes
2.9.1. AssertJ Core 3.23.0
2.9.2. AssertJ Core 3.22.0
2.9.3. AssertJ Core 3.21.0
2.9.4. AssertJ Core 3.20.2
2.9.5. AssertJ Core 3.20.1
2.9.6. AssertJ Core 3.20.0
2.9.7. AssertJ Core 3.19.0
2.9.8. AssertJ Core 3.18.1
2.9.9. AssertJ Core 3.18.0
2.9.10. AssertJ Core 3.17.2
2.9.11. AssertJ Core 3.17.1
2.9.12. AssertJ Core 3.17.0
2.9.13. AssertJ Core 3.16.1
2.9.14. AssertJ Core 3.16.0
2.9.15. AssertJ Core 3.15.0
2.9.16. AssertJ Core 3.14.0
2.9.17. AssertJ Core 3.13.2
2.9.18. AssertJ Core 3.13.1
2.9.19. AssertJ Core 3.13.0
2.9.20. AssertJ Core 3.12.2
2.9.21. AssertJ Core 3.12.1
2.9.22. AssertJ Core 3.12.0
Contributors
Breaking changes
New features
Improvements
Fixed
3. AssertJ Guava
3.1. Quick start
3.1.1. Supported Java versions
3.1.2. Get AssertJ Guava
Maven
Gradle
Other build tools
3.1.3. Use Assertions class entry point
3.1.4. Examples
3.1.5. IDE configuration
3.2. Assertions Guide
3.2.1. ByteSource
3.2.2. Multimap
3.2.3. Multiset
3.2.4. Optional
3.2.5. Range
3.2.6. RangeMap
3.2.7. RangeSet
3.2.8. Table
3.3. Javadoc
3.4. Release Notes
3.4.1. AssertJ Guava 3.5.0
3.4.2. AssertJ Guava 3.4.0
3.4.3. AssertJ Guava 3.3.0
4. AssertJ Joda
4.1. Quick start
4.1.1. Get assertj-joda-time library
Supported Java versions
Maven
Gradle
Other build tools
4.1.2. Use Assertions class entry point
4.1.3. Examples
4.1.4. IDE configuration
4.2. Assertions Guide
4.2.1. LocalDate
4.2.2. LocalDateTime
4.2.3. DateTime
4.3. Javadoc
4.4. Release Notes
4.4.1. AssertJ Joda Time 2.2.0
4.4.2. AssertJ Joda Time 2.1.0
4.4.3. AssertJ Joda Time 2.0.0
5. AssertJ Neo4j
6. AssertJ DB
6.1. Quick start
6.1.1. Add the assertj-db dependency to your project
Maven
Gradle
Other dependency management tool
6.1.2. Statically import org.assertj.db.api.Assertions.assertThat
6.2. Concepts
6.2.1. Connection to the database
AssertDbConnection
LetterCase setup
Schema retrieval mode
6.2.2. Elements of the database
Table
Request
Changes
Change
Row
Column
Value
6.2.3. Type
Data Type
Change Type
Value Type
Order Type
6.2.4. Navigation
With a Table or a Request as root
With Changes as root
6.2.5. DateValue, TimeValue and DateTimeValue
6.2.6. Default description
6.2.7. Letter Case of the database
CaseConversion
CaseComparison
LetterCase
6.2.8. Output
Type of output
Destination
6.3. Features highlight
6.3.1. Navigation
With a Table or a Request as root
With Changes as root
6.3.2. Assertions
On the type of change
On the equality with the values of a column
On the name of a column
On the nullity of the values of a column
On the nullity of the values of a row
On the type of column
On the class of column
On the content of column
On the type of data
On the modified columns in a change
On the number of changes
On the number of columns
On the number of rows
On the primary keys
On the equality with the values of a row
On the existence of a row in a change
On the chronology of a value
On the comparison with a value
On the closeness of a value
On the equality with a value
On the non equality with a value
On the nullity of a value
On the type of a value
On the class of a value
6.4. Javadoc
6.5. Examples
6.6. Mailing list
6.7. Code and issue tracker
6.8. Contributing
6.9. Release Notes
6.9.1. AssertJ DB 3.0.0
6.9.2. AssertJ DB 2.0.2
6.9.3. AssertJ DB 2.0.1
6.9.4. AssertJ DB 2.0.0
6.9.5. AssertJ DB 1.3.0
6.9.6. AssertJ DB 1.2.0
6.9.7. AssertJ DB 1.1.1
6.9.8. AssertJ DB 1.1.0
6.9.9. AssertJ DB 1.0.1
6.9.10. AssertJ DB 1.0.0
7. AssertJ Swing
7.1. Release Notes
7.1.1. AssertJ Swing 3.17.0
8. Appendix
8.1. Dependency Metadata
8.1.1. AssertJ Core
8.1.2. AssertJ Guava
8.1.3. Bill of Materials (BOM)
1. AssertJ Overview

AssertJ is composed of several modules:

A core module to provide assertions for JDK types (String, Iterable, Stream, Path, File, Map, …​)

A Guava module to provide assertions for Guava types (Multimap, Optional, …​)

A Joda Time module to provide assertions for Joda Time types (DateTime, LocalDateTime)

A Neo4J module to provide assertions for Neo4J types (Path, Node, Relationship, …​)

A DB module to provide assertions for relational database types (Table, Row, Column, …​)

A Swing module provides a simple and intuitive API for functional testing of Swing user interfaces

2. AssertJ Core

The goal of this document is to provide comprehensive reference documentation for programmers writing tests assertions with AssertJ.

2.1. What is AssertJ Core?

AssertJ is a Java library that provides a rich set of assertions and truly helpful error messages, improves test code readability, and is designed to be super easy to use within your favorite IDE.

https://www.javadoc.io/doc/org.assertj/assertj-core/3.27.7 is the latest version of AssertJ Core Javadoc, each assertion is explained, most of them with code examples so be sure to check it if you want to know what a specific assertion does.

Here are a few examples of AssertJ assertions:

// entry point for all assertThat methods and utility methods (e.g. entry)
import static org.assertj.core.api.Assertions.*;

// basic assertions
assertThat(frodo.getName()).isEqualTo("Frodo");
assertThat(frodo).isNotEqualTo(sauron);

// chaining string specific assertions
assertThat(frodo.getName()).startsWith("Fro")
                           .endsWith("do")
                           .isEqualToIgnoringCase("frodo");

// collection specific assertions (there are plenty more)
// in the examples below fellowshipOfTheRing is a List<TolkienCharacter>
assertThat(fellowshipOfTheRing).hasSize(9)
                               .contains(frodo, sam)
                               .doesNotContain(sauron);

// as() is used to describe the test and will be shown before the error message
assertThat(frodo.getAge()).as("check %s's age", frodo.getName()).isEqualTo(33);

// exception assertion, standard style ...
assertThatThrownBy(() -> { throw new Exception("boom!"); }).hasMessage("boom!");
// ... or BDD style
Throwable thrown = catchThrowable(() -> { throw new Exception("boom!"); });
assertThat(thrown).hasMessageContaining("boom");

// using the 'extracting' feature to check fellowshipOfTheRing character's names
assertThat(fellowshipOfTheRing).extracting(TolkienCharacter::getName)
                               .doesNotContain("Sauron", "Elrond");

// extracting multiple values at once grouped in tuples
assertThat(fellowshipOfTheRing).extracting("name", "age", "race.name")
                               .contains(tuple("Boromir", 37, "Man"),
                                         tuple("Sam", 38, "Hobbit"),
                                         tuple("Legolas", 1000, "Elf"));

// filtering a collection before asserting
assertThat(fellowshipOfTheRing).filteredOn(character -> character.getName().contains("o"))
                               .containsOnly(aragorn, frodo, legolas, boromir);

// combining filtering and extraction (yes we can)
assertThat(fellowshipOfTheRing).filteredOn(character -> character.getName().contains("o"))
                               .containsOnly(aragorn, frodo, legolas, boromir)
                               .extracting(character -> character.getRace().getName())
                               .contains("Hobbit", "Elf", "Man");

// and many more assertions: iterable, stream, array, map, dates, path, file, numbers, predicate, optional ...
2.2. Getting Help

Ask AssertJ related questions on Stack Overflow.

2.3. Contributing to this guide

You are very welcome to suggest or contribute improvements to this guide, that’s one great way to give back to open source projects!

The repository containing the guide is https://github.com/assertj/doc, you can create a new issue, submit a pull request. Et voila!

This guide is written with the awesome Asciidoctor which makes it easy to improve.

2.4. Quick start

This guide is for the AssertJ Core module.

2.4.1. Supported Java Versions

AssertJ Core requires Java 8 or higher.

Kotlin Support

AssertJ Core is compatible with Kotlin 1.9 or higher.

Android Support

AssertJ Core does not officially support Android but is compatible with Android API Level 26+, except for soft assertions and assumptions.

2.4.2. Get AssertJ Core

The AssertJ Core artifact can be included directly using its dependency metadata or indirectly via the Bill of Materials POM.

Maven
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-core</artifactId>
  <version>3.27.7</version>
  <scope>test</scope>
</dependency>
Gradle
testImplementation("org.assertj:assertj-core:3.27.7")
Other build tools

Check this page to find the relevant Assertj Core dependency declaration.

Spring Boot

Spring Boot provides automatic support for managing the version of AssertJ used in your project. In addition, the spring-boot-starter-test artifact automatically includes testing libraries such as JUnit Jupiter, AssertJ Core, Mockito, etc.

If you need to override the version of a dependency used in your Spring Boot application, you have to override the exact name of the version property defined in the BOM used by the Spring Boot plugin. For example, the name of the AssertJ version property in Spring Boot is assertj.version. The mechanism for changing a dependency version is documented for both Maven and Gradle.

With Maven, you can override the AssertJ version by including the following in your pom.xml file.

<properties>
  <assertj.version>3.27.7</assertj.version>
</properties>

With Gradle, you can override the AssertJ version by including the following in your build.gradle file.

ext['assertj.version'] = '3.27.7'
2.4.3. Use Assertions class entry point

The Assertions class is the only class you need to start using AssertJ, it provides all the methods you need.

Alternatively your test class can implement WithAssertions to access the same methods.

One Assertions static import to rule them all …​

import static org.assertj.core.api.Assertions.*;

... or many if you prefer:

import static org.assertj.core.api.Assertions.assertThat;  // main one
import static org.assertj.core.api.Assertions.atIndex; // for List assertions
import static org.assertj.core.api.Assertions.entry;  // for Map assertions
import static org.assertj.core.api.Assertions.tuple; // when extracting several properties at once
import static org.assertj.core.api.Assertions.fail; // use when writing exception tests
import static org.assertj.core.api.Assertions.failBecauseExceptionWasNotThrown; // idem
import static org.assertj.core.api.Assertions.filter; // for Iterable/Array assertions
import static org.assertj.core.api.Assertions.offset; // for floating number assertions
import static org.assertj.core.api.Assertions.anyOf; // use with Condition
import static org.assertj.core.api.Assertions.contentOf; // use with File assertions
Alternative entry points

AssertJ provides other entry points class, notably the WithAssertions interface and BDDAssertions for BDD style assertions that replace assertThat by then.

WithAssertions example:

import org.assertj.core.api.WithAssertions;

public class WithAssertionsExamples extends AbstractAssertionsExamples implements WithAssertions {

  // the data used are initialized in AbstractAssertionsExamples.

  @Test
  public void withAssertions_examples() {

    // assertThat methods come from WithAssertions - no static import needed
    assertThat(frodo.age).isEqualTo(33);
    assertThat(frodo.getName()).isEqualTo("Frodo").isNotEqualTo("Frodon");

    assertThat(frodo).isIn(fellowshipOfTheRing);
    assertThat(frodo).isIn(sam, frodo, pippin);
    assertThat(sauron).isNotIn(fellowshipOfTheRing);

    assertThat(frodo).matches(p -> p.age > 30 && p.getRace() == HOBBIT);
    assertThat(frodo.age).matches(p -> p > 30);
  }
}

BDDAssertions example:

import static org.assertj.core.api.BDDAssertions.then;

public class BDDAssertionsExamples extends AbstractAssertionsExamples {

  // the data used are initialized in AbstractAssertionsExamples.

  @Test
  public void withAssertions_examples() {

    // then methods come from BDDAssertions.then static
    then(frodo.age).isEqualTo(33);
    then(frodo.getName()).isEqualTo("Frodo").isNotEqualTo("Frodon");

    then(frodo).isIn(fellowshipOfTheRing);
    then(frodo).isIn(sam, frodo, pippin);
    then(sauron).isNotIn(fellowshipOfTheRing);

    then(frodo).matches(p -> p.age > 30 && p.getRace() == HOBBIT);
    then(frodo.age).matches(p -> p > 30);
  }
}
IDE configuration

You can configure your IDE so that when you start typing as and trigger code completion assertThat will show up in the suggested completions.

Eclipse:

Go to Window > Preferences > Java > Editor > Content Assist > Favorites > New Type.

Enter org.assertj.core.api.Assertions and click OK.

Check that you see org.assertj.core.api.Assertions.* in Favorites.

Intellij Idea: No special configuration is needed, just start typing asser and then invoke completion (Ctrl-Space) twice.

2.4.4. Use code completion

Type assertThat followed by the object under test and a dot …​ and any Java IDE code completion will show you all available assertions.

assertThat(objectUnderTest). 
	Use IDE code completion after the dot.

Example for String assertions:

2.4.5. Javadoc

https://www.javadoc.io/doc/org.assertj/assertj-core/3.27.7 is the latest version of AssertJ Core Javadoc, each assertion is explained, most of them with code examples so be sure to check it if you want to know what a specific assertion does.

2.5. Core assertions guide

This section describes the assertions provided by AssertJ Core and other useful features to get the best of it.

AssertJ Core Javadoc explains each assertion, most of them with code examples so be sure to check it if you want to know what a specific assertion does.

2.5.1. A simple example

Let’s start with a simple example showing a few important things.

import static org.assertj.core.api.Assertions.assertThat; 

import org.junit.jupiter.api.Test;

public class SimpleAssertionsExample {

  @Test
  void a_few_simple_assertions() {
    assertThat("The Lord of the Rings").isNotNull()   
                                       .startsWith("The") 
                                       .contains("Lord") 
                                       .endsWith("Rings"); 
  }

}
	Statically import org.assertj.core.api.Assertions.assertThat
	Pass the object under test as the sole assertThat() parameter
	Use code completion to discover and call assertions
	Chain as many assertions as you need

Except for isNotNull which is a base assertion, the other assertions are String specific as our object under test is a String.

2.5.2. Supported type assertions

AssertJ provides assertions specific to the object under test type, the following sections list the supported types grouped by categories.

The provided assertions for each of these types are documented later on.

Common types

BigDecimal

	

BigInteger




CharSequence

	

Class




Date

	

File




Future / CompletableFuture

	

InputStream




Iterable (including any kind of Collection)

	

Iterator




List

	

Map




Object

	

Object[] and Object[][]




Optional

OptionalInt / OptionalLong / OptionalDouble

	

Path




Predicate

	

Stream




String

	

Throwable / Exception

Primitive types

Primitive types and their wrapper:

short / Short

int / Integer

long / Long

byte / Byte

char / Character

float / Float

double / Double

	

Primitive type arrays:

short[]

int[]

long[]

byte[]

char[]

float[]

double[]

	

Primitive type 2D arrays:

short[][]

int[][]

long[][]

byte[][]

char[][]

float[][]

double[][]

Java 8 Temporal types

Instant

	

LocalDate




LocalDateTime

	

LocalTime




OffsetDateTime

	

OffsetTime




ZonedDateTime

	

Period

Atomic types

Atomic basic types:

AtomicInteger

AtomicLong

AtomicBoolean

	

Atomic array types:

AtomicIntegerArray

AtomicLongArray




Atomic reference types:

AtomicMarkableReference

AtomicStampedReferenceAssert

	

Atomic updater types:

AtomicIntegerFieldUpdater

AtomicLongFieldUpdater

AtomicReferenceFieldUpdater




Adder types:

LongAdder

	
2.5.3. Assertion description

It is often valuable to describe the assertion performed, especially for boolean assertions where the default error message just complains that it got false instead of true (or vice versa).

You can set such a description with as(String description, Object…​ args) but remember to do it before calling the assertion otherwise it is simply ignored as a failing assertion breaks the chained calls.

Example of a failing assertion with a description:

TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, Race.HOBBIT);

// failing assertion, remember to call as() before the assertion!
assertThat(frodo.getAge()).as("check %s's age", frodo.getName())
                          .isEqualTo(100);

The error message starts with the given description in [] :

[check Frodo's age] expected:<100> but was:<33>
Printing or consuming description

AssertJ can print each assertion description (when it is set), to do so call Assertions.setPrintAssertionsDescription(true);.

If printing assertion descriptions is not what you need, you can alternatively register a Consumer<Description> that will be called each time a description is set.

Both options are exposed in AssertJ Configuration class.

Example: using a description consumer

// initialize the description consumer
final StringBuilder descriptionReportBuilder = new StringBuilder(String.format("Assertions:%n"));
Consumer<Description> descriptionConsumer = desc -> descriptionReportBuilder.append(String.format("-- %s%n", desc));

// use the description consumer for any following assertions descriptions.
Assertions.setDescriptionConsumer(descriptionConsumer);

// execute some assertions
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, Race.HOBBIT);
assertThat(frodo.getName()).as("check name")
                          .isEqualTo("Frodo");
assertThat(frodo.getAge()).as("check age")
                          .isEqualTo(33);

// get the report
String descriptionReport = descriptionReportBuilder.toString();

resulting descriptionReport:

Assertions:
-- check name
-- check age
2.5.4. Overriding error message

AssertJ tries its best to give helpful error messages, but you can always change it with overridingErrorMessage() or withFailMessage().

Example with this failing test:

TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, Race.HOBBIT);
TolkienCharacter sam = new TolkienCharacter("Sam", 38, Race.HOBBIT);
// failing assertion, remember to call withFailMessage/overridingErrorMessage before the assertion!
assertThat(frodo.getAge()).withFailMessage("should be %s", frodo)
                          .isEqualTo(sam);

The error message is:

java.lang.AssertionError: should be TolkienCharacter [name=Frodo, age=33, race=HOBBIT]
Lazy error message overriding

If the error message is expensive to build, use the overloaded methods taking a Supplier<String> instead of a String, the message will only be built if the assertion fails.

Example:

assertThat(player.isRookie()).overridingErrorMessage(() -> "Expecting Player to be a rookie but was not.")
                             .isTrue();

assertThat(player.isRookie()).withFailMessage(() -> "Expecting Player to be a rookie but was not.")
                             .isTrue();
2.5.5. Avoiding incorrect usage

There are a few things to keep in mind when using AssertJ to avoid misusing it.

Forgetting to call an assertion

The main trap is to pass the object under test to assertThat() and forget to call an assertion afterward. This misuse can be detected by multiple static code analysis tools:

SpotBugs or FindBugs with the RV_RETURN_VALUE_IGNORED_INFERRED rule

SonarQube with the Assertions should be complete (S2970) rule

other tools that can evaluate whether calls to methods annotated with the @CheckReturnValue annotation are done correctly.

Here’s what it looks like in SpotBugs:

Figure 1. SpotBugs detecting AssertJ invalid usage

The following examples show incorrect AssertJ API usage to avoid!

Bad

// DON'T DO THIS ! It does not assert anything
assertThat(actual.equals(expected));

Good

// DO THIS:
assertThat(actual).isEqualTo(expected);

// OR THIS (less classy but ok):
assertThat(actual.equals(expected)).isTrue();

Bad

// DON'T DO THIS ! It does not assert anything and passes
assertThat(1 == 2);

Good

// DO THIS: (fails as expected)
assertThat(1).isEqualTo(2);

// OR THIS (less classy but ok):
assertThat(1 == 2).isTrue();
Calling as() after the assertion

Describing an assertion must be done before calling the assertion. Otherwise it is ignored as a failing assertion will prevent the call to as().

Bad

// DON'T DO THIS ! as/describedAs have no effect after the assertion
assertThat(actual).isEqualTo(expected).as("description");
assertThat(actual).isEqualTo(expected).describedAs("description");

Good

// DO THIS: use as/describedAs before the assertion
assertThat(actual).as("description").isEqualTo(expected);
assertThat(actual).describedAs("description").isEqualTo(expected);
Calling withFailMessage/overridingErrorMessage after the assertion

Setting an error message must be done before calling the assertion. Otherwise it is ignored as a failing assertion will prevent the call to withFailMessage() / overridingErrorMessage().

Bad

// DON'T DO THIS ! overridingErrorMessage/withFailMessage have no effect after the assertion
assertThat(actual).isEqualTo(expected).overridingErrorMessage("custom error message");
assertThat(actual).isEqualTo(expected).withFailMessage("custom error message");

Good

// DO THIS: use overridingErrorMessage/withFailMessage before the assertion
assertThat(actual).overridingErrorMessage("custom error message").isEqualTo(expected);
assertThat(actual).withFailMessage("custom error message").isEqualTo(expected);
Setting a comparator after the assertion

Setting comparators must be done before calling the assertion. Otherwise it is ignored as a failing assertion will prevent the call to usingComparator() / usingElementComparator().

Bad

// DON'T DO THIS ! Comparator is not used
assertThat(actual).isEqualTo(expected).usingComparator(new CustomComparator());

Good

// DO THIS:
assertThat(actual).usingComparator(new CustomComparator()).isEqualTo("a");
2.5.6. Configuring AssertJ

This section describes the different ways to configure AssertJ, either by setting configuration properties individually or globally using the Configuration class.

To be effective the configuration changes must be applied before the tests are executed, depending on the scope of the tests this means different things:

For a single test: change the configuration in the test and revert it in the @AfterEach method (JUnit 5).

For all tests in a class: change the configuration in the @BeforeAll method and revert the changes in the @AfterAll method (JUnit 5).

To change the configuration before any tests, you can use these options:

write a JUnit 5 extension implementing BeforeAllCallback.

register your own Configuration subclass and let AssertJ discover it automagically.

Configuring single properties

The Assertions class provides static methods to change each configuration properties.

Assertions.setAllowComparingPrivateFields(true);
Assertions.setAllowExtractingPrivateFields(false);
Assertions.setExtractBareNamePropertyMethods(false);
Assertions.setLenientDateParsing(true);
Assertions.setMaxElementsForPrinting(100);
Assertions.setMaxLengthForSingleLineDescription(250);
Assertions.setRemoveAssertJRelatedElementsFromStackTrace(true);
Assertions.useRepresentation(myRepresentation);
Assertions.registerCustomDateFormat(myCustomDateFormat);
Assertions.setPrintAssertionsDescription(true);
Assertions.setConsumerDescription(description -> writeToFile(description, report));
Representation

This property allows you to register a Representation to control the way AssertJ formats the different types displayed in the assertion error messages. Consult the Controlling type formatting chapter for details.

Defaults to StandardRepresentation.

AllowComparingPrivateFields

Globally sets whether the use of private fields is allowed for field/property by field/property comparison. Defaults to true.

AllowExtractingPrivateFields

Globally sets whether the AssertJ extracting capability should be allowed to extract private fields. Defaults to true.

ExtractBareNamePropertyMethods

Globally sets whether the AssertJ extracting capability considers bare-named property methods like String name(). Defaults to true.

LenientDateParsing

Specify whether or not date/time parsing is to be lenient for AssertJ default date formats. With lenient parsing, the parser may use heuristics to interpret inputs that do not precisely match this object’s format. With strict parsing, inputs must match this object’s format.

Custom DateFormat

In addition to the default date formats, you can register some custom ones that AssertJ will use in date assertions (see also Assertions.registerCustomDateFormat).

Note that custom date formats take precedence over default ones.

MaxElementsForPrinting

In error messages, sets the threshold for how many elements from one iterable/array/map will be included in the description. Defaults to 1000.

The point of this property is to avoid printing iterable/array/map with too many elements in error messages.

MaxLengthForSingleLineDescription

In error messages, sets the threshold when iterable/array formatting will be on one line (if their String description is less than this parameter) or it will be formatted with one element per line. Defaults to 80.

Example:

String[] greatBooks = array("A Game of Thrones", "The Lord of the Rings", "Assassin's Apprentice");

this array is formatted on one line as its length < 80:

["A Game of Thrones", "The Lord of the Rings", "Assassin's Apprentice"]

Whereas this array …​

String[] greatBooks = array("A Game of Thrones", "The Lord of the Rings", "Assassin's Apprentice", "Guards! Guards! (Discworld)");

... is formatted on multiple lines with one element per line:

["A Game of Thrones",
 "The Lord of the Rings",
 "Assassin's Apprentice",
 "Guards! Guards! (Discworld)"]
RemoveAssertJRelatedElementsFromStackTrace

Sets whether the elements related to AssertJ are removed from assertion errors stack trace. Defaults to true.

AssertJ Configuration

Since 3.13.0, AssertJ exposes a org.assertj.core.configuration.Configuration object providing access to all AssertJ globally configurable properties.

You can create an instance of org.assertj.core.configuration.Configuration and change indivual properties through setters or create your own custom configuration by inheriting from it and overriding the methods to change the default behavior as in the CustomConfiguration example below.

	Your configuration will be effective once you call Configuration.apply() or Configuration.applyAndDisplay().

Example:

Configuration configuration = new Configuration();

configuration.setBareNamePropertyExtraction(false);
configuration.setComparingPrivateFields(false);
configuration.setExtractingPrivateFields(false);
configuration.setLenientDateParsing(true);
configuration.setMaxElementsForPrinting(1001);
configuration.setMaxLengthForSingleLineDescription(81);
configuration.setRemoveAssertJRelatedElementsFromStackTrace(false);

// don't forget to apply it!
configuration.applyAndDisplay();

Printing the above configuration produces the following output:

Applying configuration org.assertj.core.configuration.Configuration
- representation .................................. = BinaryRepresentation
- comparingPrivateFieldsEnabled ................... = false
- extractingPrivateFieldsEnabled .................. = true
- bareNamePropertyExtractionEnabled ............... = false
- lenientDateParsingEnabled ....................... = true
- additional date formats ......................... = [yyyy_MM_dd, yyyy|MM|dd]
- maxLengthForSingleLineDescription ............... = 150
- maxElementsForPrinting .......................... = 2000
- removeAssertJRelatedElementsFromStackTraceEnabled = true
Automagic configuration discovery

This section describes a way to register an AssertJ Configuration without using any test framework hooks like BeforeAllCallback.

Follow the steps below to register your Configuration as an SPI:

Create your own configuration inheriting from org.assertj.core.configuration.Configuration

Create a file named org.assertj.core.configuration.Configuration in a META-INF/services directory

Make sure META-INF/services/ is in the runtime classpath, usually putting it in src/test/resources will do.

Put the fully qualified class name of your Configuration in services/org.assertj.core.configuration.Configuration.

This is all you have to do, AssertJ will pick up the Configuration automatically and display it at the first interaction with AssertJ.

Here’s an example of a custom configuration class:

package example.core;

import static org.assertj.core.presentation.BinaryRepresentation.BINARY_REPRESENTATION;
import static org.assertj.core.util.Lists.list;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.List;

import org.assertj.core.configuration.Configuration;
import org.assertj.core.presentation.Representation;

class CustomConfiguration extends Configuration {

  private static final SimpleDateFormat DATE_FORMAT1 = new SimpleDateFormat("yyyy_MM_dd");
  private static final SimpleDateFormat DATE_FORMAT2 = new SimpleDateFormat("yyyy|MM|dd");

  // we keep the default behavior for extractingPrivateFieldsEnabled since it is not overridden

  @Override
  public Representation representation() {
    return BINARY_REPRESENTATION;
  }

  @Override
  public boolean bareNamePropertyExtractionEnabled() {
    return false;
  }

  @Override
  public boolean comparingPrivateFieldsEnabled() {
    return false;
  }

  @Override
  public boolean lenientDateParsingEnabled() {
    return true;
  }

  @Override
  public List<DateFormat> additionalDateFormats() {
    return list(DATE_FORMAT1, DATE_FORMAT2);
  }

  @Override
  public int maxElementsForPrinting() {
    return 2000;
  }

  @Override
  public int maxLengthForSingleLineDescription() {
    return 150;
  }
}

With this custom configuration, the content of META-INF/services/org.assertj.core.configuration.Configuration must be:

example.core.CustomConfiguration

Printing the CustomConfiguration shows:

Applying configuration example.core.CustomConfiguration
- representation .................................. = BinaryRepresentation
- comparingPrivateFieldsEnabled ................... = false
- extractingPrivateFieldsEnabled .................. = true
- bareNamePropertyExtractionEnabled ............... = false
- lenientDateParsingEnabled ....................... = true
- additionnal date formats ........................ = [yyyy_MM_dd, yyyy|MM|dd]
- maxLengthForSingleLineDescription ............... = 150
- maxElementsForPrinting .......................... = 2000
- removeAssertJRelatedElementsFromStackTraceEnabled = true
2.5.7. Controlling type formatting

Assertions error messages use a Representation to format the different types involved. There are multiple ways of registering a custom Representation for assertions:

Changing the default global Representation by calling Assertions.useRepresentation(myRepresentation) - see Changing the default global scope custom representation

Changing the Representation per assertion with assertThat(actual).withRepresentation(myRepresentation) - see Per assertion scope custom representation

Globally registering a Configuration that specifies the Representation to use - see AssertJ global configuration.

Registering multiple fine grained representations that only defines representation of their custom types.

Let’s go over these different options with a custom Representation.

Creating a custom Representation

An example of a custom Representation:

// dummy class
private class Example {}

public class CustomRepresentation extends StandardRepresentation { 

  // override fallbackToStringOf to handle Example formatting
  @Override
  public String fallbackToStringOf(Object o) { 
    if (o instanceof Example) return "Example";
    // fallback to default formatting.
    return super.fallbackToStringOf(o);
  }

  // override a predefined type formatting: String
  @Override
  protected String toStringOf(String str) { 
    return "$" + str + "$";
  }
}
	Extends org.assertj.core.presentation.StandardRepresentation to get AssertJ default representation.
	Override fallbackToStringOf and handle your specific types before falling back to the default formatting.
	Change a predefined type formatting by overriding the toStringOf method that takes it as a parameter.

Let’s see the above custom representation in action when representing Example or String instances.

This assertion fails …​

assertThat(new Example()).isNull();

…​with the following error:

expected:<[null]> but was:<[Example]>

This one fails …​

// this one fails ...
assertThat("foo").startsWith("bar");

…​with the following error:

Expecting:
  <$foo$>
to start with:
  <$bar$>
Changing the default global scope custom representation

You only have to register CustomRepresentation once but need to do it before executing any tests, for the tests executed before that, AssertJ will use the default representation.

// to call before executing tests
Assertions.useRepresentation(new CustomRepresentation());

Consider writing a JUnit 5 extension implementing BeforeAllCallback to make sure the representation is set once for all before any test is executed.

Per assertion scope custom representation

Follow this approach if you want to use a specific representation for a single assertion only.

Example with the failing assertions used before:

Representation customRepresentation = new CustomRepresentation();

// this assertion fails ...
assertThat(new Example()).withRepresentation(customRepresentation)
                         .isNull();

assertThat("foo").withRepresentation(customRepresentation)
                 .startsWith("bar");
Registering multiple fine-grained representations

Since 3.22.0 AssertJ allows registering multiple representations (one per jar).

The typical use case is for different domain-specific libraries to be able to independently register Representation implementations for their specific domain objects.

	

In case different representations can represent the same type, the one with the highest priority wins.

Let’s take a concrete example where we have two domain specific libraries: Lotr and star wars and a project that uses them both.

The Lotr library is composed of an Hobbit class and a specific representation for it, note that LotrRepresentation represents Hobbits starting with HOBBIT unlike Hobbit toString method:

package org.assertj.example.lotr;

public class Hobbit {

  public String name;
  public String age;

  @Override
  public String toString() {
    return format("Hobbit [name=%s, age=%s]", name, age);
  }
}

public class LotrRepresentation implements Representation {

  @Override
  public String toStringOf(Object object) {
    if (object instanceof Hobbit) {
      Hobbit hobbit = (Hobbit) object;
      return String.format("HOBBIT [name=%s, age=%s]", hobbit.name, hobbit.age);
    }
    return null;
  }

  // only needed if another library was to represent Hobbit, in this case the one with highest priority wins
  @Override
  public int getPriority() {
    return 5;
  }
}

LotrRepresentation is registered by creating a META-INF/services/org.assertj.core.presentation.Representation file that contain org.assertj.example.lotr.LotrRepresentation, the file must be available in the classpath (typically by putting it in src/main/resources it will end up in the library jar).

Similarly the star wars library defines a Jedi and a StarWarsRepresentation:

package org.assertj.example.starwars;

public class Jedi {

  public String name;
  public String age;

  @Override
  public String toString() {
    return format("Jedi [name=%s, age=%s]", name, age);
  }
}

public class StarWarsRepresentation implements Representation {

  @Override
  public String toStringOf(Object object) {
    if (object instanceof Jedi) {
      Jedi jedi = (Jedi) object;
      return String.format("JEDI [name=%s, age=%s]", jedi.name, jedi.age);
    }
    return null;
  }

  @Override
  public int getPriority() {
    return 10;
  }
}

Same as the Lotr library, StarWarsRepresentation is registered by creating a META-INF/services/org.assertj.core.presentation.Representation file that contain org.assertj.example.starwars.StarWarsRepresentation.

The consuming project specifies both libraries as dependencies, since both have registered a representation, AssertJ will discover them and keep them in a composite representation that aggregates all registered representaions.

The following test fails with frodo and luke being represented by LotrRepresentation and StarWarsRepresentation respectively.

Hobbit frodo = new Hobbit();
frodo.name = "Frodo";
frodo.age = "33";

Jedi luke = new Jedi();
luke.name = "Luke";
luke.age = "23";

assertThat(frodo).isEqualTo(luke);

Error message:

org.opentest4j.AssertionFailedError:
expected: JEDI [name=Luke, age=23]
 but was: HOBBIT [name=Frodo, age=33]
2.5.8. Common assertions

This section describes the assertions common to all types, the Javadoc for common assertions methods is available here.

2.5.9. Object assertions

The Javadoc for Object assertions is available here.

2.5.10. String/CharSequence assertions

This section describes all the available assertions for CharSequence (including String, StringBuilder, StringBuffer, …​):

The Javadoc for CharSequence assertions is available here.

2.5.11. Iterable and array assertions
Reference

All the available assertions are described in:

iterables: https://www.javadoc.io/doc/org.assertj/assertj-core/3.27.7/org/assertj/core/api/AbstractIterableAssert.html#method.summary

arrays: https://www.javadoc.io/doc/org.assertj/assertj-core/3.27.7/org/assertj/core/api/AbstractObjectArrayAssert.html#method.summary

The next sections focus on some features worth knowing to get the best of AssertJ, notably:

Different ways of checking iterables/arrays content

Running assertions on some elements (any, all, none)

Navigating to a given element to check it

Filtering elements before asserting]

Extracting/mapping elements before asserting

Comparing elements with a specific comparator

Checking iterables/arrays content

There are different flavors of contains assertion, here’s a table to help choose the most relevant one:

Assertion	Description


contains

	

Verifies that the actual iterable/array contains the given values in any order




containsOnly

	

Verifies that the actual group contains only the given values and nothing else in any order and ignoring duplicates (i.e. once a value is found, its duplicates are also considered found)




containsExactly

	

Verifies that the actual iterable/array contains exactly the given values and nothing else in order




containsExactlyInAnyOrder

	

Verifies that the actual iterable/array contains exactly the given values and nothing else in any order




containsSequence

	

Verifies that the actual group contains the given sequence in the correct order and without extra values between the sequence values




containsSubsequence

	

Verifies that the actual group contains the given subsequence in the correct order possibly with other values between them




containsOnlyOnce

	

Verifies that the actual iterable/array contains the given values only once




containsAnyOf

	

Verifies that the actual iterable/array contains at least one of the given values (like an or operator on the given values)

	the assertions above have a variant accepting an iterable/array argument, ex: containsExactly(E…​) and containsExactlyElementsOf(Iterable)
Verify assertions on some elements
Satisfy

You can assert that all or any elements verify the given assertions with allSatisfy and anySatisfy, conversely noneSatisfy lets you assert that no elements verify the given assertions.

The given assertions are expressed with a Consumer (typically with a lambda).

Examples:

List<TolkienCharacter> hobbits = list(frodo, sam, pippin);

// all elements must satisfy the given assertions
assertThat(hobbits).allSatisfy(character -> {
  assertThat(character.getRace()).isEqualTo(HOBBIT);
  assertThat(character.getName()).isNotEqualTo("Sauron");
});

// at least one element must satisfy the given assertions
assertThat(hobbits).anySatisfy(character -> {
  assertThat(character.getRace()).isEqualTo(HOBBIT);
  assertThat(character.getName()).isEqualTo("Sam");
});

// no element must satisfy the given assertions
assertThat(hobbits).noneSatisfy(character -> assertThat(character.getRace()).isEqualTo(ELF));
	if allSatisfy fails, all the elements and their failing the assertions are reported.
Match

You can assert that all or any elements match the given Predicate with allMatch and anyMatch, conversely noneMatch lets you assert that no elements verify the given predicate.

Examples:

List<TolkienCharacter> hobbits = list(frodo, sam, pippin);

assertThat(hobbits).allMatch(character -> character.getRace() == HOBBIT, "hobbits")
                   .anyMatch(character -> character.getName().contains("pp"))
                   .noneMatch(character -> character.getRace() == ORC);
	You can pass a predicate description to make the error message more explicit if the assertion fails.
Navigating to a given element

The idea is to navigate to a given element in order to check it, you can navigate to the first, last or any element by index or if you expect only one element use singleElement.

	this is only available for iterables at the moment.
First / last / element(index)

Use first, last and element(index) to navigate to the corresponding element, after navigating you can only use object assertions unless you have specified an Assert class or preferrably an InstanceOfAssertFactory as shown in the following examples.

Examples:

// only object assertions available after navigation
Iterable<TolkienCharacter> hobbits = list(frodo, sam, pippin);
assertThat(hobbits).first().isEqualTo(frodo);
assertThat(hobbits).element(1).isEqualTo(sam);
assertThat(hobbits).last().isEqualTo(pippin);

// strongly typed String assertions after navigation
Iterable<String> hobbitsName = list("frodo", "sam", "pippin");
// STRING is an InstanceOfAssertFactory from org.assertj.core.api.InstanceOfAssertFactories.STRING
// as() is just synthetic sugar for readability
assertThat(hobbitsName).first(as(STRING))
                       .startsWith("fro")
                       .endsWith("do");
assertThat(hobbitsName).element(1, as(STRING))
                       .startsWith("sa")
                       .endsWith("am");
assertThat(hobbitsName).last(as(STRING))
                       .startsWith("pip")
                       .endsWith("pin");

// alternative for strongly typed assertions
assertThat(hobbitsName, StringAssert.class).first()
                                           .startsWith("fro")
                                           .endsWith("do");
Single element

singleElement checks that the iterable has only one element and navigates to it, after navigating you can only use object assertions unless you have specified an Assert class or preferrably an InstanceOfAssertFactory as shown in the following examples.

Examples:

Iterable<String> babySimpsons = list("Maggie");

// only object assertions available
assertThat(babySimpsons).singleElement()
                        .isEqualTo("Maggie");

// to get specific typed assertions, pass the corresponding InstanceOfAssertFactory from
// org.assertj.core.api.InstanceOfAssertFactories.STRING), as() is just synthetic sugar for readability
assertThat(babySimpsons).singleElement(as(STRING))
                        .endsWith("gie");

// alternative for strongly typed assertions
assertThat(babySimpsons, StringAssert.class).singleElement()
                                            .startsWith("Mag");
Filtering elements

Filtering is handy to target assertions on some specific elements, the filter criteria can be expressed by:

a java Predicate

an element property/field having a specific value (or not) or in a set of values (or not)

an element property/field having a null value

an element matching some assertions

an element matching a Condition

Let’s explore these options in some examples taken from FilterExamples from the assertions-examples project.

Filtering with a Predicate

You specify the filter condition using simple predicate, best expressed with a lambda.

Example:

assertThat(fellowshipOfTheRing).filteredOn( character -> character.getName().contains("o") )
                               .containsOnly(aragorn, frodo, legolas, boromir);
Filtering on a property or a field

First you specify the property/field name to filter on and then its expected value. The filter first tries to get the value from a property, then from a field. Reading private fields is supported by default, but can be disabled globally by calling Assertions.setAllowExtractingPrivateFields(false).

Filter supports nested properties/fields. Note that if an intermediate value is null the whole nested property/field is considered to be null, for example reading "address.street.name" will return null if "address.street" is null.

Filters support these basic operations: not, in, notIn

import static org.assertj.core.api.Assertions.in;
import static org.assertj.core.api.Assertions.not;
import static org.assertj.core.api.Assertions.notIn;
...

// filters use introspection to get property/field values
assertThat(fellowshipOfTheRing).filteredOn("race", HOBBIT)
                               .containsOnly(sam, frodo, pippin, merry);

// nested properties are supported
assertThat(fellowshipOfTheRing).filteredOn("race.name", "Man")
                               .containsOnly(aragorn, boromir);

// you can apply different comparison
assertThat(fellowshipOfTheRing).filteredOn("race", notIn(HOBBIT, MAN))
                               .containsOnly(gandalf, gimli, legolas);

assertThat(fellowshipOfTheRing).filteredOn("race", in(MAIA, MAN))
                               .containsOnly(gandalf, boromir, aragorn);

assertThat(fellowshipOfTheRing).filteredOn("race", not(HOBBIT))
                               .containsOnly(gandalf, boromir, aragorn, gimli, legolas);

// you can chain multiple filter criteria
assertThat(fellowshipOfTheRing).filteredOn("race", MAN)
                               .filteredOn("name", not("Boromir"))
                               .containsOnly(aragorn);
Filtering on a function return value

This is a more flexible way of getting the value to filter on but note that there is no support for operators like not, in and notIn.

assertThat(fellowshipOfTheRing).filteredOn(TolkienCharacter::getRace, HOBBIT)
                               .containsOnly(sam, frodo, pippin, merry);
Filtering on null value

Filters the elements whose specified property/field is null.

Filter supports nested properties/fields. Note that if an intermediate value is null the whole nested property/field is considered to be null, for example reading "address.street.name" will return null if "address.street" is null.

TolkienCharacter pippin = new TolkienCharacter("Pippin", 28, HOBBIT);
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);
TolkienCharacter merry = new TolkienCharacter("Merry", 36, HOBBIT);
TolkienCharacter mysteriousHobbit = new TolkienCharacter(null, 38, HOBBIT);

List<TolkienCharacter> hobbits = list(frodo, mysteriousHobbit, merry, pippin);

assertThat(hobbits).filteredOnNull("name"))
                   .singleElement()
                   .isEqualTo(mysteriousHobbit);
Filtering elements matching given assertions

Filters the iterable under test keeping only elements matching the given assertions specified with a Consumer.

Example: check hobbits whose age < 34

TolkienCharacter pippin = new TolkienCharacter("Pippin", 28, HOBBIT);
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);
TolkienCharacter merry = new TolkienCharacter("Merry", 36, HOBBIT);
TolkienCharacter sam = new TolkienCharacter("Sam", 38, HOBBIT);

List<TolkienCharacter> hobbits = list(frodo, sam, merry, pippin);

assertThat(hobbits).filteredOnAssertions(hobbit -> assertThat(hobbit.age).isLessThan(34))
                   .containsOnly(frodo, pippin);
Filtering with a Condition

Filter the iterable/array under test keeping only elements matching the given Condition.

Two methods are available: being(Condition) and having(Condition). They do the same job - pick the one that makes your code more readable!

import org.assertj.core.api.Condition;

Condition<Player> mvpStats= new Condition<Player>(player -> {
    return player.pointsPerGame() > 20 && (player.assistsPerGame() >= 8 || player.reboundsPerGame() >= 8);
  }, "mvp");

List<Player> players;
players.add(rose); // Derrick Rose: 25 ppg - 8 assists - 5 rebounds
players.add(lebron); // Lebron James: 27 ppg - 6 assists - 9 rebounds
players.add(noah); // Joachim Noah: 8 ppg - 5 assists - 11 rebounds

// noah does not have more than 20 ppg
assertThat(players).filteredOn(mvpStats)
                   .containsOnly(rose, lebron);
Extracting elements values
What problem extracting solves

Let’s say you have called some service and got a list (or an array) of TolkienCharacter, to check the results you have to build the expected TolkienCharacters, that can be quite tedious!

List<TolkienCharacter> fellowshipOfTheRing = tolkienDao.findHeroes();  // frodo, sam, aragorn ...

// requires creation of frodo and aragorn, the expected TolkienCharacters
assertThat(fellowshipOfTheRing).contains(frodo, aragorn);

Instead, it is usually enough to check some fields or properties on the elements, for that you have to extract the fields/properties before performing your assertions, something like:

// extract the names ...
List<String> names = fellowshipOfTheRing.stream().map(TolkienCharacter::getName).collect(toList());
// ... and finally assert something
assertThat(names).contains("Boromir", "Gandalf", "Frodo", "Legolas");

This is too much work (even with the stream API), instead AssertJ can help extracting values from the elements under tests, there are several ways of doing so:

Extracting a single value per element

Extracting a multiple values per element

Extracting and flattening multiple values per element

Extracting single value per element

Specify the field/property to extract (or pass a Function) from each elements and perform assertions on the extracted values.

Extracting by name can access private fields/properties which is handy to check internals not exposed with public methods (lambda won’t work here), it also supports nested field/property like "race.name".

Examples:

// "name" needs to be either a property or a field of the TolkienCharacter class
assertThat(fellowshipOfTheRing).extracting("name")
                               .contains("Boromir", "Gandalf", "Frodo", "Legolas")
                               .doesNotContain("Sauron", "Elrond");

// specifying nested field/property is supported
assertThat(fellowshipOfTheRing).extracting("race.name")
                               .contains("Man", "Maia", "Hobbit", "Elf");

// same thing with a lambda which is type safe and refactoring friendly:
assertThat(fellowshipOfTheRing).extracting(TolkienCharacter::getName)
                               .contains("Boromir", "Gandalf", "Frodo", "Legolas");

// same thing map an alias of extracting:
assertThat(fellowshipOfTheRing).map(TolkienCharacter::getName)
                               .contains("Boromir", "Gandalf", "Frodo", "Legolas");

Note that extracting one property can be made strongly typed by giving the property type as the second argument.

// to have type safe extracting, use the second parameter to pass the expected property type:
assertThat(fellowshipOfTheRing).extracting("name", String.class)
                               .contains("Boromir", "Gandalf", "Frodo", "Legolas")
                               .doesNotContain("Sauron", "Elrond");
Extracting multiple values

You can extract several values from the elements under test and check them using tuples.

As an example, let’s check the name, age and race’s name of each TolkienCharacter element:

// when checking several properties/fields you have to use tuples:
import static org.assertj.core.api.Assertions.tuple;

// extracting name, age and race.name nested property
assertThat(fellowshipOfTheRing).extracting("name", "age", "race.name")
                               .contains(tuple("Boromir", 37, "Man"),
                                         tuple("Sam", 38, "Hobbit"),
                                         tuple("Legolas", 1000, "Elf"));

// same assertion with functions for type safety:
assertThat(fellowshipOfTheRing).extracting(TolkienCharacter::getName,
                                            tolkienCharacter -> tolkienCharacter.age,
                                            tolkienCharacter -> tolkienCharacter.getRace().getName())
                                .contains(tuple("Boromir", 37, "Man"),
                                          tuple("Sam", 38, "Hobbit"),
                                          tuple("Legolas", 1000, "Elf"));

The extracted name, age and race’s name values of the current element are grouped in a tuple, thus you need to use tuples for specifying the expected values.

More examples are available in IterableAssertionsExamples.java of the assertj-examples project.

Extracting and flattening multiple values per element

Flat extracting is hard to explain but easy to understand with an example, so let’s see how it works (in functional programming it is juts a flatMap).

Let’s assume we have a Player class with a teamMates property returning a List<Player> and we want to assert that it returns the expected players:

Player jordan = ... // initialized with Pippen and Kukoc team mates
Player magic = ... // initialized with Jabbar and Worthy team mates
List<Player> reallyGoodPlayers = list(jordan, magic);

// check all team mates by specifying the teamMates property (Player has a getTeamMates() method):
assertThat(reallyGoodPlayers).flatExtracting("teamMates")
                             .contains(pippen, kukoc, jabbar, worthy);

// alternatively, you can use a Function for type safety:
assertThat(reallyGoodPlayers).flatExtracting(BasketBallPlayer::getTeamMates)
                             .contains(pippen, kukoc, jabbar, worthy);

// flatMap is an alias of flatExtracting:
assertThat(reallyGoodPlayers).flatMap(BasketBallPlayer::getTeamMates)
                             .contains(pippen, kukoc, jabbar, worthy);

// if you use extracting instead of flatExtracting the result would be a list of list of players so the assertion becomes:
assertThat(reallyGoodPlayers).extracting("teamMates")
                             .contains(list(pippen, kukoc), list(jabbar, worthy));
	You can use flatMap in place of flatExtracting (except for the variant taking a String)

Flat extracting can be used to group multiple values if you don’t want to use extracting and tuples:

// extract a list of values, flatten them and use contains assertion
assertThat(fellowshipOfTheRing).flatExtracting("name", "race.name")
                               .contains("Frodo", "Hobbit", "Legolas", "Elf");

// same assertions with Functions:
assertThat(fellowshipOfTheRing).flatExtracting(TolkienCharacter::getName,
                                               tc -> tc.getRace().getName())
                               .contains("Frodo", "Hobbit", "Legolas", "Elf");
Comparing elements with a specific comparator

usingElementComparator allows you to change the way elements are compared (instead of using the elements equals method).

Examples:

List<TolkienCharacter> fellowshipOfTheRing = list(frodo, sam, merry, pippin, gandald, legolas, boromir, aragorn, gimli);

// the fellowshipOfTheRing includes Gandalf but not Sauron ...
assertThat(fellowshipOfTheRing).contains(gandalf)
                               .doesNotContain(sauron);

// ... but if we compare only races, Sauron is in fellowshipOfTheRing since he's a Maia like Gandalf
assertThat(fellowshipOfTheRing).usingElementComparator((t1, t2) -> t1.getRace().compareTo(t2.getRace()))
                               .contains(sauron);
2.5.12. Exception assertions

This chapter answers the question: how to assert that an exception has been thrown and check that it is the expected one?

Reference

All the available assertions are described in the AbstractThrowableAssert Javadoc.

In this chapter the term exception is used interchangeably with throwable.

The next sections focus on some features worth knowing to get the best of AssertJ, notably:

Checking the exception message

Checking the exception cause and root cause

BDD assertion style with catchThrowable and catchThrowableOfType

assertThatThrownBy(code)

assertThatExceptionOfType(exception class)

Testing that no exception is thrown

If you use java 7, check the Java 7 section.

Checking exception message

There are various ways for checking the exception message content, you can check the exact message, what it contains, its start, its end, if it matches a regex.

Most of the assertions expecting a String can use the String.format syntax.

Examples:

Throwable throwable = new IllegalArgumentException("wrong amount 123");

assertThat(throwableWithMessage).hasMessage("wrong amount 123")
                                .hasMessage("%s amount %d", "wrong", 123)
                                // check start
                                .hasMessageStartingWith("wrong")
                                .hasMessageStartingWith("%s a", "wrong")
                                // check content
                                .hasMessageContaining("wrong amount")
                                .hasMessageContaining("wrong %s", "amount")
                                .hasMessageContainingAll("wrong", "amount")
                                // check end
                                .hasMessageEndingWith("123")
                                .hasMessageEndingWith("amount %s", "123")
                                // check with regex
                                .hasMessageMatching("wrong amount .*")
                                // check does not contain
                                .hasMessageNotContaining("right")
                                .hasMessageNotContainingAny("right", "price")
Checking the cause and root cause

There are two approaches to check the cause and root cause, either directly or navigate to it with cause() and rootCause() and check it.

Checking the cause

You can check the cause directly if you know it, but that’s not always possible, and in such cases you can only check its type. This is pretty limited in terms of assertions, a better approach is to navigate to the cause with cause() and take advantage of all existing exception assertions.

Direct cause assertions are limited …​

NullPointerException cause = new NullPointerException("boom!");
Throwable throwable = new Throwable(cause);

assertThat(throwable).hasCause(cause)
                     // hasCauseInstanceOf will match inheritance.
                     .hasCauseInstanceOf(NullPointerException.class)
                     .hasCauseInstanceOf(RuntimeException.class)
                     // hasCauseExactlyInstanceOf will match only exact same type
                     .hasCauseExactlyInstanceOf(NullPointerException.class);

... but navigating to the cause allows taking advantage of all exception assertions:

// navigate before checking
assertThat(throwable).cause()
                     .hasMessage("boom!")
                     .hasMessage("%s!", "boom")
                     .hasMessageStartingWith("bo")
                     .hasMessageEndingWith("!")
                     .hasMessageContaining("boo")
                     .hasMessageContainingAll("bo", "oom", "!")
                     .hasMessageMatching("b...!")
                     .hasMessageNotContaining("bam")
                     .hasMessageNotContainingAny("bam", "bim")
                     // isInstanceOf will match inheritance.
                     .isInstanceOf(NullPointerException.class)
                     .isInstanceOf(RuntimeException.class)
                     // isExactlyInstanceOf will match only exact same type
                     .isExactlyInstanceOf(NullPointerException.class);

An alternative is using assertThatExceptionOfType combined with havingCause as shown in the following example:

assertThatExceptionOfType(RuntimeException.class)
         .isThrownBy(() -> { throw new RuntimeException(new IllegalArgumentException("boom!")); })
         .havingCause()
         .withMessage("boom!");
Checking the root cause

You can check the root cause directly with hasRootCause, hasRootCauseMessage and hasRootCauseInstanceOf if you have access to it but that’s not always possible, this is a bit limited in terms of assertions, a better way is to navigate to the root cause with rootCause() and take advantage of all existing exception assertions.

Examples:

NullPointerException rootCause = new NullPointerException("null!");
Throwable throwable = new Throwable(new IllegalStateException(rootCause));

// direct root cause check
assertThat(throwable).hasRootCause(rootCause)
                     .hasRootCauseMessage("null!")
                     .hasRootCauseMessage("%s!", "null")
                     // hasRootCauseInstanceOf will match inheritance
                     .hasRootCauseInstanceOf(NullPointerException.class)
                     .hasRootCauseInstanceOf(RuntimeException.class)
                     // hasRootCauseExactlyInstanceOf will match only exact same type
                     .hasRootCauseExactlyInstanceOf(NullPointerException.class);

// navigate to root cause and check
assertThat(throwable).rootCause()
                     .hasMessage("null!")
                     .hasMessage("%s!", "null")
                     .hasMessageStartingWith("nu")
                     .hasMessageEndingWith("!")
                     .hasMessageContaining("ul")
                     .hasMessageContainingAll("nu", "ull", "l!")
                     .hasMessageMatching("n...!")
                     .hasMessageNotContaining("NULL")
                     .hasMessageNotContainingAny("Null", "NULL")
                     // isInstanceOf will match inheritance.
                     .isInstanceOf(NullPointerException.class)
                     .isInstanceOf(RuntimeException.class)
                     // isExactlyInstanceOf will match only exact same type
                     .isExactlyInstanceOf(NullPointerException.class);

An alternative is using assertThatExceptionOfType combined with havingRootCause as shown in the following example:

assertThatExceptionOfType(RuntimeException.class)
         .isThrownBy(() -> { throw new RuntimeException(new IllegalArgumentException(new NullPointerException("root error"))); })
         .havingRootCause()
         .withMessage("root error");
No cause

You can verify that a Throwable does not have a cause with hasNoCause().

BDD style

BDD aficionados can separate WHEN and THEN steps by using catchThrowable(ThrowingCallable) to capture the Throwable and then perform assertions (ThrowingCallable is a functional interface which can be expressed as a lambda).

Example:

// GIVEN
String[] names = { "Pier ", "Pol", "Jak" };
// WHEN
Throwable thrown = catchThrowable(() -> System.out.println(names[9]));
// THEN
then(thrown).isInstanceOf(ArrayIndexOutOfBoundsException.class)
            .hasMessageContaining("9");

// assertThat is also available but is less "BDD style"
assertThat(thrown).isInstanceOf(ArrayIndexOutOfBoundsException.class)
                  .hasMessageContaining("9");
	catchThrowable returns null if no exception is thrown, but there is a better way to check that no exception is thrown.

catchThrowableOfType is a variation of catchThrowable where the caught exception type is verified and returned allowing to check the custom exception fields/properties.

Example:

class TextException extends Exception {
   int line;
   int column;

   public TextException(String msg, int line, int column) {
     super(msg);
     this.line = line;
     this.column = column;
   }
 }

 TextException textException = catchThrowableOfType(TextException.class,
                                                    () -> { throw new TextException("boom!", 1, 5); });
 // assertions succeed
 assertThat(textException).hasMessageContaining("boom");
 assertThat(textException.line).isEqualTo(1);
 assertThat(textException.column).isEqualTo(5);

 // fails as TextException is not a RuntimeException
 catchThrowableOfType(RuntimeException.class, () -> { throw new TextException("boom!", 1, 5); });

Although the example above can be used for any exception type, enriched alternatives for catchThrowableOfType are also available to catch an instance of various commonly used exceptions:

catchException

catchIllegalArgumentException

catchIllegalStateException

catchIndexOutOfBoundsException

catchIOException

catchNullPointerException

catchReflectiveOperationException

catchRuntimeException

For example, using catchIOException, the ThrowingCallable given as a parameter is executed: catchIOException returns null if no exception is thrown, otherwise it checks that the caught Throwable is of type IOException and casts it, making it convenient to perform subtype-specific assertions on it.

IOException iOException = catchIOException(() -> {throw new IOException("boom!");});
// assertions succeed
assertThat(iOException).hasMessage("boom!");

// succeeds as catchIOException returns null when the code does not throw any exceptions
assertThat(catchIOException(() -> {})).isNull();

// fails as the thrown instance is not an IOException
catchIOException(() -> {throw new Exception("boom!");});

The other catchXXX alternatives work the same way for their respective exception type.

assertThatThrownBy

assertThatThrownBy(ThrowingCallable) is an alternative to catchThrowable, use it if you find more readable.

Example:

assertThatThrownBy(() -> { throw new Exception("boom!"); }).isInstanceOf(Exception.class)
                                                           .hasMessageContaining("boom");
	If the provided ThrowingCallable does not raise an exception, an assertion error is immediately thrown.
assertThatExceptionOfType

assertThatExceptionOfType is an alternative syntax that some people find more natural.

assertThatExceptionOfType(IOException.class).isThrownBy(() -> { throw new IOException("boom!"); })
                                            .withMessage("%s!", "boom")
                                            .withMessageContaining("boom")
                                            .withNoCause();
	If the provided ThrowingCallable does not raise an exception, an assertion error is immediately thrown.

Similarly to catchThrowableOfType, the latter syntax has been enriched for commonly used exceptions:

assertThatNullPointerException

assertThatIllegalArgumentException

assertThatIllegalStateException

assertThatIOException

The previous example can be rewritten as:

assertThatIOException().isThrownBy(() -> { throw new IOException("boom!"); })
                       .withMessage("%s!", "boom")
                       .withMessageContaining("boom")
                       .withNoCause();
Testing that no exception is thrown

You can test that a piece of code does not throw any exception with:

// standard style
assertThatNoException().isThrownBy(() -> System.out.println("OK"));
// BDD style
thenNoException().isThrownBy(() -> System.out.println("OK"));

or similarly:

// standard style
assertThatCode(() -> System.out.println("OK")).doesNotThrowAnyException();
// BDD style
thenCode(() -> System.out.println("OK")).doesNotThrowAnyException();
With Java 7 (AssertJ 2.x)

Asserting on exceptions is not as nice compared to the Java 8 way, this is how you would do it in AssertJ 2.x :

Put the code that should throw the exception in a try-catch.

Call fail method immediately after, so that the test fails if the exception is not thrown.

Assert the caught exception.

Note that fail method can be statically imported from Assertions class.

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.fail;
import static org.assertj.core.api.Assertions.failBecauseExceptionWasNotThrown;
// ... code omitted for brevity

assertThat(fellowshipOfTheRing).hasSize(9);

// here's the typical pattern to use Fail :
try {
  fellowshipOfTheRing.get(9); // argggl !
  // we should not arrive here => use fail to expresses that
  // if IndexOutOfBoundsException was not thrown, test would fail the specified message
  fail("IndexOutOfBoundsException expected because fellowshipOfTheRing has only 9 elements");
} catch (IndexOutOfBoundsException e) {
  assertThat(e).hasMessage("Index: 9, Size: 9");
}

// Warning: don't catch Throwable as it would also catch the AssertionError thrown by fail method

// another way to do the same thing
try {
  fellowshipOfTheRing.get(9); // argggl !
  // if IndexOutOfBoundsException was not thrown, test would fail with message :
  // "Expected IndexOutOfBoundsException to be thrown"
  failBecauseExceptionWasNotThrown(IndexOutOfBoundsException.class);
} catch (IndexOutOfBoundsException e) {
  assertThat(e).hasMessage("Index: 9, Size: 9");
}
2.5.13. Field by field recursive comparison

AssertJ Core provides a fluent recursive comparison API for Object assertions with the following capabilities:

Choosing a strict or lenient recursive comparison

Ignoring fields in the comparison

Specifying how to compare specific types or fields in the comparison

Use overridden equals instead of a recursive comparison

Ignoring all expected null fields

Ignoring all actual empty optional fields.

Overriding error messages for specific fields or types.

Specifying how to introspect the objects to compare.

The recursive comparison is meant to to replace isEqualToComparingFieldByFieldRecursively.

Basic usage

The recursive comparison mode starts after calling usingRecursiveComparison().

Here’s a simple example:

public class Person {
  String name;
  double height;
  Home home = new Home();
}

public class Home {
  Address address = new Address();
  Date ownedSince;
}

public static class Address {
  int number;
  String street;
}

Person sherlock = new Person("Sherlock", 1.80);
sherlock.home.ownedSince = new Date(123);
sherlock.home.address.street = "Baker Street";
sherlock.home.address.number = 221;

Person sherlock2 = new Person("Sherlock", 1.80);
sherlock2.home.ownedSince = new Date(123);
sherlock2.home.address.street = "Baker Street";
sherlock2.home.address.number = 221;

// assertion succeeds as the data of both objects are the same.
assertThat(sherlock).usingRecursiveComparison()
                    .isEqualTo(sherlock2);

// assertion fails as Person equals only compares references.
assertThat(sherlock).isEqualTo(sherlock2);

The comparison is not symmetrical since it is limited to actual fields.

The algorithm gathers actual fields and then compares them to the corresponding expected fields. It is then possible for the expected object to have more fields than actual, which can be handy when comparing a base type to a subtype with additional fields.

How field values are resolved

The recursive comparison uses introspection to find out the fields to compare and their values.

It first looks for the object under test fields (skipping any ignored ones as specified in the configuration), then it looks for the same fields in the expected object to compare to.

The next step is resolving the field values using first a getter method (if any) or reading the field value. The getter methods for a field x are getX() or isX() for boolean fields. If you enable bare properties resolution, a method x() is also used considered as a valid getter.

Bare name property is enabled by calling Assertions.setExtractBareNamePropertyMethods(true); (it is disabled by default since 3.18.0).

Lastly if the object under test is a map, the recursive comparison tries to resolve the field value by looking it up in the map with map.get(fieldName).

Since 3.24.0, you can specify your own strategy on how the recursive comparison resolve the values to compare, go to section specifying how to introspect the objects to compare for details.

Breaking changes

Since 3.18.0 bare name getter resolution are disabled by default, to get the previous behaviour back, call Assertions.setExtractBareNamePropertyMethods(true);

Since 3.17.0 it does not use anymore equals methods of classes that have overridden it, so no need to force recursive comparison on these classes. To get the previous behavior back, use usingOverriddenEquals().

isNotEqualTo

Since 3.17.0 isNotEqualTo is available in the recursive API, example:

// equals not overridden in TolkienCharacter
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);
TolkienCharacter frodoClone = new TolkienCharacter("Frodo", 33, HOBBIT);
TolkienCharacter youngFrodo = new TolkienCharacter("Frodo", 22, HOBBIT);

// Pass as equals compares object references
assertThat(frodo).isNotEqualTo(frodoClone);

// Fail as frodo and frodoClone are equals when doing a field by field comparison.
assertThat(frodo).usingRecursiveComparison()
                 .isNotEqualTo(frodoClone);

// Pass as one the age fields differ between frodo and youngFrodo.
assertThat(frodo).usingRecursiveComparison()
                 .isNotEqualTo(youngFrodo);
Strict or lenient comparison

By default the objects to compare can be of different types but must have the same properties/fields. For example if object under test has a work field of type Address, the expected object to compare the object under test to must also have one but it can of a different type like AddressDto.

It is possible to enforce strict type checking by calling withStrictTypeChecking() and make the comparison fail whenever the compared objects or their fields are not compatible. Compatible means that the expected object/field types are the same or a subtype of actual/field types, for example if actual is an Animal and expected a Dog, they will be compared field by field in strict type checking mode.

public class Person {
  String name;
  double height;
  Person bestFriend;
}

Person sherlock = new Person("Sherlock", 1.80);
sherlock.bestFriend = new Person("Watson", 1.70);

Person sherlockClone = new Person("Sherlock", 1.80);
sherlockClone.bestFriend = new Person("Watson", 1.70);

// assertion succeeds as sherlock and sherlockClone have the same data and types
assertThat(sherlock).usingRecursiveComparison()
                    .withStrictTypeChecking()
                    .isEqualTo(sherlockClone);

// Let's now define a data structure similar to Person

public class PersonDTO {
  String name;
  double height;
  PersonDTO bestFriend;
}

PersonDTO sherlockDto = new PersonDTO("Sherlock", 1.80);
sherlockDto.bestFriend = new PersonDTO("Watson", 1.70);

// assertion fails as Person and PersonDTO are not compatible even though they have the same data
assertThat(sherlock).usingRecursiveComparison()
                    .withStrictTypeChecking()
                    .isEqualTo(sherlockDto);

// Let's define a subclass of Person

public class Detective extends Person {
  boolean busy;
}

Detective detectiveSherlock = new Detective("Sherlock", 1.80);
detectiveSherlock.bestFriend = new Person("Watson", 1.70);
detectiveSherlock.busy = true;

// assertion succeeds as Detective inherits from Person and
// only Person's fields are included into the comparison.
assertThat(sherlock).usingRecursiveComparison()
                    .withStrictTypeChecking()
                    .isEqualTo(detectiveSherlock);
Ignoring fields in the comparison

It is possible to ignore fields of the object under test in the comparison, this is can be useful when a field has a generated value (like the current time) or is simply not relevant to compare.

There are a few ways to specify the fields to ignore:

directly with ignoringFields(String…​ fieldsToIgnore)

by regexes with ignoringFieldsMatchingRegexes(String…​ regexes)

by types with ignoringFieldsOfTypes(Class…​ typesToIgnore)

Nested fields can be specified like this: home.address.street

It is also possible to ignore the object under test with ignoringActualNullFields().

Examples

Person sherlock = new Person("Sherlock", 1.80);
sherlock.home.address.street = "Baker Street";
sherlock.home.address.number = 221;

// strangely moriarty and sherlock have the same height!
Person moriarty = new Person("Moriarty", 1.80);
moriarty.home.address.street = "Crime Street";
moriarty.home.address.number = 221;

// assertion succeeds as name and home.address.street fields are ignored in the comparison
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringFields("name", "home.address.street")
                    .isEqualTo(moriarty);

// assertion succeeds as once a field is ignored, its subfields are too
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringFields("name", "home")
                    .isEqualTo(moriarty);

// ignoring fields matching regexes: name and home match .*me
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringFieldsMatchingRegexes(".*me")
                    .isEqualTo(moriarty);

// ignoring null fields example:
sherlock.name = null;
sherlock.home.address.street = null;
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringActualNullFields()
                    .isEqualTo(moriarty);

// ignore height and address fields by type:
Person tallSherlock = new Person("sherlock", 2.10);
tallSherlock.home.address.street = "Long Baker Street";
tallSherlock.home.address.number = 222;
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringFieldsOfTypes(double.class, Address.class)
                    .isEqualTo(tallSherlock);
Using overridden equals

Since 3.17.0 the recursive comparison does not use overridden equals methods to compare fields anymore, it performs a recursive comparison on these fields, it is possible to change that behavior by calling usingOverriddenEquals().

Once using overridden equals methods is enabled, you can disable it for certain types or fields (and perform a recursive comparison instead) using the following methods:

ignoringOverriddenEqualsForTypes(Class…​) Any fields of these classes are compared recursively

ignoringOverriddenEqualsForFields(String…​) Any given fields are compared recursively

ignoringOverriddenEqualsForFieldsMatchingRegexes(String…​) Any fields matching one of these regexes are compared recursively

ignoringAllOverriddenEquals() except for java types, all fields are compared field by field recursively

Example:

public class Person {
  String name;
  double height;
  Home home = new Home();
}

public class Home {
  Address address = new Address();
}

public static class Address {
  int number;
  String street;

  // only compares number, ouch!
  @Override
  public boolean equals(final Object other) {
    if (!(other instanceof Address)) return false;
    Address castOther = (Address) other;
    return Objects.equals(number, castOther.number);
  }
}

Person sherlock = new Person("Sherlock", 1.80);
sherlock.home.address.street = "Baker Street";
sherlock.home.address.number = 221;

Person sherlock2 = new Person("Sherlock", 1.80);
sherlock2.home.address.street = "Butcher Street";
sherlock2.home.address.number = 221;

// assertion succeeds but that's not what we expected since the home.address.street fields differ
// but the equals implementation in Address does not compare them.
assertThat(sherlock).usingRecursiveComparison()
                    .usingOverriddenEquals()
                    .isEqualTo(sherlock2);

// to avoid the previous issue, we force a recursive comparison on the Address type
// now this assertion fails as expected since the home.address.street fields differ.
assertThat(sherlock).usingRecursiveComparison()
                    .usingOverriddenEquals()
                    .ignoringOverriddenEqualsForTypes(Address.class)
                    .isEqualTo(sherlock2);
Ignoring all expected null fields

By using ignoringExpectedNullFields() the recursive comparison will exclude from the comparison any null fields in the expected object.
One use case for that is when the object under test have fields with values hard to predict (id, timestamp, …​), with this feature you simply build the expected object with null values values for these fields and they won’t be compared.

Example:

public class Person {
  String name;
  double height;
  Home home = new Home();
}
public class Home {
  Address address = new Address();
}
public static class Address {
  int number;
  String street;
}

Person sherlock = new Person("Sherlock", 1.80);
sherlock.home.address.street = "Baker Street";
sherlock.home.address.number = 221;

Person noName = new Person(null, 1.80);
noName.home.address.street = null;
noName.home.address.number = 221;

// assertion succeeds as name and home.address.street fields are ignored in the comparison
assertThat(sherlock).usingRecursiveComparison()
                    .ignoringExpectedNullFields()
                    .isEqualTo(noName);

// assertion fails as name and home.address.street fields are populated for sherlock but not for noName.
assertThat(noName).usingRecursiveComparison()
                  .ignoringExpectedNullFields()
                  .isEqualTo(sherlock);
Ignoring all actual empty optional fields

ignoringActualEmptyOptionalFields() makes the recursive comparison to ignore all actual empty optional fields (including Optional, OptionalInt, OptionalLong and OptionalDouble).
Note that the expected object empty optional fields are not ignored, this only applies to actual’s fields.

public class Person {
  String name;
  OptionalInt age;
  OptionalLong id;
  OptionalDouble height;
  Home home = new Home();
}

public class Home {
  String address;
  Optional<String> phone;
}

Person homerWithoutDetails = new Person("Homer Simpson");
homerWithoutDetails.home.address.street = "Evergreen Terrace";
homerWithoutDetails.home.address.number = 742;
homerWithoutDetails.home.phone = Optional.empty();
homerWithoutDetails.age = OptionalInt.empty();
homerWithoutDetails.id = OptionalLong.empty();
homerWithoutDetails.height = OptionalDouble.empty();

Person homerWithDetails = new Person("Homer Simpson");
homerWithDetails.home.address.street = "Evergreen Terrace";
homerWithDetails.home.address.number = 742;
homerWithDetails.home.phone = Optional.of("(939) 555-0113");
homerWithDetails.age = OptionalInt.of(39);
homerWithDetails.id = OptionalLong.of(123456);
homerWithDetails.height = OptionalDouble.of(1.83);

// assertion succeeds as phone is ignored in the comparison
assertThat(homerWithoutDetails).usingRecursiveComparison()
                               .ignoringActualEmptyOptionalFields()
                               .isEqualTo(homerWithDetails);

// assertion fails as phone, age, id and height are not ignored and are populated for homerWithDetails but not for homerWithoutDetails.
assertThat(homerWithDetails).usingRecursiveComparison()
                            .ignoringActualEmptyOptionalFields()
                            .isEqualTo(homerWithoutDetails);
Specifying how to compare specific types or fields in the comparison

You can specify how to compare values per (nested) fields or type with the methods below (but before calling isEqualTo otherwise this has no effect!):

withEqualsForFields(BiPredicate, String…​) or withComparatorForFields(Comparator, String…​) for one or multiple fields

withEqualsForType(BiPredicate, Class) or withComparatorForType(Comparator, Class) for a given type

Note that comparisons specified for fields take precedence over the ones specified for types.

By default floats are compared with a precision of 1.0E-6 and doubles with 1.0E-15.

	Prefer using withEqualsForFields/withEqualsForType, providing a BiPredicate is simpler than a Comparator (unless you have one already defined).

Examples:

public class TolkienCharacter {
  String name;
  double height;
}

TolkienCharacter frodo = new TolkienCharacter("Frodo", 1.2);
TolkienCharacter tallerFrodo = new TolkienCharacter("Frodo", 1.3);
TolkienCharacter reallyTallFrodo = new TolkienCharacter("Frodo", 1.9);

BiPredicate<Double, Double> closeEnough = (d1, d2) -> Math.abs(d1 - d2) <= 0.5;
// same comparison expressed with a Comparator:
// Comparator<Double> closeEnough = (d1, d2) -> Math.abs(d1 - d2) <= 0.5 ? 0 : 1;

// assertion succeeds
assertThat(frodo).usingRecursiveComparison()
                 .withEqualsForFields(closeEnough, "height")
                 .isEqualTo(tallerFrodo);

assertThat(frodo).usingRecursiveComparison()
                 .withEqualsForType(closeEnough, Double.class)
                 .isEqualTo(tallerFrodo);

// assertions fail
assertThat(frodo).usingRecursiveComparison()
                 .withEqualsForFields(closeEnough, "height")
                 .isEqualTo(reallyTallFrodo);

assertThat(frodo).usingRecursiveComparison()
                 .withEqualsForType(closeEnough, Double.class)
                 .isEqualTo(reallyTallFrodo);
Overriding error messages for specific fields or types

If AssertJ difference error description is not yo your liking, you can override it either by fields or types.

You can override messages for all fields of a given type, example for Double:

withErrorMessageForType("Double field differ", Double.class)

Alternatively can override messages for some specific fields which must be specified from the root object, for example if Foo has a Bar field and both have an id field, one can register a message for Foo and Bar id by calling:

withErrorMessageForFields("id values differ", "foo.id", "foo.bar.id")

Messages registered with withErrorMessageForFields have precedence over the ones registered with withErrorMessageForType.

Example overriding message for a field:

public class TolkienCharacter {
  String name;
  double height;
}

TolkienCharacter frodo = new TolkienCharacter("Frodo", 1.2);
TolkienCharacter tallerFrodo = new TolkienCharacter("Frodon", 1.4);

String message = "The field 'height' differ.";

// assertion fails
assertThat(frodo).usingRecursiveComparison()
                 .withErrorMessageForFields(message, "height")
                 .isEqualTo(tallerFrodo);

and the error will report the height field with the given overridden message instead of the one computed by AssertJ as with the name error:

Expecting actual:
  TolkienCharacter [name=Frodo, height=1.2]
to be equal to:
  TolkienCharacter [name=Frodon, height=1.4]
when recursively comparing field by field, but found the following 2 differences:

The field 'height' differ.

field/property 'name' differ:
- actual value  : "Frodo"
- expected value: "Frodon"

The recursive comparison was performed with this configuration:
- no overridden equals methods were used in the comparison (except for java types)
- these types were compared with the following comparators:
  - java.lang.Double -> DoubleComparator[precision=1.0E-15]
  - java.lang.Float -> FloatComparator[precision=1.0E-6]
  - java.nio.file.Path -> lexicographic comparator (Path natural order)
- actual and expected objects and their fields were compared field by field recursively even if they were not of the same type, this allows for example to compare a Person to a PersonDto (call strictTypeChecking(true) to change that behavior).
- these fields had overridden error messages:
  - height

Example overriding message for a type:

String message = "Double field differ";

// assertion fails
assertThat(frodo).usingRecursiveComparison()
                 .withErrorMessageForType(message, Double.class)
                 .isEqualTo(tallerFrodo);

and the error will report the height field with the given overridden message instead of the one computed by AssertJ as with the name error:

Expecting actual:
  TolkienCharacter [name=Frodo, height=1.2]
to be equal to:
  TolkienCharacter [name=Frodon, height=1.4]
when recursively comparing field by field, but found the following 2 differences:

Double field differ.

field/property 'name' differ:
- actual value  : "Frodo"
- expected value: "Frodon"

The recursive comparison was performed with this configuration:
- no overridden equals methods were used in the comparison (except for java types)
- these types were compared with the following comparators:
  - java.lang.Double -> DoubleComparator[precision=1.0E-15]
  - java.lang.Float -> FloatComparator[precision=1.0E-6]
  - java.nio.file.Path -> lexicographic comparator (Path natural order)
- actual and expected objects and their fields were compared field by field recursively even if they were not of the same type, this allows for example to compare a Person to a PersonDto (call strictTypeChecking(true) to change that behavior).
- these types had overridden error messages:
  - height
Recursive comparison for iterable assertions

usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) enables the recursive comparison for any iterable assertion as opposed to usingRecursiveComparison() which only allows isEqualTo and isNotEqualTo, the main difference between both isEqualTo assertions is that the usingRecursiveComparison one will give a detailed differences report while the usingRecursiveFieldByFieldElementComparator one will give a generic error message without details.

Another difference is that usingRecursiveComparison() exposes a fluent API to tweak the recursive comparison, to achieve the same you will need to initialize a RecursiveComparisonConfiguration and pass it to usingRecursiveFieldByFieldElementComparator, you can take advantage of the RecursiveComparisonConfiguration.builder() to do so.

Example:

public class Person {
  String name;
  boolean hasPhd;
}

public class Doctor {
  String name;
  boolean hasPhd;
}

Doctor drSheldon = new Doctor("Sheldon Cooper", true);
Doctor drLeonard = new Doctor("Leonard Hofstadter", true);
Doctor drRaj = new Doctor("Raj Koothrappali", true);

Person sheldon = new Person("Sheldon Cooper", false);
Person leonard = new Person("Leonard Hofstadter", false);
Person raj = new Person("Raj Koothrappali", false);
Person howard = new Person("Howard Wolowitz", false);

List<Doctor> doctors = list(drSheldon, drLeonard, drRaj);
List<Person> people = list(sheldon, leonard, raj);

RecursiveComparisonConfiguration configuration = RecursiveComparisonConfiguration.builder()
                                                                                 .withIgnoredFields("hasPhd")
                                                                                 .build();

// assertion succeeds as both lists contains equivalent items in order.
assertThat(doctors).usingRecursiveFieldByFieldElementComparator(configuration)
                   .contains(sheldon);

// assertion fails because leonard names are different.
leonard.setName("Leonard Ofstater");
assertThat(doctors).usingRecursiveFieldByFieldElementComparator(configuration)
                   .contains(leonard);

// assertion fails because howard is missing and leonard is not expected.
people = list(howard, sheldon, raj)
assertThat(doctors).usingRecursiveFieldByFieldElementComparator(configuration)
                   .contains(howard);
Specifying how to introspect the objects to compare

Since 3.24.0, you can specify your own strategy telling the recursive comparison how to resolve the values to compare, this is useful if the default strategy does not suit you.

To use your own introspection strategy, you need to:

implement RecursiveComparisonIntrospectionStrategy

call withIntrospectionStrategy(myIntrospectionStrategy) with an instance of your strategy

AssertJ provides a few strategies out of the box:

ComparingFields: introspect fields only (no properties, map keys are not considered as fields)

ComparingProperties: introspect properties only (no fields, map keys are not considered as properties)

ComparingSnakeOrCamelCaseFields: compare fields only, can match camel case fields against snake case ones, ex: firstName vs first_name which is useful when comparing types with different fields naming conventions

ComparingNormalizedFields: an abstract strategy that compares fields after normalizing them, you just need to implement normalizeFieldName(String fieldName)

ComparingSnakeOrCamelCaseFields is an example of ComparingNormalizedFields that normalizes snake case to camel case.

Here’s an example using ComparingSnakeOrCamelCaseFields where we compare Author/Book against AuthorDto/BookDto, Author/Book follow the regular camel case field naming convention while the dto classes follow the snake case naming convention.

The recursive comparison would fail comparing the Author/Book fields against AuthorDto/BookDto ones, it would not know to match Author.firstName against AuthorDto.first_name for example but with ComparingSnakeOrCamelCaseFields it will know how to match these fields.

Example:

Author martinFowler = new Author("Martin", "Fowler", 58, "https://www.thoughtworks.com/profiles/leaders/martin-fowler");
Book refactoring = new Book("Refactoring", martinFowler);
AuthorDto martinFowlerDto = new AuthorDto("Martin", "Fowler", 58, "https://www.thoughtworks.com/profiles/leaders/martin-fowler");
BookDto refactoringDto = new BookDto("Refactoring", martinFowlerDto);

RecursiveComparisonIntrospectionStrategy comparingSnakeOrCamelCaseFields = new ComparingSnakeOrCamelCaseFields();

// both assertions succeed
assertThat(refactoring).usingRecursiveComparison()
                      .withIntrospectionStrategy(comparingSnakeOrCamelCaseFields)
                      .isEqualTo(refactoringDto);
assertThat(refactoringDto).usingRecursiveComparison()
                          .withIntrospectionStrategy(comparingSnakeOrCamelCaseFields)
                          .isEqualTo(refactoring);

static class Author {
  String firstName;
  String lastName;
  int age;
  String profileURL;

  Author(String firstName, String lastName, int age, String profileUrl) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.profileURL = profileUrl;
  }
}

static class Book {
  String title;
  Author mainAuthor;

  Book(String title, Author author) {
    this.title = title;
    this.mainAuthor = author;
  }
}
static class AuthorDto {
  String first_name;
  String last_name;
  int _age;
  String profile_url;

  AuthorDto(String firstName, String lastName, int age, String profileUrl) {
    this.first_name = firstName;
    this.last_name = lastName;
    this._age = age;
    this.profile_url = profileUrl;
  }
}

static class BookDto {
  String title;
  AuthorDto main_author;

  BookDto(String title, AuthorDto author) {
    this.title = title;
    this.main_author = author;
  }
}
2.5.14. Recursive assertions

The recursive assertion allFieldsSatisfy lets you verify a Predicate is met for all the fields of the object under test graph recursively (but not the object itself).

For example if the object under test is an instance of class A, A has a B field and B a C field then allFieldsSatisfy checks A’s B field and B’s C field and all C’s fields.

Example:

class Author {
  String name;
  String email;
  List<Book> books = new ArrayList<>();

  Author(String name, String email) {
    this.name = name;
    this.email = email;
  }
}

class Book {
  String title;
  Author[] authors;

  Book(String title, Author[] authors) {
    this.title = title;
    this.authors = authors;
  }
}

Author pramodSadalage = new Author("Pramod Sadalage", "p.sadalage@recursive.test");
Author martinFowler = new Author("Martin Fowler", "m.fowler@recursive.test");
Author kentBeck = new Author("Kent Beck", "k.beck@recursive.test");

Book noSqlDistilled = new Book("NoSql Distilled", new Author[] {pramodSadalage, martinFowler});
pramodSadalage.books.add(noSqlDistilled);
martinFowler.books.add(noSqlDistilled);

Book refactoring = new Book("Refactoring", new Author[] {martinFowler, kentBeck});
martinFowler.books.add(refactoring);
kentBeck.books.add(refactoring);

// assertion succeeds
assertThat(pramodSadalage).usingRecursiveAssertion()
                          .allFieldsSatisfy(field -> field != null);

The above example is best rewritten with hasNoNullFields() which is common enough that it is supported out of the box.

The recursive assertion provides these methods to exclude fields, the predicate won’t be applied on the excluded fields:

ignoringFields(String…​fieldsToIgnore) - the assertion ignores the specified fields in the object under test

ignoringFieldsMatchingRegexes(String…​regexes) - the assertion ignores the fields matching the specified regexes in the object under test

ignoringFieldsOfTypes(Class<?>…​typesToIgnore) - the assertion ignores the object under test fields of the given types

ignoringPrimitiveFields() - avoid running the assertion on primitive fields

2.5.15. Soft assertions

With soft assertions AssertJ collects all assertion errors instead of stopping at the first one.

	This is especially useful for long tests like end to end tests as we can fix all reported errors at once and avoid multiple failing runs.

Since soft assertions don’t fail at the first error, you need to tell AssertJ when to report the captured assertion errors, there are different ways of doing so:

Calling assertAll() (basic approach)

Using a JUnit 4 rule that takes care of calling assertAll() after each tests

Using the provided JUnit 5 extension which injects a SoftAssertions or a BDDSoftAssertions parameter and calls assertAll() after each tests

Using a AutoCloseableSoftAssertions

Using assertSoftly static method

Soft assertions comes with a BDD flavor where assertThat is replaced by then.

If you have created your own custom Soft assertions it is possible to combine them all in a single soft assertions entry point.

Let’s see first how to use soft assertions requiring an explicit call to assertAll(), the other approaches that don’t require this explicitit call are described in the subsequent sections.

Example:

@Test
void basic_soft_assertions_example() {
  SoftAssertions softly = new SoftAssertions(); 

  softly.assertThat("George Martin").as("great authors").isEqualTo("JRR Tolkien");  
  softly.assertThat(42).as("response to Everything").isGreaterThan(100); 
  softly.assertThat("Gandalf").isEqualTo("Sauron"); 

  // Don't forget to call assertAll() otherwise no assertion errors are reported!
  softly.assertAll(); 
}
	Build a SoftAssertions instance to record all assertion errors
	Use softly.assertThat instead of the usual assertThat methods
	Don’t forget to call assertAll() to report all assertion errors!

The previous test fails with the message below reporting all the errors:

Multiple Failures (3 failures)
-- failure 1 --
[great authors]
Expecting:
 <"George Martin">
to be equal to:
 <"JRR Tolkien">
but was not.
-- failure 2 --
[response to Everything]
Expecting:
 <42>
to be greater than:
 <100>
-- failure 3 --
Expecting:
 <"gandalf">
to be equal to:
 <"sauron">
but was not.
BDD Soft assertions

BDD aficionados can use BDD soft assertions where assertThat is replaced by then.

Example:

@Test
void basic_bdd_soft_assertions_example() {
  BDDSoftAssertions softly = new BDDSoftAssertions(); 

  softly.then("George Martin").as("great authors").isEqualTo("JRR Tolkien");
  softly.then(42).as("response to Everything").isGreaterThan(100);
  softly.then("Gandalf").isEqualTo("Sauron");

  // Don't forget to call assertAll() otherwise no assertion errors are reported!
  softly.assertAll(); 
}

There are BDD soft assertions versions for the different soft assertions approaches:

AutoCloseableBDDSoftAssertions

Using JUnitBDDSoftAssertions that takes care of calling assertAll() after each tests

Using a JUnit 5 extension that takes care of calling assertAll() after each tests

JUnit 4 Soft assertions rule

The JUnit rule provided by AssertJ takes care of calling assertAll() at the end of each tests.

Example:

@Rule
public final JUnitSoftAssertions softly = new JUnitSoftAssertions();

@Test
void junit4_soft_assertions_example() {
  softly.assertThat("George Martin").as("great authors").isEqualTo("JRR Tolkien");  
  softly.assertThat(42).as("response to Everything").isGreaterThan(100); 
  softly.assertThat("Gandalf").isEqualTo("Sauron"); 
  // No need to call softly.assertAll(), this is automatically done by the JUnitSoftAssertions rule
}

In a similar way you can use JUnitBDDSoftAssertions where assertThat is replaced by then:

@Rule
public final JUnitBDDSoftAssertions softly = new JUnitBDDSoftAssertions();

@Test
void junit4_bdd_soft_assertions_example() {
  softly.then("George Martin").as("great authors").isEqualTo("JRR Tolkien");
  softly.then(42).as("response to Everything").isGreaterThan(100);
  softly.then("Gandalf").isEqualTo("Dauron");
  // No need to call softly.assertAll(), this is automatically done by the JUnitSoftAssertions rule
}
JUnit 5 soft assertions extension

SoftAssertionsExtension is a JUnit 5 extension that:

takes care of calling assertAll() at the end of each tests

supports initializing SoftAssertionsProvider field annotated with @InjectSoftAssertions

supports injecting a SoftAssertionsProvider parameter in each test methods

SoftAssertionsProvider is the interface that any concrete soft assertions class must implement, AssertJ provides two of them: SoftAssertions and BDDSoftAssertions, but custom implementations are also supported as long as they have a default constructor. See the end of combining soft assertions entry points section for an example.

	JUnitJupiterSoftAssertions, JUnitJupiterBDDSoftAssertions and SoftlyExtension are now deprecated in favor of SoftAssertionsExtension.
SoftAssertionsProvider field injection

SoftAssertionsExtension supports injecting any instance of SoftAssertionsProvider into a class test field annotated with @InjectSoftAssertions.
The injection occurs before each test method execution, after each test assertAll() is invoked to verify that no soft assertions failed.

A nested test class can provide a SoftAssertionsProvider field when it extends this extension or can inherit the parent’s one.

You can have multiple soft assertion providers injected into a single test class. Assertions made on any of them will be collected in a single error collector and reported all together, in the same order that they failed.

This extension throws an ExtensionConfigurationException if:

the field is static or final or cannot be accessed;

the field type is not a concrete implementation of SoftAssertionsProvider (or subclass); or

the field type has no default constructor.

Example:

import org.assertj.core.api.SoftAssertions;
import org.assertj.core.api.junit.jupiter.SoftAssertionsExtension;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(SoftAssertionsExtension.class)
public class JUnit5SoftAssertionsExtensionAssertionsExamples {

  @InjectSoftAssertions
  private SoftAssertions softly;

  @Test
  public void chained_soft_assertions_example() {
    String name = "Michael Jordan - Bulls";
    softly.assertThat(name).startsWith("Mi")
                           .contains("Bulls");
    // no need to call softly.assertAll(), this is done by the extension
  }

  // nested classes test work too
  @Nested
  class NestedExample {

    @Test
    public void football_assertions_example() {
      String kylian = "Kylian Mbappé";
      softly.assertThat(kylian).startsWith("Ky")
                               .contains("bap");
      // no need to call softly.assertAll(), this is done by the extension
    }
  }
}
SoftAssertionsProvider parameter injection

SoftAssertionsExtension supports injecting any SoftAssertionsProvider implementation as a parameter in any test method.

The term "test method" refers to any method annotated with @Test, @RepeatedTest, @ParameterizedTest, @TestFactory or @TestTemplate. Notably, the extension is compatible with parameterized tests, the parameterized arguments must come first and the soft assertions argument last.

The scope of the SoftAssertionsProvider instance managed by this extension begins when a parameter of type SoftAssertionsProvider is resolved for a test method.
It ends after the test method has been executed, this is when assertAll() will be invoked on the instance to verify that no soft assertions failed.

Parameter injection and field injection can be mixed. Assertions made on the field- and parameter-injected soft assertion providers will all be collected and reported together when the extension calls assertAll().

This extension throws a ParameterResolutionException if the resolved SoftAssertionsProvider :

is abstract; or

has no default constructor.

Example:

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.api.extension.ExtendWith;
import org.assertj.core.api.BDDSoftAssertions;
import org.assertj.core.api.SoftAssertions;
import org.assertj.core.api.junit.jupiter.SoftAssertionsExtension;

@ExtendWith(SoftAssertionsExtension.class)
public class JUnit5SoftAssertionsExample {

  @Test
  void junit5_soft_assertions_multiple_failures_example(SoftAssertions softly) {
    softly.assertThat("George Martin").as("great authors").isEqualTo("JRR Tolkien");
    softly.assertThat(42).as("response to Everything").isGreaterThan(100);
    softly.assertThat("Gandalf").isEqualTo("Sauron");
    // No need to call softly.assertAll(), this is automatically done by the SoftAssertionsExtension
  }

  @Test
  void junit5_bdd_soft_assertions_multiple_failures_example(BDDSoftAssertions softly) {
    softly.then("George Martin").as("great authors").isEqualTo("JRR Tolkien");
    softly.then(42).as("response to Everything").isGreaterThan(100);
    softly.then("Gandalf").isEqualTo("Sauron");
    // No need to call softly.assertAll(), this is automatically done by the SoftAssertionsExtension
  }

  @ParameterizedTest
  @CsvSource({ "1, 1, 2", "1, 2, 3" })
  // test parameters come first, soft assertion must come last.
  void junit5_soft_assertions_parameterized_test_example(int a, int b, int sum, SoftAssertions softly) {
    softly.assertThat(a + b).as("sum").isEqualTo(sum);
    softly.assertThat(a).isLessThan(sum);
    softly.assertThat(b).isLessThan(sum);
  }

}
Auto Closeable Soft assertions

As AutoCloseableSoftAssertions implements AutoCloseable#close() by calling assertAll(), when used in a try-with-resources block assertAll() is called automatically before exiting the block.

Example:

@Test
void auto_closeable_soft_assertions_example() {
  try (AutoCloseableSoftAssertions softly = new AutoCloseableSoftAssertions()) {
  softly.assertThat("George Martin").as("great authors").isEqualTo("JRR Tolkien");  
  softly.assertThat(42).as("response to Everything").isGreaterThan(100); 
  softly.assertThat("Gandalf").isEqualTo("Sauron"); 
    // no need to call assertAll, this is done when softly is closed.
  }
}

In a similar way you can use AutoCloseableBDDSoftAssertions where assertThat is replaced by then:

@Test
void auto_closeable_bdd_soft_assertions_example() {
  try (AutoCloseableBDDSoftAssertions softly = new AutoCloseableBDDSoftAssertions()) {
    softly.then("George Martin").as("great authors").isEqualTo("JRR Tolkien");
    softly.then(42).as("response to Everything").isGreaterThan(100);
    softly.then("Gandalf").isEqualTo("Sauron");
    // no need to call assertAll, this is done when softly is closed.
  }
}
Soft assertions with assertSoftly

The assertSoftly static method takes care of calling assertAll() before exiting.

Example:

@Test
void assertSoftly_example() {
  SoftAssertions.assertSoftly(softly -> {
    softly.assertThat("George Martin").as("great authors").isEqualTo("JRR Tolkien");
    softly.assertThat(42).as("response to Everything").isGreaterThan(100);
    softly.assertThat("Gandalf").isEqualTo("Sauron");
    // no need to call assertAll(), assertSoftly does it for us.
  });
}
Combining soft assertions entry points

Since the 3.16.0 version AssertJ provides a way to combine standard soft assertions with custom ones in a single entry point.

Let’s assume we have written an entry point for TolkienCharacter soft assertions so that we can write assertions like:

TolkienSoftAssertions softly = new TolkienSoftAssertions();
softly.assertThat(frodo).hasRace(HOBBIT)
                        .hasName("Frodo");

If we want to check standard soft assertions we could make TolkienSoftAssertions inherit SoftAssertions but if we want to have GoTSoftAssertions too then we are stuck as Java does not allow multiple inheritance.

The 3.16.0 release introduced the SoftAssertionsProvider interface to define soft assertions entry points.

Step 1
The first step consists in extending this interface to expose as many custom entry points as you need.
The typical custom SoftAssertionsProvider interface exposes default assertThat methods, as shown below:

public interface TolkienSoftAssertionsProvider extends SoftAssertionsProvider {
  // custom assertions
  default TolkienCharacterAssert assertThat(TolkienCharacter actual) {
    return proxy(TolkienCharacterAssert.class, TolkienCharacter.class, actual);
  }
}

// let's add a Game of Thrones entry point
public interface GoTSoftAssertionsProvider extends SoftAssertionsProvider {
  // custom assertions
  default GoTCharacterAssert assertThat(GoTCharacter actual) {
    return proxy(GoTCharacterAssert.class, GoTCharacter.class, actual);
  }
}

Step 2
In order to get a concrete entry point exposing all custom entry points, create a class implementing all custom SoftAssertionsProvider subinterfaces and extending AbstractSoftAssertions. AbstractSoftAssertions provides the core internal implementation to collect all errors from the different implemented entry points (it also implements SoftAssertionsProvider).

To get standard soft assertions, inherit from SoftAssertions instead of AbstractSoftAssertions (or BddSoftAssertions to get the BDD flavor).

Let’s define our concrete entry points implementing both TolkienSoftAssertionsProvider and GoTSoftAssertionsProvider:

// we extend SoftAssertions to get standard soft assertions
public class FantasySoftAssertions extends SoftAssertions
                                   implements TolkienSoftAssertionsProvider, GoTSoftAssertionsProvider {

  // we can even add more assertions here
  public HumanAssert assertThat(Human actual) {
    return proxy(HumanAssert.class, Human.class, actual);
  }
}

Step 3
The last step is to use FantasySoftAssertions:

FantasySoftAssertions softly = new FantasySoftAssertions();

// custom TolkienCharacter assertions
softly.assertThat(frodo).hasRace(HOBBIT);

// custom GoTCharacter assertions
softly.assertThat(nedStark).isDead();

// standard assertions
softly.assertThat("Games of Thrones").startsWith("Games")
                                     .endsWith("Thrones");
// verify assertions
softly.assertAll();

Optional step: create a custom JUnit 4 Rule


Because our custom assertions are defined in an interface, we can also combine them with AssertJ’s JUnit 4 rule so that we can use our custom assertions as a test rule for use in JUnit 4:

// we extend JUnitSoftAssertions to get standard soft assertions classes
public class JUnitFantasySoftAssertions extends JUnitSoftAssertions
                                   implements TolkienSoftAssertionsProvider, GoTSoftAssertionsProvider {}

Then in our test class we use it per normal:

public class JUnit4_StandardAndCustomSoftAssertionsExamples {
  @Rule
  public final JUnitFantasySoftAssertions softly = new JUnitFantasySoftAssertions();

  @Test
  public void successful_junit_soft_custom_assertion_example() {
    softly.assertThat(frodo).hasName("Frodo")
                            .hasAge(33);
    softly.assertThat(frodo.age).isEqualTo(33);
  }
}

The rule will automatically take care of calling assertAll() at the end of every test.

Optional step: use SoftAssertionsExtension


JUnit 5 SoftAssertionsExtension calls softly.assertAll() after each test so that we don’t have to do it manually.
Since 3.16.0 it is capable of injecting any SoftAssertionsProvider, we can then inject our custom FantasySoftAssertions:

@ExtendWith(SoftAssertionsExtension.class)
public class JUnit5_StandardAndCustomSoftAssertionsExamples {

  @Test
  public void successful_junit_soft_custom_assertion_example(FantasySoftAssertions softly) {
    softly.assertThat(frodo).hasName("Frodo")
                            .hasAge(33);
    softly.assertThat(frodo.age).isEqualTo(33);
  }
}
Reacting to collected soft assertions

AssertJ allows to perform an action after an AssertionError is collected.

The action is specified by the AfterAssertionErrorCollected functional interface which can be expressed as lambda, to register your callback call setAfterAssertionErrorCollected as shown below:

Example:

SoftAssertions softly = new SoftAssertions();
StringBuilder reportBuilder = new StringBuilder(format("Assertions report:%n"));

// register our callback
softly.setAfterAssertionErrorCollected(error -> reportBuilder.append(format("------------------%n%s%n", error.getMessage())));
// the AssertionError corresponding to the failing assertions are registered in the report
softly.assertThat("The Beatles").isEqualTo("The Rolling Stones");
softly.assertThat(123).isEqualTo(123)
                      .isEqualTo(456);

resulting reportBuilder:

Assertions report:
------------------
Expecting:
 <"The Beatles">
to be equal to:
 <"The Rolling Stones">
but was not.
------------------
Expecting:
 <123>
to be equal to:
 <456>
but was not.

Alternatively, if you have defined your own SoftAssertions class and inherited from AbstractSoftAssertions, you can instead override onAssertionErrorCollected(AssertionError).

Example:

class TolkienSoftAssertions extends AbstractSoftAssertions {

  public TolkienHeroesAssert assertThat(TolkienHero actual) {
    return proxy(TolkienHeroesAssert.class, TolkienHero.class, actual);
  }

  @Override
  public void onAssertionErrorCollected(AssertionError assertionError) {
    System.out.println(assertionError);
  }
}

TolkienSoftAssertions softly = new TolkienSoftAssertions();

TolkienCharacter frodo = TolkienCharacter.of("Frodo", 33, HOBBIT);

// the AssertionError corresponding to this failing assertion is printed to the console.
softly.assertThat(frodo).hasName("Bilbo");
2.5.16. Assumptions

Assumptions provide support for conditional test execution, if the assumptions are met the test is executed normally, if they don’t the test is aborted and marked as ignored.

Assumptions are typically used whenever it does not make sense to continue execution of a given test method — a typical usage is running tests depending on a given OS/environment.

All AssertJ assumptions are static methods in the Assumptions class, they match the assertion API but are names assumeThat instead of assertThat. You can also get assumptions through the WithAssumptions interface.

Example resulting in the test to be ignored:

@Test
public void when_an_assumption_is_not_met_the_test_is_ignored() {
  // since this assumption is obviously false ...
  assumeThat(frodo.getRace()).isEqualTo(ORC);
  // ... this assertion is not performed
  assertThat(fellowshipOfTheRing).contains(sauron);
}

Example resulting in the test to be executed normally:

@Test
public void when_all_assumptions_are_met_the_test_is_run_normally() {
  // since this assumption is true ...
  assumeThat(frodo.getRace()).isEqualTo(HOBBIT);
  // ... this assertion is performed
  assertThat(fellowshipOfTheRing).doesNotContain(sauron);
}
2.5.17. Javadoc

https://www.javadoc.io/doc/org.assertj/assertj-core/3.27.7 is the latest version of AssertJ Core Javadoc, each assertion is explained, most of them with code examples so be sure to check it if you want to know what a specific assertion does.

2.6. Extending assertions

AssertJ can be extends by Condition or writing your own assertions class.

2.6.1. Conditions

Assertions can be extended by using conditions, to create a condition you just have to implement org.assertj.assertions.core.Condition and its unique method matches.

Once your Condition is created, you can use it with methods: is(myCondition) or has(myCondition), both verifying that the condition is met (hint: pick the one that makes your code more readable).

Example:

// jedi is a Condition
assertThat("Yoda").is(jedi);

Conditions can be combined with :

not(Condition): given condition must not be met

allOf(Condition…​): all given conditions must be met

anyOf(Condition…​): one of the given conditions must be met

You can verify that a Condition is met on elements of a collection, with the following methods:

are(condition)/have(condition): all elements must meet the given condition

areAtLeast(n, condition)/haveAtLeast(n, condition): at least n elements must meet the given condition

areAtMost(n, condition)/haveAtMost(n, condition): no more than n elements must meet the given condition

areExactly(n, condition)/haveExactly(n, condition): exactly n elements must meet the given condition

Moreover all Condition related methods have their negation counterpart, is/isNot, have/doesNotHave, are/areNot, …​

The examples below are from assertj-examples and more specifically UsingConditionExamples.

Creating a Condition

Let’s define two similar conditions: jedi and jediPower with the same implementation to show that code readability is better when using jedi with is and jediPower with has.

import static org.assertj.core.util.Sets.newLinkedHashSet;

static Set<String> JEDIS = newLinkedHashSet("Luke", "Yoda", "Obiwan");

// implementation with Java 8 lambda
Condition<String> jediPower = new Condition<>(JEDIS::contains, "jedi power");

// implementation with Java 7
Condition<String> jedi = new Condition<String>("jedi") {
  @Override
  public boolean matches(String value) {
    return JEDIS.contains(value);
  }
};

The String parameter is describing the condition, this is used in error messages.

Using Conditions

Usage with single instances:

assertThat("Yoda").is(jedi);
assertThat("Vader").isNot(jedi);

assertThat("Yoda").has(jediPower);
assertThat("Solo").doesNotHave(jediPower);

The Condition description is used in error messages, ex:

assertThat("Vader").is(jedi);

will fail with the following error message:

"expecting:<'Vader'> to be:<jedi>"

Usage with collections:

assertThat(list("Luke", "Yoda")).are(jedi);
assertThat(list("Leia", "Solo")).areNot(jedi);

assertThat(list("Luke", "Yoda")).have(jediPower);
assertThat(list("Leia", "Solo")).doNotHave(jediPower);

assertThat(list("Luke", "Yoda", "Leia")).areAtLeast(2, jedi);
assertThat(list("Luke", "Yoda", "Leia")).haveAtLeast(2, jediPower);

assertThat(list("Luke", "Yoda", "Leia")).areAtMost(2, jedi);
assertThat(list("Luke", "Yoda", "Leia")).haveAtMost(2, jediPower);

assertThat(list("Luke", "Yoda", "Leia")).areExactly(2, jedi);
assertThat(list("Luke", "Yoda", "Leia")).haveExactly(2, jediPower);
Combining Conditions

Conditions can be combined with allOf(Condition…​) (logical and) or anyOf(Condition…​) (logical or), not can be used to invert one.

Let’s define a sith condition:

List<String> SITHS = list("Sidious", "Vader", "Plagueis");
Condition<String> sith = new Condition<>(SITHS::contains, "sith");

We can write these assertions:

assertThat("Vader").is(anyOf(jedi, sith));
assertThat("Solo").is(allOf(not(jedi), not(sith)));
2.6.2. Custom Assertions

Creating assertions specific to your own classes is interesting because these assertions will reflect the domain model. It’s a way to use Domain Driven Design ubiquitous language in your tests.

Writing your own assertions is simple: create a class inheriting from AbstractAssert and add your custom assertions methods.

	Add a static method assertThat to provide a handy entry point to your new assertion class.

Sections:

Creating your own assertion class

Providing an entry point for all your custom assertions

Providing an entry point for all your custom assertions and AssertJ ones ?

Enabling soft assertions on your custom assertions

Creating your own assertion class

Let’s see how to do that with an example!

The example is taken from {assertj-examples}/[assertj-examples] and more specifically TolkienCharacterAssert.java.

We want to have assertion for the TolkienCharacter domain model class shown below:

// getter/setter omitted for brevity
public class TolkienCharacter {
  private String name;
  private Race race; // Race is an enum
  private int age;
}

Let’s name our assertion class TolkienCharacterAssert, we make it inherit from AbstractAssert and specify two generic parameters: the first is the class itself (needed for assertion chaining) and the second is the class we want to make assertions on: TolkienCharacter.

Inheriting from AbstractAssert will give you all the basic assertions: isEqualTo, isNull, satisfies, …​

public class TolkienCharacterAssert extends AbstractAssert<TolkienCharacterAssert, TolkienCharacter> { 

  public TolkienCharacterAssert(TolkienCharacter actual) { 
    super(actual, TolkienCharacterAssert.class);
  }

  public static TolkienCharacterAssert assertThat(TolkienCharacter actual) { 
    return new TolkienCharacterAssert(actual);
  }

  public TolkienCharacterAssert hasName(String name) { 
    // check that actual TolkienCharacter we want to make assertions on is not null.
    isNotNull();
    // check assertion logic
    if (!Objects.equals(actual.getName(), name)) {
      failWithMessage("Expected character's name to be <%s> but was <%s>", name, actual.getName());
    }
    // return this to allow chaining other assertion methods
    return this;
  }

  public TolkienCharacterAssert hasAge(int age) { 
    // check that actual TolkienCharacter we want to make assertions on is not null.
    isNotNull();
    // check assertion logic
    if (actual.getAge() != age) {
      failWithMessage("Expected character's age to be <%s> but was <%s>", age, actual.getAge());
    }
    // return this to allow chaining other assertion methods
    return this;
  }
}
	Inherits from AbstractAssert
	Constructor to build your assertion class with the object under test
	An entry point to your specific assertion class to use with static import
	assertions specific to TolkienCharacter
Using our custom assertion class

To use our custom assertion class, simply call the assertThat factory method with the object to test:

// use assertThat from TolkienCharacterAssert to check TolkienCharacter
TolkienCharacterAssert.assertThat(frodo).hasName("Frodo");

// code is more elegant when TolkienCharacterAssert.assertThat is imported statically :
assertThat(frodo).hasName("Frodo");

Well, that was not too difficult, but having to add a static import for each assertThat method of you custom assertion classes is not very handy, it would be better to have a unique assertion entry point. This is what we are going to do in the next section.

Providing an entry point for all custom assertions

Now that you have a bunch of custom assertions classes, you want to access them easily. Just create a CustomAssertions class providing static assertThat methods for each of your assertions classes.

Example:

public class MyProjectAssertions {

  // give access to TolkienCharacter assertion
  public static TolkienCharacterAssert assertThat(TolkienCharacter actual) {
    return new TolkienCharacterAssert(actual);
  }

  // give access to TolkienCharacter Race assertion
  public static RaceAssert assertThat(Race actual) {
    return new RaceAssert(actual);
  }
}

Usage:

import static my.project.MyProjectAssertions.assertThat;
import static org.assertj.core.api.Assertions.assertThat;
...

@Test
public void successful_custom_assertion_example() {
  // assertThat(TolkienCharacter) comes from my.project.MyProjectAssertions.assertThat
  assertThat(frodo).hasName("Frodo");

  // assertThat(String) comes from org.assertj.core.api.Assertions.assertThat
  assertThat("frodo").contains("do");
}
	You could also make your custom Assertions entry point class inherit AssertJ’s Assertions, that will work fine if and only if you have one entry point class for your custom assertions classes!

The problem with several entry point classes inheriting from AssertJ Assertions, then when you use them Java won’t be able to resolve which assertThat(String) method to use. The following code illustrates the issue:

// both MyAssertions and MyOtherAssertions inherit from org.assertj.core.api.Assertions
import static my.project.MyAssertions.assertThat;
import static my.project.MyOtherAssertions.assertThat;
...

@Test
public void ambiguous_assertThat_resolution() {
  // ERROR: assertThat(String) is ambiguous!
  // assertThat(String) is available from MyAssertions AND MyOtherAssertions
  // (it is defined in Assertions the class both MyAssertions and MyOtherAssertions inherits from)
  assertThat("frodo").contains("do");
}
2.7. Migrating assertions

This page will help you convert your existing JUnit assertions to AssertJ ones. Note that both types of assertions can coexist, you don’t have to migrate all at once.

The idea is to convert code like:

assertEquals(expected, actual);

to:

assertThat(actual).isEqualTo(expected);

There are several ways to perform the conversion :

Automatically, with the provided migration scripts.

Automatically, with OpenRewrite.

Manually, with the regexes described in this section.

With IntelliJ IDEA, using these plugins:

Assertions2Assertj plugin.

Concise AssertJ Optimizing Nitpicker (Cajon) plugin.

With IntelliJ IDEA, using the Structural Search and Replace (SSR) feature.

The preferred approach is to use the provided migration scripts or OpenRewrite recipes as they are type safe and cover more assertions than the other ones.

2.7.1. Migration Scripts

It is as simple as running one of the following scripts depending on which test framework you are using:

JUnit 3/4 to AssertJ migration script

JUnit 5 to AssertJ migration script

TestNG to AssertJ migration script

Each shell script is based on the sed stream editor and regexps. It recursively looks at all *Test.java files and performs search and replace to convert assertions to AssertJ ones.

The script handles the cases where you use an assertion description, for example:

assertEquals("test context", "a", "a");

will be replaced by:

assertThat("a").as("test context").isEqualTo("a");

Note that the script does a best effort and some assertions might not be converted if formatted on multiple lines. Anyway the script usually migrates the vast majority of assertions.

The script works on Windows within a bash console like git bash (tested a long time ago) or cygwin (not tested).

Usage

Execute the script in the base directory containing the test files:

cd ./src/test/java
./convert-junit-assertions-to-assertj.sh

If the *Test.java file pattern does not suit you, just specify another as an argument:

# enclose your pattern with double quotes "" to avoid it to be expanded by your shell prematurely
./convert-junit-assertions-to-assertj.sh "*IT.java"

After executing it, you will need to :

Optimize imports with your IDE to remove unused imports.

If you were using assertEquals with a delta to compare numbers, you will need to statically import org.assertj.core.api.Assertions.within which is how you express deltas in AssertJ (see the number_assertions_with_offset_examples() test at the end of NumberAssertionsExamples).

Script output
Converting JUnit assertions to AssertJ assertions on files matching pattern : *Test.java

 1 - Replacing : assertEquals(0, myList.size()) ............... by : assertThat(myList).isEmpty()
 2 - Replacing : assertEquals(expectedSize, myList.size()) .... by : assertThat(myList).hasSize(expectedSize)
 3 - Replacing : assertEquals(expectedDouble, actual, delta) .. by : assertThat(actual).isCloseTo(expectedDouble, within(delta))
 4 - Replacing : assertEquals(expected, actual) ............... by : assertThat(actual).isEqualTo(expected)
 5 - Replacing : assertArrayEquals(expectedArray, actual) ..... by : assertThat(actual).isEqualTo(expectedArray)
 6 - Replacing : assertNull(actual) ........................... by : assertThat(actual).isNull()
 7 - Replacing : assertNotNull(actual) ........................ by : assertThat(actual).isNotNull()
 8 - Replacing : assertTrue(logicalCondition) ................. by : assertThat(logicalCondition).isTrue()
 9 - Replacing : assertFalse(logicalCondition) ................ by : assertThat(logicalCondition).isFalse()
10 - Replacing : assertSame(expected, actual) ................. by : assertThat(actual).isSameAs(expected)
11 - Replacing : assertNotSame(expected, actual) .............. by : assertThat(actual).isNotSameAs(expected)

Replacing JUnit static imports by AssertJ ones, at this point you will probably need to :
12 --- optimize imports with your IDE to remove unused imports
12 --- add "import static org.assertj.core.api.Assertions.within;" if you were using JUnit number assertions with deltas
2.7.2. OpenRewrite

OpenRewrite, a large-scale automated source code refactoring tool, offers a couple of recipes that assist with the migration to AssertJ:

The Migrate Hamcrest to AssertJ assertions recipe will:

Migrate various Hamcrest Matchers to AssertJ (e.g., changing equalTo to isEqualTo or changing !emptyString to isNotEmpty)

Migrate the Hamcrest is(Object) method to AssertJ

Remove the Hamcrest is(Matcher) method

Add Gradle or Maven dependencies as needed

If you want to go even further, you can run the AssertJ best practices recipe which will do all of the above plus:

Migrate JUnit to AssertJ (e.g., changing assertEquals() to assertThat().isEqualTo())

Simplify AssertJ chained assertions (e.g., assertThat(foo.size()).isEqualTo(1) would change to assertThat(foo).hasSize(1))

Statically import AssertJ’s assertThat (rather than inlining the Assertions class name in tests)

To learn more about how to run these recipes, please see the OpenRewrite Gradle or OpenRewrite Maven instructions.

2.7.3. Migration Regexes

Here’s a list of find/replace expressions to change JUnit assertions into AssertJ assertions (don’t forget to check the regex mode in your editor replace window).

These regexes described in this section are specific to JUnit 4, but you can easily adapt them for JUnit 5 or TestNG.

The order of find/replace is important to benefit from the most relevant AssertJ assertions. For example, you should convert assertEquals(0, myList.size()) to assertThat(myList).isEmpty() instead of assertThat(myList.size()).isEqualTo(0).

Converting assertEquals(0, myList.size()) to assertThat(myList).isEmpty()

Find/replace regex:

assertEquals\(0,(.*).size\(\)\); -> assertThat(\1).isEmpty();

It’s better to run this before the assertEquals → isEqualTo conversion to avoid ending with assertThat(myList.size()).isEqualTo(0).

Converting assertEquals(size, myList.size()) to assertThat(myList).hasSize(size)

Find/replace regex:

assertEquals\((.*),(.*).size\(\)\); -> assertThat(\2).hasSize(\1);

It’s better to run this before the assertEquals → isEqualTo conversion to avoid ending with assertThat(myList.size()).isEqualTo(expectedSize).

Converting assertEquals(expected, actual) to assertThat(actual).isEqualTo(expected)

Find/replace regex:

assertEquals\((.*),(.*)\); -> assertThat(\2).isEqualTo(\1);
Converting assertNull(objectUnderTest) to assertThat(objectUnderTest).isNull()

Find/replace regex:

assertNull\((.*)\); -> assertThat(\1).isNull();
Converting assertNotNull(objectUnderTest) to assertThat(objectUnderTest).isNotNull()

Find/replace regex:

assertNotNull\((.*)\); -> assertThat(\1).isNotNull();
Converting assertFalse(logicalCondition) to assertThat(logicalCondition).isFalse()

Find/replace regex:

assertFalse\((.*)\); -> assertThat(\1).isFalse();
2.8. AssertJ Sample Projects

The assertions-examples repository hosts executable AssertJ assertions examples that you can run as JUnit tests. Please have a look at assertions examples sources.

The main branch contains examples with the latest released version of AssertJ modules for Java 8, similarly the java-7 branch contains examples of AssertJ modules for Java 7. You should be able to build those two branches with mvn clean install command.

In your IDE, add src/test/generated-assertions to the project java test sources otherwise you will have errors/missing classes. This is the folder where custom assertions classes are generated by default by the maven assertions generator plugin. Note that Intellij Idea wrongly adds src/test/generated-assertions to the production sources when it should be added the test sources, you will have to fix that in your module/project settings.

Building the with-latest-snapshot-versions branch is a bit more complicated :

you need to build the needed SNAPSHOT dependencies before - most probably assertj-core and maybe other modules.

run mvn clean install in assertj-examples/assertions-examples.

In your IDE, add src/test/generated-assertions to the project java sources if you IDE shows errors/missing classes.

2.9. Release Notes
	AssertJ Core would not exist without its contributors, you can find them all directly on GitHub.

The latest release notes can be found in the GitHub releases.

Older release notes:

AssertJ Core 3.23.0

AssertJ Core 3.22.0

AssertJ Core 3.21.0

AssertJ Core 3.20.2

AssertJ Core 3.20.1

AssertJ Core 3.20.0

AssertJ Core 3.19.0

AssertJ Core 3.18.1

AssertJ Core 3.18.0

AssertJ Core 3.17.2

AssertJ Core 3.17.1

AssertJ Core 3.17.0

AssertJ Core 3.16.1

AssertJ Core 3.16.0

AssertJ Core 3.15.0

AssertJ Core 3.14.0

AssertJ Core 3.13.2

AssertJ Core 3.13.1

AssertJ Core 3.13.0

AssertJ Core 3.12.2

AssertJ Core 3.12.1

AssertJ Core 3.12.0

Even older release notes can be found in the old site: https://joel-costigliola.github.io/assertj/assertj-core-news.html, this is important to be aware of breaking changes if you are migrating from an old version.

2.9.1. AssertJ Core 3.23.0

Release date: 2022-05-31

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, BJ Hargrave, Jeremy Landis, Ashley Scopes, Roland Weisleder , Benedikt Bogason , Andreas Kutschera , Matthew , Chris HeZean , Leo0506 , Zhou Yicheng , Saria , Chunhao Liao , maxwell142857 , Jessica Hamilton , nith2001 , Arman Sharif , Yuta Saito , Minami Yoshihiko , Martin Witt , Wojciech Zankowski , Gatien Bovyn , Flora Zheng , Natalia Struharova , Sára Juhošová , Pawel , Diego Krupitza , Jiashu Zhang , YeeTone Wang , Yitong , Anugrah Singhal , Stefan Bratanov , and Almir James Lucena .

 Binary compatibility

The release is binary compatible with the previous minor version.

 New features

Add hasYear, hasMonth, hasMonthValue and hasDayOfMonth LocalDate assertions (#2541). (Jessica Hamilton and nith2001)

Add hasHour, hasMinute, hasSecond and hasNano LocalTime assertions (#2541). (Saria, Chunhao Liao, Jessica Hamilton and maxwell142857)

Add hasYear, hasMonth, hasMonthValue, hasDayOfMonth, hasHour, hasMinute, hasSecond and hasNano LocalDateTime assertions (#2541). (Leo0506, Chris HeZean, Chunhao Liao, Zhou Yicheng, Yitong and Matthew)

Add ignoring case variants of startsWith, endsWith, doesNotStartWith, and doesNotEndWith to CharSequence assertions. (Benedikt Bogason)

Add linesOf variants to load a Path content. (#2618). (Stefan Bratanov)

Add hasFileSystem and hasSameFileSystemAs Path assertions. (Ashley Scopes)

Add binaryContent Path and File assertions. (Ashley Scopes)

Add more assertThat…​Exception alternatives (#2454). (Minami Yoshihiko)

Add isStatic/isNotStatic class assertions (#2455). (Wojciech Zankowski)

Add containsIgnoringNewLines String assertion. (Flora Zheng)

Add BigDecimal scale assertion. (Almir James Lucena)

Add assertThatExceptionOfType/thenExceptionOfType to Soft/BDDSoft assertions.

Add java.util.regex.Matcher assertions class with matches assertion. (Jiashu Zhang)

Add hasNumberOfRows to two-dimensional array assertions. (Wojciech Zankowski)

Sync assumptions and assertions methods. (Wojciech Zankowski)

Expose ComparisonStrategy::areEqual in AbstractAssert. (Stefano Cordio)

 Improvements

Improved containsExactly performance from O(n2) to O(n) when the assertion succeeds (#2548). (nith2001, Sára Juhošová)

Display first stack trace elements of failures in AssertJMultipleFailuresError to ease code navigation.

Add assertThat{Interface}/then{Interface} methods like assertThatIterable to address potential ambiguous resolution.

Replace for loop with enhanced for loop (#2501). (Diego Krupitza)

Remove unnecessary unboxing in ComparatorFactory (#2502). (Diego Krupitza)

Update MapEntry::hashCode to honor Map.Entry::hashCode contract (#2503). (BJ Hargrave)

Use AbstractComparableAssert as parent class for URI assertions. (Pawel)

Avoid ValueNode being considered as iterable while using recursive comparison. (Gatien Bovyn)

Improve Float/Double isCloseTo assertions and comparators to honor offset check exactly. (YeeTone Wang)

Improve recursive comparison error when comparing unordered iterables by show expected elements not found in actual instead of unmatched actual elements.

Keep assertion state with getCause and getRootCause. (Stefano Cordio)

Improve compatibility of assertThatComparable (#2532). (Stefano Cordio)

Increase test coverage for internal and api package (#2543). (Natalia Struharova)

Increase AbstractIntegerAssert test coverage to 100% (#2515). (Sára Juhošová)

Add more tests for ShortAssert, FloatAssert, BigDecimalAssert, DoubleAssert, IntegerAssert, ShortArrayAssert, IntArrayAssert, IteratorAssert, OptionalAssert, PathAssert and InputStreamAssert. (Sára Juhošová)

Throw AssertionError with extracting(String) if actual is null. (Stefano Cordio)

Keep assertion state with content assertions for File and Path. (Stefano Cordio)

Skip well-known JDK types in AbstractCollectionAssert::isUnmodifiable (#2599). (Stefano Cordio)

Remove Byte Buddy shading (#2477). (Stefano Cordio)

Avoid cloning MultiValueMapAdapter instances (#2549). (Stefano Cordio)

Javadoc improvements. (Stefano Cordio)

Fix typos in Javadoc of ObjectEnumerableAssert (#2624). (Roland Weisleder)

Internal: Update maven wrapper to 3.1.1 (#2622). (Jeremy Landis)

Internal: Bump maven wrapper distributionUrl to 3.8.5 (#2551). (Jeremy Landis)

Internal: Align Javadoc stylesheet to be compatible with Java 17. (Stefano Cordio)

Internal: Add Gitpod configuration. (Stefano Cordio)

Internal: Open user specific fork on Gitpod. (Anugrah Singhal)

Internal: Verify binary compatibility with latest release also with PRs (#2613). (Stefano Cordio)

Internal: Change visibility of constructor in final util class to private (#2465). (Martin Witt)

Internal: Update license headers to 2022. (Stefano Cordio)

Internal: Add build with Java 19 EA. (Stefano Cordio)

Internal: Add binary compatibility result to job summary. (Stefano Cordio)

Internal: Use Java 18 GA in build (Stefano Cordio)

Internal: Use Java 17 in workflows (#2584) (Stefano Cordio)

Internal: Fix Maven Central badge. (Stefano Cordio)

Internal: Add navigation method tests to extracting variants. (Stefano Cordio)

Internal: Apply binary incompatible label to PRs (#2478). (Stefano Cordio)

Internal: Refactor test verifying that Assertions, BDDAssertions, WithAssertions and soft assertions are in sync.

Internal: Bump Bnd version to 6.2.0. (BJ Hargrave)

Internal: Bump spring-core from 5.3.14 to 5.3.20

Internal: Bump jboss-logging from 3.4.2.Final to 3.5.0.Final

Internal: Bump byte-buddy.version from 1.12.6 to 1.12.10

Internal: Bump github/codeql-action from 1 to 2

Internal: Bump pitest-maven from 1.7.5 to 1.8.0

Internal: Bump equalsverifier from 3.7.1 to 3.10

Internal: Bump parent POM to version 2.2.14 (Stefano Cordio)

Internal: Bump Mockito to version 4.5.1 (Stefano Cordio, Erhard Pointl)

Internal: Bump jacoco-maven-plugin.version from 0.8.7 to 0.8.8 (Erhard Pointl)

Internal: Bump hibernate-core from 6.0.0.Beta3 to 6.0.2.Final

Internal: Bump japicmp-maven-plugin from 0.15.4 to 0.15.7

Internal: Bump pitest-maven from 1.7.3 to 1.7.5

Internal: Bump actions/github-script from 5 to 6

Internal: Bump actions/checkout from 2 to 3 (Stefano Cordio)

Internal: Bump actions/upload-artifact from 2 to 3 (Stefano Cordio)

Internal: Bump actions/setup from 2 to 3

Internal: Bump guava from 31.0.1-jre to 31.1-jre

Internal: Bump jackson-databind from 2.13.1 to 2.13.3

Internal: Bump org.eclipse.osgi from 3.17.100 to 3.17.200

Internal: Bump cdg.pitest.version from 0.1.0 to 0.2.0

Internal: Bump pitest-github-maven-plugin from 0.1.0 to 0.1.3

Internal: Bump github/codeql-action from 1 to 2

Internal: Bump maven-invoker-plugin from 3.2.2 to 3.3.0

 Fixed

Update docs describing passing Fail.fail() as a lambda (#2512). (Arman Sharif)

Fix recursive comparison that can throw IllegalStateException when comparing Maps

Recursive comparison did not honor comparingOnlyFields when getting actual fields to compare (#2610). (Andreas Kutschera)

Fix comparingOnlyFields that was greedily evaluating fields to compare.

Fix usingRecursiveComparison with usingOverriddenEquals ignores equals method of the root object (#2479). (Yuta Saito)

Fix error in Javadoc. (Yuta Saito)

As Java 17 forbids it, don’t use reflection to compare java types in the recursive comparison, use equals even if not overridden (#2450).

Recursive comparison: Compare Atomic types embedded value recursively (value is not accessed by reflection) (#2466).

Fix pom url to match the actual url to the doc (#2514). (BJ Hargrave)

Fix file names to prevent MacOS casing issues (#2534). (Sára Juhošová)

Disable setup-java cache to fix some cache corruption. (Stefano Cordio)

Fix ShouldBeSame error message that inverted actual and expected (#2565). (Stefano Cordio)

Fix Sonar bug. (Stefano Cordio)

 Deprecated

Deprecate getCause and getRootCause for Throwable assertions

Add more assertThat…​Exception alternatives

Add more ThrowableTypeAssert entry point methods for commonly used exception:

assertThatException

assertThatRuntimeException

assertThatReflectiveOperationException

assertThatIndexOutOfBoundsException

This allow to check that piece of code expressed as a ThrowingCallable throws the proper exception type and chain additional assertions.

Example:

// succeeds
assertThatRuntimeException().isThrownBy(() -> {
  throw new RuntimeException("boom");
}).withMessage("boom");

// fails
assertThatRuntimeException().isThrownBy(() -> {
  throw new IOException();
})

Add linesOf variants to load a Path content

Loads the text content of a file at a given path into a list of strings with the given charset or the default charset if none is specified.

Each string corresponding to a line, the line endings are either \n, \r or \r\n.

Example:

// Terry-Pratchett.txt content:
// I'll be more enthusiastic about encouraging thinking outside the box ...
// ...when there's evidence of any thinking going on inside it.
Path pratchettQuotePath = Paths.get("Terry-Pratchett.txt");

assertThat(linesOf(pratchettQuotePath)).contains("I'll be more enthusiastic about encouraging thinking outside the box ...",
                                                 "...when there's evidence of any thinking going on inside it");

Add isStatic/isNotStatic class assertions

Add assertions to verify whether a class is static or not.

Example:

class MyClass {
  static class MyStaticClass {}
}

assertThat(MyClass.class).isNotStatic();
assertThat(MyStaticClass.class).isStatic();

Add containsIgnoringNewLines string assertion

Verifies that the {@code CharSequence} under test contains all the given values ignoring new line differences.

Example:

assertThat("Gandalf\nthe\ngrey").containsIgnoringNewLines("alf")
                                .containsIgnoringNewLines("alf", "grey")
                                .containsIgnoringNewLines("thegrey")
                                .containsIgnoringNewLines("thegr\ney")
                                .containsIgnoringNewLines("t\nh\ne\ng\nr\ney");

Add BigDecimal scale assertion

Returns an assert object that allows performing assertions on the scale of the BigDecimal under test.

Once this method is called, the object under test is no longer the BigDecimal but its scale. To go back performing assertions on the BigDecimal, call returnToBigDecimal().

Example:

assertThat(new BigDecimal("3.14")).scale()
                                    .isGreaterThan(1L)
                                    .isLessThan(5L)
                                  .returnToBigDecimal()
                                    .isPositive();

Add java.util.regex.Matcher assertions class with matches assertion

Verifies that the java.util.regex.Matcher matches.

Example:

Pattern pattern = Pattern.compile("a*");
Matcher matcher = pattern.matcher("aaa");
assertThat(matcher).matches();

Add hasNumberOfRows to two-dimensional array assertions

Verifies that the actual two-dimensional array has the given number of rows.

Example:

assertThat(new int[][] {{1, 2, 3}, {4, 5, 6}}).hasNumberOfRows(2);
assertThat(new long[][] {{1}, {1, 2}, {1, 2, 3}}).hasNumberOfRows(3);

Add hasYear, hasMonth, hasMonthValue and hasDayOfMonth LocalDate assertions

Verifies that actual LocalDate is in the given year, month/monthValue or day of month.

Example:

assertThat(LocalDate.of(2000, 12, 31)).hasYear(2000)
                                      .hasMonth(Month.DECEMBER)
                                      .hasMonthValue(12)
                                      .hasDayOfMonth(31);

Add hasHour, hasMinute, hasSecond and hasNano LocalTime assertions

Verifies that actual LocalTime is in the given hour, minute, second or nano.

Example:

assertThat(LocalTime.of(23, 17, 59, 05)).hasHour(23)
                                        .hasMinute(17)
                                        .hasSecond(59)
                                        .hasNano(05);

Add hasYear, hasMonth, hasMonthValue, hasDayOfMonth, hasHour, hasMinute, hasSecond and hasNano LocalDateTime assertions

Verifies that actual LocalDateTime is in the given year, month/monthValue, day of month, hour, minute, second or nano.

Example:

assertThat(LocalDateTime.of(2000, 12, 31, 23, 17, 59, 05)).hasYear(2000)
                                                         .hasMonth(Month.DECEMBER)
                                                         .hasMonthValue(12)
                                                         .hasDayOfMonth(31)
                                                         .hasHour(23)
                                                         .hasMinute(17)
                                                         .hasSecond(59)
                                                         .hasNano(05);

Add hasFileSystem and hasSameFileSystemAs Path assertions

Verifies that a path has the given file system or the same file system as another path

Examples:

Path jarFile = Paths.get("assertj-core.jar");
FileSystem mainFileSystem = jarFile.getFileSystem();

try (FileSystem fs = FileSystems.newFileSystem(jarFile, (ClassLoader) null)) {
  Path manifestFile = fs.getPath("META-INF", "MANIFEST.MF");

  assertThat(manifestFile).hasFileSystem(fs)
                          .hasSameFileSystemAs(jarFile);
}

Add binaryContent Path/File assertions

Returns ByteArray assertions on the content of the Path/File read.

Examples:

Path xFilePath = Files.write(Paths.get("xfile.txt"), "The Truth Is Out There".getBytes());
File xFile = xFilePath.toFile();

byte[] expectedBinaryContent = "The Truth Is Out There".getBytes()
assertThat(xFilePath).binaryContent().isEqualTo(expectedBinaryContent);
assertThat(xFile).binaryContent().isEqualTo(expectedBinaryContent);

Add ignoring case variants of startsWith, endsWith, doesNotStartWith, and doesNotEndWith CharSequence assertions

Add startsWithIgnoringCase, endsWithIgnoringCase, doesNotStartWithIgnoringCase and doesNotEndWithIgnoringCase to CharSequence assertions.

Examples:

assertThat("Gandalf the grey").startsWithIgnoringCase("gandalf")
                              .startsWithIgnoringCase("Gandalf")
                              .doesNotStartWithIgnoringCase("Saroumane")
                              .endsWithIgnoringCase("Grey")
                              .endsWithIgnoringCase("grey")
                              .doesNotEndWithIgnoringCase("great");
2.9.2. AssertJ Core 3.22.0

Release date: 2022-01-03

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Yusuke Mukai , Martin Tarjányi , Trang Nguyen , jbock , Annette0127, Zihan Xu , Ashley Scopes , Benjamin Ze’ev Tels , Ahmad Sadeed , temp-droid , Ilya Koshaleu , Spacca , Erik Pragt , and Jeremy Landis.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Breaking change: extracting now throws an assertion error if actual is null (Fixes #2401).

Breaking change: extracting/map for iterables now throws an assertion error if the actual Iterable is null (Fixes #2411).

Breaking change: flatExtracting/flatMap for iterables now throws an assertion error if the actual Iterable is null (Fixes #2412).

 New features

Add size assertions for File (#2322). (Erik Pragt)

Add message() navigation method for Throwable (#2378). (Trang Nguyen)

Add support for fine-grained representations (#2048). (Annette0127)

Add singleElement to Object[] assertions (#2320).

Add hasNoHost to URI and URL assertions (#2436). (Ashley Scopes)

Allow overriding error messages for specific fields and types in the recursive comparison. (Ilya Koshaleu)

Add catchThrowableOfType alternatives for commonly used exceptions (#2397). (Spacca)

Add doesNotReturn to Object assertions (#2453). (Stefano Cordio)

 Improvements

Treat class cast exception as comparison failure in the recursive comparison. (#2434)

Improve Class representation for anonymous and local types (#2445). (Stefano Cordio)

Return null when extracting the value of an empty Optional (#2372). (Stefano Cordio)

Assumptions: avoid proxying methods that don’t need to be proxied.

Accept vararg for AbstractAssert.satisfies. (Martin Tarjányi)

Print offending token in error message from containsSubsequence. (jbock)

extracting now throws an assertion error if actual is null (Fixes #2401). (Trang Nguyen)

extracting/map for iterables now throws an assertion error if the actual Iterable is null (Fixes #2411). (Trang Nguyen)

flatExtracting/flatMap for iterables now throws an assertion error if the actual Iterable is null (Fixes #2412). (Zihan Xu)

Allow checking of null keys and values with maps that do not allow them (see #2379 and #2382). (Benjamin Ze’ev Tels, Stefano Cordio)

Better isEqualTo error messages when values are multi lined (#2366). (temp-droid)

Javadoc improvements. (Stefano Cordio)

Internal: Avoid mocks for testing File assertions (#2337). (Ahmad Sadeed)

Internal: Align assertContainsKeys and assertDoesNotContainKeys testing to the pattern introduced in #2167. (Stefano Cordio)

Internal: Add JDK 9 collection factories (#2386). (Stefano Cordio)

Internal: Add release workflow (#1986). (Stefano Cordio)

Internal: Add additional test cases to isUnmodifiable. (Stefano Cordio)

Internal: Exclude Guava transitive dependency from EqualsVerifier. (Stefano Cordio)

Internal: Bump junit-jupiter.version from 5.8.0 to 5.8.2 (Erhard Pointl)

Internal: Bump mockito.version from 3.12.4 to 4.2.0 (Erhard Pointl, Stefano Cordio)

Internal: Bump jackson-databind from 2.12.5 to 2.13.1

Internal: Bump byte-buddy.version from 1.11.6 to 1.12.6

Internal: Bump guava from 30.1.1-jre to 31.0.1-jre

Internal: Bump assertj-parent-pom from 2.2.13 to 2.2.14

Internal: Bump pitest-maven from 1.7.0 to 1.7.3

Internal: Bump bnd.version from 5.3.0 to 6.1.0

Internal: Bump japicmp-maven-plugin from 0.15.3 to 0.15.4

Internal: Bump Maven version from 3.8.2 to 3.8.4 (Erhard Pointl)

Internal: Bump spring-core from 5.3.10 to 5.3.14

Internal: Bump equalsverifier from 3.7.1 to 3.8.1

Internal: Bump org.eclipse.osgi from 3.17.0 to 3.17.100

Internal: Switch to the official Maven Wrapper by Apache (#2452). (Jeremy Landis)

 Fixed

Avoid reflection when extracting Optional value that fails with Java 17 (#2364). (Stefano Cordio)

Fix assumptions for extracting methods using asInstanceOf

Fix Javadoc for containsExactlyInAnyOrderElementsOf (#2405). (Yusuke Mukai)

Fix DefaultAssertionErrorCollector that dismisses expected/actual fields during injection of line numbers.

Fall back to Map copy when cloning causes any RuntimeException (#2448). (Stefano Cordio)

 Deprecated

Deprecate encodedAsBase64 / decodedAsBase64 in favor of asBase64Encoded / asBase64Decoded

Add size assertions for File

Returns an Assert object that allows performing assertions on the size of the File under test.

Once this method is called, the object under test is no longer the File but its size, to return performing assertions on the File, call returnToFile().

Example:

File file = File.createTempFile("tmp", "bin");
Files.write(file.toPath(), new byte[] {1, 1});

assertThat(file).size()
                  .isGreaterThan(1L)
                  .isLessThan(5L)
                .returnToFile()
                  .hasBinaryContent(new byte[] {1, 1});

Add message() navigation method for Throwable

A shortcut for extracting(Throwable::getMessage, as(InstanceOfAssertFactories.STRING)) which allows to extract a throwable’s message and then execute assertions on it.

Note that once you have navigated to the throwable’s message you can’t navigate back to the throwable.

Example:

Throwable throwable = new Throwable("boom!");

assertThat(throwable).message().startsWith("boo")
                               .endsWith("!");

Add singleElement for Object[] assertions

Verifies that the array under test contains a single element and allows performing assertions on that element.

The assertions can be strongly typed if given an AssertFactory parameter.

Example:

String[] babySimpsons = { "Maggie" };

// object assertions
assertThat(babySimpsons).singleElement()
                        .isEqualTo("Maggie");

// strongly typed assertions with a predefined AssertFactory
import static org.assertj.core.api.Assertions.as; // syntactic sugar
import static org.assertj.core.api.InstanceOfAssertFactories.STRING;

assertThat(babySimpsons).singleElement(as(STRING))
                        .startsWith("Mag");

Add hasNoHost to URI and URL assertions

Verifies that the actual URI/URL has no host.

Example:

assertThat(new URI("file:///home/user/Documents/hello-world.txt")).hasNoHost();
assertThat(new URL("file:///home/user/Documents/hello-world.txt")).hasNoHost();

Add doesNotReturn to Object assertions

Verifies that the object under test does not return the given expected value from the given Function, a typical usage is to pass a method reference to assert object’s property.

Wrapping the given Function with Assertions.from(Function) makes the assertion more readable.

Example:

// from is not mandatory but it makes the assertions more readable
assertThat(frodo).doesNotReturn("Bilbo", from(TolkienCharacter::getName))
                 .doesNotReturn("Bilbo", TolkienCharacter::getName) // no from :(
                 .doesNotReturn(null, from(TolkienCharacter::getRace));
2.9.3. AssertJ Core 3.21.0

Release date: 2021-09-20

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Shivakumar Swamy, Iván Aguilar, Alberto Pascual, Gily H, Stefan Bischof, RGalways17, Andrey Kuzmin, Eugene Lesnov, Szymon Linowski, Julian Honnen, Almir James Lucena and Golan Levy.

 Binary compatibility

The release is binary compatible with the previous minor version.

 Breaking changes

Custom comparison now takes precedence over reference comparison in recursive comparison (Fixes #2335).

 New features

Add content()/content(Charset) to Path assertions to allow chaining string assertions on the Path content. (#2252)

Add content()/content(Charset) to File assertions to allow chaining string assertions on the File content. (#2243)

Add hasSize(long expectedSizeInBytes) to Path assertions (#2198). (Gily-H)

Add isMixedCase() to CharSequence assertions (#2246). (Andrey Kuzmin)

Add containsAnyOf(CharSequence…​ values) to CharSequence assertions (#2309). (Eugene Lesnov)

Add hasExtension(String extension) to Path assertions (#2255). (Szymon Linowski)

Add hasNoExtension() to Path assertions (#2318). (Szymon Linowski)

Add hasNoExtension() to File assertions.

Add hasScaleOf(int expectedScale) to BigDecimals assertions (#2321). (Almir James Lucena)

Add isUnmodifiable() to Collection assertions (#2328). (Stefano Cordio)

 Improvements

Add CollectionAssert hierarchy (#2315). (Stefano Cordio)

Change AssertJ MapEntry and Java Map.Entry representation to be key=value.

Improve containsEntry and containsAllEntriesOf error message when keys match but not values.

Improve assertion error for hasSameElementsAs(emptyList()). (RGalways17)

Add stack trace information of Throwable that fails hasCauseInstanceOf or hasCauseExactlyInstanceOf (#2209). (RGalways17)

Add isReadable as an alias of canRead for File assertions (#2249). (Alberto Pascual)

Add isWritable as an alias of canWrite for File assertions (#2273). (Iván Aguilar)

Add hasFileName as an alias of hasName for File assertions (#2247). (Shivakumar Swamy)

Add satisfies with ThrowingConsumer to accept consumers that throw checked exceptions (#2297).

Add satisfiesAnyOf with ThrowingConsumer to accept consumers that throw checked exceptions.

Add allSatisfy, anySatisfy, satisfiesExactly, noneSatisfy, satisfiesExactlyInAnyOrder and filteredOnAssertions with ThrowingConsumer to accept consumers that throw checked exceptions.

Allow specifying supertype consumers for satisfies and satisfiesAnyOf in AbstractAssert.

Allow configuring the preferred assumption exception (#2267).

Generate proper conditionDescriptionWithStatus in MappedCondition. (Stefan Bischof)

Use conditionDescriptionWithStatus on Join Condition. (Stefan Bischof)

Add type parameter to ThrowableAssert (#2311). (Stefano Cordio)

Sync BDDAssumptions with Assumptions (#2313). (Stefano Cordio)

Javadoc improvements (#2274). (Golan Levy)

Javadoc improvements. (Stefano Cordio)

Fix Javadoc warnings. (Stefano Cordio)

Internal: Add binary compatibility check of main against latest release (#2271). (Stefano Cordio)

Internal: Add binary compatibility check of branches against main (#2285). (Stefano Cordio)

Internal: Use custom display name generator instead of @DisplayName on each test and remove unnecessary @DisplayName annotation. (Stefano Cordio)

Internal: Path and File assertions refactoring. (Stefano Cordio)

Internal: Add additional tests for Path assertions. (Stefano Cordio)

Internal: Remove unnecessary clean goal in build. (Stefano Cordio)

Internal: Remove MockPathsBaseTest in favor of PathsBaseTest and @TempDir. (Stefano Cordio)

Internal: Remove memoryfilesystem. (Stefano Cordio)

Internal: Reorder POM based on Maven code conventions. (Stefano Cordio)

Internal: Use Java 17 GA, remove EOL Java 16 in CI build. (Stefano Cordio)

Internal: Bump junit-jupiter.version from 5.7.2 to 5.8.0. (Stefano Cordio)

Internal: Bump mockito.version from 3.11.1 to 3.12.4. (Stefano Cordio)

Internal: Bump byte-buddy version from 1.11.2 to 1.11.16

Internal: Bump cdg.pitest.version from 0.0.10 to 0.1.0

Internal: Bump Bump pitest-junit5-plugin from 0.14 to 0.15

Internal: Bump pitest-maven from 1.6.7 to 1.7.0

Internal: Bump jackson-databind from 2.12.3 to 2.12.5

Internal: Bump equalsverifier from 3.6.1 to 3.7.1

Internal: Bump commons-io from 2.10.0 to 2.11.0.

Internal: Bump spring-core from 5.3.8 to 5.3.10

Internal: Bump org.eclipse.osgi from 3.16.300 to 3.17.0

Internal: Bump maven version from 3.8.1 to 3.8.2. (Stefano Cordio)

 Fixed

Add default method lookup to hasMethods (#2324). (Stefano Cordio)

Load default configuration after default constants values to make sure the latter are initialized.

Don’t use String.format to describe ComparisonDifference in case the given string has a % that must not be interpreted (#2279).

Fix handling of mappings to null in MappedCondition. (Stefan Bischof)

Fix Javadoc warnings.

Add content()/content(Charset) to Path/File assertions to allow chaining string assertions on the Path/File content

Returns String assertions on the content of the actual Path/File read with the given charset or the default charset if no charset was given.

Example with content():

File xFile = Files.write(Paths.get("xfile.txt"), "The Truth Is Out There".getBytes()).toFile();

// assertion succeeds (default charset is used to read xFile content)
assertThat(xFile).content().startsWith("The Truth Is ")
                           .endsWith("There");
// assertion fails
assertThat(xFile).content().contains("Elsewhere");

Example with content(Charset):

File utf8File = Files.write(Paths.get("utf8.txt"), "é à".getBytes()).toFile();

// assertion succeeds
assertThat(utf8File).content(StandardCharsets.UTF_8).startsWith("é")
                                                    .endsWith("à");
// assertion fails
assertThat(utf8File).content(StandardCharsets.UTF_8).contains("e");

Add hasSize(long expectedSizeInBytes) to Path assertions

Asserts that the tested Path has the given size in bytes.

Note that the actual Path must exist and be a regular file.

Examples:

Path foxPath = Files.write(Paths.get("/fox.txt"), "The Quick Brown Fox.".getBytes());

// assertion succeeds
assertThat(foxPath).hasSize(20);

// assertion fails
assertThat(foxPath).hasSize(3);

Add isMixedCase() to CharSequence assertions

Verifies that the actual CharSequence is a mixed case CharSequence, i.e., neither uppercase nor lowercase.

If actual is empty or contains only case-independent characters, the assertion will pass.

Examples:

// assertions succeed
assertThat("Capitalized").isMixedCase();
assertThat("camelCase").isMixedCase();
assertThat("rAndOMcAse1234").isMixedCase();
assertThat("1@3$567").isMixedCase();
assertThat("").isMixedCase();

// assertions fail
assertThat("I AM GROOT!").isMixedCase();
assertThat("please be quiet").isMixedCase();

Add containsAnyOf(CharSequence…​ values) to CharSequence assertions

Verifies that the actual CharSequence contains any of the given values.

Examples:

// assertion succeeds
assertThat("Gandalf the grey").containsAnyOf("grey", "black");

// assertion fails
assertThat("Gandalf the grey").containsAnyOf("white", "black");

Add hasExtension(String extension) to Path assertions

Verifies that the actual Path has the given extension.

Examples:

Path path = Paths.get("file.java");

// assertion succeeds
assertThat(path).hasExtension("java");

// assertion fails
assertThat(path).hasExtension("png");

Add hasNoExtension() to Path and File assertions

Verifies that the actual Path or File has no extension.

Examples with Path:

// assertion succeeds
assertThat(Paths.get("file")).hasNoExtension();
assertThat(Paths.get("file.")).hasNoExtension();

// assertion fails
assertThat(Paths.get("file.txt")).hasNoExtension();

Add hasScaleOf(int expectedScale) to BigDecimals assertions

Verifies the BigDecimal under test has the given scale.

Examples:

// assertions succeed
assertThat(new BigDecimal("8.00")).hasScaleOf(2);
assertThat(new BigDecimal("8.00").setScale(4)).hasScaleOf(4);

// assertion fail
assertThat(new BigDecimal("8.00")).hasScaleOf(3);
assertThat(new BigDecimal("8.00").setScale(4)).hasScaleOf(2);

Add isUnmodifiable() to Collection assertions

Verifies that the actual collection is unmodifiable, i.e., throws an UnsupportedOperationException with any attempt to modify the collection.

Example:

// assertions succeed
assertThat(Collections.unmodifiableCollection(new ArrayList<>())).isUnmodifiable();
assertThat(Collections.unmodifiableList(new ArrayList<>())).isUnmodifiable();
assertThat(Collections.unmodifiableSet(new HashSet<>())).isUnmodifiable();

// assertions fail
assertThat(new ArrayList<>()).isUnmodifiable();
assertThat(new HashSet<>()).isUnmodifiable();
2.9.4. AssertJ Core 3.20.2

Release date: 2021-06-20

Bugfix release that revert a breaking change in 3.20.0 due to the heavy impact on binary compatibility and to continue allowing third-party libraries returning their own assertion classes with overridden assertThat methods.

Thanks to David Schlosnagle and Stefano Cordio for the fixes in this release.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Fixed

Restore deep equality comparison for map containsOnly assertions. (David Schlosnagle)

Revert "[Breaking change] Align return types across assertions / assumptions / soft assertions and do not use Abstract Asserts" introduced in 3.20.0.

2.9.5. AssertJ Core 3.20.1

Release date: 2021-06-16

Bugfix release.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Fixed

Fix StandardComparisonStrategy.areEqual array comparison when given a non null array and a null one.

2.9.6. AssertJ Core 3.20.0

Release date: 2021-06-15

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Harsha Vipparti, Julien Roy, Aakarshit Uppal, Abhijeet Shukla, Jack Gough, Filip Hrisafov, RGalways17, Stefan Birkner, Stefan Bischof, Matthieu Baechler, sustc11810424, Henry Coles, Annette0127, Johannes Becker, Slawomir Jaranowski, and Patrick Allain.

Special thanks to Filip Hrisafov to have got rid of the heap pollution compiler warning when using soft assertions or assumptions with methods having a generic vararg parameters.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

PropertyOrFieldSupport fails when trying to get map value for an unknown key instead of returning null, this impacts:

assertThat(map).hasFieldOrPropertyWithValue(name, value) and assertThat(map).hasFieldOrProperty(name) now fail if name is not a known key.

assertThat(map).extracting("unknown") now fails instead of returning null.

assertThat(map).flatExtracting("unknown1", "unknown2") now fails instead of returning a list of with null values for unknown keys.

assertThat(map).containsAllEntriesOf(otherMap) now succeeds when otherMap is empty instead of failing.

RecursiveComparisonConfiguration now uses the same default values when built from builder and constructor.

usingRecursiveFieldByFieldElementComparator in iterable/array/atomic reference array now uses the new recursive comparison instead of the old implementation.

RecursiveFieldByFieldComparator was removed as it has been replaced by the recursive comparison in usingRecursiveFieldByFieldElementComparator.

Public methods that could cause heap pollution have been made final to improve the user experience with soft assertions and soft assumptions. In case a subclass was overriding any of these methods, a similar result can be achieved by overriding the corresponding ForProxy method. For example, AbstractMapAssert#contains now delegates the implementation to AbstractMapAssert#containsForProxy, which is protected and therefore can be overridden.

Align return types across assertions / assumptions / soft assertions and return concrete types. The breaking change is for people that have implemented WithAssertions or WithAssumption as they now have different return types, the regular user should not see any difference.

 New features

Add containsIgnoringWhitespaces to String assertions. (Johannes Becker)

Add IterableAssert.elements(int…​) to assert on specific elements in an Iterable. (Matthieu Baechler)

Add hasExactlyElementsOfTypes assertion for iterables, arrays and AtomicReferenceArrays. (RGalways17)

Add asString(charset) to AbstractInputStreamAssert to support String assertions. (Stefan Birkner)

Add assertWith assertion construct.

Add isNotFinite float and double assertions.

Add isNotInfinite float and double assertions.

Add comparingOnlyFields to the recursive comparison to restrict the comparison to the specified fields.

Add usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration configuration) to AtomicReferenceArray and Object[] assertions (it is already supported for iterable assertions).

Add usingRecursiveFieldByFieldElementComparatorOnFields(String…​) for iterable/array/atomic reference array assertions to restrict the recursive comparison to the specified fields.

Add usingRecursiveFieldByFieldElementComparatorIgnoringFields(String…​) to iterable/array/atomic reference array assertions.

Add MappedCondition to verify a Condition on the result of a map operation. (Stefan Bischof)

Add VerboseCondition to get a detailed description when the condition fails. (Stefan Bischof)

 Improvements

In error messages, use 'toString' method of subclasses of AtomicReference when overridden. (sustc11810424)

SoftAssertionsExtension now reports line number in reported assertion errors.

Align return types across assertions / assumptions / soft assertions and do not use Abstract Asserts. (Filip Hrisafov)

Use varargs for satisfiesAnyOf to remove the multiple overloaded versions. (Filip Hrisafov)

Remove compiler heap pollution warnings that were raised for soft assertions or assumptions. (Filip Hrisafov)

Improve performance in StandardComparisonStrategy#areEqual. (Filip Hrisafov)

Return concrete type where proxyable types were used in Assumptions, BDDAssumptions and WithAssumptions.

RecursiveComparisonConfiguration now uses the same default values when built from builder and constructor.

Improve error message when map is not empty and expected entries is. (Abhijeet Shukla)

ThrowableTypeAlternative now inherits from AbstractObjectAssert as AbstractThrowableAssert did.

Make assertThat(map).containsAllEntriesOf(otherMap) assertion to succeed when otherMap is empty. (Aakarshit Uppal)

Add non assertions methods in BDDAssertions that existed in Assertions but were missing in BDDAssertions.

Display proper collection type in contains and containsAll error messages . (Patrick Allain)

Rework StandardComparisonStrategy#areEqual to avoid shortcuts. (Stefano Cordio)

Disambiguate error messages by adding "actual" before printing actual value. (Harsha Vipparti)

Recursive comparison: properly track field location for maps and honor ignored fields.

allOf condition error message shows state (successful/failed) of each combined conditions.

Javadoc improvements. (Stefano Cordio)

Clarify newListAssertInstance Javadoc.

Fix flaky test by making sure default date formats are used before tests.

Remove unnecessary space ShouldNotBe and ShouldNotHave error messages. (Annette0127)

Internal: Rename test to match its purpose. (Matthieu Baechler)

Internal: Fix some warnings in AssertJ codebase. (Filip Hrisafov)

Internal: Remove Proxyable assert classes since we don’t need to subclass assert classes to fix heap pollution with @SafeVarargs.

Internal: Hide implementation detail of assertContainsOnlyKeys. (Stefano Cordio)

Internal: Remove unnecessary Javadoc from internal class, import Map.Entry. (Stefano Cordio)

Internal: Favor requireNonNull with Supplier. (Stefano Cordio)

Internal: Update CodeQL workflow. (Stefano Cordio)

Internal: Mention the JDK 11 requirement in the contribution guidelines. (Stefano Cordio)

Internal: Remove EOL JDK versions from CI multi versions build. (Stefano Cordio)

Internal: Bump maven version from 3.6.3 to 3.8.1 (Stefano Cordio)

Internal: Bump jacoco-maven-plugin.version from 0.8.6 to 0.8.7

Internal: Bump guava from 30.1-jre to 30.1.1-jre

Internal: Bump org.eclipse.osgi from 3.16.100 to 3.16.200

Internal: Bump jackson-databind from 2.12.1 to 2.12.3

Internal: Bump commons-lang3 from 3.11 to 3.12.0

Internal: Bump commons-io from 2.8.0 to 2.9.0.

Internal: Bump mockito.version from 3.7.7 to 3.10.0 (Erhard Pointl)

Internal: Bump bnd.version from 5.2.0 to 5.3.0

Internal: Bump sonar-maven-plugin to version 3.8.0.2131 (Stefano Cordio)

Internal: Bump equalsverifier from 3.5.2 to 3.6.1

Internal: Bump spring-core from 5.3.6 to 5.3.7

Internal: Bump byte-buddy version from 1.10.19 to 1.11.1

Internal: Bump maven-invoker-plugin from 3.2.1 to 3.2.2

Internal: Bump junit-jupiter.version from 5.6.3 to 5.7.2 (Erhard Pointl)

Internal: Bump junit.version from 4.13.1 to 4.13.2 (Erhard Pointl)

Internal: Fix IntelliJ flaky test due to JUnit upgrade to version 5.7. (Stefano Cordio)

Internal: Build AssertJ Core with java 16 in CI cross version build. (Erhard Pointl)

Internal: Bump actions/setup-java to version 2 (Stefano Cordio)

Internal: Verify PRs with pitest (Henry Coles)

Internal: Add .DS_Store to .gitignore (Slawomir Jaranowski)

Internal: Enforce Java 11 or newer to build the project (Slawomir Jaranowski)

Internal: Define Java 9 compile execution instead of maven profile (Slawomir Jaranowski)

 Fixed

Honor map key comparison semantics in containsOnly assertions. (Stefano Cordio and Filip Hrisafov)

Fix containsSubsequence String assertion failing when given multiple empty values. (Jack Gough)

Fix NullPointerException in primitive double assertions where a null Double is compared to a primtive one. (Jack Gough)

Fix NullPointerException in StandardRepresentation. (Jack Gough)

Make IterableDiff to always compare actual elements to expected elements and not the other way around in case the comparison is not symmetrical.

Add enum types to the types that can’t cause cycles in a recursive comparison.

Fix hasOnlyFields which should not consider static fields.

Fix StackOverflowError when usingRecursiveComparison of Path on Windows by using path natural comparator. (Julien Roy)

Extract value only if the map key exists in PropertyOrFieldSupport. (Stefano Cordio)

Replace references to mapOf by Guava ImmutableMap.of in Javadoc.

Fix Javadoc warnings.

 Deprecated

The main deprecations are related to shallow field by field comparison classes and methods:

usingFieldByFieldElementComparator

Use usingRecursiveFieldByFieldElementComparator() or usingRecursiveComparison() instead to perform a true recursive comparison.

usingElementComparatorOnFields

Use usingRecursiveFieldByFieldElementComparatorOnFields(String…​) instead.

usingElementComparatorIgnoringFields

Use usingRecursiveFieldByFieldElementComparatorIgnoringFields(String…​) instead.

usingComparatorForElementFieldsWithNames

This method is used with usingFieldByFieldElementComparator() which is deprecated in favor of usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) or usingRecursiveComparison().

When using usingRecursiveComparison() the equivalent is:

RecursiveComparisonAssert.withEqualsForFields(java.util.function.BiPredicate, String…​) or

RecursiveComparisonAssert.withComparatorForFields(Comparator, String…​)

and when using usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration config), sets the config with:

RecursiveComparisonConfiguration.Builder.withEqualsForFields(java.util.function.BiPredicate, String…​) or

RecursiveComparisonConfiguration.Builder.withComparatorForFields(Comparator, String…​)

usingComparatorForElementFieldsWithType

This method is used with usingFieldByFieldElementComparator() which is deprecated in favor of usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) or usingRecursiveComparison().

When using usingRecursiveComparison() the equivalent is:

RecursiveComparisonAssert.withEqualsForType(java.util.function.BiPredicate, Class) or

RecursiveComparisonAssert.withComparatorForType(Comparator, Class)

and when] using usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration config), sets the config with:

RecursiveComparisonConfiguration.Builder.withEqualsForType(java.util.function.BiPredicate, Class) or

RecursiveComparisonConfiguration.Builder.withComparatorForType(Comparator, Class)

Add containsIgnoringWhitespaces to String assertions

Verifies that the actual CharSequence contains all the given values, ignoring whitespace differences.

Example:

assertThat("Gandalf the grey").containsIgnoringWhitespaces("alf")
                              .containsIgnoringWhitespaces("alf", "grey")
                              .containsIgnoringWhitespaces("thegrey")
                              .containsIgnoringWhitespaces("thegr  ey")
                              .containsIgnoringWhitespaces("t h e g r\t\r\n ey");

Add IterableAssert.elements(int…​) to assert on specific elements in an Iterable

Allow to perform assertions on the elements corresponding to the given indices (the iterable Iterable under test is changed to an iterable with the selected elements).

Example:

Iterable<TolkienCharacter> hobbits = Arrays.asList(frodo, sam, pippin);

// assertion succeeds
assertThat(hobbits).elements(1, 2)
                   .hasSize(2)
                   .containsExactly(sam, pippin);

// assertion fails
assertThat(hobbits).element(1, 2)
                   .containsExactly(frodo, pippin);

Add hasExactlyElementsOfTypes assertion for iterables, arrays and AtomicReferenceArrays

Verifies that the actual elements are of the given types in the given order, there should be as many expected types as there are actual elements.

This assertion is available for iterables, arrays and AtomicReferenceArrays.

Example:

Iterable<Object> list = Arrays.asList(1, "a", "b", 1.00);

assertThat(list).hasExactlyElementsOfTypes(Integer.class, String.class, String.class, Double.class);

Add asString(charset) to AbstractInputStreamAssert to support String assertions

Converts the content of the actual InputStream to a String by decoding its bytes using the given charset and returns assertions for the computed String allowing String specific assertions from this call.

Example:

InputStream abcInputStream = new ByteArrayInputStream("abc".getBytes());

assertThat(abcInputStream).asString(UTF_8)
                          .startsWith("a");

allOf condition error message shows state (successful/failed) of each combined conditions

allOf condition error message reports which conditions failed [✗] and which succeeded [✓] to ease understanding the failure cause.

Let’s use an allOf condition checking 3 conditions: young, very tall and Jedi and try it on Yoda, it fails with the following error:

Expecting actual:
  "Yoda"
to be:
[✗] all of:[
   [✓] a Jedi,
   [✗] very tall,
   [✗] young
]

Add assertWith assertion construct

Uses the given instance as the instance under test for all the assertions expressed as the passed Consumer.

This is useful to avoid repeating getting the instance to test, a bit like a with block which turns the target into the equivalent of this (as in Groovy for example).

Example:

assertWith(team.getPlayers().get(0).getStats(),
           stats -> {
              assertThat(stats.pointPerGame).isGreaterThan(25.7);
              assertThat(stats.assistsPerGame).isGreaterThan(7.2);
              assertThat(stats.reboundsPerGame).isBetween(9, 12);
           });

assertWith is variation of AbstractAssert.satisfies(Consumer) hopefully easier to find for some users.

Add isNotFinite float and double assertions

Verifies that the double/float value is not a finite floating-point value.

Note that 'not finite' is not equivalent to infinite as NaN is neither finite or infinite.

Examples:

assertThat(Double.POSITIVE_INFINITY).isNotFinite();
assertThat(Double.NEGATIVE_INFINITY).isNotFinite();
assertThat(Double.NaN).isNotFinite();

assertThat(Float.POSITIVE_INFINITY).isNotFinite();
assertThat(Float.NEGATIVE_INFINITY).isNotFinite();
assertThat(Float.NaN).isNotFinite();

Add isNotInfinite float and double assertions

Verifies that the double/float value represents neither positive infinity nor negative infinity.

Examples with doubles:

// assertions succeed
assertThat(1.0).isNotInfinite();
assertThat(Double.NaN).isNotInfinite();

// assertions fail
assertThat(Double.POSITIVE_INFINITY).isNotInfinite();
assertThat(Double.NEGATIVE_INFINITY).isNotInfinite();

Add comparingOnlyFields float and double assertions

Makes the recursive comparison to only compare given actual fields and their subfields (no other fields will be compared).

Specifying a field will make all its subfields to be compared, for example specifying person will lead to compare person.name, person.address and all other Person fields. On the other hand if you specify person.name, person won’t be compared but person.name will be.

The fields are specified by name, not by value, for example you can specify person.name but not "Jack" as "Jack" is not a field value.

comparingOnlyFields can be combined with ignoring fields methods to restrict further the fields actually compared, the resulting compared fields = {specified compared fields} - {specified ignored fields}. For example if compared fields = {"foo", "bar", "baz"} and ignored fields = {"bar"} then only {"foo", "baz"} fields will be compared.

Example:

public class Person {
  String name;
  double height;
  Home home = new Home();
}

public class Home {
  Address address = new Address();
}

public static class Address {
  int number;
  String street;
}

Person sherlock = new Person("Sherlock", 1.80);
sherlock.home.address.street = "Baker Street";
sherlock.home.address.number = 221;

Person moriarty = new Person("Moriarty", 1.80);
moriarty.home.address.street = "Butcher Street";
moriarty.home.address.number = 221;

// assertion succeeds as name and home.address.street fields are not compared.
assertThat(sherlock).usingRecursiveComparison()
                    .comparingOnlyFields("height", "home.address.number")
                    .isEqualTo(moriarty);

// assertion fails as home.address.street fields differ.
assertThat(sherlock).usingRecursiveComparison()
                    .comparingOnlyFields("height", "home")
                    .isEqualTo(moriarty);

Add usingRecursiveFieldByFieldElementComparatorOnFields(String…​) to iterable/array/atomic reference array assertions to restrict the recursive comparison to the specified fields

The assertions chained after this method will use a recursive field by field comparison on the given fields (including inherited fields) instead of relying on the element equals method. This is handy when the element equals method is not overridden or implemented as you expect.

Nested fields are supported and are expressed like: name.first

The comparison is recursive: elements are compared field by field, if a field type has fields they are also compared field by field (and so on).

Example:

Player derrickRose = new Player(new Name("Derrick", "Rose"), "Chicago Bulls");
derrickRose.nickname = new Name("Crazy", "Dunks");

Player jalenRose = new Player(new Name("Jalen", "Rose"), "Chicago Bulls");
jalenRose.nickname = new Name("Crazy", "Defense");

// assertion succeeds as all compared fields match
assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparatorOnFields("name.last", "team", "nickname.first")
                             .contains(jalenRose);

// assertion fails, name.first values differ
assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparatorOnFields("name")
                             .contains(jalenRose);

This method is actually a shortcut of usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) with a configuration comparing only the given fields, the previous example can be written as:

RecursiveComparisonConfiguration configuration = RecursiveComparisonConfiguration.builder()
                                                                                 .withComparedFields("name.last", "team", "nickname.first")
                                                                                 .build();

assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparator(configuration)
                             .contains(jalenRose);

Add usingRecursiveFieldByFieldElementComparatorIgnoringFields(String…​) to iterable/array/atomic reference array assertions to ignore some fields in the recursive comparison

The assertions chained after this method will use a recursive field by field comparison on all fields (including inherited fields) except the given ones instead of relying on the element equals method. This is handy when the element equals method is not overridden or implemented as you expect.

Nested fields are supported and are expressed like: name.first

The comparison is recursive: elements are compared field by field, if a field type has fields they are also compared field by field (and so on).

Example:

Player derrickRose = new Player(new Name("Derrick", "Rose"), "Chicago Bulls");
derrickRose.nickname = new Name("Crazy", "Dunks");

Player jalenRose = new Player(new Name("Jalen", "Rose"), "Chicago Bulls");
jalenRose.nickname = new Name("Crazy", "Defense");

// assertion succeeds as all compared fields match
assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparatorIgnoringFields("name.last", "nickname.first")
                             .contains(jalenRose);

// assertion fails, names are ignored but nicknames are not and nickname.last values differ
assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparatorIgnoringFields("name")
                             .contains(jalenRose);

This method is actually a shortcut of usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) with a configuration comparing only the given fields, the previous example can be written as:

RecursiveComparisonConfiguration configuration = RecursiveComparisonConfiguration.builder()
                                                                                 .withIgnoredFields("name.first", "nickname.last")
                                                                                 .build();

assertThat(list(derrickRose)).usingRecursiveFieldByFieldElementComparator(configuration)
                             .contains(jalenRose);

Add MappedCondition to verify a Condition on the result of a map operation

A MappedCondition is defined with a map operation and a Condition that accepts the type returned by the map operation.
When applied the MappedCondition first map the value under test and then verify the resulting mapped value against its nested Condition.

Let’s see how it works on an example:

// nested Condition
Condition<String> hasLineSeparator = new Condition<>(s -> s.contains(System.lineSeparator()), "has lineSeparator");
// mapped Condition
Condition<Optional<String>> optionalWithLineSeparator = MappedCondition.mappedCondition(Optional::get, hasLineSeparator, "optional value has lineSeparator");

// assertion succeeds
assertThat(Optional.of("a" + System.lineSeparator())).is(optionalWithLineSeparator)

// assertion fails
assertThat(Optional.of("a")).is(optionalWithLineSeparator)

Add VerboseCondition to get a detailed description when the condition fails

A VerboseCondition shows the value under test when it fails thanks to the specified objectUnderTestDescriptor function.

When defining the objectUnderTestDescriptor function, you should take in consideration whether the condition is going to be used with is(Condition) or has(Condition) since the start of the error message is different between the two.

Let’s see how it works with an example that works well with is(Condition):

Condition<String> shorterThan4 = VerboseCondition.verboseCondition(actual -> actual.length() < 4,
                                                                   // predicate description
                                                                   "shorter than 4",
                                                                   // value under test description transformation function
                                                                   s -> String.format(" but length was %s", s.length()));

If we execute:

assertThat("foooo").is(shorterThan4);

we get the following assertion error:

Expecting actual:
  "foooo"
to be shorter than 4 but length was 5

Note that the beginning of the error message looks nice with is(Condition) but not so much has(Condition):

Expecting actual:
  "foooo"
to have shorter than 4 but length was 5
2.9.7. AssertJ Core 3.19.0

Release date: 2021-01-24

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, Arsen Ibragimov, Kim S. Ly, Victor Wang, Omar Morales, Reto Weiss, Michael Florian Grafl, Sergei Tachenov, Mayra Lucero Garcia Ramírez, Eveneko, Julieta Navarro, Michael Keppler, Alex Dukhno, Himadri Mandal and Jin Kwon.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Replacement of FieldLocation by String breaking changes:

Remove deprecated RecursiveComparisonConfiguration.registerComparatorForField(Comparator<?> comparator, FieldLocation fieldLocation) in favor of registerComparatorForFields(Comparator<?> comparator, String…​ fieldLocations)

getIgnoredCollectionOrderInFields(), getIgnoredFields() and getIgnoredOverriddenEqualsForFields() now return a collection of String instead of FieldLocation

comparatorByFields() now returns Stream<Entry<String, Comparator<?>>> instead of Stream<Entry<FieldLocation, Comparator<?>>>

Ignore static and synthetic fields when introspecting fields as they are not relevant in for instance assertions. This change impacts:

hasFieldOrProperty

hasFieldOrPropertyWithValue

extracting field by name

Probably not an impactful breaking change: abstract classes' constructors are now protected instead of public.

Return generic return type for AbstractSoftAssertions.fail for convenience and to be consistent with Assertions.fail. This is a binary incompatible but still source compatible change.

 New features

Add isEqualToNormalizingUnicode CharSequence assertion. (Julieta Navarro)

Add satisfiesExactly iterable/array assertion. (Michael Florian Grafl)

Add satisfiesExactlyInAnyOrder iterable/array assertion.

Add Instant variants to Date assertions. (Arsen Ibragimov)

Add float/double finite or infinite assertions. (Jin Kwon)

Add doesNotHaveSameHashCodeAs assertion. (Kim S. Ly)

Add doesNotHaveToString assertion. (Kim S. Ly)

Add overloaded contains assertions with boxed arrays to primitive array assertions. (Stefano Cordio, Mayra Lucero Garcia Ramírez, Omar Morales)

Add hasOnlyFields assertion. (Victor Wang)

Allow to pass a lazy description only evaluated if the assertion fails.

Add isEmptyFile/isNotEmptyFile to Path assertions. (Omar Morales)

 Improvements

Change isEqualTo error message to follow pattern:

expected: "abc"
but was : "bcd"

Remove <> from error messages when displaying values as it was deemed noisy. (Erhard Pointl, Omar Morales, Himadri Mandal)

Better indentation consistency in error messages.

Include the first 3 stacktrace elements in throwable representation (configurable). (Eveneko)

Change abstract class constructor to protected.

Use normalized actual and expected in String assertion errors that compare normalized values. (Etienne Miret)

Refactor common representation code into UnambiguousRepresentation. (Etienne Miret)

Use org.junit.ComparisonFailure when available. (Etienne Miret)

Improve describe error readability of ElementsShouldSatisfy. (Drummond Dawson)

Recursive comparison: show the index of the array/list element compared in the reported differences.

Recursive comparison documentation: make it clear that ignoringFields and ignoringFieldsMatchingRegexes operate on field names.

Ignore getters with void return type during property introspection. (Reto Weiss)

Recalculate description for nested Conditions like Not and Join as some Condition description when the Condition is evaluated. (Stefan Bischof)

Javadoc Date assertions improvements.

Explain reference to newLinkedHashMap in Javadoc.

Internal: Only instantiate assertion error from AssertionErrorCreator. (Alex Dukhno)

Internal: Use parent pom 2.2.10 that bumps the licence year to 2021. (Erhard Pointl)

Internal: Use java11 in codeql workflow. (Erhard Pointl)

Internal: Fix a bunch of sonar violations. (Erhard Pointl)

Internal: Reduce test fragility. (Erhard Pointl)

Internal: Enforce surefire encoding. (Stefano Cordio)

Internal: Bump junit version from 4.13 to 4.13.1 (Erhard Pointl)

Internal: Bump highlight version to 10.4.0

Internal: Bump mockito version from 3.6.0 to 3.6.28 (Erhard Pointl)

Internal: Bump jackson-databind from 2.11.3 to 2.12.1

Internal: Bump guava from 30.0-jre to 30.1-jre

Internal: Bump org.eclipse.osgi from 3.16.0 to 3.16.100

Internal: Bump byte-buddy version from 1.10.18 to 1.10.19

Internal: Bump mockito version from 3.6.28 to 3.7.7

Internal: Bump equalsverifier from 3.5 to 3.5.2

 Fixed

Fix long overflow in AbstractTemporalAssert. (Sergei Tachenov)

Make Collection extending AtomicInteger to be represented as a collection instead of an AtomicInteger.

Fix Javadoc typo. (Michael Keppler)

 Deprecated

Deprecate isXmlEqualToContentOf in favor of XML Unit.

Add isEqualToNormalizingUnicode CharSequence assertion

Verifies that the actual CharSequence is equal to the given one after they have been normalized according to the Normalizer.Form.NFC form, which is a canonical decomposition followed by canonical composition.

Examples:

// assertions succeed:

// Ä = \u00C4 - Ä = \u0041\u0308
assertThat("Ä").isEqualToNormalizingUnicode("Ä");
assertThat("\u00C4").isEqualToNormalizingUnicode("\u0041\u0308");

// assertions fail:
assertThat("ñ").isEqualToNormalizingUnicode("n");
assertThat("Ä").isEqualToNormalizingUnicode("b");

Add satisfiesExactly iterable/array assertion

Verifies that each element satisfies the requirements corresponding to its index, so the first element must satisfy the first requirements, the second element the second requirements etc…​

Each requirement is expressed as a Consumer, and there must be as many requirements as there are iterable elements.

Examples:

Iterable<TolkienCharater> characters = list(frodo, aragorn, legolas);

// assertions succeed
assertThat(characters).satisfiesExactly(character -> assertThat(character.getRace()).isEqualTo("Hobbit"),
                                        character -> assertThat(character.isMortal()).isTrue(),
                                        character -> assertThat(character.getName()).isEqualTo("Legolas"));

// you can specify more that one assertion per requirements
assertThat(characters).satisfiesExactly(character -> {
                                           assertThat(character.getRace()).isEqualTo("Hobbit");
                                           assertThat(character.getName()).isEqualTo("Frodo");
                                        },
                                        character -> {
                                           assertThat(character.isMortal()).isTrue();
                                           assertThat(character.getName()).isEqualTo("Aragorn");
                                        },
                                        character -> {
                                           assertThat(character.getRace()).isEqualTo("Elf");
                                           assertThat(character.getName()).isEqualTo("Legolas");
                                        });

// assertion fails as aragorn does not meet the second requirements
assertThat(characters).satisfiesExactly(character -> assertThat(character.getRace()).isEqualTo("Hobbit"),
                                        character -> assertThat(character.isMortal()).isFalse(),
                                        character -> assertThat(character.getName()).isEqualTo("Legolas"));

Add satisfiesExactlyInAnyOrder iterable/array assertion

Verifies that at least one combination of iterable elements exists that satisfies the consumers in order (there must be as many consumers as iterable elements and once a consumer is matched it cannot be reused to match other elements).

This is a variation of satisfiesExactly where order does not matter.

Examples:

List<String> starWarsCharacterNames = list("Luke", "Leia", "Yoda");

// these assertions succeed:
assertThat(starWarsCharacterNames).satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Y"), // matches "Yoda"
                                                              name -> assertThat(name).contains("L"), // matches "Luke" and "Leia"
                                                              name -> {
                                                                assertThat(name).hasSize(4);
                                                                assertThat(name).doesNotContain("a"); // matches "Luke" but not "Leia"
                                                              })
                                  // satisfiesExactly would have succeeded for this assertion
                                  .satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Lu"),
                                                              name -> assertThat(name).contains("Le"),
                                                              name -> assertThat(name).contains("Yo"))
                                  // satisfiesExactly would have failed for this assertion
                                  .satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Yo"),
                                                              name -> assertThat(name).contains("Lu"),
                                                              name -> assertThat(name).contains("Le"))
                                  // satisfiesExactly would have failed for this assertion
                                  .satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Le"),
                                                              name -> assertThat(name).contains("Yo"),
                                                              name -> assertThat(name).contains("Lu"));

// this assertion fails as 3 consumer/requirements are expected
assertThat(starWarsCharacterNames).satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Y"),
                                                              name -> assertThat(name).contains("L"));

// this assertion fails as no element contains "Han" (first consumer/requirements can't be met)
assertThat(starWarsCharacterNames).satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Han"),
                                                              name -> assertThat(name).contains("L"),
                                                              name -> assertThat(name).contains("Y"));

// this assertion fails as "Yoda" element can't satisfy any consumers/requirements (even though all consumers/requirements are met)
assertThat(starWarsCharacterNames).satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("L"),
                                                              name -> assertThat(name).contains("L"),
                                                              name -> assertThat(name).contains("L"));

// this assertion fails as no combination of elements can satisfy the consumers in order
// the problem is if the last consumer is matched by Leia then no other consumer can match Luke (and vice versa)
assertThat(starWarsCharacterNames).satisfiesExactlyInAnyOrder(name -> assertThat(name).contains("Y"),
                                                              name -> assertThat(name).contains("o"),
                                                              name -> assertThat(name).contains("L"));

Add Instant variants to Date assertions

Date assertions now understand Instant parameters.

Examples:

final Date dateTimeWithMs = parseDatetimeWithMs("2001-02-03T04:05:06.700");

assertThat(dateTimeWithMs).isEqualTo(dateTimeWithMs.toInstant())
                          .isBefore(Instant.parse("2002-01-01T00:00:00.00Z"))
                          .isAfter(Instant.parse("2000-01-01T00:00:00.00Z"))
                          .isBetween(Instant.parse("2000-01-01T00:00:00.00Z"),
                                     Instant.parse("2002-01-01T00:00:00.00Z"))
                          .isCloseTo(dateTimeWithMs.toInstant().minusMillis(10), 20)
                          .isEqualToIgnoringHours(dateTimeWithMs.toInstant().plus(1, ChronoUnit.HOURS))
                          .isEqualToIgnoringMinutes(dateTimeWithMs.toInstant().plus(1, ChronoUnit.MINUTES))
                          .isEqualToIgnoringSeconds(dateTimeWithMs.toInstant().plus(1, ChronoUnit.SECONDS))
                          .isEqualToIgnoringMillis(dateTimeWithMs.toInstant().plus(1, ChronoUnit.MILLIS))
                          .isIn(dateTimeWithMs.toInstant(), dateTimeWithMs.toInstant().plusMillis(10))
                          .isInSameDayAs(dateTimeWithMs.toInstant().plus(1, ChronoUnit.MINUTES))
                          .isInSameMonthAs(Instant.parse("2001-02-01T00:00:00.00Z"))
                          .isInSameYearAs(Instant.parse("2001-01-01T00:00:00.00Z"))
                          .isNotIn(dateTimeWithMs.toInstant().minusMillis(10), dateTimeWithMs.toInstant().plusMillis(10));

Add float/double finite or infinite assertions

Examples:

assertThat(1.0f).isFinite();
assertThat(Float.NEGATIVE_INFINITY).isInfinite();

assertThat(1.0).isFinite();
assertThat(Double.POSITIVE_INFINITY).isInfinite();

Add doesNotHaveSameHashCodeAs assertion

Verifies that the actual object does not have the same hashCode as the given object.

Examples:

// assertions succeed
assertThat(42L).doesNotHaveSameHashCodeAs(2501L);
assertThat("The Force").doesNotHaveSameHashCodeAs("Awakens");

// assertions fail
assertThat(42L).doesNotHaveSameHashCodeAs(42L);
assertThat("The Force").doesNotHaveSameHashCodeAs("The Force");
assertThat(new Jedi("Yoda", "Blue")).doesNotHaveSameHashCodeAs(new Jedi("Yoda", "Blue"));

Add doesNotHaveToString assertion

Verifies that the actual object does not have the same toString as the given object.

Examples:

CartoonCharacter homer = new CartoonCharacter("Homer");

// Instead of writing ...
assertThat(homer.toString()).isNotEqualTo("Marge");
// ... you can simply write:
assertThat(homer).doesNotHaveToString("Marge");

Add overloaded contains assertions with boxed arrays for primitive array assertions

Primitive array assertions (like long[] assertions) support variants with boxed arrays (e.g. Long[]) for contains assertions.

Examples:

assertThat(new boolean[] { true, false, true }).containsExactly(new Boolean[] {true, false, true });
assertThat(new short[] { 1,  2,  3 }).containsExactly(new Short[] { 1,  2,  3 });
assertThat(new int[] { 1,  2,  3 }).containsExactly(new Integer[] { 1,  2,  3 });
assertThat(new long[] { 1L, 2L, 3L }).contains(new Long[] { 1L, 2L });
assertThat(new float[] { 1.0f, 2.0f, 3.0f }).containsExactly(new Float[] { 1.0f, 2.0f, 3.0f });
assertThat(new double[] { 1.0, 2.0, 3.0 }).containsExactly(new Double[] { 1.0, 1.98, 3.01 }, withPrecision(0.05));
assertThat(new char[] { 'a', 'b', 'c' }).contains(new Character[] { 'a', 'b' });

Add hasOnlyFields assertion

Verifies that the actual object has only the specified fields and nothing else.

The assertion only checks declared fields (inherited fields are not checked) that are not static or synthetic.

Examples:

public class TolkienCharacter {

  private String name;
  public int age;

  public String getName() {
    return this.name;
  }
}

TolkienCharacter frodo = new TolkienCharacter("Frodo", 33);

// assertion succeeds:
assertThat(frodo).hasOnlyFields("name", "age");

// assertions fail:
assertThat(frodo).hasOnlyFields("name");
assertThat(frodo).hasOnlyFields("not_exists");

Allow to pass a lazy description only evaluated when the assertion fails

Lazily specifies the description of the assertion that is going to be called, the given description is not evaluated if the assertion succeeds. This is useful if descriptions are expansive to build.

Examples:

// we all know Mr Frodo is 33 years old
frodo.setAge(33);

// the lazy test description is not evaluated as the assertion succeeds
assertThat(frodo.getAge()).as(() -> "check Frodo's age").isEqualTo(33);

// the lazy test description is evaluated as the assertion fails
assertThat(frodo.getAge()).as(() -> "check Frodo's age").isEqualTo(50);

The error message of the failing assertion is:

[check Frodo's age]
expected: 33
but was : 50

Add isEmptyFile and isNotEmptyFile to Path assertions

Verify that the actual Path is respectively an empty or non empty regular file.

Note that the actual Path must exist and be a regular file.

Examples given the files below:

/root/sub-dir-1/file-1.ext (no content)
/root/sub-dir-1/file-2.ext (content)

Here are some assertions examples:

Path withoutContent = Paths.get("/root/sub-dir-1/file-1.ext");
Path withContent = Paths.get("/root/sub-dir-1/file-2.ext");

// The following assertions succeed:
assertThat(withoutContent).isEmptyFile();
assertThat(withContent).isNotEmptyFile();

// The following assertions fail:
assertThat(withoutContent).isNotEmptyFile();
assertThat(withContent).isEmptyFile();
2.9.8. AssertJ Core 3.18.1

Release date: 2020-11-11

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio and Kim S. Ly.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 New features

Add map and flatMap to iterable assertions as aliases of extracting and flatExtracting.

 Improvements

Make isElementOfCustomAssert protected to ease integration with 3rd party libraries like XML Unit.

Add Javadoc for methods that needs to be implemented in AbstractIterableAssert subclasses.

Internal: Adjust hasPackage tests style. (Stefano Cordio)

Internal: Bump junit-jupiter version from 5.6.2 to 5.6.3. (Erhard Pointl)

Internal: Bump mockito from 3.5.15 to 3.6.0. (Erhard Pointl)

Internal: Bump byte-buddy version from 1.10.17 to 1.10.18.

 Fixed

Fix ShouldNotHaveSameClass error message. ( Kim S. Ly)

Fix hasNotFailed Javadoc deprecation example.

2.9.9. AssertJ Core 3.18.0

Release date: 2020-10-25

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, Fr Jeremy Krieg, BJ Hargrave, Matteo Mirk and Valeriy Vyrva.

Shout out to Fr Jeremy Krieg for adding soft assertions field injection capability in JUnit 5 SoftAssertionsExtension!

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Breaking change: disable bare name getter by default, to get the previous behaviour back, call Assertions.setExtractBareNamePropertyMethods(true);

Exclude net.bytebuddy.experimental property from shading scope: ensures that the property controls ByteBuddy experimental features also inside AssertJ, usually needed when using JDK early access builds. Before this change, ByteBuddy experimental features in AssertJ could only be controlled by org.assertj.core.internal.bytebuddy.experimental.

 New features

Add field injection capability to SoftAssertionsExtension. (Fr Jeremy Krieg)

Add hasPackage to Class assertions. (Matteo Mirk)

Add hasValueSatisfying to AtomicReference assertions. (Valeriy Vyrva)

Add hasValueMatching to AtomicReference assertions. (Valeriy Vyrva)

Add isCloseTo to Duration assertions.

Add failsWithin to Future and CompletableFuture assertions.

 Improvements

Add AssertionError factory methods to AbstractAssert. (Fr Jeremy Krieg)

Improve describe error readability of ElementsShouldSatisfy. (Drummond Dawson)

Improve isTrue/isFalse assertions error messages.

Use two spaces indentation in "should be close to" error messages.

Internal: Add CodeQL analysis. (Stefano Cordio)

Internal: Clean up some pom dependencies now that Bnd 5.2.0 is being used (BJ Hargrave)

Internal: Add assumptions it tests. (Stefano Cordio)

Internal: Reduce visibility of FieldUtils as no method is publicly accessible. (Stefano Cordio)

Internal: Remove unnecessary semicolons. (Erhard Pointl)

Internal: Enforce surefire encoding. (Stefano Cordio)

Internal: Bump jackson-databind from 2.11.2 to 2.11.3.

Internal: Bump org.eclipse.osgi from 3.15.300 to 3.16.0.

Internal: Bump equalsverifier from 3.4.2 to 3.5.

Internal: Bump byte-buddy from 1.10.14 to 1.10.17.

Internal: Bump assertj-parent-pom from 2.2.7 to 2.2.8.

Internal: Bump mockito from 3.5.10 to 3.5.15.

Internal: Bump guava from 29.0-jre to 30.0-jre.

Internal: Bump jacoco-maven-plugin from 0.8.5 to 0.8.6. (Stefano Cordio)

Internal: Bump bnd from 5.1.2 to 5.2.0.

 Fixed

Honor toString if overridden in Iterable that are not collections.

 Deprecated

Deprecate isXmlEqualTo in favor of XML Unit.

Deprecate SoftlyExtension in favor of SoftAssertionsExtension that now supports field injection.

Deprecate hasFailed() CompletableFuture assertion:

// deprecated
assertThat(future).hasFailed();
// instead calls
assertThat(future).isCompletedExceptionally()
                  .isNotCancelled();

Deprecate hasFailedWithThrowableThat() CompletableFuture assertion in favor failsWithin:

// deprecated
CompletableFuture future = new CompletableFuture();
future.completeExceptionally(new RuntimeException("boom!"));

assertThat(future).hasFailedWithThrowableThat().isInstanceOf(RuntimeException.class);
                                               .hasMessage("boom!");
// instead calls
assertThat(future).failsWithin(1, TimeUnit.SECONDS)
                  .withThrowableOfType(RuntimeException.class)
                  .withMessage("boom!");

Please note that the semantics of a failure in failsWithin differs from hasFailedWithThrowableThat, failsWithin tries to get the future after the given duration and return the exception that led to its failure while hasFailedWithThrowableThat checks the future is completed exceptionnaly and was not cancelled.

Deprecate hasNotFailed() CompletableFuture assertion:

CompletableFuture future = new CompletableFuture();
future.cancel(true);
// deprecated
assertThat(future).hasNotFailed();
// instead calls
assertThat(future).matches (f -> f.isNotCompletedExceptionally() || f.isCancelled());

Add hasPackage to Class assertions

Verifies that the actual Class under test has the given package name.

Example:

package one.two;

class MyClass {}

assertThat(MyClass.class).hasPackage("one.two")
                         .hasPackage(Package.getPackage("one.two"));

Add isCloseTo to java.time.Duration assertions

Verifies that the actual Duration is close to the given one within the given allowed difference (assertion succeeds if difference = allowed difference).

This is equivalent of: abs(actual - expected) ≤ allowed difference.

For readability, Assertions.withMarginOf(Duration) can be used to express the allowed difference.

Examples:

Duration twoMinutes = Duration.ofMinutes(2);

assertThat(twoMinutes).isCloseTo(Duration.ofMinutes(3), Duration.ofMinutes(5));
assertThat(twoMinutes).isCloseTo(Duration.ofMinutes(-3), Duration.ofMinutes(10));
assertThat(twoMinutes).isCloseTo(Duration.ofMinutes(3), Duration.ofMinutes(1));

// assertions using withMarginOf syntactic sugar
assertThat(twoMinutes).isCloseTo(Duration.ofMinutes(3), withMarginOf(Duration.ofMinutes(5)));
assertThat(twoMinutes).isCloseTo(Duration.ofMinutes(3), withMarginOf(Duration.ofMinutes(1)));

Add failsWithin to Future and CompletableFuture assertionss

Checks that the Future/CompletableFuture does not complete within the given time and returns the exception that caused the failure for further (exception) assertions, the exception can be any of InterruptedException, ExecutionException, TimeoutException or CancellationException as per Future.get(long, TimeUnit) behaviour.

WARNING

failsWithin does not fully integrate with soft assertions, if the future completes the test will fail immediately (the error is not collected as a soft assertion error), if the assertion succeeds the chained assertions are executed and any errors will be collected as a soft assertion errors. The rationale is that if we collect failsWithin error as a soft assertion error, the chained assertions would be executed but that does not make sense since there is no exception to check as the future has completed.

Examples:

ExecutorService executorService = Executors.newSingleThreadExecutor();

Future<String> future = executorService.submit(() -> {
  Thread.sleep(100);
  return "ook!";
});

// assertion succeeds as the future is not completed after 50ms
assertThat(future).failsWithin(Duration.ofMillis(10))
                  .withThrowableOfType(TimeoutException.class);

// alternative assertion syntax, the time out is expressed with a TimeUnit value
assertThat(future).failsWithin(10, TimeUnit.MILLISECONDS);


// fails as the future is completed within 200ms
assertThat(future).failsWithin(Duration.ofMillis(200));

Improve isTrue/isFalse assertions error messages

Before:

Expecting:
 <false>
to be equal to:
 <true>
but was not.

After:

Expecting value to be true but was false

Add hasValueSatisfying to AtomicReference assertions

Verifies that the atomic under test has a value satisfying the given predicate.

Examples:

assertThat(new AtomicReference("foo")).hasValueMatching(result -> result != null);

// you can pass a description for the predicate that will be used in the error message
assertThat(new AtomicReference("foo")).hasValueMatching(result -> result != null, "expected not null");

Add hasValueSatisfying to AtomicReference assertions

Verifies that the atomic under test has a value satisfying the given requirements.

Example:

assertThat(new AtomicReference("foo")).hasValueSatisfying(result -> assertThat(result).isNotBlank());
2.9.10. AssertJ Core 3.17.2

Release date: 2020-09-06

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio and BJ Hargrave.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Change precedence of assumption classes when raising the assumption exception:

Old order: org.opentest4j.TestAbortedException, org.testng.SkipException and org.junit.AssumptionViolatedException

New order: org.testng.SkipException, org.junit.AssumptionViolatedException and org.opentest4j.TestAbortedException

 Improvements

Handle soft proxies for custom assert classes in OSGi bundles. (BJ Hargrave)

Internal: Add OSGi integration tests. (BJ Hargrave)

Internal: Fix maven-shade-plugin warning about overlapping MANIFEST.MF. (Stefano Cordio)

Internal: Exclude net.bytebuddy.experimental from shading scope. (Stefano Cordio)

Internal: Bump mockito version from 3.5.5 to 3.5.10. (Erhard Pointl, Stefano Cordio)

 Fixed

Fix: assumptions were broken in JUnit4 when opentest4j is in the classpath. (Stefano Cordio)

2.9.11. AssertJ Core 3.17.1

Release date: 2020-08-30

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, rpolton, Andrey Nudko and Davide Angelocola.

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Change precedence of assumption classes when raising the assumption exception:

Old order: org.junit.AssumptionViolatedException, org.opentest4j.TestAbortedException and org.testng.SkipException

New order: org.opentest4j.TestAbortedException, org.testng.SkipException and org.junit.AssumptionViolatedException

 Improvements

Speed up recursive comparison by caching results of Method lookup performed by reflection and using conditions instead of catching exceptions. (Andrey Nudko)

Make contains and containsOnly assertions to work for iterables that can be traversed only once. (rpolton)

Minor code cleanup. (Davide Angelocola)

Internal: Add Java 16 EA build. (Stefano Cordio)

 Fixed

Fix Object2DArrayAssert#isDeepEqualTo(). (Stefano Cordio)

2.9.12. AssertJ Core 3.17.0

Release date: 2020-08-23

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, Junhao Liang, Bibibiu, Andrey "Bass" Shcheglov, SuntCrick, Yubin Hu, rpolton, Ting Sun, Peng Weiyuan, Brummolix, Maciej Wajcht, Hayden Meloche, Cal027, sullis, mgrafl, Rupert Madden-Abbott, Shiva, Ahmad M, Phillip Webb and BJ Hargrave.

Joel Costigliola: Apologies to Hayden Meloche, when integrating his work the final squashed commit was pushed with me as the author instead of him, sorry Hayden!

 Binary compatibility

The release is not binary compatible with the previous minor version.

 Breaking changes

Make the recursive comparison to ignore all overridden equals by default as most users were confused by it, call usingOverriddenEquals to revert to the previous behaviour.

Improve AssertionFailedError by replacing actual and expected by their representation as some default toString are not great (arrays for example).

Make Offset, MapEntry, Percentage, FieldLocation and Index final.

Add 2D array assertions, which provide new and potentially different methods for existing array assertions having two-dimensional arguments.

 New features

Add java.time.Period assertions. (Hayden Meloche)

Allow printing or consuming assertions description.

Add assertThatNoException().isThrownBy(code) assertion (and also thenNoException()). (Phillip Webb)

Add isNotEqualTo() to RecursiveComparisonAssert. (Junhao Liang)

Add JUnit 5 SoftlyExtension to set up SoftAssertions field and automatically call assertAll() after each test. (Bibibiu)

Add lazy error message overriding to only build the message when the assertion fails. (Yubin Hu)

Add usingRecursiveFieldByFieldElementComparator(RecursiveComparisonConfiguration) to get the recursive api full power to all iterable assertions.

Add isEmpty to InputStream assertion. (Peng Weiyuan)

Add isNotEmpty to InputStream assertion. (Peng Weiyuan)

Add doesNotContainIgnoringCase to CharSequence assertions. (Brummolix)

Add primitive and Object 2D array assertions. (Maciej Wajcht)

Add isEven/isOdd assertions for byte, short, int and long. (Cal027)

Soft assertions: add a way to react to collected assertion error.

Add singleElement() and singleElement(InstanceOfAssertFactory) to iterable assertions (it replaces hasOnlyOneElementSatisfying). (mgrafl)

Add filteredOn(Function, expectedValue) to Iterable, Object[] and AtomicReferenceArray assertions. (mgrafl)

Add succeedsWithin to Future and CompletableFuture assertions. (Rupert Madden-Abbott)

 Improvements

Allow specifying equals BiPredicate instead of Comparator in recursive comparison.

Display the beginning and the end of huge iterables/array/map instead of just the beginning. (SuntCrick)

Handle infinite or singly-traversable iterables for sequences assertions. (rpolton) - see #1938 for details.

Explicitly set Javadoc locale to English. (Erhard Pointl)

Make Percentage and FieldLocation final, update equals() and hashCode(). (Ahmad M)

Make Offset, MapEntry and Index final, update equals() and hashCode(). (Stefano Cordio)

Javadoc improvements. (Stefano Cordio, Erhard Pointl)

Better handle soft proxies for custom assert classes in OSGi bundles. (BJ Hargrave)

Best effort to avoid cycles when representing iterables or object arrays.

Internal: Refactor urls test classes. (SuntCrick)

Internal: Add tests for hasNoPath URL/URI assertions. (Ting Sun)

Internal: Bump equalsverifier from 3.2 to 3.4.2.

Internal: Bump commons-io from 2.6 to 2.7.

Internal: Bump commons-lang3 from 3.10 to 3.11.

Internal: Bump bnd version from 5.0.1 to 5.1.2 and re-enable java 15 build. (Pascal Schumacher)

Internal: Bump maven-shade-plugin from 3.2.3 to 3.2.4.

Internal: Bump byte-buddy version from 1.10.10 to 1.10.14.

Internal: Bump mockito version from 3.3.3 to 3.5.5 (Erhard Pointl)

Internal: Add dependabot. (sullis)

Internal: Bump actions/cache from v1 to v2.

Internal: Fix "Remove this 'public' modifier" sonar violations. (Erhard Pointl, Shiva)

Internal: Make Longs_assertIsOne_Test#should_succeed_since_actual_is_one testing assertIsOne. (Erhard Pointl)

Internal: Make IterableAssert_anyMatch_Test testing anyMatch and IterableAssert_anySatisfy_Test testing anySatisfy. (Erhard Pointl)

Internal: Add missing ObjectArrayAssert_anySatisfy_Test test. (Erhard Pointl)

Internal: Fix mockito warnings. (Erhard Pointl)

Internal: Disable shallow clone during Sonar analysis. (Stefano Cordio)

Internal: Clean up code. (Stefano Cordio, Erhard Pointl)

 Fixed

AbstractByteArrayAssert#asString now build a new String with the default or a given charset instead returning the byte array toString.

Allow soft assertion failures to be recorded from multiple threads. (Andrey "Bass" Shcheglov)

Fix containsExactly assertion that failed for iterable that can only be read once. (rpolton)

Fix references to main branch after master was renamed to main to support Black Lives Matter. (Steven Crockett)

Fix Recursive comparison that did not compare enums as they don’t have fields, now it compares enums with equals.

 Deprecated

hasOnlyOneElementSatisfying(Consumer<? super ELEMENT> elementAssertions) has been deprecated in favor of singleElement()

Deprecate all non recursive field by field comparison assertions in favor of the recursive comparison ones:

isEqualToComparingFieldByField

isEqualToIgnoringNullFields

isEqualToComparingOnlyGivenFields

Deprecate AssertionErrorMessagesAggregrator in favor of AssertionErrorMessagesAggregator. (Ahmad M)

Add java.time.Period assertions

Provides the following assertions for the Period:

hasDays(int expectedDays): Verifies that the actual Period has the given days.

hasMonths(int expectedMonths): Verifies that the actual Period has the given months.

hasYears(int expectedYears): Verifies that the actual Period has the given years.

isNegative(): Verifies that the actual Period is negative (i.e. is less than Period.ZERO).

isPositive(): Verifies that the actual Period is positive (i.e. is greater than Period.ZERO).

Examples:

assertThat(Period.ofYears(5)).hasYears(5);

assertThat(Period.ofMonths(5)).hasMonths(5);

assertThat(Period.ofDays(5)).hasDays(5)
                            .isPositive();

assertThat(Period.ofMonths(-5)).isNegative();

Display the beginning and the end of huge iterables/array/map

Before this version only the first maxElementsForPrinting elements would be displayed, now the maxElementsForPrinting displayed elements are split between first and last elements.

The number of elements to display can be set with Assertions.setMaxElementsForPrinting(n);

Example:

// 6 elements array
String[] greatBooks = {"A Game of Thrones", "The Lord of the Rings", "Assassin's Apprentice",
                       "Guards! Guards!", "The Lies of Locke Lamora", "Aux Ombres d’Abyme"};

// limit the number of elements to display/print to 4
Assertions.setMaxElementsForPrinting(4);

// formatted as:
["A Game of Thrones", "The Lord of the Rings", ... "The Lies of Locke Lamora", "Aux Ombres d’Abyme"]

Add isEmpty to InputStream assertion

Verifies whether the content of the actual InputStream is empty.

Examples:

// assertion will pass
assertThat(new ByteArrayInputStream(new byte[] {})).isEmpty());

// assertions will fail
assertThat(new ByteArrayInputStream(new byte[] {0xa})).isEmpty();

Add isNotEmpty to InputStream assertion

Verifies that the content of the actual InputStream is not empty.

Examples:

// assertion will pass
assertThat(new ByteArrayInputStream(new byte[] {0xa})).isNotEmpty());

// assertions will fail
assertThat(new ByteArrayInputStream(new byte[] {})).isNotEmpty();

Add doesNotContainIgnoringCase to CharSequence assertions

Verifies that the actual CharSequence does not contain any of the given values, ignoring case considerations.

Example:

// assertions will pass
assertThat("Frodo").doesNotContainIgnoringCase("pippin")
                   .doesNotContainIgnoringCase("Merry", "sam");

// assertions will fail
assertThat("Frodo").doesNotContainIgnoringCase("Fro", "Gimli", "Legolas");
assertThat("Frodo").doesNotContainIgnoringCase("fro");

primitive and Object 2D array assertions

The following assertions are available 2D arrays, here they are for int[][]:

isEqualTo(Object expected): Verifies that the actual int[][] is equal to the given one.

isDeepEqualTo(int[][] expected): Verifies that the actual 2D array is deeply equal to the given one.

isEmpty(): Verifies that the actual array is empty, i.e the array has no elements, said otherwise it can have any number of rows but all rows must be empty.

isNullOrEmpty(): Verifies that the actual array is null or empty, empty means the same as isEmpty().

isNotEmpty(): Verifies that the actual array is not empty, i.e. the array has at least one element.

contains(int[] value, Index index): Verifies that the actual array contains the given int[] at the given index.

doesNotContain(int[] value, Index index): Verifies that the actual array does not contain the given value at the given index.

hasDimensions(int expectedFirstDimension, int expectedSecondDimension): Verifies that the actual 2D array has the given dimensions.

hasSameDimensionsAs(Object array): Verifies that the actual int[][] has the same dimensions as the given array.

The same assertions are available for long[][], short[][], byte[][], float[][], double[][], boolean[][] and Object[][] (obviously replacing int by the array type).

Object[][] assertions are generic, they take a parameter type, ex: isDeepEqualTo(ELEMENT[][] expected).

The migration path from one-dimensional array assertions is the following:

Before 3.17.0	After 3.17.0


contains(ELEMENT, Index)

	

contains(ELEMENT[], Index)




doesNotContain(ELEMENT, Index)

	

doesNotContain(ELEMENT[], Index)




hasSameSizeAs(Iterable)

	

hasSameDimensionsAs(Object)




hasSize(int)

	

hasDimensions(int, int)




isEmpty()

	

isEmpty()




isEqualTo(Object)

	

isEqualTo(Object)




isNotEmpty()

	

isNotEmpty()




isNullOrEmpty()

	

isNullOrEmpty()

The remaining one-dimensional array assertions do not have a direct replacement. Please raise a feature request if there is any use case for them.

Add isEven/isOdd assertions for byte, short, int and long

Verifies whether the given byte, short, int and or long is even/odd.

Examples:

assertThat(12).isEven();
assertThat(-46).isEven();

assertThat(3).isOdd();
assertThat(-17).isOdd();

Add singleElement to iterable assertions

singleElement() and singleElement(InstanceOfAssertFactory assertFactory) verify that the Iterable under test contains a single element and allow to perform assertions on that element (this is a shorthand for hasSize(1).first()).

You can only chain Object assertions after singleElement(), to get strongly typed assertions, use singleElement(InstanceOfAssertFactory) and pass the proper InstanceOfAssertFactory.

Examples:

import static org.assertj.core.api.InstanceOfAssertFactories.STRING;
import static org.assertj.core.api.Assertions.as; // syntactic sugar

List<String> babySimpsons = list("Maggie");

// assertion succeeds, only Object assertions are available after singleElement()
assertThat(babySimpsons).singleElement()
                        .isEqualTo("Maggie");

// String assertion succeeds, String assertions as we have passed InstanceOfAssertFactories.STRING
assertThat(babySimpsons).singleElement(as(STRING))
                        .startsWith("Mag");

Add succeedsWithin to Future and CompletableFuture assertions

succeedsWithin waits if necessary for at most the given time for this future to complete and then returns its result for further assertions.

If the future’s result is not available for any reason an assertion error is thrown.

To get assertions for the future result’s type use the method taking an additionnal InstanceOfAssertFactory parameter instead.

Examples:

ExecutorService executorService = Executors.newSingleThreadExecutor();

Future<String> future = executorService.submit(() -> {
  Thread.sleep(100);
  return "ook!";
});

// assertion succeeds
assertThat(future).succeedsWithin(200, TimeUnit.MILLISECONDS)
                  .isEqualTo("ook!");

// same assertion with a Duration to express the time out
Duration timeout = Duration.ofMillis(200);
assertThat(future).succeedsWithin(timeout)
                  .isEqualTo("ook!");

// fails as the future is not done after the given timeout
assertThat(future).succeedsWithin(50, TimeUnit.MILLISECONDS);

Examples with stronly typed assertions and CompletableFuture:

import static org.assertj.core.api.InstanceOfAssertFactories.STRING;
import static org.assertj.core.api.Assertions.as; // syntactic sugar

CompletableFuture<String> future = CompletableFuture.completedFuture("ook!");

Duration timeout = Duration.ofMillis(200);

// strongly typed assertion:
assertThat(future).succeedsWithin(timeout, as(STRING))
                  .contains("ok");

// same assertion with the timeout expressed differently:
assertThat(future).succeedsWithin(200, TimeUnit.MILLISECONDS, as(STRING))
                  .contains("ok");

Add filteredOn(Function, expectedValue) to Iterable, Object[] and AtomicReferenceArray assertions

Filters the iterable under test keeping only elements for which the result of the function is equal to expectedValue.

It allows to filter elements more safely than by using filteredOn(String, Object) as it doesn’t utilize introspection.

As an example, let’s check all employees 800 years old (yes, special employees): Examples:

Employee yoda   = new Employee(1L, new Name("Yoda"), 800);
Employee obiwan = new Employee(2L, new Name("Obiwan"), 800);
Employee luke   = new Employee(3L, new Name("Luke", "Skywalker"), 26);
Employee noname = new Employee(4L, null, 50);

List<Employee> employees = newArrayList(yoda, luke, obiwan, noname);

assertThat(employees).filteredOn(Employee::getAge, 800)
                     .containsOnly(yoda, obiwan);

assertThat(employees).filteredOn(e -> e.getName(), null)
                     .containsOnly(noname);
2.9.13. AssertJ Core 3.16.1

Release date: 2020-05-09

 Contributors

Thanks to Erhard Pointl and Eddú Meléndez Gonzales for their contributions.

 Fixed

Fix NPE in recursive comparison when checking local or anonymous classes. (#1868)

Fix assertThat(Duration actual) Javadoc. (Eddú Meléndez Gonzales)

2.9.14. AssertJ Core 3.16.0

Release date: 2020-05-05

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, Wim Deblauwe, Fabien Duminy, Piotrek Żygieło, Indrek Priks, Jakzi666, Daniel Avila, Harisha Talanki, Grzegorz Piwowarek, Andreas Mager, Sunt-ing, ebundy, Stefan Birkner, WuYff, Cal027, Yubin Hu and Fr Jeremy Krieg.

 Breaking changes

AbstractSoftAssertions is now abstract

The following base soft assertions classes were changed to interfaces (with default methods) and renamed:

AbstractBDDSoftAssertions was renamed to BDDSoftAssertionsProvider

AbstractStandardSoftAssertions was renamed to StandardSoftAssertionsProvider

Java6AbstractBDDSoftAssertions was renamed to Java6BDDSoftAssertionsProvider

Java6AbstractStandardSoftAssertions was renamed to Java6StandardSoftAssertionsProvider

Move ThrowingCallable from AbstractSoftAssertions to SoftAssertionsProvider.

 New features

Allow combining soft assertions entry points. (Fr Jeremy Krieg)

Support injecting custom soft assertions in JUnit 5 SoftAssertionExtension. (Fr Jeremy Krieg)

Add assertions on the cause and root cause exception message. (Wim Deblauwe)

Recursive comparison learned to ignore null fields from the expected object.

Recursive comparison learned to ignore all actual empty optional fields.

Add assertion to compare string ignoring punctuation and normalizing whitespaces. (Harisha Talanki)

Add isBase64 to String assertions. (Stefano Cordio)

Add decodedAsBase64 to String assertions. (Stefano Cordio)

Add encodedAsBase64 to byte[] assertions. (Stefano Cordio)

Add java.util.concurrent.atomic.LongAdder assertions. (Grzegorz Piwowarek)

Add asHexString to byte[] assertions. (Andreas Mager)

Add isEqualToWithSortedQueryParameters to URL assertions. (Sunt-ing)

Add isDirectoryRecursivelyContaining to File/Path assertions. (ebundy)

Add hasBinaryContent to InputStream assertions. (Stefan Birkner)

Add containsOnlyOnceElementsOf to Iterable/Object array/AtomicReferenceArray assertions. (Cal027)

 Improvements

ByteArrayAssert.containsExactly(byte…​) error message now mentions not found and unexpected elements. (Indrek Priks)

In "should be package private" class assertion, the error message now explicitly mentions package-private instead of a blank value.

Use primitive comparison in Float and Double isNotEqualTo when compared to primitive float/double values.

Disambiguate colliding date/time representation.

Support up to four arguments for satisfiesAnyOf(). (Jakzi666)

Clarify the error message when comparing float/double NaN with ==.

Use a more descriptive element’s name in ShouldContain/ShouldContainOnly error message. (WuYff)

Add short array assertions taking int…​. (Daniel Avila)

Use AssertJ site theme for Javadoc.

Improve converting JUnit/JUnit5 assertions to AssertJ. (Yubin Hu)

Move core extracting features from AbstractObjectAssert to AbstractAssert, making them available for custom assertions. (Stefano Cordio)

Improve line number accuracy in soft assertion error messages. (Stefano Cordio)

Internal: introduce EqualsVerifier for internal tests. (Stefano Cordio)

Internal: optimize Charset finding in tests. (Fabien Duminy)

Internal: clean up unused imports (Erhard Pointl, Piotrek Żygieło, Stefano Cordio, Pascal Schumacher)

Internal: use static imports. (Piotrek Żygieło)

Internal: remove unnecessary type parameters from extractors. (Stefano Cordio)

Internal: access assertion info directly in AtomicLongAssert/AtomicIntegerAssert. (Grzegorz Piwowarek)

Re-enable Sonar reports. (Stefano Cordio)

Update ByteBuddy to version 1.10.10.

Update JUnit Jupiter to version 5.6.2 (still optional).

 Fixed

Fix infinite recursion in recursive comparison when dealing with Path. (#1855)

Fix recursive comparison way of tracking already visited objects. (#1854)

Fix typos (Wim Deblauwe, Stefano Cordio)

 Deprecated

Deprecate areEqual() and areEqualArrays() in org.assertj.core.util.Objects.

Deprecate temporaryFolder() in org.assertj.core.util.Files. (Sunt-ing)

Add java.util.concurrent.atomic.LongAdder assertions

The following java.util.concurrent.atomic.LongAdder assertions are available:

hasValue(long expected), which verifies that the actual LongAdder sum has the given value.

doesNotHaveValue(long unexpected), which verifies that the actual LongAdder sum has not the given value.

All the assertions provided by NumberAssert, using the LongAdder sum as actual value.

All the assertions provided by ComparableAssert, using the LongAdder sum as actual value.

Comparison ignoring punctuation and normalizing whitespaces

Verifies that the actual CharSequence is equal to the given one, after the punctuation of both strings have been normalized.

To be exact, the following rules are applied:

All punctuation of actual and expected strings are ignored and whitespaces are normalized

Punctuation is any of the following characters: !"#$%&'()*+,-./:;=<>?@[\]^_{|}~\`

Examples:

// assertions succeed:
assertThat("Game'of'Thrones").isEqualToNormalizingPunctuationAndWhitespace("GameofThrones")
assertThat("Game of Throne's").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat(":Game of Thrones:").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat(":Game-of-Thrones:").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat("Game of Thrones?").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat("Game of Thrones!!!").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat("Game of  {{(!)}}    Thrones!!!").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones")
assertThat("{(Game)-(of)-(Thrones)!!!}").isEqualToNormalizingPunctuationAndWhitespace("GameofThrones");

// assertions fail:
assertThat("Game-of-Thrones").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones");
assertThat("{Game:of:Thrones}").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones");
assertThat("{(Game)-(of)-(Thrones)!!!}").isEqualToNormalizingPunctuationAndWhitespace("Game of Thrones");

isBase64

Verifies that the given String is a valid Base64 encoded string. (this is not available for CharSequence).

Examples:

// assertions succeeds
assertThat("QXNzZXJ0Sg==").isBase64();

// assertion succeeds even without padding as it is optional by specification
assertThat("QXNzZXJ0Sg").isBase64();

// assertion fails as it has invalid Base64 characters
assertThat("inv@lid").isBase64();

decodedAsBase64

Decodes the actual String value as a Base64 encoded string, the decoded bytes becoming the new array under test.

Examples:

// assertions succeeds
assertThat("QXNzZXJ0Sg==").decodedAsBase64()
                          .containsExactly("AssertJ".getBytes());

// assertion succeeds even without padding as it is optional by specification
assertThat("QXNzZXJ0Sg").decodedAsBase64()
                        .containsExactly("AssertJ".getBytes());

// assertion fails as it has invalid Base64 characters
assertThat("inv@lid").decodedAsBase64();

Add asHexString to byte[] assertions

Converts the actual byte array under test to an hexadecimal String and returns assertions for the computed String allowing String specific assertions from this call.
The hexadecimal String representation is in upper case.

Example :

byte[] bytes = new byte[] { -1, 0, 1 };

// assertion will pass
assertThat(bytes).asHexString()
                 .startsWith("FF")
                 .isEqualTo("FF0001");

Add isEqualToWithSortedQueryParameters] to URL assertions

Verifies that the actual URL is equivalent to the given one after their parameters are sorted.

Example :

URL url = new URL("http://example.com?a=b&c=d");

// these assertions succeed ...
assertThat(url).isEqualToWithSortedQueryParameters(new URL("http://example.com?c=d&a=b"))
               .isEqualToWithSortedQueryParameters(new URL("http://example.com?a=b&c=d"));

// ... but this one fails as parameters do not match.
assertThat(url).isEqualToWithSortedQueryParameters(new URL("http://example.com?a=b&c=e"));

//... and this one fails as domains are different.
assertThat(url).isEqualToWithSortedQueryParameters(new URL("http://example2.com?amp;a=b&c=d"));

Add isDirectoryRecursivelyContaining to File/Path assertions

Verify that the actual File/Path directory or any of its subdirectories (recursively) contains at least one file matching the given criteria expressed as:

a String interpreted as a path matcher (as per FileSystem.getPathMatcher(String))

a String interpreted as a path matcher (as per FileSystem.getPathMatcher(String))

These assertions are similart to isDirectoryContaining but recursively go into subdirectories.

Note that the actual File/Path must exist and be a directory.

Examples with files given the following directory structure:

root
|—— foo
|    |—— foobar
|         |—— foo-file-1.ext
|—— foo-file-2.ext

Examples with syntax patterns:

File root = new File("root");

// The following assertions succeed:
assertThat(root).isDirectoryRecursivelyContaining("glob:**foo")
                .isDirectoryRecursivelyContaining("glob:**ooba*")
                .isDirectoryRecursivelyContaining("glob:**file-1.ext")
                .isDirectoryRecursivelyContaining("regex:.*file-2.*")
                .isDirectoryRecursivelyContaining("glob:**.{ext,dummy}");

// The following assertions fail:
assertThat(root).isDirectoryRecursivelyContaining("glob:**fooba");
assertThat(root).isDirectoryRecursivelyContaining("glob:**.bin");
assertThat(root).isDirectoryRecursivelyContaining("glob:**.{java,class}");

Examples with predicates:

File root = new File("root");

// The following assertions succeed:
assertThat(root).isDirectoryRecursivelyContaining(file -> file.getName().startsWith("foo-file-1"))
                .isDirectoryRecursivelyContaining(file -> file.getName().endsWith("file-2.ext"))
                .isDirectoryRecursivelyContaining(file -> file.getName().equals("foo"))
                .isDirectoryRecursivelyContaining(file -> file.getParentFile().getName().equals("foo"))

// The following assertions fail:
assertThat(root).isDirectoryRecursivelyContaining(file -> file.getName().equals("foo-file-1"))
assertThat(root).isDirectoryRecursivelyContaining(file -> file.getName().equals("foo/foobar"));

Add hasBinaryContent to InputStream assertions

Verifies that the binary content of the actual InputStream is exactly equal to the given one.

Example: the following failing assertion …​

InputStream inputStream = new ByteArrayInputStream(new byte[] {1, 2});

// assertion will pass
assertThat(inputStream).hasBinaryContent(new byte[] {1, 2});

// assertions will fail
assertThat(inputStream).hasBinaryContent(new byte[] { });
assertThat(inputStream).hasBinaryContent(new byte[] {0, 0});

Add containsOnlyOnceElementsOf to Iterable/Object array/AtomicReferenceArray assertions

Verifies that the actual group contains the elements of the given iterable only once (same semantic as containsOnlyOnce(Object…​)).

Examples:

// assertions will pass
assertThat(list("winter", "is", "coming")).containsOnlyOnceElementsOf(list("winter"))
                                          .containsOnlyOnceElementsOf(list("coming", "winter"));

// assertions will fail
assertThat(list("winter", "is", "coming")).containsOnlyOnceElementsOf(list("Lannister"));
assertThat(list("Arya", "Stark", "daughter", "of", "Ned", "Stark")).containsOnlyOnceElementsOf(list("Stark"));
assertThat(list("Arya", "Stark", "daughter", "of", "Ned", "Stark")).containsOnlyOnceElementsOf(list("Stark", "Lannister", "Arya"));

Disambiguate colliding date/time representation

Different date/time types can be represented the same way (LocalDateTime and Date for example) which makes it difficult to understand error messages as they don’t show any difference between actual and expected values. AssertJ now adds the date/time type name for types whose representation may collide.

Example: the following failing assertion …​

Date now = new Date();
Object localDateTime = LocalDateTime.ofInstant(now.toInstant(), ZoneId.systemDefault());

assertThat(List.of(localDateTime)).containsExactly(now);

... fails with this error:

Expecting:
  <[2020-03-19T22:32:42.875 (java.time.LocalDateTime)]>
to contain exactly (and in same order):
  <[2020-03-19T22:32:42.875 (java.util.Date)]>
but some elements were not found:
  <[2020-03-19T22:32:42.875 (java.util.Date)]>
and others were not expected:
  <[2020-03-19T22:32:42.875 (java.time.LocalDateTime)]>

Before that the error would have been confusing:

Expecting:
  <[2020-03-19T22:32:42.875]>
to contain exactly (and in same order):
  <[2020-03-19T22:32:42.875]>
but some elements were not found:
  <[2020-03-19T22:32:42.875]>
and others were not expected:
  <[2020-03-19T22:32:42.875]>
2.9.15. AssertJ Core 3.15.0

Release date: 2020-01-28

The recursive comparison API has been promoted and is not a beta API anymore.

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Pascal Schumacher, BJ Hargrave, Raymond Augé, Thomas Weißschuh, Maciej Wajcht, Hayden Meloche, Filip Hrisafov, Jayati Goyal, Gyumin Kim, Clemens Grabmann, Roman Leventov, Fr Jeremy Krieg, Benoit Dupont, Nikolaos Georgiou, Christian Stein, Jeremy Landis, Graham Dennis, Fabien Duminy, Tommy Situ and Vincent Ricard.

Shout out to Vincent Ricard for the various tests refactoring, that was quite a lot of work!

 Breaking changes

Compares OffsetDateTime, ZonedDateTime and LocalDateTime using their timeLineOrder() comparator as default.

For OffsetDateTime the timeLineOrder comparator only compares the underlying instant and ignores different timezones / offsets / chronologies.

For ZonedDateTime the timeLineOrder comparator ignores the chronology, this is equivalent to comparing the epoch-second and nano-of-second.

For LocalDateTime the timeLineOrder comparator ignores the chronology, this is equivalent to comparing the epoch-day and nano-of-day and allows dates in different calendar systems to be compared based on the position of the date-time on the local time-line.

A single Path parameter for containsOnlyKeys in Map assertions is treated as a single key rather than an Iterable of keys.

Fix floating point comparison behavior in DoubleAssert and FloatAssert, which now follows primitive comparison (==, ≤, ≥) when the expected value is primitive but uses the corresponding equals semantic when the expected value is a wrapper.

Fix a double decoding issue in UriAssert, which now uses the raw query to evaluate URI parameters avoiding the mishandling of escaped & and =. (Graham Dennis)

Remove duplication for Descriptable implementations using default methods. This is a binary incompatible change. (Fr Jeremy Krieg)

 New features

Add java.time.Duration assertions. (Filip Hrisafov)

Add isPackagePrivate to Class assertions. (Hayden Meloche)

Add hasSameBinaryContentAs to File/Path assertions. (Nikolaos Georgiou)

Add succeedsWithin to CompletableFuture assertions.

Add hasSuperclass to Class assertions. (Stefano Cordio)

Add hasNoSuperclass to Class assertions. (Stefano Cordio)

Make the recursive comparison API directly available to Iterable, Map, Optional and array assertions.

Allow to ignore fields by type in the recursive comparison. (Tommy Situ)

 Improvements

Show explicitly if a class is package-private in ClassModifierShouldBe error message.

Various module descriptor improvements: (Christian Stein and Stefano Cordio)

Remove JSR-305 due to issues with java 9 modules. (Stefano Cordio)

Remove .core.internal from exported packages. (Stefano Cordio)

Update ByteBuddy to version 1.10.6.

Update JUnit to version 4.13 (still optional).

Update JUnit Jupiter to version 5.6.0 (still optional).

Make OSGi import of jdk.* packages optional. (BJ Hargrave)

Use bnd 5.0.0 to a) use -noclassforname instruction b) generate most up to date OSGi metadata c) add verification that additional package imports never sneak in. (Raymond Augé)

Get rid of unnecessary extra arguments in String.format. (Erhard Pointl)

Unify actual and expected formatting in hasToString() error which is now AssertionFailedError to allow visual comparison. (Thomas Weißschuh)

Add missing BDD assertions for exception handling (thenExceptionOfType, thenNullPointerException, thenIllegalArgumentException, thenIOException and thenIllegalStateException). (Maciej Wajcht)

Rewrite LocalDateAssert, LocalDateTimeAssert, LocalTimeAssert and OffsetDateTimeAssert tests to be more compliant with the contribution guidelines. (Clemens Grabmann)

Remove IntelliJ IDEA configuration file for Language Injection as the rules are part of the built-in configuration since IntelliJ IDEA 2019.3. (Stefano Cordio)

Improve performance of containsOnly() on very large collections. (Roman Leventov)

Configure GitHub Actions for Windows and MacOS. (Filip Hrisafov)

Use parameterized tests for assertHasParameter() in URI assertions. (Stefano Cordio)

Show the stack trace of the Throwable under test when hasMessageContaining and hasMessageContainingAll fails. (Benoit Dupont)

Bump maven wrapper to 0.5.6. (Jeremy Landis)

Improve the representation of failed CompletableFuture showing the exception that caused the failure.

Use Objects.requireNonNull instead of manually creating NullPointerExceptions. (Pascal Schumacher)

Remove unused methods. (Fabien Duminy)

Replace try/catch exception assertion with catchThrowable pattern. (Vincent Ricard)

Remove failBecauseExpectedAssertionErrorWasNotThrown. (Vincent Ricard)

Replace the TestFailures helper class by the catchThrowable pattern. (Vincent Ricard)

Update license year to 2020.

 Fixed

Fix grammatical errors in README.md (Jayati Goyal)

Fix allOf(Iterable) and anyOf(Iterable) that no longer tracked descriptions when built with an Iterable<Condition>.

Fix typos in Javadoc and comments. (Erhard Pointl)

Add abstract modifier for Java6AbstractStandardSoftAssertions. (Stefano Cordio)

Fix typo in Javadoc. (Gyumin Kim)

Fix how Enum are compared in recursive comparison which now compares them by value.

Fix tests failing only on Windows. (Fr Jeremy Krieg)

Refactoring: remove useless null check. (Pascal Schumacher)

Fix use equals to compare enum names in recursive comparison.

Fix how containsOnlyKeys in MapAssert considers a single Path parameter, which is now treated as a single key rather than an Iterable of keys. (Stefano Cordio)

Fix the recursive comparison that used to register fields of objects with overridden equals when it should not have to.

Fix property and field extraction with Map input, which now tries at first to extract a property or a field by name and only in case of failure uses the input name as a Map key. (Stefano Cordio)

 Deprecated

Deprecate hasSameContentAs in favor of hasSameTextualContentAs and the new hasSameBinaryContentAs.

Deprecate Preconditions#checkNotNull(Object) in favor of Objects.requireNonNull(Object).

Deprecate Preconditions#checkNotNull(Object, String) in favor of Objects.requireNonNull(Object, String).

Add java.time.Duration assertions

The following java.time.Duration assertions are available:

hasDays(long otherDays): Verifies that the actual Duration has the given days.

hasHours(long otherHours): Verifies that the actual Duration has the given hours.

hasMillis(long otherMillis): Verifies that the actual Duration has the given millis.

hasMinutes(long otherMinutes): Verifies that the actual Duration has the given minutes.

hasNanos(long otherNanos): Verifies that the actual Duration has the given nanos.

hasSeconds(long otherSeconds): Verifies that the actual Duration has the given seconds.

isNegative(): Verifies that the actual Duration is negative (i.e. < Duration.ZERO)

isPositive(): Verifies that the actual Duration is positive (i.e. > Duration.ZERO)

isZero(): Verifies that the actual Duration is Duration.ZERO.

Examples:

assertThat(Duration.ofDays(5)).hasDays(5);
assertThat(Duration.ofHours(15)).hasHours(15);

assertThat(Duration.ofMinutes(65)).hasMinutes(65);
assertThat(Duration.ofSeconds(250)).hasSeconds(250);

assertThat(Duration.ofMillis(250)).hasMillis(250);
assertThat(Duration.ofNanos(145)).hasNanos(145);

assertThat(Duration.ofHours(5)).isPositive();
assertThat(Duration.ofMinutes(-15)).isNegative();
assertThat(Duration.ZERO).isZero();

Add isPackagePrivate to Class assertions

Verifies that the actual Class is package-private (i.e. has no modifier).

Example:

class MyClass {}

// this assertion succeeds:
assertThat(MyClass.class).isPackagePrivate();

// this assertion fails:
assertThat(String.class).isPackagePrivate();

Add hasSameBinaryContentAs to File/Path assertions

Verifies that the content of the actual file/path is equal to the content of the given one, the comparison is done at the binary level.

Example with Path (works the same with File):

// The first two paths have the same content, the third does not
Path aPath = Files.write(Paths.get("a-file.bin"), new byte[] { 42 });
Path bPath = Files.write(Paths.get("b-file.bin"), new byte[] { 42 });
Path cPath = Files.write(Paths.get("c-file.bin"), new byte[] { 24 });

// The following assertion succeeds:
assertThat(aPath).hasSameBinaryContentAs(bPath);

// The following assertion fails:
assertThat(aPath).hasSameBinaryContent(cPath);

Add succeedsWithin to CompletableFuture assertions

Waits if necessary for at most the given time for this future to complete, and then returns its result for futher assertions. If the future’s result is not available for any reason an assertion error is thrown.

The time to wait for can be expressed with a Duration or a TimeUnit.

To get assertions for the future result’s type use succeedsWithin that takes an additional InstanceOfAssertFactory parameter.

Examples:

CompletableFuture<String> future = CompletableFuture.completedFuture("ook!");

// assertion expressed with TimeUnit
assertThat(future).succeedsWithin(100, TimeUnit.MILLISECONDS)
                  .isEqualTo("ook!");

// same assertion with Duration
assertThat(future).succeedsWithin(Duration.ofMillis(100))
                  .isEqualTo("ook!");

// STRING is a static import of InstanceOfAssertFactories.STRING
// we can then chain String assertions
assertThat(future).succeedsWithin(100, TimeUnit.MILLISECONDS, STRING)
                  .startsWith("oo");

Add hasSuperclass to Class assertions

Verifies that the actual Class has the given superclass.

Example:

// this assertion succeeds:
assertThat(Integer.class).hasSuperclass(Number.class);

// this assertion succeeds as superclass for array classes is Object:
assertThat(Integer[].class).hasSuperclass(Object.class);

// this assertion fails:
assertThat(String.class).hasSuperclass(Number.class);

// this assertion fails as only direct superclass matches:
assertThat(String.class).hasSuperclass(Object.class);

// this assertion fails as interfaces are not superclasses:
assertThat(String.class).hasSuperclass(Comparable.class);

Add hasNoSuperclass to Class assertions

Verifies that the actual Class has no superclass.

Example:

// this assertion succeeds as interfaces have no superclass:
assertThat(Cloneable.class).hasNoSuperclass();

// this assertion succeeds as primitive types have no superclass:
assertThat(Integer.TYPE).hasNoSuperclass();

// this assertion succeeds as void type has no superclass:
assertThat(Void.TYPE).hasNoSuperclass();

// this assertion fails as Integer has Number as superclass:
assertThat(Integer.class).hasNoSuperclass();

Make recursive comparison API directly available to Iterable, Map, Optional and array assertions

Expose the recursive comparison for Iterable, Map, Optional and array assertions without having to cast them to Object as previously (because the API was only available for Object assertions).

At the moment, the only assertion available after in the recursive comparison is isEqualTo, there are plans to provide type specific recursive assertions in future (ex: iterable contains).

The recursive comparison API lets you finely control how to compare instances, please consult the documentation for a detailed guide.

For the following examples we use Person and Doctor, two classes with the same structure:

public class Person {
  String name;
  boolean hasPhd;
}

public class Doctor {
 String name;
 boolean hasPhd;
}

Doctor drSheldon = new Doctor("Sheldon Cooper", true);
Doctor drLeonard = new Doctor("Leonard Hofstadter", true);
Doctor drRaj = new Doctor("Raj Koothrappali", true);

Person sheldon = new Person("Sheldon Cooper", true);
Person leonard = new Person("Leonard Hofstadter", true);
Person raj = new Person("Raj Koothrappali", true);

Iterable example:

List<Doctor> doctors = list(drSheldon, drLeonard, drRaj);
List<Person> people = list(sheldon, leonard, raj);

// assertion succeeds as both lists contains equivalent items in order.
assertThat(doctors).usingRecursiveComparison()
                   .isEqualTo(people);

Array example:

Doctor[] doctors = { drSheldon, drLeonard, drRaj };
Person[] people = { sheldon, leonard, raj };

// assertion succeeds as both lists contains equivalent items in order.
assertThat(doctors).usingRecursiveComparison()
                   .isEqualTo(people);

Map example:

Map<String, Doctor> doctors = mapOf(entry(drSheldon.name, drSheldon),
                                    entry(drLeonard.name, drLeonard),
                                    entry(drRaj.name, drRaj));

Map<String, Person> people = mapOf(entry(sheldon.name, sheldon),
                                   entry(leonard.name, leonard),
                                   entry(raj.name, raj));

// assertion succeeds as both maps contains equivalent items.
assertThat(doctors).usingRecursiveComparison()
                   .isEqualTo(people);

Optional example:

Optional<Doctor> doctor = Optional.of(drSheldon);
Optional<Person> person = Optional.of(sheldon);

// assertion succeeds as both maps contains equivalent items.
assertThat(doctor).usingRecursiveComparison()
                  .isEqualTo(person);
2.9.16. AssertJ Core 3.14.0

Release date: 2019-10-27

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, Jonas Berlin, Thami Inaflas, Geoffrey Arthaud, Carter Kozak, Kevin Toublanc, Krishna Chaithanya Ganta, sowmiyamuthuraman, Edgar Asatryan, Oleksii Khomchenko, Gonzalo Müller Bravo, Stephen O’Rourke, Sven Johansson, William Bakker, Rob Spieldenner, Raymond Pressly, Michael Keppler and Clemens Grabmann.

 Breaking changes

Stop throwing an IllegalArgumentException when isIn and isNotIn are given an empty group of values.

 New features

Add BDD assumptions. (Gonzalo Müller Bravo)

Add Spliterator assertions. (William Bakker)

Add isAtSameInstantAs to OffsetDateTime assertions. (Raymond Pressly)

Add assertAlso SoftAssertions method to allow combining different soft assertions instances. (Kevin Toublanc)

Add isEmpty and isNotEmpty file assertions. (Stephen O’Rourke)

Add hasSize(long expectedSizeInBytes) to File assertions. (Krishna Chaithanya Ganta)

Avoid BDDMockito/BDDAssertions then(object) clash with and.then(object) method. (Gonzalo Müller Bravo)

Add hasRootCauseMessage to Throwable assertions. (Oleksii Khomchenko)

Add syntax sugar as(InstanceOfAssertFactory) to Assertions and WithAssertions for improved readability. (Stefano Cordio)

Add extracting(String, InstanceOfAssertFactory) to Object assertions. (Stefano Cordio)

Add extracting(Function, InstanceOfAssertFactory) to Object assertions. (Stefano Cordio)

Add extractingByKey(KEY) and extractingByKeys(KEY…​) to Map assertions. (Stefano Cordio)

Add extractingByKey(KEY, InstanceOfAssertFactory) to Map assertions. (Stefano Cordio)

Add get(InstanceOfAssertFactory) to Optional assertions. (Stefano Cordio)

Add first(InstanceOfAssertFactory) to Iterable assertions. (Stefano Cordio)

Add last(InstanceOfAssertFactory) to Iterable assertions. (Stefano Cordio)

Add element(int, InstanceOfAssertFactory) to Iterable assertions. (Stefano Cordio)

Add IntelliJ IDEA configuration file for Language Injection to add syntax highlighting on AssertJ methods with regexp parameters. (Jonas Berlin)

Add String.format support for expected message in hasMessageStartingWith, hasMessageContaining, hasMessageEndingWith and hasStackTraceContaining assertions. (Krishna Chaithanya Ganta)

 Improvements

AssertJ’s Javadoc are now searchable.

Use beautiful AssertJ’s site code style for Javadoc :)

ObjectAssert.extracting(String…​) learned to extract nested map key field/property. (Sven Johansson)

Prettify allOf and anyOf combined conditions description. (Edgar Asatryan)

Clearly differentiate top level objects in the new recursive comparison.

Show actual’s stack trace in hasRootCause and hasRootCauseMessage to give users more information. (Oleksii Khomchenko)

Show actual’s stack trace in hasMessageMatching and hasMessageFindingMatch to give users more information. (Stephen O’Rourke)

Update message text in ShouldHaveSameSizeAs to show both actual and expected collections. (Thami Inaflas)

Add matching syntactic sugar method to use Hamcrest Matcher as Condition. (Jonas Berlin)

Update ByteBuddy to version 1.10.2.

Update Hamcrest to version 2.2.

Fix Javadoc typos and incorrect references. (Erhard Pointl, Stefano Cordio)

Stop throwing an IllegalArgumentException when isIn and isNotIn are given an empty group of values.

Expose AbstractAssert.objects to be used by subclasses.

Bump opentest4j from 1.1.1 to 1.2.0. (still optional)

Improve HamcrestCondition generic type inference. (Carter Kozak)

Remove shouldHaveThrown(Assertion.class) used internally. (sowmiyamuthuraman)

Replace catchThrowable + isInstanceOf(AssertionError.class) by expectAssertionError (internal use). (Clemens Grabmann)

Rewrite CompletableFutureAssert tests with assertThatAssertionErrorIsThrownBy. (internal use). (Clemens Grabmann)

 Fixed

Fix BDDSoftAssertions.then(URL actual) that just did not work 🤦‍. (Rob Spieldenner)

Fix possible MissingFormatArgumentException in ShouldHaveMessage and ShouldContain. (Erhard Pointl)

Fix Javadoc search.

Fix Javadoc links. (Stefano Cordio)

Fix hasSizeBetween() that did not work with strings. (Geoffrey Arthaud)

Fix failing soft assertions when combined with asInstanceOf.

Fix missing soft assertions proxying for get of OptionalAssert. (Stefano Cordio)

Make convert-junit-assertions-to-assertj.sh conversion script work on Windows. (Michael Keppler)

 Deprecated

Deprecate the confusing containsOnlyElementsOf in favor of isSubsetOf or hasSameElementsAs.

Deprecate Map assertions extracting(Object) and extracting(Object…​) in favor of extractingByKey(KEY) and extractingByKeys(KEY…​), respectively. (Stefano Cordio)

Add BDD assumptions

Add Behavior Driven Development style entry point for assumption methods for different types, which allow to skip test execution when assumptions are not met.

The difference with the Assumptions class is that entry point methods are named given instead of assumeThat.

Example:

String hobbit = "HOBBIT";
List<String> fellowshipOfTheRing = list("Aragorn", "Gandalf", "Frodo", "Legolas");

@Test
public void given_the_assumption_is_not_met_the_test_is_skipped() {
  given(hobbit).isEqualTo("ORC");
  // ... following code is not executed, the test is skipped
  then(fellowshipOfTheRing).contains("Sauron");
}

@Test
public void given_the_assumption_is_met_the_test_is_executed() {
  given(hobbit).isEqualTo("HOBBIT");
  // ... following code is executed and fails!
  then(fellowshipOfTheRing).doesNotContain("Sauron");
}

Add Spliterator assertions

Add hasCharacteristics and hasOnlyCharacteristics assertions for the Spliterator type.

Example:

Spliterator<Integer> spliterator = Stream.of(1, 2, 3).spliterator();

assertThat(spliterator).hasCharacteristics(Spliterator.SIZED,
                                           Spliterator.ORDERED)
                       .hasOnlyCharacteristics(Spliterator.SIZED,
                                               Spliterator.SUBSIZED,
                                               Spliterator.IMMUTABLE,
                                               Spliterator.ORDERED);

Add isAtSameInstantAs to OffsetDateTime assertions

Verifies that actual and given OffsetDateTime are at the same Instant.

Example:

OffsetDateTime offsetDateTime1 = OffsetDateTime.of(2000, 12, 12, 3, 0, 0, 0, ZoneOffset.ofHours(3));
OffsetDateTime offsetDateTime2 = OffsetDateTime.of(2000, 12, 12, 0, 0, 0, 0, ZoneOffset.ofHours(0));
// assertion succeeds
assertThat(offsetDateTime1).isAtSameInstantAs(offsetDateTime2);

offsetDateTime2 = OffsetDateTime.of(2000, 12, 12, 2, 0, 0, 0, ZoneOffset.ofHours(0));
// assertion fails
assertThat(offsetDateTime1).isAtSameInstantAs(offsetDateTime2);

Add assertAlso SoftAssertions method to allow combining different soft assertions instances

assertAlso lets you combine other soft assertions instances together.

Example:

Mansion mansion = new Mansion();

SoftAssertions check_kitchen() {
  SoftAssertions softly = new SoftAssertions();
  softly.assertThat(mansion.kitchen()).as("Kitchen").isEqualTo("clean");
  return softly;
}

SoftAssertions check_library() {
  SoftAssertions softly = new SoftAssertions();
  softly.assertThat(mansion.library()).as("Library").isEqualTo("clean");
  return softly;
}

@Test
void host_dinner_party_where_nobody_dies() {
  SoftAssertions softly = new SoftAssertions();
  mansion.hostPotentiallyMurderousDinnerParty();
  softly.assertThat(mansion.guests()).as("Living Guests").isEqualTo(7);
  softly.assertThat(mansion.revolverAmmo()).as("Revolver Ammo").isEqualTo(6);
  softly.assertThat(mansion.candlestick()).as("Candlestick").isEqualTo("pristine");
  softly.assertThat(mansion.colonel()).as("Colonel").isEqualTo("well kempt");
  softly.assertThat(mansion.professor()).as("Professor").isEqualTo("well kempt");

  SoftAssertions kitchen = check_kitchen();
  softly.assertAlso(kitchen);

  SoftAssertions library = check_library();
  softly.assertAlso(library);

  softly.assertAll();
}

Add isEmpty and isNotEmpty file assertions

Verify that the actual File is empty (i.e. the file size = 0) or not empty (i.e. the file size > 0) .

Example:

File file = File.createTempFile("tmp", "txt");

// assertion will pass
assertThat(file).isEmpty();

Files.write(file.toPath(), new byte[]{1, 1});

// assertion will pass
assertThat(file).isNotEmpty();

Add hasSize(long expectedSizeInBytes) to File assertions

Verifies that the size of the File under test is exactly equal to the given size in bytes.

Example:

File file = File.createTempFile("tmp", "bin");
Files.write(file.toPath(), new byte[] {1, 1});

// assertion will pass
assertThat(file).hasSize(2);

// assertion will fail
assertThat(file).hasSize(1);

Avoid BDDMockito/BDDAssertions then(object) clash with and.then(object)

To avoid clash with libraries like Mockito that exposes a static then(object) method, you can statically use the and field.

import static org.mockito.BDDMockito.then;
// can't use import static org.assertj.core.api.BDDAssertions.then because of BDDMockito.then;
import static org.assertj.core.api.BDDAssertions.and;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;

// suppress and.then warning: The static method BDDAssertions.then() should be accessed in a static way
@SuppressWarnings("static-access")
@Test
public void bdd_assertions_with_bdd_mockito() {
  // GIVEN
  Person person = mock(Person.class)
  // WHEN
  person.ride(bike);
  person.ride(bike);
  // THEN
  // mockito then()
  then(person).should(times(2)).ride(bike);
  // use AssertJ and.then(person) as then(person) would clash with mockito then(person)
  and.then(person.hasBike()).isTrue();
}

Add hasRootCauseMessage to Throwable assertions

Verifies that the message of the root cause of the actual Throwable is equal to the given one, a simple String or String.format is supported to specify the expected root cause message.

Example:

Throwable throwable = new Throwable(new IllegalStateException(new NullPointerException("expected message")));

// assertions will pass
assertThat(throwable).hasRootCauseMessage("expected message")
                     .hasRootCauseMessage("expected %s", "message");

// assertions will fail
assertThat(throwable).hasRootCauseMessage("another message");
assertThat(throwable).hasRootCauseMessage("%s", "message");
// no root cause message
assertThat(new Throwable()).hasRootCauseMessage("%s %s", "expected", "message");

Add syntax sugar as(InstanceOfAssertFactory) to Assertions and WithAssertions for improved readability

A syntax sugar to write fluent assertion with methods having an InstanceOfAssertFactory parameter. Added as a static method in Assertions, it is also available as a default method in the WithAssertions interface.

Example:

Jedi yoda = new Jedi("Yoda", "Green");

assertThat(yoda).extracting(Jedi::getName, as(InstanceOfAssertFactories.STRING))
                .startsWith("Yo");

as(InstanceOfAssertFactory) can be used together with the following assertion methods:

ObjectAssert#extracting(String, InstanceOfAssertFactory)

ObjectAssert#extracting(Function, InstanceOfAssertFactory)

MapAssert#extractingByKey(KEY, InstanceOfAssertFactory)

OptionalAssert#get(InstanceOfAssertFactory)

Add extracting with String and InstanceOfAssertFactory parameters to Object assertions

Extracts the value of given field/property from the object under test, the extracted value becoming the new object under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

// Create frodo, setting its name, age and Race (Race having a name property)
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);

// let's extract and verify Frodo's name:
assertThat(frodo).extracting("name", as(InstanceOfAssertFactories.STRING))
                 .startsWith("Fro");

// The following assertion will fail as Frodo's name is not an Integer:
assertThat(frodo).extracting("name", as(InstanceOfAssertFactories.INTEGER))
                 .isZero();

Add extracting with Function and InstanceOfAssertFactory parameters to Object assertions

Uses the given Function to extract a value from the object under test, the extracted value becoming the new object under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

// Create frodo, setting its name, age and Race (Race having a name property)
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);

// let's extract and verify Frodo's name:
assertThat(frodo).extracting(TolkienCharacter::getName, as(InstanceOfAssertFactories.STRING))
                 .startsWith("Fro");

// The following assertion will fail as Frodo's name is not an Integer:
assertThat(frodo).extracting(TolkienCharacter::getName, as(InstanceOfAssertFactories.INTEGER))
                 .isZero();

Add extractingByKey with KEY and InstanceOfAssertFactory parameters to Map assertions

Extracts the value of given key from the map under test, the extracted value becoming the new object under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

Map<String, Object> map = new HashMap<>();
map.put("name", "kawhi");

// The following assertion will succeed:
assertThat(map).extractingByKey("name", as(InstanceOfAssertFactories.STRING))
               .startsWith("kaw");

// The following assertion will fail as the value is not an Integer:
assertThat(map).extractingByKey("name", as(InstanceOfAssertFactories.INTEGER))
               .isZero();

Add get with InstanceOfAssertFactory parameters to Optional assertions

Verifies that the optional is not null and not empty and returns an new assertion instance to chain assertions on the optional value. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

Optional<String> optional = Optional.of("Frodo");

// The following assertion will succeed:
assertThat(optional).get(as(InstanceOfAssertFactories.STRING))
                    .startsWith("Fro");

// The following assertion will fail as the value is not an Integer:
assertThat(optional).get(as(InstanceOfAssertFactories.INTEGER))
                    .isZero();

Add first with InstanceOfAssertFactory parameters to Iterable assertions

Navigates and allows to perform assertions on the first element of the Iterable under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

Iterable<String> hobbits = newArrayList("Frodo", "Sam", "Pippin");

// assertion succeeds
assertThat(hobbits).first(as(InstanceOfAssertFactories.STRING))
                   .startsWith("Fro")
                   .endsWith("do");
// assertion fails
assertThat(hobbits).first(as(InstanceOfAssertFactories.STRING))
                   .startsWith("Pip");
// assertion fails because of wrong factory type
assertThat(hobbits).first(as(InstanceOfAssertFactories.INTEGER))
                   .isZero();

Add last with InstanceOfAssertFactory parameters to Iterable assertions

Navigates and allows to perform assertions on the last element of the Iterable under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

Iterable<String> hobbits = newArrayList("Frodo", "Sam", "Pippin");

// assertion succeeds
assertThat(hobbits).last(as(InstanceOfAssertFactories.STRING))
                   .startsWith("Pip")
                   .endsWith("pin");
// assertion fails
assertThat(hobbits).last(as(InstanceOfAssertFactories.STRING))
                   .startsWith("Fro");
// assertion fails because of wrong factory type
assertThat(hobbits).last(as(InstanceOfAssertFactories.INTEGER))
                   .isZero();

Add element with InstanceOfAssertFactory parameters to Iterable assertions

Navigates and allows to perform assertions on the chosen element of the Iterable under test. The InstanceOfAssertFactory parameter is used to get the assertions narrowed to the factory type.

Examples:

Iterable<String> hobbits = newArrayList("Frodo", "Sam", "Pippin");

// assertion succeeds
assertThat(hobbits).element(1, as(InstanceOfAssertFactories.STRING))
                   .startsWith("Sa")
                   .endsWith("am");
// assertion fails
assertThat(hobbits).element(1, as(InstanceOfAssertFactories.STRING))
                   .startsWith("Fro");
// assertion fails because of wrong factory type
assertThat(hobbits).element(1, as(InstanceOfAssertFactories.INTEGER))
                   .isZero();

Add String.format support for expected message in hasMessageStartingWith, hasMessageContaining, hasMessageEndingWith and hasStackTraceContaining assertions

Instead of taking a simple String the assertions mentioned above now accept a String.format like parameters, i.e. (String description, Object…​ parameters) making it easier to build more involved expected strings.

Examples:

Throwable throwableWithMessage = new IllegalArgumentException("wrong amount 123");

assertThat(throwableWithMessage).hasMessageStartingWith("%s a", "wrong")
                                .hasMessageContaining("wrong %s", "amount")
                                .hasMessageEndingWith("%s 123", "amount")
                                .hasStackTraceContaining("%s amount", "wrong");

ObjectAssert.extracting(String…​) learned to extract nested map key field/property

extracting is now able to extract a deeply nested map key, before this improvement extracting a value by key was only supported for a Map object under test (but not for fields of type Map).

Let’s clarify things with a concrete example:

Jedi luke = new Jedi(new Name("Luke", "Skywalker"), 26);
// setAttribute puts a new entry in 'attributes' Map field
luke.setAttribute("side", "light");

Jedi leia = new Jedi(new Name("Leia", "Skywalker"), 26);
// setRelation puts a new entry in 'relations' Map field
luke.setRelation("sister", leia);
leia.setRelation("brother", luke);

assertThat(luke).extracting("name.last",
                            "attributes.side",
                            "relations.sister",
                            "relations.sister.relations.brother")
                .containsExactly("Skywalker",
                                 "light",
                                 leia,
                                 luke);

Prettify allOf and anyOf combined conditions description

To make it more readable, reformat the error message when multiple combined conditions with allOf and anyOf fail.

Examples: the following assertion will fail …​

private static Condition<String> contains(String s) {
  return new Condition<>(value -> value.contains(s), "contains " + s);
}

// failing assertion:
assertThat("Gandalf").has(anyOf(contains("i"),
                                allOf(contains("o"),
                                      anyOf(contains("a"),
                                            contains("b"),
                                            contains("c")))));

With the following error message

Expecting:
 <"Gandalf">
to have:
 <any of:[
   contains i,
   all of:[
      contains o,
      any of:[
         contains a,
         contains b,
         contains c
      ]
   ]
]>

Add matching syntactic sugar method to use Hamcrest Matcher as Condition

Syntactic sugar to construct a Condition using the Hamcrest Matcher given as a parameter.

Example:

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.HamcrestCondition.matching;
import static org.hamcrest.core.StringContains.containsString;

@Test
public void matching_example() {
 assertThat("abc").is(matching(containsString("a")));
}
2.9.17. AssertJ Core 3.13.2

Release date: 2019-08-04

This release ships a few improvements:

Fixes an annoyance in InstanceOfAssertFactories, where URL and URI constants have been renamed to URL_TYPE and URI_TYPE respectively to avoid a clash with java.net.URL and java.net.URI. See https://github.com/assertj/assertj-core/issues/1567 for details.

Updates ByteBuddy to version 1.10.0.

Fixes some Javadoc typos.

Enforces banned dependencies with maven-enforcer-plugin.

2.9.18. AssertJ Core 3.13.1

Release date: 2019-07-29

This release addresses the 3.13.0 issue by which AssertJ required OpenTest4J to be on the classpath otherwise a java.lang.NoClassDefFoundError: org/opentest4j/MultipleFailuresError would be raised. Thanks Pascal Schumacher for the quick fix!

java.lang.NoClassDefFoundError: org/opentest4j/MultipleFailuresError
   at java.base/java.lang.ClassLoader.defineClass1(Native Method)
   at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1016)
   at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:174)
   at java.base/jdk.internal.loader.BuiltinClassLoader.defineClass(BuiltinClassLoader.java:802)
   at java.base/jdk.internal.loader.BuiltinClassLoader.findClassOnClassPathOrNull(BuiltinClassLoader.java:700)
   at java.base/jdk.internal.loader.BuiltinClassLoader.loadClassOrNull(BuiltinClassLoader.java:623)
   at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:581)
   at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:178)
   at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:521)
   at org.assertj.core.internal.Failures.<init>(Failures.java:46)
   at org.assertj.core.internal.Failures.<clinit>(Failures.java:44)
   at org.assertj.core.internal.Objects.<init>(Objects.java:87)
   at org.assertj.core.internal.Objects.<init>(Objects.java:101)
   at org.assertj.core.internal.Objects.<clinit>(Objects.java:82)
   at org.assertj.core.api.AbstractAssert.<init>(AbstractAssert.java:65)
   at org.assertj.core.api.AbstractCharSequenceAssert.<init>(AbstractCharSequenceAssert.java:53)
   at org.assertj.core.api.AbstractStringAssert.<init>(AbstractStringAssert.java:28)
   at org.assertj.core.api.StringAssert.<init>(StringAssert.java:25)
   at org.assertj.core.api.AssertionsForClassTypes.assertThat(AssertionsForClassTypes.java:484)
   at org.assertj.core.api.Assertions.assertThat(Assertions.java:2585)
2.9.19. AssertJ Core 3.13.0

Release date: 2019-07-28

The highlight of this release is the addition of asInstanceOf which allows to chain specific type assertions from a value that was initially declared with a different type (usually Object). Thanks Stefano Cordio for this contribution!

Example:

Object value = "abc";

// This line DOES NOT COMPILE since startsWith is a String assertion and value is an Object
assertThat(value).startsWith("ab");

// This line COMPILES because we tell AssertJ to consider value as a String
assertThat(value).asInstanceOf(InstanceOfAssertFactories.STRING).startsWith("ab");

This feature is more detailed in the notes below.

 Contributors

Thanks to all the contributors of this release:

Pascal Schumacher, Erhard Pointl, Stefano Cordio, Thomas Traude, Andrei Solntsev, Matej Drobnič, Željko Mirović, Mike Gilchrist, Phillip Webb, Michal Fotyga,Valeriy Vyrva, Eddú Meléndez Gonzales, GaspardPO, Bengt Brodersen, Jiri Pejchal, Christian Stein, Nikolaos Georgiou and Sam Brannen.

Special thanks to Nils Winkler for his work on the assertions conversion scripts and Stefano Cordio for the asInstanceOf contribution.

 Breaking changes

As the extracting(String) method for Object and Map extracts only one value, it now returns Object assertions instead of list assertions (on a singleton list). This means that any list assertions used won’t compile anymore, they need to be replaced by Object assertions.

// GIVEN
Map<String, Object> basketballPlayer = new HashMap<>();
basketballPlayer.put("name", "kawhi");
basketballPlayer.put("age", 25);

// Does not compile anymore!
assertThat(basketballPlayer).extracting("name")
                            .containsExactly("kawhi"); // DOES NOT COMPILE

// Use Object assertions like isEqualTo
assertThat(basketballPlayer).extracting("name")
                            .isEqualTo("kawhi");

// multiple values work as before, no problem there!
assertThat(basketballPlayer).extracting("name", "age")
                            .containsExactly("kawhi", 25);

In the new recursive comparison, we now use the expected field as a reference to determine how to compare it to corresponding the actual field. Sorted vs non sorted collections comparison semantics have been replaced by ordered vs unordered collections semantics (ordered types are List, SortedSet and LinkedHashSet). As a consequence of the two previous points, when comparing collection/map fields, if the actual field is ordered and the expected is unordered, the comparison is allowed but not the other way around (unless order is ignored explicitely in the comparison configuration).

 New features

Add asInstanceOf to chain specific type assertions. (Stefano Cordio)

Add extracting(String) to Object and Map assertions. (Stefano Cordio)

Add a way to configure AssertJ for all tests.

Add hasCauseReference throwable assertion. (Mike Gilchrist)

Add directory content assertions for File and Path. (Valeriy Vyrva)

Add hasMessageContainingAll and hasMessageNotContainingAny to throwable assertions. (Phillip Webb)

Allow using any custom assertions in soft assertions. (Bengt Brodersen)

Add containsExactlyInAnyOrderEntriesOf to map assertions. (Stefano Cordio)

Add isCloseToUtcNow to LocalDateTime and OffsetDateTime assertions. (Nikolaos Georgiou)

 Improvements

Junit 4/5 and TestNG assertions convertion scripts improvements. (Nils Winkler)

Add support for combined millisecond and timezone parsing. (Matej Drobnič)

Add support for Optional in the new recursive comparison.

Allow ignoring collection order in specific fields in the new recursive comparison. (Željko Mirović)

Make catchThrowableOfType easier to discover in the Javadoc.

Rename methods isBeforeOrEqualsTo and isAfterOrEqualsTo to isBeforeOrEqualTo and isAfterOrEqualTo. (Eddú Meléndez Gonzales)

Improve error messages in the new recursive comparison when group size differs or when trying to compare actual unordered vs expected ordered.

Introduce explicit module descriptor. (Christian Stein)

Allow returned values of WithAssertions#fail methods to be ignored by FindBugs/SpotBugs. (Jiri Pejchal)

Improve the error message when multiple (soft) assertions error are raised.

Propagate value type with extracting(Function). (Stefano Cordio)

 Fixed

Fix Soft assertions JUnit 5 extension that did not support parallel test nor @TestInstance(PER_CLASS) lifecycle semantics. (Sam Brannen)

Fix JavaDoc regarding AnyOf and AllOf. (Thomas Traude)

Make sure that isEqualTo("abc") is not resolved to isEqualTo(String, Object…​ args). (Andrei Solntsev)

Fix Javadoc typos. (GaspardPO, Michal Fotyga)

Fix typo in error message factories ShouldBeBeforeOrEqualTo and ShouldBeAfterOrEqualTo. (Stefano Cordio)

 Deprecated

Deprecate Java 6/Android assertions entry points as they don’t truly provide 100% Java 6/Android compatibility.

Deprecate methods isBeforeOrEqualTo and isAfterOrEqualTo in favor of isBeforeOrEqualsTo and isAfterOrEqualsTo (Eddú Meléndez Gonzales).

Deprecate JUnitJupiterSoftAssertions and JUnitJupiterBDDSoftAssertions in favor of SoftAssertionsExtension

Add asInstanceOf to chain specific type assertions

asInstanceOf allows to chain specific type assertions from a value initially declared as a less specific type (often Object).

Let’s start with the problem asInstanceOf is solving: in the following example we would like to call String assertions but this is not possible since value is declared as an Object thus only Object assertions are accessible.

// Given a String declared as an Object
Object value = "Once upon a time in the west";

// We would like to call String assertions but this is not possible since value is declared as an Object
assertThat(value).startsWith("ab"); // this does not compile !

Thanks to asInstanceOf we can now tell AssertJ to consider value as a String in order to call String assertions. To do so we need to pass an InstanceOfAssertFactory that can build a StringAssert, fortunately you don’t have to write it, it is already available in InstanceOfAssertFactories!

import static org.assertj.core.api.InstanceOfAssertFactories.STRING;

// Given a String declared as an Object
Object value = "Once upon a time in the west";

// With asInstanceOf, we switch to specific String assertion by specifying the InstanceOfAssertFactory for String
assertThat(value).asInstanceOf(STRING).startsWith("Once");

AssertJ verifies that the actual value is compatible with the assertions InstanceOfAssertFactory is going to give access to.

InstanceOfAssertFactories provides static factories for all types AssertJ provides assertions for, additional factories can be created with custom InstanceOfAssertFactory instances.

Here’s another example showing the parameterized type support:

// Actually a List<TolkienCharacter>
Object hobbits = list(frodo, pippin, merry, sam);

// As we specify the TolkienCharacter class, the following chained assertion expect to be given TolkienCharacters.
// This means that method like extracting or filteredOn are given a TolkienCharacter
assertThat(hobbits).asInstanceOf(InstanceOfAssertFactories.list(TolkienCharacter.class))
                   .contains(frodo, sam)
                   .extracting(TolkienCharacter::getName)
                   .contains("Frodo", "Sam");

// Use LIST if the elements type is not important but note that the chained assertions
// will be given Object not TolkienCharacter
assertThat(hobbits).asInstanceOf(InstanceOfAssertFactories.LIST)
                    //.extracting(TolkienCharacter::getName) does not work as extracting is given an Object
                   .contains(frodo);

Add extracting with single parameter to Object and Map assertions

Extracts the value of given field/property from the object under test, the extracted value becoming the new object under test.

Examples:

// Create frodo, setting its name, age and Race (Race having a name property)
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, HOBBIT);

// let's extract and verify Frodo's name:
assertThat(frodo).extracting("name")
                 .isEqualTo("Frodo");

// The extracted value being a String, we would like to use String assertions but we can't due to Java generics limitations.
// The following assertion does NOT compile:
assertThat(frodo).extracting("name")
                 .startsWith("Fro");

// To get String assertions use asInstanceOf:
assertThat(frodo).extracting("name")
                 .asInstanceOf(InstanceOfAssertFactories.STRING)
                 .startsWith("Fro");

If the object under test is a Map, the parameter is used as a key to the map.

Example:

Map<String, Object> basketballPlayer = new HashMap<>();
basketballPlayer.put("name", "kawhi");
basketballPlayer.put("age", 25);

// single value
assertThat(basketballPlayer).extracting("name")
                            .isEqualTo("kawhi");

AssertJ global configuration

AssertJ 3.13.0 introduces a Configuration class allowing to change AssertJ behavior and a way to register automatically. Read Configuring AssertJ chapter to learn about it.

Add hasCauseReference to throwable assertions

Verifies that the actual Throwable has a cause that refers to the given one, i.e. using == comparison.

Example:

Throwable invalidArgException = new IllegalArgumentException("invalid arg");
Throwable throwable = new Throwable(invalidArgException);

// This assertion succeeds:
assertThat(throwable).hasCauseReference(invalidArgException);

// These assertions fail:
assertThat(throwable).hasCauseReference(new IllegalArgumentException("invalid arg"));
assertThat(throwable).hasCauseReference(new NullPointerException());
assertThat(throwable).hasCauseReference(null); // prefer hasNoCause()

New directory content assertions

The new assertions have been added for both File and Path, they add support for

checking what a directory contains with isDirectoryContaining

checking what a directory does not contain with isDirectoryNotContaining

checking if directory is empty with isEmptyDirectory or not with isNotEmptyDirectory

Both isDirectoryContaining and isDirectoryNotContaining accept either Predicate or String parameters, the String one being interpreted as a path matcher.

As File and Path assertions are similar, the examples will only show File assertions.

The examples use the following directory structure:

/root/
/root/sub-dir-1/
/root/sub-dir-1/file-1.ext
/root/sub-dir-1/file-2.ext
/root/sub-dir-2/
/root/sub-file-1.ext
/root/sub-file-2.ext

isDirectoryContaining assertions examples:

File root = new File("root");

// Successfull assertions with predicate parameter:
assertThat(root).isDirectoryContaining(file -> file.getName().startsWith("sub-dir"))
                .isDirectoryContaining(file -> file.getName().startsWith("sub-file"))
                .isDirectoryContaining(file -> file.getName().endsWith(".ext"))
                .isDirectoryContaining(File::isDirectory);

// Successfull assertions with String path matcher parameter:
assertThat(root).isDirectoryContaining("glob:**sub-dir*")
                .isDirectoryContaining("glob:**sub-file*")
                .isDirectoryContaining("glob:**.ext")
                .isDirectoryContaining("regex:.*ext")
                .isDirectoryContaining("glob:**.{ext,bin");


// The following assertions fail:
assertThat(root).isDirectoryContaining(file -> file.getName().startsWith("dir"));
assertThat(root).isDirectoryContaining(file -> file.getName().endsWith(".bin"));
assertThat(root).isDirectoryContaining("glob:**dir");
assertThat(root).isDirectoryContaining("glob:**.bin");

isDirectoryNotContaining assertion examples:

File root = new File("root");

// Successfull assertions with predicate parameter:
assertThat(root).isDirectoryNotContaining(file -> file.getName().startsWith("dir"))
                .isDirectoryNotContaining(file -> file.getName().endsWith(".bin"));

// Successfull assertions with String path matcher parameter:
assertThat(root).isDirectoryNotContaining("glob:**dir")
                .isDirectoryNotContaining("glob:**.bin")
                .isDirectoryNotContaining("regex:.*bin")
                .isDirectoryNotContaining("glob:**.{java,class}");

// The following assertions fail:
assertThat(root).isDirectoryContaining(file -> file.getName().startsWith("dir"));
assertThat(root).isDirectoryContaining(file -> file.getName().endsWith(".bin"));
assertThat(root).isDirectoryNotContaining("glob:**sub-dir*");
assertThat(root).isDirectoryNotContaining("regex:.*ext");
assertThat(root).isDirectoryNotContaining("glob:**.{ext,bin");

isEmptyDirectory assertion examples:

File root = new File("root");

// The following assertion succeeds:
assertThat(new File(root, "sub-dir-2")).isEmptyDirectory();

// The following assertions fail:
assertThat(root).isEmptyDirectory();
assertThat(new File(root, "sub-dir-1")).isEmptyDirectory();

isNotEmptyDirectory assertion examples:

File root = new File("root");

// The following assertions succeed:
assertThat(root).isNotEmptyDirectory();
assertThat(new File(root, "sub-dir-1")).isNotEmptyDirectory();

// The following assertion fails:
 assertThat(new File(root, "sub-dir-2")).isNotEmptyDirectory();

Add hasMessageContainingAll and hasMessageNotContainingAny to throwable assertions

These assertions are the equivalent of hasMessageContaining and hasMessageNotContaining but accepting multiple String parameters instead of only one.

Example:

Throwable throwableWithMessage = new IllegalArgumentException("wrong amount 123");
Throwable throwableWithoutMessage = new IllegalArgumentException();

// assertion will pass:
assertThat(throwableWithMessage).hasMessageContainingAll("amount", "123")
                                .hasMessageNotContainingAny("foo", "234");

assertThat(throwableWithoutMessage).hasMessageNotContainingAny("234");

// assertions will fail:
assertThat(throwableWithMessage).hasMessageContainingAll("234");
assertThat(throwableWithoutMessage).hasMessageContainingAll("123");

assertThat(throwableWithMessage).hasMessageNotContainingAny("foo", "amount");

The same assertions have been added to ThrowableAssertAlternative with these names withMessageContainingAll and withMessageNotContainingAny:

Throwable illegalArgumentException = new IllegalArgumentException("wrong amount 123");

// assertions will pass
assertThatExceptionOfType(Throwable.class)
          .isThrownBy(() -> {throw illegalArgumentException;})
          .withMessageContainingAll("amount", "123")
          .withMessageNotContainingAny("foo", "234");

Allow using any custom assertions in soft assertions

The new check method catches and collect assertion errors coming from standard and custom assertions.

Example:

SoftAssertions softly = new SoftAssertions();

// custom assertions
softly.check(() -> LotrAssertions.assertThat(frodo).hasName("Frodon"));
softly.check(() -> LotrAssertions.assertThat(frodo).hasName("Frodo"));

// standard assertions
softly.assertThat("foo").startsWith("bar");
// could be written with check like (but it's as elegant as the standard use):
// softly.check(() -> Assertions.assertThat("foo").startsWith("bar"));

// 2 errors: "foo" does not start with "bar" and frodo's name is not "Frodon"
assertThat(softly.errorsCollected()).hasSize(2);

Add containsExactlyInAnyOrderEntriesOf to map assertions

Verifies that the actual map contains only the given entries and nothing else, in any order.

This is the same assertion as containsOnly(Map.Entry…​ entries), it simply handles the conversion of Map.entrySet() to array.

Example :

Map<Ring, TolkienCharacter> ringBearers = newLinkedHashMap(entry(oneRing, frodo),
                                                           entry(nenya, galadriel),
                                                           entry(narya, gandalf));
// assertion will pass
assertThat(ringBearers).containsExactlyInAnyOrderEntriesOf(newLinkedHashMap(entry(oneRing, frodo),
                                                                            entry(nenya, galadriel),
                                                                            entry(narya, gandalf)));
// assertion will pass although actual and expected order differ
assertThat(ringBearers).containsExactlyInAnyOrderEntriesOf(newLinkedHashMap(entry(nenya, galadriel),
                                                                            entry(narya, gandalf),
                                                                            entry(oneRing, frodo)));
// assertion will fail as actual does not contain all entries of expected
assertThat(ringBearers).containsExactlyInAnyOrderEntriesOf(newLinkedHashMap(entry(oneRing, frodo),
                                                                            entry(nenya, galadriel),
                                                                            entry(oneRing, frodo)));
// assertion will fail as actual and expected have different sizes
assertThat(ringBearers).containsExactlyInAnyOrderEntriesOf(newLinkedHashMap(entry(oneRing, frodo),
                                                                            entry(nenya, galadriel),
                                                                            entry(narya, gandalf),
                                                                            entry(narya, gandalf)));

Add isCloseToUtcNow to LocalDateTime and OffsetDateTime assertions

Verifies that the actual LocalDateTime/OffsetDateTime is close to the current date and time on the UTC timezone, according to the given offset.

You can build the offset parameter using Assertions.within(long, TemporalUnit) or Assertions.byLessThan(long, TemporalUnit).

If the difference is equal to the offset, the assertion succeeds.

Example with LocalDateTime:

LocalDateTime actual = LocalDateTime.now(Clock.systemUTC());

// assertion will pass if executed less than one second after actual was built
assertThat(actual).isCloseToUtcNow(byLessThan(1, ChronoUnit.SECONDS));

// assertion will fail
assertThat(actual.plusSeconds(2)).isCloseToUtcNow(within(1, ChronoUnit.SECONDS));

The same example works with OffsetDateTime by simply defining actual as:

OffsetDateTime actual = OffsetDateTime.now(Clock.systemUTC());

Add support for combined millisecond and timezone parsing

Add yyyy-MM-dd HH:mm:ss.SSSX to the default date formats AssertJ supports in Date assertions that take a String parameter representating a Date.

Here’s an example of string following this format: "2003-04-26T00:00:00.123+00:00".

Example:

// GIVEN
SimpleDateFormat isoFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");
isoFormat.setTimeZone(TimeZone.getTimeZone("UTC"));
// WHEN
Date date = isoFormat.parse("2003-04-26T00:00:00.123");
// THEN
assertThat(date).isEqualTo("2003-04-26T00:00:00.123+00:00");

Add support for Optional in the new recursive comparison

The recursive comparison added in 3.12.0 now compares Optional values recursively instead of comparing Optional with equals. This is consistent with comparing list elements by elements as an Optional can be seen as a list with at most one element.

Example:

// Song constructor parameters: song, author and coAuthor (optional)
Song song = new Song("I Can't Get No Satisfaction", new Author("Mick Jagger"), new Author("Keith Richards"));
Song expectedSong = new Song("I Can't Get No Satisfaction", new Author("Mick Jagger"), new Author("Keith Richards"));
// THEN
assertThat(song).usingRecursiveComparison()
                .isEqualTo(expectedSong);

where Song and Author don’t override equals:

class Song {

  Author author;
  Optional<Author> coAuthor;
  String song;

  Song(String song, Author author, Author coAuthor) {
    this.song = song;
    this.author = author;
    this.coAuthor = Optional.ofNullable(coAuthor);
  }

  // no equals!
}

class Author {

  String name;

  Author(String name) {
    this.name = name;
  }

  String getName() {
    return name;
  }

  // no equals!
}

If we fail the test ...

Song song = new Song("I Can't Get No Satisfaction", new Author("Mick Jagger"), new Author("Jimi Hendrix"));
Song expectedSong = new Song("I Can't Get No Satisfaction", new Author("Mick Jagger"), new Author("Keith Richards"));
// FAIL
assertThat(song).usingRecursiveComparison()
                .isEqualTo(expectedSong);

... here’s the error reported:

Expecting:
  <Song [author=Mick Jagger, coAuthor=Optional[Jimi Hendrix], song=I Can't Get No Satisfaction]>
to be equal to:
  <Song [author=Mick Jagger, coAuthor=Optional[Keith Richards], song=I Can't Get No Satisfaction]>
when recursively comparing field by field, but found the following difference:

field/property 'coAuthor.value.name' differ:
- actual value   : "Jimi Hendrix"
- expected value : "Keith Richards"

The recursive comparison was performed with this configuration:
- overridden equals methods were used in the comparison
- these types were compared with the following comparators:
  - java.lang.Double -> DoubleComparator[precision=1.0E-15]
  - java.lang.Float -> FloatComparator[precision=1.0E-6]
- actual and expected objects and their fields were compared field by field recursively even if they were not of the same type, this allows for example to compare a Person to a PersonDto (call strictTypeChecking(true) to change that behavior).

Allow ignoring collection order in the new recursive comparison

The recursive comparison added in 3.12.0 can now ignore collection order in all fields in the object under test, this is handy when comparing list to set fields where only the content is relevant but not the order.

Example:

public class Person {
  String name;
  List<Person> friends = new ArrayList<>();
}

Person sherlock1 = new Person("Sherlock Holmes");
sherlock1.friends.add(new Person("Dr. John Watson"));
sherlock1.friends.add(new Person("Molly Hooper"));

Person sherlock2 = new Person("Sherlock Holmes");
sherlock2.friends.add(new Person("Molly Hooper"));
sherlock2.friends.add(new Person("Dr. John Watson"));

// assertion succeeds as all fields collection order is ignored in the comparison
assertThat(sherlock1).usingRecursiveComparison()
                     .ignoringCollectionOrder()
                     .isEqualTo(sherlock2);

// assertion fails as fields collection order is not ignored in the comparison
assertThat(sherlock1).usingRecursiveComparison()
                     .isEqualTo(sherlock2);

Propagate value type with extracting(Function)

extracting(Function) learned to propagate the type parameter of the resulting ObjectAssert allowing then to chain other type aware methods (e.g. additional extracting).

Example:

// Old implementation
assertThat(yoda).extracting(Jedi::getName) // ObjectAssert<Object>
                .extracting(String::length) // Not compiling
                .isEqualTo(4);

// New implementation
assertThat(yoda).extracting(Jedi::getName) // ObjectAssert<String>
                .extracting(String::length)  // Compiling!
                .isEqualTo(4);
2.9.20. AssertJ Core 3.12.2

The main issue fixed was to ignore static methods when finding property accessors (contributed by Andy Wilkinson) which could break some tests since bare name method introspection was introduced in 3.12.0.

anySatisfy for Maps was improved and does not continue evaluating elements once a match is found (contributed by Erhard Pointl).

2.9.21. AssertJ Core 3.12.1

Fix a regression that included a bad module-info.class (thanks Jaro Kuruc) and other minor improvements.

2.9.22. AssertJ Core 3.12.0

Release date: 2019-02-14

The main feature of this release is a beta version of the new Recursive comparison API! It covers what isEqualToComparingFieldByFieldRecursively used but easier to use and with more capabilities.

It is a Beta version because we want to have feedback from the community to make it even better before freezing the API. There are more capabilities to come in the next releases, stay tuned!

Contributors

Big thanks to all the contributors of this release:

Pascal Schumacher, Erhard Pointl, Vladimir Chernikov, Sandra Parsick, Martin Tarjanyi, Stephan Windmüller, Yaroslav Mitsynskiy, Thomas Traude, Georg Berky, Tomek Kaczanowski, Lukáš Křečan, Yoann Rodière, Filip Hrisafov, Steven Schlansker, Jeremy Landis, Jack Gough, Sebastian Kempken, Stefan Mandel, Alexandre de Champeaux, Arvid Heise, Jeff Walker, Dmitrii Priporov and Joshua Kitchen.

Breaking changes

Introduce first class Iterator assertions (Stephan Windmüller).

	This removes the previously supported “Iterable” assertions (like containsOnly), call IteratorAssert#toIterable to access them again, ex:
Iterator<String> bestBasketBallPlayers = getBestBasketBallPlayers();

assertThat(bestBasketBallPlayers).toIterable().contains("Jordan", "Magic", "Lebron");

Add configurable support for bare-named property introspection. (Steven Schlansker)

AssertJ uses introspection in various places, one example is extracting properties as in extracting("name"). AssertJ is able to get values with getters like getName(), with this improvement it now can get property values with bare name method like name().

	Bare-named property introspection is enabled by default and thus changes AssertJ behavior which can break some existing tests relying on introspection, this is especially true as AssertJ wrongly tries static methods (https://github.com/assertj/assertj-core/issues/1458 had been created to address that).

It is possible to avoid this problem by calling Assertions.setExtractBareNamePropertyMethods(false); before every impacted tests.

This is a bit tedious but an improvement is planned in the next release to provide a place to perform global configuration with the same mechanism allowing to register a custom representation.

New features

New Recursive comparison API! (Beta version)

Add satisfiesAnyOf base assertion.

Add isAbstract to Class assertions. (Erhard Pointl)

Add hasValueCloseTo(percentage) to OptionalDouble assertion. (Joshua Kitchen)

Add hasOnlyOneElementSatisfying(Consumer) to AtomicReferenceArray assertions. (Vladimir Chernikov)

Add hasAllNullFieldsOrProperties and hasAllNullFieldsOrPropertiesExcept. (Vladimir Chernikov)

Add hasSizeGreaterThan, hasSizeLessThanOrEqualTo, hasSizeGreaterThanOrEqualTo and hasSizeGreaterThan to CharSequence and String assertions. (Sandra Parsick)

Add hasSizeGreaterThan, hasSizeLessThanOrEqualTo, hasSizeGreaterThanOrEqualTo, hasSizeGreaterThan and hasSizeBetween to object and primitives array, Iterable and Map. (Martin Tarjanyi)

Add hasSizeBetween to CharSequence and String assertions. (Martin Tarjanyi)

Add noneSatisfy(BiConsumer) to Map assertions. (Erhard Pointl)

Add containsExactlyEntriesOf assertion to check that a Map contains exactly all entries of another Map. (Filip Hrisafov)

Add containsOnlyKeys(Iterable keys) to Map assertion. (Sebastian Kempken)

Add anySatifies(BiConsumer) to Map assertion. (Stefan Mandel)

Add hasMessageNotContaining to Throwable assertions. (Georg Berky and Sandra Parsick)

Add shouldHaveRootCause to Throwable assertions to check the content of a root cause. (Jack Gough)

Add isEqualTo(String string, Objects…​ param) to String assertion. (Dmitrii Priporov)

Add assertThatObject/thenObject to force Object assertion. (Arvid Heise)

Add JUnit5 to AssertJ assertions migration script for osx. (Tomek Kaczanowski)

Improvements

Add stack trace of original exception to catchThrowableOfType. (Sam Smyth)

anySatisfy and noneSatisfy now reports all failing elements. (Erhard Pointl)

ElementsShouldSatisfy now uses the configured Representation to format objects.

ZipSatisfyError now uses the configured Representation to format objects. (Jeff Walker)

AssertJ Double and Float comparators now support Infinity. (Alexandre de Champeaux)

Throw AssertionFailedError instead of AssertionError in some String assertions to allow IDEs to show actual vs expected visual differences. (Yaroslav Mitsynskiy)

Optional hasValue/contains assertions throws AssertionFailedError to allow IDEs to show actual vs expected visual differences.

Annotate Assertions and Assumptions classes with @CheckReturnValue and annotate methods to exclude from checking with @CanIgnoreReturnValue. (Pascal Schumacher)

The error message of allSatisfy(BiConsumer) Map assertion now reports all failing entries instead of the first one. (Stefan Mandel)

Add missing @Since annotations. (Erhard Pointl)

Get rid of Arguments usage when possible in unit tests. (Erhard Pointl)

Unit tests code cleanup and better use of JUnit 5. (Erhard Pointl, Pascal Schumacher and Jack Gough)

Update to JUnit 5.4.0. (Erhard Pointl)

Update to opentest4j to 1.1.1. (Erhard Pointl)

Update to Byte Buddy 1.9.10. (Pascal Schumacher)

Update Maven version to and the Maven wrapper. (Thomas Traude, Jeremy Landis)

Do not proxy useComparator method in soft assertions. (Lukáš Křečan)

Fix an NPE in ObjectArrays#assertHasOnlyElementsOfType. (Yoann Rodière)

Deprecate Extractor in favor of java.util.function.Function. (Filip Hrisafov)

Fixed

Use @CanIgnoreReturnValue on Assertions fail* methods to revert the effect of the default @CheckReturnValue annotation. (Erhard Pointl)

Fix ElementsShouldSatisfy that failed to handle objects whose string representation contained %.

Fix ElementsShouldZipSatisfy that failed to handle objects whose string representation contained %. (Arvid Heise)

3. AssertJ Guava
3.1. Quick start

This guide is for the AssertJ Guava module.

3.1.1. Supported Java versions

AssertJ Guava requires Java 8 or higher.

3.1.2. Get AssertJ Guava

The AssertJ Guava artifact can be included directly using its dependency metadata or indirectly via the Bill of Materials POM.

Maven
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-guava</artifactId>
  <version>3.27.7</version>
  <scope>test</scope>
</dependency>
Gradle
testImplementation("org.assertj:assertj-guava:3.27.7")
Other build tools

Check this page to find the relevant AssertJ Guava dependency declaration.

3.1.3. Use Assertions class entry point

The org.assertj.guava.api.Assertions class is the only class you need to start using AssertJ Guava.

import static org.assertj.guava.api.Assertions.assertThat;
3.1.4. Examples
import static org.assertj.guava.api.Assertions.assertThat;
import static org.assertj.guava.api.Assertions.entry;

// Multimap assertions
Multimap<String, String> actual = ArrayListMultimap.create();
actual.putAll("Lakers", newArrayList("Kobe Bryant", "Magic Johnson", "Kareem Abdul Jabbar"));
actual.putAll("Spurs", newArrayList("Tony Parker", "Tim Duncan", "Manu Ginobili"));

assertThat(actual).containsKeys("Lakers", "Spurs");
assertThat(actual).contains(entry("Lakers", "Kobe Bryant"), entry("Spurs", "Tim Duncan"));

// Multiset assertions
Multiset<String> actual = HashMultiset.create();
actual.add("shoes", 2);

assertThat(actual).contains(2, "shoes");
assertThat(actual).containsAtLeast(1, "shoes");
assertThat(actual).containsAtMost(3, "shoes");

// Range assertions
Range<Integer> range = Range.closed(10, 12);

assertThat(range).isNotEmpty()
                 .contains(10, 11, 12)
                 .hasClosedLowerBound()
                 .hasLowerEndpointEqualTo(10)
                 .hasUpperEndpointEqualTo(12);

// Table assertions
Table<Integer, String, String> bestMovies = HashBasedTable.create();

bestMovies.put(1970, "Palme d'Or", "M.A.S.H");
bestMovies.put(1994, "Palme d'Or", "Pulp Fiction");
bestMovies.put(2008, "Palme d'Or", "Entre les murs");
bestMovies.put(2000, "Best picture Oscar", "American Beauty");
bestMovies.put(2011, "Goldener Bär", "A Separation");

assertThat(bestMovies).hasRowCount(5).hasColumnCount(3).hasSize(5)
                      .containsValues("American Beauty", "A Separation", "Pulp Fiction")
                      .containsCell(1994, "Palme d'Or", "Pulp Fiction")
                      .containsColumns("Palme d'Or", "Best picture Oscar", "Goldener Bär")
                      .containsRows(1970, 1994, 2000, 2008, 2011);

Note that you can find more working examples in the assertj-examples project: https://github.com/assertj/assertj-examples/tree/main/assertions-examples/src/test/java/org/assertj/examples/guava.

3.1.5. IDE configuration

You can configure your IDE so that when you start typing as and trigger code completion assertThat will show up in the suggested completions.

Eclipse:

Go to Window > Preferences > Java > Editor > Content Assist > Favorites > New Type.

Enter org.assertj.guava.api.Assertions and click OK.

Check that you see org.assertj.guava.api.Assertions.* in Favorites.

Intellij Idea: No special configuration is needed, just start typing asser and then invoke completion (Ctrl-Space) twice.

3.2. Assertions Guide

This section describes the assertions provided by AssertJ Guava.

3.2.1. ByteSource
Assertion	Description


hasSameContentAs

	

Verifies that the actual ByteSource has the same content as the provided one.




hasSize

	

Verifies that the size of the actual ByteSource is equal to the given one.




isEmpty

	

Verifies that the actual ByteSource is empty.

3.2.2. Multimap
Assertion	Description


contains

	

Verifies that the actual Multimap contains the given entries.




containsAllEntriesOf

	

Verifies that the actual Multimap contains all entries of the given one (it might contain more entries).




containsKeys

	

Verifies that the actual Multimap contains the given keys.




containsValues

	

Verifies that the actual Multimap contains the given values for any key.




doesNotContainKey

	

Verifies that the actual Multimap does not contain the given key.




doesNotContainKeys

	

Verifies that the actual Multimap does not contain the given keys.




hasSameEntriesAs

	

Verifies that the actual Multimap has the same entries as the given one.




hasSize

	

Verifies that the number of values in the actual Multimap is equal to the given one.




isEmpty

	

Verifies that the actual Multimap is empty.




isNotEmpty

	

Verifies that the actual Multimap is not empty.

3.2.3. Multiset

In addition to Iterable assertions, the following are also available.

Assertion	Description


contains

	

Verifies the actual Multiset contains the given value exactly the given number of times.




containsAtLeast

	

Verifies the actual Multiset contains the given value at least the given number of times.




containsAtMost

	

Verifies the actual Multiset contains the given value at most the given number of times.

3.2.4. Optional
Assertion	Description


contains

	

Verifies that the actual Optional contains the given value.




extractingCharSequence

	

Chain assertion on the content of the Optional.




extractingValue

	

Chain assertion on the content of the Optional.




isAbsent

	

Verifies that the actual Optional contained instance is absent/null.




isPresent

	

Verifies that the actual Optional contains a (non-null) instance.

3.2.5. Range
Assertion	Description


contains

	

Verifies that the actual Range contains the given values.




doesNotContain

	

Verifies that the actual Range does not contain the given values.




hasClosedLowerBound

	

Verifies that the actual Range lower bound is closed.




hasClosedUpperBound

	

Verifies that the actual Range upper bound is closed.




hasLowerEndpointEqualTo

	

Verifies that the actual Range lower endpoint is equal to the given value.




hasOpenedLowerBound

	

Verifies that the actual Range lower bound is opened.




hasOpenedUpperBound

	

Verifies that the actual Range upper bound is opened.




hasUpperEndpointEqualTo

	

Verifies that the actual Range upper endpoint is equal to the given value.




isEmpty

	

Verifies that the actual Range is empty.




isNotEmpty

	

Verifies that the actual Range is not empty.

3.2.6. RangeMap
Assertion	Description


contains

	

Verifies that the actual RangeMap contains the given entries.




containsKeys

	

Verifies that the actual RangeMap contains the given keys.




containsValues

	

Verifies that the actual RangeMap contains the given values.




isEmpty

	

Verifies that the actual RangeMap is empty.




isNotEmpty

	

Verifies that the actual RangeMap is not empty.

3.2.7. RangeSet
Assertion	Description


contains

	

Verifies that the given RangeSet contains the given ranges.




containsAll

	

Verifies that the given RangeSet contains all the given ranges.




containsAnyOf

	

Verifies that the given RangeSet contains at least one of the given ranges.




containsAnyRangesOf

	

Verifies that the given RangeSet contains at least one of the given ranges.




doesNotContain

	

Verifies that the given RangeSet does not contain any of the given ranges.




doesNotContainAll

	

Verifies that the given RangeSet does not contain any of the given ranges.




doesNotEnclose

	

Verifies that the given RangeSet does not enclose the given ranges.




doesNotEncloseAnyRangesOf

	

Verifies that the given RangeSet does not enclose any range from the given range set.




doesNotEncloseAnyRangesOf

	

Verifies that the given RangeSet does not enclose any of the given ranges.




doesNotIntersect

	

Verifies that the given RangeSet does not intersect the given ranges.




doesNotIntersectAnyRangeFrom

	

Verifies that the given RangeSet does not intersect ranges from the given range set.




doesNotIntersectAnyRangeFrom

	

Verifies that the given RangeSet does not intersect all the given ranges.




encloses

	

Verifies that the given RangeSet encloses the given ranges.




enclosesAll

	

Verifies that the given RangeSet encloses all ranges from the given range set.




enclosesAll

	

Verifies that the given RangeSet encloses all the given ranges.




enclosesAnyOf

	

Verifies that the given RangeSet encloses at least one of the given ranges.




enclosesAnyRangesOf

	

Verifies that the given RangeSet encloses at least one range from the given range set.




enclosesAnyRangesOf

	

Verifies that the given RangeSet encloses at least one range of the given ranges.




hasSize

	

Verifies that the given RangeSet has specific size of disconnected Range elements.




intersects

	

Verifies that the given RangeSet intersects all the given ranges.




intersectsAll

	

Verifies that the given RangeSet intersects all the given range set.




intersectsAll

	

Verifies that the given RangeSet intersects all the given ranges.




intersectsAnyOf

	

Verifies that the given RangeSet intersects at least one of the given ranges.




intersectsAnyRangesOf

	

Verifies that the given RangeSet intersects at least one range of the given range set.




intersectsAnyRangesOf

	

Verifies that the given RangeSet intersects at least one of the given ranges.




isEmpty

	

Verifies that the actual RangeSet is empty.




isNotEmpty

	

Verifies that the actual RangeSet is not empty.




isNullOrEmpty

	

Verifies that the actual RangeSet is null or empty.

3.2.8. Table
Assertion	Description


containsCell

	

Verifies that the actual Table contains the mapping of row/column to value.




containsColumns

	

Verifies that the actual Table contains the given columns.




containsRows

	

Verifies that the actual Table contains the given rows.




containsValues

	

Verifies that the actual Table contains the given values for any key.




hasColumnCount

	

Verifies that the actual Table has the expected number of columns.




hasRowCount

	

Verifies that the actual Table has the expected number of rows.




hasSize

	

Verifies that the actual Table has the expected number of cells.




isEmpty

	

Verifies that the actual Table is empty.




isNotEmpty

	

Verifies that the actual Table is not empty.

3.3. Javadoc

The latest Javadoc for AssertJ Guava API is here.

3.4. Release Notes
	AssertJ Guava main documentation is still in https://joel-costigliola.github.io/assertj/assertj-guava.html until it is moved to this website.

The latest release notes can be found in the GitHub releases.

Older release notes:

AssertJ Guava 3.5.0

AssertJ Guava 3.4.0

AssertJ Guava 3.3.0

Even older release notes can be found in the old site: https://joel-costigliola.github.io/assertj/assertj-guava.html#latest-release.

3.4.1. AssertJ Guava 3.5.0

Release date: 2022-06-11

 Contributors

Thanks to all the contributors of this release: Erhard Pointl, Stefano Cordio, BJ Hargrave , sullis .

 Binary compatibility

The release is binary compatible with the previous minor version.

 Improvements

Remove <> from error messages (Erhard Pointl)

Internal: Add binary compatibility check of main against the latest release (Stefano Cordio)

Internal: Add binary compatibility checks for pull requests (Stefano Cordio)

Internal: Add Code of Conduct (Stefano Cordio)

Internal: Add CodeQL workflow (Stefano Cordio)

Internal: Add Dependabot (sullis)

Internal: Add release workflow (Stefano Cordio)

Internal: Bump actions/cache from v1 to v2

Internal: Bump actions/checkout from 2 to 3

Internal: Bump actions/setup-java from 1 to 3

Internal: Bump actions/upload-artifact from 2 to 3

Internal: Bump assertj-core from 3.15.0 to 3.23.1 (sullis, Erhard Pointl, Stefano Cordio)

Internal: Bump assertj-parent-pom from 2.2.6 to 2.2.17

Internal: Bump github/codeql-action from 1 to 2

Internal: Bump guava from 29.0-jre to 31.1-jre

Internal: Bump Maven version from 3.6.3 to 3.8.5 (Erhard Pointl, Stefano Cordio)

Internal: Bump maven-bundle-plugin from 3.0.1 to 5.1.4

Internal: Convert JUnit 4 tests to JUnit 5 (Stefano Cordio)

Internal: Move RangeSet assertions to the api package (Stefano Cordio)

Internal: Simplify maven-bundle-plugin configuration (Stefano Cordio)

Internal: Switch to the official Maven Wrapper by Apache (Stefano Cordio)

Internal: Update license headers (Erhard Pointl, Stefano Cordio)

Internal: Use bnd-maven-plugin instead of maven-bundle-plugin (BJ Hargrave)

 Fixed

Remove the usage of assertj-core internal API to fix the compatibility with OSGi (Stefano Cordio)

3.4.2. AssertJ Guava 3.4.0

Release date: 2020-04-24

 Contributors

Thanks to Ilya Koshaleu for its contribution!

 New features

Add RangeSet assertions (Ilya Koshaleu):

contains(T…​ ranges): Verifies that the given RangeSet contains the given ranges.

containsAll(Iterable<T> ranges): Verifies that the given RangeSet contains all the given ranges.

containsAnyOf(T…​ ranges): Verifies that the given RangeSet contains at least one of the given ranges.

containsAnyRangesOf(Iterable<T> ranges): Verifies that the given RangeSet contains at least one of the given ranges.

doesNotContain(T…​ ranges): Verifies that the given RangeSet does not contain any of the given ranges.

doesNotContainAll(Iterable<T> ranges): Verifies that the given RangeSet does not contain any of the given ranges.

doesNotEnclose(Range<T>…​ ranges): Verifies that the given RangeSet does not enclose the given ranges.

doesNotEncloseAnyRangesOf(RangeSet<T> rangeSet): Verifies that the given RangeSet does not enclose any range from the given range set.

doesNotEncloseAnyRangesOf(Iterable<Range<T>> ranges): Verifies that the given RangeSet does not enclose any of the given ranges.

doesNotIntersect(Range<T>…​ ranges): Verifies that the given RangeSet does not intersect the given ranges.

doesNotIntersectAnyRangeFrom(RangeSet<T> rangeSet): Verifies that the given RangeSet does not intersect ranges from the given range set.

doesNotIntersectAnyRangeFrom(Iterable<Range<T>> ranges): Verifies that the given RangeSet does not intersect all the given ranges.

encloses(Range<T>…​ ranges): Verifies that the given RangeSet encloses the given ranges.

enclosesAll(RangeSet<T> rangeSet): Verifies that the given RangeSet encloses all ranges from the given range set.

enclosesAll(Iterable<Range<T>> ranges): Verifies that the given RangeSet encloses all the given ranges.

enclosesAnyOf(Range<T>…​ ranges): Verifies that the given RangeSet encloses at least one of the given ranges.

enclosesAnyRangesOf(RangeSet<T> rangeSet): Verifies that the given RangeSet encloses at least one range from the given range set.

enclosesAnyRangesOf(Iterable<Range<T>> ranges): Verifies that the given RangeSet encloses at least one range of the given ranges.

hasSize(int size): Verifies that the given RangeSet has the specific size of disconnected Range elements.

intersects(Range<T>…​ ranges): Verifies that the given RangeSet intersects all the given ranges.

intersectsAll(RangeSet<T> rangeSet): Verifies that the given RangeSet intersects all the given range set.

intersectsAll(Iterable<Range<T>> ranges): Verifies that the given RangeSet intersects all the given ranges.

intersectsAnyOf(Range<T>…​ ranges): Verifies that the given RangeSet intersects at least one of the given ranges.

intersectsAnyRangesOf(RangeSet<T> rangeSet): Verifies that the given RangeSet intersects at least one range of the given range set.

intersectsAnyRangesOf(Iterable<Range<T>> ranges): Verifies that the given RangeSet intersects at least one of the given ranges.

isEmpty(): Verifies that the actual RangeSet is empty.

isNotEmpty(): Verifies that the actual RangeSet is not empty.

isNullOrEmpty(): Verifies that the actual RangeSet is null or empty.

 Improvements

Javadoc uses AssertJ site beautiful theme :)

Uses to assertj-core version 3.15.0.

Uses to guava version 29.0-jre.

Internal: setup GitHub actions CI build and sonar reporting.

3.4.3. AssertJ Guava 3.3.0

Release date: 2019-11-09

 Contributors

Thanks to chrisly42 and Stefano Cordio for their contributions!

 New features

Add InstanceOfAssertFactories to chain specific type assertions. (Stefano Cordio)

 Improvements

AssertJ’s Javadoc are now searchable.

Use beautiful AssertJ’s site code style for Javadoc :)

Migrate to JUnit 5 and assertj-core version 3.14.0.

 Fixed

Fix for OptionalAssert.contains() that was not working for primitive arrays. (chrisly42)

 Deprecated

Deprecate org.assertj.guava.data.MapEntry for org.assertj.core.data.MapEntry

Add InstanceOfAssertFactories to allow chain specific type assertions

Add factories for ByteSource, Multimap, Multiset, Optional (guava) and Table to allow to chain specific type assertions from a value initially declared as a less specific type.

Let’s start with the problem asInstanceOf is solving: in the following example we would like to call Table assertions but this is not possible since value is declared as an Object thus only Object assertions are accessible.

// Given a Table declared as an Object
Object actual = HashBasedTable.<Integer, Integer, String> create();

// We would like to call Table assertions but this is not possible since value is declared as an Object
assertThat(actual).isEmpty(); // this does not compile !

Thanks to asInstanceOf we can now tell AssertJ to consider value as a Table in order to call Table assertions.
To do so we need to pass an InstanceOfAssertFactory that can build a TableAssert, fortunately you don’t have to write it, it is already available in InstanceOfAssertFactories!

// Given a Table declared as an Object
Object actual = HashBasedTable.<Integer, Integer, String> create();

// With asInstanceOf, we switch to specific Table assertion by specifying the InstanceOfAssertFactory for Table
assertThat(value).asInstanceOf(InstanceOfAssertFactories.TABLE)
                 .isEmpty();

AssertJ verifies that the actual value is compatible with the assertions InstanceOfAssertFactory is going to give access to.

InstanceOfAssertFactories provides static factories for all types AssertJ provides assertions for, additional factories can be created with custom InstanceOfAssertFactory instances.

4. AssertJ Joda
4.1. Quick start

This guide is for the AssertJ Joda Time module.

4.1.1. Get assertj-joda-time library

AssertJ Joda Time artifacts are in the Maven central repository.

Supported Java versions

AssertJ Joda Time major versions depend on different Java versions:

AssertJ Joda Time 2.x requires Java 8 or higher

AssertJ Joda Time 1.x requires Java 7 or higher

Maven
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-joda-time</artifactId>
  <!-- use 1.1.0 for Java 7 projects -->
  <version>2.2.0</version>
  <scope>test</scope>
</dependency>
Gradle

For Gradle users (using the Maven Central Repository)

testImplementation("org.assertj:assertj-joda-time:2.2.0")

Or version 1.1.0 for Java 7 projects

testImplementation("org.assertj:assertj-joda-time:1.1.0")
Other build tools

Check this page to find the relevant assertj joda-time dependency declaration.

4.1.2. Use Assertions class entry point

The org.assertj.jodatime.api.Assertions class is the only class you need to start using AssertJ Joda Time.

import static org.assertj.jodatime.api.Assertions.assertThat;
4.1.3. Examples
assertThat(dateTime).isBefore(firstDateTime);
assertThat(dateTime).isAfterOrEqualTo(secondDateTime);

// you can use Strings in comparisons to avoid a conversion (we do that for you)
assertThat(new DateTime("2000-01-01")).isEqualTo("2000-01-01");

// compare DateTimes ignoring seconds and milliseconds in the comparison
dateTime1 = new DateTime(2000, 1, 1, 23, 50, 0, 0, UTC);
dateTime2 = new DateTime(2000, 1, 1, 23, 50, 10, 456, UTC);
// assertion succeeds
assertThat(dateTime1).isEqualToIgnoringSeconds(dateTime2);

For DateTime assertions, comparison is performed in the DateTimeZone of DateTime to test, consequently the following assertion passes:

DateTime utcTime = new DateTime(2013, 6, 10, 0, 0, DateTimeZone.UTC);
DateTime cestTime = new DateTime(2013, 6, 10, 2, 0, DateTimeZone.forID("Europe/Berlin"));

assertThat(utcTime).as("in UTC time").isEqualTo(cestTime);

You can compare DateTime to another DateTime, or LocalDateTime to LocalDateTime, but not DateTime to LocalDateTime, it doesn’t make sense as one is timezone dependent and the other is not.

Note that you can find more working examples in the JodaTimeAssertionsExamples.java class of the assertj-examples project.

4.1.4. IDE configuration

You can configure your IDE so that when you start typing as and trigger code completion assertThat will show up in the suggested completions.

Eclipse:

Go to Window > Preferences > Java > Editor > Content Assist > Favorites > New Type.

Enter org.assertj.jodatime.api.Assertions and click OK.

Check that you see org.assertj.jodatime.api.Assertions.* in Favorites.

Intellij Idea: No special configuration is needed, just start typing asser and then invoke completion (Ctrl-Space) twice.

4.2. Assertions Guide

This section describes the assertions provided by AssertJ Joda Time.

In addition to specific type assertions, each type inherits assertions from org.assertj.core.api.AbstractAssert.

4.2.1. LocalDate
Assertion	Description


hasYear(int expectedYear)

	

Verifies that the year of the actual LocalDate is equal to the given year




hasMonthOfYear(int expectedMonthOfYear)

	

Verifies that the month of the actual LocalDate is equal to the given month




hasDayOfMonth(int expectedDayOfMonth)

	

Verifies that the day of month of the actual LocalDate is equal to the given day of month




isAfter(org.joda.time.LocalDate other)

	

Verifies that the actual LocalDate is strictly after the given one




isAfter(String localDateAsString)

	

Calls isAfter(DateTime) with a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isAfterOrEqualTo(org.joda.time.LocalDate other)

	

Verifies that the actual LocalDate is after or equals to the given one




isAfterOrEqualTo(String localDateAsString)

	

Calls isAfterOrEqualTo(DateTime) with a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isBefore(org.joda.time.LocalDate other)

	

Verifies that the actual LocalDate is strictly before the given one




isBefore(String localDateAsString)

	

Calls isBefore(DateTime) with a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isBeforeOrEqualTo(org.joda.time.LocalDate other)

	

Verifies that the actual LocalDate is before or equals to the given one




isBeforeOrEqualTo(String localDateAsString)

	

Calls isBeforeOrEqualTo(DateTime) with a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isEqualTo(String localDateAsString)

	

Calls AbstractAssert.isEqualTo(Object) passing a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isIn(String…​ dateTimesAsString)

	

Calls isIn(DateTime…​) with DateTimes built from given Strings which must follow ISO8601 format yyyy-MM-dd




isNotEqualTo(String localDateAsString)

	

Calls isNotEqualTo(DateTime) with a LocalDate built from the given String which must follow ISO8601 format yyyy-MM-dd




isNotIn(String…​ localDatesAsString)

	

Calls isNotIn(org.joda.DateTime…​) with DateTime built from the given strings which must follow ISO8601 format yyyy-MM-dd

4.2.2. LocalDateTime
Assertion	Description


hasDayOfMonth(int expectedDayOfMonth)

	

Verifies that the day of month of the actual LocalDateTime is equal to the given day of month




hasHourOfDay(int expectedHourOfDay)

	

Verifies that the hour of the actual LocalDateTime is equal to the given hour




hasMillisOfSecond(int expectedMillisOfSecond)

	

Verifies that the milliseconds of the actual LocalDateTime is equal to the given milliseconds




hasMinuteOfHour(int expectedMinuteOfHour)

	

Verifies that the minute of the actual LocalDateTime is equal to the given minute




hasMonthOfYear(int expectedMonthOfYear)

	

Verifies that the month of the actual LocalDateTime is equal to the given month




hasSecondOfMinute(int expectedSecondOfMinute)

	

Verifies that the seconds of the actual LocalDateTime is equal to the given seconds




hasYear(int expectedYear)

	

Verifies that the year of the actual LocalDateTime is equal to the given year




isAfter(org.joda.time.LocalDateTime other)

	

Verifies that the actual LocalDateTime is strictly after the given one




isAfter(String localDateTimeAsString)

	

Calls isAfter(DateTime) with a LocalDateTime built from the given String which must follow ISO DateTime format.




isAfterOrEqualTo(org.joda.time.LocalDateTime other)

	

Verifies that the actual LocalDateTime is after or equals to the given one




isAfterOrEqualTo(String localDateTimeAsString)

	

Calls isAfterOrEqualTo(DateTime) with a LocalDateTime built from the given String which must follow ISO DateTime format.




isBefore(org.joda.time.LocalDateTime other)

	

Verifies that the actual LocalDateTime is strictly before the given one




isBefore(String localDateTimeAsString)

	

Calls isBefore(DateTime) with a LocalDateTime built from the given String which must follow ISO DateTime format.




isBeforeOrEqualTo(org.joda.time.LocalDateTime other)

	

Verifies that the actual LocalDateTime is before or equals to the given one




isBeforeOrEqualTo(String localDateTimeAsString)

	

Calls isBeforeOrEqualTo(DateTime) with a LocalDateTime built from the given String which must follow ISO DateTime format.




isEqualTo(String localDateTimeAsString)

	

Calls AbstractAssert.isEqualTo(Object) passing a LocalDateTime built from the given String which must follow ISO DateTime format.




isEqualToIgnoringHours(org.joda.time.LocalDateTime other)

	

Verifies that actual and given LocalDateTime have same year, month and day fields (hour, minute, second and millisecond fields are ignored in comparison)




isEqualToIgnoringMinutes(org.joda.time.LocalDateTime other)

	

Verifies that actual and given LocalDateTime have same year, month, day and hour fields (minute, second and millisecond fields are ignored in comparison)




isEqualToIgnoringSeconds(org.joda.time.LocalDateTime other)

	

Verifies that actual and given LocalDateTime have same year, month, day, hour and minute fields (second and millisecond fields are ignored in comparison)




isEqualToIgnoringMillis(org.joda.time.LocalDateTime other)

	

Verifies that actual and given LocalDateTime have same year, month, day, hour, minute and second fields, (millisecond fields are ignored in comparison)




isIn(String…​ localDateTimesAsString)

	

Calls isIn(DateTime…​) with DateTimes built from given Strings which must follow ISO DateTime format




isNotEqualTo(String localDateTimeAsString)

	

Calls isNotEqualTo(DateTime) with a LocalDateTime built from the given String which must follow ISO DateTime format




isNotIn(String…​ dateTimesAsString)

	

Calls isNotIn(org.joda.DateTime…​) with DateTime built from the given strings which must follow ISO DateTime format

4.2.3. DateTime
Assertion	Description


hasDayOfMonth(int expectedDayOfMonth)

	

Verifies that the day of month of the actual DateTime is equal to the given day of month




hasHourOfDay(int expectedHourOfDay)

	

Verifies that the hour of the actual DateTime is equal to the given hour




hasMillisOfSecond(int expectedMillisOfSecond)

	

Verifies that the milliseconds of the actual DateTime is equal to the given milliseconds




hasMinuteOfHour(int expectedMinuteOfHour)

	

Verifies that the minute of the actual DateTime is equal to the given minute




hasMonthOfYear(int expectedMonthOfYear)

	

Verifies that the month of the actual DateTime is equal to the given month




hasSecondOfMinute(int expectedSecondOfMinute)

	

Verifies that the seconds of the actual DateTime is equal to the given seconds




hasYear(int expectedYear)

	

Verifies that the year of the actual DateTime is equal to the given year




isAfter(org.joda.time.DateTime other)

	

Verifies that the actual DateTime is strictly after the given one




isAfter(String dateTimeAsString)

	

Calls isAfter(DateTime) with a DateTime built from the given String which must follow ISO DateTime format.




isAfterOrEqualTo(org.joda.time.DateTime other)

	

Verifies that the actual DateTime is after or equals to the given one




isAfterOrEqualTo(String dateTimeAsString)

	

Calls isAfterOrEqualTo(DateTime) with a DateTime built from the given String which must follow ISO DateTime format.




isBefore(org.joda.time.DateTime other)

	

Verifies that the actual DateTime is strictly before the given one




isBefore(String dateTimeAsString)

	

Calls isBefore(DateTime) with a DateTime built from the given String which must follow ISO DateTime format.




isBeforeOrEqualTo(org.joda.time.DateTime other)

	

Verifies that the actual DateTime is before or equals to the given one




isBeforeOrEqualTo(String dateTimeAsString)

	

Calls isBeforeOrEqualTo(DateTime) with a DateTime built from the given String which must follow ISO DateTime format.




isEqualTo(org.joda.time.DateTime expected)

	

Verifies that the actual DateTime is equal to the given one in actual’s DateTimeZone




isEqualTo(String dateTimeAsString)

	

Calls isEqualTo(DateTime) with a DateTime built from the given String which must follow ISO DateTime format.




isEqualToIgnoringHours(org.joda.time.DateTime other)

	

Verifies that actual and given DateTime have same year, month and day fields (hour, minute, second and millisecond fields are ignored in comparison)




isEqualToIgnoringMinutes(org.joda.time.DateTime other)

	

Verifies that actual and given DateTime have same year, month, day and hour fields (minute, second and millisecond fields are ignored in comparison)




isEqualToIgnoringSeconds(org.joda.time.DateTime other)

	

Verifies that actual and given DateTime have same year, month, day, hour and minute fields (second and millisecond fields are ignored in comparison)




isEqualToIgnoringMillis(org.joda.time.DateTime other)

	

Verifies that actual and given DateTime have same year, month, day, hour, minute and second fields, (millisecond fields are ignored in comparison)




isIn(org.joda.time.DateTime…​ expected)

	

Verifies that the actual DateTime is equal to one of the given DateTime in the actual’s DateTimeZone




isIn(String…​ dateTimesAsString)

	

Calls isIn(DateTime…​) with DateTimes built from given Strings which must follow ISO DateTime format




isNotEqualTo(org.joda.time.DateTime expected)

	

Verifies that the actual value is not equal to the given one in actual’s DateTimeZone




isNotEqualTo(String dateTimeAsString)

	

Calls isNotEqualTo(DateTime) with a DateTime built from the given String which must follow ISO DateTime format




isNotIn(org.joda.time.DateTime…​ expected)

	

Verifies that the actual DateTime is equal to one of the given DateTime in the actual’s DateTimeZone




isNotIn(String…​ dateTimesAsString)

	

Calls isNotIn(org.joda.DateTime…​) with DateTime built from the given strings which must follow ISO DateTime format

4.3. Javadoc

https://www.javadoc.io/doc/org.assertj/assertj-joda-time/ is the latest version of the javadoc.

4.4. Release Notes

Latest release notes:

AssertJ Joda Time 2.2.0

AssertJ Joda Time 2.1.0

AssertJ Joda Time 2.0.0

The Javadoc for this release can be found here: https://www.javadoc.io/doc/org.assertj/assertj-joda-time/2.2.0/index.html

4.4.1. AssertJ Joda Time 2.2.0

Release date: 2018-06-15

 Contributors

Thanks to Eugene Strepetov for his contribution.

 New features

Add LocalDate assertions providing the following ones (Eugene Strepetov):

hasYear: Verifies that the year of the actual LocalDate is equal to the given year.

hasMonthOfYear: Verifies that the month of the actual LocalDate is equal to the given month

hasDayOfMonth: Verifies that the day of month of the actual LocalDate is equal to the given day

isBefore: Verifies that the actual LocalDate is strictly before the given one.

isBeforeOrEqualTo: Verifies that the actual LocalDate is before or equals to the given one.

isEqualTo: Same assertion as AbstractAssert.isEqualTo(Object…​) but to be used with LocalDate String representation.

isAfter: Verifies that the actual LocalDate is strictly after the given one.

isAfterOrEqualTo: Verifies that the actual LocalDate is after or equals to the given one.

isIn: Same assertion as AbstractAssert.isIn(Object…​) but to be used with LocalDate String representation.

isNotIn: Same assertion as AbstractAssert.isNotIn(Object…​) but to be used with LocalDate String representation.

The assertions taking String parameter(s) can be used with LocalDate String representation: yyyy-MM-dd.

Examples:

LocalDate localDate = new LocalDate(2000, 1, 1);

assertThat(localDate).hasYear(2000)
                     .hasMonthOfYear(1)
                     .hasDayOfMonth(1)
                     .isBefore(new LocalDate(2000, 1, 2))
                     .isBefore("2000-01-02")
                     .isBeforeOrEqualTo(new LocalDate(2000, 1, 1))
                     .isBeforeOrEqualTo("2000-01-01")
                     .isBeforeOrEqualTo(new LocalDate(2000, 1, 2))
                     .isBeforeOrEqualTo("2000-01-02")
                     .isEqualTo(new LocalDate(2000, 1, 1))
                     .isEqualTo("2000-01-01")
                     .isAfterOrEqualTo(new LocalDate(2000, 1, 1))
                     .isAfterOrEqualTo("2000-01-01")
                     .isAfterOrEqualTo(new LocalDate(1999, 12, 31))
                     .isAfterOrEqualTo("1999-12-31")
                     .isAfter(new LocalDate(1999, 12, 31))
                     .isAfter("1999-12-31")
                     .isNotEqualTo("2000-01-15")
                     .isNotEqualTo(new LocalDate(2000, 1, 15))
                     .isIn(new LocalDate(1999, 12, 31), new LocalDate(2000, 1, 1))
                     .isIn("1999-12-31", "2000-01-01")
                     .isNotIn(new LocalDate(1999, 12, 31), new LocalDate(2000, 1, 2))
                     .isNotIn("1999-12-31", "2000-01-02");
4.4.2. AssertJ Joda Time 2.1.0

Release date: 2018-05-27

 Contributors

Thanks to John Killmer for his contribution.

 New features

Add LocalDateTime assertions providing the following ones (John Killmer):

hasYear: Verifies that the year of the actual LocalDateTime is equal to the given year.

hasMonthOfYear: Verifies that the month of the actual LocalDateTime is equal to the given month

hasDayOfMonth: Verifies that the day of month of the actual LocalDateTime is equal to the given day of month

hasHourOfDay: Verifies that the hour of the actual DateTime is equal to the given hour

hasMinuteOfHour: Verifies that the minute of the actual LocalDateTime is equal to the given minute

hasSecondOfMinute: Verifies that the seconds of the actual LocalDateTime is equal to the given seconds

hasMillisOfSecond: Verifies that the milliseconds of the actual LocalDateTime is equal to the given milliseconds

Examples:

DateTime dateTime = new DateTime(1999, 12, 31, 23, 59, 59, 999, DateTimeZone.UTC);

assertThat(dateTime).hasYear(1999)
                    .hasMonthOfYear(12)
                    .hasDayOfMonth(31)
                    .hasHourOfDay(23)
                    .hasMinuteOfHour(59)
                    .hasSecondOfMinute(59)
                    .hasMillisOfSecond(999);
4.4.3. AssertJ Joda Time 2.0.0

Release date: 2016-04-10

 Contributors

Thanks to Pascal Schumacher and David Simmons for their contributions.

 Breaking changes

AssertJ Joda Time 2.0.0 requires Java 8 as it relies on AssertJ Core 3.x, use 1.1.0 version if you are still using Java 7.

 Improvements

DateTime assertion: better handling of null in assertions. (David Simmons)

To be OS agnostic, replace \n with %n in error messages. (Pascal Schumacher)

Better spacing in Javadoc code examples. (Pascal Schumacher)

5. AssertJ Neo4j
6. AssertJ DB

AssertJ-DB provides assertions to test data in a database. It requires Java 8 or later and can be used with either JUnit or TestNG.

If you need additional assertions, please create a ticket in the AssertJ-DB issue tracker.

AssertJ-DB is hosted on GitHub: https://github.com/assertj/assertj-db.

Big thanks to Joel Costigliola for his welcome, for his help and for having accepted to associate this project with a great project like AssertJ.

Régis Pouiller (AssertJ-DB creator)

6.1. Quick start

Suppose that the database contains this table MEMBERS :

ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

05-10-60

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

08-08-61

	

1.77




3

	

'Clayton'

	

'Adam'

	

 

	

03-13-60

	

1.78




4

	

'Mullen'

	

'Larry'

	

 

	

10-31-61

	

1.70

To quickly start using DataBase assertions, follow the steps below.

6.1.1. Add the assertj-db dependency to your project
Maven
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-db</artifactId>
  <version>3.0.1</version>
  <scope>test</scope>
</dependency>
Gradle

For Gradle users (using the Maven Central Repository)

testImplementation("org.assertj:assertj-db:3.0.1")
Other dependency management tool

Check this page to find the relevant assertj db dependency declaration.

6.1.2. Statically import org.assertj.db.api.Assertions.assertThat

... and use your preferred IDE code completion after assertThat.

Example from TableAssertionExamples.java :

import static org.assertj.db.api.Assertions.assertThat;

import org.assertj.db.type.AssertDbConnection;
import org.assertj.db.type.AssertDbConnectionFactory;
import org.assertj.db.type.DateValue;
import org.assertj.db.type.Table;

private AssertDbConnection assertDbConnection = AssertDbConnectionFactory.of("jdbc:h2:mem:test", "sa", "").create();

Table table = assertDbConnection.table("members").build();

// Check column "name" values
assertThat(table).column("name")
        .value().isEqualTo("Hewson")
        .value().isEqualTo("Evans")
        .value().isEqualTo("Clayton")
        .value().isEqualTo("Mullen");

// Check row at index 1 (the second row) values
assertThat(table).row(1)
        .value().isEqualTo(2)
        .value().isEqualTo("Evans")
        .value().isEqualTo("David Howell")
        .value().isEqualTo("The Edge")
        .value().isEqualTo(DateValue.of(1961, 8, 8))
        .value().isEqualTo(1.77);

In this simple example you can see many `[concepts of AssertJ-DB] (the concepts are simple but I advice you to take the time to get to know them well) :

the elements :

Table which represents a table in the database

Column which represents a column of the table

Row which represents a row of the table

Value which represents a value in a column or in a row

the navigation :

The first check, navigates from the table to the column called "name" (column("name") moves the assertion to the column), from this column to the first value (the first call of value() moves to the first value) and after that to each value (each call of value() moves to the next value of the column).

The second check, navigates from the table to the row with index 1 (row(1) moves the assertion to the row), from this row to the first value and after that to each value (value() calls have similar behavior for rows and columns).

DateValue : Since 2.0.0, AssertJ-DB baseline is Java 8. The preferred way to compare values with date, time and date/time is to use java.time.LocalDate, java.time.LocalTime, java.time.LocalDateTime. But for the backward compatibility, it’s always possible to use AssertJ-DB DateValue utilities.

6.2. Concepts

Connection to the database

AssertDbConnection (since 3.0.0)

LetterCase setup (since 3.0.0)

Schema retrieval mode (since 3.0.0)

Elements of the database

Table (modified in 3.0.0)

Request (modified in 3.0.0)

Changes (modified in 3.0.0)

Change

Row

Column

Value

Type

DataType

ChangeType

ValueType

OrderType (since 1.2.0)

Navigation

With a Table or a Request as root

With Changes as root

DateValue, TimeValue and DateTimeValue

Default description

Letter Case of the database (since 1.1.0)

CaseConversion

CaseComparison

lettercase

Output (since 1.1.0)

Type of output

Destination

For the examples below, suppose that the database contains these three tables :

Table 1. MEMBERS
ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

05-10-60

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

08-08-61

	

1.77




3

	

'Clayton'

	

'Adam'

		

03-13-60

	

1.78




4

	

'Mullen'

	

'Larry'

		

10-31-61

	

1.70

Table 2. ALBUMS
ID	RELEASE	TITLE	NUMBEROFSONGS	DURATION	LIVE


1

	

10-20-80

	

'Boy'

	

12

	

42:17

	


2

	

10-12-81

	

'October'

	

11

	

41:08

	


3

	

02-28-83

	

'War'

	

10

	

42:07

	


4

	

11-07-83

	

'Under a Blood Red Sky'

	

8

	

33:25

	

true




5

	

10-01-84

	

'The Unforgettable Fire'

	

10

	

42:42

	


6

	

06-10-85

	

'Wide Awake in America'

	

4

	

20:30

	

true




7

	

03-09-87

	

'The Joshua Tree'

	

11

	

50:11

	


8

	

10-10-88

	

'Rattle and Hum'

	

17

	

72:27

	


9

	

11-18-91

	

'Achtung Baby'

	

12

	

55:23

	


10

	

07-06-93

	

'Zooropa'

	

10

	

51:15

	


11

	

03-03-97

	

'Pop'

	

12

	

60:08

	


12

	

10-30-00

	

'All That You Can’t Leave Behind'

	

11

	

49:23

	


13

	

11-22-04

	

'How to Dismantle an Atomic Bomb'

	

11

	

49:08

	


14

	

03-02-09

	

'No Line on the Horizon'

	

11

	

53:44

	


15

	

09-09-14

	

'Songs of Innocence'

	

11

	

48:11

	
Table 3. GROUP
ID	NAME


1

	

'U2'




2

	

'Coldplay'

6.2.1. Connection to the database

To make assertions on a database, it is necessary to connect. The concept of AssertDbConnection represent how AssertJ-DB can retrieve data and schema information from database.

It’s also with a AssertDbConnection that you can instantiate the following element : Table, Request, Changes.

AssertDbConnection

A AssertDbConnection is created with the factory AssertDbConnectionFactory.

There are 2 way to begin the AssertDbConnectionFactory, with a DataSource ( the classic Java way to get a Connection to a database ) or with JDBC connection information.

Below is an example of using a DataSource to connect to H2 in memory database :

AssertDbConnection connection = AssertDbConnectionFactory.of("jdbc:h2:mem:test", "sa", "").create();

And using a DataSource to connect :

AssertDbConnection connection = AssertDbConnectionFactory.of(dataSource).create();
LetterCase setup

AssertDbConnectionFactory provide the capacity to indicate the LetterCase to use for the tables, columns and primary keys.

AssertDbConnection connection = AssertDbConnectionFactory
    .of(dataSource)
    .letterCase(tableLetterCase, columnLetterCase, pkLetterCase)
    .create();

For more information, see the paragraph on LetterCase.

Schema retrieval mode

Since 3.0.0

For many assertions, AssertJ-DB require to discover database schema metadata ( list of tables, columns, …​ ). When the schema contains many tables this operation can slow down the tests executions.

To avoid that and when the database schema is not updated during the test session, you can use the option SchemaMetaDataMode of AssertDbConnectionFactory to keep in memory the schema.

Available mode are :

DYNAMIC ( default ): Retrieve schema metadata each time is required.

STATIC : Retrieve schema metadata only once and keep in memory for all duration of connection.

Below is an example of using the STATIC mode for a connection :

AssertDbConnection connection = AssertDbConnectionFactory.of(dataSource)
    .schemaMetaDataMode(SchemaMetaDataMode.STATIC)
    .create();
6.2.2. Elements of the database

Here the elements on which it is possible to make assertions.

Note that, there are only 3 root elements : Table, Request and Changes.

That means that the other elements are components or sub components of a root element.

A root element is an element on which the assertion start (in practice, the parameter of a assertThat(…​) method).

Table

A Table represents a table in the database.

A Table can be constructed with the builder method table(String name) from AssertDbConnection.

// Prepare the connection
AssertDbConnection connection = ...
// Declare the "members" table by using a AssertDbConnection table builder
Table table1 = connection.table("members").build();

For more information about table construction, see the Table.Builder javadoc.

Table 4. Representation of "table1"
ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

05-10-60

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

08-08-61

	

1.77




3

	

'Clayton'

	

'Adam'

		

03-13-60

	

1.78




4

	

'Mullen'

	

'Larry'

		

10-31-61

	

1.70

For a Table, it is possible to choose the columns to include and to exclude in the assertions.

// Get the data of the "id" and "name" columns of the "members" table
Table table2 = connection.table("members").columnsToCheck(new String[] { "id", "name" }).build();
// Get the data of the "members" table but not of the "birthdate" column
Table table3 = connection.table("members").columnsToExclude(new String[] { "birthdate" }).build();
// Get the data of the "name" column of the "members" table (because "id" is included and excluded)
Table table4 = connection.table("members").columnsToCheck(new String[] { "id", "name" }).columnsToExclude(new String[] { "id" }).build();
Table 5. Representation of "table2"
ID	NAME


1

	

'Hewson'




2

	

'Evans'




3

	

'Clayton'




4

	

'Mullen'

Table 6. Representation of "table3"
ID	NAME	FIRSTNAME	SURNAME	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

1.77




3

	

'Clayton'

	

'Adam'

		

1.78




4

	

'Mullen'

	

'Larry'

		

1.70

Table 7. Representation of "table4"
NAME


'Hewson'




'Evans'




'Clayton'




'Mullen'

Since version 1.2.0, there are the possibility to indicate delimiters (start delimiter and end delimiter) and Order.

The delimiters are useful when the table name or column name is a reserved word or contains special characters (like space or '%'). Order allows to choose the order of the Row.

// The line code below throws SQLException because "group" is SQL reserved word
Table table5 = connection.table("group").build();
// Get the data of the "group" table by using "`" delimiter
// That generates a request
Table table6 = connection.table("group").delimiters('`', '`').build();

// Get the data from "members" table and order on "name" column in ascending order
Table table7 = connection.table("members").columnsToOrder(new Order[] { Order.asc("name") }).build();
Table 8. Representation of "table6"
ID	NAME


1

	

'U2'




2

	

'Colplay'

Table 9. Representation of "table7"
ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


3

	

'Clayton'

	

'Adam'

		

03-13-60

	

1.78




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

08-08-61

	

1.77




1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

05-10-60

	

1.75




4

	

'Mullen'

	

'Larry'

		

10-31-61

	

1.70

Request

A Request represents a SQL request on the database.

Like a Table, a Request can be constructed with the builder method request(String sql) from AssertDbConnection.

// Prepare the connection
AssertDbConnection connection = ...
// Declare a request which gets the name and the firstname of the corresponding members
Request request1 = connection.request("select name, firstname from members where id = 2 or id = 3").build();

For more information about request construction, see the Request.Builder javadoc.

Table 10. Representation of "request1"
NAME	FIRSTNAME	SURNAME


'Evans'

	

'David Howell'

	

'The Edge'




'Clayton'

	

'Adam'

	

For a Request, it is possible to use a simple SQL request or a SQL request with one or many parameters.

// Declare a request which gets the name and the firstname of the members
// and use "%e%" as a parameter
Request request2 = connection.request(
                               "select name, firstname from members " +
                               "where name like ?;")
                               .parameters("%e%")
                               .build();
// Declare a request which gets the name and the firstname of the members
// and use "%e%" and "%Paul%" as parameters
Request request3 = connection.request(
                               "select name, firstname from members " +
                               "where name like ? and firstname like ?;")
                               .parameters("%e%", "%Paul%")
                               .build();
Table 11. Representation of "request2"
NAME	FIRSTNAME	SURNAME


'Hewson'

	

'Paul David'

	

'Bono'




'Evans'

	

'David Howell'

	

'The Edge'




'Mullen'

	

'Larry'

	
Table 12. Representation of "request3"
NAME	FIRSTNAME	SURNAME


'Hewson'

	

'Paul David'

	

'Bono'

Changes

The Changes are the differences of states in database between a start point and a end point.

Assume that there are these SQL statements between the start point and the end point.

DELETE FROM ALBUMS WHERE ID = 15;
INSERT INTO MEMBERS(ID, NAME, FIRSTNAME) VALUES(5, 'McGuiness', 'Paul');
UPDATE MEMBERS SET SURNAME = 'Bono Vox' WHERE ID = 1;
UPDATE ALBUMS SET NAME = 'Rattle & Hum', LIVE = true WHERE ID = 8;
// Prepare the connection
AssertDbConnection connection = ...
// The changes can be on a DataSource or on a Source
Changes changes1 = connection.changes().build();
// The changes can also be on a Table or on a Request
Changes changes2 = connection.changes().table(table3).build();
Changes changes3 = connection.changes().request(request2).build();
// The names of the columns used for the primary key are found in the metadata for a table
// but for a request it can be important to set the primary key
Changes changes4 = connection.changes().request("select name, firstname from members", r -> r.pksName("name")).build();

For more information about changes construction, see the Changes.Builder javadoc.

The changes are ordered :

First by the type of the change : creation, modification and after deletion

After if it is a change on a table by the name of the table

To finish by the values of the primary key and if there are no primary key by the values of the row (for a modification)

As indicated above, the primary key is used to order the changes. But more important, the primary key is used to determinate which rows at the same with modifications.

In Representation of "changes3" the modification of first row of the table become a creation and deletion.

Table 13. Representation of "changes1"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


At start point

						


At end point

	

5

	

'McGuiness'

	

'Paul'

			



Modification

	

"ALBUMS" table

	

8 as PK

	
	ID	RELEASE	TITLE	NUMBEROFSONGS	DURATION	LIVE


At start point

	

8

	

10-10-88

	

'Rattle and Hum'

	

17

	

72:27

	


At end point

	

8

	

10-10-88

	

'Rattle & Hum'

	

17

	

72:27

	

true




Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	BIRTHDATE	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

05-10-60

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

05-10-60

	

1.75




Deletion

	

"ALBUMS" table

	

15 as PK

	
	ID	RELEASE	TITLE	NUMBEROFSONGS	DURATION	LIVE


At start point

	

15

	

09-09-14

	

'Songs of Innocence'

	

11

	

48:11

	


At end point

						
Table 14. Representation of "changes2"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

					


At end point

	

5

	

'McGuiness'

	

'Paul'

		



Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

1.75

Table 15. Representation of "changes3"

Creation

		

No PK

	
	NAME	FIRSTNAME	SURNAME


At start point

			


At end point

	

'Hewson'

	

'Paul David'

	

'Bono Vox'




Creation

		

No PK

	
	NAME	FIRSTNAME	SURNAME


At start point

			


At end point

	

'McGuiness'

	

'Paul'

	



Deletion

		

No PK

	
	NAME	FIRSTNAME	SURNAME


At start point

			


At end point

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

Table 16. Representation of "changes4"

Creation

		

'McGuiness' as PK

	
	NAME	FIRSTNAME	SURNAME


At start point

			


At end point

	

'McGuiness'

	

'Paul'

	



Modification

		

'Hewson' as PK

	
	NAME	FIRSTNAME	SURNAME


At start point

	

'Hewson'

	

'Paul David'

	

'Bono'




At end point

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

Change

A Change is an element of the Changes.

Below framed in red the first Change of "changes2".

Table 17. Representation of "changes2"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

					


At end point

	

5

	

'McGuiness'

	

'Paul'

		



Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

1.75

Row

A Row can represent a row of a Table , of a Request or of a Change.

Below framed in red the third Row of "table3".

Table 18. Representation of "table3"
ID	NAME	FIRSTNAME	SURNAME	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

1.77




3

	

'Clayton'

	

'Adam'

		

1.78




4

	

'Mullen'

	

'Larry'

		

1.70

Below framed in red the second Row of "request2".

Table 19. Representation of "request2"
NAME	FIRSTNAME	SURNAME


'Hewson'

	

'Paul David'

	

'Bono'




'Evans'

	

'David Howell'

	

'The Edge'




'Mullen'

	

'Larry'

	

Below framed in red the Row at end point of the second Change of "changes3".

Table 20. Representation of "changes2"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

					


At end point

	

5

	

'McGuiness'

	

'Paul'

		



Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

1.75

Column

A Column can represent a column of a Table , of a Request or of a Change.

Below framed in red the second Column of "table3".

Table 21. Representation of "table3"
ID	NAME	FIRSTNAME	SURNAME	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

1.77




3

	

'Clayton'

	

'Adam'

		

1.78




4

	

'Mullen'

	

'Larry'

		

1.70

Below framed in red the second Column of "request2".

Table 22. Representation of "request2"
NAME	FIRSTNAME	SURNAME


'Hewson'

	

'Paul David'

	

'Bono'




'Evans'

	

'David Howell'

	

'The Edge'




'Mullen'

	

'Larry'

	

Below framed in red the fourth Column of the second Change of "changes3".

Table 23. Representation of "changes2"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

					


At end point

	

5

	

'McGuiness'

	

'Paul'

		



Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

1.75

Value

A value can be in a Row or in a Column.

Below framed in red (depending of the path) :

the second value of the third Row of "table3"

the third value of the second Column of "table3"

Table 24. Representation of "table3"
ID	NAME	FIRSTNAME	SURNAME	SIZE


1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




2

	

'Evans'

	

'David Howell'

	

'The Edge'

	

1.77




3

	

'Clayton'

	

'Adam'

		

1.78




4

	

'Mullen'

	

'Larry'

		

1.70

Below framed in red (depending of the path) :

the second value of the second Row of "request2"

the second value of the second Column of "request2"

Table 25. Representation of "request2"
NAME	FIRSTNAME	SURNAME


'Hewson'

	

'Paul David'

	

'Bono'




'Evans'

	

'David Howell'

	

'The Edge'




'Mullen'

	

'Larry'

	

Below framed in red (depending of the path) :

the fourth value of the Row at end point of the second Change of "changes2"

the value at end point of the fourth Column of the second Change of "changes2"

Table 26. Representation of "changes2"

Creation

	

"MEMBERS" table

	

5 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

					


At end point

	

5

	

'McGuiness'

	

'Paul'

		



Modification

	

"MEMBERS" table

	

1 as PK

	
	ID	NAME	FIRSTNAME	SURNAME	SIZE


At start point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono'

	

1.75




At end point

	

1

	

'Hewson'

	

'Paul David'

	

'Bono Vox'

	

1.75

6.2.3. Type
Data Type

As see above there are three root elements of database, but only Table and Request are data elements. All the possible types of data are contained in the DataType enumeration.

The type of the data can be :

TABLE

REQUEST

Change Type

The change can be a creation, a modification or a deletion. All the possible types of change are contained in the ChangeType enumeration.

The type of the change depends of operation on database :

CREATION for a insert sql request

MODIFICATION for a update sql request

DELETION for a delete sql request

Value Type

The value can be a date, a boolean or a text for example. All the possible types of value are contained in the ValueType enumeration.

The type of the value depends of class of the object given by java.sql when the data are got from database :

BYTES for a array of bytes (byte[])

BOOLEAN for a java.lang.Boolean

TEXT for a java.lang.String

DATE for a java.sql.Date

TIME for a java.sql.Time

DATE_TIME for a java.sql.Timestamp

UUID for a java.util.UUID (since 1.1.0)

NUMBER for a java.lang.Byte, java.lang.Short, java.lang.Integer, java.lang.Long, java.lang.Double, java.lang.Float or java.math.BigDecimal

NOT_IDENTIFIED for other cases (for example when the value is null)

Order Type

Since 1.2.0

The order can be a ascending or descending. All the possible types of order are contained in the Table.Order.OrderType enumeration.

The type of the order can be :

ASC for an ascending order

DESC for a descending order

6.2.4. Navigation

The navigation offers the ability to chain assertions at different levels and instructions to go inside the sub-elements and return to root element.

There are examples of the navigation in NavigationExamples.java

With a Table or a Request as root

The assertThat(…​) static method of org.assertj.db.api.Assertions allows to create a root assertion on a Table.

import static org.assertj.db.api.Assertions.assertThat;

assertThat(table)...

or on a Request.

import static org.assertj.db.api.Assertions.assertThat;

assertThat(request)...

From these root assertions, it is possible to navigate to the sub elements and return to the root element as in the picture below.

More details on this concept in assertj-db-features-highlight.html#tableorrequestasroot[feature highlight].

With Changes as root

The assertThat(…​) static method of org.assertj.db.api.Assertions allows to create a root assertion on Changes.

import static org.assertj.db.api.Assertions.assertThat;

assertThat(changes)...

From this root assertion, it is possible to navigate to the sub elements and return to the root element as in the picture below.

More details on this concept in feature highlight.

6.2.5. DateValue, TimeValue and DateTimeValue

Since 2.0.0, AssertJ-DB baseline is Java 8. The preferred way to compare values with date, time and date/time is to use java.time.LocalDate, java.time.LocalTime, java.time.LocalDateTime directly.

But for the backward compatibility, it’s always possible to use AssertJ-DB DateValue utilities.

So The DateValue, TimeValue and DateTimeValue classes are simpler but contains this kind of informations.

There is 4 kinds of static methods to instantiate these values :

of which receives the informations as int parameters

DateValue dateValue = DateValue.of(2007, 12, 23);

// With hours and minutes only
TimeValue timeValue1 = TimeValue.of(9, 1);
// With seconds additional
TimeValue timeValue2 = TimeValue.of(9, 1, 6);
// With nanoseconds additional
TimeValue timeValue3 = TimeValue.of(9, 1, 6, 3);

// With date only (so hour is midnight)
DateTimeValue dateTimeValue1 = DateTimeValue.of(dateValue);
// With date and time
DateTimeValue dateTimeValue2 = DateTimeValue.of(dateValue, timeValue1);

from which receives the equivalent from java.sql package (java.sql.Date, java.sql.Time and java.sql.Timestamp) or a java.util.Calendar (since 1.1.0)

Date date = Date.valueOf("2007-12-23");
DateValue dateValue = DateValue.from(date);

Time time = Time.valueOf("09:01:06");
TimeValue timeValue = TimeValue.from(time);

Timestamp timestamp = Timestamp.valueOf("2007-12-23 09:01:06.000000003");
DateTimeValue dateTimeValue = DateTimeValue.from(timestamp);

// Since 1.1.0
Calendar calendar = Calendar.getInstance();
DateValue dateValueFromCal = DateValue.from(calendar);
TimeValue timeValueFromCal = TimeValue.from(calendar);
DateTimeValue dateTimeValueFromCal = DateTimeValue.from(calendar);

parse which receives a String to represent the value (this method can throw a ParseException)

DateValue dateValue = DateValue.parse("2007-12-23");

// With hours and minutes only
TimeValue timeValue1 = TimeValue.parse("09:01");
// With seconds additional
TimeValue timeValue2 = TimeValue.parse("09:01:06");
// With nanoseconds additional
TimeValue timeValue3 = TimeValue.parse("09:01:06.000000003");

// With date only (so hour is midnight)
DateTimeValue dateTimeValue1 = DateTimeValue.parse("2007-12-23");
// With date and time (hours and minutes only)
DateTimeValue dateTimeValue2 = DateTimeValue.parse("2007-12-23T09:01");
// With date and time (seconds additional)
DateTimeValue dateTimeValue2 = DateTimeValue.parse("2007-12-23T09:01:06");
// With date and time (nanoseconds additional)
DateTimeValue dateTimeValue2 = DateTimeValue.parse("2007-12-23T09:01:06.000000003");

now (since 1.1.0) which create an instance corresponding to the current moment.

DateValue dateValue = DateValue.now();                   // The current date
TimeValue timeValue = TimeValue.now();                   // The current time
DateTimeValue dateTimeValue = DateTimeValue.now();       // The current date/time

All these static methods (except for now method) have equivalent constructors.

6.2.6. Default description

In assertj, it is possible to add a description with the methods of the Descriptable interface. This description is used in the error message if the assertion fails.

Due to the navigation, it is more complicated in assertj-db to know on which element an error is thrown. So to help the tester, there are default descriptions.

For example :

"members table" for an assertion on a table

"'select * from actor' request" for an assertion on a request

"'select id, name, firstname, bi…​' request" for an assertion on a request with more text

"Row at index 0 of members table" for an assertion on a row of a table

"Column at index 0 (column name : ID) of 'select * from members' request" for an assertion on a column of a request

"Value at index 0 of Column at index 0 (column name : ID) of 'select * from members' request" for an assertion on a value of a column of a request

"Value at index 0 (column name : ID) of Row at index 0 of 'select * from members' request" for an assertion on a value of a row of a request

"Value at index 0 (column name : ID) of Row at end point of Change at index 0 (on table : MEMBERS and with primary key : [4]) of Changes on tables of 'sa/jdbc:h2:mem:test' source" for an assertion on a value of the row at end point of a change on a table

This default description can be replaced by the choice of the tester by using the methods of Descriptable.

6.2.7. Letter Case of the database

Since 1.1.0

Databases have different letter cases for the name of the elements. For example, the name of the table can be upper case either the name is inputted in upper case or not. So this concept (and feature too) is here to manage these shades.

It is possible to declare a LetterCase with a AssertDbConnection with LetterCase.

The concept of LetterCase is composed of CaseConversion and CaseComparison.

CaseConversion

The CaseConversion is used when getting a name with letter case from database : a table name, a column name or a primary key name.

There are three conversions modes : UPPER which converts to upper case ("Name" becomes "NAME"), LOWER which converts to lower case ("Name" becomes "name") and NO which keeps the case ("Name" remains "Name").

Each name (table, column and primary key) got from the database is converted using a CaseConversion.

CaseComparison

The CaseComparison is used when comparing something with letter case from database or with a parameter.

There are two comparison modes : IGNORE which compares String`s by ignoring the case (`"Name" is considered equal to "NAME") and STRICT which compares String`s strictly (`"Name" is considered different from "NAME").

During navigation (e.g. from table to column) and assertion (e.g. on column name), the name are compared using a CaseComparison.

LetterCase

A LetterCase is created with the getLetterCase static method which has a CaseConversion and a CaseComparison as parameters.

LetterCase letterCase = LetterCase.getLetterCase(CaseConversions.NO, CaseComparisons.IGNORE);

In AssertJ-DB, there are three different uses of a LetterCase : the table name, the column name and the primary key name. That is the reason why the AssertDbConnection have three LetterCase parameters.

The LetterCase on the tables is used :

to convert the table name : when a name is got from the database like for the Table instantiation or for the table with changes found with Changes.

to compare the table name : for the instantiation when the table is search in the database for Table, for navigation (e.g. from changes to a change on a table) or for a assertion (like isOnTable(String name)).

The LetterCase on the columns is used :

to convert the column name : when a column name is got from the database for a table or a request

to compare the column name : for the navigation (e.g. from a table to a column) or for a assertion (like hasColumnName(String columnName)).

The LetterCase on the primary keys is used :

to convert the primary key name : when a primary key name is got from the database for a table

to compare the primary key name : for a assertion (like hasPksNames(String…​ names)).

The default settings for LetterCase in AssertDbConnection are :

NO conversion and IGNORE comparison for table names

UPPER conversion and IGNORE comparison for the column and primary key name

In this example, the two connections are equivalent :

AssertDbConnection jdbcConnection = AssertDbConnectionFactory.of("jdbc:h2:mem:test", "sa", "").create();
Table table = jdbcConnection.table("members").build();

LetterCase tableLetterCase = LetterCase.getLetterCase(CaseConversions.NO, CaseComparisons.IGNORE);
LetterCase columnLetterCase = LetterCase.getLetterCase(CaseConversions.UPPER, CaseComparisons.IGNORE);
LetterCase pkLetterCase = LetterCase.getLetterCase(CaseConversions.UPPER, CaseComparisons.IGNORE);
AssertDbConnection connectionWithLC = AssertDbConnectionFactory.of("jdbc:h2:mem:test", "sa", "")
                                        .letterCase(tableLetterCase, columnLetterCase, pkLetterCase)
                                        .create();
Table tableWithLC = connectionWithLC.table("members").build();

Note that the letter case is extensible because the getLetterCase static method’s parameters are instances of the CaseConversion and the CaseComparison interfaces. So this is not limited to the implementations in the corresponding enumerations.

6.2.8. Output

Since 1.1.0

It can be interesting to view the values on which an assertion is made (for example for debugging). The output allows that.

This is a simple example :

import static org.assertj.db.output.Outputs.output;

Table table = connection.table("members");

// Output the content of the table in the console
output(table).toConsole();

These lines give the result below :

[MEMBERS table]
|-----------|---------|-----------|-----------|--------------|-----------|-----------|-----------|
|           |         | *         |           |              |           |           |           |
|           | PRIMARY | ID        | NAME      | FIRSTNAME    | SURNAME   | BIRTHDATE | SIZE      |
|           | KEY     | (NUMBER)  | (TEXT)    | (TEXT)       | (TEXT)    | (DATE)    | (NUMBER)  |
|           |         | Index : 0 | Index : 1 | Index : 2    | Index : 3 | Index : 4 | Index : 5 |
|-----------|---------|-----------|-----------|--------------|-----------|-----------|-----------|
| Index : 0 | 1       | 1         | Hewson    | Paul David   | Bono      | 05-10-60  | 1.75      |
| Index : 1 | 2       | 2         | Evans     | David Howell | The Edge  | 08-08-61  | 1.77      |
| Index : 2 | 3       | 3         | Clayton   | Adam         |           | 03-13-60  | 1.78      |
| Index : 4 | 4       | 4         | Mullen    | Larry        |           | 10-31-61  | 1.70      |
|-----------|---------|-----------|-----------|--------------|-----------|-----------|-----------|

In the example above, the output is in plain text in the console. It is possible to change the type of the output and the destination.

Type of output

There are two outputs already implemented :

PLAIN : shown in the example above (the default output type)

HTML : which represents the result as an HTML document

// Change the output of the table to be HTML
output(table).withType(OutputType.HTML).....;

Note that the type of output is extensible because the withType(Output outputType) method’s parameter is an instance of the Output interface. So this is not limited to the implementations in the OutputType enum.

Destination

The destination is the way to print the display. There are three destinations :

the console (with the toConsole() method)

a file (with the toFile(String fileName) method)

a stream (with the toStream(OutputStream outputStream) method)

Note that with this last method the possibilities of destination are really flexible.

These three methods are fluent. In this short example, the output is a plain text representation in the console and a html output in a file :

// Display the content of the table with plain text in the console
// and with HTML output in the file
output(table).toConsole().withType(OutputType.HTML).toFile("test.html");
6.3. Features highlight

Before reading this page, it is recommended to be familiar with the concepts of AssertJ-DB.

The purpose of this page is to show the different features of AssertJ-DB.

Navigation

With a Table or a Request as root

To a Row

To a Column

To a Value

With Changes as root

To Changes

To a Change

To a Row

To a Column

To a Value

Assertions

On the type of change

On the equality with the values of a column

With Boolean

With Bytes

With Number

With Date

With Time

With Date/Time

With String

With UUID (since in 1.1.0)

With Character (since in 1.2.0)

On the name of a column

On the nullity of the values of a column

On the nullity of the values of a row (since in 1.2.0)

On the type of column

On the class of column (since in 1.1.0)

On the content of column (since in 1.1.0)

On the type of data

On the modified columns in a change (modified in 1.1.0)

On the number of changes (modified in 1.1.0)

On the number of columns (modified in 1.1.0)

On the number of rows (modified in 1.1.0 and 1.2.0)

On the primary keys

On the equality with the values of a row

On the existence of a row in a change

On the chronology of a value

On the comparison with a value

On the closeness of a value (since in 1.1.0)

On the equality with a value

With Boolean

With Bytes

With Number

With Date

With Time

With Date/Time

With String

With UUID (since in 1.1.0)

With Character (since in 1.2.0)

On the non equality with a value

With Boolean

With Bytes

With Number

With Date

With Time

With Date/Time

With String

With UUID (since in 1.1.0)

With Character (since in 1.2.0)

On the nullity of a value

On the type of a value

On the class of a value (since in 1.1.0)

6.3.1. Navigation
With a Table or a Request as root

As shown in the concepts (to easily understand this chapter it is important to know the concepts of assertj-db), the assertThat(…​) static method is used to begin an assertion on a Table or on a Request.

The navigation from a table or from a request are similar, so in most of the examples below a table will be used :

assertThat(tableOrRequest)...

If there is a difference if will be specified.

All the navigation methods work from an origin point. That means that if the method is executed from another point, it is like the execution is from the point of view of the origin.

There are some recurring points in the different navigation methods :

a method without parameter which allows to navigate on the next element after the element reached on the last call (if it is the first call, navigate to the first element)

a method with an int parameter (an index) which allows to navigate on the element which is at the corresponding index

a method with an String parameter (a column name) which allows to navigate on the element corresponding at the column name

To a Row

These methods are described in the ToRow interface.

The row() method allows to navigate to the next row after the row reached on the last call.

// If it is the first call, navigate to the first row
assertThat(tableOrRequest).row()...
// It is possible to chain the calls to navigate to the next row
// after the first row (so the second row)
assertThat(tableOrRequest).row().row()...

The row(int index) method with index as parameter allows to navigate to the row corresponding to row at the index.

// Navigate to the row at index 2
assertThat(tableOrRequest).row(2)...
// It is possible to chain the calls to navigate to another row.
// Here row at index 6
assertThat(tableOrRequest).row(2).row(6)...
// It is possible to combine the calls to navigate to the next row
// after the row at index 2. Here row at index 3
assertThat(tableOrRequest).row(2).row()...

This picture shows from where it is possible to navigate to a row.

The origin point of the row(…​) methods is the Table or the Request. So if the method is executed from a row, from a column or from a value it is like if the method was executed from the Table or the Request.

When the position is on a row, it is possible to return to the origin.

// Return to the table from a row of a table
assertThat(table).row().returnToTable()...
// Return to the request from a row of a request
assertThat(request).row().returnToRequest()...

That also means that the two navigations below are equivalent.

// Navigate to the first row
// Return to the table from this row
// Navigate to the next row
assertThat(table).row().returnToTable().row()...
// The same thing is done but the return to the table is implicit
assertThat(table).row().row()...
To a Column

These methods are described in the ToColumn interface.

The column() method allows to navigate to the next column after the column reached on the last call.

// If it is the first call, navigate to the first column
assertThat(tableOrRequest).column()...
// It is possible to chain the calls to navigate to the next column
// after the first column (so the second column)
assertThat(tableOrRequest).column().column()...

The column(int index) method with index as parameter allows to navigate to the column corresponding to column at the index.

// Navigate to the column at index 2
assertThat(tableOrRequest).column(2)...
// It is possible to chain the calls to navigate to another column.
// Here column at index 6
assertThat(tableOrRequest).column(2).column(6)...
// It is possible to combine the calls to navigate to the next column
// after the column at index 2. Here column at index 3
assertThat(tableOrRequest).column(2).column()...
// It is possible to combine the calls with other navigation methods
// Here first column
assertThat(tableOrRequest).row(2).column()...
// Here column at index 3
assertThat(tableOrRequest).row(2).column(3)...
// Here column at index 4 because the origin remember last navigation to a column
assertThat(tableOrRequest).column(3).row(2).column()...

The column(String columnName) method with columnName as parameter allows to navigate to the column corresponding to the column with the column name.

// Navigate to the column with the name "SURNAME"
assertThat(tableOrRequest).column("surname")...
// Like for the other methods, it is possible to chain the calls
assertThat(tableOrRequest).column("surname").column().column(6).column("id")...

This picture shows from where it is possible to navigate to a column.

The origin point of the column(…​) methods is the Table or the Request. So if the method is executed from a row, from a column or from a value it is like if the method was executed from the Table or The Request.

When the position is on a column, it is possible to return to the origin.

// Return to the table from a column of a table
assertThat(table).column().returnToTable()...
// Return to the request from a column of a request
assertThat(request).column().returnToRequest()...

That also means that the two navigations below are equivalent.

// Navigate to the first column
// Return to the table from this column
// Navigate to the next column
assertThat(table).column().returnToTable().column()...
// The same thing is done but the return to the table is implicit
assertThat(table).column().column()...
To a Value

These methods are described in the ToValue and the ToValueFromRow interfaces.

The value() method allows to navigate to the next value after the value reached on the last call.

// If it is the first call, navigate to the first value
assertThat(tableOrRequest).row().value()...
// It is possible to chain the calls to navigate to the next value
// after the first value (so the second value)
assertThat(tableOrRequest).column().value().value()...

The value(int index) method with index as parameter allows to navigate to the value corresponding to value at the index.

// Navigate to the value at index 2
assertThat(tableOrRequest).column().value(2)...
// It is possible to chain the calls to navigate to another value.
// Here value at index 6
assertThat(tableOrRequest).row(4).value(2).value(6)...
// It is possible to combine the calls to navigate to the next value
// after the value at index 2. Here value at index 3
assertThat(tableOrRequest).column(4).value(2).value()...
// Here value at index 4 because the origin remember last navigation to a column
assertThat(tableOrRequest).column().value(3).row(2).column(0).value()...

The value(String columnName) method with columnName as parameter (only available from a row) allows to navigate to the value of the column corresponding to the column with the column name.

// Navigate to the value of the column with the name "SURNAME"
assertThat(tableOrRequest).row().value("surname")...
// Like for the other methods, it is possible to chain the calls
assertThat(tableOrRequest).row().value("surname").value().value(6).value("id")...

This picture shows from where it is possible to navigate to a value.

The origin point of the value(…​) methods is the Row or the Column. So if the method is executed from a value it is like if the method was executed from the Row or The Column.

When the position is on a value, it is possible to return to the origin.

// Return to the column from a value
assertThat(table).column().value().returnToColumn()...
// Return to the row from a value
assertThat(request).row().value().returnToRow()...

That also means that the two navigations below are equivalent.

// Navigate to the first column
// Navigate to the first value
// Return to the column from this value
// Navigate to the next value
assertThat(table).column().value().returnToColumn().value()...
// The same thing is done but the return to the column is implicit
assertThat(table).column().value().value()...
With Changes as root
To Changes

These methods are described in the ToChanges interface.

The ofCreation() method allows to navigate to the changes of creation.

// Navigate to the changes of creation
assertThat(changes).ofCreation()...

The ofCreationOnTable() method with tableName as parameter allows to navigate to the changes of creation of a table.

// Navigate to the changes of creation on the "members" table
assertThat(changes).ofCreationOnTable("members")...

The ofCreation() method allows to navigate to the changes of modification.

// Navigate to the changes of modification
assertThat(changes).ofModification()...

The ofModificationOnTable() method with tableName as parameter allows to navigate to the changes of modification of a table.

// Navigate to the changes of modification on the "members" table
assertThat(changes).ofModificationOnTable("members")...

The ofCreation() method allows to navigate to the changes of deletion.

// Navigate to the changes of deletion
assertThat(changes).ofDeletion()...

The ofDeletionOnTable() method with tableName as parameter allows to navigate to the changes of deletion of a table.

// Navigate to the changes of deletion on the "members" table
assertThat(changes).ofDeletionOnTable("members")...

The onTable(String tableName) method with tableName as parameter allows to navigate to the changes of a table.

// Navigate to all the changes on the "members" table
assertThat(changes).onTable("members")...

The ofAll() method allows to navigate to all the changes.

// Navigate to all the changes
assertThat(changes).ofAll()...
// The navigation can be chained
assertThat(changes).ofCreation().ofAll()...

This picture shows from where it is possible to navigate to changes.

The origin point of these methods is the Changes. So if the method is executed from a change, a column, a row or a value it is like if the method was executed from the Changes.

To a Change

These methods are described in the ToChange interface.

The change() method allows to navigate to the next change after the change reached on the last call.

// If it is the first call, navigate to the first change
assertThat(changes).change()...
// It is possible to chain the calls to navigate to the next change
// after the first change (so the second change)
assertThat(changes).change().change()...

The change(int index) method with index as parameter allows to navigate to the change corresponding to change at the index.

// Navigate to the change at index 2
assertThat(changes).change().change(2)...
// It is possible to chain the calls to navigate to another change.
// Here change at index 7
assertThat(changes).change(6).change()...

The changeOnTable(String tableName) method with tableName as parameter allows to navigate to the next change corresponding to the table name after the change corresponding to the table name reached on the last call.

// If it is the first call, navigate to the first change on "members" table
assertThat(changes).changeOnTable("members")...
// It is possible to chain the calls to navigate to the next change on the "members" table
// after the first change on the "members" table (so the second change)
assertThat(changes).changeOnTable("members").changeOnTable("members")...

The changeOnTable(String tableName, int index) method with tableName and index as parameters allows to navigate to the change corresponding to change on the table name at the index.

// Navigate to the change at index 2 of "members" table
assertThat(changes).changeOnTable("members").changeOnTable("members", 2)...
// It is possible to chain the calls to navigate to another change.
// Here change at index 7 of "members" table
assertThat(changes).changeOnTable("members", 6).changeOnTable("members")...

There are 12 other methods which are derived from the 4 methods above :

changeOfCreation(), changeOfModification() and changeOfDeletion() methods which allows to navigate to the next change of creation, modification and deletion like change() method

// If it is the first call, navigate to the first change of creation
assertThat(changes).changeOfCreation()...
// Navigate to the first change of creation
// and after the second change of creation
assertThat(changes).changeOfCreation().changeOfCreation()...

changeOfCreation(int index), changeOfModification(int index) and changeOfDeletion(int index) methods with index as parameter which allows to navigate to the change of creation, modification and deletion corresponding to change of creation, modification and deletion at the index like change(int index) method

// Navigate to the change of modification at index 2
assertThat(changes).changeOfModification()
                   .changeOfModification(2)...
// It is possible to chain the calls
// to navigate to another change of modification.
// Here change of modification at index 5
assertThat(changes).changeOfModification(4)
                   .changeOfModification()...

changeOfCreationOnTable(String tableName), changeOfModificationOnTable(String tableName) and changeOfDeletionOnTable(String tableName) methods with tableName as parameter which allows to navigate to the next change of creation, modification and deletion corresponding to the table name like changeOnTable(String tableName) method

// If it is the first call, navigate
// to the first change of creation on "members" table
assertThat(changes).changeOfCreationOnTable("members")...
// It is possible to chain the calls to navigate
// to the next change of creation on the "members" table
// after the first change of creation on the "members" table
// (so the second change of creation)
assertThat(changes).changeOfCreationOnTable("members")
                   .changeOfCreationOnTable("members")...

changeOfCreationOnTable(String tableName, int index), changeOfModificationOnTable(String tableName, int index) and changeOfDeletionOnTable(String tableName, int index) methods with tableName and index as parameters which allows to navigate to the next change of creation, modification and deletion corresponding to the table name and index like changeOnTable(String tableName, int index) method

// Navigate to the change of deletion at index 2 of "members" table
assertThat(changes).changeOfDeletionOnTable("members")
                   .changeOfDeletionOnTable("members", 2)...
// It is possible to chain the calls
// to navigate to another change of deletion.
// Here change of deletion at index 7 of "members" table
assertThat(changes).changeOfDeletionOnTable("members", 6)
                   .changeOfDeletionOnTable("members")...

The changeOnTableWithPks(String tableName, Object…​ pksValues) method allows to navigate to the change corresponding to the table and the primary keys.

// Navigate to the change with primary key 1 of "members" table
assertThat(changes).changeOnTableWithPks("members", 1)...
// It is possible to chain the calls to navigate to the next change
// after the change with primary key 1 of "members" table
assertThat(changes).changeOnTableWithPks("members", 1).change()...

This picture shows from where it is possible to navigate to a change.

The origin point of the change(…​) methods is the current Changes and the origin point of other methods is the Changes of origin. So if the method is executed from a change, a column, a row or a value it is like if the method was executed from these origins.

That means there is an important difference.

// Navigate to the changes of deletion
// Navigate to the first change of this changes of deletion
assertThat(changes).ofDeletion().change()...
// Navigate to the changes of deletion
// Navigate to the first change of this changes of creation
assertThat(changes).ofDeletion().changeOfCreation()...
// This is equivalent to
assertThat(changes).ofDeletion().ofAll().changeOfCreation()...

When the position is on a change, it is possible to return to the origin.

// Return to the change from a column
assertThat(changes).change().returnToChanges()...

That also means that the two navigations below are equivalent.

// Navigate to the first change
// Return to the changes
// Navigate to the next change
assertThat(changes).change().returnToChanges().change()...
// The same thing is done but the return to the changes is implicit
assertThat(changes).change().change()...
To a Row

These methods are described in the ToRowFromChange interface.

The rowAtStartPoint() and rowAtEndPoint() methods allows to navigate to the row at the start point and at the end point.

// Navigate to the row at the start point
assertThat(changes).change().rowAtStartPoint()...
// Navigate to the row at the end point (note that the methods can be chained)
assertThat(changes).change().rowAtStartPoint().rowAtEndPoint()...

This picture shows from where it is possible to navigate to a row.

The origin point of the rowAtStartPoint() and rowAtEndPoint() methods is the Change. So if the method is executed from a row, from a column or from a value it is like if the method was executed from the Change.

When the position is on a row, it is possible to return to the origin.

// Return to the change from a row
assertThat(changes).change().rowAtStartPoint().returnToChange()...

That also means that the two navigations below are equivalent.

// Navigate to the first change
// Navigate to the row at start point
// Return to the change from this column
// Navigate to the row at end point
assertThat(changes).change().rowAtStartPoint().returnToChange().rowAtEndPoint()...
// The same thing is done but the return to the change is implicit
assertThat(changes).change().rowAtStartPoint().rowAtEndPoint()...
To a Column

These methods are described in the ToColumn and ToColumnFromChange interfaces.

The column() method allows to navigate to the next column after the column reached on the last call.

// If it is the first call, navigate to the first column
assertThat(changes).change().column()...
// It is possible to chain the calls to navigate to the next column
// after the first column (so the second column)
assertThat(changes).change().column().column()...

The column(int index) method with index as parameter allows to navigate to the column corresponding to column at the index.

// Navigate to the column at index 2
assertThat(changes).change().column(2)...
// It is possible to chain the calls to navigate to another column.
// Here column at index 6
assertThat(changes).change().column(2).column(6)...
// It is possible to combine the calls to navigate to the next column
// after the column at index 2. Here column at index 3
assertThat(changes).change().column(2).column()...
// It is possible to combine the calls with other navigation methods
// Here first column
assertThat(changes).change().rowAtStartPoint().column()...
// Here column at index 3
assertThat(changes).change().rowAtEndPoint().column(3)...
// Here column at index 4 because the origin remember last navigation to a column
assertThat(changes).change().column(3).rowAtEndPoint().column()...

The column(String columnName) method with columnName as parameter allows to navigate to the column corresponding to the column with the column name.

// Navigate to the column with the name "SURNAME"
assertThat(changes).change().column("surname")...
// Like for the other methods, it is possible to chain the calls
assertThat(changes).change().column("surname").column().column(6).column("id")...

The columnAmongTheModifiedOnes() method allows to navigate to the next column with modifications after the column reached on the last call.

// If it is the first call, navigate to the first column with modifications
assertThat(changes).change().columnAmongTheModifiedOnes()...
// It is possible to chain the calls to navigate to the next column
// after the first column (so the second column with modifications)
assertThat(changes).change().columnAmongTheModifiedOnes()
                            .columnAmongTheModifiedOnes()...

The columnAmongTheModifiedOnes(int index) method with index as parameter allows to navigate to the column with modifications corresponding to column at the index.

// Navigate to the column at index 2 (the third column with modifications)
assertThat(changes).change().columnAmongTheModifiedOnes(2)...
// It is possible to chain the calls to navigate to another column.
// Here column at index 0 (the first column with modifications)
assertThat(changes).change().columnAmongTheModifiedOnes(2)
                            .columnAmongTheModifiedOnes(0)...

The columnAmongTheModifiedOnes(String columnName) method with columnName as parameter allows to navigate to the column with modifications corresponding to the column with the column name.

// Navigate to the column with modifications and the name "SURNAME"
assertThat(changes).change().columnAmongTheModifiedOnes("surname")...
// Like for the other methods, it is possible to chain the calls
assertThat(changes).change().column("surname").columnAmongTheModifiedOnes()
                            .column(6).columnAmongTheModifiedOnes("id")...

This picture shows from where it is possible to navigate to a column.

The origin point of the column(…​) methods is the Change. So if the method is executed from a row, from a column or from a value it is like if the method was executed from the Change.

When the position is on a column, it is possible to return to the origin.

// Return to the change from a column
assertThat(changes).change().column().returnToChange()...

That also means that the two navigations below are equivalent.

// Navigate to the first change
// Navigate to the first column
// Return to the change from this column
// Navigate to the next column
assertThat(changes).change().column().returnToChange().column()...
// The same thing is done but the return to the change is implicit
assertThat(changes).change().column().column()...
To a Value

These methods are described in the ToValue, ToValueFromColumn and ToValueFromRow interfaces.

This picture shows from where it is possible to navigate to a value.

The value() method (only available from a row) allows to navigate to the next value after the value reached on the last call.

// If it is the first call, navigate to the first value
assertThat(changes).change().rowAtEndPoint().value()...
// It is possible to chain the calls to navigate to the next value
// after the first value (so the second value)
assertThat(changes).change().rowAtEndPoint().value().value()...

The value(int index) method with index as parameter (only available from a row) allows to navigate to the value corresponding to value at the index.

// Navigate to the value at index 2
assertThat(changes).change().rowAtEndPoint().value(2)...
// It is possible to chain the calls to navigate to another value.
// Here value at index 6
assertThat(changes).change().rowAtEndPoint().value(2).value(6)...
// It is possible to combine the calls to navigate to the next value
// after the value at index 2. Here value at index 3
assertThat(changes).change().rowAtEndPoint().value(2).value()...
// Here value at index 4 because the origin remember last navigation to the row
assertThat(changes).change().rowAtEndPoint().value(3).column(2).rowAtEndPoint().value()...

The value(String columnName) method with columnName as parameter (only available from a row) allows to navigate to the value of the column corresponding to the column with the column name.

// Navigate to the value of the column with the name "SURNAME"
assertThat(changes).change().rowAtEndPoint().value("surname")...
// Like for the other methods, it is possible to chain the calls
assertThat(changes).change().rowAtEndPoint().value("surname").value().value(6).value("id")...

The valueAtStartPoint() and valueAtEndPoint() methods (only available from a column) allows to navigate to the value at the start point and at the end point.

// Navigate to the value at the start point of the row
assertThat(changes).change().column().valueAtStartPoint()...
// Navigate to the value at the end point of the row (note that the methods can be chained)
assertThat(changes).change().column().valueAtStartPoint().valueAtEndPoint()...

This picture shows from where it is possible to navigate to a value.

The origin point of the value(…​) methods is the Row or the Column. So if the method is executed from a value it is like if the method was executed from the Row or The Column.

When the position is on a value, it is possible to return to the origin.

// Return to the column from a value
assertThat(changes).change().column().valueAtEndPoint().returnToColumn()...
// Return to the row from a value
assertThat(changes).change().rowAtEndPoint().value().returnToRow()...

That also means that the two navigations below are equivalent.

// Navigate to the first change
// Navigate to the row at end point
// Navigate to the first value
// Return to the column from this value
// Navigate to the next value
assertThat(changes).change().rowAtEndPoint().value().returnToRow().value()...
// The same thing is done but the return to the row is implicit
assertThat(changes).change().rowAtEndPoint().value().value()...
6.3.2. Assertions
On the type of change

These assertions are described in the AssertOnChangeType interface.

These assertions allow to verify the type of a change (the concept of change of type is described here).

// Verify that the first change is a change of creation
assertThat(changes).change().isOfType(ChangeType.CREATION);

There are specific assertion methods for each type of change. For example, the assertion below is equivalent to the one above

assertThat(changes).change().isCreation();
On the equality with the values of a column

These assertions are described in the AssertOnColumnEquality and the AssertOnColumnOfChangeEquality interfaces.

These assertion allow to verify the values of a column (the column of a table, of a request or of a change).

With Boolean
// Verify that the values of the column "live" of the request
// was equal to true, to false and after to true
assertThat(request).column("live").hasValues(true, false, true);
// Verify that the value of the first column of the first change
// was false at start point and is true at end point
assertThat(changes).change().column().hasValues(false, true);
// Verify that the value of the third column of the first change
// is not modified and is true
assertThat(changes).change().column(2).hasValues(true);
With Bytes
// Get bytes from a file and from a resource in the classpath
byte[] bytesFromFile = Assertions.bytesContentOf(file);
byte[] bytesFromClassPath = Assertions.bytesContentFromClassPathOf(resource);
// Verify that the values of the second column of the request
// was equal to the bytes from the file, to null and to bytes from the resource
assertThat(request).column(1).hasValues(bytesFromFile, null, bytesFromClassPath);
// Verify that the value of the first column of the first change
// was equal to bytes from the file at start point and to bytes from the resource at end point
assertThat(changes).change().column().hasValues(bytesFromFile, bytesFromClassPath);
With Number
// Verify that the values of the first column of the table
// was equal to 5.9, 4 and 15000
assertThat(table).column().hasValues(5.9, 4, new BigInteger("15000"));
// Verify that the value of the first column of the first change
// is not modified and is equal to 5
assertThat(changes).change().column().hasValues(5);
With Date
// Verify that the values of the first column of the table
// was equal to December 23rd 2007 and May 19th 1975
assertThat(table).column()
            .hasValues(LocalDate.of(2007, 12, 23),
                       LocalDate.of(1975, 5, 19));
// Verify that the value of the first column of the first change
// was equal December 23rd 2007 at start point
// and is equal to May 19th 1975 at end point
assertThat(changes).change().column()
            .hasValues(LocalDate.parse("2007-12-23"),
                       LocalDate.parse("1975-05-19"));
With Time
// Verify that the values of the first column of the table
// was equal to 09:01am and 05:30:50pm
assertThat(table).column()
            .hasValues(LocalTime.of(9, 1),
                       LocalTime.of(17, 30, 50));
// Verify that the value of the first column of the first change
// was equal to 09:01am at start point
// and is equal to 05:30:50pm at end point
assertThat(changes).change().column()
            .hasValues(LocalTime.parse("09:01"),
                       LocalTime.parse("17:30:50"));
With Date/Time
// Verify that the values of the first column of the table
// was equal to December 23rd 2007 09:01am and May 19th 1975
assertThat(table).column()
            .hasValues(LocalDateTime.of(LocalDate.of(2007, 12, 23),
                                        LocalTime.parse("09:01")),
                       LocalDateTime.of(LocalDate.of(1975, 5, 19),
                                        LocalTime.MIDNIGHT));
// Verify that the value of the first column of the first change
// was equal December 23rd 2007 09:01am at start point
// and is equal to May 19th 1975 at end point
assertThat(changes).change().column()
            .hasValues(LocalDateTime.parse("2007-12-23T09:01"),
                       LocalDateTime.parse("1975-05-19T00:00"));
With String
// Verify that values are equal to texts
assertThat(table).column("name")
            .hasValues("Hewson",
                       "Evans",
                       "Clayton",
                       "Mullen");
// Verify that the value of the column "size" of the first change of modification
// is not modified and is equal to 1.75 by parsing
assertThat(changes).changeOfModification().column("size")
            .hasValues("1.75");
// Verify that values are equal to dates, times or dates/times by parsing
assertThat(table).column()
            .hasValues("2007-12-23T09:01"),
                       "1975-05-19");
With UUID

Since 1.1.0

// Verify that the values of the first column of the table
// was equal to 30B443AE-C0C9-4790-9BEC-CE1380808435, 0E2A1269-EFF0-4233-B87B-B53E8B6F164D
// and 2B0D1BDD-909E-4362-BA10-C930BA82718D
assertThat(table).column().hasValues(UUID.fromString("30B443AE-C0C9-4790-9BEC-CE1380808435"),
                                     UUID.fromString("0E2A1269-EFF0-4233-B87B-B53E8B6F164D"),
                                     UUID.fromString("2B0D1BDD-909E-4362-BA10-C930BA82718D"));
// Verify that the value of the first column of the first change
// is not modified and is equal to 399FFFCA-7874-4225-9903-E227C4E9DCC1
assertThat(changes).change()
                   .column().hasValues(UUID.fromString("399FFFCA-7874-4225-9903-E227C4E9DCC1"));
With Character

Since 1.2.0

// Verify that the values of the first column of the table
// was equal to 'T', 'e', 's' and 't'
assertThat(table).column().hasValues('T', 'e', 's', 't');
// Verify that the value of the first column of the first change
// is not modified and is equal to 'T'
assertThat(changes).change().column().hasValues('T');
On the name of a column

This assertion is described in the AssertOnColumnName interface.

This assertion allows to verify the name of a column (the column of a table, of a request or of a change).

// Verify that the fifth column of the table is called "firstname"
assertThat(table).column(4).hasColumnName("firstname");
// Verify that the third value of the second row of the request is in a column called "name"
assertThat(request).row(1).value(2).hasColumnName("name");
// Verify that the first column of the first change is called "id"
assertThat(changes).change().column().hasColumnName("id");
On the nullity of the values of a column

These assertions are described in the AssertOnColumnNullity interface.

These assertion allows to verify the nullity of the values of a column (the column of a table or of a request).

// Verify that the fifth column of the table has only null values
assertThat(table).column(4).hasOnlyNullValues();
// Verify that the column "name" has only not null values
assertThat(request).column("name").hasOnlyNotNullValues();
On the nullity of the values of a row

Since 1.2.0

These assertions are described in the AssertOnRowNullity interface.

These assertion allows to verify the nullity of the values of a row (the row of a table or of a request).

// Verify that the fifth row of the table has only not null values
assertThat(table).row(4).hasOnlyNotNullValues();
// Verify that the first column has only not null values
assertThat(request).row().hasOnlyNotNullValues();
On the type of column

These assertions are described in the AssertOnColumnType interface.

These assertions allow to verify the type of the values of a column (a column from a table, from a request or from a change).

// Verify that the values of the column called "firstname"
// of the table are a text (null values are considered as wrong)
assertThat(table).column("firstname").isOfType(ValueType.TEXT, false);
// The same verification (with the specific method)
// on the third column of the request
assertThat(request).column(2).isText(false);
// Now the same verification again but with a lenience with null values
// (the null values are not considered as wrong)
assertThat(request).column(2).isText(true);
// Verify that the values of the first column
// of the first change is either a date or a number
assertThat(changes).change().column()
    .isOfAnyOfTypes(ValueType.DATE, ValueType.NUMBER);
On the class of column

Since 1.1.0

This assertion is described in the AssertOnColumnClass interface.

This assertion allows to verify the class of the values of a column (a column from a table, from a request or from a change).

// Verify that the values of the column called "firstname"
// of the table are a String (null values are considered as wrong)
assertThat(table).column("firstname").isOfClass(String.class, false);
// Verify that the values of the first column
// of the first change is a Locale (null values are considered as right)
assertThat(changes).change().column().isOfClass(Locale.class, true);
On the content of column

Since 1.1.0

These assertions are described in the AssertOnColumnContent interface.

These assertions allow to verify the content of a column (a column from a table or from a request).

// Verify that the content of the column called "name"
assertThat(table).column("name").containsValues("Hewson",
                                                "Evans",
                                                "Clayton",
                                                "Mullen");
// This second assertion is equivalent because the order of the values is not important
assertThat(table).column("name").containsValues("Evans",
                                                "Clayton",
                                                "Hewson",
                                                "Mullen");
On the type of data

These assertions are described in the AssertOnDataType interface.

These assertions allow to verify the type of the date on which is a change.

// Verify that the change is on a table
assertThat(changes).change().isOnDataType(DataType.TABLE);
// The same verification (with the specific method)
assertThat(changes).change().isOnTable();
// Verify that the change is on the "members" table
assertThat(changes).change().isOnTable("members");
On the modified columns in a change

These assertions are described in the AssertOnModifiedColumn and the AssertOnModifiedColumns interfaces.

These assertions allow to verify if a column of a change have been modified between the start point and the end point (see the concept of changes).

// Verify that first column of the change is not modified
// and the second column is modified
assertThat(changes).change().column().isNotModified().column().isModified();
// Verify that there are 2 modified columns in the change
assertThat(changes).change().hasNumberOfModifiedColumns(2);
// Verify that the modified column in change are at index 1 and 2
assertThat(changes).change().hasModifiedColumns(1, 2);
// Verify that the modified column in change are "name" and "firstname"
assertThat(changes).change().hasModifiedColumns("name", "firstname");

Since version 1.1.0, there are new assertions which allow to compare the number of modified columns between the start point and the end point.

// Verify that the number of modified columns in the first change is more than 5
assertThat(changes).change().hasNumberOfModifiedColumnsGreaterThan(5);
// Verify that the number of modified columns in the first change is at least 5
assertThat(changes).change().hasNumberOfModifiedColumnsGreaterThanOrEqualTo(5);
// Verify that the number of modified columns in the first change is less than 6
assertThat(changes).change().hasNumberOfModifiedColumnsLessThan(6);
// Verify that the number of modified columns in the first change is at most 6
assertThat(changes).change().hasNumberOfModifiedColumnsLessThanOrEqualTo(6);
On the number of changes

This assertion is described in the AssertOnNumberOfChanges interface.

This assertion allows to verify the number of changes.

// Verify that there are 4 changes
assertThat(changes).hasNumberOfChanges(4);

Since version 1.1.0, there are new assertions which allow to compare the number of changes between the start point and the end point.

// Verify that the number of changes is more than 5
assertThat(changes).hasNumberOfChangesGreaterThan(5);
// Verify that the number of changes is at least 5
assertThat(changes).hasNumberOfChangesGreaterThanOrEqualTo(5);
// Verify that the number of changes is less than 6
assertThat(changes).hasNumberOfChangesLessThan(6);
// Verify that the number of changes is at most 6
assertThat(changes).hasNumberOfChangesLessThanOrEqualTo(6);
On the number of columns

This assertion is described in the AssertOnNumberOfColumns interface.

This assertion allows to verify the number of columns (columns from a table, from a request or from a change).

// Verify that there are 6 columns in the table
assertThat(table).hasNumberOfColumns(6);
// Verify that there are 4 columns in the change
assertThat(changes).change().hasNumberOfColumns(4);

Since version 1.1.0, there are new assertions which allow to compare the number of columns.

// Verify that the number of columns is more than 5
assertThat(table).hasNumberOfColumnsGreaterThan(5);
// Verify that the number of columns is at least 5
assertThat(request).hasNumberOfColumnsGreaterThanOrEqualTo(5);
// Verify that the number of columns is less than 6
assertThat(changes).hasNumberOfColumnsLessThan(6);
// Verify that the number of columns is at most 6
assertThat(changes).hasNumberOfColumnsLessThanOrEqualTo(6);
On the number of rows

This assertion is described in the AssertOnNumberOfRows interface.

This assertion allows to verify the number of rows (rows from a table or from a request).

// Verify that there are 7 rows in the table
assertThat(table).hasNumberOfRows(7);

Since version 1.1.0, there are new assertions which allow to compare the number of rows.

// Verify that the number of rows is more than 5
assertThat(table).hasNumberOfRowsGreaterThan(5);
// Verify that the number of rows is at least 5
assertThat(request).hasNumberOfRowsGreaterThanOrEqualTo(5);
// Verify that the number of rows is less than 6
assertThat(changes).hasNumberOfRowsLessThan(6);
// Verify that the number of rows is at most 6
assertThat(changes).hasNumberOfRowsLessThanOrEqualTo(6);

Since version 1.2.0, there is a new assertion which allow to verify if rows are empty (equivalent to hasNumberOfRows(0)).

// Verify that the table are empty
assertThat(table).isEmpty();
On the primary keys

These assertions are described in the AssertOnPrimaryKey interface.

These assertions allow to verify the names and the values of the columns which compose the primary keys of the rows from a change.

// Verify that the columns of the primary keys are "id" and "name"
assertThat(changes).change().hasPksNames("id", "name");
// Verify that the values of the primary keys are 1 and "HEWSON"
assertThat(changes).change().hasPksValues(1, "HEWSON");
On the equality with the values of a row

This assertion is described in the AssertOnRowEquality interface.

This assertion allow to verify the values of a row (the row of a table, of a request or of a change).

// Verify the values of the row at index 1
assertThat(table).row(1)
                 .hasValues(2,
                            "Evans",
                            "David Howell",
                            "The Edge",
                            DateValue.of(1961, 8, 8),
                            1.77);
// Verify the values of the row at end point
assertThat(changes).change().rowAtEndPoint()
                            .hasValues(5,
                                       "McGuiness",
                                       "Paul",
                                       null,
                                       "1951-06-17",
                                       null);
On the existence of a row in a change

These assertions are described in the AssertOnRowOfChangeExistence interface.

These assertions allow to verify that the row at start point or at end point of a change exists or not (for a creation, the row do not exist at start point and for a deletion it is the contrary : the row do not exist at end point).

// Verify that row at start point exists
assertThat(changes).change().rowAtStartPoint().exists();
// Verify that the row at end point do not exist
assertThat(changes).change().rowAtEndPoint().doesNotExist();
On the chronology of a value

These assertions are described in the AssertOnValueChronology interface.

These assertions allow to compare a value (the value of a table, of a request or of a change) to a date, a time or a date/time.

// Compare the value with a date
assertThat(table).row(1).value("birthdate")
                        .isAfter(DateValue.of(1950, 8, 8));
// Verify the value is between two dates/times
assertThat(changes).change().column("release").valueAtEndPoint()
                            .isAfterOrEqualTo(DateTimeValue.parse("2014-09-08T23:30"))
                            .isBeforeOrEqualTo(DateTimeValue.parse("2014-09-09T05:30"));
On the comparison with a value

These assertions are described in the AssertOnValueComparison interface.

These assertions allow to compare a value (the value of a table, of a request or of a change) to a number.

// Compare the value with a number
assertThat(table).row(1).value("size")
                        .isGreaterThan(1.5);
// Verify the value is between two numbers
assertThat(changes).change().column("size").valueAtEndPoint()
                            .isGreaterThanOrEqualTo(1.7)
                            .isLessThanOrEqualTo(1.8);
On the closeness of a value

Since 1.1.0

These assertions are described in the AssertOnValueCloseness interface.

These assertions allow to verify if a value (the value of a table, of a request or of a change) is close to another.

// Verify if the value is close to 2 with a tolerance of 0.5
// So the values between 1.5 and 2.5 are right
assertThat(table).row(1).value("size")
                        .isCloseTo(2, 0.5);
// Verify the value is close to 05-10-1960 with a tolerance of two days
assertThat(changes).change().column("birth").valueAtEndPoint()
                            .isCloseTo(DateValue(1960, 5, 10),
                                       DateValue(0, 0, 2));
On the equality with a value

These assertions are described in the AssertOnValueEquality interface.

These assertion allow to verify that a value (the value of a table, of a request or of a change) is equal to another value (in parameter).

With Boolean
// Verify that the value is equal to true
assertThat(table).row(3).value("live").isEqualTo(true);
// Do the same thing with the specific method
assertThat(table).row(3).value("live").isTrue();
With Bytes
// Get bytes from a file
byte[] bytesFromFile = Assertions.bytesContentOf(file);
// Verify that the value at end point of the first column of the first change
// is equal to bytes from the file
assertThat(changes).change().column().valueAtStartPoint().isEqualTo(bytesFromFile);
With Number
// Verify that the first value is equal to 1.77,
// the second is equal to 50 and the last is equal to zero
assertThat(request).column("size").value().isEqualTo(1.77)
                                  .value().isEqualTo(50)
                                  .value().isEqualTo(0).isZero();
With Date
// Verify that values are equal to dates
assertThat(changes).changeOfCreation()
                       .rowAtEndPoint()
                           .value("birthdate")
                               .isEqualTo(LocalDate.of(1951, 6, 17))
                   .changeOfModification()
                       .column("birthdate")
                           .isEqualTo()
                               .isNotEqualTo(LocalDate.parse("1960-05-10"))
                           .valueAtEndPoint()
                               .isEqualTo(LocalDate.of(1960, 5, 10));
With Time
// Verify that the value is equal to a time
assertThat(table).row().value("duration").isEqualTo(LocalTime.of(9, 1));
With Date/Time
// Verify that the value is equal to a date/time
assertThat(request).column().value()
                   .isEqualTo(LocalDateTime.of(2007, 12, 23,9, 1, 0))
                   .isEqualTo(LocalDateTime.parse("2007-12-23T09:01"));
With String
// Verify that the values are equal to numbers, texts and dates
assertThat(table).row().value().isEqualTo("1")
                       .value().isEqualTo("Hewson")
                       .value().isEqualTo("Paul David")
                       .value().isEqualTo("Bono")
                       .value().isEqualTo("1960-05-10")
                       .value().isEqualTo("1.75");
With UUID

Since 1.1.0

// Verify that the values are equal to UUID
assertThat(table).column().value().isEqualTo(UUID.fromString("30B443AE-C0C9-4790-9BEC-CE1380808435"))
                          .value().isEqualTo(UUID.fromString("0E2A1269-EFF0-4233-B87B-B53E8B6F164D"))
                          .value().isEqualTo(UUID.fromString("2B0D1BDD-909E-4362-BA10-C930BA82718D"));
With Character

Since 1.2.0

// Verify that the values are equal to Character
assertThat(table).column().value().isEqualTo('T')
                          .value().isEqualTo('e')
                          .value().isEqualTo('s')
                          .value().isEqualTo('t');
On the non equality with a value

These assertions are described in the AssertOnValueNonEquality interface.

These assertion allow to verify that a value (the value of a table, of a request or of a change) is not equal to another value (in parameter).

With Boolean
// Verify that the values (values "live" in the row at index 3 and index 5)
// are not equal to false
assertThat(table).row(3).value("live").isNotEqualTo(false)
                 .row(5).value("live").isNotEqualTo(false);
With Bytes
// Get bytes from a resource in the classpath
byte[] bytesFromClassPath = Assertions.bytesContentFromClassPathOf(resource);
// Verify that the value at end point of the first column of the first change
// is not equal to bytes from the resource
assertThat(changes).change().column().valueAtStartPoint().isNotEqualTo(bytesFromClassPath);
With Number
// Verify that the first value is not equal to 1.78,
// the second is not equal to 55 and the last is not equal to 15
assertThat(request).column("size").value().isNotEqualTo(1.78)
                                  .value().isNotEqualTo(55)
                                  .value().isNotEqualTo(15);
With Date
// Verify that values are not equal to dates
assertThat(changes).changeOfCreation()
                       .rowAtEndPoint()
                           .value("birthdate")
                               .isNotEqualTo(LocalDate.of(1951, 6, 17))
                   .changeOfModification()
                       .column("birthdate")
                           .valueAtStartPoint()
                               .isNotEqualTo(LocalDate.parse("1960-05-10"))
                           .valueAtEndPoint()
                               .isNotEqualTo(LocalDate.of(1960, 5, 10));
With Time
// Verify that the value is equal to a time
assertThat(table).row().value("duration").isNotEqualTo(LocalTime.of(9, 1));
With Date/Time
// Verify that the value is not equal to a date/time
assertThat(request).column().value()
                   .isNotEqualTo(LocalDateTime.of(2015, 5, 26,22, 46)))
                   .isNotEqualTo(LocalDateTime.parse("2015-05-26T22:46"));
With String
// Verify that the values are not equal to numbers, texts and dates
assertThat(table).row().value().isNotEqualTo("5")
                       .value().isNotEqualTo("McGuiness")
                       .value().isNotEqualTo("Paul")
                       .value("birthdate").isNotEqualTo("1951-06-17");
With UUID

Since 1.1.0

// Verify that the values are not equal to UUID
assertThat(table).column()
                 .value().isNotEqualTo(UUID.fromString("30B443AE-C0C9-4790-9BEC-CE1380808435"))
                 .value().isNotEqualTo(UUID.fromString("0E2A1269-EFF0-4233-B87B-B53E8B6F164D"))
                 .value().isNotEqualTo(UUID.fromString("2B0D1BDD-909E-4362-BA10-C930BA82718D"));
With Character

Since 1.2.0

// Verify that the values are not equal to Character
assertThat(table).column()
                 .value().isNotEqualTo('T')
                 .value().isNotEqualTo('e')
                 .value().isNotEqualTo('s')
                 .value().isNotEqualTo('t');
On the nullity of a value

These assertions are described in the AssertOnValueNullity interface.

These assertions allow to verify if a value (the value of a table, of a request or of a change) is null or not.

// Verify that the value at index 1 is null and the next value is not null
assertThat(table).column().value(1).isNull()
                          .value().isNotNull();
// Verify the value is not null
assertThat(changes).change().rowAtStartPoint().value("live")
                            .isNotNull();
On the type of a value

These assertions are described in the AssertOnValueType interface.

This assertion allows to verify the type of a value (a value from a table, from a request or from changes).

// Verify that the value of the column called "firstname"
// of the fifth row of the table is a text
assertThat(table).row(4).value("firstname").isOfType(ValueType.TEXT);
// The same verification (with the specific method)
// on the third value of the second row of the request
assertThat(request).row(1).value(2).isText();
// Verify that the value at start point of the first column
// of the first change is either a date or a number
assertThat(changes).change().column().valueAtStartPoint()
    .isOfAnyOfTypes(ValueType.DATE, ValueType.NUMBER);
On the class of a value

Since 1.1.0

This assertion is described in the AssertOnValueClass interface.

This assertion allows to verify the class of a value (a value from a table, from a request or from changes).

// Verify that the value of the column called "firstname"
// of the fifth row of the table is a String
assertThat(table).row(4).value("firstname").isOfClass(String.class);
// Verify that the value at start point of the first column
// of the first change is a Locale
assertThat(changes).change().column().valueAtStartPoint()
    .isOfClass(Locale.class);
6.4. Javadoc

Latest Javadoc release: AssertJ DB Javadoc.

6.5. Examples

Some implementations examples are visible at the assertj-db-examples tests. They show what is possible with AssertJ DB Assertions with running code. You can clone the repository and run its tests !

6.6. Mailing list

If you have any questions, please use the AssertJ google group.

6.7. Code and issue tracker

AssertJ-DB is hosted on GitHub: https://github.com/assertj/assertj-db.

Please report bugs or missing features in the AssertJ-DB issue tracker.

6.8. Contributing

Thanks for your interest ! Please check our contributor’s guidelines.

6.9. Release Notes

Latest release notes:

AssertJ DB 3.0.0

AssertJ DB 2.0.2

AssertJ DB 2.0.1

AssertJ DB 2.0.0

AssertJ DB 1.3.0

AssertJ DB 1.2.0

AssertJ DB 1.1.1

AssertJ DB 1.1.0

AssertJ DB 1.0.1

AssertJ DB 1.0.0

6.9.1. AssertJ DB 3.0.0

Release date: 2024-11-20

 Improvements

Fluent construction of AssertJ-DB connection to database

Cacheable database schema metadata

Fluent database element builder ( Table, Request, Changes )

 Breaking changes

Remove classes : Source, SourceWithLetterCase, DataSourceWithLetterCase

Remove public constructor of classes : Table, Request, Changes

 Fixed

issue #117: setStartPoint opens a lot of connections to the db

 Chore

Upgrade GitHub actions

Upgrade to AssertJ Core 3.21.0

6.9.2. AssertJ DB 2.0.2

Release date: 2020-10-17

 Contributors

Thanks to @soezen for his contribution.

 Fixed

issue #107: Fix SoftAssertions on changes

 Chore

Upgrade to AssertJ Core 3.17.2

Upgrade to AssertJ Parent POM 2.2.8

Upgrade to ByteBuddy 1.10.17

6.9.3. AssertJ DB 2.0.1

Release date: 2020-10-07

 Contributors

Thanks to Yosuke Nishikawa ( @sciencesakura ) for his contribution.

 Improvements

Implement isNotEqualTo, isBefore, isBeforeOrEqualTo, isAfter, isAfterOrEqualTo for JSR-310 types

 Fixed

Fix isEqualTo for JSR-310 types

6.9.4. AssertJ DB 2.0.0

Release date: 2020-07-06

 Contributors

Thanks to Yosuke Nishikawa ( @sciencesakura ), Pascal Schumacher and @sullis for their contributions.

 Improvements

Baseline upgrade to Java 8

Upgrade to AssertJ Core 3.16.1

Support JSR-310 types ( LocalDate, LocalTime, LocalDateTime )

Move from CGLIB to Bytebuddy for soft assertions

 Breaking changes

Baseline upgrade to Java 8

Upgrade to AssertJ Core 3.16.1

 Chore

Replace Travis by GitHub actions

Activate SonarCloud analysis

6.9.5. AssertJ DB 1.3.0

Release date: 2019-12-26

 Improvements

issue #58: Implement SoftAssertions

issue #57: Implement condition assertions

issue #12: Implement assertions on table existence

 Fixed

issue #62: Fix close-to when tolerance exceed 60 seconds

6.9.6. AssertJ DB 1.2.0

Release date: 2017-05-08

 Improvements

issue #36: Add order on table (with Order)

issue #41: Add BDDAssertions so you can use then() instead of assertThat() (Pascal Schumacher)

issue #43: Add isEqualTo(Character) and isNotEqualTo(Character) for values. Add hasValues(Character…​) and containsValues(Character…​) for columns. Add hasValues(Character) and hasValues(Character, Character) for columns of changes

issue #45: Add support for testing that a row contains no Null values: hasOnlyNotNullValues() assertion method (fiery-phoenix)

Add isEmpty() assertion method related to number of rows (fiery-phoenix)

 Fixed

issue #39: Add start delimiter and end delimiter for table name and column name (used to generate the request) in Table

issue #49: NullPointerException while asserting no changes

issue #52: Fix about the outputs with column name and value with %

6.9.7. AssertJ DB 1.1.1

Release date: 2016-04-23

 Fixed

issue #37: assertj-db 1.1.0 does not work with java 7

6.9.8. AssertJ DB 1.1.0

Release date: 2016-04-14

 Improvements

Add from(Calendar) and now() methods to DateValue, TimeValue and DateTimeValue

issue #9: Provide a way to view the data of a Table, of a Request or of Changes with Outputs

issue #15: Add support for UUID type columns (Otoniel Isidoro)

Add a isOfClass(Class) assertion method for value and column

issue #18: Add isCloseTo(…​) methods for Number, DateValue, TimeValue and DateTimeValue

issue #19: Add support for BLOBs and CLOBs

issue #22: Add isEqualTo(Object) for values. Add hasValues(Object…​) for columns. Add hasValues(Object) and hasValues(Object, Object) for columns of changes

issue #25: Add containsValues(…​) methods for columns

issue #29: Add hasNumberOfXXXGreaterThan(…​), hasNumberOfXXXLessThan(…​), hasNumberOfXXXGreaterThanOrEqualTo(…​) and hasNumberOfXXXLessThanOrEqualTo(…​) methods for the rows, columns, changes and modified columns

issue #34: Enhance exception message when column does not exist

 Fixed

issue #21: Add possibility to pass a reference containing a null value like parameter to isEqualTo() and isNotEqualTo()

issue #23: Fix support of Numbers (bug when the mapping is a Double instance)

issue #31: Fix detection of primary keys (caused by letter case) in some DBMS

issue #32: Fix SQL requests for DBMS with letter case different from upper case in the name of the DB elements

6.9.9. AssertJ DB 1.0.1

Release date: 2015-08-09

 Fixed

issue #13: AbstractMethodError when creating a Table using a Datasource instead of a Source

6.9.10. AssertJ DB 1.0.0

Release date: 2015-07-12

First AssertJ DB release.

7. AssertJ Swing
7.1. Release Notes
	AssertJ Swing would not exist without its contributors, you can find them all directly on GitHub.

Latest release notes:

AssertJ Swing 3.17.0

Older release notes can be found in the old site: https://joel-costigliola.github.io/assertj/assertj-swing-news.html, this is important to be aware of breaking changes if you are migrating from an old version.

7.1.1. AssertJ Swing 3.17.0

Release date: 2020-09-13

 Contributors

Thanks to all the contributors of this release: diba1013, Stefano Cordio and Edwin Stang.

 Breaking changes

Change of AssertJ Core from 3.11.1 to 3.17.0

 Improvements

Allow exceptions to be thrown for smaller test-code footprint.

 Fixed

Fix: NPE on invoking JFrames with tray within AssertJSwingJUnitTestCase. (Edwin Stang)

8. Appendix
8.1. Dependency Metadata

Artifacts for final releases and milestones are deployed to Maven Central. Snapshot artifacts are not deployed.

8.1.1. AssertJ Core

Group ID: org.assertj

Artifact ID: assertj-core

Version: 3.27.7

8.1.2. AssertJ Guava

Group ID: org.assertj

Artifact ID: assertj-guava

Version: 3.27.7

8.1.3. Bill of Materials (BOM)

The Bill of Materials POM provided under the following Maven coordinates can be used to ease dependency management when referencing multiple of the above artifacts using Maven or Gradle.

Group ID: org.assertj

Artifact ID: assertj-bom

Version: 3.27.7

Version 1.0
Last updated 2026-03-04 13:34:24 UTC
