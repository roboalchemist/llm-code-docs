# Metadata

**Source:** [https://developer.wordpress.org/apis/metadata/](https://developer.wordpress.org/apis/metadata/)







## In this article


Table of Contents- Overview
- Function Reference
- Database RequirementsDefault Meta TablesMeta Table Structure
- Source File
- Related



↑Back to top



## Overview


TheMetadata APIis a simple and standarized way for retrieving and manipulating metadata of various WordPress object types.


Metadata for an object is a represented by a simple key-value pair.


Objects may contain multiple metadata entries that share the same key and differ only in their value.


## Function Reference


Add/Delete Metadata:


- add_metadata()
- delete_metadata()


Get/Update Metadata:


- get_metadata()
- update_metadata()


## Database Requirements


This function assumes that a dedicated MySQL table exists for the$meta_typeyou specify. Some desired$meta_typesdo not come with pre-installed WordPress tables, and so they must be created manually.


### Default Meta Tables


Assuming a prefix ofwp_, WordPress’s included meta tables are:


- wp_commentmeta: Metadata for specific comments.
- wp_postmeta: Metadata for pages, posts, and all other post types.
- wp_usermeta: Metadata for users.


### Meta Table Structure


To store data for meta types not included in the above table list, a new table needs to be created. All meta tables require four columns.


- meta_id– BIGINT(20): unsigned, auto_increment, not null, primary key.
- object_id– BIGINT(20): unsigned, not null.Replaceobjectwith the singular name of the content type being used.For instance, this column might be named post_id or term_id.Although this column is used like a foreign key, it should not be defined as one.
- meta_key– VARCHAR(255): The key of your custom meta data.
- meta_value– LONGTEXT: The value of your custom meta data.


## Source File


Metadata API is located inwp-includes/meta.php.


## Related


Metadata API:add_metadata(),get_metadata(),update_metadata(),delete_metadata().





First published


August 12, 2019


Last updated


November 21, 2022



[PreviousGlobal VariablesPrevious: Global Variables](https://developer.wordpress.org/apis/global-variables/)
[NextOptionsNext: Options](https://developer.wordpress.org/apis/options/)


