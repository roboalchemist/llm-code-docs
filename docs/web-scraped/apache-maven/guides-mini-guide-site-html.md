# Source: https://maven.apache.org/guides/mini/guide-site.html

Title: Creating a site – Maven

URL Source: https://maven.apache.org/guides/mini/guide-site.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-site.html)[](https://maven.apache.org/guides/mini/guide-site.html)
Creating Content[](https://maven.apache.org/guides/mini/guide-site.html#creating-content)
-----------------------------------------------------------------------------------------

The first step to creating your site is to create some content. In Maven, the site content is separated by format, as there are several available.

```
+- src/
   +- site/
      +- apt/
      |  +- index.apt
      !
      +- markdown/
      |  +- content.md
      |
      +- fml/
      |  +- general.fml
      |  +- faq.fml
      |
      +- xdoc/
      |  +- other.xml
      |
      +- site.xml
```

You will notice there is now a `${project.basedir}/src/site` directory within which is contained a `site.xml` site descriptor along with various directories corresponding to the supported document types.

Let's take a look at the examples of the various document types:

*   `apt`: the APT format, “Almost Plain Text”, is a wiki-like format that allows you to write simple, structured documents (like this one) very quickly. A full reference of the [APT Format](https://maven.apache.org/doxia/references/apt-format.html) is available,
*   `markdown`: the well known [Markdown](https://en.wikipedia.org/wiki/Markdown) format,
*   `fml`: the FML format is the [FAQ format](https://maven.apache.org/doxia/references/fml-format.html),
*   `xdoc`: an XML document conforming to a small and simple set of tags, see the [full reference](https://maven.apache.org/doxia/references/xdoc-format.html).

Other formats are available, but at this point these 4 are the best tested.

There are also several possible output formats, but as of Maven Site Plugin, only XHTML is available.

Note that all of the above is optional - just one index file is required in one of the input trees. Each of the paths will be merged together to form the root directory of the site.

[](https://maven.apache.org/guides/mini/guide-site.html)
Customizing the Look & Feel[](https://maven.apache.org/guides/mini/guide-site.html#customizing-the-look-feel)
-------------------------------------------------------------------------------------------------------------

If you want to tune the way your site looks, you can use a custom **skin** to provide your own CSS styles. If that is still not enough, you can even tweak the output templates that Maven uses to generate the site documentation.

You can visit the [Skins index](https://maven.apache.org/skins/) to have a look at some of the skins that you can use to change the look of your site.

[](https://maven.apache.org/guides/mini/guide-site.html)
Generating the Site[](https://maven.apache.org/guides/mini/guide-site.html#generating-the-site)
-----------------------------------------------------------------------------------------------

Generating the site is very simple, and fast!

```
mvn site
```

By default, the resulting site will be in `target/site/...`

For more information on the Maven Site Plugin, see the [maven-site-plugin reference](https://maven.apache.org/plugins/maven-site-plugin/).

[](https://maven.apache.org/guides/mini/guide-site.html)
Deploying the Site[](https://maven.apache.org/guides/mini/guide-site.html#deploying-the-site)
---------------------------------------------------------------------------------------------

[](https://maven.apache.org/guides/mini/guide-site.html)
### Classical Website deployment[](https://maven.apache.org/guides/mini/guide-site.html#classical-website-deployment)

To be able to deploy the site with a classical network protocol (ftp, scp, webdav), you must first declare a location to distribute to in your `pom.xml`, similar to the repository for deployment:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<distributionManagement>`
4.   `<site>`
5.   `<id>website</id>`
6.   `<url>scp://www.mycompany.com/www/docs/project/</url>`
7.   `</site>`
8.   `</distributionManagement>`
9.   `...`
10.   `</project>`

*   the `<id>` element identifies the repository, so that you can attach credentials to it in your `settings.xml` file using the [`<servers>` element](https://maven.apache.org/settings.html#Servers) as you would for any other repository,
*   the `<url>` gives the location to deploy to. Currently, only SSH is supported by default, as above which copies to the host `www.mycompany.com` in the path `/www/docs/project/`, but you can [add more protocols as required](https://maven.apache.org/plugins/maven-site-plugin/examples/adding-deploy-protocol.html). If subprojects inherit the site URL from a parent POM, they will automatically get their `<artifactId>` appended to form their effective deployment location.

Once distribution location is configured, deploying the site is done by using the `site-deploy` phase of the site lifecycle.

```
mvn site-deploy
```
[](https://maven.apache.org/guides/mini/guide-site.html)
### GitHub Pages, Apache svnpubsub/gitpubsub Deployment[](https://maven.apache.org/guides/mini/guide-site.html#github-pages-apache-svnpubsub-gitpubsub-deployment)

When site publication is done with a SCM commit, like with [GitHub Pages](https://pages.github.com/) or [Apache svnpubsub/gitpubsub](https://infra.apache.org/project-site.html#tools), deploying the site will be done with [Maven SCM Publish Plugin](https://maven.apache.org/plugins/maven-scm-publish-plugin/).

For example with a project hosted on GitHub and using GitHub Pages for its site publication:

1.   `<plugin>`
2.   `<groupId>org.apache.maven.plugins</groupId>`
3.   `<artifactId>maven-scm-publish-plugin</artifactId>`
4.   `<version>3.1.0</version>`
5.   `<configuration>`
6.   `<pubScmUrl>${project.scm.developerConnection}</pubScmUrl>`
7.   `<scmBranch>gh-pages</scmBranch>`
8.   `</configuration>`
9.   `</plugin>`

Deploying the site is done in 2 steps:

1.   staging the content by using the `site` phase of the site lifecycle followed by `site:stage`: `mvn site site:stage`
2.   publishing the staged site to the SCM: `mvn scm-publish:publish-scm`

[](https://maven.apache.org/guides/mini/guide-site.html)
Creating a Site Descriptor[](https://maven.apache.org/guides/mini/guide-site.html#creating-a-site-descriptor)
-------------------------------------------------------------------------------------------------------------

The `site.xml` file is used to describe the structure of the site. A sample is given below:

1.   `<?xml version="1.0" encoding="ISO-8859-1"?>`
2.   `<project xmlns="http://maven.apache.org/DECORATION/1.8.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/DECORATION/1.8.0 https://maven.apache.org/xsd/decoration-1.8.0.xsd"`
4.   `name="Maven">`
5.   `<bannerLeft>`
6.   `<name>Maven</name>`
7.   `<src>https://maven.apache.org/images/apache-maven-project.png</src>`
8.   `<href>https://maven.apache.org/</href>`
9.   `</bannerLeft>`
10.   `<bannerRight>`
11.   `<src>https://maven.apache.org/images/maven-small.gif</src>`
12.   `</bannerRight>`

14.   `<body>`
15.   `<links>`
16.   `<item name="Apache" href="http://www.apache.org/" />`
17.   `<item name="Maven 1.x" href="https://maven.apache.org/maven-1.x/"/>`
18.   `<item name="Maven 2" href="https://maven.apache.org/"/>`
19.   `</links>`

21.   `<menu name="Maven 2.0">`
22.   `<item name="Introduction" href="index.html"/>`
23.   `<item name="Download" href="download.html"/>`
24.   `<item name="Release Notes" href="release-notes.html" />`
25.   `<item name="General Information" href="about.html"/>`
26.   `<item name="For Maven 1.x Users" href="maven1.html"/>`
27.   `<item name="Road Map" href="roadmap.html" />`
28.   `</menu>`

30.   `<menu ref="reports"/>`

32.   `...`
33.   `</body>`
34.   `</project>`

**Note:** The `<menu ref="reports"/>` element above. When building the site, this is replaced by a menu with links to all the reports that you have configured.

More information about the site descriptor is available at the [dedicated page of Maven Site Plugin](https://maven.apache.org/plugins/maven-site-plugin/examples/sitedescriptor.html).

[](https://maven.apache.org/guides/mini/guide-site.html)
You can add any arbitrary resource to your site by including them in a `resources` directory as shown below. Additional CSS files will be picked up when they are placed in the `css` directory within the `resources` directory.

```
+- src/
   +- site/
      +- resources/
         +- css/
         |  +- site.css
         |
         +- images/
            +- pic1.jpg
```

The file `site.css` will be added to the default XHTML output, so it can be used to adjust the default Maven stylesheets if desired.

The file `pic1.jpg` will be available via a relative reference to the `images` directory from any page in your site.

[](https://maven.apache.org/guides/mini/guide-site.html)
Configuring Reports[](https://maven.apache.org/guides/mini/guide-site.html#configuring-reports)
-----------------------------------------------------------------------------------------------

Maven has several reports that you can add to your web site to display the current state of the project. These reports take the form of plugins, just like those used to build the project.

There are many standard reports that are available by gleaning information from the POM. Currently what is provided by default are:

*   Dependencies Report
*   Mailing Lists
*   Continuous Integration
*   Source Repository
*   Issue Tracking
*   Project Team
*   License

To find out more please refer to the [Project Info Reports Plugin](https://maven.apache.org/plugins/maven-project-info-reports-plugin/).

To add these reports to your site, you must add the Project Info Reports plugin to a special `<reporting>` section in the POM. The following example shows how to configure the standard project information reports that display information from the POM in a friendly format:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<reporting>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-project-info-reports-plugin</artifactId>`
8.   `<version>2.8</version><!-- define version here if not already defined in build/plugins or build/pluginManagement -->`
9.   `</plugin>`
10.   `</plugins>`
11.   `</reporting>`
12.   `...`
13.   `</project>`

If you have included the appropriate `<menu ref="reports"/>` tag in your `site.xml` descriptor, then when you regenerate the site those items will appear in the menu.

Many other plugins provide reporting goals: look for “R” (Reporting) value in the “Type” column of the [list of plugins](https://maven.apache.org/plugins/). When plugins are both Build and Reporting plugins, defining explicitly the version in the reporting section is usually not necessary since reporting will use the version from `build/plugins` or `build/pluginManagement`. Since Maven Site Plugin 3.4, reporting plugin also get configuration from `build/pluginManagement`.

**Note:** Many report plugins provide a parameter called `outputDirectory` or similar to specify the destination for their report outputs. This parameter is only relevant if the report plugin is run standalone, i.e. by invocation directly from the command line. In contrast, when reports are generated as part of the site, the configuration of the Maven Site Plugin will determine the effective output directory to ensure that all reports end up in a central location.

[](https://maven.apache.org/guides/mini/guide-site.html)
Internationalization[](https://maven.apache.org/guides/mini/guide-site.html#internationalization)
-------------------------------------------------------------------------------------------------

Internationalization in Maven is very simple, as long as the reports you are using have that particular locale defined. For an overview of supported languages and instructions on how to add further languages, please see the related article [Internationalization](https://maven.apache.org/plugins/maven-site-plugin/i18n.html) from the Maven Site Plugin.

To enable multiple locales, add a configuration similar to the following to your POM:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-site-plugin</artifactId>`
8.   `<version>3.4</version>`
9.   `<configuration>`
10.   `<locales>en,fr</locales>`
11.   `</configuration>`
12.   `</plugin>`
13.   `</plugins>`
14.   `</build>`
15.   `...`
16.   `</project>`

This will generate both an English and a French version of the site. If `en` is your current locale, then it will be generated at the root of the site, with a copy of the French translation of the site in the `fr/` subdirectory.

To add your own content for that translation instead of using the default, place a subdirectory with that locale name in your site directory and create a new site descriptor with the locale in the file name. For example:

```
+- src/
   +- site/
      +- apt/
      |  +- index.apt     (Default version)
      |
      +- fr/
      |  +- apt/
      |     +- index.apt  (French version)
      |
      +- site.xml         (Default site descriptor)
      +- site_fr.xml      (French site descriptor)
```

With one site descriptor per language, the translated site(s) can evolve independently.
