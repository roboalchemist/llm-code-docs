# Source: https://maven.apache.org/guides/introduction/introduction-to-archetypes.html

Title: Introduction to Archetypes – Maven

URL Source: https://maven.apache.org/guides/introduction/introduction-to-archetypes.html

Markdown Content:
[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
What is Archetype?
------------------

In short, Archetype is a Maven project templating toolkit. An archetype is defined as _an original pattern or model from which all other things of the same kind are made_. The name fits as we are trying to provide a system that provides a consistent means of generating Maven projects. Archetype will help authors create Maven project templates for users, and provides users with the means to generate parameterized versions of those project templates.

Using archetypes provides a great way to enable developers work quickly in a way consistent with best practices employed by your project or organization. Within the Maven project, we use archetypes to try and get our users up and running as quickly as possible by providing a sample project that demonstrates many of the features of Maven, while introducing new users to the best practices employed by Maven. In a matter of seconds, a new user can have a working Maven project to use as a jumping board for investigating more of the features in Maven. We have also tried to make the Archetype mechanism additive, and by that we mean allowing portions of a project to be captured in an archetype so that pieces or aspects of a project can be added to existing projects. A good example of this is the Maven site archetype. If, for example, you have used the quick start archetype to generate a working project, you can then quickly create a site for that project by using the site archetype within that existing project. You can do anything like this with archetypes.

You may want to standardize J2EE development within your organization, so you may want to provide archetypes for EJBs, or WARs, or for your web services. Once these archetypes are created and deployed in your organization's repository, they are available for use by all developers within your organization.

[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
Using an Archetype[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html#using-an-archetype)
---------------------------------------------------------------------------------------------------------------------

To create a new project based on an Archetype, you need to call `mvn archetype:generate` goal, like the following:

```
mvn archetype:generate
```

Please refer to [Archetype Plugin page](https://maven.apache.org/archetype/maven-archetype-plugin/).

[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
Provided Archetypes[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html#provided-archetypes)
-----------------------------------------------------------------------------------------------------------------------

Maven provides several Archetype artifacts:

| Archetype ArtifactIds | Description |
| --- | --- |
| maven-archetype-archetype | An archetype to generate a sample archetype project. |
| maven-archetype-j2ee-simple | An archetype to generate a simplifed sample J2EE application. |
| maven-archetype-plugin | An archetype to generate a sample Maven plugin. |
| maven-archetype-plugin-site | An archetype to generate a sample Maven plugin site. |
| maven-archetype-portlet | An archetype to generate a sample JSR-268 Portlet. |
| maven-archetype-quickstart | An archetype to generate a sample Maven project. |
| maven-archetype-simple | An archetype to generate a simple Maven project. |
| maven-archetype-site | An archetype to generate a sample Maven site which demonstrates some of the supported document types like APT, XDoc, and FML and demonstrates how to i18n your site. |
| maven-archetype-site-simple | An archetype to generate a sample Maven site. |
| maven-archetype-webapp | An archetype to generate a sample Maven Webapp project. |

For more information on these archetypes, please refer to the [Maven Archetype Bundles page](https://maven.apache.org/archetypes/index.html).

[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
What makes up an Archetype?[](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html#what-makes-up-an-archetype)
--------------------------------------------------------------------------------------------------------------------------------------

Archetypes are packaged up in a JAR and they consist of the archetype metadata which describes the contents of archetype, and a set of [Velocity](http://velocity.apache.org/) templates which make up the prototype project. If you would like to know how to make your own archetypes, please refer to our [Guide to creating archetypes](https://maven.apache.org/guides/mini/guide-creating-archetypes.html).
