# Source: https://jmeter.apache.org/usermanual/regular_expressions.html

Title: Apache JMeter
          -
          User's Manual: Regular Expressions

URL Source: https://jmeter.apache.org/usermanual/regular_expressions.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Regular Expressions
===============
[Main content](https://jmeter.apache.org/usermanual/regular_expressions.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/functions.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/hints_and_tips.html)

21. Regular Expressions[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#regex "Link to here")
==============================================================================================================

21.1 Overview[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#overview "Link to here")
-------------------------------------------------------------------------------------------------------

JMeter includes the pattern matching software [Apache Jakarta ORO](http://attic.apache.org/projects/jakarta-oro.html)

 There is some documentation for this on the Jakarta web-site, for example [a summary of the pattern matching characters](http://archimedes.fas.harvard.edu/scrapbook/jakarta-oro-2.0.6/docs/api/org/apache/oro/text/regex/package-summary.html)

There is also documentation on an older incarnation of the product at [OROMatcher User's guide](http://www.savarese.org/oro/docs/OROMatcher/index.html), which might prove useful.

 With JMeter version 5.5 the Regex implementation can be switched from Oro to the JDK based one by setting the JMeter property jmeter.regex.engine to some value different than oro. 

The pattern matching is very similar to the pattern matching in Perl. A full installation of Perl will include plenty of documentation on regular expressions - look for perlrequick, perlretut, perlre and perlreref.

It is worth stressing the difference between "_contains_" and "_matches_", as used on the Response Assertion test element:

 "_contains_"  means that the regular expression matched at least some part of the target, so 'alphabet' "_contains_" 'ph.b.' because the regular expression matches the substring 'phabe'.  "_matches_"  means that the regular expression matched the whole target. So 'alphabet' is "_matched_" by 'al.*t'. 
In this case, it is equivalent to wrapping the regular expression in ^ and $, viz '^al.*t$'.

However, this is not always the case. For example, the regular expression 'alp|.lp.*' is "_contained_" in 'alphabet', but does not "_match_" 'alphabet'.

Why? Because when the pattern matcher finds the sequence 'alp' in 'alphabet', it stops trying any other combinations - and 'alp' is not the same as 'alphabet', as it does not include 'habet'.

 Unlike Perl, there is no need to (i.e. do not) enclose the regular expression in //. 

So how does one use the modifiers ismx etc. if there is no trailing /? The solution is to use _extended regular expressions_, i.e. /abc/i becomes (?i)abc. See also [Placement of modifiers](https://jmeter.apache.org/usermanual/regular_expressions.html#placement) below.

21.2 Examples[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#examples "Link to here")
-------------------------------------------------------------------------------------------------------

### Extract single string

Suppose you want to match the following portion of a web-page: 

name="file" value="readme.txt">

 and you want to extract readme.txt. 

 A suitable regular expression would be: 

name="file" value="(.+?)">

The special characters above are:

( and )these enclose the portion of the match string to be returned.match any character+one or more times?don't be greedy, i.e. stop when first match succeeds
Note: without the ?, the .+ would continue past the first "> until it found the last possible "> - which is probably not what was intended.

Note: although the above expression works, it's more efficient to use the following expression: 

name="file" value="([^"]+)"> where 

[^"] - means match anything except "

 In this case, the matching engine can stop looking as soon as it sees the first ", whereas in the previous case the engine has to check that it has found "> rather than say " >.

### Extract multiple strings

Suppose you want to match the following portion of a web-page: 

name="file.name" value="readme.txt" and you want to extract both file.name and readme.txt. 

 A suitable regular expression would be: 

name="([^"]+)" value="([^"]+)"

 This would create 2 groups, which could be used in the JMeter Regular Expression Extractor template as $1$ and $2$.

The JMeter Regex Extractor saves the values of the groups in additional variables.

For example, assume:

*    Reference Name: MYREF
*    Regex: name="(.+?)" value="(.+?)"
*    Template: $1$$2$

 Do not enclose the regular expression in / /

The following variables would be set:

MYREF file.namereadme.txt MYREF_g0 name="file.name" value="readme.txt"MYREF_g1 file.name MYREF_g2 readme.txt These variables can be referred to later on in the JMeter test plan, as ${MYREF}, ${MYREF_g1} etc. 

21.3 Line mode[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#line_mode "Link to here")
---------------------------------------------------------------------------------------------------------

The pattern matching behaves in various slightly different ways, depending on the setting of the multi-line and single-line modifiers. Note that the single-line and multi-line operators have nothing to do with each other; they can be specified independently.

### Single-line mode

Single-line mode only affects how the '.' meta-character is interpreted.

Default behaviour is that '.' matches any character except newline. In single-line mode, '.' also matches newline.

### Multi-line mode

Multi-line mode only affects how the meta-characters '^' and '$' are interpreted.

Default behaviour is that '^' and '$' only match at the very beginning and end of the string. When Multi-line mode is used, the '^' metacharacter matches at the beginning of every line, and the '$' metacharacter matches at the end of every line.

21.4 Meta characters[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#meta_chars "Link to here")
----------------------------------------------------------------------------------------------------------------

Regular expressions use certain characters as meta characters - these characters have a special meaning to the RE engine. Such characters must be escaped by preceding them with \ (backslash) in order to treat them as ordinary characters. Here is a list of the meta characters and their meaning (please check the ORO documentation if in doubt).

( and )grouping[ and ]character classes{ and }repetition*, + and ?repetition.wild-card character\escape character|alternatives^ and $start and end of string or line

 Please note that ORO does not support the \Q and \E meta-characters. [In other RE engines, these can be used to quote a portion of an RE so that the meta-characters stand for themselves.] You can use function to do the equivalent, see [${__escapeOroRegexpChars(valueToEscape)}](https://jmeter.apache.org/usermanual/functions.html#__escapeOroRegexpChars). 

The following Perl5 extended regular expressions are supported by ORO.

(?#text)An embedded comment causing text to be ignored.(?:regexp) Groups things like "()" but doesn't cause the group match to be saved. (?=regexp) A zero-width positive lookahead assertion. For example, \w+(?=\s) matches a word followed by whitespace, without including whitespace in the MatchResult. (?!regexp) A zero-width negative lookahead assertion. For example foo(?!bar) matches any occurrence of "foo" that isn't followed by "bar". Remember that this is a zero-width assertion, which means that a(?!b)d will match ad because a is followed by a character that is not b (the d) and a d follows the zero-width assertion. (?imsx) One or more embedded pattern-match modifiers. i enables case insensitivity, m enables multiline treatment of the input, s enables single line treatment of the input, and x enables extended whitespace comments. **Note that (?<=regexp) - lookbehind - is not supported.**

21.5 Placement of modifiers[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#placement "Link to here")
----------------------------------------------------------------------------------------------------------------------

Modifiers can be placed anywhere in the regex, and apply from that point onwards. [A bug in ORO means that they cannot be used at the very end of the regex. However they would have no effect there anyway.]

The single-line (?s) and multi-line (?m) modifiers are normally placed at the start of the regex.

The ignore-case modifier (?i) may be usefully applied to just part of a regex, for example:

Match ExAct case or (?i)ArBiTrARY(?-i) case
 would match Match ExAct case or arbitrary case as well as Match ExAct case or ARBitrary case, but not Match exact case or ArBiTrARY case. 

21.6 Testing Regular Expressions[¶](https://jmeter.apache.org/usermanual/regular_expressions.html#testing_expressions "Link to here")
=====================================================================================================================================

Since JMeter 2.4, the listener [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) include a RegExp Tester to test regular expressions directly on sampler response data.

There is a [Website](http://www.regexplanet.com/advanced/java/index.html) to test Java Regular expressions.

Another approach is to use a simple test plan to test the regular expressions. The Java Request sampler can be used to generate a sample, or the HTTP Sampler can be used to load a file. Add a Debug Sampler and a Tree View Listener and changes to the regular expression can be tested quickly, without needing to access any external servers.

*   [< Prev](https://jmeter.apache.org/usermanual/functions.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/hints_and_tips.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/regular_expressions.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/regular_expressions.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/regular_expressions.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
