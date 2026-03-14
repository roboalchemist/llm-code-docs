# Source: https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html

Title: Building a Test Plan Programmatically

URL Source: https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Building a Test Plan Programmatically
===============
[Main content](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#content)

[![Image 1: Logo ASF](https://jmeter.apache.org/images/asf-logo.svg)](https://www.apache.org/)

[![Image 2: Apache JMeter](https://jmeter.apache.org/images/logo.svg)](https://jmeter.apache.org/)

[![Image 3: Current Apache event teaser](https://www.apache.org/events/current-event-234x60.png)](https://www.apache.org/events/current-event.html)

*   About 
    *   [Overview](https://jmeter.apache.org/index.html)
    *   [License](https://www.apache.org/licenses/)

*   Download 
    *   [Download Releases](https://jmeter.apache.org/download_jmeter.cgi)
    *   [Release Notes](https://jmeter.apache.org/changes.html)

*   Documentation 
    *   [Get Started](https://jmeter.apache.org/usermanual/get-started.html)
    *   [User Manual](https://jmeter.apache.org/usermanual/index.html)
    *   [Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
    *   [Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
    *   [Functions Reference](https://jmeter.apache.org/usermanual/functions.html)
    *   [Properties Reference](https://jmeter.apache.org/usermanual/properties_reference.html)
    *   [Change History](https://jmeter.apache.org/changes_history.html)
    *   [Javadocs](https://jmeter.apache.org/api/index.html)
    *   [JMeter Wiki](https://cwiki.apache.org/confluence/display/JMETER/Home)
    *   [FAQ (Wiki)](https://cwiki.apache.org/confluence/display/JMETER/JMeterFAQ)

*   Tutorials 
    *   [Distributed Testing](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
    *   [Recording Tests](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)
    *   [JUnit Sampler](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
    *   [Access Log Sampler](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html)
    *   [Extending JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

*   Community 
    *   [Issue Tracking](https://jmeter.apache.org/issues.html)
    *   [Security](https://jmeter.apache.org/security.html)
    *   [Mailing Lists](https://jmeter.apache.org/mail.html)
    *   [Source Repositories](https://jmeter.apache.org/svnindex.html)
    *   [Building and Contributing](https://jmeter.apache.org/building.html)
    *   [Project info at Apache](https://projects.apache.org/project.html?jmeter)
    *   [Contributors](https://cwiki.apache.org/confluence/display/JMETER/JMeterCommitters)

*   Foundation 
    *   [The Apache Software Foundation (ASF)](https://www.apache.org/)
    *   [Get Involved in the ASF](https://www.apache.org/foundation/getinvolved.html)
    *   [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
    *   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    *   [Thanks](https://www.apache.org/foundation/thanks.html)

*   [Twitter](https://twitter.com/ApacheJMeter "Follow us on Twitter")
*   [github](https://github.com/apache/jmeter "Fork us on github")

*   [< Prev](https://jmeter.apache.org/usermanual/build-jms-topic-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/listeners.html)

Building a Test Plan Programmatically[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#building "Link to here")
========================================================================================================================================

 JMeter 5.6 brings experimental classes and methods to build test plans programmatically, so please feel free to provide your feedback. 

In this section, you will learn how to create a [Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) with JMeter APIs.

The Test Plan is a collection of elements arranged in a tree-like manner. However, in JMeter APIs, the elements do not form a tree. Parent-child relationships are stored in a separate structure: ListedHashTree.

Creating a plan with low-level APIs[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#low_level_api "Link to here")
===========================================================================================================================================

Let us create Test Plan => Thread Group => Debug Sampler plan

ListedHashTree root = new ListedHashTree(); // (1)
TestPlan testPlan = new TestPlan();
ListedHashTree testPlanSubtree = root.add(testPlan); // (2)
TestPlan threadGroup = new ThreadGroup();
threadGroup.setName("Search Order Thread Group");
ListedHashTree threadGroupSubtree = testPlanSubtree.add(threadGroup); // (3)
DebugSampler debugSampler = new DebugSampler();
threadGroupSubtree.add(debugSampler);
*    Firstly, we create the tree at (1)
*    Then we create elements, and add them to the tree in (2)
*    Note how adding element returns the subtree, so we add threadGroup under testPlan in (2)

 Don't confuse ListedHashTree with HashTree. HashTree does not honour element order, so the generated elements might shuffle unexpectedly. 

Generating code from UI[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#generating_code "Link to here")
=================================================================================================================================

To aid with creating code, JMeter implements Copy Code context action, so you could generate code for any element in the plan. It would generate code for the element and its children.

[![Image 4: Copy Code context action](https://jmeter.apache.org/images/screenshots/copy_code/http_sampler_copy_code.png)](https://jmeter.apache.org/images/screenshots/copy_code/http_sampler_copy_code.png)

Copy Code context action

Here's the generated code (Kotlin DSL):

org.apache.jmeter.protocol.http.sampler.HTTPSamplerProxy::class {
    props {
        it[arguments] = org.apache.jmeter.config.Arguments().apply {
            props {
                it[arguments] = listOf(
                    org.apache.jmeter.protocol.http.util.HTTPArgument().apply {
                        props {
                            it[value] = "World"
                            it[metadata] = "="
                            it[useEquals] = true
                            it[argumentName] = "user"
                        }
                    },
                    org.apache.jmeter.protocol.http.util.HTTPArgument().apply {
                        props {
                            it[alwaysEncode] = true
                            it[value] = "test_value"
                            it[metadata] = "="
                            it[useEquals] = true
                            it[argumentName] = "test"
                        }
                    },
                )
                it[name] = "User Defined Variables"
                it[guiClass] = "org.apache.jmeter.protocol.http.gui.HTTPArgumentsPanel"
                it[testClass] = "org.apache.jmeter.config.Arguments"
            }
        }
        it[domain] = "example.com"
        it[path] = "/api/v1/login"
        it[method] = "GET"
        it[followRedirects] = true
        it[useKeepalive] = true
        it[proxy.scheme] = "https"
        it[proxy.host] = "localhost"
        it[proxy.port] = "8080"
        it[proxy.username] = "secret"
        it[proxy.password] = "password1"
        it[name] = "/login"
        it[guiClass] = "org.apache.jmeter.protocol.http.control.gui.HttpTestSampleGui"
    }

    org.apache.jmeter.extractor.RegexExtractor::class {
        props {
            it[guiClass] = "org.apache.jmeter.extractor.gui.RegexExtractorGui"
            it[name] = "extract user id"
            it[referenceName] = "regexVar"
            it[regularExpression] = "hello\\s+?world"
            it[template] = "\$1\$"
        }
    }

    org.apache.jmeter.protocol.http.control.HeaderManager::class {
        props {
            it[headers] = listOf(
                org.apache.jmeter.protocol.http.control.Header().apply {
                    props {
                        it[headerName] = "Accept"
                        it[value] = "text/plain"
                    }
                },
                org.apache.jmeter.protocol.http.control.Header().apply {
                    props {
                        it[headerName] = "User-Agent"
                        it[value] = "JMeter"
                    }
                },
                org.apache.jmeter.protocol.http.control.Header().apply {
                    props {
                        it[headerName] = "X-JMeter-Thread"
                        it[value] = "Thread \${__threadNum}"
                    }
                },
            )
            it[guiClass] = "org.apache.jmeter.protocol.http.gui.HeaderPanel"
            it[name] = "HTTP Header Manager"
        }
    }
}

Creating a plan with Kotlin DSL[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#treebuilder_kotlin_dsl "Link to here")
================================================================================================================================================

JMeter 5.6 introduces Kotlin DSL which might make it easier to create and maintain test plans as the structure of the code would resemble the structure of the generated test plan tree

import org.apache.jmeter.sampler.DebugSampler
import org.apache.jmeter.testelement.TestPlan
import org.apache.jmeter.threads.ThreadGroup
import org.apache.jmeter.treebuilder.dsl.testTree

val root = testTree { // (1)
  TestPlan::class { // (2)
    ThreadGroup::class {
       name = "Search Order Thread Group"
       +DebugSampler::class // (3)
       +DebugSampler() // (4)
    }
  }
}
*    Firstly, we create a TreeBuilder at (1)
*    Then we add elements to the tree in (2), and populate its children 
*    Note how adding element returns the subtree, so we add threadGroup under testPlan in (2)
*    If no children needed, the element can be appended to the tree with a unary plus operator as in (3)
*    By default, JMeter uses no-argument constructors to create elements, however, you can add TestElement instances to the tree as well, see (4)

Extending Kotlin DSL[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#extending_treebuilder_kotlin_dsl "Link to here")
===============================================================================================================================================

As you use the DSL for test plan generation, you might want to factor out the common patterns. For instance, imagine you want factor out Thread Group creation so it always has a Summariser element.

import kotlin.time.Duration.Companion.seconds
import org.apache.jmeter.sampler.DebugSampler
import org.apache.jmeter.testelement.TestPlan
import org.apache.jmeter.threads.ThreadGroup
import org.apache.jmeter.treebuilder.dsl.testTree

fun TreeBuilder.threadGroup( // (1)
    name: String,
    numThreads: Int = 10,
    rampUp: Duration = 3.seconds,
    body: Action<ThreadGroup>
) {
    ThreadGroup::class { // (2)
        this.name = name
        this.numThreads = numThreads
        this.rampUp = rampUp.inWholeSeconds.toInt()
        +Summariser::class
        body(this) // (3)
    }
}

fun buildTree() {
  val root = testTree {
    TestPlan::class {
      threadGroup(name = "Search Order Thread Group", rampUp = 1.seconds) { // (4)
         +DebugSampler::class
      }
    }
  }
*    Firstly, you can factor test element creation logic as an extension function for TreeBuilder as in (1). It uses regular DSL to add an element (see (2)), and then it calls the lambda body in (3) to fill thread group children. 
*    You can use the extension by calling it when you need it in the test plan, see (4)
*   Note how named parameters, and default values keep the code readable

Creating a plan with Java DSL[¶](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#treebuilder_java_dsl "Link to here")
============================================================================================================================================

JMeter 5.6 introduces Java DSL which might make it easier to create and maintain test plans as the structure of the code would resemble the structure of the generated test plan tree

import org.apache.jmeter.sampler.DebugSampler
import org.apache.jmeter.testelement.TestPlan
import org.apache.jmeter.threads.ThreadGroup
import static org.apache.jmeter.treebuilder.dsl.TreeBuilders.testTree

ListedHashTree root = testTree(b -> { // (1)
  b.add(TestPlan.class, tp -> { // (2)
    b.add(ThreadGroup.class, tg -> {
       tg.setName("Search Order Thread Group");
       b.add(DebugSampler.class); // (3)
       b.add(new DebugSampler()); // (4)
    });
  });
});
*    Firstly, we create a TreeBuilder at (1). Note how this builder reference should be used to append all the elements 
*    Then we add elements to the tree in (2), and populate its children. The lambda parameters correspond to the added elements, so you can configure their properties 
*    Note how adding element returns the subtree, so we add threadGroup under testPlan in (2)
*    If no children needed, you could omit the lambda parameter as in (3)
*    By default, JMeter uses no-argument constructors to create elements, however, you can add TestElement instances to the tree as well, see (4)

*   [< Prev](https://jmeter.apache.org/usermanual/build-jms-topic-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/listeners.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
