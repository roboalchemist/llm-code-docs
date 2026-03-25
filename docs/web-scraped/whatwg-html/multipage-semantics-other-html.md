# Source: https://html.spec.whatwg.org/multipage/semantics-other.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/semantics-other.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 4.13 Custom elements — Table of Contents — 5 Microdata →
4.14 Common idioms without dedicated elements
4.14.1 Breadcrumb navigation
4.14.2 Tag clouds
4.14.3 Conversations
4.14.4 Footnotes
4.15 Disabled elements
4.16 Matching HTML elements using selectors and CSS
4.16.1 Case-sensitivity of the CSS 'attr()' function
4.16.2 Case-sensitivity of selectors
4.16.3 Pseudo-classes
4.14 Common idioms without dedicated elements
4.14.1 Breadcrumb navigation

This specification does not provide a machine-readable way of describing breadcrumb navigation menus. Authors are encouraged to just use a series of links in a paragraph. The nav element can be used to mark the section containing these paragraphs as being navigation blocks.

In the following example, the current page can be reached via two paths.

<nav>
 <p>
  <a href="/">Main</a> ▸
  <a href="/products/">Products</a> ▸
  <a href="/products/dishwashers/">Dishwashers</a> ▸
  <a>Second hand</a>
 </p>
 <p>
  <a href="/">Main</a> ▸
  <a href="/second-hand/">Second hand</a> ▸
  <a>Dishwashers</a>
 </p>
</nav>
4.14.2 Tag clouds

This specification does not define any markup specifically for marking up lists of keywords that apply to a group of pages (also known as tag clouds). In general, authors are encouraged to either mark up such lists using ul elements with explicit inline counts that are then hidden and turned into a presentational effect using a style sheet, or to use SVG.

Here, three tags are included in a short tag cloud:

<style>
.tag-cloud > li > span { display: none; }
.tag-cloud > li { display: inline; }
.tag-cloud-1 { font-size: 0.7em; }
.tag-cloud-2 { font-size: 0.9em; }
.tag-cloud-3 { font-size: 1.1em; }
.tag-cloud-4 { font-size: 1.3em; }
.tag-cloud-5 { font-size: 1.5em; }

@media speech {
  .tag-cloud > li > span { display:inline }
}
</style>
...
<ul class="tag-cloud">
 <li class="tag-cloud-4"><a title="28 instances" href="/t/apple">apple</a> <span>(popular)</span>
 <li class="tag-cloud-2"><a title="6 instances"  href="/t/kiwi">kiwi</a> <span>(rare)</span>
 <li class="tag-cloud-5"><a title="41 instances" href="/t/pear">pear</a> <span>(very popular)</span>
</ul>

The actual frequency of each tag is given using the title attribute. A CSS style sheet is provided to convert the markup into a cloud of differently-sized words, but for user agents that do not support CSS or are not visual, the markup contains annotations like "(popular)" or "(rare)" to categorize the various tags by frequency, thus enabling all users to benefit from the information.

The ul element is used (rather than ol) because the order is not particularly important: while the list is in fact ordered alphabetically, it would convey the same information if ordered by, say, the length of the tag.

The tag rel-keyword is not used on these a elements because they do not represent tags that apply to the page itself; they are just part of an index listing the tags themselves.

4.14.3 Conversations

This specification does not define a specific element for marking up conversations, meeting minutes, chat transcripts, dialogues in screenplays, instant message logs, and other situations where different players take turns in discourse.

Instead, authors are encouraged to mark up conversations using p elements and punctuation. Authors who need to mark the speaker for styling purposes are encouraged to use span or b. Paragraphs with their text wrapped in the i element can be used for marking up stage directions.

This example demonstrates this using an extract from Abbot and Costello's famous sketch, Who's on first:

<p> Costello: Look, you gotta first baseman?
<p> Abbott: Certainly.
<p> Costello: Who's playing first?
<p> Abbott: That's right.
<p> Costello becomes exasperated.
<p> Costello: When you pay off the first baseman every month, who gets the money?
<p> Abbott: Every dollar of it.

The following extract shows how an IM conversation log could be marked up, using the data element to provide Unix timestamps for each line. Note that the timestamps are provided in a format that the time element does not support, so the data element is used instead (namely, Unix time_t timestamps). Had the author wished to mark up the data using one of the date and time formats supported by the time element, that element could have been used instead of data. This could be advantageous as it would allow data analysis tools to detect the timestamps unambiguously, without coordination with the page author.

