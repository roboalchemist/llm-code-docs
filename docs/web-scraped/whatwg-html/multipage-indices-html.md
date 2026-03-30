# Source: https://html.spec.whatwg.org/multipage/indices.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/indices.html

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 17 IANA considerations — Table of Contents — References →
Index
Elements
Element content categories
Attributes
Element interfaces
All interfaces
Events
HTTP headers
MIME types
Index

The following sections only cover conforming elements and features.

Elements

This section is non-normative.

List of elements
Element	Description	Categories	Parents†	Children	Attributes	Interface
a	Hyperlink	flow; phrasing*; interactive; palpable	phrasing	transparent*	globals; href; target; download; ping; rel; hreflang; type; referrerpolicy	HTMLAnchorElement
abbr	Abbreviation	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
address	Contact information for a page or article element	flow; palpable	flow	flow*	globals	HTMLElement
area	Hyperlink or dead area on an image map	flow; phrasing	phrasing*	empty	globals; alt; coords; shape; href; target; download; ping; rel; referrerpolicy	HTMLAreaElement
article	Self-contained syndicatable or reusable composition	flow; sectioning; palpable	flow	flow	globals	HTMLElement
aside	Sidebar for tangentially related content	flow; sectioning; palpable	flow	flow	globals	HTMLElement
audio	Audio player	flow; phrasing; embedded; interactive; palpable*	phrasing	source*; track*; transparent*	globals; src; crossorigin; preload; autoplay; loop; muted; controls	HTMLAudioElement
b	Keywords	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
base	Base URL and default target navigable for hyperlinks and forms	metadata	head	empty	globals; href; target	HTMLBaseElement
bdi	Text directionality isolation	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
bdo	Text directionality formatting	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
blockquote	A section quoted from another source	flow; palpable	flow	flow	globals; cite	HTMLQuoteElement
body	Document body	none	html	flow	globals; onafterprint; onbeforeprint; onbeforeunload; onhashchange; onlanguagechange; onmessage; onmessageerror; onoffline; ononline; onpageswap; onpagehide; onpagereveal; onpageshow; onpopstate; onrejectionhandled; onstorage; onunhandledrejection; onunload	HTMLBodyElement
br	Line break, e.g. in poem or postal address	flow; phrasing	phrasing	empty	globals	HTMLBRElement
button	Button control	flow; phrasing; interactive; listed; labelable; submittable; form-associated; palpable	phrasing	phrasing*	globals; command; commandfor; disabled; form; formaction; formenctype; formmethod; formnovalidate; formtarget; name; popovertarget; popovertargetaction; type; value	HTMLButtonElement
canvas	Scriptable bitmap canvas	flow; phrasing; embedded; palpable	phrasing	transparent	globals; width; height	HTMLCanvasElement
caption	Table caption	none	table	flow*	globals	HTMLTableCaptionElement
cite	Title of a work	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
code	Computer code	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
col	Table column	none	colgroup	empty	globals; span	HTMLTableColElement
colgroup	Group of columns in a table	none	table	col*; template*	globals; span	HTMLTableColElement
data	Machine-readable equivalent	flow; phrasing; palpable	phrasing	phrasing	globals; value	HTMLDataElement
datalist	Container for options for combo box control	flow; phrasing	phrasing	phrasing*; option*; script-supporting elements*	globals	HTMLDataListElement
dd	Content for corresponding dt element(s)	none	dl; div*	flow	globals	HTMLElement
del	A removal from the document	flow; phrasing*; palpable	phrasing	transparent	globals; cite; datetime	HTMLModElement
details	Disclosure control for hiding details	flow; interactive; palpable	flow	summary*; flow	globals; name; open	HTMLDetailsElement
dfn	Defining instance	flow; phrasing; palpable	phrasing	phrasing*	globals	HTMLElement
dialog	Dialog box or window	flow	flow	flow	globals; open	HTMLDialogElement
div	Generic flow container, or container for name-value groups in dl elements	flow; palpable; select element inner content elements; optgroup element inner content elements; option element inner content elements	flow; dl; select element inner content elements; optgroup element inner content elements; option element inner content elements	flow select element inner content elements*; optgroup element inner content elements*; option element inner content elements*	globals	HTMLDivElement
dl	Association list consisting of zero or more name-value groups	flow; palpable	flow	dt*; dd*; div*; script-supporting elements	globals	HTMLDListElement
dt	Legend for corresponding dd element(s)	none	dl; div*	flow*	globals	HTMLElement
em	Stress emphasis	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
embed	Plugin	flow; phrasing; embedded; interactive; palpable	phrasing	empty	globals; src; type; width; height; any*	HTMLEmbedElement
fieldset	Group of form controls	flow; listed; form-associated; palpable	flow	legend*; flow	globals; disabled; form; name	HTMLFieldSetElement
figcaption	Caption for figure	none	figure	flow	globals	HTMLElement
figure	Figure with optional caption	flow; palpable	flow	figcaption*; flow	globals	HTMLElement
footer	Footer for a page or section	flow; palpable	flow	flow*	globals	HTMLElement
form	User-submittable form	flow; palpable	flow	flow*	globals; accept-charset; action; autocomplete; enctype; method; name; novalidate; rel; target	HTMLFormElement
h1, h2, h3, h4, h5, h6	Heading	flow; heading; palpable	legend; summary; flow	phrasing	globals	HTMLHeadingElement
head	Container for document metadata	none	html	metadata content*	globals	HTMLHeadElement
header	Introductory or navigational aids for a page or section	flow; palpable	flow	flow*	globals	HTMLElement
hgroup	Heading container	flow; palpable	legend; summary; flow	h1; h2; h3; h4; h5; h6; p; script-supporting elements	globals	HTMLElement
hr	Thematic break	flow; select element inner content elements	flow; select element inner content elements	empty	globals	HTMLHRElement
html	Root element	none	none*	head*; body*	globals	HTMLHtmlElement
i	Alternate voice	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
iframe	Child navigable	flow; phrasing; embedded; interactive; palpable	phrasing	empty	globals; src; srcdoc; name; sandbox; allow; allowfullscreen; width; height; referrerpolicy; loading	HTMLIFrameElement
img	Image	flow; phrasing; embedded; interactive*; form-associated; palpable	phrasing; picture	empty	globals; alt; src; srcset; sizes; crossorigin; usemap; ismap; width; height; referrerpolicy; decoding; loading; fetchpriority	HTMLImageElement
input	Form control	flow; phrasing; interactive*; listed; labelable; submittable; resettable; form-associated; palpable*	phrasing	empty	globals; accept; alpha; alt; autocomplete; checked; colorspace; dirname; disabled; form; formaction; formenctype; formmethod; formnovalidate; formtarget; height; list; max; maxlength; min; minlength; multiple; name; pattern; placeholder; popovertarget; popovertargetaction; readonly; required; size; src; step; type; value; width	HTMLInputElement
ins	An addition to the document	flow; phrasing*; palpable	phrasing	transparent	globals; cite; datetime	HTMLModElement
kbd	User input	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
label	Caption for a form control	flow; phrasing; interactive; palpable	phrasing	phrasing*	globals; for	HTMLLabelElement
legend	Caption for fieldset	none	fieldset; optgroup	phrasing*; heading content	globals	HTMLLegendElement
li	List item	none	ol; ul; menu*	flow	globals; value*	HTMLLIElement
link	Link metadata	metadata; flow*; phrasing*	head; noscript*; phrasing*	empty	globals; href; crossorigin; rel; as; media; hreflang; type; sizes; imagesrcset; imagesizes; referrerpolicy; integrity; blocking; color; disabled; fetchpriority	HTMLLinkElement
main	Container for the dominant contents of the document	flow; palpable	flow*	flow	globals	HTMLElement
map	Image map	flow; phrasing*; palpable	phrasing	transparent; area*	globals; name	HTMLMapElement
mark	Highlight	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
MathML math	MathML root	flow; phrasing; embedded; palpable	phrasing	per [MATHML]	per [MATHML]	Element
menu	Menu of commands	flow; palpable*	flow	li; script-supporting elements	globals	HTMLMenuElement
meta	Text metadata	metadata; flow*; phrasing*	head; noscript*; phrasing*	empty	globals; name; http-equiv; content; charset; media	HTMLMetaElement
meter	Gauge	flow; phrasing; labelable; palpable	phrasing	phrasing*	globals; value; min; max; low; high; optimum	HTMLMeterElement
nav	Section with navigational links	flow; sectioning; palpable	flow	flow	globals	HTMLElement
noscript	Fallback content for script	metadata; flow; phrasing; select element inner content elements; optgroup element inner content elements	head*; phrasing*	varies*	globals	HTMLElement
object	Image, child navigable, or plugin	flow; phrasing; embedded; interactive*; listed; form-associated; palpable	phrasing	transparent	globals; data; type; name; form; width; height	HTMLObjectElement
ol	Ordered list	flow; palpable*	flow	li; script-supporting elements	globals; reversed; start; type	HTMLOListElement
optgroup	Group of options in a list box	select element inner content elements	select; div*	optgroup element inner content elements; legend*	globals; disabled; label	HTMLOptGroupElement
option	Option in a list box or combo box control	select element inner content elements; optgroup element inner content elements	select; datalist; optgroup; div*	text*; option element inner content elements*	globals; disabled; label; selected; value	HTMLOptionElement
output	Calculated output value	flow; phrasing; listed; labelable; resettable; form-associated; palpable	phrasing	phrasing	globals; for; form; name	HTMLOutputElement
p	Paragraph	flow; palpable	flow	phrasing	globals	HTMLParagraphElement
picture	Image	flow; phrasing; embedded; palpable	phrasing	source*; one img; script-supporting elements	globals	HTMLPictureElement
pre	Block of preformatted text	flow; palpable	flow	phrasing	globals	HTMLPreElement
progress	Progress bar	flow; phrasing; labelable; palpable	phrasing	phrasing*	globals; value; max	HTMLProgressElement
q	Quotation	flow; phrasing; palpable	phrasing	phrasing	globals; cite	HTMLQuoteElement
rp	Parenthesis for ruby annotation text	none	ruby	text	globals	HTMLElement
rt	Ruby annotation text	none	ruby	phrasing	globals	HTMLElement
ruby	Ruby annotation(s)	flow; phrasing; palpable	phrasing	phrasing; rt; rp*	globals	HTMLElement
s	Inaccurate text	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
samp	Computer output	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
script	Embedded script	metadata; flow; phrasing; script-supporting	head; phrasing; script-supporting	script, data, or script documentation*	globals; src; type; nomodule; async; defer; crossorigin; integrity; referrerpolicy; blocking; fetchpriority	HTMLScriptElement
search	Container for search controls	flow; palpable	flow	flow	globals	HTMLElement
section	Generic document or application section	flow; sectioning; palpable	flow	flow	globals	HTMLElement
select	List box control	flow; phrasing; interactive; listed; labelable; submittable; resettable; form-associated; palpable	phrasing	select element inner content elements; button*	globals; autocomplete; disabled; form; multiple; name; required; size	HTMLSelectElement
selectedcontent	Mirrors content from an option	none	button	empty	globals	HTMLSelectedContentElement
slot	Shadow tree slot	flow; phrasing	phrasing	transparent	globals; name	HTMLSlotElement
small	Side comment	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
source	Image source for img or media source for video or audio	none	picture; video; audio	empty	globals; type; media; src; srcset; sizes; width; height	HTMLSourceElement
span	Generic phrasing container	flow; phrasing; palpable	phrasing; option element inner content elements*	phrasing	globals	HTMLSpanElement
strong	Importance	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
style	Embedded styling information	metadata	head; noscript*	text*	globals; media; blocking	HTMLStyleElement
sub	Subscript	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
summary	Caption for details	none	details	phrasing; heading content	globals	HTMLElement
sup	Superscript	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
SVG svg	SVG root	flow; phrasing; embedded; palpable	phrasing	per [SVG]	per [SVG]	SVGSVGElement
table	Table	flow; palpable	flow	caption*; colgroup*; thead*; tbody*; tfoot*; tr*; script-supporting elements	globals	HTMLTableElement
tbody	Group of rows in a table	none	table	tr; script-supporting elements	globals	HTMLTableSectionElement
td	Table cell	none	tr	flow	globals; colspan; rowspan; headers	HTMLTableCellElement
template	Template	metadata; flow; phrasing; script-supporting	metadata; phrasing; script-supporting; colgroup*	empty	globals; shadowrootmode; shadowrootdelegatesfocus; shadowrootclonable; shadowrootserializable; shadowrootcustomelementregistry	HTMLTemplateElement
textarea	Multiline text controls	flow; phrasing; interactive; listed; labelable; submittable; resettable; form-associated; palpable	phrasing	text	globals; autocomplete; cols; dirname; disabled; form; maxlength; minlength; name; placeholder; readonly; required; rows; wrap	HTMLTextAreaElement
tfoot	Group of footer rows in a table	none	table	tr; script-supporting elements	globals	HTMLTableSectionElement
th	Table header cell	interactive*	tr	flow*	globals; colspan; rowspan; headers; scope; abbr	HTMLTableCellElement
thead	Group of heading rows in a table	none	table	tr; script-supporting elements	globals	HTMLTableSectionElement
time	Machine-readable equivalent of date- or time-related data	flow; phrasing; palpable	phrasing	phrasing	globals; datetime	HTMLTimeElement
title	Document title	metadata	head	text*	globals	HTMLTitleElement
tr	Table row	none	table; thead; tbody; tfoot	th*; td; script-supporting elements	globals	HTMLTableRowElement
track	Timed text track	none	audio; video	empty	globals; default; kind; label; src; srclang	HTMLTrackElement
u	Unarticulated annotation	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
ul	List	flow; palpable*	flow	li; script-supporting elements	globals	HTMLUListElement
var	Variable	flow; phrasing; palpable	phrasing	phrasing	globals	HTMLElement
video	Video player	flow; phrasing; embedded; interactive; palpable	phrasing	source*; track*; transparent*	globals; src; crossorigin; poster; preload; autoplay; playsinline; loop; muted; controls; width; height	HTMLVideoElement
wbr	Line breaking opportunity	flow; phrasing	phrasing	empty	globals	HTMLElement
autonomous custom elements	Author-defined elements	flow; phrasing; palpable	flow; phrasing	transparent	globals; any, as decided by the element's author	Supplied by the element's author (inherits from HTMLElement)

