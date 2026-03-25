# Source: https://mantisbt.org/docs/erd/latest.pdf

Title: latest.pdf

URL Source: https://mantisbt.org/docs/erd/latest.pdf

Published Time: Thu, 29 Aug 2019 10:47:11 GMT

Number of Pages: 1

Markdown Content:
## mantis_bug_file_table 

id INT(7) bug_id INT(7) 

title VARCHAR(250) 

description VARCHAR(250) 

diskfile VARCHAR(250) 

filename VARCHAR(250) 

folder VARCHAR(250) 

filesize INT(11) 

file_type VARCHAR(250) 

content LONGBLOB 

date_added INT(10) 

user_id INT(10) 

bugnote_id INT(10) 

## mantis_bug_history_table 

id INT(7) 

user_id INT(7) 

bug_id INT(7) 

field_name VARCHAR(64) 

old_value VARCHAR(255) 

new_value VARCHAR(255) 

type INT(2) 

date_modified INT(10) 

## mantis_bug_monitor_table 

user_id INT(7) bug_id INT(7) 

## mantis_bug_relationship_t… 

id INT(7) source_bug_id INT(7) destination_bug_id INT(7) 

relationship_type INT(2) 

## mantis_bug_revision_ta… 

id INT(10) bug_id INT(10) bugnote_id INT(10) user_id INT(10) 

type INT(10) 

value LONGTEXT 

timestamp INT(10) 

## mantis_bug_tag_table 

bug_id INT(10) tag_id INT(10) user_id INT(10) 

date_attached INT(10) 

## mantis_bug_text_table 

id INT(7) 

description TEXT 

steps_to_reproduce TEXT 

additional_information TEXT 

## mantis_bugnote_table 

id INT(7) bug_id INT(7) reporter_id INT(7) bugnote_text_id INT(7) 

view_state INT(2) 

note_type INT(7) 

note_attr VARCHAR(250) 

time_tracking INT(10) 

last_modified INT(10) 

date_submitted INT(10) 

## mantis_bugnote_text_t… 

id INT(7) 

note TEXT 

## mantis_category_table 

id INT(10) project_id INT(10) 

user_id INT(10) 

name VARCHAR(128) 

status INT(10) 

## mantis_config_table 

config_id VARCHAR(64) project_id INT(11) user_id INT(11) 

access_reqd INT(11) 

type INT(11) 

value TEXT 

## mantis_custom_field_project_table 

field_id INT(3) project_id INT(7) 

sequence INT(2) 

## mantis_custom_field_string_table 

field_id INT(3) bug_id INT(7) 

value VARCHAR(255) 

text LONGTEXT 

## mantis_custom_field_table 

id INT(3) 

name VARCHAR(64) 

type INT(2) 

possible_values TEXT 

default_value VARCHAR(255) 

valid_regexp VARCHAR(255) 

access_level_r INT(2) 

access_level_rw INT(2) 

length_min INT(3) 

length_max INT(3) 

require_report BOOLEAN 

require_update BOOLEAN 

display_report BOOLEAN 

display_update BOOLEAN 

require_resolved BOOLEAN 

display_resolved BOOLEAN 

display_closed BOOLEAN 

require_closed BOOLEAN 

filter_by BOOLEAN 

## mantis_email_table 

email_id INT(10) 

email VARCHAR(64) 

subject VARCHAR(250) 

metadata TEXT 

body TEXT 

submitted INT(10) 

## mantis_filters_table 

id INT(7) user_id INT(7) project_id INT(7) 

is_public TINYINT(1) 

name VARCHAR(64) 

filter_string TEXT 

## mantis_news_table 

id INT(7) project_id INT(7) poster_id INT(7) 

view_state INT(2) 

announcement INT(1) 

headline VARCHAR(64) 

body TEXT 

last_modified INT(10) 

date_posted INT(10) 

## mantis_plugin_ta… 

basename VARCHAR(40) 

enabled BOOLEAN 

protected BOOLEAN 

priority INT(10) 

## mantis_project_file_table 

id INT(7) project_id INT(7) 

title VARCHAR(250) 

description VARCHAR(250) 

diskfile VARCHAR(250) 

filename VARCHAR(250) 

folder VARCHAR(250) 

filesize INT(11) 

file_type VARCHAR(250) 

content LONGBLOB 

date_added INT(10) 

user_id INT(10) 

## mantis_project_hierarchy_table 

child_id INT(10) 

parent_id INT(10) 