<p> <data value="1319898155">14:22</data> <b>egof</b> I'm not that nerdy, I've only seen 30% of the star trek episodes
<p> <data value="1319898192">14:23</data> <b>kaj</b> if you know what percentage of the star trek episodes you have seen, you are inarguably nerdy
<p> <data value="1319898200">14:23</data> <b>egof</b> it's unarguably
<p> <data value="1319898228">14:23</data> <i>* kaj blinks</i>
<p> <data value="1319898260">14:24</data> <b>kaj</b> you are not helping your case

HTML does not have a good way to mark up graphs, so descriptions of interactive conversations from games are more difficult to mark up. This example shows one possible convention using dl elements to list the possible responses at each point in the conversation. Another option to consider is describing the conversation in the form of a DOT file, and outputting the result as an SVG image to place in the document. [DOT]

<p> Next, you meet a fisher. You can say one of several greetings:
<dl>
 <dt> "Hello there!"
 <dd>
  <p> She responds with "Hello, how may I help you?"; you can respond with:
  <dl>
   <dt> "I would like to buy a fish."
   <dd> <p> She sells you a fish and the conversation finishes.
   <dt> "Can I borrow your boat?"
   <dd>
    <p> She is surprised and asks "What are you offering in return?".
    <dl>
     <dt> "Five gold." (if you have enough)
     <dt> "Ten gold." (if you have enough)
     <dt> "Fifteen gold." (if you have enough)
     <dd> <p> She lends you her boat. The conversation ends.
     <dt> "A fish." (if you have one)
     <dt> "A newspaper." (if you have one)
     <dt> "A pebble." (if you have one)
     <dd> <p> "No thanks", she replies. Your conversation options
     at this point are the same as they were after asking to borrow
     her boat, minus any options you've suggested before.
    </dl>
   </dd>
  </dl>
 </dd>
 <dt> "Vote for me in the next election!"
 <dd> <p> She turns away. The conversation finishes.
 <dt> "Madam, are you aware that your fish are running away?"
 <dd>
  <p> She looks at you skeptically and says "Fish cannot run, miss".
  <dl>
   <dt> "You got me!"
   <dd> <p> The fisher sighs and the conversation ends.
   <dt> "Only kidding."
   <dd> <p> "Good one!" she retorts. Your conversation options at this
   point are the same as those following "Hello there!" above.
   <dt> "Oh, then what are they doing?"
   <dd> <p> She looks at her fish, giving you an opportunity to steal
   her boat, which you do. The conversation ends.
  </dl>
 </dd>
</dl>

In some games, conversations are simpler: each character merely has a fixed set of lines that they say. In this example, a game FAQ/walkthrough lists some of the known possible responses for each character:

<section>
 <h1>Dialogue</h1>
 <p><small>Some characters repeat their lines in order each time you interact
 with them, others randomly pick from amongst their lines. Those who respond in
 order have numbered entries in the lists below.</small>
 <h2>The Shopkeeper</h2>
 <ul>
  <li>How may I help you?
  <li>Fresh apples!
  <li>A loaf of bread for madam?
 </ul>
 <h2>The pilot</h2>
 <p>Before the accident:
 <ul>
  <li>I'm about to fly out, sorry!
  <li>Sorry, I'm just waiting for flight clearance and then I'll be off!
 </ul>
 <p>After the accident:
 <ol>
  <li>I'm about to fly out, sorry!
  <li>Ok, I'm not leaving right now, my plane is being cleaned.
  <li>Ok, it's not being cleaned, it needs a minor repair first.
  <li>Ok, ok, stop bothering me! Truth is, I had a crash.
 </ol>
 <h2>Clan Leader</h2>
 <p>During the first clan meeting:
 <ul>
  <li>Hey, have you seen my daughter? I bet she's up to something nefarious again...
  <li>Nice weather we're having today, eh?
  <li>The name is Bailey, Jeff Bailey. How can I help you today?
  <li>A glass of water? Fresh from the well!
 </ul>
 <p>After the earthquake:
 <ol>
  <li>Everyone is safe in the shelter, we just have to put out the fire!
  <li>I'll go and tell the fire brigade, you keep hosing it down!
 </ol>
