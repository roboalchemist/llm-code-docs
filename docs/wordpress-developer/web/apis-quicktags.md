# Quicktags

**Source:** [https://developer.wordpress.org/apis/quicktags/](https://developer.wordpress.org/apis/quicktags/)



# Quicktags




## In this article


Table of Contents- Description
- History
- Usage
- Parameters
- Return Values
- ExamplesModern exampleAnother modern exampleTraditional example
- Default Quicktags
- Source File



↑Back to top



## Description


The Quicktags API allows you to include additional buttons in the Text (HTML) mode of the WordPress Classic editor.



## History


This API was introduced inWordPress 3.3.


## Usage


```text
QTags.addButton( id, display, arg1, arg2, access_key, title, priority, instance, object );
```text
## Parameters


- id(string) (required):The html id for the button. Default:None
- display(string) (required):The html value for the button. Default:None
- arg1(string) (required):Either a starting tag to be inserted like “<span>” or a callback that is executed when the button is clicked. Default:None
- arg2(string) (optional):Ending tag like “</span>”. Leave empty if tag doesn’t need to be closed (i.e. “<hr />”). Default:None
- access_key(string) (optional):Deprecated and Not used.Shortcut access key for the button. Default:None
- title(string) (optional):The html title value for the button. Default:None
- priority(int) (optional):A number representing the desired position of the button in the toolbar. 1 – 9 = first, 11 – 19 = second, 21 – 29 = third, etc. Default:None
- instance(string) (optional):Limit the button to a specific instance of Quicktags, add to all instances if not present. Default:None
- object(attr) (optional):Used to pass additional attributes. Currently supportsariaLabelandariaLabelClose(for “close tag” state)


## Return Values


(mixed) Null or the button object that is needed for back-compat.


## Examples


Below examples would add HTML buttons to the default Quicktags in the Text editor.


### Modern example


This example uses the inline JS API to add the JavaScript when quicktags are enqueued.


```text
/**
 * Add a paragraph tag button to the quicktags toolbar
 *
 * @return void
 */
function wporg_add_quicktag_paragraph() {
    wp_add_inline_script(
        'quicktags',
        "QTags.addButton( 'eg_paragraph_v2', 'p_v2', '<p>', '</p>', '', 'Paragraph tag v2', 2, '', { ariaLabel: 'Paragraph', ariaLabelClose: 'Close Paragraph tag' });"
    );
}
add_action( 'admin_enqueue_scripts', 'wporg_add_quicktag_paragraph' );
```text
### Another modern example


In this example,


1. Enqueue a script using the proper WordPress functionwp_enqueue_script.
1. Call any JavaScript that you want to fire when or after the QuickTag was clicked inside the QuickTag call-back.


#### Enqueue the script


Put below codes into active theme’sfunctions.php.


```text
function enqueue_quicktag_script(){
    wp_enqueue_script( 'your-handle', get_template_directory_uri() . '/editor-script.js', array( 'jquery', 'quicktags' ), '1.0.0', true );
}
add_action( 'admin_enqueue_scripts', 'enqueue_quicktag_script' );
```text
#### The JavaScript itself


Create new fileeditor-scriptand save under the active theme directory.


```text
QTags.addButton( 'eg_paragraph_v3', 'p_v3', my_callback, '', '', 'Prompted Paragraph tag', 3, '', { ariaLabel: 'Prompted Paragraph' } ); 

function my_callback(){
  var my_stuff = prompt( 'Enter Some Stuff:', '' );
  if ( my_stuff ) {
    QTags.insertContent( '<p>' + my_stuff + '</p>' );
  }
}
```text
### Traditional example


This example manually add hardcoded JavaScript withwp_script_ison the admin footer hook. You should consider to use modern example. See above.


```text
/**
 * Add more buttons to the quicktags HTML editor
 *
 * @return void
 */
function wporg_traditional_add_quicktags() {
    if ( ! wp_script_is( 'quicktags' ) ) {
        return;
    }

    ?>
    <script type="text/javascript">
        QTags.addButton( 'eg_paragraph', 'p', '<p>', '</p>', '', 'Paragraph tag', 1, '', { ariaLabel: 'Paragraph', ariaLabelClose: 'Close Paragraph tag' } );
        QTags.addButton( 'eg_hr', 'hr', '<hr />', '', '', 'Horizontal rule line', 201, '', { ariaLabel: 'Horizontal' } );
        QTags.addButton( 'eg_pre', 'pre', '<pre lang="php">', '</pre>', '', 'Preformatted text tag', 111, '', { ariaLabel: 'Pre', ariaLabelClose: 'Close Pre tag' } );
    </script>
    <?php
}

add_action( 'admin_print_footer_scripts', 'wporg_traditional_add_quicktags', 11 );
```text
Note:


- To avoid a Reference Error we check to see whether or not the ‘quicktags’ script is in use.
- Since WordPress 6.0, the script loading order was changed and the error “QTags is not defined” occurs without 3rd parameter ofadd_action(). Also, you have to specfy the larger number than 10 (ex.11).


The “p” button HTML would be:


```text
<input type="button" id="qt_content_eg_paragraph" class="ed_button button button-small" title="Paragraph tag" aria-label="Paragraph" value="p">
```text
The ID value for each button is automatically prepended with the string qt_content_.



Here is a dump of the docblock fromquicktags.js, it’s pretty useful on it’s own.


```text
/**
 * Main API function for adding a button to Quicktags
 *
 * Adds qt.Button or qt.TagButton depending on the args. The first three args are always required.
 * To be able to add button(s) to Quicktags, your script should be enqueued as dependent
 * on "quicktags" and outputted in the footer. If you are echoing JS directly from PHP,
 * use add_action( 'admin_print_footer_scripts', 'output_my_js', 100 ) or add_action( 'wp_footer', 'output_my_js', 100 )
 *
 * Minimum required to add a button that calls an external function:
 *     QTags.addButton( 'my_id', 'my button', my_callback );
 *     function my_callback() { alert('yeah!'); }
 *
 * Minimum required to add a button that inserts a tag:
 *     QTags.addButton( 'my_id', 'my button', '<span>', '</span>' );
 *     QTags.addButton( 'my_id2', 'my button', '<br />' );
 */
```text
## Default Quicktags


Here are the values of the default Quicktags added by WordPress to the Text editor. ID must be unique. When adding your own buttons, do not use these values:


**ID****Value****Tag Start****Tag End**linklink<a href=”‘ + URL + ‘”></a>strongb<strong></strong>codecode<code></code>deldel<del datetime=”‘ + _datetime + ‘”></del>fullscreenfullscreenemi<em></em>lilit<li></li>nimgimg<img src=”‘ + src + ‘” alt=”‘ + alt + ‘” />olol<ol>n</ol>nnblockb-quotenn<blockquote></blockquote>nninsins<ins datetime=”‘ + _datetime + ‘”></ins>moremore<!–more–>ulul<ul>n</ul>nnspelllookupcloseclose
Some tag values above use variables, such as URL and_datetime, passed from functions.


## Source File


qt.addButton() source is located injs/_enqueues/lib/quicktags.js, during build it’s output inwp-incudes/js/quicktags.jsandwp-includes/js/quicktags.min.js.





First published


August 12, 2019


Last updated


February 27, 2023



[PreviousAuthenticationPrevious: Authentication](https://developer.wordpress.org/apis/making-http-requests/authentication/)
[NextRESTNext: REST](https://developer.wordpress.org/apis/rest/)


