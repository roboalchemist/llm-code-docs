# Source: https://docs.pentaho.com/rest-api/file-management-apis-file-resource.md

# File Management APIs   File Resource

This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management.

## Backup Pentaho system data

> Performs a backup of the existing Pentaho System including content, schedules, users, roles, datasources, and the metastore.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/repo/files/backup\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/backup>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/x-www-form-urlencoded" \\\
> &#x20; -d "logFile=/path/to/export.log\&logLevel=INFO\&outputFile=/path/to/backup.zip"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/backup":{"post":{"tags":["File Management APIs - File Resource"],"summary":"Backup Pentaho system data","consumes":["application/x-www-form-urlencoded"],"description":"Performs a backup of the existing Pentaho System including content, schedules, users, roles, datasources, and the metastore.\n\n**Example Request:**\n```\nPOST pentaho/api/repo/files/backup\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/repo/files/backup\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/x-www-form-urlencoded\" \\\n  -d \"logFile=/path/to/export.log&logLevel=INFO&outputFile=/path/to/backup.zip\"\n```\n","requestBody":{"required":false,"content":{"application/x-www-form-urlencoded":{"schema":{"type":"object","properties":{"logFile":{"type":"string","description":"Path to the log file for the backup operation"},"logLevel":{"type":"string","description":"Log level for the backup operation"},"outputFile":{"type":"string","description":"Path for the output backup file"}}}}}},"responses":{"200":{"description":"Successfully exported the existing Pentaho System","content":{"application/zip":{"schema":{"type":"string","format":"binary","description":"Encrypted file stream containing the backup"}}}},"400":{"description":"User has provided an invalid file path"},"403":{"description":"User does not have administrative permissions"},"500":{"description":"Failure to complete the export"}}}}}}
````

## System restore from backup

> Performs a system restore of the Hitachi Vantara system. This includes content, schedules, users, roles, datasources, and the metastore.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/repo/files/systemRestore\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/systemRestore>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: multipart/form-data" \\\
> &#x20; -F "fileUpload=@backup.zip" \\\
> &#x20; -F "overwriteFile=true" \\\
> &#x20; -F "applyAclSettings=true" \\\
> &#x20; -F "overwriteAclSettings=true" \\\
> &#x20; -F "logFile=/path/to/import.log" \\\
> &#x20; -F "logLevel=INFO" \\\
> &#x20; -F "backupBundlePath=/path/to/bundle"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/systemRestore":{"post":{"tags":["File Management APIs - File Resource"],"summary":"System restore from backup","consumes":["multipart/form-data"],"description":"Performs a system restore of the Hitachi Vantara system. This includes content, schedules, users, roles, datasources, and the metastore.\n\n**Example Request:**\n```\nPOST pentaho/api/repo/files/systemRestore\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/repo/files/systemRestore\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: multipart/form-data\" \\\n  -F \"fileUpload=@backup.zip\" \\\n  -F \"overwriteFile=true\" \\\n  -F \"applyAclSettings=true\" \\\n  -F \"overwriteAclSettings=true\" \\\n  -F \"logFile=/path/to/import.log\" \\\n  -F \"logLevel=INFO\" \\\n  -F \"backupBundlePath=/path/to/bundle\"\n```\n","requestBody":{"required":true,"content":{"multipart/form-data":{"schema":{"type":"object","properties":{"fileUpload":{"type":"string","format":"binary","description":"The zip file generated using the backup endpoint, used to do a full system restore"},"overwriteFile":{"type":"string","description":"The file to be imported"},"overwrite":{"type":"string","description":"Whether to overwrite existing files during restore. If kept at the default of true, overwrites any value found on the system with the matching value that is being imported. Values that exist on the system, but do not exist in the import will not be deleted. When the overwrite flag is equal to false, any value that is found in the import process that already exists will not be imported."},"applyAclSettings":{"type":"string","description":"Whether to apply ACL settings from the backup"},"overwriteAclSettings":{"type":"string","description":"Whether to overwrite existing ACL settings"},"logFile":{"type":"string","description":"Path to the log file for the restore operation"},"logLevel":{"type":"string","description":"Log level for the restore operation"},"backupBundlePath":{"type":"string","description":"Path to the backup bundle"}},"required":["fileUpload"]}}}},"responses":{"200":{"description":"Successfully imported the Pentaho System"},"400":{"description":"User has provided an invalid file path"},"403":{"description":"User does not have administrative permissions"},"500":{"description":"Failure to complete the import"}}}}}}
````

## Move files to trash folder

> Move a list of files to the user's trash folder.\
> \
> \*\*Important Note:\*\* This end-point is not intended for concurrent execution by the same user or session.\
> It facilitates the User Console deletion UI, and should not be used in a manner inconsistent with how that UI operates.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/delete\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/delete>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: text/plain" \\\
> &#x20; -d "home:admin:file1.txt,home:admin:file2.txt"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/delete":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Move files to trash folder","consumes":["*/*"],"description":"Move a list of files to the user's trash folder.\n\n**Important Note:** This end-point is not intended for concurrent execution by the same user or session.\nIt facilitates the User Console deletion UI, and should not be used in a manner inconsistent with how that UI operates.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/delete\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/delete\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: text/plain\" \\\n  -d \"home:admin:file1.txt,home:admin:file2.txt\"\n```\n","requestBody":{"required":true,"content":{"*/*":{"schema":{"type":"string","description":"Comma separated list of the files to be moved to trash folder"}}}},"responses":{"200":{"description":"Successfully moved file to trash"},"500":{"description":"Failure move the file to the trash"}}}}}}
````

## Permanently delete files from system

