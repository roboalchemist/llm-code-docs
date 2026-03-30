# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/rest-api-requests-list.md

# REST API requests list

Below, you can find a list of endpoints that <http://getint.io> will call during integration configuration and data synchronization.

### During integration configuration <a href="#during-integration-configuration" id="during-integration-configuration"></a>

[/api/now/table/sys\_db\_object?sysparm\_query=sys\_name%3DTask](https://dev57744.service-now.com/api/now/table/sys_db_object?sysparm_query=sys_name%3DTask) - finding task table details.

[/api/now/table/sys\_db\_object?sysparm\_query=super\_class%3De3f033c4c923101091f9f06464832716](https://dev57744.service-now.com/api/now/table/sys_db_object?sysparm_query=super_class%3De3f033c4c923101091f9f06464832716) - finding tables extending task.

[/now/table/sys\_db\_object/fa257b04c927101091f9f06464832798](https://dev57744.service-now.com/api/now/table/sys_db_object/fa257b04c927101091f9f06464832798) - table meta data.

[/now/table/sys\_db\_object/e3f033c4c923101091f9f06464832716](https://dev57744.service-now.com/api/now/table/sys_db_object/e3f033c4c923101091f9f06464832716) - table meta data.

[/api/now/v2/table/sys\_choice?name=task\&element=assignment\_group](https://dev57744.service-now.com/api/now/v2/table/sys_choice?name=task\&element=assignment_group) - fetching e.g. groups for assignment group field.

[/api/now/v2/table/sys\_user\_group?sysparm\_fields=sys\_id,name](https://dev57744.service-now.com/api/now/v2/table/sys_user_group?sysparm_fields=sys_id,name) - fetching user groups.

[/api/now/v2/table/sys\_user?sysparm\_fields=sys\_id,name](https://dev57744.service-now.com/api/now/v2/table/sys_user?sysparm_fields=sys_id,name) - fetching users who can be assigned.

[/api/now/v2/table/sys\_choice?name=incident\&element=state](https://dev57744.service-now.com/api/now/v2/table/sys_choice?name=incident\&element=state) - fetching options for state field.

[/api/now/table/sys\_dictionary?sysparm\_query=name=incident](https://dev57744.service-now.com/api/now/table/sys_dictionary?sysparm_query=name=incident) - fetching fields from incident table.

[/api/now/table/sys\_dictionary?sysparm\_query=name=task](https://dev57744.service-now.com/api/now/table/sys_dictionary?sysparm_query=name=task) - fetching fields for task table.

### During synchronization <a href="#during-synchronization" id="during-synchronization"></a>

[/api/now/v2/table/incident?sysparm\_fields=sys\_id,sys\_updated\_on\&sysparm\_limit=50\&sysparm\_offset=0\&sysparm\_query=%5Esys\_updated\_on%3E%3D2021-03-24+14%3A15%3A03null](https://dev57744.service-now.com/api/now/v2/table/incident?sysparm_fields=sys_id,sys_updated_on\&sysparm_limit=50\&sysparm_offset=0\&sysparm_query=%5Esys_updated_on%3E%3D2021-03-24+14%3A15%3A03null) - fetching incidents.

[/api/now/v2/table/incident](https://dev57744.service-now.com/api/now/v2/table/incident) - creating incidents.

[/api/now/v2/table/incident?sysparm\_query=sys\_id%3D680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/incident?sysparm_query=sys_id%3D680e615edb83a010a1db5385ca9619e3) - fetching incident by sys id.

[/api/now/v2/table/incident/680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/incident/680e615edb83a010a1db5385ca9619e3) - update incident fields, write comments.

[/api/now/v2/table/sys\_journal\_field?sysparm\_limit=100\&element\_id=680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/sys_journal_field?sysparm_limit=100\&element_id=680e615edb83a010a1db5385ca9619e3) - fetching comments for incident.

[/api/now/attachment](https://dev57744.service-now.com/api/now/attachment) - fetching attachments by sys id.

[/api/now/attachment/upload](https://dev57744.service-now.com/api/now/attachment/upload) - upload attachments.

At Getint, we take feedback and customer inquiries seriously. Therefore, if you experience any errors while trying to integrate your app, or if you have any custom requirements, please raise a ticket at our support channel [here.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyO43KDfREuL9Vo6QaCZh%2F19.png?alt=media&#x26;token=32c85bb9-310a-4a64-9a0e-f0d7d5170924" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