</section>
4.14.4 Footnotes

HTML does not have a dedicated mechanism for marking up footnotes. Here are the suggested alternatives.

For short inline annotations, the title attribute could be used.

In this example, two parts of a dialogue are annotated with footnote-like content using the title attribute.

<p> <b>Customer</b>: Hello! I wish to register a complaint. Hello. Miss?
<p> <b>Shopkeeper</b>: <span title="Colloquial pronunciation of 'What do you'"
>Watcha</span> mean, miss?
<p> <b>Customer</b>: Uh, I'm sorry, I have a cold. I wish to make a complaint.
<p> <b>Shopkeeper</b>: Sorry, <span title="This is, of course, a lie.">we're
closing for lunch</span>.

Unfortunately, relying on the title attribute is currently discouraged as many user agents do not expose the attribute in an accessible manner as required by this specification (e.g. requiring a pointing device such as a mouse to cause a tooltip to appear, which excludes keyboard-only users and touch-only users, such as anyone with a modern phone or tablet).

If the title attribute is used, CSS can be used to draw the reader's attention to the elements with the attribute.

For example, the following CSS places a dashed line below elements that have a title attribute.

[title] { border-bottom: thin dashed; }

For longer annotations, the a element should be used, pointing to an element later in the document. The convention is that the contents of the link be a number in square brackets.

In this example, a footnote in the dialogue links to a paragraph below the dialogue. The paragraph then reciprocally links back to the dialogue, allowing the user to return to the location of the footnote.

<p> Announcer: Number 16: The <i>hand</i>.
<p> Interviewer: Good evening. I have with me in the studio tonight
Mr Norman St John Polevaulter, who for the past few years has been
contradicting people. Mr Polevaulter, why <em>do</em> you
contradict people?
<p> Norman: I don't. <sup><a href="#fn1" id="r1">[1]</a></sup>
<p> Interviewer: You told me you did!
...
<section>
 <p id="fn1"><a href="#r1">[1]</a> This is, naturally, a lie,
 but paradoxically if it were true he could not say so without
 contradicting the interviewer and thus making it false.</p>
</section>

For side notes, longer annotations that apply to entire sections of the text rather than just specific words or sentences, the aside element should be used.

In this example, a sidebar is given after a dialogue, giving it some context.

<p> <span class="speaker">Customer</span>: I will not buy this record, it is scratched.
<p> <span class="speaker">Shopkeeper</span>: I'm sorry?
<p> <span class="speaker">Customer</span>: I will not buy this record, it is scratched.
<p> <span class="speaker">Shopkeeper</span>: No no no, this's'a tobacconist's.
<aside>
 <p>In 1970, the British Empire lay in ruins, and foreign
 nationalists frequented the streets — many of them Hungarians
 (not the streets — the foreign nationals). Sadly, Alexander
 Yalt has been publishing incompetently-written phrase books.
</aside>

For figures or tables, footnotes can be included in the relevant figcaption or caption element, or in surrounding prose.

In this example, a table has cells with footnotes that are given in prose. A figure element is used to give a single legend to the combination of the table and its footnotes.

<figure>
 <figcaption>Table 1. Alternative activities for knights.</figcaption>
 <table>
  <tr>
   <th> Activity
   <th> Location
   <th> Cost
  <tr>
   <td> Dance
   <td> Wherever possible
   <td> £0<sup><a href="#fn1">1</a></sup>
  <tr>
   <td> Routines, chorus scenes<sup><a href="#fn2">2</a></sup>
   <td> Undisclosed
   <td> Undisclosed
  <tr>
   <td> Dining<sup><a href="#fn3">3</a></sup>
   <td> Camelot
   <td> Cost of ham, jam, and spam<sup><a href="#fn4">4</a></sup>
 </table>
 <p id="fn1">1. Assumed.</p>
 <p id="fn2">2. Footwork impeccable.</p>
 <p id="fn3">3. Quality described as "well".</p>
 <p id="fn4">4. A lot.</p>
</figure>
4.15 Disabled elements

An element is said to be actually disabled if it is one of the following:

