# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-lucene-searchindex-slows-server-performance.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-lucene-searchindex-slows-server-performance.md

# Jackrabbit Lucene SearchIndex slows server performance

The purpose of the Jackrabbit `SearchIndex` tag is to index property values and node names when data is saved or whenever a data transaction is performed. With the Pentaho Platform, Jackrabbit’s Lucene tries to index all of the text from every file in the repository. The `SearchIndex` tag has been disabled for Pentaho 6.1 and higher to improve overall repository performance.

When you upgrade to Pentaho 6.1 or higher and bring your previous `repository.xml` forward to the new version, your server will start and function as it did in your previous version of Pentaho. This Jackrabbit Lucene indexing can cause degradation in repository performance.

If you are bringing forward your `repository.xml`, you will need to disable the `SearchIndex` tag within Jackrabbit. Depending on whether you have a custom-configured repository or a default repository, follow one of these procedures for disabling the `SearchIndex` tag.

{% tabs %}
{% tab title="Custom repository XML file" %}
If you have a custom-configured `repository.xml` file, follow these steps to disable the `SearchIndex` tag:

1. Navigate to the `pentaho-solutions/system/jackrabbit` directory.
2. Open the `repository.xml` file with any text editor.
3. Search for the `SearchIndex` tag.
4. You should find it within two tags: the `<Workspace>` tag and the `<Repository>` tag.
5. In the `<Repository>` tag only, delete or comment out the `SearchIndex` tag. Make sure that you don't change the `SearchIndex` tag within the `<Workspace>` tag.
6. Save and close the `repository.xml` file.

Whenever you make any changes to the Jackrabbit `repository.xml` file, you need to delete the `pentaho-solutions/system/jackrabbit/repository` folder and restart your Pentaho Server. The folder will be recreated with your new `repository.xml` settings upon server restart.
{% endtab %}

{% tab title="Default repository XML file" %}
If you have a default `repository.xml` file, follow these steps to disable the `SearchIndex` tag:

1. Navigate to the `pentaho-solutions/system/jackrabbit` directory.
2. Open the `repository.xml` file with any text editor.
3. Search for the following instance of the `SearchIndex` tag:

   ```xml
   <SearchIndex class="org.apache.jackrabbit.core.query.lucene.SearchIndex">
       <param name="path" value="${rep.home}/repository/index"/>
       <param name="supportHighlighting" value="true"/>
   </SearchIndex>
   ```
4. Delete or comment out that `SearchIndex` tag.
5. Save and close the `repository.xml` file.

Whenever you make any changes to the Jackrabbit `repository.xml` file, you need to delete the `pentaho-solutions/system/jackrabbit/repository` folder and restart your Pentaho Server. The folder will be recreated with your new `repository.xml` settings upon server restart.
{% endtab %}
{% endtabs %}
