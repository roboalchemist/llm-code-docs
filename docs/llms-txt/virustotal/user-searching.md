# Source: https://virustotal.readme.io/docs/user-searching.md

# Searching for users

<style>
.tbd {  
  background-color: lightgray;  
}  
table {  
  width: 100%;  
  padding: 5px 2px 11px 4px;  
  font-size: 12px;  
  vertical-align: top;  
}  
table td:first-child {  
  max-width: 200px;  
}  
table td:nth-child(2) {  
  max-width: 600px;  
}  
</style>

The VirusTotal group view includes a user listing. Displayed users can be filtered using the "*Search user*" text box found at the top of the users list.

![Users searching form](https://storage.googleapis.com/vtdocresources/guides/account-management/usersearching_form_20231114.png)

You can use the following search modifiers to search for users matching certain criteria:

|                             |                                                                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **api\_quota\_group**       | Display only the users that are consuming premium API quota licensed by the organization.<br/>Example: *api\_quota\_group:your\_group\_name* |
| **email**                   | Filter users based on their email address.<br/>Example: *email:<foo@bar.com>*                                                                |
| **first\_name**             | Filter users based on their first name. This is a fulltext search, you need to provide an entire word.<br/>Example: *first\_name:john*       |
| **last\_name**              | Filter users based on their last name. This is a fulltext search, you need to provide an entire word.<br/>Example: *last\_name:snow*         |
| **username**                | Search for users with a given user name.<br/>Example: *username:vtusername*                                                                  |
| **Free text, no modifiers** | Search through any of the fields above.                                                                                                      |

The most common usage will be free text searches to locate users by a given email address, name or user name.