> Permanently delete files from the repository system. This operation cannot be undone.\
> \
> \*\*Important Note: This end-point is not intended for concurrent execution by the\
> same user or session. It facilitates the User Console deletion UI, and should\
> not be used in a manner inconsistent with how that UI operates.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/deletepermanent\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/deletepermanent>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: text/plain" \\\
> &#x20; -d "home:admin:file1.txt,home:admin:file2.txt"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/deletepermanent":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Permanently delete files from system","consumes":["*/*"],"description":"Permanently delete files from the repository system. This operation cannot be undone.\n\n**Important Note: This end-point is not intended for concurrent execution by the\nsame user or session. It facilitates the User Console deletion UI, and should\nnot be used in a manner inconsistent with how that UI operates.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/deletepermanent\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/deletepermanent\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: text/plain\" \\\n  -d \"home:admin:file1.txt,home:admin:file2.txt\"\n```\n","requestBody":{"required":true,"content":{"*/*":{"schema":{"type":"string","description":"Comma separated list of the files to be deleted permanently"}}}},"responses":{"200":{"description":"Successfully deleted the comma separated list of fileIds from the system"},"403":{"description":"Failure to delete the file due to path not found"}}}}}}
````

## Check if file exists

> Checks if a file exists at the specified path in the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/exists?pathId=%2Fhome%2Fuser%2Ftest\_file.wtr\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/exists?pathId=%2Fhome%2Fuser%2Ftest\\_file.wtr>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/exists":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check if file exists","description":"Checks if a file exists at the specified path in the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/exists?pathId=%2Fhome%2Fuser%2Ftest_file.wtr\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/exists?pathId=%2Fhome%2Fuser%2Ftest_file.wtr\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"query","required":true,"description":"Encoded path of the repository file to check. Must be URL-encoded.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully finds the file"},"404":{"description":"Failed to find the file or invalid input"},"500":{"description":"For any other exceptions"}}}}}}
````

## Get file or directory content

> Takes a pathId and returns a JAX-RS Response object with the appropriate status code,\
> header, and body containing the output stream based on the file located at the pathId.\
> \
> Produces MediaType.WILDCARD (\*/\*) to support any content type based on the file being retrieved.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/jmeter-test:test\\_file\\_1.xml>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: \*/\*"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get file or directory content","produces":["*/*"],"description":"Takes a pathId and returns a JAX-RS Response object with the appropriate status code,\nheader, and body containing the output stream based on the file located at the pathId.\n\nProduces MediaType.WILDCARD (*/*) to support any content type based on the file being retrieved.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/jmeter-test:test_file_1.xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: */*\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully get the file or directory","content":{"*/*":{"schema":{"type":"string","format":"binary","description":"File content stream with appropriate headers (supports any media type)"}}}},"404":{"description":"Failed to find the file or resource"},"500":{"description":"Failed to open content"}}}}}}
````

## Create a new file

