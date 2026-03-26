# Source: https://docs.syncfusion.com/java-file-formats/word-library/installation/configure-to-download-syncfusion-java-packages-from-apache-maven.md

# Source: https://docs.syncfusion.com/java-file-formats/installation/configure-to-download-syncfusion-java-packages-from-apache-maven.md

# Configure to download Syncfusion<sup style="font-size:70%">&reg;</sup> Java packages from Apache Maven

You can easily download the Syncfusion<sup style="font-size:70%">&reg;</sup> packages for Java using the [maven repository](https://jars.syncfusion.com/).

The following command shows how to mention the repository in Apache Maven.

{% tabs %}  

{% highlight XML %}
<repository>
   <id>Syncfusion-Java</id>
   <name>Syncfusion<sup style="font-size:70%">&reg;</sup> Java repo</name>
   <url>https://jars.syncfusion.com/repository/maven-public/</url>
</repository>
{% endhighlight %}

{% endtabs %}

The following command shows how to refer to the Syncfusion<sup style="font-size:70%">&reg;</sup> package, which needs to be used in your project as the dependency.

{% tabs %}  

{% highlight XML %}
<dependency>
   <groupId>com.syncfusion</groupId>
   <artifactId>syncfusion-docio</artifactId>
   <version>18.4.0.30</version>
</dependency>
{% endhighlight %}

{% endtabs %}