An asterisk (*) in a cell indicates that the actual rules are more complicated than indicated in the table above.

† Categories in the "Parents" column refer to parents that list the given categories in their content model, not to elements that themselves are in those categories. For example, the a element's "Parents" column says "phrasing", so any element whose content model contains the "phrasing" category could be a parent of an a element. Since the "flow" category includes all the "phrasing" elements, that means the th element could be a parent to an a element.

Element content categories

This section is non-normative.

List of element content categories
Category	Elements	Elements with exceptions
Metadata content	base; link; meta; noscript; script; style; template; title	—
Flow content	a; abbr; address; article; aside; audio; b; bdi; bdo; blockquote; br; button; canvas; cite; code; data; datalist; del; details; dfn; dialog; div; dl; em; embed; fieldset; figure; footer; form; h1; h2; h3; h4; h5; h6; header; hgroup; hr; i; iframe; img; input; ins; kbd; label; map; mark; MathML math; menu; meter; nav; noscript; object; ol; output; p; picture; pre; progress; q; ruby; s; samp; script; search; section; select; slot; small; span; strong; sub; sup; SVG svg; table; template; textarea; time; u; ul; var; video; wbr; autonomous custom elements; Text	area (if it is a descendant of a map element); link (if it is allowed in the body); main (if it is a hierarchically correct main element); meta (if the itemprop attribute is present)
Sectioning content	article; aside; nav; section	—
Heading content	h1; h2; h3; h4; h5; h6; hgroup	—
Phrasing content	a; abbr; audio; b; bdi; bdo; br; button; canvas; cite; code; data; datalist; del; dfn; em; embed; i; iframe; img; input; ins; kbd; label; map; mark; MathML math; meter; noscript; object; output; picture; progress; q; ruby; s; samp; script; select; selectedcontent; slot; small; span; strong; sub; sup; SVG svg; template; textarea; time; u; var; video; wbr; autonomous custom elements; Text	area (if it is a descendant of a map element); link (if it is allowed in the body); meta (if the itemprop attribute is present)
Embedded content	audio; canvas; embed; iframe; img; MathML math; object; picture; SVG svg; video	—
Interactive content	button; details; embed; iframe; label; select; textarea	a (if the href attribute is present); audio (if the controls attribute is present); img (if the usemap attribute is present); input (if the type attribute is not in the Hidden state); video (if the controls attribute is present)
Form-associated elements	button; fieldset; input; label; object; output; select; textarea; img; form-associated custom elements	—
Listed elements	button; fieldset; input; object; output; select; textarea; form-associated custom elements	—
Submittable elements	button; input; select; textarea; form-associated custom elements	—
Resettable elements	input; output; select; textarea; form-associated custom elements	—
Autocapitalize-and-autocorrect inheriting elements	button; fieldset; input; output; select; textarea	—
Labelable elements	button; input; meter; output; progress; select; textarea; form-associated custom elements	—
Palpable content	a; abbr; address; article; aside; b; bdi; bdo; blockquote; button; canvas; cite; code; data; del; details; dfn; div; em; embed; fieldset; figure; footer; form; h1; h2; h3; h4; h5; h6; header; hgroup; i; iframe; img; ins; kbd; label; main; map; mark; MathML math; meter; nav; object; output; p; picture; pre; progress; q; ruby; s; samp; search; section; select; small; span; strong; sub; sup; SVG svg; table; textarea; time; u; var; video; autonomous custom elements	audio (if the controls attribute is present); dl (if the element's children include at least one name-value group); input (if the type attribute is not in the Hidden state); menu (if the element's children include at least one li element); ol (if the element's children include at least one li element); ul (if the element's children include at least one li element); Text that is not inter-element whitespace
Script-supporting elements	script; template	—
select element inner content elements	option; optgroup; hr; script-supporting elements; noscript; div	—
optgroup element inner content elements	option; script-supporting elements; noscript; div	—
option element inner content elements	div	phrasing content except for datalist, object, interactive content, or elements with tabindex
Attributes