> Creates a new file with the provided contents at a given path.\
> Returns a JAX-RS Response object with the appropriate status code, header, and body.\
> \
> Consumes MediaType.WILDCARD (\*/\*) to accept any content type for the file being created.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT /repo/files/:jmeter-test:test\_file\_1.xml\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/jmeter-test:test\\_file\\_1.xml>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: \*/\*" \\\
> &#x20; \--data-binary @file\_content.xml\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Create a new file","consumes":["*/*"],"description":"Creates a new file with the provided contents at a given path.\nReturns a JAX-RS Response object with the appropriate status code, header, and body.\n\nConsumes MediaType.WILDCARD (*/*) to accept any content type for the file being created.\n\n**Example Request:**\n```\nPUT /repo/files/:jmeter-test:test_file_1.xml\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/jmeter-test:test_file_1.xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: */*\" \\\n  --data-binary @file_content.xml\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"*/*":{"schema":{"type":"string","format":"binary","description":"An Input Stream with the contents of the file to be created"}}}},"responses":{"200":{"description":"Successfully created the file"},"403":{"description":"Failure to create the file due to permissions, file already exists, or invalid path id"}}}}}}
````

## Get file access control list

> Retrieves the ACL settings of the requested repository file in either xml or json format.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/acl\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/acl>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileAclDto":{"type":"object","description":"Repository file access control list","properties":{"id":{"type":"string","description":"Unique identifier for the ACL"},"owner":{"type":"string","description":"Owner of the file"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"inheriting":{"type":"boolean","description":"Whether ACL inherits from parent"},"entriesInheriting":{"type":"boolean","description":"Whether entries inherit"},"aces":{"type":"array","description":"Access control entries","items":{"type":"object","properties":{"recipient":{"type":"string","description":"Recipient of the access control entry"},"recipientType":{"type":"integer","description":"Type of recipient (USER, ROLE)"},"permissions":{"type":"array","description":"Permissions granted","items":{"type":"integer"}}}}}}}}},"paths":{"/repo/files/{pathId}/acl":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get file access control list","produces":["application/json","application/xml"],"description":"Retrieves the ACL settings of the requested repository file in either xml or json format.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/acl\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/acl\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}}],"responses":{"200":{"description":"Returns the requested file permissions in xml or json format","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileAclDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileAclDto"}}}},"500":{"description":"File failed to be retrieved. This could be caused by an invalid path, or the file does not exist"}}}}}}
````

## Update file access control list

> This method is used to update and save the acls of the selected file to the repository. Supports both XML and JSON formats.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/acl\
> \`\`\`\
> \
> \*\*cURL Example (JSON):\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/acl>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/json" \\\
> &#x20; -d '{"entriesInheriting":true,"id":"d45d4972-989e-48d5-8bd0-f7024a77f08f","owner":"admin","ownerType":0}'\
> \`\`\`\
> \
> \*\*cURL Example (XML):\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/acl>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -d '\<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\<repositoryFileAclDto>\<entriesInheriting>true\</entriesInheriting>\<id>d45d4972-989e-48d5-8bd0-f7024a77f08f\</id>\<owner>admin\</owner>\<ownerType>0\</ownerType>\</repositoryFileAclDto>'\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileAclDto":{"type":"object","description":"Repository file access control list","properties":{"id":{"type":"string","description":"Unique identifier for the ACL"},"owner":{"type":"string","description":"Owner of the file"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"inheriting":{"type":"boolean","description":"Whether ACL inherits from parent"},"entriesInheriting":{"type":"boolean","description":"Whether entries inherit"},"aces":{"type":"array","description":"Access control entries","items":{"type":"object","properties":{"recipient":{"type":"string","description":"Recipient of the access control entry"},"recipientType":{"type":"integer","description":"Type of recipient (USER, ROLE)"},"permissions":{"type":"array","description":"Permissions granted","items":{"type":"integer"}}}}}}}}},"paths":{"/repo/files/{pathId}/acl":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Update file access control list","consumes":["application/json","application/xml"],"description":"This method is used to update and save the acls of the selected file to the repository. Supports both XML and JSON formats.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:jmeter-test:test_file_1.xml/acl\n```\n\n**cURL Example (JSON):**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/acl\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\"entriesInheriting\":true,\"id\":\"d45d4972-989e-48d5-8bd0-f7024a77f08f\",\"owner\":\"admin\",\"ownerType\":0}'\n```\n\n**cURL Example (XML):**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/acl\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/xml\" \\\n  -d '<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><repositoryFileAclDto><entriesInheriting>true</entriesInheriting><id>d45d4972-989e-48d5-8bd0-f7024a77f08f</id><owner>admin</owner><ownerType>0</ownerType></repositoryFileAclDto>'\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileAclDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileAclDto"}}}},"responses":{"200":{"description":"Successfully saved file"},"400":{"description":"Failed to save acls due to malformed xml"},"403":{"description":"Failed to save acls due to missing or incorrect properties"},"500":{"description":"Failed to save acls due to another error"}}}}}}
````

## Check whether the current user has specific permission on the selected repository file

> Check whether the current user has specific permission on the selected repository file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/canAccess?permissions=1\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/canAccess?permissions=1>" \\\
> &#x20; -H "Authorization: Basic YWRtaW06cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/canAccess":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check whether the current user has specific permission on the selected repository file","produces":["text/plain"],"description":"Check whether the current user has specific permission on the selected repository file.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/canAccess?permissions=1\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/canAccess?permissions=1\" \\\n  -H \"Authorization: Basic YWRtaW06cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}},{"name":"permissions","in":"query","required":false,"description":"Pipe separated list of permissions","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the permissions of the given paths","content":{"text/plain":{"schema":{"type":"string","enum":["true","false"],"description":"String \"true\" if the user has requested permissions on the file, or \"false\" otherwise"}}}},"500":{"description":"Unable to retrieve the permissions of the given paths due to some other error"}}}}}}
````

## Check file access permissions map

> Checks whether the current user has permissions to the selected files. \
> This can check for more than one permission at once but will only return true if all permissions checked are valid.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.txt/canAccessMap?permissions=1\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.txt/canAccessMap?permissions=1>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/canAccessMap":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check file access permissions map","produces":["application/xml","application/json"],"description":"Checks whether the current user has permissions to the selected files. \nThis can check for more than one permission at once but will only return true if all permissions checked are valid.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.txt/canAccessMap?permissions=1\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.txt/canAccessMap?permissions=1\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}},{"name":"permissions","in":"query","required":true,"description":"Pipe separated permissions to be checked","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the permissions of the file","content":{"application/xml":{"schema":{"type":"object"}},"application/json":{"schema":{"type":"object","properties":{"setting":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},"value":{"type":"string"}}}}}}}}},"500":{"description":"Unable to retrieve the permissions of the file due to some other error"}}}}}}
````

## Download file or directory

> Download the selected file or folder from the repository. In order to download file \
> from the repository, the user needs to have Publish action. How the file comes down \
> to the user and where it is saved is system and browser dependent.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/download?locale=de\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/download?locale=de>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "User-Agent: Mozilla/5.0" \\\
> &#x20; -o test\_file\_1.xml\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> Encrypted file stream\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/download":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Download file or directory","produces":["*/*"],"description":"Download the selected file or folder from the repository. In order to download file \nfrom the repository, the user needs to have Publish action. How the file comes down \nto the user and where it is saved is system and browser dependent.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/download?locale=de\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/download?locale=de\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"User-Agent: Mozilla/5.0\" \\\n  -o test_file_1.xml\n```\n\n**Example Response:**\n```\nEncrypted file stream\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file.","schema":{"type":"string"}},{"name":"withManifest","in":"query","required":false,"description":"true or false (download file with manifest). Defaults to true (include manifest) if this string can't be directly parsed to 'false' (case sensitive). This argument is only used if a directory is being downloaded.","schema":{"type":"string"}},{"name":"user-agent","in":"header","required":false,"description":"A string representing the type of browser to use. Currently only applicable if contains 'FireFox' as FireFox requires a header with encoding information (UTF-8) and a quoted filename, otherwise encoding information is not supplied and the filename is not quoted.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successful download","content":{"*/*":{"schema":{"type":"string","format":"binary","description":"Encrypted file stream"}}}},"400":{"description":"Usually a bad pathId"},"403":{"description":"pathId points at a file the user doesn't have access to"},"404":{"description":"File not found"},"500":{"description":"Failed to download file for another reason"}}}}}}
````

## Get file as inline content

