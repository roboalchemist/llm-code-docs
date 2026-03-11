# Source: https://backendless.com/docs/js/users_guest_login.html

Title: Guest Login API - Backendless SDK for JavaScript API Documentation

URL Source: https://backendless.com/docs/js/users_guest_login.html

Markdown Content:
Guest Login API - Backendless SDK for JavaScript API Documentation
===============

- [x] - [x]

[Skip to content](https://backendless.com/docs/js/users_guest_login.html#guest-login-api)

[![Image 7: logo](https://backendless.com/docs/js/backendlesslogo.png)](https://backendless.com/docs/js/index.html "Backendless SDK for JavaScript API Documentation")

 Backendless SDK for JavaScript API Documentation

 Guest Login API

[![Image 8: logo](https://backendless.com/docs/js/backendlesslogo.png)](https://backendless.com/docs/js/index.html "Backendless SDK for JavaScript API Documentation") Backendless SDK for JavaScript API Documentation  
- [Welcome](https://backendless.com/docs/js/index.html)
- [Backendless Application](https://backendless.com/docs/js/backendless_application.html)
- [Quick Start Guide](https://backendless.com/docs/js/quick_start_guide.html)
- [Client-side Setup](https://backendless.com/docs/js/setup.html)
- [Blocking and Non-blocking APIs](https://backendless.com/docs/js/sync_and_async_calls.html)
- [Error Handling](https://backendless.com/docs/js/shared_error_handling.html)
- [Backendless Error Codes](https://backendless.com/docs/js/backendless_error_codes.html)
- - [x]  User Service API   User Service API  
  - [Overview](https://backendless.com/docs/js/users_overview.html)
  - [User Registration](https://backendless.com/docs/js/users_user_registration.html)
  - - [x]  Login   Login  
    - [Backendless Login API](https://backendless.com/docs/js/users_login.html)
    - [Validating User Login](https://backendless.com/docs/js/users_validating_user_login.html)
    - [Passwordless Login API](https://backendless.com/docs/js/users_passwordless_login.html)
    - - [x]  Guest Login API  [Guest Login API](https://backendless.com/docs/js/users_guest_login.html) Table of contents  
      - [Overview](https://backendless.com/docs/js/users_guest_login.html#overview)
      - [Anonymous Login API](https://backendless.com/docs/js/users_guest_login.html#anonymous-login-api)
        - [Method](https://backendless.com/docs/js/users_guest_login.html#method)
        - [Return Value](https://backendless.com/docs/js/users_guest_login.html#return-value)

      - [User Session](https://backendless.com/docs/js/users_guest_login.html#user-session)
      - [Persistent Login](https://backendless.com/docs/js/users_guest_login.html#persistent-login)
      - [Guest to Regular User Conversion](https://backendless.com/docs/js/users_guest_login.html#guest-to-regular-user-conversion)
      - [Security Consideration](https://backendless.com/docs/js/users_guest_login.html#security-consideration)
      - [CloudCode Consideration](https://backendless.com/docs/js/users_guest_login.html#cloudcode-consideration)
      - [Guest Accounts Cleanup](https://backendless.com/docs/js/users_guest_login.html#guest-accounts-cleanup)
      - [Codeless Reference](https://backendless.com/docs/js/users_guest_login.html#codeless-reference)

    - - [x]  Social and OAuth2 Logins   Social and OAuth2 Logins  
      - [Initial Configuration](https://backendless.com/docs/js/users_oauth2.html)
      - [Get Authorization URL](https://backendless.com/docs/js/users_get_authorization_url.html)
      - [OAuth2 Login API](https://backendless.com/docs/js/users_oauth2_login_api.html)
      - [OAuth1 Login API - Twitter](https://backendless.com/docs/js/users_oauth1_login_api___twitter.html)

  - [Cookie Based Authorization](https://backendless.com/docs/js/users_cookie_based_authorization.html)
  - - [x]  User Properties   User Properties  
    - [About User Properties](https://backendless.com/docs/js/users_about_user_properties.html)
    - [Retrieving User Properties](https://backendless.com/docs/js/users_retrieving_user_properties.html)
    - [Set User Properties](https://backendless.com/docs/js/users_set_user_properties.html)
    - [Update User Object](https://backendless.com/docs/js/users_update_user_properties.html)

  - - [x]  Enable/Disable User   Enable/Disable User  
    - [About User Statuses](https://backendless.com/docs/js/users_about_user_statuses.html)
    - [Enable User](https://backendless.com/docs/js/users_enable_user.html)
    - [Disable User](https://backendless.com/docs/js/users_disable_user.html)

  - [Remove User](https://backendless.com/docs/js/users_remove_user.html)
  - [Find User By](https://backendless.com/docs/js/users_find_user_by.html)
  - [Create Email Confirmation](https://backendless.com/docs/js/users_create_email_confirmation.html)
  - [Resend Email Confirmation](https://backendless.com/docs/js/users_resend_email_confirmation.html)
  - [Get Current User](https://backendless.com/docs/js/users_get_current_user.html)
  - [Get Current User Token](https://backendless.com/docs/js/users_get_current_user_token.html)
  - [Set Current User](https://backendless.com/docs/js/users_set_current_user.html)
  - [Set Current User Token](https://backendless.com/docs/js/users_set_current_user_token.html)
  - [Password Verification](https://backendless.com/docs/js/users_password_verification.html)
  - [Logout](https://backendless.com/docs/js/users_logout.html)
  - [Password Reset](https://backendless.com/docs/js/users_password_recovery.html)
  - [Retrieve User Schema](https://backendless.com/docs/js/users_retrieve_user_properties.html)
  - [Global Permissions](https://backendless.com/docs/js/users_global_permissions.html)
  - [Asset Container Permissions](https://backendless.com/docs/js/users_asset_container_permissions.html)
  - [Asset Permissions](https://backendless.com/docs/js/users_asset_permissions.html)
  - - [x]  Security And User Roles   Security And User Roles  
    - [About Roles](https://backendless.com/docs/js/users_about_roles.html)
    - [Retrieving Available User Roles](https://backendless.com/docs/js/users_retrieving_available_user_role.html)
    - [Retrieving Users By Role](https://backendless.com/docs/js/users_retrieving_users_by_role.html)
    - [Retrieving User Roles By User ID](https://backendless.com/docs/js/users_retrieving_user_roles_by_user_id.html)
    - [Assigning a Role to a User](https://backendless.com/docs/js/users_assigning_a_role_to_a_user.html)
    - [Unassigning a Role from a User](https://backendless.com/docs/js/users_unassigning_a_role_from_a_user.html)

- - [x]  Database API   Database API  
  - [Overview](https://backendless.com/docs/js/data_overview.html)
  - [About Backendless Database](https://backendless.com/docs/js/data_about_backendless_database.html)
  - - [x]  Data Types   Data Types  
    - [About Data Types](https://backendless.com/docs/js/data_about_data_types.html)
    - [Auto Number (Auto-Increment)](https://backendless.com/docs/js/data_auto_number_auto_increment.html)
    - [Boolean/Checkbox](https://backendless.com/docs/js/data_boolean_checkbox.html)
    - [DateTime](https://backendless.com/docs/js/data_datetime.html)
    - [File Reference](https://backendless.com/docs/js/data_file_reference.html)
    - [Multiple Choice](https://backendless.com/docs/js/data_multiple_choice.html)

  - [Data Object](https://backendless.com/docs/js/data_data_object.html)
  - [Generated Columns](https://backendless.com/docs/js/data_generated_columns.html)
  - - [x]  Saving Data Objects   Saving Data Objects  
    - [Overview](https://backendless.com/docs/js/data_saving_objects_overview.html)
    - [Saving Single Object](https://backendless.com/docs/js/data_single_object_create.html)
    - [Saving Multiple Objects](https://backendless.com/docs/js/data_multiple_objects_bulk_create.html)
    - [Dynamic Schema Definition](https://backendless.com/docs/js/data_dynamic_schema_definition.html)

  - - [x]  Updating Data Objects   Updating Data Objects  
    - [Overview](https://backendless.com/docs/js/data_updating_object_overview.html)
    - [Updating Single Object](https://backendless.com/docs/js/data_single_object_update.html)
    - [Updating Multiple Objects](https://backendless.com/docs/js/data_multiple_objects_bulk_update.html)

  - - [x]  Upsert Operation   Upsert Operation  
    - [Upsert Single Object](https://backendless.com/docs/js/data_upsert_single_object.html)
    - [Upsert Multiple Objects](https://backendless.com/docs/js/data_upsert_multiple_objects.html)

  - - [x]  Deleting Data Objects   Deleting Data Objects  
    - [Deleting Single Object](https://backendless.com/docs/js/data_single_object_deletion.html)
    - [Deleting Multiple Objects](https://backendless.com/docs/js/data_multiple_objects_bulk_delete.html)

  - - [x]  Deep Save   Deep Save  
    - [Overview](https://backendless.com/docs/js/data_deepsaveoverview.html)
    - [Saving New Objects](https://backendless.com/docs/js/data_deepsave_saving_new_objects.html)
    - [Update with Adding a Relation](https://backendless.com/docs/js/data_update_with_adding_a_relation.html)
    - [Update Parent and Child](https://backendless.com/docs/js/data_update_parent_and_child.html)

  - [Retrieving Schema Definition](https://backendless.com/docs/js/data_retrieving_schema_definition.html)
  - [Get Object Count](https://backendless.com/docs/js/data_get_object_count.html)
  - [Basic Object Retrieval](https://backendless.com/docs/js/data_basic_search.html)
  - - [x]  Advanced Object Retrieval   Advanced Object Retrieval  
    - [General API](https://backendless.com/docs/js/data_general_api.html)
    - [Working with Properties](https://backendless.com/docs/js/data_working_wih_properties.html)
    - [Search with the Where Clause](https://backendless.com/docs/js/data_search_with_where_clause.html)
    - [Search with SubQuery](https://backendless.com/docs/js/data_search_with_subquery.html)
    - - [x]  Aggregate Functions   Aggregate Functions  
      - [Overview](https://backendless.com/docs/js/data_aggregate_functions_overview.html)
      - [AVERAGE](https://backendless.com/docs/js/data_average.html)
      - [COUNT](https://backendless.com/docs/js/data_count.html)
      - [SUM](https://backendless.com/docs/js/data_sum.html)
      - [MIN](https://backendless.com/docs/js/data_min.html)
      - [MAX](https://backendless.com/docs/js/data_max.html)
      - [Data Filtering](https://backendless.com/docs/js/data_data_filtering.html)

    - [Retrieving Unique Objects](https://backendless.com/docs/js/data_retrieving_unique_objects_.html)
    - [Using Dates in Search](https://backendless.com/docs/js/data_search_with_dates.html)
    - [Data retrieval with Paging](https://backendless.com/docs/js/data_data_paging.html)
    - [Data retrieval with Sorting](https://backendless.com/docs/js/data_sorting.html)
    - [Search by distance](https://backendless.com/docs/js/data_search_by_distance.html)

  - [Relations Overview](https://backendless.com/docs/js/data_relations.html)
  - - [x]  Relations API (Set/Add)   Relations API (Set/Add)  
    - [Overview](https://backendless.com/docs/js/data_relation_add_set_overview_js.html)
    - [Set Relation with objects](https://backendless.com/docs/js/data_set_relation_with_objects.html)
    - [Set Relation using condition](https://backendless.com/docs/js/data_set_relation_with_condition.html)
    - [Add Relation with objects](https://backendless.com/docs/js/data_add_relation_with_objects.html)
    - [Add Relation using condition](https://backendless.com/docs/js/data_add_relation_with_condition.html)

  - - [x]  Relations API (Delete)   Relations API (Delete)  
    - [Overview](https://backendless.com/docs/js/data_relation_delete_overview_js.html)
    - [Delete Objects from relation](https://backendless.com/docs/js/data_delete_relation_with_obj2.html)
    - [Delete Relation using condition](https://backendless.com/docs/js/data_delete_relation_with_con2.html)

  - - [x]  Relations (Retrieve)   Relations (Retrieve)  
    - [Overview](https://backendless.com/docs/js/data_relations_retrieve_overview.html)
    - [Single Step Retrieval](https://backendless.com/docs/js/data_single_step_retrieval.html)
    - [Two Steps Retrieval](https://backendless.com/docs/js/data_two_step_retrieval.html)
    - [Retrieval with Relation Depth](https://backendless.com/docs/js/data_retrieval_with_relation_depth.html)
    - [Relation Paging](https://backendless.com/docs/js/data_relation_paging.html)
    - [Inverted Relation Retrieval](https://backendless.com/docs/js/data_inverted_relation_retrieval.html)

  - - [x]  JSON Data   JSON Data  
    - [Overview](https://backendless.com/docs/js/data_json_overview.html)
    - [Declaring JSON Columns](https://backendless.com/docs/js/data_declaring_json_columns.html)
    - [JSON Path](https://backendless.com/docs/js/data_json_path.html)
    - [Saving JSON Data](https://backendless.com/docs/js/data_saving_json_data.html)
    - [Retrieving JSON Data](https://backendless.com/docs/js/data_retrieving_json_data.html)
    - [JSON Query](https://backendless.com/docs/js/data_json_query.html)
    - [Updating JSON Data](https://backendless.com/docs/js/data_updating_json_data.html)

  - - [x]  Geolocation Data   Geolocation Data  
    - [Overview](https://backendless.com/docs/js/data_spatial_overview.html)
    - [Spatial Data Types](https://backendless.com/docs/js/data_spatial_data_types.html)
    - [Spatial Data Management](https://backendless.com/docs/js/data_spatial_data_management.html)
    - [Spatial Data Retrieval API](https://backendless.com/docs/js/data_spatial_retrieval_api.html)
    - [Spatial Data Create/Update API](https://backendless.com/docs/js/data_spatial_create_update_api.html)
    - [Spatial Data Delete API](https://backendless.com/docs/js/data_spatial_delete_api.html)

  - - [x]  Transactions   Transactions  
    - [Overview](https://backendless.com/docs/js/data_transactions_overview.html)
    - [Unit of Work API](https://backendless.com/docs/js/data_transactions_about_unitofwork.html)
    - [Transaction Isolation](https://backendless.com/docs/js/data_transactions_isolation.html)
    - [Operation Result](https://backendless.com/docs/js/data_transactions_operation_result.html)
    - [Retrieving objects](https://backendless.com/docs/js/data_transactions_retrieving_objects.html)
    - [Saving a single object](https://backendless.com/docs/js/data_transactions_saving_single_object.html)
    - [Saving multiple objects](https://backendless.com/docs/js/data_transactions_saving_multiple_objects.html)
    - [Updating a single object](https://backendless.com/docs/js/data_transactions_updating_single_object.html)
    - [Updating multiple objects](https://backendless.com/docs/js/data_transactions_updating_multiple_objects.html)
    - [Upsert a single object](https://backendless.com/docs/js/data_upsert_a_single_object_transactions.html)
    - [Upsert multiple objects](https://backendless.com/docs/js/data_upsert_multiple_objects_transactions.html)
    - [Deleting a single object](https://backendless.com/docs/js/data_transactions_deleting_single_object.html)
    - [Deleting multiple objects](https://backendless.com/docs/js/data_transactions_deleting_multiple_objects.html)
    - [Transactions and Relations](https://backendless.com/docs/js/data_transactions_and_relations.html)
    - [Setting a relation](https://backendless.com/docs/js/data_transactions_setting_a_relation.html)
    - [Adding to a relation](https://backendless.com/docs/js/data_transactions_adding_to_a_relation.html)
    - [Deleting from a relation](https://backendless.com/docs/js/data_transactions_deleting_from_a_relation.html)

  - [Database Functions](https://backendless.com/docs/js/data_database_functions.html)
  - [Security](https://backendless.com/docs/js/data_security.html)
  - [Permissions API](https://backendless.com/docs/js/data_permissions_api.html)

- - [x]  Hive API   Hive API  
  - [Hive Overview](https://backendless.com/docs/js/hive_overview.html)
  - [Hive Management](https://backendless.com/docs/js/hive_management.html)
  - - [x]  Management API   Management API  
    - [About Management API](https://backendless.com/docs/js/management_api_about.html)
    - [Create Hive](https://backendless.com/docs/js/management_api_create_hive.html)
    - [Rename Hive](https://backendless.com/docs/js/management_api_rename_a_hive.html)
    - [Delete Hive](https://backendless.com/docs/js/management_api_delete_hive.html)
    - [Get Hive Names](https://backendless.com/docs/js/management_api_get_hive_names.html)

  - - [x]  General API   General API  
    - [About General API](https://backendless.com/docs/js/general_api_about.html)
    - [Get Key Names](https://backendless.com/docs/js/general_api_get_key_names.html)
    - [Delete Key](https://backendless.com/docs/js/general_api_delete_a_key.html)
    - [Delete Keys](https://backendless.com/docs/js/general_api_delete_keys.html)
    - [Check If Keys Exist](https://backendless.com/docs/js/general_api_check_if_multiple_keys_exist.html)
    - [Rename Key](https://backendless.com/docs/js/general_api_rename.html)
    - [Set Key Expiration - TTL](https://backendless.com/docs/js/general_api_set_key_expiration_ttl.html)
    - [Set Key Expiration - Unix Time](https://backendless.com/docs/js/general_api_set_key_expiration_unixtime.html)
    - [Get Key Expiration Time](https://backendless.com/docs/js/general_api_get_expiration_time.html)
    - [Clear Key Expiration Time](https://backendless.com/docs/js/general_api_remove_expiration_time.html)
    - [Time Since Last Operation](https://backendless.com/docs/js/general_api_time_since_last_operation.html)
    - [Reset Last Operation Time](https://backendless.com/docs/js/general_api_reset_last_operation_time.html)

  - - [x]  Key-Value API   Key-Value API  
    - [Get Value](https://backendless.com/docs/js/keyvalue_api_get_key.html)
    - [Get Values](https://backendless.com/docs/js/keyvalue_api_get_multiple_keys.html)
    - [Set Key-Value](https://backendless.com/docs/js/keyvalue_api_create_modify_keyvalue.html)
    - [Set Keys and Values](https://backendless.com/docs/js/keyvalue_api_create_modify_multiple_keyvalues.html)
    - [Increment](https://backendless.com/docs/js/keyvalue_api_increment.html)
    - [Decrement](https://backendless.com/docs/js/keyvalue_api_decrement.html)

  - - [x]  List API   List API  
    - [Get Key Items](https://backendless.com/docs/js/list_api_get_data.html)
    - [Insert Before](https://backendless.com/docs/js/list_api_insert.html)
    - [Insert After](https://backendless.com/docs/js/list_api_insert_after.html)
    - [Add First](https://backendless.com/docs/js/list_api_add_first.html)
    - [Add Last](https://backendless.com/docs/js/list_api_add_last.html)
    - [Delete Value](https://backendless.com/docs/js/list_api_remove_values.html)
    - [Delete First](https://backendless.com/docs/js/list_api_remove_and_return_first.html)
    - [Delete Last](https://backendless.com/docs/js/list_api_remove_and_return_last.html)
    - [Length](https://backendless.com/docs/js/list_api_length.html)

  - - [x]  Map API   Map API  
    - [Get All Key-Values](https://backendless.com/docs/js/map_api_get_all_key_value_pairs.html)
    - [Get Specific Key-Values](https://backendless.com/docs/js/map_api_get_key_value_pairs.html)
    - [Get All Keys Names](https://backendless.com/docs/js/map_api_get_all_keys.html)
    - [Get All Values](https://backendless.com/docs/js/map_api_get_all_values.html)
    - [Get Value By Key Name](https://backendless.com/docs/js/map_api_get_value_by_object_key.html)
    - [Check If Exists](https://backendless.com/docs/js/map_api_check_if_exists.html)
    - [Set Values](https://backendless.com/docs/js/map_api_set_data.html)
    - [Set Value By Key Name](https://backendless.com/docs/js/map_api_set_value_by_object_key.html)
    - [Overwrite Current Value](https://backendless.com/docs/js/map_api_overwrite_current_value.html)
    - [Increment](https://backendless.com/docs/js/map_api_increment_decrement_by_object_key.html)
    - [Decrement](https://backendless.com/docs/js/map_api_decrement_by_obj_key.html)
    - [Delete By Key Name](https://backendless.com/docs/js/map_api_delete_by_object_key.html)
    - [Length](https://backendless.com/docs/js/map_api_length.html)

  - - [x]  Set API   Set API  
    - [Get Key Items](https://backendless.com/docs/js/set_api_get_all_values.html)
    - [Get Random Values](https://backendless.com/docs/js/set_api_get_random_values.html)
    - [Delete Random Key Items](https://backendless.com/docs/js/set_api_get_random_values_and_delete.html)
    - [Contains](https://backendless.com/docs/js/set_api_is_member.html)
    - [Add Values](https://backendless.com/docs/js/set_api_add_data.html)
    - [Delete Values](https://backendless.com/docs/js/set_api_remove_values.html)
    - [Difference](https://backendless.com/docs/js/set_api_difference.html)
    - [Intersection](https://backendless.com/docs/js/set_api_intersection.html)
    - [Union](https://backendless.com/docs/js/set_api_union.html)
    - [Length](https://backendless.com/docs/js/set_api_length.html)

  - - [x]  Sorted-Set API   Sorted-Set API  
    - [Add Items](https://backendless.com/docs/js/sorted_set_api_add_items.html)
    - [Increment Score](https://backendless.com/docs/js/sorted_set_api_increment_the_score.html)
    - [Decrement Score](https://backendless.com/docs/js/sorted_set_api_decrement_the_score.html)
    - [Get Random Values](https://backendless.com/docs/js/sorted_set_api_get_random_values.html)
    - [Get Score](https://backendless.com/docs/js/sorted_set_api_get_score.html)
    - [Get Rank](https://backendless.com/docs/js/sorted_set_api_get_rank.html)
    - [Get Values By Rank Range](https://backendless.com/docs/js/sorted_set_api_get_range_of_values_by_rank.html)
    - [Get Values By Score Range](https://backendless.com/docs/js/sorted_set_api_get_range_of_values_by_score.html)
    - [Difference](https://backendless.com/docs/js/sorted_set_api_difference.html)
    - [Intersection](https://backendless.com/docs/js/sorted_set_api_intersection.html)
    - [Union](https://backendless.com/docs/js/sorted_set_api_union.html)
    - [Delete Value(s)](https://backendless.com/docs/js/sorted_set_api_remove_multiple_values.html)
    - [Delete Values With Max Score](https://backendless.com/docs/js/sorted_set_api_remove_values_with_max_score.html)
    - [Delete Values With Min Score](https://backendless.com/docs/js/sorted_set_api_remove_values_with_min_score.html)
    - [Delete Values By Rank Range](https://backendless.com/docs/js/sorted_set_api_remove_range_by_rank.html)
    - [Delete Values By Score Range](https://backendless.com/docs/js/sorted_set_api_remove_range_by_score.html)
    - [Length](https://backendless.com/docs/js/sorted_set_api_length.html)
    - [Length with a Query](https://backendless.com/docs/js/sorted_set_api_count_values_within_score_range.html)

- - [x]  Real-Time Database   Real-Time Database  
  - [Overview](https://backendless.com/docs/js/rt_overview.html)
  - [Handlers, Events and Listeners](https://backendless.com/docs/js/rt_handlers_and_events.html)
  - - [x]  Object Created Event   Object Created Event  
    - [Overview](https://backendless.com/docs/js/rt_created_event_overview.html)
    - [Conditional Delivery of New Objects](https://backendless.com/docs/js/rt_conditional_delivery_create.html)
    - [Unconditional Delivery Listeners](https://backendless.com/docs/js/rt_unconditional_delivery_create.html)
    - [Triggering Create Event](https://backendless.com/docs/js/rt_triggering_an_event_create.html)
    - [Removing Listeners](https://backendless.com/docs/js/rt_removing_listeners.html)

  - - [x]  Object Updated Event   Object Updated Event  
    - [Overview](https://backendless.com/docs/js/rt_updated_event_overview.html)
    - [Conditional Delivery of Updated Objects](https://backendless.com/docs/js/rt_conditional_delivery_update.html)
    - [Unconditional Delivery Listeners](https://backendless.com/docs/js/rt_unconditional_delivery_listeners_update.html)
    - [Triggering Update Event](https://backendless.com/docs/js/rt_trirgering_an_event_update.html)
    - [Removing Listeners](https://backendless.com/docs/js/rt_removing_listeners_update.html)

  - - [x]  Object Upserted Event   Object Upserted Event  
    - [Overview](https://backendless.com/docs/js/rt_overview_upsert.html)
    - [Conditional Delivery of Upserted Objects](https://backendless.com/docs/js/rt_conditional_delivery_of_upserted_objects.html)
    - [Unconditional Delivery Listeners](https://backendless.com/docs/js/rt_unconditional_delivery_listeners.html)
    - [Removing Upsert Listeners](https://backendless.com/docs/js/rt_removing_listeners_upsert.html)

  - - [x]  Object Deleted Event   Object Deleted Event  
    - [Overview](https://backendless.com/docs/js/rt_deleted_event_overview.html)
    - [Conditional Delivery of Deleted Objects](https://backendless.com/docs/js/rt_conditional_delivery_delete.html)
    - [Unconditional Delivery Listeners](https://backendless.com/docs/js/rt_unconditional_delivery_delete.html)
    - [Triggering Delete Event](https://backendless.com/docs/js/rt_trigerring_an_event_delete.html)
    - [Removing Listeners](https://backendless.com/docs/js/rt_removing_listeners_delete.html)

  - - [x]  Relation Change Event   Relation Change Event  
    - [Overview](https://backendless.com/docs/js/rt_overview_relation_change_event.html)
    - [Conditional Delivery Listeners](https://backendless.com/docs/js/rt_conditional_delivery_listeners_relation.html)
    - [Unconditional Delivery Listeners](https://backendless.com/docs/js/rt_unconditional_delivery_listeners_relation.html)
    - [Removing Relation Event Listeners](https://backendless.com/docs/js/rt_removing_relation_event_listeners.html)

  - [Condition Syntax](https://backendless.com/docs/js/rt_condition_query_syntax.html)
  - [Security and Permissions](https://backendless.com/docs/js/rt_security_and_permissions.html)
  - [Connection Management](https://backendless.com/docs/js/ut_connection_management.html)
  - [Cloud Code - Business Logic](https://backendless.com/docs/js/rt_cloud_code___business_logic.html)

- - [x]  Real-Time Messaging   Real-Time Messaging  
  - [Overview](https://backendless.com/docs/js/pubsub_overview.html)
  - [About Messages](https://backendless.com/docs/js/pubsub_about_messages.html)
  - - [x]  Subscription API   Subscription API  
    - [Introduction](https://backendless.com/docs/js/pubsub_subscription_introduction.html)
    - [Channel Subscription](https://backendless.com/docs/js/pubsub_establish_subscription.html)
    - [Receiving Unfiltered Messages](https://backendless.com/docs/js/pubsub_message_listener.html)
    - [Receiving Filtered Messages](https://backendless.com/docs/js/pubsub_message_filtering.html)
    - [Removing Listeners](https://backendless.com/docs/js/pubsub_removing_listeners.html)
    - [Channel State](https://backendless.com/docs/js/pubsub_channel_state.html)

  - - [x]  Publishing API   Publishing API  
    - [General API](https://backendless.com/docs/js/pubsub_general_publish_api.html)
    - [Basic Publish](https://backendless.com/docs/js/pubsub_basic_publish.html)
    - [Publish with Headers](https://backendless.com/docs/js/pubsub_publish_with_headers.html)
    - [Delayed Delivery](https://backendless.com/docs/js/pubsub_delayed_publish.html)
    - [Repeated Publish](https://backendless.com/docs/js/pubsub_repeated_publish.html)
    - [Get Message Status](https://backendless.com/docs/js/pubsub_get_message_status.html)
    - [Cancel Scheduled Message](https://backendless.com/docs/js/pubsub_cancel_scheduled_message.html)

  - - [x]  Pub/Sub Examples   Pub/Sub Examples  
    - [Publish Strings](https://backendless.com/docs/js/pubsub_publish_strings.html)
    - [Publish Custom Type](https://backendless.com/docs/js/pubsub_publish_custom_type.html)
    - [Publish Map/Dictionary](https://backendless.com/docs/js/pubsub_publish_map_dictionary.html)
    - [Publish in the Future](https://backendless.com/docs/js/pubsub_publish_in_the_future.html)
    - [Conditional Pub/Sub](https://backendless.com/docs/js/pubsub_conditional_pub_sub.html)

  - [Cloud Code - Business Logic](https://backendless.com/docs/js/pubsub_cloud_code___business_logic.html)

- - [x]  Email API   Email API  
  - [Overview](https://backendless.com/docs/js/email_overview.html)
  - [Email Settings](https://backendless.com/docs/js/email_settings.html)
  - [Send Basic Emails API](https://backendless.com/docs/js/email_send_basic_smails_api.html)
  - [Email Templates](https://backendless.com/docs/js/email_templates.html)
  - [Send Emails with Templates API](https://backendless.com/docs/js/email_send_email_with_templates_api.html)

- - [x]  Push Notifications   Push Notifications  
  - [Overview](https://backendless.com/docs/js/push_overview.html)
  - [Push Notification Setup (Android)](https://backendless.com/docs/js/push_push_notification_setup_androi.html)
  - [Push Notification Setup (iOS)](https://backendless.com/docs/js/push_push_notification_setup_ios.html)
  - - [x]  Push Notification Management   Push Notification Management  
    - [Overview](https://backendless.com/docs/js/push_management_overview.html)
    - [About Push Templates](https://backendless.com/docs/js/push_about_push_templates.html)
    - [About Button Options](https://backendless.com/docs/js/push_about_button_templates.html)
    - [Android Notification Buttons](https://backendless.com/docs/js/push_android_notification_buttons.html)
    - [iOS Notification Buttons](https://backendless.com/docs/js/push_ios_notification_buttons.html)
    - [About Channel Options](https://backendless.com/docs/js/push_about_channel_templates.html)
    - [About Push Composer](https://backendless.com/docs/js/push_about_push_composer.html)
    - [Notification Content (WHAT)](https://backendless.com/docs/js/push_notification_content.html)
    - [Notification Audience (WHO)](https://backendless.com/docs/js/push_notification_audience.html)
    - [Android Push (OPTIONS)](https://backendless.com/docs/js/push_android_push_options.html)
    - [iOS Push (OPTIONS)](https://backendless.com/docs/js/push_ios_push_options.html)

  - - [x]  Push Notifications API   Push Notifications API  
    - [Overview](https://backendless.com/docs/js/push_publish_push_overview.html)
    - [Device Registration API](https://backendless.com/docs/js/push_device_registration.html)
    - [Cancel Device Registration](https://backendless.com/docs/js/push_cancel_device_registration.html)
    - [Managing Registrations](https://backendless.com/docs/js/push_managing_registrations.html)
    - [Push from Console](https://backendless.com/docs/js/push_push_from_console.html)
    - [Push with API](https://backendless.com/docs/js/push_push_with_api.html)
    - [Push Notification Headers](https://backendless.com/docs/js/push_push_notification_headers.html)
    - [Get Message Status](https://backendless.com/docs/js/push_get_message_status_2.html)
    - [Retrieve Device Registration](https://backendless.com/docs/js/push_retrieve_device_registration.html)
    - [Send Notification from a Push Template](https://backendless.com/docs/js/push_example_notification_from_a_push_template.html)
    - [Example: Basic Push](https://backendless.com/docs/js/push_basic_push_example.html)
    - [Example: Target All Devices for an OS](https://backendless.com/docs/js/push_target_a_group_of_devices_exam.html)
    - [Example: Target Individual Devices](https://backendless.com/docs/js/push_target_specific_devices.html)
    - [Example: Delayed Push](https://backendless.com/docs/js/push_delayed_push.html)

- - [x]  Files API   Files API  
  - [Overview](https://backendless.com/docs/js/files_overview.html)
  - [Handling Files in Console](https://backendless.com/docs/js/file_handling_files_via_console.html)
  - [File Upload](https://backendless.com/docs/js/files_file_upload.html)
  - [Save Files From Byte Arrays](https://backendless.com/docs/js/file_save_files_from_byte_arrays.html)
  - [File Download](https://backendless.com/docs/js/files_file_download.html)
  - [Create a Directory](https://backendless.com/docs/js/file_create_a_file_directory.html)
  - [Renaming a File/Directory](https://backendless.com/docs/js/file_renaming_a_file_directory.html)
  - [Copying a File/Directory](https://backendless.com/docs/js/file_file_copy.html)
  - [Moving a File/Directory](https://backendless.com/docs/js/file_renaming_a_file_director2.html)
  - [Directory Listing](https://backendless.com/docs/js/file_directory_listing.html)
  - [Get Files Count](https://backendless.com/docs/js/file_get_file_count.html)
  - [Deleting a File](https://backendless.com/docs/js/files_file_deletion.html)
  - [Deleting a Directory](https://backendless.com/docs/js/files_directory_deletion.html)
  - [Append Data To File](https://backendless.com/docs/js/file_append.html)
  - [Web Hosting](https://backendless.com/docs/js/files_web_hosting.html)
  - [Custom Domain Name](https://backendless.com/docs/js/files_custom_domain_name.html)
  - [Files Security](https://backendless.com/docs/js/files_files_security.html)
  - [Permissions API](https://backendless.com/docs/js/file_permissions_api.html)
  - [Cache and CDN Integration](https://backendless.com/docs/js/file_cache_and_cdn_integration.html)

- - [x]  Logging API   Logging API  
  - [Overview](https://backendless.com/docs/js/ut_logging.html)
  - [Retrieving a Logger](https://backendless.com/docs/js/ut_retrieving_a_logger.html)
  - [Logging a message](https://backendless.com/docs/js/ut_logging_a_message.html)
  - [Configuring log buffer policy](https://backendless.com/docs/js/ut_configuring_log_buffer_policy.html)

- - [x]  Caching API   Caching API  
  - [Overview](https://backendless.com/docs/js/ut_caching_js.html)
  - [Putting data into cache](https://backendless.com/docs/js/ut_putting_data_into_cache_js.html)
  - [Retrieving data from cache](https://backendless.com/docs/js/ut_retrieving_data_from_cache_js.html)
  - [Checking if key exists in cache](https://backendless.com/docs/js/ut_checking_if_key_exists_in_js.html)
  - [Extending the life of object in cache](https://backendless.com/docs/js/ut_extending_objects_life_in_cache_js.html)
  - [Deleting object from cache](https://backendless.com/docs/js/ut_deleting_object_from_cache_js.html)

- - [x]  Atomic Counters API   Atomic Counters API  
  - [Overview](https://backendless.com/docs/js/ut_atomic_counters_api_js.html)
  - [Increment by 1, return previous](https://backendless.com/docs/js/ut_increment_by_1__return_previous_js.html)
  - [Increment by 1, return current](https://backendless.com/docs/js/ut_increment_by_1__return_current_js.html)
  - [Decrement by 1, return previous](https://backendless.com/docs/js/ut_decrement_by_1__return_previous_js.html)
  - [Decrement by 1, return current](https://backendless.com/docs/js/ut_decrement_by_1__return_current_js.html)
  - [Increment by N, return current](https://backendless.com/docs/js/ut_increment_by_n__return_current_js.html)
  - [Increment by N, return previous](https://backendless.com/docs/js/ut_increment_by_n__return_previous_js.html)
  - [Conditional update](https://backendless.com/docs/js/ut_conditional_update_js.html)
  - [Get current counter value](https://backendless.com/docs/js/ut_get_current_counter_value_js.html)
  - [Reset counter](https://backendless.com/docs/js/ut_reset_counter_js.html)

- - [x]  App Management   App Management  
  - [Data Import](https://backendless.com/docs/js/mgmt_import.html)
  - [Email Settings](https://backendless.com/docs/js/mgmt_email_settings.html)
  - [Domain Control (CORS)](https://backendless.com/docs/js/mgmt_cross_origin_requests.html)
  - [Custom Domains](https://backendless.com/docs/js/mgmt_custom_domain.html)
  - [Logging](https://backendless.com/docs/js/mgmt_logging.html)
  - [Landing Pages](https://backendless.com/docs/js/mgmt_landing_pages.html)

- - [x]  Zapier Integration   Zapier Integration  
  - [Integration Overview](https://backendless.com/docs/js/zp_overview.html)
  - [Backendless Triggers](https://backendless.com/docs/js/zp_triggers.html)
  - [Backendless Actions](https://backendless.com/docs/js/zp_actions.html)

 Table of contents  
- [Overview](https://backendless.com/docs/js/users_guest_login.html#overview)
- [Anonymous Login API](https://backendless.com/docs/js/users_guest_login.html#anonymous-login-api)
  - [Method](https://backendless.com/docs/js/users_guest_login.html#method)
  - [Return Value](https://backendless.com/docs/js/users_guest_login.html#return-value)

- [User Session](https://backendless.com/docs/js/users_guest_login.html#user-session)
- [Persistent Login](https://backendless.com/docs/js/users_guest_login.html#persistent-login)
- [Guest to Regular User Conversion](https://backendless.com/docs/js/users_guest_login.html#guest-to-regular-user-conversion)
- [Security Consideration](https://backendless.com/docs/js/users_guest_login.html#security-consideration)
- [CloudCode Consideration](https://backendless.com/docs/js/users_guest_login.html#cloudcode-consideration)
- [Guest Accounts Cleanup](https://backendless.com/docs/js/users_guest_login.html#guest-accounts-cleanup)
- [Codeless Reference](https://backendless.com/docs/js/users_guest_login.html#codeless-reference)

Guest Login API[¶](https://backendless.com/docs/js/users_guest_login.html#guest-login-api "Permanent link")
===========================================================================================================

### Overview[¶](https://backendless.com/docs/js/users_guest_login.html#overview "Permanent link")

Backendless supports anonymous login, which is an operation of creating a "guest" user account. This functionality is useful when your application needs to provide some of its services to users prior to them registering as a fully functional user. For example, consider an application where users can add items to a shopping cart with a subsequent check out. To simplify the user experience, your application may allow adding items to the shopping cart before the user has completed the registration process. At the same time, you may want to have a persistent record in the database for the user with relationships between the user record and the pending order. This can be implemented using the anonymous login.

The process of using anonymous login consists of the following steps:

1. Login the user anonymously using the API documented below;
2. Perform any application specific logic, such as establishing data object relationships with the user data record;
3. Convert the guest user account to a registered user by using the [user registration API](https://backendless.com/docs/js/users_user_registration.html).

When logging in anonymously, Backendless creates a user record in the Users database table. The account (record in the database) is identified by a unique `objectId`, and can be used like any other data object. If your database schema includes relationships between users and other tables, the guest user accounts can benefit from the same relationships.

Important

If the Users table has any validators for any of the columns, the anonymous login operation ignores them. If any of the columns have the "not null" or the NN constraint, Backendless will assign random values for those columns.

### Anonymous Login API[¶](https://backendless.com/docs/js/users_guest_login.html#anonymous-login-api "Permanent link")

#### Method[¶](https://backendless.com/docs/js/users_guest_login.html#method "Permanent link")

```
Backendless.UserService.loginAsGuest(stayLoggedIn): Promise<Backendless.User>;
```

where:

| Argument | Description |
| --- | --- |
| `stayLoggedIn` | Optional parameter. When set to `true` the user session remains persistent on the device. In that case, when the application is re-launched, the session identifier (also known as `user-token`) is re-used by the SDK for all API invocations. For more information see the [User Session section](https://backendless.com/docs/js/users_guest_login.html#user-session) below. Boolean value. |

#### Return Value[¶](https://backendless.com/docs/js/users_guest_login.html#return-value "Permanent link")

The [`BackendlessUser`](https://backendless.com/docs/js/users_about_user_properties.html#backendlessuser-object) object representing the guest user. The object is also stored in the database and is uniquely identified by the `"objectId"` property.

```
{  
  "userStatus":"GUEST",  
  "user-token":"user-token-value",  
  "objectId":"guest-user-objectId"  
}
```

where:

| Argument | Description |
| --- | --- |
| `"user-token-value"` | A string value uniquely identifying guest user's session. The value should be passed to the server as a request header with all subsequent API calls in order to maintain user's session. The name of the request header must be `user-token`. |
| `"guest-user-objectId"` | The `"objectId"` property is a unique identifier assigned by Backendless to the user account. You can see the user account/record in the [Users](https://backendless.com/docs/js/users_about_user_properties.html) table of the Backendless database. Click the Users icon in Backendless Console, select the Users table and locate the object by its `objectId`. |

### User Session[](https://backendless.com/docs/js/users_guest_login.html)[¶](https://backendless.com/docs/js/users_guest_login.html#user-session "Permanent link")

Guest logins are subject to the same session policy as regular logins. To maintain the session, the user-token value returned from the anonymous login API must be sent back to the server with every API call. This is done automatically by Backendless SDKs. Every session has an inactivity timeout which can be configured in Backendless Console. The inactivity timeout is the number of seconds since the last invocation. When the time gap between two invocations is greater then the inactivity timeout, Backendless returns an error.

To configure session inactivity timeout:

1. Login to your account in Backendless Console, select your app and click **Users**, then **Login**.
2. Click the **Enable Session Timeout** toggle.
3. Enter a value for the **Inactivity timeout(sec)** field.
4. Click outside the field to save the value on the server:

![Image 9: session-timeout](https://backendless.com/docs/images/users/session-timeout.zoom49.png)

### Persistent Login[¶](https://backendless.com/docs/js/users_guest_login.html#persistent-login "Permanent link")

Anonymous login API provides the "persistent login" option via the `stayLoggedIn` argument. When the argument is `true`, the information about the user session including `objectId` assigned to the guest user account are stored on the device and can be re-used when the application is re-launched again. In that case, the `BackendlessUser` object representing the existing guest user session must be reconstructed as shown below:

```
const guestUser = new BackendlessUser()

guestUser.setProperty('objectId', Backendless.UserService.loggedInUser())
```

In some cases, you may need to retrieve the guest user object from the database as there may be additional data stored from the previous time the user used the application (for example, you may need to load the contents of the shopping cart). The following code demonstrates how the user object can be retrieved using `objectId` saved on the client-side:

```
const guestUserObjectId = Backendless.UserService.loggedInUser()

Backendless.Data.of( 'Users' ).findById( guestUserObjectId )
   .then( guestUser => console.log( guestUser ) )
   .catch( error => console.log(error) )
```

Client-server session identifying guest user is represented by a special value generated by Backendless called `user-token`. For persistent logins Backendless SDK saves user-token on the client-side so it can be used again when users re-launch your application. However, a special consideration must be made to ensure the user-token (and thus the actual guest user session) is still valid. The token and the session may be invalidated if the time since the last invocation is greater than the session inactivity timeout (see the User Session section above). To ensure the token is still valid, your application should use the API documented on the Login page - see the [Validating User Login section](https://backendless.com/docs/js/users_login.html#validate-user-login) for details.

### Guest to Regular User Conversion[¶](https://backendless.com/docs/js/users_guest_login.html#guest-to-regular-user-conversion "Permanent link")

Guest user accounts created with the Anonymous Login API documented below can be "converted" to regular users using the [User Registration API](https://backendless.com/docs/js/users_user_registration.html). The `BackendlessUser` object used in the registration request must contain the same value for the `objectId` property as the one returned in the response for the Anonymous Login API request. Alternatively, you can use the same `BackendlessUser` object returned from the Anonymous Login. The code below demonstrates how the `BackendlessUser` object should be constructed for the registration API:

```
const guestConversionUser = new Backendless.User()
guestConversionUser.email = 'email of the actual NON guest user'
guestConversionUser.password = 'actual password the user is registering with'
guestConversionUser.objectId = 'objectId received from the guest login API'

Backendless.Users.register(guestConversionUser)
  .then(registeredUser => {
    // guest user has been converted to registered and now can login
  })
  .catch(error => {
    // an error has occurred, the error code can be retrieved with error.code
  })
```

### Security Consideration[¶](https://backendless.com/docs/js/users_guest_login.html#security-consideration "Permanent link")

Every API call handled by Backendless has a security role associated with it. For example, when an API call is made in an app with a logged-in user, Backendless assigns the role of `AuthenticatedUser` to the request. This becomes important as each role has its own permissions for various backend operations thus Backendless can automatically handle how different roles can access your data, files, etc. When your application makes API requests on behalf of a guest user, Backendless assigns special security role to these requests. The role name is `GuestUser`. You can configure global permissions for the role using the **Users**>**Security Roles** screen in Backendless console:

![Image 10: guestuser-role](https://backendless.com/docs/images/users/guestuser-role.zoom44.png)

Permissions for the role for individual data tables, folders/files, messaging channels, geo categories and API services can be configured in the respective sections in Backendless Console.

### CloudCode Consideration[¶](https://backendless.com/docs/js/users_guest_login.html#cloudcode-consideration "Permanent link")

You can use Backendless Cloud Code to inject your own logic and functionality to be executed when Backendless executes API operations. Your code/logic can be added as "event handlers" which run before and/or after Backendless' native API implementation. In cases when some additional logic should be executed before and/or after the Anonymous Login implementation, add an event handler for the `loginAsGuest` event on the **Business Logic**>**Event Handlers** screen in Backendless Console:

![Image 11: loginasguest-eventhandler](https://backendless.com/docs/images/users/loginasguest-eventhandler.zoom46.png)

Your event handler can be implemented with JavaScript, Java or without any code using Backendless' own Codeless technology. For more information see the Cloud Code developer guide ([JavaScript](https://backendless.com/docs/bl-js/bl_event_handlers.html), [Java](https://backendless.com/docs/bl-java/bl_event_handlers.html), [Codeless](https://backendless.com/docs/codeless/codeless_what_is_a_codeless_event_handl.html)).

### Guest Accounts Cleanup[¶](https://backendless.com/docs/js/users_guest_login.html#guest-accounts-cleanup "Permanent link")

As your application uses the anonymous login functionality, it is natural that some guest accounts will be abandoned. This happens when a user starts a session while working with your app and leaves without completing the workflow without creating a permanent user registration. Backendless database runs a routine check for the abandoned guest accounts and purges them from the system. The trigger for the account removal is the expiration of the session associated with the account.

### Codeless Reference[¶](https://backendless.com/docs/js/users_guest_login.html#codeless-reference "Permanent link")

![Image 12: user_service_codeless_guest_login](https://backendless.com/docs/images/users/user_service_codeless_guest_login.zoom85.png)

where:

| Argument | Description |
| --- | --- |
| `stay logged in` | A boolean value requesting user login information to be saved so it can be reused when the application restarts (or page is reloaded). |
| `return user` | Optional parameter. When this option is checked, the operation returns [`BackendlessUser`](https://backendless.com/docs/js/users_about_user_properties.html#backendlessuser-object)object. |

Returns the [`BackendlessUser`](https://backendless.com/docs/js/users_about_user_properties.html#backendlessuser-object) object representing the guest user.

The example below initiates the guest session and returns the `BackendlessUser` object, since the `return user` option is checked.

![Image 13: user_service_codeless_example_login_guest_user](https://backendless.com/docs/images/users/user_service_codeless_example_login_guest_user.zoom87.png)

After the Codeless logic runs, the operation returns the `BackendlessUser` object, but with limited number of properties narrowed down to `"userStatus"`, `"user-token"` and `"objectId"`.

![Image 14: user_service_codeless_example_guest_login](https://backendless.com/docs/images/users/user_service_codeless_example_guest_login.zoom91.png)

where:

| Argument | Description |
| --- | --- |
| `"user-token"` | A string value uniquely identifying guest user's session. The value should be passed to the server as a request header with all subsequent API calls in order to maintain user's session. The name of the request header must be `user-token`. |
| `"objectId"` | The `"objectId"` property is a unique identifier assigned by Backendless to the user account. You can see the user account/record in the [Users](https://backendless.com/docs/js/users_about_user_properties.html) table of the Backendless database. Click the Users icon in Backendless Console, select the Users table and locate the object by its `objectId`. |

 Copyright © 2022 Backendless Corp

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
