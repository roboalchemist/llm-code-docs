# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/adding-tags-to-rule.md

# Adding tags to a rule

Most rules have some tags out of the box. Issues inherit the tags of the rules that raised them. With the Administer Quality Profiles permission, you can add tags to the rules. You have the option to apply your own custom tags to rules or use the tags that are built-in to SonarQube.&#x20;

{% hint style="info" %}
End users can manage the tags assigned to issues within their project. They can add tags using either built-in rule tags or their own custom tags, and they can remove inherited tags.&#x20;
{% endhint %}

To add a tag to a rule:

1. In SonarQube, go to **Rules** and retrieve the rule you want to tag.
2. In the **Tags** section of the rule, select the plus sign. The **Edit Tags** dialog opens.

<figure><img src="broken-reference" alt="Select the plus sing in the Tags section."><figcaption></figcaption></figure>

3. In the search field, enter the name of the tag to be added. The list of existing tags is filtered. If the tag doesn't exist, its name is displayed in the search results with a plus sign as illustrated below.&#x20;

<figure><img src="broken-reference" alt="In the search field, enter the name of your custom tag."><figcaption></figcaption></figure>

4. In the search results, select the tag you want to add. The tag is created (if it did not exist) and added to the rule.&#x20;

### Related pages <a href="#built-in-rule-tags" id="built-in-rule-tags"></a>

* [built-in-rule-tags](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/built-in-rule-tags "mention")
* [#tagging](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing#tagging "mention")