> Retrieves the file from the repository as inline. This is mainly used for css and dependent files for the html document.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/inline\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/inline>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\
> \<repositoryFileAclDto>\
> &#x20; \<entriesInheriting>true\</entriesInheriting>\
> &#x20; \<id>d45d4972-989e-48d5-8bd0-f7024a77f08f\</id>\
> &#x20; \<owner>admin\</owner>\
> &#x20; \<ownerType>0\</ownerType>\
> \</repositoryFileAclDto>\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/inline":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get file as inline content","produces":["*/*"],"description":"Retrieves the file from the repository as inline. This is mainly used for css and dependent files for the html document.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/inline\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/inline\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<repositoryFileAclDto>\n  <entriesInheriting>true</entriesInheriting>\n  <id>d45d4972-989e-48d5-8bd0-f7024a77f08f</id>\n  <owner>admin</owner>\n  <ownerType>0</ownerType>\n</repositoryFileAclDto>\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved file","content":{"*/*":{"schema":{"type":"string","format":"binary","description":"The file content for inline display"}}}},"403":{"description":"Failed to retrieve file due to permission problem"},"404":{"description":"Failed to retrieve file due because file was not found"},"500":{"description":"Failed to download file because of some other error"}}}}}}
````

## Get file locale information

> Retrieves the list of locale maps for the selected repository file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/locales\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/locales>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/locales":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get file locale information","produces":["application/xml","application/json"],"description":"Retrieves the list of locale maps for the selected repository file.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/locales\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/locales\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved locale information","content":{"application/json":{"schema":{"type":"object","properties":{"localePropertiesMapEntries":{"type":"array","items":{"type":"object","properties":{"locale":{"type":"string","description":"The locale identifier"},"properties":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string"},"value":{"type":"string"}}}}}}}}}},"application/xml":{"schema":{"type":"object","xml":{"name":"localePropertiesMapEntries"}}}}},"404":{"description":"Failed to retrieve locales because the file was not found"},"500":{"description":"Unable to retrieve locales due to some other error"}}}}}}
````

## Get locale properties for a file

> Retrieve the list of locale properties for a given locale.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/localeProperties?locale=ja\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/localeProperties?locale=ja>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/localeProperties":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get locale properties for a file","produces":["application/xml","application/json"],"description":"Retrieve the list of locale properties for a given locale.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/localeProperties?locale=ja\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/localeProperties?locale=ja\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}},{"name":"locale","in":"query","required":true,"description":"The specified locale","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved locale properties","content":{"application/json":{"schema":{"type":"object","properties":{"stringKeyStringValueDtoes":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string"},"value":{"type":"string"}}}}}}},"application/xml":{"schema":{"type":"object","xml":{"name":"stringKeyStringValueDtoes"}}}}},"500":{"description":"Unable to retrieve locale properties due to some other error"}}}}}}
````

## Set locale properties for a file

> Save list of locale properties for a given locale.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/localeProperties?locale=ja\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/localeProperties?locale=ja>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -d '\<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\
> &#x20; \<stringKeyStringValueDtoes>\
> &#x20;   \<stringKeyStringValueDto>\
> &#x20;     \<key>file.title\</key>\
> &#x20;     \<value>チャート選択リスト\</value>\
> &#x20;   \</stringKeyStringValueDto>\
> &#x20;   \<stringKeyStringValueDto>\
> &#x20;     \<key>jcr:primaryType\</key>\
> &#x20;     \<value>nt:unstructured\</value>\
> &#x20;   \</stringKeyStringValueDto>\
> &#x20;   \<stringKeyStringValueDto>\
> &#x20;     \<key>file.description\</key>\
> &#x20;     \<value>複数のチャートタイプを表示します\</value>\
> &#x20;   \</stringKeyStringValueDto>\
> &#x20; \</stringKeyStringValueDtoes>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> This response does not contain data.\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/localeProperties":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Set locale properties for a file","produces":["application/xml","application/json"],"description":"Save list of locale properties for a given locale.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:jmeter-test:test_file_1.xml/localeProperties?locale=ja\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/localeProperties?locale=ja\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/xml\" \\\n  -d '<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n  <stringKeyStringValueDtoes>\n    <stringKeyStringValueDto>\n      <key>file.title</key>\n      <value>チャート選択リスト</value>\n    </stringKeyStringValueDto>\n    <stringKeyStringValueDto>\n      <key>jcr:primaryType</key>\n      <value>nt:unstructured</value>\n    </stringKeyStringValueDto>\n    <stringKeyStringValueDto>\n      <key>file.description</key>\n      <value>複数のチャートタイプを表示します</value>\n    </stringKeyStringValueDto>\n  </stringKeyStringValueDtoes>'\n```\n\n**Example Response:**\n```\nThis response does not contain data.\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}},{"name":"locale","in":"query","required":true,"description":"A string representation of the locale to set properties on","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"stringKeyStringValueDtoes":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}},"required":["key","value"]}}}}},"application/xml":{"schema":{"type":"object","properties":{"stringKeyStringValueDtoes":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}},"required":["key","value"]}}}}}}},"responses":{"200":{"description":"Successfully updated locale properties","content":{"application/xml":{"schema":{"type":"object","description":"This response does not contain data"}},"application/json":{"schema":{"type":"object","description":"This response does not contain data"}}}},"500":{"description":"Unable to update locale properties due to some other error"}}}}}}
````

## Delete locale for a file

> Delete the locale for the selected file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/deleteLocale?locale=ja\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/deleteLocale?locale=ja>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> This response does not contain data.\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/deleteLocale":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Delete locale for a file","produces":["application/xml","application/json"],"description":"Delete the locale for the selected file.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:jmeter-test:test_file_1.xml/deleteLocale?locale=ja\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/deleteLocale?locale=ja\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nThis response does not contain data.\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file","schema":{"type":"string"}},{"name":"locale","in":"query","required":true,"description":"A string representations of the locale to be deleted","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully deleted the locale","content":{"application/xml":{"schema":{"type":"object","description":"This response does not contain data"}},"application/json":{"schema":{"type":"object","description":"This response does not contain data"}}}},"500":{"description":"Unable to delete the locale properties due to some other error"}}}}}}
````

