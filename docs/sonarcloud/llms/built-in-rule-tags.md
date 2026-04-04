# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/rules/built-in-rule-tags.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/built-in-rule-tags.md

# Built-in rule tags

Tags are a way to categorize rules and issues. Issues inherit the tags on the rules that raised them. Some tags are language-specific, but many more appear across languages. Users can add tags to rules and issues, but most rules have some tags out of the box. Here is a non-comprehensive list of what some of those built-in tags mean:

{% hint style="info" %}
*Most of the links below to* [*rules.sonarsource.com*](https://rules.sonarsource.com/) *will be initially filtered for Java language rules*
{% endhint %}

* [architecture](https://rules.sonarsource.com/java/tag/architecture): there is something questionable about the architecture of the code.
* [brain-overload](https://rules.sonarsource.com/java/tag/brain-overload) - there is too much to keep in your head at one time
* [bad-practice](https://rules.sonarsource.com/java/tag/bad-practice) - the code likely works as designed, but the way it was designed is widely recognized as being a bad idea.
* [cert](https://rules.sonarsource.com/java/tag/cert) - relates to a rule in a [CERT](https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards) standard. There are currently three CERT standards: [C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard), [C++](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046682), and [Java](https://wiki.sei.cmu.edu/confluence/display/java/SEI+CERT+Oracle+Coding+Standard+for+Java). Many of these rules are not language-specific, but are good programming practices. That’s why you’ll see this tag on non-C/C++, Java rules.
* [clumsy](https://rules.sonarsource.com/java/tag/clumsy) - extra steps are used to accomplish something that could be done more clearly and concisely. (E.G. calling .toString() on a String).
* [confusing](https://rules.sonarsource.com/java/tag/confusing) - will take maintainers longer to understand than is really justified by what the code actually does
* [convention](https://rules.sonarsource.com/java/tag/convention) - coding convention - typically formatting, naming, whitespace…
* [cwe](https://rules.sonarsource.com/java/tag/cwe) - relates to a rule in the [Common Weakness Enumeration](http://cwe.mitre.org/). For more on CWE and on security-related rules in general, see the [security-related-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-related-rules "mention") page.
* [lock-in](https://rules.sonarsource.com/java/tag/lock-in) - environment-specific features are used
* [misra](https://rules.sonarsource.com/cpp/tag/misra-c2012) - relates to a rule in one of the [MISRA](http://www.misra.org.uk/) standards. While the MISRA rules are primarily about C and C++, many of them are not language-specific (E.G. don’t use a float as a loop counter) but are simply good programming practices. That’s why you’ll see these tags on non-C/C++ rules.
* [pitfall](https://rules.sonarsource.com/java/tag/pitfall) - nothing is wrong yet, but something could go wrong in the future; a trap has been set for the next guy and he’ll probably fall into it and screw up the code.
* [suspicious](https://rules.sonarsource.com/java/tag/suspicious) - it’s not guaranteed that this is a **bug**, but it looks suspiciously like one. At the very least, the code should be re-examined & likely refactored for clarity.
* [unpredictable](https://rules.sonarsource.com/java/tag/unpredictable) - the code may work fine under current conditions, but may fail erratically if conditions change.
* [unused](https://rules.sonarsource.com/java/tag/unused) - unused code, E.G. a private variable that is never used.
* [user-experience](https://rules.sonarsource.com/java/tag/user-experience) - there’s nothing technically wrong with your code, but it may make some or all of your users hate you.
