# Source: https://backendless.com/docs/js/backendless_error_codes.html

Title: Backendless Error Codes - Backendless SDK for JavaScript API Documentation

URL Source: https://backendless.com/docs/js/backendless_error_codes.html

Markdown Content:
**Performance**999 Cannot process request - request per second limit has been exhausted
**Data Service**1000 Entity with the specified ID cannot be found
1001 Cannot update object without any properties
1002 Cannot process request, use User Service to create new user entities.
1003 Cannot persist object. Property "id" must be set by the server. Make sure the property is not initialized when saving new object.
1004 Invalid offset. Offset must be greater than 0 and less than the total number of records
1005 Invalid pagesize. Page size cannot be negative. Values greater than 100 will default to 100.
1006 Unable to retrieve data. Query contains invalid object properties.
1007 Unable to update object - invalid data type for properties - XXX.
1009 Unable to retrieve data - unknown entity
1010 Unable to retrieve data - object store is empty
1011 User has no permission to create entity
1012 User has no permission to update entity
1013 User has no permission to find elements in persistence storage.
1014 User has no permission to delete elements from persistence storage.
1015 User has no permission to describe elements from persistence storage.
1017 Invalid where clause
1020 Missing ___class property for entity:
1021 There are no such properties :
1022 All related objects for a property must be of the same type
1023 User has no permission to change permission for the current table.
1024 Cannot update permission: %s
1025 Invalid pagesize. Page size cannot be greater than 100.
1026 The object exceeds maximum permitted serialized size of 10240 bytes
1027 Key can not be null
1028 Expiration time cannot be greater than 7200 seconds
1029 Expected value cannot be null
1030 Value is too large for the 'Long' type
1031 Timestamp should be after the current date
1032 Unable to remove the object. Property objectId is missing.
1034 Unable to retrieve the object. Property objectId is missing.
1035 Unable to retrieve object. Object with the specified primary key does not exist.
1036 Bulk update operation is prohibited for the system columns: %s, %s, ...
1037 Property doesn't exist: %s
1038 Grave character is not allowed in property name: %s, %s, ...
1101 Failed to create entity. Entity with the same primary key already exists
1102 Failed to perform operation due to incomplete primary key. Please, specify all elements of a composite key correctly
1103 This operation is not supported for external data sources
1104 In external data mode the access to internal data tables is denied
1105 Could not delete entity due to its being referenced by parent foreign entity. Please, delete parent entity before deleting this one.
1107 Could not perform operation due to missing primary key
1108 Inspection failed due to a table name collision of an external data table and Users table. Please rename the appropriate table in your external database to resolve this conflict.
1109 Could not connect to external database. Password field may not be empty.
1110 Saving object failed due to incorrect datetime value specified.
1111 In external mode relationship from geo-point cannot be established.
1125 Unable to save entity, table, %s does not exist
1126 Unable to save entity, column %s does not exist
1127 Unable to define relationship, column %s does not exist
1128 Unable to save more than one related object for column %s
1129 Unable to perform operation due to incomplete primary key. Missing column: %s
1130 Unable to perform operation due to incorrectly specified primary key. Column %s is not a part of a composite primary key.
1131 Unable to save entity. The required column %s in table %s is missing
1132 Unable to save entity. Related table %s does not exist.
1133 Unable to inspect tables. %s exceeds maximum allowed size of 45 characters. Please, rename it and try again.
1134 Current user has no permission for %s operation on this table
1135 The entity name 'GeoPoint' is reserved
1136 Bulk update is prohibited for system columns: %s
1137 Unable to save entity, property %s cannot be null
1138 Concurrent schema modification
1139 There is more then one primary key in the schema, use findById with object argument
1140 Remote database unavailable
1141 Table has no primary key
1142 Product has already been changed
1143 Failed to add column
1144 Failed to delete column
1145 Update column failed
1146 Delete all records failed
1147 Add relation failed
1148 Operations in the Users table are prohibited. Use UserProperty service
1149 The maximum number of columns is reached. Adding new column failed
1150 Before creating a relation please add a related table. Adding a relation failed
1151 The maximum number of columns is already reached. Update column failed
1152 Column with the same name already exists
1153 Failed to update relationship
1154 Could not add new table. This name is reserved, please choose another table name
1155 Duplicate entry
1156 Unable to set not null (required) constraint because column already contains nulls. Remove/initialize null entries and try again
1157 Unable to set unique constraints for one-to-many relation
1158 Unable to add index for relation column
1159 Failed to update column with current constraints. Retry without constraints
1160 External database inspection is already in progress
1161 Table with the same name already exists
1162 Fetch of UserDataTable %`s size failed
1163 Operation over system column % is prohibited
1164 Updating column type failed. Changing column to type % will lead to loss of data.
1165 Column '%' cannot be empty
1166 Duplicate entry for column '%'
1167 Could not remove relation. First disable not null (required) relation for column '%'
**Security**2000 Operation is not allowed
2001 Wrong operation
2002 Unable to find application. Check application id and/or API key.
2003 Role does not support for this operation
2004 Wrong data
2005 Could not find role
2006 Role %s already exists in database
2007 Could not assign system role
2008 Could not unassign system role
2009 Wrong domain
2010 Could not get origin domains
2011 Assigning/unassigning a role can be done only from server code
**Users Service**3000 User cannot be logged in
3001 Missing login configuration. Possibly invalid application ID.
3002 User is already logged in from another device/computer. The application is configured to disable multiple concurrent logins with the same user credentials.
3003 Invalid login or password
3004 Wrong social identity for user account
3005 Missing parameter '%s.'
3006 Login or password is missing or null
3007 Unable to logout.
3008 Missing application id and/or API key.
3009 User registration is disabled.
3010 Dynamic property definition is disabled.
3011 Property 'password' is required
3012 Unable to register user. Property '%s' is required
3013 Unable to register user. Missing identity value for '%s'
3014 Unable to register user. External registration failed with message: %s
3015 Missing parameter '%s'
3016 Property name is reserved for system purposes
3017 User property with name '%s' already exists
3018 User with identity '%s' already exists
3019 Missing parameter '%s'
3020 Cannot perform password recovery. Unable to find a user with the specified identity.
3021 Unable to register user due to error: %s
3022 Unable to login user due to error: %s
3023 Unable to logout user due to error: %s
3024 Unable to update user account due to error: %s
3025 Unable to perform password recovery due to error: %s
3026 Unable to retrieve user properties due to error: %s
3027 Unknown error: %s
3028 Unable to update user. User should be logged in
3029 Unable to update user. User accounts can be updated only by admin or by the user himself.
3030 Unable to update user. User cannot be located.
3031 Unable to update user. Dynamic property definition is disabled.
3032 Unable to update user. Could not find user registration properties
3033 Unable to register user. User already exists.
3034 Unable to login. User login is disabled.
3036 Unable to login. User account is locked out due to too many failed logins.
3038 Some of required parameters are null
3039"objectId" is a reserved system property and is not allowed when registering a user.
3040 Provided email has wrong format.
3041 Unable to register user. Missing required property value for '%s'
3042 Event with name '%s' does not exist.
3043 Unable to register user. There are the same properties in request.
3044 Unable to login. Multiple login limit for the same user account has been reached
3045 Unable to update user. Required fields are empty.
3046 There is no default user. Please contact support.
3047 There is no system authenticated role
3048 Session timeout. Url: <...>
3049 Wrong value type for property '%s'.
3050 Password should be string
3051 Confirmation failed
3052 External authentication failed with message '%s'
3053 External authentication failed with message: URL is invalid
3054 Unable to register user. External registration failed with message: URL is invalid
3055 Incorrect password. Operation is not permitted
3056"Could not change user property type, cause there is users with values, that could not be converted to selected type"
3057 Could not find user by id or identity
3058 Could not assign role to user
3059 Could not unassign role from user
3060 Could not approve social account.
3061 Could not find any permitted Facebook application Id.
3062 Requested Facebook application is not permitted.
3063 The number of characters exceeds the limit of 200
3064 Could not get user properties
3065 Property '%s' cannot be deleted
3066 Cannot create task SendTestEmailTask.
3067 Cannot disable 'Confirmation template' while 'Require Email Confirmation' option is enabled.
3068 Cannot enable 'Require Email Confirmation' option while 'Confirmation template' is disabled.
3069 Failed to get default user properties
3070 Default user identity not found
3071 Could not create '%s'
3072 Social user cannot use password
3073 Could not change user property. Required or identity property should not contain 'null' values in existing users.
3074 Cannot enable the 'Require Email Confirmation' option while there is no 'email' user property.
3075"Cannot request password restoration for a user, authorized using a social network"
3076"updated" is a reserved system property and is not allowed while registration
3077"created" is a reserved system property and is not allowed while registration
3078 You can not register user without the 'email' property value while 'Require Email Confirmation' is enabled
3079 Could not delete property 'email' while 'Require Email Confirmation' is enabled
3080 Wrong or unsupported authorized user redirect URL
3081 Could not get roles for the user.
3082 You must confirm email address
3083 Unable to manage user. User should be logged in.
3084 Unable to manage user. User accounts can be managed only by admin or by themselves.
3085 Unable to disable user. User is already disabled.
3086 Unable to enable user. User is already enabled.
3087 Unable to login. User email is not confirmed.
3088 Property 'email' must be selected as 'required' if 'Require Email Confirmation' is enabled
3089 Cannot enable 'Require Email Confirmation' option while 'email' user property is not required
3090 User account is disabled
3091 Session timeout
3092 User already activated
3094 User can be updated only by himself or admin
3095 User can be deleted only by himself or admin
3096 Identity for social user cannot be changed
3097 First login by social user
3098 Bulk update operation is prohibited for identity columns: %s
3099 Registering new user with related properties is not allowed in external data mode
3100 Updating a user with related properties is not allowed in external data mode
3101 Password recovery is disabled
3102 User has already confirmed the email address. Email confirmation will not be sent.
3103 Unable to send email confirmation. The "Require Email Confirmation" option must be enabled in Backendless Console (see the Users > Registration screen)
3104 Unable to send email confirmation - user account with the email cannot be found.
**Geo Service**4000 Unable to add geo point. geo point is NULL.
4001 Unable to remove category. Category cannot be found.
4002 Unable to search/add geo point. Invalid coordinates.
4003 Unable to execute geo query. Offset must be a positive value less than the total number of geo points in the specified categories.
4004 Invalid pagesize. Pagesize must be a positive number not exceeding 100.
4005 Cannot add category. Category name is NULL.
4006 Cannot add category. Category name is empty.
4007 Cannot add category. Category name is ""Default"".
4008 Unable to perform operation. Ambiguous query parameters. Either rectangular coordinates or search radius for a geo point must be set.
4009 User has no permission to add geo point
4010 Unable to add geo point.
4011 User has no permission to get category %s
4012 User has no permission to add geo categories
4013 User has no permission to remove geo categories
4014 Wrong coordinates of a rectangle.
4015 Cannot remove category. Category name is NULL.
4016 Cannot remove category. Category name is empty.
4017 Cannot remove category. Category name is ""Default"".
4018 Metadata key cannot be NULL.
4019 Unable to search geo points. Invalid rectangular area
4020 Unable to search geo points. Coordinates are null.
4021 Get total points failed.
4022 Get total points for category failed.
4023 Radius must be positive.
4024 Geo point with specified id doesn't exist
4025 Specified category doesn't exist.
4026 User has no permission to search in category '%s'
4027 Metadata key cannot be empty.
4028 Metadata key contains invalid characters ( ' or / ): %s
4029 Invalid metadata key - %s. Should start with a letter and contain only letters, digits and _
4030 Invalid file format
4031 Invalid category name: %s
4032 Invalid coordinate. Coordinate must be a number
4034 Complex metadata value should contain property '___class'
4035 The metadata must contain key-value pairs
4036 The property %s doesn't exist
4037 The property 'categories' must be an array
4038 Relation type update is prohibited - property %s must relate to table %s but not %s
4040 Wrong value for the property %s. The property %s has the type %s
4041 To perform relative search, both relativeFindMetadata and relativeFindPercentThreshold must be specified
4042 Users can only be added as related objects by specifying their valid object ID, all other values are ignored. For creating or updating Users please use User API.
4043 Invalid number of the "point" argument. Number must be a positive integer
4044 Invalid value of "dpp" argument. Dpp must belong to the interval (0; 360].
4045 Invalid value of the "size" argument. Size must be a positive integer.
4046 Invalid value of the "objectId" argument. For cluster value must be a positive integer.
4047 Invalid type of the "fence" argument. Type must be CIRCLE or RECT or SHAPE
4048 Invalid amount of the "node" argument. Fence with type CIRCLE must have two nodes
4049 Invalid amount of the "node" argument. Fence with type RECT must have two nodes
4050 Invalid amount of the "node" argument. Fence with type SHAPE must have at least tree nodes
4051 Invalid value of %s
4052 Cannot activate/deactivate GeoFence
4053 Invalid type of GeoFence action. Type must be PUSH or PUBSUB or URL or EVENT
4054 Invalid query value
4055 Invalid push notification configuration. You must fill at least the first three fields in a tab
4056 GeoFence contains objectId
4057 ObjectId from body and from query are different
4058 Invalid value of the "duration" parameter. Duration must be positive
4059 Invalid field name
4060 GeoFence name must be unique in a Backendless app.
4061 Cannot find a geo fence with the name
4062 Geo fence is not active. Geo point tracking is disabled
4063 Geo fence does not have an action configured for the %s event
4064 Invalid HTTP method. Specified method is not supported
4065 Cannot update fence nodes or qualification criteria when fence is active
4066 Your plan does not allow to add more geo fences.
4067 Invalid sortBy parameters. You cannot sort by same field twice at the same time
4068 GeoPoint coordinates not found. Either add them to the request URL or add the Content-Type:application/json header and put the coordinates into the request body.
4080 Cannot accept discovered beacons - discovery mode is turned off.
**Messaging Service**5000 Unable to retrieve device. Invalid device ID.
5001 Unable to cancel device registration. Invalid device ID
5002 Unable to create subscription - unknown messaging channel.
5003 Invalid expiration date
5004 Unable to register device. Invalid expiration date.
5005 Wrong json format for device registration:
5006 Device registration can't be null
5007 User has no permission to publish message
5008 User has no permission to subscribe
5009 Error during subscribing
5010 Can't find message channel with such name for the given application
5011 Unable to register device, deviceId cannot be null
5012 Channel with name '%s' already exists
5030 Invalid publish date
5040 Can't cancel message. Already cancelled or there is no such message
5041 Invalid message for push notification, provide message that could be cast to String
5042 Unable to delete devices
5043 Could not register channel
5044 Channel name contains invalid character
5045 Cannot send email with the default Email Settings. Change the Email Settings in the console and try again
5046 Cannot set email. Invalid email settings
5047 Invalid recipient
5048 You must specify at least one recipient's email address
5049 You must specify at least one body
5050 Unable to complete operation. Backend application is not properly configured. Contact the application developer and report a problem with Email Configuration
5052 Cannot send email. Invalid path for the attachment(s).
5053 Cannot send email. Error: %s
**File Service**6000 Unable to delete file or directory. File or directory cannot be found.
6001 Unable to save file. File name or path contain invalid characters
6002 Unable to write bytes into file %s
6003 Unable to upload file: file already exists
6004 Unable to delete file or directory %s
6005 Unable to encode filename or path to URL format %s
6006 Path contains prohibited symbols
6007 The specified resource was not found
6008 Unable to save file entry to database
6009 Unable to upload file
6010 Corrupted multipart request. Header Content-Type must be set to value multipart/form-data
6011 Corrupted multipart request. File content is absent in request body
6012 Corrupted multipart request. Request body contains more than one file
6013 Mismatch between application-id value in request header and URL
6014 Directory download is not supported
6015 File size must be less or equal 10M
6016 Cannot save files created from byte array when the payload exceeds 2,800,000 bytes
6017 Corrupted text/plain request. File contents have wrong request body
6018 Unable to modify file/folder: file/folder already exists: %s
6019 Unable to modify service file/folder: %s
6020 Unable to copy file to file
6021 Unable to move file to file
6022 Upload into the servercode folder is forbidden: %path_to_file%
6023 File already exists in target directory
6024 Wrong file's operation:%s. You can only use available file's operations: %s
6025 Failed to execute operation
6026 Deletion is forbidden for service file/folder: %s
6027 Upload into git service folder is forbidden: %s
6028 Parameter '%s' cannot be null
6029 Specified resource must be a directory
6030 Cannot sort by property: %s
6031 Write to file failed:
6032 Failed to set file attribute:
**Data model**7000 Failed to get %s from database
7001 Instance of %s does not exist in database
7002 Failed to load %s for %s from database
7003 Relation %s for %s does not exist in database
7004 Failed to remove %s from database
7005 Failed to add %s to database
7006 Failed to update %s to database
7007 Failed to create or update %s to database
7008 Instance of %s already exist in database
7009 Could not create data mapper of %s
7010 Relation %s for %s already exists in database
7011 Failed to find %s in database
7012 Failed to get %s. There is ambiguity.
7013 Failed to create database object
**Common**8000 Invalid value range
8001 Duplicate property: %s
8002 Could not parse request with message: %s
8003 Invalid date format
8004 Parsing input json params failed
8005 Invalid empty param for request
8006 Invalid NULL param for request
8007 Missing parameter '%s'.
8008 Invalid parameter '%s'
8009 Username and Password not accepted
8010 Missing field '%s'
8011 Any error message
8012 Application '%s' already exists
8021 Cannot save email settings whit default UserId
8022 Missing "application-id" header
8044 Cannot save entity with primitive collection property %s
**Management**9000 Wrong application id provided
9001 Could not share data
9002 Could not copy data
9003 Could not share messaging
9004 Could not copy messaging
9005 Invalid developer's login or password
9006 Invalid developer's email.
9007 You are not authorized.
9008 Could not delete system role
9009 Application version with url prefix %s exists
9010 Invalid social identity
9011 Invalid application name
9012 Email already exist
9013 Invalid email format
9014 User already exist
9015 Provided wrong captcha
9017 Specified field %s is too large
9016 Could not change origin domains
9018 Developer's social login is disabled in Standalone Backendless
9019 Could not load developers from database
9020 You try to get access to different application
9021 You can use only latin letters, numbers, and the underscore symbol ('_'). Values cannot begin with a number or underscore
9022 Malformed JWS, unable to decode signature
9023 There is not enough data to make import
9024 Lock has already been acquired
**Config**10000 Could not load config file
10001 Could not get config value
**Billing**11001 Subscription already exists
11002 Subscription not found
11003 Can't upgrade to product plan
11004 Can't upgrade to product component
11005 You have reached the plan's limit. To increase the limit you need to purchase the '{componentName}' function pack from the Marketplace
11006 The transaction cannot be executed. Check your credit card balance
11007 Custom business logic execution has been terminated because the size of code is bigger than allowed in the current payment tier
11008 The number of external hosts for custom business logic in your current configuration exceeds the limit of the free tier
11009 API call limit reached. Limitation of is
11010 The number of geo fences exceeds the limit of the . You must decrease number of geo fences to and then switch to the
11011 Cannot delete the application. Payment is required
11012 Cannot uninstall the function pack. Payment is required
11013 Cannot modify the function pack. Payment is required
11033 The application has been blocked due to exceeding the limit.
**Media Service**12001 MediaTube does not contain such related media
12002 MediaTube does not exist
**Commerce**13001 Google Play developer email is not set
13002 Google service account private key is not set
13003 Request to googleapis.com failed: %s
**Custom Services**14000 Common CustomService exception with developer message
14001 Service not found
14002 Service method not found
14003 Service with name %s already exists.
14003 Service Version with name %s in current service already exist
14003 Service with name %s and version %s already exist
14004 Service invocation failed: %s
14005 Service invocation failed by timeout
14006 Cannot delete a service which is published to marketplace. Remove the service from the marketplace first, then try deleting again
14007 Service already suspended
14008 Access denied
14009 Incorrect number of arguments on method invoke
14010 Can not persist service information
14011 It is not valid description of service.
14012 Can not parse generic service: %s
14013"OperationId" must contain only letters, numbers and underscores, must not begin with number or underscore, must contain only 45 symbols."
14014 Method name in service description file must be unique.
14015 Can't generate SDK code for this service or platform.
14016 Can't change ACL. Internal Error.
14017 Can't create generic service
14018 Can't create imported service
14019 Service Version not found
14020 Can not generate xml schema document for codegen
14021 Debugging utility is disconnected
**Server Code (CodeRunner)**15000 Custom business logic execution has been terminated because it did not complete in permitted time - XX seconds
15001 Wrong host name
**Caching Service**16000 Cannot place object into cache - maximum number of concurrently stored object has been reached. Clear cache or wait till some entries expire
16001 Cannot extend object's life in cache - object does not exist
16002 Timestamp format is invalid
16003 The difference between timestamp and the current time must be greater than zero, equal or less than 7200000 milliseconds (2 hours)
16014 The external host cannot be found
16017 You already have the called method in debug mode. Try later or check you breakpoints.
**Script Service**17000 No script runner is available
17001 The Content-Type header not set. Supported Content-Types are text/plain, application/json and text/xml
17002 The Content-Type %s is not supported. Supported Content-Types are text/plain, application/json and text/xml
17003 Invalid request URI formed
17004 Request method %s is not supported - GET or POST required
17005 Exceeded memory usage limit
17006 Whitespaces are not allowed in script path
**Analytics**18000 Could not find hour data for all day
18001 Start date is not selected or empty. Please, select start date
18002 End date is not selected or empty. Please, select end date
18003 Maximum interval cannot be bigger than 12 month
18004 No MongoDB host available
**"whereClause" Parser**19000 Invalid where clause: %s
19001 Invalid having clause: %s
**Data Connectors**20000 Data Connector not found
20001 Data Connector operation not implemented
20002 The same Data Connector already exists
20003 Can not attach data connector
20004 Can not perform action, an error occurred
20005 Stored procedure not found!
20006 View not found!
20007 Can not perform action. Entity is view.
20008 Can not perform action. Entity is procedure.
20009 An error occurred: %s
20010 Can not activate Data Connector. Table with name %s already exists
20011%s. Click Force Refresh button to update schema
20012 Can not execute DDL operation
20013 Failed to execute stored procedure: %s
20014%s (error from external database)
20015 Cannot delete row from table without primary key
20016 Cannot update row from table without primary key
**Logging**21000 Invalid or missing fields for Log Level or Policy Name.
21001 File policy with name 'FIXED-FILE-SIZE' must have a valid value for "size".
21002 Cannot save log entity.
21003 Invalid Json for save log(s).
21004 Some of required parameters are null
**Bonuses**22000 Current developer is not a member of specified application
22001 Unable to decrease %s points, current balance is %s points
22002 Unable to find developer with email: %s
22003 Unable to find subscriptionId for application with id: %s
**Code Generation**23001 Can't generate code