## Get directory children

> Retrieve a list of child files from the selected repository path of the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test/children\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test/children>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/children":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get directory children","produces":["application/xml","application/json"],"description":"Retrieve a list of child files from the selected repository path of the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test/children\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test/children\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}},{"name":"filter","in":"query","required":false,"description":"Filter to be applied for search. The filter can be broken down into 3 parts; File types, Child Node Filter, and Member Filters. Each part is separated with a pipe (|) character. File Types are represented by a word phrase. This phrase is recognized as a file type phrase and processed accordingly. Valid File Type word phrases include \"FILES\", \"FOLDERS\", and \"FILES_FOLDERS\" and denote whether to return files, folders, or both files and folders, respectively. The Child Node Filter is a list of allowed names of files separated by the pipe (|) character. Each file name in the filter may be a full name or a partial name with one or more wildcard characters (\"*\"). The filter does not apply to root node. The Member Filter portion of the filter parameter allows the caller to specify which properties of the metadata to return. Member Filters start with \"includeMembers=\" or \"excludeMembers=\" followed by a list of comma separated field names that are to be included in, or, excluded from, the list. Valid field names can be found in  org.pentaho.platform.repository2.unified.webservices#RepositoryFileAdapter. Omission of a member filter will return all members. It is invalid to both and includeMembers= and an excludeMembers= clause in the same service call.","schema":{"type":"string"}},{"name":"showHidden","in":"query","required":false,"description":"Include or exclude hidden files from the file list","schema":{"type":"boolean","default":false}},{"name":"includeAcls","in":"query","required":false,"description":"Include permission information about the file in the output","schema":{"type":"boolean","default":false}}],"responses":{"200":{"description":"Successfully retrieved the list of child files from selected repository path of the repository","content":{"application/xml":{"schema":{"type":"object"}},"application/json":{"schema":{"type":"object","properties":{"repositoryFileDto":{"type":"array","items":{"type":"object","properties":{"createdDate":{"type":"integer"},"fileSize":{"type":"integer"},"folder":{"type":"boolean"},"hidden":{"type":"boolean"},"id":{"type":"string"},"locale":{"type":"string"},"locked":{"type":"boolean"},"name":{"type":"string"},"ownerType":{"type":"integer"},"path":{"type":"string"},"title":{"type":"string"},"versioned":{"type":"boolean"}}}}}}}}},"500":{"description":"Server Error"}}}}}}
````

## Get directory tree

> Retrieve the recursive list of children of the selected repository file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:public/tree?showHidden=false\&filter=\*|FILES&\_=1389042244670\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:public/tree?showHidden=false\\&filter=\\*|FILES&\\_=1389042244670>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileTreeDto":{"type":"object","description":"Repository file tree structure","properties":{"file":{"$ref":"#/components/schemas/RepositoryFileDto"},"children":{"type":"array","description":"Child files and directories","items":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}}}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/{pathId}/tree":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get directory tree","produces":["application/xml","application/json"],"description":"Retrieve the recursive list of children of the selected repository file.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:public/tree?showHidden=false&filter=*|FILES&_=1389042244670\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:public/tree?showHidden=false&filter=*|FILES&_=1389042244670\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}},{"name":"depth","in":"query","required":false,"description":"How many level should the search go.","schema":{"type":"integer"}},{"name":"filter","in":"query","required":false,"description":"Filter to be applied for search. The filter can be broken down into 3 parts; File types, \nChild Node Filter, and Member Filters. Each part is separated with a pipe (|) character.\n\nFile Types are represented by a word phrase. This phrase is recognized as a file type phrase \nand processed accordingly. Valid File Type word phrases include \"FILES\", \"FOLDERS\", and \n\"FILES_FOLDERS\" and denote whether to return files, folders, or both files and folders, respectively.\n\nThe Child Node Filter is a list of allowed names of files separated by the pipe (|) character. \nEach file name in the filter may be a full name or a partial name with one or more wildcard \ncharacters (\"*\"). The filter does not apply to root node.\n\nThe Member Filter portion of the filter parameter allows the caller to specify which properties \nof the metadata to return. Member Filters start with \"includeMembers=\" or \"excludeMembers=\" \nfollowed by a list of comma separated field names that are to be included in, or, excluded from, \nthe list. Valid field names can be found in org.pentaho.platform.repository2.unified.webservices#RepositoryFileAdapter.\nOmission of a member filter will return all members. It is invalid to both and includeMembers= \nand an excludeMembers= clause in the same service call.\n","schema":{"type":"string"}},{"name":"showHidden","in":"query","required":false,"description":"Include or exclude hidden files from the file list.","schema":{"type":"boolean","default":false}},{"name":"includeAcls","in":"query","required":false,"description":"Include permission information about the file in the output.","schema":{"type":"boolean","default":false}},{"name":"includeSysDirs","in":"query","required":false,"description":"Include system directories in the output.","schema":{"type":"boolean","default":false}}],"responses":{"200":{"description":"Successfully retrieved the list of files from root of the repository. A RepositoryFileTreeDto object containing the files at the root of the repository. Will return files but not folders under the \"/\" folder. The fields returned will include the name, filesize, description, id and title.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}}}},"404":{"description":"Invalid parameters."},"500":{"description":"Server Error."}}}}}}
````

## Check administration permissions

> Checks to see if the current user is an administer of the platform and returns a boolean response.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/canAdminister\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/canAdminister>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/canAdminister":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check administration permissions","produces":["text/plain"],"description":"Checks to see if the current user is an administer of the platform and returns a boolean response.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/canAdminister\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/canAdminister\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Successfully returns a boolean value, either true or false","content":{"text/plain":{"schema":{"type":"string","description":"String \"true\" if the user can administer the platform, or \"false\" otherwise."}}}}}}}}}
````