This section is non-normative.

List of attributes (excluding event handler content attributes)
Attribute	Element(s)	Description	Value
abbr	th	Alternative label to use for the header cell when referencing the cell in other contexts	Text*
accept	input	Hint for expected file type in file upload controls	Set of comma-separated tokens* consisting of valid MIME type strings with no parameters or audio/*, video/*, or image/*
accept-charset	form	Character encodings to use for form submission	ASCII case-insensitive match for "UTF-8"
accesskey	HTML elements	Keyboard shortcut to activate or focus element	Ordered set of unique space-separated tokens, none of which are identical to another, each consisting of one code point in length
action	form	URL to use for form submission	Valid non-empty URL potentially surrounded by spaces
allow	iframe	Permissions policy to be applied to the iframe's contents	Serialized permissions policy
allowfullscreen	iframe	Whether to allow the iframe's contents to use requestFullscreen()	Boolean attribute
alpha	input	Allow the color's alpha component to be set	Boolean attribute
alt	area; img; input	Replacement text for use when images are not available	Text*
as	link	Destination for a preload request (for rel="preload" and rel="modulepreload")	Preload destination, for rel="preload"; module preload destination, for rel="modulepreload"
async	script	Execute script when available, without blocking while fetching	Boolean attribute
autocapitalize	HTML elements	Recommended autocapitalization behavior (for supported input methods)	"on"; "off"; "none"; "sentences"; "words"; "characters"
autocomplete	form	Default setting for autofill feature for controls in the form	"on"; "off"
autocomplete	input; select; textarea	Hint for form autofill feature	Autofill field name and related tokens*
autocorrect	HTML elements	Recommended autocorrection behavior (for supported input methods)	"on"; "off"; the empty string
autofocus	HTML elements	Automatically focus the element when the page is loaded	Boolean attribute
autoplay	audio; video	Hint that the media resource can be started automatically when the page is loaded	Boolean attribute
blocking	link; script; style	Whether the element is potentially render-blocking	Unordered set of unique space-separated tokens*
charset	meta	Character encoding declaration	"utf-8"
checked	input	Whether the control is checked	Boolean attribute
cite	blockquote; del; ins; q	Link to the source of the quotation or more information about the edit	Valid URL potentially surrounded by spaces
class	HTML elements	Classes to which the element belongs	Set of space-separated tokens
closedby	dialog	Which user actions will close the dialog	"any"; "closerequest"; "none";
color	link	Color to use when customizing a site's icon (for rel="mask-icon")	CSS <color>
colorspace	input	The color space of the serialized color	"limited-srgb"; "display-p3"
cols	textarea	Maximum number of characters per line	Valid non-negative integer greater than zero
colspan	td; th	Number of columns that the cell is to span	Valid non-negative integer greater than zero
command	button	Indicates to the targeted element which action to take.	"toggle-popover"; "show-popover"; "hide-popover"; "close"; "request-close"; "show-modal"; a custom command keyword
commandfor	button	Targets another element to be invoked.	ID*
content	meta	Value of the element	Text*
contenteditable	HTML elements	Whether the element is editable	"true"; "false"; "plaintext-only"; the empty string
controls	audio; video	Show user agent controls	Boolean attribute
coords	area	Coordinates for the shape to be created in an image map	Valid list of floating-point numbers*
crossorigin	audio; img; link; script; video	How the element handles crossorigin requests	"anonymous"; "use-credentials"; the empty string
data	object	Address of the resource	Valid non-empty URL potentially surrounded by spaces
datetime	del; ins	Date and (optionally) time of the change	Valid date string with optional time
datetime	time	Machine-readable value	Valid month string, valid date string, valid yearless date string, valid time string, valid local date and time string, valid time-zone offset string, valid global date and time string, valid week string, valid non-negative integer, or valid duration string
decoding	img	Decoding hint to use when processing this image for presentation	"sync"; "async"; "auto"
default	track	Enable the track if no other text track is more suitable	Boolean attribute
defer	script	Defer script execution	Boolean attribute
dir	HTML elements	The text directionality of the element	"ltr"; "rtl"; "auto"
dir	bdo	The text directionality of the element	"ltr"; "rtl"
dirname	input; textarea	Name of form control to use for sending the element's directionality in form submission	Text*
disabled	button; input; optgroup; option; select; textarea; form-associated custom elements	Whether the form control is disabled	Boolean attribute
disabled	fieldset	Whether the descendant form controls, except any inside legend, are disabled	Boolean attribute
disabled	link	Whether the link is disabled	Boolean attribute
download	a; area	Whether to download the resource instead of navigating to it, and its filename if so	Text
draggable	HTML elements	Whether the element is draggable	"true"; "false"
enctype	form	Entry list encoding type to use for form submission	"application/x-www-form-urlencoded"; "multipart/form-data"; "text/plain"
enterkeyhint	HTML elements	Hint for selecting an enter key action	"enter"; "done"; "go"; "next"; "previous"; "search"; "send"
fetchpriority	img; link; script	Sets the priority for fetches initiated by the element	"auto"; "high"; "low"
for	label	Associate the label with form control	ID*
for	output	Specifies controls from which the output was calculated	Unordered set of unique space-separated tokens consisting of IDs*
form	button; fieldset; input; object; output; select; textarea; form-associated custom elements	Associates the element with a form element	ID*
formaction	button; input	URL to use for form submission	Valid non-empty URL potentially surrounded by spaces
formenctype	button; input	Entry list encoding type to use for form submission	"application/x-www-form-urlencoded"; "multipart/form-data"; "text/plain"
formmethod	button; input	Variant to use for form submission	"GET"; "POST"; "dialog"
formnovalidate	button; input	Bypass form control validation for form submission	Boolean attribute
formtarget	button; input	Navigable for form submission	Valid navigable target name or keyword
headers	td; th	The header cells for this cell	Unordered set of unique space-separated tokens consisting of IDs*
headingoffset	HTML elements	Offsets heading levels for descendants	Valid non-negative integer between 0 and 8
headingreset	HTML elements	Prevents a heading offset computation from traversing beyond the element with the attribute	Boolean attribute
height	canvas; embed; iframe; img; input; object; source (in picture); video	Vertical dimension	Valid non-negative integer
hidden	HTML elements	Whether the element is relevant	"until-found"; "hidden"; the empty string
high	meter	Low limit of high range	Valid floating-point number*
href	a; area	Address of the hyperlink	Valid URL potentially surrounded by spaces
href	link	Address of the hyperlink	Valid non-empty URL potentially surrounded by spaces
href	base	Document base URL	Valid URL potentially surrounded by spaces
hreflang	a; link	Language of the linked resource	Valid BCP 47 language tag
http-equiv	meta	Pragma directive	"content-type"; "default-style"; "refresh"; "x-ua-compatible"; "content-security-policy"
id	HTML elements	The element's ID	Text*
imagesizes	link	Image sizes for different page layouts (for rel="preload")	Valid source size list
imagesrcset	link	Images to use in different situations, e.g., high-resolution displays, small monitors, etc. (for rel="preload")	Comma-separated list of image candidate strings
inert	HTML elements	Whether the element is inert.	Boolean attribute
inputmode	HTML elements	Hint for selecting an input modality	"none"; "text"; "tel"; "email"; "url"; "numeric"; "decimal"; "search"
integrity	link; script	Integrity metadata used in Subresource Integrity checks [SRI]	Text
is	HTML elements	Creates a customized built-in element	Valid custom element name of a defined customized built-in element
ismap	img	Whether the image is a server-side image map	Boolean attribute
itemid	HTML elements	Global identifier for a microdata item	Valid URL potentially surrounded by spaces
itemprop	HTML elements	Property names of a microdata item	Unordered set of unique space-separated tokens consisting of valid absolute URLs, defined property names, or text*
itemref	HTML elements	Referenced elements	Unordered set of unique space-separated tokens consisting of IDs*
itemscope	HTML elements	Introduces a microdata item	Boolean attribute
itemtype	HTML elements	Item types of a microdata item	Unordered set of unique space-separated tokens consisting of valid absolute URLs*
kind	track	The type of text track	"subtitles"; "captions"; "descriptions"; "chapters"; "metadata"
label	optgroup; option; track	User-visible label	Text
lang	HTML elements	Language of the element	Valid BCP 47 language tag or the empty string
list	input	List of autocomplete options	ID*
loading	iframe; img	Used when determining loading deferral	"lazy"; "eager"
loop	audio; video	Whether to loop the media resource	Boolean attribute
low	meter	High limit of low range	Valid floating-point number*
max	input	Maximum value	Varies*
max	meter; progress	Upper bound of range	Valid floating-point number*
maxlength	input; textarea	Maximum length of value	Valid non-negative integer
media	link; meta; source; style	Applicable media	Valid media query list
method	form	Variant to use for form submission	"GET"; "POST"; "dialog"
min	input	Minimum value	Varies*
min	meter	Lower bound of range	Valid floating-point number*
minlength	input; textarea	Minimum length of value	Valid non-negative integer
multiple	input; select	Whether to allow multiple values	Boolean attribute
muted	audio; video	Whether to mute the media resource by default	Boolean attribute
name	button; fieldset; input; output; select; textarea; form-associated custom elements	Name of the element to use for form submission and in the form.elements API	Text*
name	details	Name of group of mutually-exclusive details elements	Text*
name	form	Name of form to use in the document.forms API	Text*
name	iframe; object	Name of content navigable	Valid navigable target name or keyword
name	map	Name of image map to reference from the usemap attribute	Text*
name	meta	Metadata name	Text*
name	slot	Name of shadow tree slot	Text
nomodule	script	Prevents execution in user agents that support module scripts	Boolean attribute
nonce	HTML elements	Cryptographic nonce used in Content Security Policy checks [CSP]	Text
novalidate	form	Bypass form control validation for form submission	Boolean attribute
open	details	Whether the details are visible	Boolean attribute
open	dialog	Whether the dialog box is showing	Boolean attribute
optimum	meter	Optimum value in gauge	Valid floating-point number*
pattern	input	Pattern to be matched by the form control's value	Regular expression matching the JavaScript Pattern production
ping	a; area	URLs to ping	Set of space-separated tokens consisting of valid non-empty URLs
placeholder	input; textarea	User-visible label to be placed within the form control	Text*
playsinline	video	Encourage the user agent to display video content within the element's playback area	Boolean attribute
popover	HTML elements	Makes the element a popover element	"auto"; "manual"; "hint"; the empty string
popovertarget	button; input	Targets a popover element to toggle, show, or hide	ID*
popovertargetaction	button; input	Indicates whether a targeted popover element is to be toggled, shown, or hidden	"toggle"; "show"; "hide"
poster	video	Poster frame to show prior to video playback	Valid non-empty URL potentially surrounded by spaces
preload	audio; video	Hints how much buffering the media resource will likely need	"none"; "metadata"; "auto"; the empty string
readonly	input; textarea	Whether to allow the value to be edited by the user	Boolean attribute
readonly	form-associated custom elements	Affects willValidate, plus any behavior added by the custom element author	Boolean attribute
referrerpolicy	a; area; iframe; img; link; script	Referrer policy for fetches initiated by the element	Referrer policy
rel	a; area	Relationship between the location in the document containing the hyperlink and the destination resource	Unordered set of unique space-separated tokens*
rel	link	Relationship between the document containing the hyperlink and the destination resource	Unordered set of unique space-separated tokens*
required	input; select; textarea	Whether the control is required for form submission	Boolean attribute
reversed	ol	Number the list backwards	Boolean attribute
rows	textarea	Number of lines to show	Valid non-negative integer greater than zero
rowspan	td; th	Number of rows that the cell is to span	Valid non-negative integer
sandbox	iframe	Security rules for nested content	Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of
"allow-downloads"
"allow-forms"
"allow-modals"
"allow-orientation-lock"
"allow-pointer-lock"
"allow-popups"
"allow-popups-to-escape-sandbox"
"allow-presentation"
"allow-same-origin"
"allow-scripts"
"allow-top-navigation"
"allow-top-navigation-by-user-activation"
"allow-top-navigation-to-custom-protocols"

scope	th	Specifies which cells the header cell applies to	"row"; "col"; "rowgroup"; "colgroup"
selected	option	Whether the option is selected by default	Boolean attribute
shadowrootclonable	template	Sets clonable on a declarative shadow root	Boolean attribute
shadowrootcustomelementregistry	template	Enables declarative shadow roots to indicate they will use a custom element registry	Boolean attribute
shadowrootdelegatesfocus	template	Sets delegates focus on a declarative shadow root	Boolean attribute
shadowrootmode	template	Enables streaming declarative shadow roots	"open"; "closed"
shadowrootserializable	template	Sets serializable on a declarative shadow root	Boolean attribute
shape	area	The kind of shape to be created in an image map	"circle"; "default"; "poly"; "rect"
size	input; select	Size of the control	Valid non-negative integer greater than zero
sizes	link	Sizes of the icons (for rel="icon")	Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of sizes*
sizes	img; source	Image sizes for different page layouts	Valid source size list
slot	HTML elements	The element's desired slot	Text
span	col; colgroup	Number of columns spanned by the element	Valid non-negative integer greater than zero
spellcheck	HTML elements	Whether the element is to have its spelling and grammar checked	"true"; "false"; the empty string
src	audio; embed; iframe; img; input; script; source (in video or audio); track; video	Address of the resource	Valid non-empty URL potentially surrounded by spaces
srcdoc	iframe	A document to render in the iframe	The source of an iframe srcdoc document*
srclang	track	Language of the text track	Valid BCP 47 language tag
srcset	img; source	Images to use in different situations, e.g., high-resolution displays, small monitors, etc.	Comma-separated list of image candidate strings
start	ol	Starting value of the list	Valid integer
step	input	Granularity to be matched by the form control's value	Valid floating-point number greater than zero, or "any"
style	HTML elements	Presentational and formatting instructions	CSS declarations*
tabindex	HTML elements	Whether the element is focusable and sequentially focusable, and the relative order of the element for the purposes of sequential focus navigation	Valid integer
target	a; area	Navigable for hyperlink navigation	Valid navigable target name or keyword
target	base	Default navigable for hyperlink navigation and form submission	Valid navigable target name or keyword
target	form	Navigable for form submission	Valid navigable target name or keyword
title	HTML elements	Advisory information for the element	Text
title	abbr; dfn	Full term or expansion of abbreviation	Text
title	input	Description of pattern (when used with pattern attribute)	Text
title	link	Title of the link	Text
title	link; style	CSS style sheet set name	Text
translate	HTML elements	Whether the element is to be translated when the page is localized	"yes"; "no"; the empty string
type	a; link	Hint for the type of the referenced resource	Valid MIME type string
type	button	Type of button	"submit"; "reset"; "button"
type	embed; object; source	Type of embedded resource	Valid MIME type string
type	input	Type of form control	input type keyword
type	ol	Kind of list marker	"1"; "a"; "A"; "i"; "I"
type	script	Type of script	"module"; "importmap"; "speculationrules"; a valid MIME type string that is not a JavaScript MIME type essence match
usemap	img	Name of image map to use	Valid hash-name reference*
value	button; option	Value to be used for form submission	Text
value	data	Machine-readable value	Text*
value	input	Value of the form control	Varies*
value	li	Ordinal value of the list item	Valid integer
value	meter; progress	Current value of the element	Valid floating-point number
width	canvas; embed; iframe; img; input; object; source (in picture); video	Horizontal dimension	Valid non-negative integer
wrap	textarea	How the value of the form control is to be wrapped for form submission	"soft"; "hard"
writingsuggestions	HTML elements	Whether the element can offer writing suggestions or not.	"true"; "false"; the empty string

An asterisk (*) in a cell indicates that the actual rules are more complicated than indicated in the table above.

✔MDN
List of event handler content attributes
Attribute	Element(s)	Description	Value
onafterprint	body	afterprint event handler for Window object	Event handler content attribute
onauxclick	HTML elements	auxclick event handler	Event handler content attribute
onbeforeinput	HTML elements	beforeinput event handler	Event handler content attribute
onbeforematch	HTML elements	beforematch event handler	Event handler content attribute
onbeforeprint	body	beforeprint event handler for Window object	Event handler content attribute
onbeforeunload	body	beforeunload event handler for Window object	Event handler content attribute
onbeforetoggle	HTML elements	beforetoggle event handler	Event handler content attribute
onblur	HTML elements	blur event handler	Event handler content attribute
oncancel	HTML elements	cancel event handler	Event handler content attribute
oncanplay	HTML elements	canplay event handler	Event handler content attribute
oncanplaythrough	HTML elements	canplaythrough event handler	Event handler content attribute
onchange	HTML elements	change event handler	Event handler content attribute
onclick	HTML elements	click event handler	Event handler content attribute
onclose	HTML elements	close event handler	Event handler content attribute
oncommand	HTML elements	command event handler	Event handler content attribute
oncontextlost	HTML elements	contextlost event handler	Event handler content attribute
oncontextmenu	HTML elements	contextmenu event handler	Event handler content attribute
oncontextrestored	HTML elements	contextrestored event handler	Event handler content attribute
oncopy	HTML elements	copy event handler	Event handler content attribute
oncuechange	HTML elements	cuechange event handler	Event handler content attribute
oncut	HTML elements	cut event handler	Event handler content attribute
ondblclick	HTML elements	dblclick event handler	Event handler content attribute
ondrag	HTML elements	drag event handler	Event handler content attribute
ondragend	HTML elements	dragend event handler	Event handler content attribute
ondragenter	HTML elements	dragenter event handler	Event handler content attribute
ondragleave	HTML elements	dragleave event handler	Event handler content attribute
ondragover	HTML elements	dragover event handler	Event handler content attribute
ondragstart	HTML elements	dragstart event handler	Event handler content attribute
ondrop	HTML elements	drop event handler	Event handler content attribute
ondurationchange	HTML elements	durationchange event handler	Event handler content attribute
onemptied	HTML elements	emptied event handler	Event handler content attribute
onended	HTML elements	ended event handler	Event handler content attribute
onerror	HTML elements	error event handler	Event handler content attribute
onfocus	HTML elements	focus event handler	Event handler content attribute
onformdata	HTML elements	formdata event handler	Event handler content attribute
onhashchange	body	hashchange event handler for Window object	Event handler content attribute
oninput	HTML elements	input event handler	Event handler content attribute
oninvalid	HTML elements	invalid event handler	Event handler content attribute
onkeydown	HTML elements	keydown event handler	Event handler content attribute
onkeypress	HTML elements	keypress event handler	Event handler content attribute
onkeyup	HTML elements	keyup event handler	Event handler content attribute
onlanguagechange	body	languagechange event handler for Window object	Event handler content attribute
onload	HTML elements	load event handler	Event handler content attribute
onloadeddata	HTML elements	loadeddata event handler	Event handler content attribute
onloadedmetadata	HTML elements	loadedmetadata event handler	Event handler content attribute
onloadstart	HTML elements	loadstart event handler	Event handler content attribute
onmessage	body	message event handler for Window object	Event handler content attribute
onmessageerror	body	messageerror event handler for Window object	Event handler content attribute
onmousedown	HTML elements	mousedown event handler	Event handler content attribute
onmouseenter	HTML elements	mouseenter event handler	Event handler content attribute
onmouseleave	HTML elements	mouseleave event handler	Event handler content attribute
onmousemove	HTML elements	mousemove event handler	Event handler content attribute
onmouseout	HTML elements	mouseout event handler	Event handler content attribute
onmouseover	HTML elements	mouseover event handler	Event handler content attribute
onmouseup	HTML elements	mouseup event handler	Event handler content attribute
onoffline	body	offline event handler for Window object	Event handler content attribute
ononline	body	online event handler for Window object	Event handler content attribute
onpagehide	body	pagehide event handler for Window object	Event handler content attribute
onpagereveal	body	pagereveal event handler for Window object	Event handler content attribute
onpageshow	body	pageshow event handler for Window object	Event handler content attribute
onpageswap	body	pageswap event handler for Window object	Event handler content attribute
onpaste	HTML elements	paste event handler	Event handler content attribute
onpause	HTML elements	pause event handler	Event handler content attribute
onplay	HTML elements	play event handler	Event handler content attribute
onplaying	HTML elements	playing event handler	Event handler content attribute
onpopstate	body	popstate event handler for Window object	Event handler content attribute
onprogress	HTML elements	progress event handler	Event handler content attribute
onratechange	HTML elements	ratechange event handler	Event handler content attribute
onreset	HTML elements	reset event handler	Event handler content attribute
onresize	HTML elements	resize event handler	Event handler content attribute
onrejectionhandled	body	rejectionhandled event handler for Window object	Event handler content attribute
onscroll	HTML elements	scroll event handler	Event handler content attribute
onscrollend	HTML elements	scrollend event handler	Event handler content attribute
onsecuritypolicyviolation	HTML elements	securitypolicyviolation event handler	Event handler content attribute
onseeked	HTML elements	seeked event handler	Event handler content attribute
onseeking	HTML elements	seeking event handler	Event handler content attribute
onselect	HTML elements	select event handler	Event handler content attribute
onslotchange	HTML elements	slotchange event handler	Event handler content attribute
onstalled	HTML elements	stalled event handler	Event handler content attribute
onstorage	body	storage event handler for Window object	Event handler content attribute
onsubmit	HTML elements	submit event handler	Event handler content attribute
onsuspend	HTML elements	suspend event handler	Event handler content attribute
ontimeupdate	HTML elements	timeupdate event handler	Event handler content attribute
ontoggle	HTML elements	toggle event handler	Event handler content attribute
onunhandledrejection	body	unhandledrejection event handler for Window object	Event handler content attribute
onunload	body	unload event handler for Window object	Event handler content attribute
onvolumechange	HTML elements	volumechange event handler	Event handler content attribute
onwaiting	HTML elements	waiting event handler	Event handler content attribute
onwheel	HTML elements	wheel event handler	Event handler content attribute
Element interfaces

This section is non-normative.

List of interfaces for elements
Element(s)	Interface(s)
a	HTMLAnchorElement : HTMLElement
abbr	HTMLElement
address	HTMLElement
area	HTMLAreaElement : HTMLElement
article	HTMLElement
aside	HTMLElement
audio	HTMLAudioElement : HTMLMediaElement : HTMLElement
b	HTMLElement
base	HTMLBaseElement : HTMLElement
bdi	HTMLElement
bdo	HTMLElement
blockquote	HTMLQuoteElement : HTMLElement
body	HTMLBodyElement : HTMLElement
br	HTMLBRElement : HTMLElement
button	HTMLButtonElement : HTMLElement
canvas	HTMLCanvasElement : HTMLElement
caption	HTMLTableCaptionElement : HTMLElement
cite	HTMLElement
code	HTMLElement
col	HTMLTableColElement : HTMLElement
colgroup	HTMLTableColElement : HTMLElement
data	HTMLDataElement : HTMLElement
datalist	HTMLDataListElement : HTMLElement
dd	HTMLElement
del	HTMLModElement : HTMLElement
details	HTMLDetailsElement : HTMLElement
dfn	HTMLElement
dialog	HTMLDialogElement : HTMLElement
div	HTMLDivElement : HTMLElement
dl	HTMLDListElement : HTMLElement
dt	HTMLElement
em	HTMLElement
embed	HTMLEmbedElement : HTMLElement
fieldset	HTMLFieldSetElement : HTMLElement
figcaption	HTMLElement
figure	HTMLElement
footer	HTMLElement
form	HTMLFormElement : HTMLElement
h1	HTMLHeadingElement : HTMLElement
h2	HTMLHeadingElement : HTMLElement
h3	HTMLHeadingElement : HTMLElement
h4	HTMLHeadingElement : HTMLElement
h5	HTMLHeadingElement : HTMLElement
h6	HTMLHeadingElement : HTMLElement
head	HTMLHeadElement : HTMLElement
header	HTMLElement
hgroup	HTMLElement
hr	HTMLHRElement : HTMLElement
html	HTMLHtmlElement : HTMLElement
i	HTMLElement
iframe	HTMLIFrameElement : HTMLElement
img	HTMLImageElement : HTMLElement
input	HTMLInputElement : HTMLElement
ins	HTMLModElement : HTMLElement
kbd	HTMLElement
label	HTMLLabelElement : HTMLElement
legend	HTMLLegendElement : HTMLElement
li	HTMLLIElement : HTMLElement
link	HTMLLinkElement : HTMLElement
main	HTMLElement
map	HTMLMapElement : HTMLElement
mark	HTMLElement
menu	HTMLMenuElement : HTMLElement
meta	HTMLMetaElement : HTMLElement
meter	HTMLMeterElement : HTMLElement
nav	HTMLElement
noscript	HTMLElement
object	HTMLObjectElement : HTMLElement
ol	HTMLOListElement : HTMLElement
optgroup	HTMLOptGroupElement : HTMLElement
option	HTMLOptionElement : HTMLElement
output	HTMLOutputElement : HTMLElement
p	HTMLParagraphElement : HTMLElement
picture	HTMLPictureElement : HTMLElement
pre	HTMLPreElement : HTMLElement
progress	HTMLProgressElement : HTMLElement
q	HTMLQuoteElement : HTMLElement
rp	HTMLElement
rt	HTMLElement
ruby	HTMLElement
s	HTMLElement
samp	HTMLElement
search	HTMLElement
script	HTMLScriptElement : HTMLElement
section	HTMLElement
select	HTMLSelectElement : HTMLElement
selectedcontent	HTMLSelectedContentElement : HTMLElement
slot	HTMLSlotElement : HTMLElement
small	HTMLElement
source	HTMLSourceElement : HTMLElement
span	HTMLSpanElement : HTMLElement
strong	HTMLElement
style	HTMLStyleElement : HTMLElement
sub	HTMLElement
summary	HTMLElement
sup	HTMLElement
table	HTMLTableElement : HTMLElement
tbody	HTMLTableSectionElement : HTMLElement
td	HTMLTableCellElement : HTMLElement
template	HTMLTemplateElement : HTMLElement
textarea	HTMLTextAreaElement : HTMLElement
tfoot	HTMLTableSectionElement : HTMLElement
th	HTMLTableCellElement : HTMLElement
thead	HTMLTableSectionElement : HTMLElement
time	HTMLTimeElement : HTMLElement
title	HTMLTitleElement : HTMLElement
tr	HTMLTableRowElement : HTMLElement
track	HTMLTrackElement : HTMLElement
u	HTMLElement
ul	HTMLUListElement : HTMLElement
var	HTMLElement
video	HTMLVideoElement : HTMLMediaElement : HTMLElement
wbr	HTMLElement
custom elements	supplied by the element's author (inherits from HTMLElement)
All interfaces

This section is non-normative.

AudioTrack
AudioTrackList
BarProp
BeforeUnloadEvent
BroadcastChannel
CanvasGradient
CanvasPattern
CanvasRenderingContext2D
CloseWatcher
CommandEvent
CustomElementRegistry
CustomStateSet
DOMParser
DOMStringList
DOMStringMap
DataTransfer
DataTransferItem
DataTransferItemList
DedicatedWorkerGlobalScope
Document, partial 1 2
DragEvent
Element, partial
ElementInternals
ErrorEvent
EventSource
External
FormDataEvent
HTMLAllCollection
HTMLAnchorElement, partial
HTMLAreaElement, partial
HTMLAudioElement
HTMLBRElement, partial
HTMLBaseElement
HTMLBodyElement, partial
HTMLButtonElement
HTMLCanvasElement
HTMLDListElement, partial
HTMLDataElement
HTMLDataListElement
HTMLDetailsElement
HTMLDialogElement
HTMLDirectoryElement
HTMLDivElement, partial
HTMLElement
HTMLEmbedElement, partial
HTMLFieldSetElement
HTMLFontElement
HTMLFormControlsCollection
HTMLFormElement
HTMLFrameElement
HTMLFrameSetElement
HTMLHRElement, partial
HTMLHeadElement
HTMLHeadingElement, partial
HTMLHtmlElement, partial
HTMLIFrameElement, partial
HTMLImageElement, partial
HTMLInputElement, partial
HTMLLIElement, partial
HTMLLabelElement
HTMLLegendElement, partial
HTMLLinkElement, partial
HTMLMapElement
HTMLMarqueeElement
HTMLMediaElement
HTMLMenuElement, partial
HTMLMetaElement, partial
HTMLMeterElement
HTMLModElement
HTMLOListElement, partial
HTMLObjectElement, partial
HTMLOptGroupElement
HTMLOptionElement
HTMLOptionsCollection
HTMLOutputElement
HTMLParagraphElement, partial
HTMLParamElement
HTMLPictureElement
HTMLPreElement, partial
HTMLProgressElement
HTMLQuoteElement
HTMLScriptElement, partial
HTMLSelectElement
HTMLSelectedContentElement
HTMLSlotElement
HTMLSourceElement
HTMLSpanElement
HTMLStyleElement, partial
HTMLTableCaptionElement, partial
HTMLTableCellElement, partial
HTMLTableColElement, partial
HTMLTableElement, partial
HTMLTableRowElement, partial
HTMLTableSectionElement, partial
HTMLTemplateElement
HTMLTextAreaElement
HTMLTimeElement
HTMLTitleElement
HTMLTrackElement
HTMLUListElement, partial
HTMLUnknownElement
HTMLVideoElement
HashChangeEvent
History
ImageBitmap
ImageBitmapRenderingContext
ImageData
Location
MediaError
MessageChannel
MessageEvent
MessagePort
MimeType
MimeTypeArray
NavigateEvent
Navigation
NavigationActivation
NavigationCurrentEntryChangeEvent
NavigationDestination
NavigationHistoryEntry
NavigationPrecommitController
NavigationTransition
Navigator, partial
NotRestoredReasonDetails
NotRestoredReasons
OffscreenCanvas
OffscreenCanvasRenderingContext2D
Origin
PageRevealEvent
PageSwapEvent
PageTransitionEvent
Path2D
Plugin
PluginArray
PopStateEvent
PromiseRejectionEvent
RadioNodeList
Range, partial
ShadowRoot, partial
SharedWorker
SharedWorkerGlobalScope
Storage
StorageEvent
SubmitEvent
TextMetrics
TextTrack
TextTrackCue
TextTrackCueList
TextTrackList
TimeRanges
ToggleEvent
TrackEvent
UserActivation
ValidityState
VideoTrack
VideoTrackList
VisibilityStateEntry
Window, partial
Worker
WorkerGlobalScope
WorkerLocation
WorkerNavigator
Worklet
WorkletGlobalScope
XMLSerializer
Events

This section is non-normative.

The following table lists events fired by this document, excluding those already defined in media element events and drag-and-drop events.

List of events
Event	Interface	Interesting targets	Description
DOMContentLoaded
✔MDN
	Event	Document	Fired at the Document once the parser has finished
afterprint
✔MDN
	Event	Window	Fired at the Window after printing
beforeprint
✔MDN
	Event	Window	Fired at the Window before printing
beforematch
⚠MDN
	Event	Elements	Fired on elements with the hidden=until-found attribute before they are revealed.
beforetoggle
✔MDN
	ToggleEvent	Elements	Fired on elements with the popover attribute when they are transitioning between showing and hidden
beforeunload
✔MDN
	BeforeUnloadEvent	Window	Fired at the Window when the page is about to be unloaded, in case the page would like to show a warning prompt
blur	Event	Window, elements	Fired at nodes when they stop being focused
cancel
✔MDN
	Event	CloseWatcher, dialog elements, input elements	Fired at CloseWatcher objects or dialog elements when they receive a close request, or at input elements whose type attribute is in the File state when the user does not change their selection
change
✔MDN
	Event	Form controls	Fired at controls when the user commits a value change (see also the input event)
click	PointerEvent	Elements	Normally a mouse event; also synthetically fired at an element before its activation behavior is run, when an element is activated from a non-pointer input device (e.g. a keyboard)
close
✔MDN
	Event	CloseWatcher, dialog elements, MessagePort	Fired at CloseWatcher objects or dialog elements when they are closed via a close request or via web developer code, or at MessagePort objects when disentangled
command	CommandEvent	Elements	Fired at elements when they handle a user invocation, via a commandfor attribute.
connect
✔MDN
	MessageEvent	SharedWorkerGlobalScope	Fired at a shared worker's global scope when a new client connects
contextlost
⚠MDN
	Event	canvas elements, OffscreenCanvas objects	Fired when the corresponding CanvasRenderingContext2D or OffscreenCanvasRenderingContext2D is lost
contextrestored
⚠MDN
	Event	canvas elements, OffscreenCanvas objects	Fired when the corresponding CanvasRenderingContext2D or OffscreenCanvasRenderingContext2D is restored after being lost
currententrychange	NavigationCurrentEntryChangeEvent	Navigation	Fired when navigation.currentEntry changes
dispose	Event	NavigationHistoryEntry	Fired when the session history entry corresponding to the NavigationHistoryEntry has been permanently evicted from session history and can no longer be traversed to
error
✔MDN
	Event or ErrorEvent	Global scope objects, Worker objects, elements, networking-related objects	Fired when unexpected errors occur (e.g. networking errors, script errors, decoding errors)
focus	Event	Window, elements	Fired at nodes gaining focus
formdata
✔MDN
	FormDataEvent	form elements	Fired at a form element when it is constructing the entry list
hashchange
✔MDN
	HashChangeEvent	Window	Fired at the Window when the fragment part of the document's URL changes
input	Event	Elements	Fired when the user changes the contenteditable element's content, or the form control's value. See also the change event for form controls.
invalid
✔MDN
	Event	Form controls	Fired at controls during form validation if they do not satisfy their constraints
languagechange
✔MDN
	Event	Global scope objects	Fired at the global scope object when the user's preferred languages change
load	Event	Window, elements	Fired at the Window when the document has finished loading; fired at an element containing a resource (e.g. img, embed) when its resource has finished loading
message
✔MDN
	MessageEvent	Window, EventSource, MessagePort, BroadcastChannel, DedicatedWorkerGlobalScope, Worker, ServiceWorkerContainer	Fired at an object when it receives a message
messageerror
✔MDN
	MessageEvent	Window, MessagePort, BroadcastChannel, DedicatedWorkerGlobalScope, Worker, ServiceWorkerContainer	Fired at an object when it receives a message that cannot be deserialized
navigate	NavigateEvent	Navigation	Fired before the navigable navigates, reloads, traverses, or otherwise changes its URL
navigateerror	ErrorEvent	Navigation	Fired when a navigation does not complete successfully
navigatesuccess	Event	Navigation	Fired when a navigation completes successfully
offline
✔MDN
	Event	Global scope objects	Fired at the global scope object when the network connections fails
online
✔MDN
	Event	Global scope objects	Fired at the global scope object when the network connections returns
open
✔MDN
	Event	EventSource	Fired at EventSource objects when a connection is established
pageswap	PageSwapEvent	Window	Fired at the Window right before a document is unloaded as a result of a navigation.
pagehide
✔MDN
	PageTransitionEvent	Window	Fired at the Window when the page's session history entry stops being the active entry
pagereveal	PageRevealEvent	Window	Fired at the Window when the page begins to render for the first time after it has been initialized or reactivated
pageshow
✔MDN
	PageTransitionEvent	Window	Fired at the Window when the page's session history entry becomes the active entry
pointercancel	PointerEvent	Elements and Text nodes	Fired at the source node when the user attempts to initiate a drag-and-drop operation
popstate
✔MDN
	PopStateEvent	Window	Fired at the Window when in some cases of session history traversal
readystatechange
✔MDN
	Event	Document	Fired at the Document when it finishes parsing and again when all its subresources have finished loading
rejectionhandled	PromiseRejectionEvent	Global scope objects	Fired at global scope objects when a previously-unhandled promise rejection becomes handled
reset
✔MDN
	Event	form elements	Fired at a form element when it is reset
select
✔MDN
	Event	Form controls	Fired at form controls when their text selection is adjusted (whether by an API or by the user)
storage
✔MDN
	StorageEvent	Window	Fired at Window event when the corresponding localStorage or sessionStorage storage areas change
submit
✔MDN
	SubmitEvent	form elements	Fired at a form element when it is submitted
toggle
✔MDN
	ToggleEvent	details and popover elements	Fired at details elements when they open or close; fired on elements with the popover attribute when they are transitioning between showing and hidden
unhandledrejection
✔MDN
	PromiseRejectionEvent	Global scope objects	Fired at global scope objects when a promise rejection goes unhandled
unload
✔MDN
	Event	Window	Fired at the Window object when the page is going away
visibilitychange
✔MDN
	Event	Document	Fired at the Document object when the page becomes visible or hidden to the user
HTTP headers

This section is non-normative.

The following HTTP request headers are defined by this specification:

`Last-Event-ID`
`Ping-From`
`Ping-To`

The following HTTP response headers are defined by this specification:

`Cross-Origin-Embedder-Policy`
`Cross-Origin-Embedder-Policy-Report-Only`
`Cross-Origin-Opener-Policy`
`Cross-Origin-Opener-Policy-Report-Only`
`Origin-Agent-Cluster`
`Refresh`
`X-Frame-Options`
MIME types

This section is non-normative.

The following MIME types are mentioned in this specification:

application/atom+xml
Atom [ATOM]
application/json
JSON [JSON]
application/octet-stream
Generic binary data [RFC2046]
application/microdata+json
Microdata as JSON
application/rss+xml
RSS
application/wasm
WebAssembly [WASM]
application/x-www-form-urlencoded
Form submission
application/xhtml+xml
HTML
application/xml
XML [XML] [RFC7303]
image/gif
GIF images [GIF]
image/jpeg
JPEG images [JPEG]
image/png
PNG images [PNG]
image/svg+xml
SVG images [SVG]
multipart/form-data
Form submission [RFC7578]
multipart/mixed
Generic mixed content [RFC2046]
multipart/x-mixed-replace
Streaming server push
text/css
CSS [CSS]
text/event-stream
Server-sent event streams
text/javascript
JavaScript [JAVASCRIPT] [RFC9239]
text/json
JSON (legacy type)
text/plain
Generic plain text [RFC2046] [RFC3676]
text/html
HTML
text/ping
Hyperlink auditing
text/uri-list
List of URLs [RFC2483]
text/vcard
vCard [RFC6350]
text/vtt
WebVTT [WEBVTT]
text/xml
XML [XML] [RFC7303]
video/mp4
MPEG-4 video [RFC4337]
video/mpeg
MPEG video [RFC2046]
← 17 IANA considerations — Table of Contents — References →