a button element that is disabled
an input element that is disabled
a select element that is disabled
a textarea element that is disabled
an optgroup element that has a disabled attribute
an option element that is disabled
a fieldset element that is a disabled fieldset
a form-associated custom element that is disabled

This definition is used to determine what elements are focusable and which elements match the :enabled and :disabled pseudo classes.

4.16 Matching HTML elements using selectors and CSS
4.16.1 Case-sensitivity of the CSS 'attr()' function

CSS Values and Units leaves the case-sensitivity of attribute names for the purpose of the 'attr()' function to be defined by the host language. [CSSVALUES]

When comparing the attribute name part of a CSS 'attr()' function to the names of namespace-less attributes on HTML elements in HTML documents, the name part of the CSS 'attr()' function must first be converted to ASCII lowercase. The same function when compared to other attributes must be compared according to its original case. In both cases, to match, the values must be identical to each other (and therefore the comparison is case sensitive).

This is the same as comparing the name part of a CSS attribute selector, specified in the next section.

4.16.2 Case-sensitivity of selectors

Selectors leaves the case-sensitivity of element names, attribute names, and attribute values to be defined by the host language. [SELECTORS]

When comparing a CSS element type selector to the names of HTML elements in HTML documents, the CSS element type selector must first be converted to ASCII lowercase. The same selector when compared to other elements must be compared according to its original case. In both cases, to match, the values must be identical to each other (and therefore the comparison is case sensitive).

When comparing the name part of a CSS attribute selector to the names of attributes on HTML elements in HTML documents, the name part of the CSS attribute selector must first be converted to ASCII lowercase. The same selector when compared to other attributes must be compared according to its original case. In both cases, the comparison is case-sensitive.

Attribute selectors on an HTML element in an HTML document must treat the values of attributes with the following names as ASCII case-insensitive:

accept
accept-charset
align
alink
axis
bgcolor
charset
checked
clear
codetype
color
compact
declare
defer
dir
direction
disabled
enctype
face
frame
hreflang
http-equiv
lang
language
link
media
method
multiple
nohref
noresize
noshade
nowrap
readonly
rel
rev
rules
scope
scrolling
selected
shape
target
text
type
valign
valuetype
vlink

For example, the selector [bgcolor="#ffffff"] will match any HTML element with a bgcolor attribute with values including #ffffff, #FFFFFF and #fffFFF. This happens even if bgcolor has no effect for a given element (e.g., div).

The selector [type=a s] will match any HTML element with a type attribute whose value is a, but not whose value is A, due to the s flag.

All other attribute values and everything else must be treated as entirely identical to each other for the purposes of selector matching. This includes:

IDs and classes in no-quirks mode and limited-quirks mode

the names of elements not in the HTML namespace

the names of HTML elements in XML documents

the names of attributes of elements not in the HTML namespace

the names of attributes of HTML elements in XML documents

the names of attributes that themselves have namespaces