## Check create permissions

> Checks the users permission to determine if that user can create new content in the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/canCreate\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/canCreate>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/canCreate":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check create permissions","produces":["text/plain"],"description":"Checks the users permission to determine if that user can create new content in the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/canCreate\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/canCreate\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Successfully returns true or false depending on the users permissions","content":{"text/plain":{"schema":{"type":"string","description":"String \"true\" if the user can create new content, or \"false\" otherwise."}}}}}}}}}
````

## Get reserved characters

> Returns the list of reserved characters from the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/reservedCharacters\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/reservedCharacters>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/reservedCharacters":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get reserved characters","produces":["text/plain"],"description":"Returns the list of reserved characters from the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/reservedCharacters\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/reservedCharacters\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Successfully returns a list of repositroy reserved characters","content":{"text/plain":{"schema":{"type":"string","description":"List of characters that are reserved by the repository."}}}}}}}}}
````

## Get reserved characters for display

> Returns the list of reserved characters from the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/reservedCharactersDisplay\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/reservedCharactersDisplay>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/reservedCharactersDisplay":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get reserved characters for display","produces":["text/plain"],"description":"Returns the list of reserved characters from the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/reservedCharactersDisplay\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/reservedCharactersDisplay\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Successfully returns a list of repositroy reserved characters","content":{"text/plain":{"schema":{"type":"string","description":"List of characters that are reserved by the repository."}}}}}}}}}
````

## Check edit permissions

> Checks the users permission to determine if that user can edit an existing content in the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/canEdit\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/canEdit>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/canEdit":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check edit permissions","produces":["text/plain"],"description":"Checks the users permission to determine if that user can edit an existing content in the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/canEdit\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/canEdit\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Successfully returns true or false depending on the users permissions","content":{"text/plain":{"schema":{"type":"string","description":"String \"true\" if the user can edit existing content, or \"false\" otherwise."}}}}}}}}}
````

## Rename file or directory

