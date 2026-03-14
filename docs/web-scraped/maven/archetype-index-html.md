# Source: https://maven.apache.org/archetype/index.html

Title: About – Maven Archetype

URL Source: https://maven.apache.org/archetype/index.html

Markdown Content:
[](https://maven.apache.org/archetype/index.html)[](https://maven.apache.org/archetype/index.html)
What is Archetype?
------------------

In short, Archetype is a Maven project templating toolkit. An archetype is defined as _an original pattern or model from which all other things of the same kind are made_. The names fits as we are trying to provide a system that provides a consistent means of generating Maven projects. Archetype will help authors create Maven project templates for users, and provides users with the means to generate parameterized versions of those project templates.

Using archetypes provides a great way to enable developers quickly in a way consistent with best practices employed by your project or organization. Within the Maven project we use archetypes to try and get our users up and running as quickly as possible by providing a sample project that demonstrates many of the features of Maven while introducing new users to the best practices employed by Maven. In a matter of seconds a new user can have a working Maven project to use as a jumping board for investigating more of the features in Maven. We have also tried to make the Archetype mechanism additive and by that we mean allowing portions of a project to be captured in an archetype so that pieces or aspects of a project can be added to existing projects. A good example of this is the Maven site archetype. If, for example, you have used the quick start archetype to generate a working project you can then quickly create a site for that project by using the site archetype within that existing project. You can do anything like this with archetypes.

You may want to standardize J2EE development within your organization so you may want to provide archetypes for EJBs, or WARs, or for your web services. Once these archetypes are created and deployed in your organization's repository they are available for use by all developers within your organization.

[](https://maven.apache.org/archetype/index.html)
Using an Archetype
------------------

To create a new project based on an Archetype, you need to call `mvn archetype:generate` goal, like the following:

`mvn archetype:generate`
Please refer to [Archetype Plugin Page](http://maven.apache.org/plugins/maven-archetype-plugin/usage.html) for more details.

[](https://maven.apache.org/archetype/index.html)
Content
-------

Maven Archetype is composed of several modules:

| Module | Description |
| --- | --- |
| **[maven-archetype-plugin](https://maven.apache.org/archetype/maven-archetype-plugin/)** | Archetype Plugin to use archetypes with Maven, |
| [archetype-packaging](https://maven.apache.org/archetype/archetype-packaging/) | Archetype lifecycle and packaging definition, |
| [archetype-models](https://maven.apache.org/archetype/archetype-models/) | Descriptors classes and reference documentation, |
| [archetype-common](https://maven.apache.org/archetype/archetype-common/) | Core classes, |

Some archetypes are also provided by Maven: see [Maven Archetype Bundles](https://maven.apache.org/archetypes/).