inherit_parent BOOLEAN 

## mantis_project_user_list_table 

project_id INT(7) user_id INT(7) 

access_level INT(2) 

## mantis_project_version_table 

id INT(7) project_id INT(7) 

version VARCHAR(64) 

description TEXT 

released BOOLEAN 

obsolete BOOLEAN 

date_order INT(10) 

## mantis_sponsorship_table 

id INT(7) bug_id INT(7) user_id INT(7) 

amount INT(7) 

logo VARCHAR(128) 

url VARCHAR(128) 

paid INT(1) 

date_submitted INT(10) 

last_updated INT(10) 

## mantis_tag_table 

id INT(10) user_id INT(10) 

name VARCHAR(100) 

description LONGTEXT 

date_created INT(10) 

date_updated INT(10) 

## mantis_tokens_t… 

id INT(11) owner INT(11) 

type INT(11) 

value TEXT 

timestamp INT(10) 

expiry INT(10) 

## mantis_user_pref_table 

id INT(7) user_id INT(7) project_id INT(7) 

default_profile INT(7) 

default_project INT(7) 

refresh_delay INT(4) 

redirect_delay INT(11) 

bugnote_order VARCHAR(4) 

email_on_new BOOLEAN 

email_on_assigned BOOLEAN 

email_on_feedback BOOLEAN 

email_on_resolved BOOLEAN 

email_on_closed BOOLEAN 

email_on_reopened BOOLEAN 

email_on_bugnote BOOLEAN 

email_on_status BOOLEAN 

email_on_priority BOOLEAN 

email_on_priority_min_severity INT(2) 

email_on_status_min_severity INT(2) 

email_on_bugnote_min_severity INT(2) 

email_on_reopened_min_severity INT(2) 

email_on_closed_min_severity INT(2) 

email_on_resolved_min_severity INT(2) 

email_on_feedback_min_severity INT(2) 

email_on_assigned_min_severity INT(2) 

email_on_new_min_severity INT(2) 

email_bugnote_limit INT(2) 

language VARCHAR(32) 

timezone VARCHAR(32) 

## mantis_user_print_pref_table 

user_id INT(7) 

print_pref VARCHAR(64) 

## mantis_user_profile_table 

id INT(7) user_id INT(7) 

platform VARCHAR(32) 

os VARCHAR(32) 

os_build VARCHAR(32) 

description TEXT 

## Entity-Relationship Diagram for MantisBT 2.23.0 and later (schema v210), revision 1 Copyright (c) 2016-2019 MantisBT team - mantisbt-dev@lists.sourceforge.net - https://mantisbt.org 

## mantis_api_token_table 

id INT(10) user_id INT(11) 

name VARCHAR(128) 

hash VARCHAR(128) 

date_created INT(10) 

date_used INT(10) 

## mantis_bug_table 

id INT(7) project_id INT(7) 

reporter_id INT(7) 

handler_id INT(7) 

duplicate_id INT(7) 

priority VARCHAR(32) 

severity VARCHAR(32) 

reproducibility VARCHAR(32) 

status VARCHAR(32) 

resolution VARCHAR(32) 

projection VARCHAR(32) 

eta VARCHAR(32) bug_text_id INT(7) 

os VARCHAR(32) 

os_build VARCHAR(32) 

platform VARCHAR(32) 

version VARCHAR(64) 

fixed_in_version VARCHAR(64) 

build VARCHAR(32) 

profile_id INT(7) 

view_state INT(2) 

summary VARCHAR(128) 

sponsorship_total INT(7) 

sticky TINYINT(1) 

target_version VARCHAR(64) 

category_id INT(10) 

date_submitted INT(10) 

due_date INT(10) 

last_updated INT(10) 

## mantis_project_table 

id INT(7) 

name VARCHAR(128) 

status VARCHAR(32) 

enabled BOOLEAN 

view_state VARCHAR(32) 

access_min INT(2) 

file_path VARCHAR(250) 

description TEXT 

category_id INT(10) 

inherit_global BOOLEAN 

## mantis_user_table 

id INT(7) 

username VARCHAR(191) 

realname VARCHAR(191) 

email VARCHAR(191) 

password VARCHAR(64) 

enabled BOOLEAN 

protected BOOLEAN 

access_level VARCHAR(32) 

login_count INT(11) 

lost_password_request_count INT(2) 

failed_login_count INT(2) 

cookie_string VARCHAR(64) 

last_visit INT(10) 

date_created INT(10)