Selectors defines that ID and class selectors (such as #foo and .bar), when matched against elements in documents that are in quirks mode, will be matched in an ASCII case-insensitive manner. However, this does not apply for attribute selectors with "id" or "class" as the name part. The selector [class="foobar"] will treat its value as case-sensitive even in quirks mode.

4.16.3 Pseudo-classes
MDN

There are a number of dynamic selectors that can be used with HTML. This section defines when these selectors match HTML elements. [SELECTORS] [CSSUI]

:defined
✔MDN

The :defined pseudo-class must match any element that is defined.

:link
✔MDN
:visited
✔MDN

All a elements that have an href attribute, and all area elements that have an href attribute, must match one of :link and :visited.

Other specifications might apply more specific rules regarding how these elements are to match these pseudo-classes, to mitigate some privacy concerns that apply with straightforward implementations of this requirement.

:active
✔MDN

The :active pseudo-class is defined to match an element while an element is being activated by the user.

To determine whether a particular element is being activated for the purposes of defining the :active pseudo-class only, an HTML user agent must use the first relevant entry in the following list.

If the element is a button element
If the element is an input element whose type attribute is in the Submit Button, Image Button, Reset Button, or Button state
If the element is an a element that has an href attribute
If the element is an area element that has an href attribute
If the element is focusable

The element is being activated if it is in a formal activation state.

For example, if the user is using a keyboard to push a button element by pressing the space bar, the element would match this pseudo-class in between the time that the element received the keydown event and the time the element received the keyup event.

If the element is being actively pointed at

The element is being activated.

An element is said to be in a formal activation state between the time the user begins to indicate an intent to trigger the element's activation behavior and either the time the user stops indicating an intent to trigger the element's activation behavior, or the time the element's activation behavior has finished running, which ever comes first.

An element is said to be being actively pointed at while the user indicates the element using a pointing device while that pointing device is in the "down" state (e.g. for a mouse, between the time the mouse button is pressed and the time it is released; for a finger in a multitouch environment, while the finger is touching the display surface).

Per the definition in Selectors, :active also matches flat tree ancestors of elements that are being activated. [SELECTORS]

Additionally, any element that is the labeled control of a label element that is currently matching :active, also matches :active. (But, it does not count as being being activated.)

:hover
✔MDN

The :hover pseudo-class is defined to match an element while the user designates an element with a pointing device. For the purposes of defining the :hover pseudo-class only, an HTML user agent must consider an element as being one that the user designates if it is an element that the user indicates using a pointing device.

Per the definition in Selectors, :hover also matches flat tree ancestors of elements that are designated. [SELECTORS]

Additionally, any element that is the labeled control of a label element that is currently matching :hover, also matches :hover. (But, it does not count as being designated.)

Consider in particular a fragment such as:

<p> <label for=c> <input id=a> </label> <span id=b> <input id=c> </span> </p>

If the user designates the element with ID "a" with their pointing device, then the p element (and all its ancestors not shown in the snippet above), the label element, the element with ID "a", and the element with ID "c" will match the :hover pseudo-class. The element with ID "a" matches it by being designated; the label and p elements match it because of the condition in Selectors about flat tree ancestors; and the element with ID "c" matches it through the additional condition above on labeled controls (i.e., its label element matches :hover). However, the element with ID "b" does not match :hover: its flat tree descendant is not designated, even though that flat tree descendant matches :hover.

:focus
✔MDN

For the purposes of the CSS :focus pseudo-class, an element has the focus when:

it is not itself a navigable container; and

any of the following are true:

it is one of the elements listed in the current focus chain of the top-level traversable; or

its shadow root shadowRoot is not null and shadowRoot is the root of at least one element that has the focus.

:target
✔MDN

For the purposes of the CSS :target pseudo-class, the Document's target elements are a list containing the Document's target element, if it is not null, or containing no elements, if it is. [SELECTORS]

:popover-open
✔MDN

The :popover-open pseudo-class is defined to match any HTML element whose popover attribute is not in the No Popover state and whose popover visibility state is showing.

:enabled
✔MDN

The :enabled pseudo-class must match any button, input, select, textarea, optgroup, option, fieldset element, or form-associated custom element that is not actually disabled.

:disabled
✔MDN

The :disabled pseudo-class must match any element that is actually disabled.

:checked
✔MDN

The :checked pseudo-class must match any element falling into one of the following categories:

input elements whose type attribute is in the Checkbox state and whose checkedness state is true
input elements whose type attribute is in the Radio Button state and whose checkedness state is true
option elements whose selectedness is true
:indeterminate
✔MDN

The :indeterminate pseudo-class must match any element falling into one of the following categories:

input elements whose type attribute is in the Checkbox state and whose indeterminate IDL attribute is set to true
input elements whose type attribute is in the Radio Button state and whose radio button group contains no input elements whose checkedness state is true.
progress elements with no value content attribute
:default
✔MDN

The :default pseudo-class must match any element falling into one of the following categories:

Submit buttons that are default buttons of their form owner.
input elements to which the checked attribute applies and that have a checked attribute
option elements that have a selected attribute
:placeholder-shown

The :placeholder-shown pseudo-class must match any element falling into one of the following categories:

input elements that have a placeholder attribute whose value is currently being presented to the user
textarea elements that have a placeholder attribute whose value is currently being presented to the user
:valid
✔MDN

The :valid pseudo-class must match any element falling into one of the following categories:

elements that are candidates for constraint validation and that satisfy their constraints
form elements that are not the form owner of any elements that themselves are candidates for constraint validation but do not satisfy their constraints
fieldset elements that have no descendant elements that themselves are candidates for constraint validation but do not satisfy their constraints
:invalid
✔MDN

The :invalid pseudo-class must match any element falling into one of the following categories:

elements that are candidates for constraint validation but that do not satisfy their constraints
form elements that are the form owner of one or more elements that themselves are candidates for constraint validation but do not satisfy their constraints
fieldset elements that have of one or more descendant elements that themselves are candidates for constraint validation but do not satisfy their constraints
:user-valid

The :user-valid pseudo-class must match input, textarea, and select elements whose user validity is true, are candidates for constraint validation, and that satisfy their constraints.

:user-invalid

The :user-invalid pseudo-class must match input, textarea, and select elements whose user validity is true, are candidates for constraint validation but do not satisfy their constraints.

:in-range
✔MDN

The :in-range pseudo-class must match all elements that are candidates for constraint validation, have range limitations, and that are neither suffering from an underflow nor suffering from an overflow.

:out-of-range
✔MDN

The :out-of-range pseudo-class must match all elements that are candidates for constraint validation, have range limitations, and that are either suffering from an underflow or suffering from an overflow.

:required
✔MDN

The :required pseudo-class must match any element falling into one of the following categories:

input elements that are required
select elements that have a required attribute
textarea elements that have a required attribute
:optional
✔MDN

The :optional pseudo-class must match any element falling into one of the following categories:

input elements to which the required attribute applies that are not required
select elements that do not have a required attribute
textarea elements that do not have a required attribute
:autofill
MDN
:-webkit-autofill

The :autofill and :-webkit-autofill pseudo-classes must match input elements which have been autofilled by user agent. These pseudo-classes must stop matching if the user edits the autofilled field.

One way such autofilling might happen is via the autocomplete attribute, but user agents could autofill even without that attribute being involved.

:read-only
✔MDN
:read-write
✔MDN

The :read-write pseudo-class must match any element falling into one of the following categories, which for the purposes of Selectors are thus considered user-alterable: [SELECTORS]

input elements to which the readonly attribute applies, and that are mutable (i.e. that do not have the readonly attribute specified and that are not disabled)
textarea elements that do not have a readonly attribute, and that are not disabled
elements that are editing hosts or editable and are neither input elements nor textarea elements

The :read-only pseudo-class must match all other HTML elements.

:modal

The :modal pseudo-class must match any element falling into one of the following categories:

dialog elements whose is modal is true
elements whose fullscreen flag is true
:dir(ltr)
MDN

The :dir(ltr) pseudo-class must match all elements whose directionality is 'ltr'.

:dir(rtl)

The :dir(rtl) pseudo-class must match all elements whose directionality is 'rtl'.

Custom state pseudo-class

The :state(identifier) pseudo-class must match all custom elements whose states set's set entries contains identifier.

:heading

The :heading pseudo-class must match all h1, h2, h3, h4, h5, and h6 elements.

:heading(integer#)

The :heading(integer#) pseudo-class must match all h1, h2, h3, h4, h5, and h6 elements that have a heading level of integer. [CSSSYNTAX] [CSSVALUES]

:playing

The :playing pseudo-class must match all media elements whose paused attribute is false.

:paused

The :paused pseudo-class must match all media elements whose paused attribute is true.

:seeking

The :seeking pseudo-class must match all media elements whose seeking attribute is true.

:buffering

The :buffering pseudo-class must match all media elements whose paused attribute is false, networkState attribute is NETWORK_LOADING, and ready state is HAVE_CURRENT_DATA or less.

:stalled

The :stalled pseudo-class must match all media elements that match the :buffering pseudo-class and whose is currently stalled is true.

This pseudo-class is intended for displaying player state UI when video playback has been buffering for too long. Unlike the stalled event, which fires whenever the network download has stalled regardless of playback or ready state.

:muted

The :muted pseudo-class must match all media elements that are muted.

:volume-locked

The :volume-locked pseudo-class must match all media elements when the user agent's volume locked is true.

:open

The :open pseudo-class must match any element falling into one of the following categories:

details elements that have an open attribute

dialog elements that have an open attribute

select elements that are a drop-down box and whose drop-down boxes are open

input elements that support a picker and whose pickers are open

This specification does not define when an element matches the :lang() dynamic pseudo-class, as it is defined in sufficient detail in a language-agnostic fashion in Selectors. [SELECTORS]

← 4.13 Custom elements — Table of Contents — 5 Microdata →
