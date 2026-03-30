# Settings

**Source:** [https://developer.wordpress.org/apis/settings/](https://developer.wordpress.org/apis/settings/)



# Settings




## In this article


Table of Contents- Overview
- Function Reference
- Adding Setting Fields
- Adding Settings Sections
- Registering Settings
- Options Form Rendering
- ExampleAdding a settings section with a new field in it
- External References
- Generators
- PHP Class



↑Back to top



## Overview


TheSettings API, added inWordPress 2.7, allows admin pages containing settings forms to be managed semi-automatically. It lets you define settings pages, sections within those pages and fields within the sections.


New settings pages can be registered along with sections and fields inside them. Existing settings pages can also be added to by registering new settings sections or fields inside of them.


Organizing registration and validation of fields still requires some effort from developers using the Settings API, but avoids a lot of complex debugging of underlying options management.


NOTE: When using the Settings API, the form posts towp-admin/options.phpwhich provides fairly strict capabilities checking. Users will needmanage_optionscapability (and in MultiSite will have to be a Super Admin) to submit the form.


The functions are found inwp-admin/includes/plugin.phpandwp-admin/includes/template.php


## Function Reference


Setting Register/Unregister:


- register_setting()
- unregister_setting()


Add Field/Section:


- add_settings_field()
- add_settings_section()


Options Form Rendering:


- settings_fields()
- do_settings_sections()
- do_settings_fields()


Errors:


- add_settings_error()
- get_settings_errors()
- settings_errors()


## Adding Setting Fields


You can add new settings fields (basically, an option in thewp_optionsdatabase table but totally managed for you) to the existing WordPress pages using this function. Your callback function just needs to output the appropriate HTML input and fill it with the old value, the saving will be done behind the scenes. You can create your own sections on existing pages usingadd_settings_section()as described below.


NOTE:You MUST register any options you use withadd_settings_field()or they won’t be saved and updated automatically. See below for details and an example.


```text
add_settings_field( $id, $title, $callback, $page, $section = 'default', $args = array() )
```text
- $id– String for use in the ‘id’ attribute of tags.
- $title– Title of the field.
- $callback– Function that fills the field with the desired inputs as part of the larger form. Name and id of the input should match the $id given to this function. The function should echo its output.
- $page– The type of settings page on which to show the field (general, reading, writing, …).
- $section– The section of the settings page in which to show the box (default or a section you added with add_settings_section, look at the page in the source to see what the existing ones are.)
- $args– Extra arguments passed into the callback function


## Adding Settings Sections


Settings Sections are the groups of settings you see on WordPress settings pages with a shared heading. In your plugin you can add new sections to existing settings pages rather than creating a whole new page. This makes your plugin simpler to maintain and creates fewer new pages for users to learn. You just tell them to change your setting on the relevant existing page.


```text
add_settings_section( $id, $title, $callback, $page );
```text
- $id– String for use in the ‘id’ attribute of tags.
- $title– Title of the section.
- $callback– Function that fills the section with the desired content. The function should echo its output.
- $page– The type of settings page on which to show the section (general, reading, writing, media etc.)


## Registering Settings


```text
register_setting( $option_group, $option_name, $args );
```text
```text
unregister_setting( $option_group, $option_name );
```text
NOTE:register_setting()as well as the above mentionedadd_settings_*()functions should all be called from aadmin_initaction hook callback function. Refer to the “Examples” section below.


## Options Form Rendering


When using the API to add settings to existing options pages, you do not need to be concerned about the form itself, as it has already been defined for the page. When you define a new page from scratch, you need to output a minimal form structure that contains a few tags that in turn output the actual sections and settings for the page.


To display the hidden fields and handle security of your options form, the Settings API provides thesettings_fields()function.settings_fields( $option_group );


$option_group(string) (required):


A settings group name. This must match the group name used inregister_setting(), which is the page slug name on which the form is to appear. Default:None


To display the sections assigned to the page and the settings contained within, the Settings API provides thedo_settings_sections()function.do_settings_sections( $page );


$page(string) (required):


The slug name of the page whose settings sections you want to output. This should match the page name used inadd_settings_section(). Default:None


Thedo_settings_fields()function is provided to output the fields assigned to a particular page and section. You should not call this function directly, rather usedo_settings_sections()to output the Section content as well as the associated fields.


Your options form also needs a submit button. You can use thesubmit_button()function to do this.


Finally, you need to output the HTML <form> tag defining the action destination of options.php and method of POST. Here is an example options form code to generate all the sections and fields added to a page who’s slug name ismy-page:


```text
<form method="POST" action="options.php">
<?php 
settings_fields( 'my-page' ); // pass slug name of page, also referred to in Settings API as option group name
do_settings_sections( 'my-page' );  // pass slug name of page
submit_button(); // submit button
?>
</form>
```text
## Example


### Adding a settings section with a new field in it


```text
<?php 
/**
 * Add all your sections, fields and settings during admin_init
 */
 
function wporg_settings_api_init() {
     // Add the section to reading settings so we can add our
     // fields to it
     add_settings_section(
        'wporg_setting_section',
        'Example settings section in reading',
        'wporg_setting_section_callback_function',
        'reading'
    );
     
     // Add the field with the names and function to use for our new
     // settings, put it in our new section
     add_settings_field(
        'wporg_setting_name',
        'Example setting Name',
        'wporg_setting_callback_function',
        'reading',
        'wporg_setting_section'
    );
     
     // Register our setting so that $_POST handling is done for us and
     // our callback function just has to echo the <input>
     register_setting( 'reading', 'wporg_setting_name' );
 } // wporg_settings_api_init()
 
 add_action( 'admin_init', 'wporg_settings_api_init' );
 
  
/**
 * Settings section callback function
 *
 * This function is needed if we added a new section. This function 
 * will be run at the start of our section
 */
 
 function wporg_setting_section_callback_function() {
     echo '<p>Intro text for our settings section</p>';
 }
 
/*
 * Callback function for our example setting
 *
 * creates a checkbox true/false option. Other types are surely possible
 */
 
 function wporg_setting_callback_function() {
     echo '<input name="wporg_setting_name" id="wporg_setting_name" type="checkbox" value="1" class="code" ' . checked( 1, get_option( 'wporg_setting_name' ), false ) . ' /> <label for="wporg_setting_name">Explanation text</label>';
 }
```text
#### Graphical Representation of where all those code should go



## External References


- The WordPress Settings APIby Konstantin Kovshenin, Oct 23 2012
- Incorporating the Settings API in WordPress Themesby Chip Bennett, Feb 2011
- Settings API Explainedby David Gwyer
- WordPress Settings API Tutorialby Otto
- Handling Plugin Options with register_setting()by Ozh
- Intro to the WordPress Settings APIby BobGneu
- Using The Settings API:Part 1,Part 2bySarah Neuber
- Class Based Settings with WordPressby Francis Yaconiello
- Adding multiple sections on a single settings screenby Mathieu Decaffmeyer
- Adding multiple forms on a single settings screenby Mathieu Decaffmeyer
- The Complete Guide To The WordPress Settings APIby Tom McFarlin, Jan 31st 2012
- WordPress Settings API Cheat Sheetby Kenneth Odle, July 16th 2015


## Generators


- WordPress Settings API (options page) Generator


## PHP Class


- WordPress settings API Class





First published


August 12, 2019


Last updated


November 21, 2022



[PreviousExamplePrevious: Example](https://developer.wordpress.org/apis/security/example/)
[NextShortcodeNext: Shortcode](https://developer.wordpress.org/apis/shortcode/)


