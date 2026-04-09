# luigi.contrib.mongodb

Classes

`MongoCellTarget`(mongo_client, index, ...)

Target for a ressource in a specific field from a MongoDB document

`MongoCollectionTarget`(mongo_client, index, ...)

Target for existing collection

`MongoCountTarget`(mongo_client, index, ...)

Target for documents count

`MongoRangeTarget`(mongo_client, index, ...)

Target for a level 0 field in a range of documents

`MongoTarget`(mongo_client, index, collection)

Target for a resource in MongoDB

class luigi.contrib.mongodb.MongoTarget(*mongo_client*, *index*, *collection*)

Target for a resource in MongoDB

Parameters:

- 

**mongo_client** (*MongoClient*) – MongoClient instance

- 

**index** (*str*) – database index

- 

**collection** (*str*) – index collection

get_collection()

Return targeted mongo collection to query on

get_index()

Return targeted mongo index to query on

class luigi.contrib.mongodb.MongoCellTarget(*mongo_client*, *index*, *collection*, *document_id*, *path*)

Target for a ressource in a specific field from a MongoDB document

Parameters:

- 

**document_id** (*str*) – targeted mongo document

- 

**path** (*str*) – full path to the targeted field in the mongo document

exists()

Test if target has been run
Target is considered run if the targeted field exists

read()

Read the target value
Use $project aggregate operator in order to support nested objects

write(*value*)

Write value to the target

class luigi.contrib.mongodb.MongoRangeTarget(*mongo_client*, *index*, *collection*, *document_ids*, *field*)

Target for a level 0 field in a range of documents

Parameters:

- 

**document_ids** – targeted mongo documents

- 

**field** (*str*) – targeted field in documents

exists()

Test if target has been run
Target is considered run if the targeted field exists in ALL documents

read()

Read the targets value

write(*values*)

Write values to the targeted documents
Values need to be a dict as : {document_id: value}

get_empty_ids()

Get documents id with missing targeted field

class luigi.contrib.mongodb.MongoCollectionTarget(*mongo_client*, *index*, *collection*)

Target for existing collection

Parameters:

- 

**mongo_client** (*MongoClient*) – MongoClient instance

- 

**index** (*str*) – database index

- 

**collection** (*str*) – index collection

exists()

Test if target has been run
Target is considered run if the targeted collection exists in the database

read()

Return if the target collection exists in the database

class luigi.contrib.mongodb.MongoCountTarget(*mongo_client*, *index*, *collection*, *target_count*)

Target for documents count

Parameters:

**target_count** – Value of the desired item count in the target

exists()

Test if the target has been run
Target is considered run if the number of items in the target matches value of self._target_count

read()

Using the aggregate method to avoid inaccurate count if using a sharded cluster
https://docs.mongodb.com/manual/reference/method/db.collection.count/#behavior