> Rename the selected file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/rename?newName=test\_file\_8\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/rename?newName=test\\_file\\_8>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/rename":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Rename file or directory","consumes":["*/*"],"produces":["*/*"],"description":"Rename the selected file.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:jmeter-test:test_file_1.xml/rename?newName=test_file_8\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/rename?newName=test_file_8\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}},{"name":"newName","in":"query","required":true,"description":"String indicating the new name of the file.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully renamed file.","content":{"*/*":{"schema":{"type":"string","description":"Response with 200 OK, if the file does not exist to be renamed the response will return 200 OK with the string \"File to be renamed does not exist\"."}}}},"403":{"description":"Forbidden."},"404":{"description":"File not found."}}}}}}
````

## Get root directory properties

> Retrieves the properties of the root directory.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/properties\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/properties>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/properties":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get root directory properties","produces":["application/xml","application/json"],"description":"Retrieves the properties of the root directory.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/properties\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/properties\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","responses":{"200":{"description":"Successfully retrieved the properties of the root directory.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDto"}}}},"404":{"description":"Unable to retrieve the properties of the root directory due to file not found error."},"500":{"description":"Unable to retrieve the properties of the root directory due to some other error."}}}}}}
````

## Get specific file properties

> Retrieves the properties of a selected repository file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:/properties\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/home:admin:report.prpt/properties>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/{pathId}/properties":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get specific file properties","produces":["application/xml","application/json"],"description":"Retrieves the properties of a selected repository file.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:/properties\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/home:admin:report.prpt/properties\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the repository file.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the properties for a file.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDto"}}}},"204":{"description":"Invalid file path."}}}}}}
````

## Get file metadata

> Retrieve the metadata of the selected file. Even though the hidden flag is a property of the file node itself, and not\
> the metadata child, it is considered metadata from PUC and is included in the setMetadata call.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/metadata\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/home:admin:report.prpt/metadata>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{}},"paths":{"/repo/files/{pathId}/metadata":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get file metadata","produces":["application/json"],"description":"Retrieve the metadata of the selected file. Even though the hidden flag is a property of the file node itself, and not\nthe metadata child, it is considered metadata from PUC and is included in the setMetadata call.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/metadata\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/home:admin:report.prpt/metadata\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of /\nor \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.\n","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved metadata.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StringKeyStringValueDtoWrapper"}}}},"403":{"description":"Invalid path."},"500":{"description":"Server Error."}}}}}}
````

## Update file metadata

> Store the metadata of the selected file. Even though the hidden flag is a property of the file node itself, and not\
> the metadata child, it is considered metadata from PUC and is included in the setMetadata call.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/metadata\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/metadata>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/json" \\\
> &#x20; -d '{\
> &#x20;   "stringKeyStringValueDtoes": \[\
> &#x20;     {\
> &#x20;       "key": "metadata.key.1",\
> &#x20;       "value": "metadata.value.1"\
> &#x20;     }\
> &#x20;   ]\
> &#x20; }'\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{}},"paths":{"/repo/files/{pathId}/metadata":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Update file metadata","produces":["application/xml","application/json"],"consumes":["application/json"],"description":"Store the metadata of the selected file. Even though the hidden flag is a property of the file node itself, and not\nthe metadata child, it is considered metadata from PUC and is included in the setMetadata call.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:jmeter-test:test_file_1.xml/metadata\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/metadata\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"stringKeyStringValueDtoes\": [\n      {\n        \"key\": \"metadata.key.1\",\n        \"value\": \"metadata.value.1\"\n      }\n    ]\n  }'\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of /\nor \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.\n","schema":{"type":"string"}}],"requestBody":{"required":true,"description":"A list of StringKeyStringValueDto objects.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StringKeyStringValueDtoWrapper"}}}},"responses":{"200":{"description":"Successfully retrieved metadata."},"400":{"description":"Invalid payload."},"403":{"description":"Invalid path."},"500":{"description":"Server Error."}}}}}}
````

## Create directory

> Creates a new folder with the specified name.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/files/:public:jmeter-test-dir/createDir\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:public:jmeter-test-dir/createDir>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/{pathId}/createDir":{"put":{"tags":["File Management APIs - File Resource"],"summary":"Create directory","consumes":["*/*"],"description":"Creates a new folder with the specified name.\n\n**Example Request:**\n```\nPUT pentaho/api/repo/files/:public:jmeter-test-dir/createDir\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/files/:public:jmeter-test-dir/createDir\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in\nplace of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.\n","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully created folder."},"403":{"description":"Forbidden."},"409":{"description":"Path already exists."},"500":{"description":"Server Error."}}}}}}
````

## Get generated content

> Retrieve the list of executed contents for a selected content from the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/generatedContent?locale=de\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/generatedContent?locale=de>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDtoWrapper":{"type":"object","description":"Wrapper for list of repository files","properties":{"children":{"type":"array","description":"List of repository files","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}},"xml":{"name":"repositoryFileDtoes"}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/{pathId}/generatedContent":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get generated content","produces":["application/xml","application/json"],"description":"Retrieve the list of executed contents for a selected content from the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/generatedContent?locale=de\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/generatedContent?locale=de\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the destination for files to be copied.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the list of RepositoryFileDto objects.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}}}}}}}}}
````

## Get generated content for user

> Retrieve the executed contents for a selected repository file and a given user.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/:jmeter-test:test\_file\_1.xml/generatedContentForUser?user=admin\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test\\_file\\_1.xml/generatedContentForUser?user=admin>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDtoWrapper":{"type":"object","description":"Wrapper for list of repository files","properties":{"children":{"type":"array","description":"List of repository files","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}},"xml":{"name":"repositoryFileDtoes"}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/{pathId}/generatedContentForUser":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get generated content for user","produces":["application/xml","application/json"],"description":"Retrieve the executed contents for a selected repository file and a given user.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/:jmeter-test:test_file_1.xml/generatedContentForUser?user=admin\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/:jmeter-test:test_file_1.xml/generatedContentForUser?user=admin\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"Colon separated path for the destination for files to be copied.","schema":{"type":"string"}},{"name":"user","in":"query","required":false,"description":"The username for the generated content folder.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the list of RepositoryFileDto objects.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}}}},"500":{"description":"Server Error."}}}}}}
````

## Check download permissions

> Validates if a current user is authorized to download content from the given dir.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/canDownload\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/canDownload>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/canDownload":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check download permissions","produces":["text/plain"],"description":"Validates if a current user is authorized to download content from the given dir.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/canDownload\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/canDownload\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"dirPath","in":"query","required":false,"description":"to be validated for download action for the current user.","schema":{"type":"string","default":""}}],"responses":{"200":{"description":"Returns a boolean response.","content":{"text/plain":{"schema":{"type":"string"}}}}}}}}}
````

## Check upload permissions

> Validates if a current user is authorized to upload content to the given dir\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/canUpload\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/canUpload>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/files/canUpload":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Check upload permissions","produces":["text/plain"],"description":"Validates if a current user is authorized to upload content to the given dir\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/canUpload\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/canUpload\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"dirPath","in":"query","required":false,"description":"to be validated for upload action for the current user.","schema":{"type":"string","default":""}}],"responses":{"200":{"description":"Returns a boolean response.","content":{"text/plain":{"schema":{"type":"string"}}}}}}}}}
````

## Get root children

> Retrieve a list of child files from the root of the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/children?showHidden=false\&filter=\*|FILES&\_=1389042244670\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/children?showHidden=false\\&filter=\\*|FILES>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDtoWrapper":{"type":"object","description":"Wrapper for list of repository files","properties":{"children":{"type":"array","description":"List of repository files","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}},"xml":{"name":"repositoryFileDtoes"}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/children":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get root children","produces":["application/xml","application/json"],"description":"Retrieve a list of child files from the root of the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/children?showHidden=false&filter=*|FILES&_=1389042244670\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/children?showHidden=false&filter=*|FILES\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"filter","in":"query","required":false,"description":"Filter to be applied for search. The filter can be broken down into 3 parts; File types, Child Node\nFilter, and Member Filters. Each part is separated with a pipe (|) character.\n\nFile Types are represented by a word phrase. This phrase is recognized as a file type phrase and processed\naccordingly. Valid File Type word phrases include \"FILES\", \"FOLDERS\", and \"FILES_FOLDERS\" and denote\nwhether to return files, folders, or both files and folders, respectively.\n\nThe Child Node Filter is a list of allowed names of files separated by the pipe (|) character. Each file\nname in the filter may be a full name or a partial name with one or more wildcard characters (\"*\"). The\nfilter does not apply to root node.\n\nThe Member Filter portion of the filter parameter allows the caller to specify which properties of the\nmetadata to return. Member Filters start with \"includeMembers=\" or \"excludeMembers=\" followed by a list of\ncomma separated field names that are to be included in, or, excluded from, the list. Valid field names can\nbe found in org.pentaho.platform.repository2.unified.webservices#RepositoryFileAdapter.\nOmission of a member filter will return all members. It is invalid to both and includeMembers= and an\nexcludeMembers= clause in the same service call.\n","schema":{"type":"string"}},{"name":"showHidden","in":"query","required":false,"description":"Include or exclude hidden files from the file list.","schema":{"type":"boolean"}},{"name":"includeAcls","in":"query","required":false,"description":"Include permission information about the file in the output.","schema":{"type":"boolean","default":false}}],"responses":{"200":{"description":"Successfully retrieved the list of child files from root of the repository.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}}}},"500":{"description":"Server Error."}}}}}}
````

## Get deleted files

> Retrieve a list of files in the trash folder of the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/deleted\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/deleted>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDtoWrapper":{"type":"object","description":"Wrapper for list of repository files","properties":{"children":{"type":"array","description":"List of repository files","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}},"xml":{"name":"repositoryFileDtoes"}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/deleted":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get deleted files","produces":["application/xml","application/json"],"description":"Retrieve a list of files in the trash folder of the repository.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/deleted\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/deleted\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","responses":{"200":{"description":"Successfully retrieved the list of files from trash folder of the repository.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileDtoWrapper"}}}},"500":{"description":"Server Error."}}}}}}
````

## Check paths access list

> Checks whether the current user has permissions to the provided list of paths.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/repo/files/pathsAccessList\
> \`\`\`\
> \
> \*\*cURL Example (JSON):\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/pathsAccessList>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/json" \\\
> &#x20; -d '{\
> &#x20;   "strings": \["/public", "/home/admin", "/etc"]\
> &#x20; }'\
> \`\`\`\
> \
> \*\*cURL Example (XML):\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/pathsAccessList>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -d '\<?xml version="1.0" encoding="UTF-8"?>\
> &#x20; \<stringListWrapper>\
> &#x20;   \<strings>/public\</strings>\
> &#x20;   \<strings>/home/admin\</strings>\
> &#x20;   \<strings>/etc\</strings>\
> &#x20; \</stringListWrapper>'\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"StringListWrapper":{"type":"object","description":"Wrapper for list of strings","properties":{"stringList":{"type":"array","description":"List of strings","items":{"type":"string"}}}}}},"paths":{"/repo/files/pathsAccessList":{"post":{"tags":["File Management APIs - File Resource"],"summary":"Check paths access list","consumes":["application/xml","application/json"],"produces":["application/xml","application/json"],"description":"Checks whether the current user has permissions to the provided list of paths.\n\n**Example Request:**\n```\nPOST pentaho/api/repo/files/pathsAccessList\n```\n\n**cURL Example (JSON):**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/repo/files/pathsAccessList\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"strings\": [\"/public\", \"/home/admin\", \"/etc\"]\n  }'\n```\n\n**cURL Example (XML):**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/repo/files/pathsAccessList\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/xml\" \\\n  -d '<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n  <stringListWrapper>\n    <strings>/public</strings>\n    <strings>/home/admin</strings>\n    <strings>/etc</strings>\n  </stringListWrapper>'\n```\n","requestBody":{"required":true,"description":"Collection of Strings containing the paths to be checked.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StringListWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/StringListWrapper"}}}},"responses":{"200":{"description":"Successfully retrieved the permissions of the given paths.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/SettingsWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/SettingsWrapper"}}}},"500":{"description":"Unable to retrieve the permissions of the given paths due to some other error."}}}}}}
````

