# Sanitizing Data

**Source:** [https://developer.wordpress.org/apis/security/sanitizing/](https://developer.wordpress.org/apis/security/sanitizing/)



# Sanitizing Data




## In this article


Table of Contents- Example
- Sanitization functions



↑Back to top



Untrusted data comes from many sources (users, third party sites, even your own database!) and all of it needs to be checked before it’s used.


Remember: Even admins are users, and users will enter incorrect data, either on purpose or accidentally. It’s your job to protect them from themselves.


Sanitizinginput is the process of securing/cleaning/filtering input data. Validation is preferred over sanitization because validation is more specific. But when “more specific” isn’t possible, sanitization is the next best thing.


## Example


Let’s say we have an input field namedtitle:


```
<input id="title" type="text" name="title">
```


We can’t use Validation here because the text field is too general: it can be anything at all. So we sanitize the input data with thesanitize_text_field()function:


```
$title = sanitize_text_field( $_POST['title'] );
update_post_meta( $post->ID, 'title', $title );
```


Behind the scenes,sanitize_text_field()does the following:


1. Checks for invalid UTF-8
1. Converts single less-than characters (<) to entity
1. Strips all tags
1. Removes line breaks, tabs and extra white space
1. Strips octets


## Sanitization functions


There are many functions that will help you sanitize your data.


- sanitize_email()
- sanitize_file_name()
- sanitize_hex_color()
- sanitize_hex_color_no_hash()
- sanitize_html_class()
- sanitize_key()
- sanitize_meta()
- sanitize_mime_type()
- sanitize_option()
- sanitize_sql_orderby()
- sanitize_term()
- sanitize_term_field()
- sanitize_text_field()
- sanitize_textarea_field()
- sanitize_title()
- sanitize_title_for_query()
- sanitize_title_with_dashes()
- sanitize_user()
- sanitize_url()
- wp_kses()
- wp_kses_post()





First published


November 20, 2022


Last updated


May 31, 2023



[PreviousSecurityPrevious: Security](https://developer.wordpress.org/apis/security/)
[NextValidating DataNext: Validating Data](https://developer.wordpress.org/apis/security/data-validation/)


