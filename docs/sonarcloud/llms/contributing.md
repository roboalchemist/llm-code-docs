# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/contributing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/contributing.md

# Contributing

Please be aware that we are not actively looking for feature contributions to SonarQube Community Build itself because it’s extremely difficult for someone outside Sonar to comply with our roadmap and expectations. Therefore, we typically only accept minor cosmetic changes and typo fixes for SonarQube Community Build, but we do happily welcome contributions to the other open-source projects under the Sonar umbrella.

### General guidelines <a href="#general-guidelines" id="general-guidelines"></a>

* Choose an open ticket in [JIRA](https://jira.sonarsource.com/secure/Dashboard.jspa) or propose your change on the [SonarQube community forum](https://community.sonarsource.com/); the discussion there is likely to result in the opening of a JIRA ticket. ;-)
* Use the Sonar conventions, which you’ll find neatly packaged here: <https://github.com/SonarSource/sonar-developer-toolset#the-almost-unbreakable-build>.
* Use pull requests to submit your work.

### New rule implementations in existing plugins <a href="#new-rule-implementations-in-existing-plugins" id="new-rule-implementations-in-existing-plugins"></a>

* Start from an existing [RSpec](https://jira.sonarsource.com/browse/RSPEC-1973?filter=10375) (Rule Specification) that lists your language of interest in the **Targeted languages** field.
  * If the RSpec you’re interested in doesn’t target the language where you want to implement it, raise the question on the community forums.
  * If no RSpec exists for the rule you want to implement, raise the question on the [Community forum](https://community.sonarsource.com/).
* Put your rule implementation class in the \[language]-checks (for example: java-checks, or javascript-checks) module, in the checks sub-package.
* The naming convention for implementation classes is `[A-Z][a-za-z]+Check.java`. (Yes, put `Check` in the name too.) The class name should be descriptive and not reflect the rule key. For example, `FindBadCodeCheck.java`, not `S007.java`.
* A good way to get started on a rule implementation is to look at the implementations of rules that do similar things.
* During development, there’s no need to load the plugin in a server to test your implementation, use the rule’s unit test for that.
* For a complete implementation, make sure all of the following are done:
  * create HTML description file and metadata file.
  * write test class.
  * register the rule in `CheckList.java`.
  * add the rule to the profile used for the integration test in `profile.xml`.
  * run the integration test and add any new issues to the set of expected issues.