## Get repository tree

> Retrieve the recursive list of files from root of the repository based on the filters provided.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/files/tree?showHidden=false\&filter=\*|FILES&\_=1389042244670\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/files/tree?showHidden=false\\&filter=\\*|FILES>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - File Resource","description":"This service provides comprehensive file management operations including upload, download, delete, permissions, and metadata management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileTreeDto":{"type":"object","description":"Repository file tree structure","properties":{"file":{"$ref":"#/components/schemas/RepositoryFileDto"},"children":{"type":"array","description":"Child files and directories","items":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}}}},"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/repo/files/tree":{"get":{"tags":["File Management APIs - File Resource"],"summary":"Get repository tree","produces":["application/xml","application/json"],"description":"Retrieve the recursive list of files from root of the repository based on the filters provided.\n\n**Example Request:**\n```\nGET pentaho/api/repo/files/tree?showHidden=false&filter=*|FILES&_=1389042244670\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/files/tree?showHidden=false&filter=*|FILES\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"depth","in":"query","required":false,"description":"How many level should the search go.","schema":{"type":"integer"}},{"name":"filter","in":"query","required":false,"description":"Filter to be applied for search. The filter can be broken down into 3 parts; File types, Child Node\nFilter, and Member Filters. Each part is separated with a pipe (|) character.\n\nFile Types are represented by a word phrase. This phrase is recognized as a file type phrase and processed\naccordingly. Valid File Type word phrases include \"FILES\", \"FOLDERS\", and \"FILES_FOLDERS\" and denote\nwhether to return files, folders, or both files and folders, respectively.\n\nThe Child Node Filter is a list of allowed names of files separated by the pipe (|) character. Each file\nname in the filter may be a full name or a partial name with one or more wildcard characters (\"*\"). The\nfilter does not apply to root node.\n\nThe Member Filter portion of the filter parameter allows the caller to specify which properties of the\nmetadata to return. Member Filters start with \"includeMembers=\" or \"excludeMembers=\" followed by a list of\ncomma separated field names that are to be included in, or, excluded from, the list. Valid field names can\nbe found in org.pentaho.platform.repository2.unified.webservices#RepositoryFileAdapter.\nOmission of a member filter will return all members. It is invalid to both and includeMembers= and an\nexcludeMembers= clause in the same service call.\n","schema":{"type":"string"}},{"name":"showHidden","in":"query","required":false,"description":"Include or exclude hidden files from the file list.","schema":{"type":"boolean"}},{"name":"includeAcls","in":"query","required":false,"description":"Include permission information about the file in the output.","schema":{"type":"boolean","default":false}}],"responses":{"200":{"description":"Successfully retrieved the list of files from root of the repository. A RepositoryFileTreeDto object containing the files at the root of the repository. Will return files but not folders under the \"/\" folder. The fields returned will include the name, filesize, description, id and title.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}},"application/xml":{"schema":{"$ref":"#/components/schemas/RepositoryFileTreeDto"}}}},"404":{"description":"Invalid parameters."},"500":{"description":"Server Error."}}}}}}
````
