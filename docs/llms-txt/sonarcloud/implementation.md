# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/implementation.md

# Implementation

For each project, the Clean as You Code implementation looks like this:

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-a28927121710562efcbc8d5bbccf76c002f3d787%2F307b1bf05e851145edf3e1d6b7aa2e562ab058ed.png?alt=media)

First, you define the quality standard for your project:

* With a *quality profile*, you define the set of rules to be applied during analysis.
* With a quality gate, you define a set of conditions that the code must meet.

Then, you define what is considered *new code* in your project, adapting your configuration to the nature of your project: versioned, continuous delivery, etc.

Finally, you ensure your code is analyzed frequently and at different stages of its journey, in your IDE and your DevOps platforms.

### Practicing Clean as You Code as a developer <a href="#practicing-clean-as-you-code-as-developer" id="practicing-clean-as-you-code-as-developer"></a>

The configuration steps described above and in the following sections are handled by project administrators. As a developer, you practice Clean as You Code by reviewing and fixing the issues detected in new code, ensuring that the quality gate is always green and that only clean code is merged.

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-954e7906845573d58cac5e9ed3982e525725c4d2%2F72ec481f503887ad295114bfe90b6590d6377f52.png?alt=media)

To learn more about these topics, refer to the Issues, Quality gates, and Clean Code sections (see links below).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-clean-as-you-code](https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/setting-up-clean-as-you-code "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/introduction "mention")
* [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/introduction "mention")
