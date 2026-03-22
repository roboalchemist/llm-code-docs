# Source: https://html.spec.whatwg.org/multipage/speculative-loading.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/speculative-loading.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 7.5 Document lifecycle](https://html.spec.whatwg.org/multipage/document-lifecycle.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8 Web application APIs →](https://html.spec.whatwg.org/multipage/webappapis.html)
1.       1.   [7.6 Speculative loading](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading)
        1.   [7.6.1 Speculation rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules)
            1.   [7.6.1.1 Data model](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-data-model)
            2.   [7.6.1.2 Parsing](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-parsing)
            3.   [7.6.1.3 Processing model](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-processing-model)

        2.   [7.6.2 Navigational prefetching](https://html.spec.whatwg.org/multipage/speculative-loading.html#navigational-prefetching)
        3.   [7.6.3 The ``Speculation-Rules`` header](https://html.spec.whatwg.org/multipage/speculative-loading.html#the-speculation-rules-header)
        4.   [7.6.4 The ``Sec-Speculation-Tags`` header](https://html.spec.whatwg.org/multipage/speculative-loading.html#the-sec-speculation-tags-header)
        5.   [7.6.5 Security considerations](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-security)
            1.   [7.6.5.1 Cross-site requests](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-cross-site-requests)
            2.   [7.6.5.2 Injected content](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-injected-content)
            3.   [7.6.5.3 IP anonymization](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-ip-anonymization)

        6.   [7.6.6 Privacy considerations](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-privacy)
            1.   [7.6.6.1 Heuristics and optionality](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-heuristics)
            2.   [7.6.6.2 State partitioning](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-state-partitioning)
            3.   [7.6.6.3 Identity joining](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-identity-joining)

    2.   [7.7 The ``X-Frame-Options`` header](https://html.spec.whatwg.org/multipage/speculative-loading.html#the-x-frame-options-header)
    3.   [7.8 The ``Refresh`` header](https://html.spec.whatwg.org/multipage/speculative-loading.html#the-refresh-header)
    4.   [7.9 Browser user interface considerations](https://html.spec.whatwg.org/multipage/speculative-loading.html#nav-traversal-ui)

### 7.6 Speculative loading[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading)

Speculative loading is the practice of performing navigation actions, such as prefetching, ahead of navigation starting. This makes subsequent navigations faster.

Developers can initiate speculative loads by using [speculation rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set). User agents might also perform speculative loads in certain [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) scenarios, such as typing into the address bar.

#### 7.6.1 Speculation rules[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules)

[Speculation rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set) are how developers instruct the browser about speculative loading operations that the developer believes will be beneficial. They are delivered as JSON documents, via either:

*   inline `script` elements with their `type` attribute set to "`speculationrules`"; or

*   resources fetched from a URL specified in the ``Speculation-Rules`` HTTP response header.

The following JSON document is parsed into a [speculation rule set](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set) specifying a number of desired conditions for the user agent to [start a referrer-initiated navigational prefetch](https://wicg.github.io/nav-speculation/prefetch.html#start-a-referrer-initiated-navigational-prefetch):

```
{
  "prefetch": [
    {
      "urls": ["/chapters/5"]
    },
    {
      "eagerness": "moderate",
      "where": {
        "and": [
          { "href_matches": "/*" },
          { "not": { "selector_matches": ".no-prefetch" } }
        ]
      }
    }
  ]
}
```

A JSON document representing a [speculation rule set](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set) must meet the following :

*   It must be valid JSON. [[JSON]](https://html.spec.whatwg.org/multipage/references.html#refsJSON)

*   The JSON must represent a JSON object, with at most three keys "`tag`", "`prefetch`" and "`prerender`".

In this standard, "`prerender`" is optionally converted to "`prefetch`" [at parse time](https://html.spec.whatwg.org/multipage/speculative-loading.html#note-speculation-rules-parse-prerender-as-prefetch). Some implementations might implement different behavior for prerender, as specified in Prerendering Revamped. [[PRERENDERING-REVAMPED]](https://html.spec.whatwg.org/multipage/references.html#refsPRERENDERING-REVAMPED)

*   The value corresponding to the "`tag`" key, if present, must be a [speculation rule tag](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag).

*   The values corresponding to the "`prefetch`" and "`prerender`" keys, if present, must be arrays of [valid speculation rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-speculation-rule).

A valid speculation rule is a JSON object that meets the following requirements:

*   It must have at most the following keys: "`source`", "`urls`", "`where`", "`relative_to`", "`eagerness`", "`referrer_policy`", "`tag`", "`requires`", "`expects_no_vary_search`", or "`target_hint`".

In this standard, ["`target_hint`" is ignored](https://html.spec.whatwg.org/multipage/speculative-loading.html#note-speculation-rules-parse-target-hint).

*   The value corresponding to the "`source`" key, if present, must be either "`list`" or "`document`".

*   If the value corresponding to the "`source`" key is "`list`", then the "`urls`" key must be present, and the "`where`" key must be absent.

*   If the value corresponding to the "`source`" key is "`document`", then the "`urls`" key must be absent.

*   The "`urls`" and "`where`" keys must not both be present.

*   If the value corresponding to the "`source`" key is "`document`" or the "`where`" key is present, then the "`relative_to`" key must be absent.

*   The value corresponding to the "`urls`" key, if present, must be an array of [valid URL strings](https://url.spec.whatwg.org/#valid-url-string).

*   The value corresponding to the "`where`" key, if present, must be a [valid document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-document-rule-predicate).

*   The value corresponding to the "`relative_to`" key, if present, must be either "`ruleset`" or "`document`".

*   The value corresponding to the "`eagerness`" key, if present, must be a [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness).

*   The value corresponding to the "`referrer_policy`" key, if present, must be a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy).

*   The value corresponding to the "`tag`" key, if present, must be a [speculation rule tag](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag).

*   The value corresponding to the "`requires`" key, if present, must be an array of [speculation rule requirements](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-requirement).

*   The value corresponding to the "`expects_no_vary_search`" key, if present, must be a [string](https://infra.spec.whatwg.org/#string) that is [parseable](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#parse-a-url-search-variance) as a ``No-Vary-Search`` header value.

A valid document rule predicate is a JSON object that meets the following requirements:

*   It must contain exactly one of the keys "`and`", "`or`", "`not`", "`href_matches`", or "`selector_matches`".

*   It must not contain any keys apart from the above or "`relative_to`".

*   If it contains the key "`relative_to`", then it must also contain the key "`href_matches`".

*   The value corresponding to the "`relative_to`" key, if present, must be either "`ruleset`" or "`document`".

*   The value corresponding to the "`and`" or "`or`" keys, if present, must be arrays of [valid document rule predicates](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-document-rule-predicate).

*   The value corresponding to the "`not`" key, if present, must be a [valid document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-document-rule-predicate).

*   The value corresponding to the "`href_matches`" key, if present, must be either a [valid URL pattern input](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-url-pattern-input) or an array of [valid URL pattern inputs](https://html.spec.whatwg.org/multipage/speculative-loading.html#valid-url-pattern-input).

*   The value corresponding to the "`selector_matches`" key, if present, must be either a [string](https://infra.spec.whatwg.org/#string) matching `<selector-list>` or an array of [strings](https://infra.spec.whatwg.org/#string) that match `<selector-list>`.

A valid URL pattern input is either:

*   a [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string) that can be successfully [parsed](https://urlpattern.spec.whatwg.org/#parse-a-constructor-string) as a URL pattern constructor string, or;

*   a JSON object whose keys are drawn from the members of the `URLPatternInit` dictionary and whose values are [scalar value strings](https://infra.spec.whatwg.org/#scalar-value-string).

##### 7.6.1.1 Data model[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-data-model)

A speculation rule set is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   prefetch rules, a [list](https://infra.spec.whatwg.org/#list) of [speculation rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule), initially empty

In the future, other rules will be possible, e.g., prerender rules. See Prerendering Revamped for such not-yet-accepted extensions. [[PRERENDERING-REVAMPED]](https://html.spec.whatwg.org/multipage/references.html#refsPRERENDERING-REVAMPED)

A speculation rule is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   URLs, an [ordered set](https://infra.spec.whatwg.org/#ordered-set) of [URLs](https://url.spec.whatwg.org/#concept-url)

*   predicate, a [document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate) or null

*   eagerness, a [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)

*   referrer policy, a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy)

*   tags, an [ordered set](https://infra.spec.whatwg.org/#ordered-set) of [speculation rule tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag)

*   requirements, an [ordered set](https://infra.spec.whatwg.org/#ordered-set) of [speculation rule requirements](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-requirement)

*   No-Vary-Search hint, a [URL search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#name-data-model)

* * *

A document rule predicate is one of the following:

*   a [document rule conjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-conjunction);

*   a [document rule disjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-disjunction);

*   a [document rule negation](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-negation);

*   a [document rule URL pattern predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-url-pattern-predicate); or

*   a [document rule selector predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-selector-predicate).

A document rule conjunction is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   clauses, a [list](https://infra.spec.whatwg.org/#list) of [document rule predicates](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate)

A document rule disjunction is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   clauses, a [list](https://infra.spec.whatwg.org/#list) of [document rule predicates](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate)

A document rule negation is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   clause, a [document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate)

A document rule URL pattern predicate is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   patterns, a [list](https://infra.spec.whatwg.org/#list) of [URL patterns](https://urlpattern.spec.whatwg.org/#url-pattern)

A document rule selector predicate is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   selectors, a [list](https://infra.spec.whatwg.org/#list) of [selectors](https://drafts.csswg.org/selectors/#selector)

* * *

A speculation rule eagerness is one of the following [strings](https://infra.spec.whatwg.org/#string):

"`immediate`"
The developer believes that performing the associated speculative loads is very likely to be worthwhile, and they might also expect that load to require significant lead time to complete. User agents should usually enact the speculative load candidate as soon as practical, subject only to considerations such as user preferences, device conditions, and resource limits.

"`eager`"
User agents should enact the speculative load candidate on even a slight suggestion that the user may navigate to this URL in the future. For instance, the user might have moved the cursor toward a link or hovered it, even momentarily, or paused scrolling when the link is one of the more prominent ones in the viewport. The author is seeking to capture as many navigations as possible, as early as possible.

"`moderate`"
User agents should enact the candidate if user behavior suggests the user may navigate to this URL in the near future. For instance, the user might have scrolled a link into the viewport and shown signs of being likely to click it, e.g., by moving the cursor over it for some time. The developer is seeking a balance between "`eager`" and "`conservative`".

"`conservative`"
User agents should enact the candidate only when the user is very likely to navigate to this URL at any moment. For instance, the user might have begun to interact with a link. The developer is seeking to capture some of the benefits of speculative loading with a fairly small tradeoff of resources.

A [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)A is less eager than another [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)B if A follows B in the above list.

A [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)A is at least as eager as another [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)B if A is not [less eager](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-eagerness-less-eager) than B.

* * *

A speculation rule tag is either an [ASCII string](https://infra.spec.whatwg.org/#ascii-string) whose [code points](https://infra.spec.whatwg.org/#code-point) are all in the range U+0020 to U+007E inclusive, or null.

This code point range restriction ensures the value can be sent in an HTTP header with no escaping or modification.

* * *

A speculation rule requirement is the string "`anonymous-client-ip-when-cross-origin`".

In the future, more possible requirements might be defined.

##### 7.6.1.2 Parsing[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-parsing)

Since speculative loading is a progressive enhancement, this standard is fairly conservative in its parsing behavior. In particular, unknown keys or invalid values usually cause parsing failure, since it is safer to do nothing than to possibly misinterpret a speculation rule.

That said, parsing failure for a single speculation rule still allows other speculation rules to be processed. It is only in the case of top-level misconfiguration that the entire speculation rule set is discarded.

To parse a speculation rule set string given a [string](https://infra.spec.whatwg.org/#string)input, a `Document`document, and a [URL](https://url.spec.whatwg.org/#concept-url)baseURL:

1.   Let parsed be the result of [parsing a JSON string to an Infra value](https://infra.spec.whatwg.org/#parse-a-json-string-to-an-infra-value) given input.

2.   If parsed is not a [map](https://infra.spec.whatwg.org/#ordered-map), then throw a `TypeError` indicating that the top-level value needs to be a JSON object.

3.   Let result be a new [speculation rule set](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set).

4.   Let tag be null.

5.   If parsed["`tag`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If parsed["`tag`"] is not a [speculation rule tag](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag), then throw a `TypeError` indicating that the speculation rule tag is invalid.

    2.   Set tag to parsed["`tag`"].

6.   Let typesToTreatAsPrefetch be « "`prefetch`" ».

7.   The user agent may [append](https://infra.spec.whatwg.org/#list-append) "`prerender`" to typesToTreatAsPrefetch.

[](https://html.spec.whatwg.org/multipage/speculative-loading.html#note-speculation-rules-parse-prerender-as-prefetch)Since this specification only includes prefetching, this allows user agents to treat requests for prerendering as requests for prefetching. User agents which implement prerendering, per the Prerendering Revamped specification, will instead interpret these as prerender requests. [[PRERENDERING-REVAMPED]](https://html.spec.whatwg.org/multipage/references.html#refsPRERENDERING-REVAMPED)

8.   [For each](https://infra.spec.whatwg.org/#list-iterate)type of typesToTreatAsPrefetch:

    1.   If parsed[type] [exists](https://infra.spec.whatwg.org/#map-exists):

        1.   If parsed[type] is a [list](https://infra.spec.whatwg.org/#list), then [for each](https://infra.spec.whatwg.org/#list-iterate)rule of parsed[type]:

            1.   Let rule be the result of [parsing a speculation rule](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-speculation-rule) given rule, tag, document, and baseURL.

            2.   If rule is null, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

            3.   [Append](https://infra.spec.whatwg.org/#list-append)rule to result's [prefetch rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-set-prefetch).

        2.   Otherwise, the user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the rules list for type needs to be a JSON array.

9.   Return result.

To parse a speculation rule given a [map](https://infra.spec.whatwg.org/#ordered-map)input, a [speculation rule tag](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag)rulesetLevelTag, a `Document`document, and a [URL](https://url.spec.whatwg.org/#concept-url)baseURL:

1.   If input is not a [map](https://infra.spec.whatwg.org/#ordered-map):

    1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the rule needs to be a JSON object.

    2.   Return null.

2.   If input has any [key](https://infra.spec.whatwg.org/#map-key) other than "`source`", "`urls`", "`where`", "`relative_to`", "`eagerness`", "`referrer_policy`", "`tag`", "`requires`", "`expects_no_vary_search`", or "`target_hint`":

    1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the rule has unrecognized keys.

    2.   Return null.

[](https://html.spec.whatwg.org/multipage/speculative-loading.html#note-speculation-rules-parse-target-hint)"`target_hint`" has no impact on the processing model in this standard. However, implementations of Prerendering Revamped can use it for prerendering rules, and so requiring user agents to fail parsing such rules would be counterproductive. [[PRERENDERING-REVAMPED]](https://html.spec.whatwg.org/multipage/references.html#refsPRERENDERING-REVAMPED).

3.   Let source be null.

4.   If input["`source`"] [exists](https://infra.spec.whatwg.org/#map-exists), then set source to input["`source`"].

5.   Otherwise, if input["`urls`"] [exists](https://infra.spec.whatwg.org/#map-exists) and input["`where`"] does not [exist](https://infra.spec.whatwg.org/#map-exists), then set source to "`list`".

6.   Otherwise, if input["`where`"] [exists](https://infra.spec.whatwg.org/#map-exists) and input["`urls`"] does not [exist](https://infra.spec.whatwg.org/#map-exists), then set source to "`document`".

7.   If source is neither "`list`" nor "`document`":

    1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that a source could not be inferred or an invalid source was specified.

    2.   Return null.

8.   Let urls be an empty [list](https://infra.spec.whatwg.org/#list).

9.   Let predicate be null.

10.   If source is "`list`":

    1.   If input["`where`"] [exists](https://infra.spec.whatwg.org/#map-exists):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that there were conflicting sources for this rule.

        2.   Return null.

    2.   If input["`relative_to`"] [exists](https://infra.spec.whatwg.org/#map-exists):

        1.   If input["`relative_to`"] is neither "`ruleset`" nor "`document`":

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied relative-to value was invalid.

            2.   Return null.

        2.   If input["`relative_to`"] is "`document`", then set baseURL to document's [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

    3.   If input["`urls`"] does not [exist](https://infra.spec.whatwg.org/#map-exists) or is not a [list](https://infra.spec.whatwg.org/#list):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied URL list was invalid.

        2.   Return null.

    4.   [For each](https://infra.spec.whatwg.org/#list-iterate)urlString of input["`urls`"]:

        1.   If urlString is not a string:

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied URL must be a string.

            2.   Return null.

        2.   Let parsedURL be the result of [URL parsing](https://url.spec.whatwg.org/#concept-url-parser)urlString with baseURL.

        3.   If parsedURL is failure, or parsedURL's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme):

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied URL string was unparseable.

            2.   [Continue](https://infra.spec.whatwg.org/#iteration-continue).

        4.   [Append](https://infra.spec.whatwg.org/#list-append)parsedURL to urls.

11.   If source is "`document`":

    1.   If input["`urls`"] or input["`relative_to`"] [exists](https://infra.spec.whatwg.org/#map-exists):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that there were conflicting sources for this rule.

        2.   Return null.

    2.   If input["`where`"] does not [exist](https://infra.spec.whatwg.org/#map-exists), then set predicate to a [document rule conjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-conjunction) whose [clauses](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-c-clauses) is an empty [list](https://infra.spec.whatwg.org/#list).

Such a predicate will match all links.

    3.   Otherwise, set predicate to the result of [parsing a document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-document-rule-predicate) given input["`where`"], document, and baseURL.

    4.   If predicate is null, then return null.

12.   Let eagerness be "`immediate`" if source is "`list`"; otherwise, "`conservative`".

13.   If input["`eagerness`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If input["`eagerness`"] is not a [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the eagerness was invalid.

        2.   Return null.

    2.   Set eagerness to input["`eagerness`"].

14.   Let referrerPolicy be the empty string.

15.   If input["`referrer_policy`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If input["`referrer_policy`"] is not a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the referrer policy was invalid.

        2.   Return null.

    2.   Set referrerPolicy to input["`referrer_policy`"].

16.   Let tags be an empty [ordered set](https://infra.spec.whatwg.org/#ordered-set).

17.   If rulesetLevelTag is not null, then [append](https://infra.spec.whatwg.org/#set-append)rulesetLevelTag to tags.

18.   If input["`tag`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If input["`tag`"] is not a [speculation rule tag](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the tag was invalid.

        2.   Return null.

    2.   [Append](https://infra.spec.whatwg.org/#set-append)input["`tag`"] to tags.

19.   If tags[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [append](https://infra.spec.whatwg.org/#set-append) null to tags.

20.   [Assert](https://infra.spec.whatwg.org/#assert): tags's [size](https://infra.spec.whatwg.org/#list-size) is either 1 or 2.

21.   Let requirements be an empty [ordered set](https://infra.spec.whatwg.org/#ordered-set).

22.   If input["`requires`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If input["`requires`"] is not a [list](https://infra.spec.whatwg.org/#list):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the requirements were not understood.

        2.   Return null.

    2.   [For each](https://infra.spec.whatwg.org/#list-iterate)requirement of input["`requires`"]:

        1.   If requirement is not a [speculation rule requirement](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-requirement):

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the requirement was not understood.

            2.   Return null.

        2.   [Append](https://infra.spec.whatwg.org/#set-append)requirement to requirements.

23.   Let noVarySearchHint be the [default URL search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#name-data-model).

24.   If input["`expects_no_vary_search`"] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   If input["`expects_no_vary_search`"] is not a [string](https://infra.spec.whatwg.org/#string):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the ``No-Vary-Search`` hint was invalid.

        2.   Return null.

    2.   Set noVarySearchHint to the result of [parsing a URL search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#parse-a-url-search-variance) given input["`expects_no_vary_search`"].

25.   Return a [speculation rule](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule) with:

[URLs](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-urls)urls[predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-predicate)predicate[eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-eagerness)eagerness[referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-referrer-policy)referrerPolicy[tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-tags)tags[requirements](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-requirements)requirements[No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-nvs-hint)noVarySearchHint

To parse a document rule predicate given a value input, a `Document`document, and a [URL](https://url.spec.whatwg.org/#concept-url)baseURL:

1.   If input is not a [map](https://infra.spec.whatwg.org/#ordered-map):

    1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate was invalid.

    2.   Return null.

2.   If input does not [contain](https://infra.spec.whatwg.org/#map-exists) exactly one of "`and`", "`or`", "`not`", "`href_matches`", or "`selector_matches`":

    1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate was empty or ambiguous.

    2.   Return null.

3.   Let predicateType be the single key found in the previous step.

4.   If predicateType is "`and`" or "`or`":

    1.   If input has any [key](https://infra.spec.whatwg.org/#map-key) other than predicateType:

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate had unexpected extra options.

        2.   Return null.

    2.   If input[predicateType] is not a [list](https://infra.spec.whatwg.org/#list):

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate had an invalid clause list.

        2.   Return null.

    3.   Let clauses be an empty [list](https://infra.spec.whatwg.org/#list).

    4.   [For each](https://infra.spec.whatwg.org/#list-iterate)rawClause of input[predicateType]:

        1.   Let clause be the result of [parsing a document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-document-rule-predicate) given rawClause, document, and baseURL.

        2.   If clause is null, then return null.

        3.   [Append](https://infra.spec.whatwg.org/#list-append)clause to clauses.

    5.   If predicateType is "`and`", then return a [document rule conjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-conjunction) whose [clauses](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-c-clauses) is clauses.

    6.   Return a [document rule disjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-disjunction) whose [clauses](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-d-clauses) is clauses.

5.   If predicateType is "`not`":

    1.   If input has any [key](https://infra.spec.whatwg.org/#map-key) other than "`not`":

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate had unexpected extra options.

        2.   Return null.

    2.   Let clause be the result of [parsing a document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-document-rule-predicate) given input[predicateType], document, and baseURL.

    3.   If clause is null, then return null.

    4.   Return a [document rule negation](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-negation) whose [clause](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-n-clause) is clause.

6.   If predicateType is "`href_matches`":

    1.   If input has any [key](https://infra.spec.whatwg.org/#map-key) other than "`href_matches`" or "`relative_to`":

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate had unexpected extra options.

        2.   Return null.

    2.   If input["`relative_to`"] [exists](https://infra.spec.whatwg.org/#map-exists):

        1.   If input["`relative_to`"] is neither "`ruleset`" nor "`document`":

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied relative-to value was invalid.

            2.   Return null.

        2.   If input["`relative_to`"] is "`document`", then set baseURL to document's [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

    3.   Let rawPatterns be input["`href_matches`"].

    4.   If rawPatterns is not a [list](https://infra.spec.whatwg.org/#list), then set rawPatterns to « rawPatterns ».

    5.   Let patterns be an empty [list](https://infra.spec.whatwg.org/#list).

    6.   [For each](https://infra.spec.whatwg.org/#list-iterate)rawPattern of rawPatterns:

        1.   Let pattern be the result of [building a URL pattern from an Infra value](https://urlpattern.spec.whatwg.org/#build-a-url-pattern-from-an-infra-value) given rawPattern and baseURL. If this step throws an exception, catch the exception and set pattern to null.

        2.   If pattern is null:

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied URL pattern was invalid.

            2.   Return null.

        3.   [Append](https://infra.spec.whatwg.org/#list-append)pattern to patterns.

    7.   Return a [document rule URL pattern predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-url-pattern-predicate) whose [patterns](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-urlpattern-patterns) is patterns.

7.   If predicateType is "`selector_matches`":

    1.   If input has any [key](https://infra.spec.whatwg.org/#map-key) other than "`selector_matches`":

        1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the document rule predicate had unexpected extra options.

        2.   Return null.

    2.   Let rawSelectors be input["`selector_matches`"].

    3.   If rawSelectors is not a [list](https://infra.spec.whatwg.org/#list), then set rawSelectors to « rawSelectors ».

    4.   Let selectors be an empty [list](https://infra.spec.whatwg.org/#list).

    5.   [For each](https://infra.spec.whatwg.org/#list-iterate)rawSelector of rawSelectors:

        1.   Let parsedSelectorList be failure.

        2.   If rawSelector is a string, then set parsedSelectorList to the result of [parsing a selector](https://drafts.csswg.org/selectors/#parse-a-selector) given rawSelector.

        3.   If parsedSelectorList is failure:

            1.   The user agent may [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) indicating that the supplied selector list was invalid.

            2.   Return null.

        4.   [For each](https://infra.spec.whatwg.org/#list-iterate)selector of parsedSelectorList, [append](https://infra.spec.whatwg.org/#list-append)selector to selectors.

    6.   Return a [document rule selector predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-selector-predicate) whose [selectors](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-cssselector-selectors) is selectors.

8.   [Assert](https://infra.spec.whatwg.org/#assert): this step is never reached, as one of the previous branches was taken.

##### 7.6.1.3 Processing model[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-processing-model)

A speculative load candidate is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   URL, a [URL](https://url.spec.whatwg.org/#concept-url)

*   No-Vary-Search hint, a [URL search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#name-data-model)

*   eagerness, a [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)

*   referrer policy, a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy)

*   tags, an [ordered set](https://infra.spec.whatwg.org/#ordered-set) of [speculation rule tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-tag)

A prefetch candidate is a [speculative load candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-load-candidate) with the following additional [item](https://infra.spec.whatwg.org/#struct-item):

*   anonymization policy, a [prefetch IP anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#prefetch-ip-anonymization-policy)

A prefetch IP anonymization policy is either null or a [cross-origin prefetch IP anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#cross-origin-prefetch-ip-anonymization-policy).

A cross-origin prefetch IP anonymization policy is a [struct](https://infra.spec.whatwg.org/#struct) whose single [item](https://infra.spec.whatwg.org/#struct-item) is its origin, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin).

* * *

A [speculative load candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-load-candidate)candidateA is redundant with another [speculative load candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-load-candidate)candidateB if the following steps return true:

1.   If candidateA's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) is not equal to candidateB's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint), then return false.

2.   If candidateA's [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) is not [equivalent modulo search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#name-comparing) to candidateB's [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) given candidateA's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint), then return false.

3.   Return true.

The requirement that the [No-Vary-Search hints](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) be equivalent is somewhat strict. It means that some cases which could theoretically be treated as matching, are not treated as such. Thus, redundant speculative loads could happen.

However, allowing more lenient matching makes the check no longer an equivalence relation, and producing such matches would require an implementation strategy that does a full comparison, instead of a simpler one using normalized URL keys. This is in line with the best practices for server operators, and attendant HTTP cache implementation notes, in [No Vary Search §6 Comparing](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#section-6).

In practice, we do not expect this to cause redundant speculative loads, since server operators and the corresponding speculation rules-writing web developers will follow best practices and use static ``No-Vary-Search`` header values/speculation rule hints.

Consider three [speculative load candidates](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-load-candidate):

1.   A has a [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) of `https://example.com?a=1&b=1` and a [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) parsed from `params=("a")`.

2.   B has a [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) of `https://example.com?a=2&b=1` and a [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) parsed from `params=("b")`.

3.   C has a [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) of `https://example.com?a=2&b=2` and a [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) parsed from `params=("a")`.

With the current definition of [redundant with](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-redundant-with), none of these candidates are redundant with each other. A [speculation rule set](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set) which contained all three could cause three separate speculative loads.

A definition which did not require equivalent [No-Vary-Search hints](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) could consider A and B to match (using A's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint)), and B and C to match (using B's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint)). But it could not consider A and C to match, so it would not be transitive, and thus not an equivalence relation.

* * *

Every `Document` has speculation rule sets, a [list](https://infra.spec.whatwg.org/#list) of [speculation rule sets](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set), initially empty.

Every `Document` has a consider speculative loads microtask queued, a boolean, initially false.

To consider speculative loads for a `Document`document:

1.   If document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is not a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then return.

Supporting speculative loads into [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) has some complexities and is not currently defined. It might be possible to define it in the future.

2.   If document's [consider speculative loads microtask queued](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads-microtask-queued) is true, then return.

3.   Set document's [consider speculative loads microtask queued](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads-microtask-queued) to true.

4.   [Queue a microtask](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) given document to run the following steps:

    1.   Set document's [consider speculative loads microtask queued](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads-microtask-queued) to false.

    2.   Run the [inner consider speculative loads steps](https://html.spec.whatwg.org/multipage/speculative-loading.html#inner-consider-speculative-loads-steps) for document.

In addition to the call sites explicitly given in this standard:

*   When style recalculation would cause selector matching results to change, the user agent must [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) for the relevant `Document`.

*   When the user indicates interest in [hyperlinks](https://html.spec.whatwg.org/multipage/links.html#hyperlink), in one of the [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) ways that the user agent uses to implement the [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness) heuristics, the user agent may [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) for the hyperlink's [node document](https://dom.spec.whatwg.org/#concept-node-document).

For example, a user agent which implements "`conservative`" eagerness by watching for `pointerdown` events would want to [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) as part of reacting to such events.

In this standard, every call to [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) is given just a `Document`, and the algorithm re-computes all possible candidates in a stateless way. A real implementation would likely cache previous computations, and pass along information from the call site to make updates more efficient. For example, if an `a` element's `href` attribute is changed, that specific element could be passed along in order to update only the related [speculative load candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-load-candidate).

Note that because of how [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) queues a microtask, by the time the [inner consider speculative loads steps](https://html.spec.whatwg.org/multipage/speculative-loading.html#inner-consider-speculative-loads-steps) are run, multiple updates (or [cancelations](https://html.spec.whatwg.org/multipage/speculative-loading.html#step-prefetch-record-cancel-and-discard)) might be processed together.

The inner consider speculative loads steps for a `Document`document are:

1.   If document is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return.

2.   Let prefetchCandidates be an empty [list](https://infra.spec.whatwg.org/#list).

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)ruleSet of document's [speculation rule sets](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-sr-sets):

    1.   [For each](https://infra.spec.whatwg.org/#list-iterate)rule of ruleSet's [prefetch rules](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-set-prefetch):

        1.   Let anonymizationPolicy be null.

        2.   If rule's [requirements](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-requirements)[contains](https://infra.spec.whatwg.org/#list-contain) "`anonymous-client-ip-when-cross-origin`", then set anonymizationPolicy to a [cross-origin prefetch IP anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#cross-origin-prefetch-ip-anonymization-policy) whose [origin](https://html.spec.whatwg.org/multipage/speculative-loading.html#copiap-origin) is document's [origin](https://dom.spec.whatwg.org/#concept-document-origin).

        3.   [For each](https://infra.spec.whatwg.org/#list-iterate)url of rule's [URLs](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-urls):

            1.   Let referrerPolicy be the result of [computing a speculative load referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#compute-a-speculative-load-referrer-policy) given rule and null.

            2.   [Append](https://infra.spec.whatwg.org/#list-append) a new [prefetch candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#prefetch-candidate) with

[URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url)url[No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint)rule's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-nvs-hint)[eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-eagerness)rule's [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-eagerness)[referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-referrer-policy)referrerPolicy[tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-tags)rule's [tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-tags)[anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-anonymization-policy)anonymizationPolicy
to prefetchCandidates.

        4.   If rule's [predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-predicate) is not null:

            1.   Let links be the result of [finding matching links](https://html.spec.whatwg.org/multipage/speculative-loading.html#find-matching-links) given document and rule's [predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-predicate).

            2.   [For each](https://infra.spec.whatwg.org/#list-iterate)link of links:

                1.   Let referrerPolicy be the result of [computing a speculative load referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#compute-a-speculative-load-referrer-policy) given rule and link.

                2.   [Append](https://infra.spec.whatwg.org/#list-append) a new [prefetch candidate](https://html.spec.whatwg.org/multipage/speculative-loading.html#prefetch-candidate) with

[URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url)link's [url](https://html.spec.whatwg.org/multipage/links.html#concept-hyperlink-url)[No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint)rule's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-nvs-hint)[eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-eagerness)rule's [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-eagerness)[referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-referrer-policy)referrerPolicy[tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-tags)rule's [tags](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-tags)[anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-anonymization-policy)anonymizationPolicy
to prefetchCandidates.

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)prefetchRecord of document's [prefetch records](https://wicg.github.io/nav-speculation/prefetch.html#document-prefetch-records):

    1.   If prefetchRecord's [source](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-source) is not "`speculation rules`", then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   [Assert](https://infra.spec.whatwg.org/#assert): prefetchRecord's [state](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-state) is not "`canceled`".

    3.   If prefetchRecord is not [still being speculated](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-still-being-speculated) given prefetchCandidates, then [cancel and discard](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-cancel-and-discard)prefetchRecord given document.

5.   Let prefetchCandidateGroups be an empty [list](https://infra.spec.whatwg.org/#list).

6.   [For each](https://infra.spec.whatwg.org/#list-iterate)candidate of prefetchCandidates:

    1.   Let group be « candidate ».

    2.   [Extend](https://infra.spec.whatwg.org/#list-extend)group with all [items](https://infra.spec.whatwg.org/#list-item) in prefetchCandidates, apart from candidate itself, which are [redundant with](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-redundant-with)candidate and whose [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-eagerness) is [at least as eager](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-eagerness-at-least-as-eager) as candidate's [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-eagerness).

    3.   If prefetchCandidateGroups[contains](https://infra.spec.whatwg.org/#list-contain) another group whose [items](https://infra.spec.whatwg.org/#list-item) are the same as group, ignoring order, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    4.   [Append](https://infra.spec.whatwg.org/#list-append)group to prefetchCandidateGroups.

The following speculation rules generate two [redundant](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-redundant-with)[prefetch candidates](https://html.spec.whatwg.org/multipage/speculative-loading.html#prefetch-candidate):

```
{
  "prefetch": [
    {
      "tag": "a",
      "urls": ["next.html"]
    },
    {
      "tag": "b",
      "urls": ["next.html"],
      "referrer_policy": "no-referrer"
    }
  ]
}
```

This step will create a single group containing them both, in the given order. (The second pass through will not create a group, since its contents would be the same as the first group, just in a different order.) This means that if the user agent chooses to execute the "may" step below to enact the group, it will enact the first candidate, and ignore the second. Thus, the request will be made with the [default referrer policy](https://w3c.github.io/webappsec-referrer-policy/#default-referrer-policy), instead of using "`no-referrer`".

However, the [collect tags from speculative load candidates](https://html.spec.whatwg.org/multipage/speculative-loading.html#collect-tags-from-speculative-load-candidates) algorithm will collect tags from both candidates in the group, so the ``Sec-Speculation-Tags`` header value will be ``"a", "b"``. This indicates to server operators that either rule could have caused the speculative load.

7.   [For each](https://infra.spec.whatwg.org/#list-iterate)group of prefetchCandidateGroups:

    1.   The user agent may run the following steps:

        1.   Let prefetchCandidate be group[0].

        2.   Let tagsToSend be the result of [collecting tags from speculative load candidates](https://html.spec.whatwg.org/multipage/speculative-loading.html#collect-tags-from-speculative-load-candidates) given group.

        3.   Let prefetchRecord be a new [prefetch record](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record) with

[source](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-source)"`speculation rules`"[URL](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-url)prefetchCandidate's [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url)[No-Vary-Search hint](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-no-vary-search-hint)prefetchCandidate's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint)[referrer policy](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-referrer-policy)prefetchCandidate's [referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-referrer-policy)[anonymization policy](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-anonymization-policy)prefetchCandidate's [anonymization policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-anonymization-policy)[tags](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-tags)tagsToSend
        4.   [Start a referrer-initiated navigational prefetch](https://wicg.github.io/nav-speculation/prefetch.html#start-a-referrer-initiated-navigational-prefetch) given document and prefetchRecord.

When deciding whether to execute this "may" step, user agents should consider prefetchCandidate's [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-eagerness), in accordance to the current behavior of the user and the definitions of [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness).

prefetchCandidate's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) can also be useful in implementing the heuristics defined for the [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness) values. For example, a user hovering of a link whose [URL](https://html.spec.whatwg.org/multipage/links.html#concept-hyperlink-url) is [equivalent modulo search variance](https://httpwg.org/http-extensions/draft-ietf-httpbis-no-vary-search.html#name-comparing) to prefetchCandidate's [URL](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-url) given prefetchCandidate's [No-Vary-Search hint](https://html.spec.whatwg.org/multipage/speculative-loading.html#sl-candidate-nvs-hint) could indicate to the user agent that performing this step would be useful.

When deciding whether to execute this "may" step, user agents should prioritize user preferences (express or implied, such as data-saver or battery-saver modes) over the eagerness supplied by the web developer.

To compute a speculative load referrer policy given a [speculation rule](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule)rule and an `a` element, `area` element, or null link:

1.   If rule's [referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-referrer-policy) is not the empty string, then return rule's [referrer policy](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-referrer-policy).

2.   If link is null, then return the empty string.

3.   Return link's [hyperlink referrer policy](https://html.spec.whatwg.org/multipage/links.html#hyperlink-referrer-policy).

* * *

To find matching links given a `Document`document and a [document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate)predicate:

1.   Let links be an empty [list](https://infra.spec.whatwg.org/#list).

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)[shadow-including descendant](https://dom.spec.whatwg.org/#concept-shadow-including-descendant)descendant of document, in [shadow-including tree order](https://dom.spec.whatwg.org/#concept-shadow-including-tree-order):

    1.   If descendant is not an `a` or `area` element with an `href` attribute, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   If descendant is not [being rendered](https://html.spec.whatwg.org/multipage/rendering.html#being-rendered) or is part of [skipped contents](https://drafts.csswg.org/css-contain/#skips-its-contents), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

Such links, though present in document, aren't available for the user to interact with, and thus are unlikely to be good candidates. In addition, they might not have their style or layout computed, which might make selector matching less efficient in user agents which skip some or all of that work for these elements.

    3.   If descendant's [url](https://html.spec.whatwg.org/multipage/links.html#concept-hyperlink-url) is null, or its [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    4.   If predicate[matches](https://html.spec.whatwg.org/multipage/speculative-loading.html#dr-predicate-matches)descendant, then [append](https://infra.spec.whatwg.org/#list-append)descendant to links.

3.   Return links.

A [document rule predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate)predicate matches an `a` or `area` element el if the following steps return true, switching on predicate's type:

[document rule conjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-conjunction)
1.   [For each](https://infra.spec.whatwg.org/#list-iterate)clause of predicate's [clauses](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-c-clauses):

    1.   If clause does not [match](https://html.spec.whatwg.org/multipage/speculative-loading.html#dr-predicate-matches)el, then return false.

2.   Return true.

[document rule disjunction](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-disjunction)
1.   [For each](https://infra.spec.whatwg.org/#list-iterate)clause of predicate's [clauses](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-d-clauses):

    1.   If clause[matches](https://html.spec.whatwg.org/multipage/speculative-loading.html#dr-predicate-matches)el, then return true.

2.   Return false.

[document rule negation](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-negation)
1.   If predicate's [clause](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-n-clause)[matches](https://html.spec.whatwg.org/multipage/speculative-loading.html#dr-predicate-matches)el, then return false.

2.   Return true.

[document rule URL pattern predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-url-pattern-predicate)
1.   [For each](https://infra.spec.whatwg.org/#list-iterate)pattern of predicate's [patterns](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-urlpattern-patterns):

    1.   If performing a [match](https://urlpattern.spec.whatwg.org/#url-pattern-match) given pattern and el's [url](https://html.spec.whatwg.org/multipage/links.html#concept-hyperlink-url) gives a non-null value, then return true.

2.   Return false.

[document rule selector predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-selector-predicate)
1.   [For each](https://infra.spec.whatwg.org/#list-iterate)selector of predicate's [selectors](https://html.spec.whatwg.org/multipage/speculative-loading.html#sr-dr-cssselector-selectors):

    1.   If performing a [match](https://drafts.csswg.org/selectors/#match-a-selector-against-an-element) given selector and el with the [scoping root](https://drafts.csswg.org/selectors/#scoping-root) set to el's [root](https://dom.spec.whatwg.org/#concept-tree-root) returns success, then return true.

2.   Return false.

* * *

Speculation rules features use the speculation rules task source, which is a [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source).

Because speculative loading is generally less important than processing tasks for the purpose of the current document, implementations might give [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) enqueued here an especially low priority.

#### 7.6.2 Navigational prefetching[](https://html.spec.whatwg.org/multipage/speculative-loading.html#navigational-prefetching)

For now, the navigational prefetching process is defined in the Prefetch specification. Moving it into this standard is tracked in [issue #11123](https://github.com/whatwg/html/issues/11123). [[PREFETCH]](https://html.spec.whatwg.org/multipage/references.html#refsPREFETCH)

This standard refers to the following concepts defined there:

*   [prefetch record](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record), and its items [source](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-source), [URL](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-url), [No-Vary-Search hint](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-no-vary-search-hint), [referrer policy](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-referrer-policy), [anonymization policy](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-anonymization-policy), [tags](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-tags), and [state](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-state)
*   [cancel and discard](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-cancel-and-discard)
*   [still being speculated](https://wicg.github.io/nav-speculation/prefetch.html#prefetch-record-still-being-speculated)
*   [prefetch records](https://wicg.github.io/nav-speculation/prefetch.html#document-prefetch-records)
*   [start a referrer-initiated navigational prefetch](https://wicg.github.io/nav-speculation/prefetch.html#start-a-referrer-initiated-navigational-prefetch)

The ``Speculation-Rules`` HTTP response header allows the developer to request that the user agent fetch and apply a given [speculation rule set](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-set) to the current . It is a [structured header](https://httpwg.org/specs/rfc8941.html) whose value must be a [list](https://httpwg.org/specs/rfc8941.html#list) of [strings](https://httpwg.org/specs/rfc8941.html#string) that are all [valid URL strings](https://url.spec.whatwg.org/#valid-url-string).

To given a document and a [response](https://fetch.spec.whatwg.org/#concept-response)response:

1.   Let parsedList be the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) given `` and "`list`" from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

2.   If parsedList is null, then return.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)item of parsedList:

    1.   If item is not a [string](https://infra.spec.whatwg.org/#string), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   Let url be the result of [URL parsing](https://url.spec.whatwg.org/#concept-url-parser)item with document's [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

    3.   If url is failure, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    4.   [In parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

        1.   Optionally, wait for an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) amount of time.

This allows the implementation to prioritize other work ahead of loading speculation rules, as especially during creation and header processing, there are often many more important things going on.

        2.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [speculation rules task source](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rules-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

            1.   Let request be a new [request](https://fetch.spec.whatwg.org/#concept-request) whose [URL](https://fetch.spec.whatwg.org/#concept-request-url) is url, [destination](https://fetch.spec.whatwg.org/#concept-request-destination) is "`speculationrules`", and [mode](https://fetch.spec.whatwg.org/#concept-request-mode) is "`cors`".

            2.   [Fetch](https://fetch.spec.whatwg.org/#concept-fetch)request with the following _[processResponseConsumeBody](https://fetch.spec.whatwg.org/#process-response-end-of-body)_ steps given [response](https://fetch.spec.whatwg.org/#concept-response)response and null, failure, or a [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)bodyBytes:

                1.   If bodyBytes is null or failure, then abort these steps.

                2.   If response's [status](https://fetch.spec.whatwg.org/#concept-response-status) is not an [ok status](https://fetch.spec.whatwg.org/#ok-status), then abort these steps.

                3.   If the result of [extracting a MIME type](https://fetch.spec.whatwg.org/#concept-header-extract-mime-type) from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list) does not have an [essence](https://mimesniff.spec.whatwg.org/#mime-type-essence) of "", then abort these steps.

                4.   Let bodyText be the result of [UTF-8 decoding](https://encoding.spec.whatwg.org/#utf-8-decode)bodyBytes.

                5.   Let ruleSet be the result of [parsing a speculation rule set string](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-speculation-rule-set-string) given bodyText, document, and response's [URL](https://fetch.spec.whatwg.org/#concept-response-url). If this throws an exception, then abort these steps.

                6.   [Append](https://infra.spec.whatwg.org/#list-append)ruleSet to document's [speculation rule sets](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-sr-sets).

                7.   [Consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) for document.

The ``Sec-Speculation-Tags`` HTTP request header specifies the web developer-provided tags associated with the speculative navigation request. It can also be used to distinguish speculative navigation requests from speculative subresource requests, since `` can be sent by both categories of requests.

The header is a [structured header](https://httpwg.org/specs/rfc8941.html) whose value must be a [list](https://httpwg.org/specs/rfc8941.html#list). The list can contain either [token](https://httpwg.org/specs/rfc8941.html#token) or [string](https://httpwg.org/specs/rfc8941.html#string) values. String values represent developer-provided tags, whereas token values represent predefined tags. As of now, the only predefined tag is `null`, which indicates a speculative navigation request with no developer-defined tag.

#### 7.6.5 Security considerations[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-security)

##### 7.6.5.1 Cross-site requests[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-cross-site-requests)

Speculative loads can be initiated by web pages to cross-site destinations. However, because such cross-site speculative loads are always done without [credentials](https://fetch.spec.whatwg.org/#credentials), as explained [below](https://html.spec.whatwg.org/multipage/speculative-loading-state-partitioning), ambient authority is limited to requests that are already possible via other mechanisms on the platform.

The ``Speculation-Rules`` header can also be used to issue requests, for JSON documents whose body will be [parsed as a speculation rule set string](https://html.spec.whatwg.org/multipage/speculative-loading.html#parse-a-speculation-rule-set-string). However, they use the "`same-origin`" [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode), the "`cors`" [mode](https://fetch.spec.whatwg.org/#concept-request-mode), and responses which do not use the `application/speculationrules+json`[MIME type essence](https://mimesniff.spec.whatwg.org/#mime-type-essence) are ignored, so they are not useful in mounting attacks.

##### 7.6.5.2 Injected content[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-injected-content)

Because links in a document can be selected for speculative loading via [document rule predicates](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate), developers need to be cautious if such links might contain user-generated markup. For example, if the `href` of a link can be entered by one user and displayed to all other users, a malicious user might choose a value like "`/logout`", causing other users' browsers to automatically log out of the site when that link is speculatively loaded. Using a [document rule selector predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-selector-predicate) to exclude such potentially-dangerous links, or using a [document rule URL pattern predicate](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-url-pattern-predicate) to allowlist known-safe links, are useful techniques in this regard.

As with all uses of the `script` element, developers need to be cautious about inserting user-provided content into `<script type=speculationrules>`'s [child text content](https://dom.spec.whatwg.org/#concept-child-text-content). In particular, the insertion of an unescaped closing `</script>` tag could be used to break out of the `script` element context and inject attacker-controlled markup.

The `<script type=speculationrules>` feature causes activity in response to content found in the document, so it is worth considering the options open to an attacker able to inject unescaped HTML. Such an attacker is already able to inject JavaScript or `iframe` elements. Speculative loads are generally less dangerous than arbitrary script execution. However, the use of [document rule predicates](https://html.spec.whatwg.org/multipage/speculative-loading.html#document-rule-predicate) could be used to speculatively load links in the document, and the existence of those loads could provide a vector for exfiltrating information about those links. Defense-in-depth against this possibility is provided by Content Security Policy. In particular, the `script-src` directive can be used to restrict the parsing of speculation rules `script` elements, and the `default-src` directive applies to navigational prefetch requests arising from such speculation rules. Additional defense is provided by the requirement that speculative loads are only performed to [potentially-trustworthy URLs](https://w3c.github.io/webappsec-secure-contexts/#potentially-trustworthy-url), so an on-path attacker would only have access to metadata and traffic analysis, and could not see the URLs directly. [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

It's generally not expected that user-generated content will be added as arbitrary response headers: server operators are already going to encounter significant trouble if this is possible. It is therefore unlikely that the ``Speculation-Rules`` header meaningfully expands the XSS attack surface. For this reason, Content Security Policy does not apply to the loading of rule sets via that header.

##### 7.6.5.3 IP anonymization[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-ip-anonymization)

This standard allows developers to request that navigational prefetches are performed using IP anonymization technology provided by the user agent. The details of this anonymization are not specified, but some general security principles apply.

To the extent IP anonymization is implemented using a proxy service, it is advisable to minimize the information available to the service operator and other entities on the network path. This likely involves, at a minimum, the use of TLS for the connection.

Site operators need to be aware that, similar to virtual private network (VPN) technology, the client IP address seen by the HTTP server might not exactly correspond to the user's actual network provider or location, and a traffic for multiple distinct subscribers could originate from a single client IP address. This can affect site operators' security and abuse prevention measures. IP anonymization measures might make an effort to use an egress IP address which has a similar geolocation or is located in the same jurisdiction as the user, but any such behavior is particular to the user agent and not guaranteed.

#### 7.6.6 Privacy considerations[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-privacy)

##### 7.6.6.1 Heuristics and optionality[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-heuristics)

The [consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) algorithm contains a crucial "may" step, which encourages user agents to [start referrer-initiated navigational prefetches](https://wicg.github.io/nav-speculation/prefetch.html#start-a-referrer-initiated-navigational-prefetch) based on a combination of the [speculation rule eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness) and other features of the user's environment. Because it can be observable to the document whether speculative loads are performed, user agents must take care to protect privacy when making such decisions—for instance by only using information which is already available to the origin. If these heuristics depend on any persistent state, that state must be erased whenever the user erases other site data. If the user agent automatically clears other site data from time to time, it must erase such persistent state at the same time.

The use of [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) instead of [site](https://html.spec.whatwg.org/multipage/browsers.html#site) here is intentional. Although same-site origins are generally allowed to coordinate if they wish, the web's security model is premised on preventing origins from accessing the data of other origins, even same-site ones. Thus, the user agent needs to be sure not to leak such data unintentionally across origins, not just across sites.

Examples of inputs which would be already known to the document:

*   author-supplied [eagerness](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculation-rule-eagerness)

*   order of appearance in the document

*   whether a link is in the viewport

*   whether the cursor is near a link

*   rendered size of a link

Examples of persistent data related to the origin (which the origin could have gathered itself) but which must be erased according to user intent:

*   whether the user has clicked this or similar links on this document or other documents on the same origin

Examples of device information which might be valuable in deciding whether speculative loading is appropriate, but which needs to be considered as part of the user agent's overall privacy posture because it can make the user more identifiable across origins:

*   coarse device class (CPU, memory)

*   coarse battery level

*   whether the network connection is known to be metered

*   any user-toggleable settings, such as a speculative loading toggle, a battery-saver toggle, or a data-saver toggle

##### 7.6.6.2 State partitioning[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-state-partitioning)

The [start a referrer-initiated navigational prefetch](https://wicg.github.io/nav-speculation/prefetch.html#start-a-referrer-initiated-navigational-prefetch) algorithm is designed to ensure that the HTTP requests that it issues behave consistently with how user agents partition [credentials](https://fetch.spec.whatwg.org/#credentials) according to [storage keys](https://storage.spec.whatwg.org/#storage-key). This property is maintained even for cross-partition prefetches, as follows.

If a future navigation using a prefetched response would load a document in the same partition, then at prefetch time, the partitioned credentials can be sent, as they can with subresource requests and scripted fetches. If such a future navigation would instead load a document in another partition, it would be inconsistent with the partitioning scheme to use partitioned credentials for the destination partition (since this would cross the boundary between partitions without a top-level navigation) and also inconsistent to use partitioned credentials within the originating partition (since this would result in the user seeing a document with different state than a non-prefetched navigation). Instead, a third, initially empty, partition is used for such requests. These requests therefore send along no credentials from either partition. However, the resulting prefetched response body constructed using this initially-empty partition can only be used if, at activation time, the destination partition contains no credentials.

This is somewhat similar to the behavior of only sending such prefetch requests if the destination partition is known ahead of time to not contain credentials. However, to avoid such behavior being used a way of probing for the presence of credentials, instead such prefetch requests are always completed, and in the case of conflicting credentials, their results are not used.

Redirects are possible between these two types of requests. A redirect from a same- to cross-partition URL could contain information derived from partitioned credentials in the originating partition; however, this is equivalent to the originating document fetching the same-partition URL itself and then issuing a request for the cross-partition URL. A redirect from a cross- to same-origin URL could carry credentials from the isolated partition, but since this partition has no prior state this does not enable tracking based on the user's prior browsing activity on that site, and the document could construct the same state by issuing uncredentialed requests itself.

##### 7.6.6.3 Identity joining[](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading-identity-joining)

Speculative loads provide a mechanism through which HTTP requests for later top-level navigation can be made without a user gesture. It is natural to ask whether it is possible for two coordinating sites to connect user identities.

Since existing [credentials](https://fetch.spec.whatwg.org/#credentials) for the destination site are not sent (as explained in the previous section), that site is limited in its ability to identify the user before navigation in a similar way to if the referrer site had simply used `fetch()` to make an uncredentialed request. Upon navigation, this becomes similar to ordinary navigation (e.g., by clicking a link that was not speculatively loaded).

To the extent that user agents attempt to mitigate identity joining for ordinary fetches and navigations, they can apply similar mitigations to speculatively-loaded navigations.

[Headers/X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options "The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame>, <iframe>, <embed> or <object>. Sites can use this to avoid click-jacking attacks, by ensuring that their content is not embedded into other sites.")

Support in all current engines.

Firefox 4+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android Yes Safari iOS Yes Chrome Android Yes WebView Android?Samsung Internet?Opera Android?

The ``X-Frame-Options`` HTTP response header is a way of controlling whether and how a may be loaded inside of a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable). For sites using CSP, the directive provides more granular control over the same situations. It was originally defined in HTTP Header Field X-Frame-Options, but the definition and processing model here supersedes that document. [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)[[RFC7034]](https://html.spec.whatwg.org/multipage/references.html#refsRFC7034)

In particular, HTTP Header Field X-Frame-Options specified an ``ALLOW-FROM`` variant of the header, but that is not to be implemented.

Per the below processing model, if both a CSP directive and an `` header are used in the same [response](https://fetch.spec.whatwg.org/#concept-response), then `` is ignored.

For web developers and conformance checkers, its value [ABNF](https://fetch.spec.whatwg.org/#abnf) is:

`X-Frame-Options = "DENY" / "SAMEORIGIN"`

To check a navigation response's adherence to ``X-Frame-Options``, given a [response](https://fetch.spec.whatwg.org/#concept-response)response, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [CSP list](https://w3c.github.io/webappsec-csp/#csp-list)cspList, and an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)destinationOrigin:

1.   If navigable is not a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable), then return true.

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)policy of cspList:

    1.   If policy's [disposition](https://w3c.github.io/webappsec-csp/#policy-disposition) is not "`enforce`", then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   If policy's [directive set](https://w3c.github.io/webappsec-csp/#policy-directive-set)[contains](https://infra.spec.whatwg.org/#list-contain) a directive, then return true.

3.   Let rawXFrameOptions be the result of [getting, decoding, and splitting](https://fetch.spec.whatwg.org/#concept-header-list-get-decode-split) `` from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

4.   Let xFrameOptions be a new [set](https://infra.spec.whatwg.org/#ordered-set).

5.   [For each](https://infra.spec.whatwg.org/#list-iterate)value of rawXFrameOptions, [append](https://infra.spec.whatwg.org/#set-append)value, [converted to ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase), to xFrameOptions.

6.   If xFrameOptions's [size](https://infra.spec.whatwg.org/#list-size) is greater than 1, and xFrameOptions[contains](https://infra.spec.whatwg.org/#list-contain) any of "`deny`", "`allowall`", or "`sameorigin`", then return false.

The intention here is to block any attempts at applying `` which were trying to do something valid, but appear confused.

This is the only impact of the legacy ``ALLOWALL`` value on the processing model.

7.   If xFrameOptions's [size](https://infra.spec.whatwg.org/#list-size) is greater than 1, then return true.

This means it contains multiple invalid values, which we treat the same way as if the header was omitted entirely.

8.   If xFrameOptions[0] is "`deny`", then return false.

9.   If xFrameOptions[0] is "`sameorigin`", then:

    1.   Let containerDocument be navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document).

    2.   [While](https://infra.spec.whatwg.org/#iteration-while)containerDocument is not null:

        1.   If containerDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with destinationOrigin, then return false.

        2.   Set containerDocument to containerDocument's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#doc-container-document).

10.   Return true.

If we've reached this point then we have a lone invalid value (which could potentially be one the legacy ``ALLOWALL`` or ``ALLOW-FROM`` forms). These are treated as if the header were omitted entirely.

* * *

The following table illustrates the processing of various values for the header, including non-conformant ones:

| ``X-Frame-Options`` | Valid | Result |
| --- | --- | --- |
| ``DENY`` | ✅ | embedding disallowed |
| ``SAMEORIGIN`` | ✅ | same-origin embedding allowed |
| ``INVALID`` | ❌ | embedding allowed |
| ``ALLOWALL`` | ❌ | embedding allowed |
| ``ALLOW-FROM=https://example.com/`` | ❌ | embedding allowed (from anywhere) |

The following table illustrates how various non-conformant cases involving multiple values are processed:

| ``X-Frame-Options`` | Result |
| --- | --- |
| ``SAMEORIGIN, SAMEORIGIN`` | same-origin embedding allowed |
| ``SAMEORIGIN, DENY`` | embedding disallowed |
| ``SAMEORIGIN,`` | embedding disallowed |
| ``SAMEORIGIN, ALLOWALL`` | embedding disallowed |
| ``SAMEORIGIN, INVALID`` | embedding disallowed |
| ``ALLOWALL, INVALID`` | embedding disallowed |
| ``ALLOWALL,`` | embedding disallowed |
| ``INVALID, INVALID`` | embedding allowed |

The same results are obtained whether the values are delivered in a single header whose value is comma-delimited, or in multiple headers.

The ``Refresh`` HTTP response header is the HTTP-equivalent to a element with an attribute in the [Refresh state](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv-refresh). It takes [the same value](https://html.spec.whatwg.org/multipage/semantics.html#conformance-attr-meta-http-equiv-refresh) and works largely the same. Its processing model is detailed in [create and initialize a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object).

### 7.9 Browser user interface considerations[](https://html.spec.whatwg.org/multipage/speculative-loading.html#nav-traversal-ui)

Browser user agents should provide the ability to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate), [reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload), and [stop loading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#nav-stop) any [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) in their [top-level traversable set](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable-set).

For example, via a location bar and reload/stop button UI.

Browser user agents should provide the ability to [traverse by a delta](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta) any [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) in their [top-level traversable set](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable-set).

For example, via back and forward buttons, possibly including long-press abilities to change the delta.

It is suggested that such user agents allow traversal by deltas greater than one, to avoid letting a page "trap" the user by stuffing the session history with spurious entries. (For example, via repeated calls to `history.pushState()` or [fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid).)

Some user agents have heuristics for translating a single "back" or "forward" button press into a larger delta, specifically to overcome such abuses. We are contemplating specifying these heuristics in [issue #7832](https://github.com/whatwg/html/issues/7832).

Browser user agents should offer users the ability to [create a fresh top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-fresh-top-level-traversable), given a user-provided or user agent-determined initial [URL](https://url.spec.whatwg.org/#concept-url).

For example, via a "new tab" or "new window" button.

Browser user agents should offer users the ability to arbitrarily [close](https://html.spec.whatwg.org/multipage/document-sequences.html#close-a-top-level-traversable) any [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) in their [top-level traversable set](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable-set).

For example, by clicking a "close tab" button.

* * *

Browser user agents may provide ways for the user to explicitly cause any [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) (not just a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)) to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate), [reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload), or [stop loading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#nav-stop).

For example, via a context menu.

Browser user agents may provide the ability for users to [destroy a top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-top-level-traversable).

For example, by force-closing a window containing one or more such [top-level traversables](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable).

* * *

When a user requests a [reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload) of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) whose [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource) is a [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource), the user agent should prompt the user to confirm the operation first, since otherwise transactions (e.g., purchases or database modifications) could be repeated.

When a user requests a [reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload) of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), user agents may provide a mechanism for ignoring any caches when reloading.

* * *

All calls to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) initiated by the mechanisms mentioned above must have the _[userInvolvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-user-involvement)_ argument set to "`browser UI`".

All calls to [reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload) initiated by the mechanisms mentioned above must have the _[userInvolvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload-user-involvement)_ argument set to "`browser UI`".

All calls to [traverse the history by a delta](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta) initiated by the mechanisms mentioned above must not pass a value for the _[sourceDocument](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-sourcedocument)_ argument.

* * *

The above recommendations, and the data structures in this specification, are not meant to place restrictions on how user agents represent the session history to the user.

For example, although a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)'s [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) are stored and maintained as a list, and the user agent is recommended to give an interface for [traversing that list by a delta](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta), a novel user agent could instead or in addition present a tree-like view, with each page having multiple "forward" pages that the user can choose between.

Similarly, although session history for all descendant [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) is stored in their [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable), user agents could present the user with a more nuanced per-[navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) view of the session history.

* * *

Browser user agents may use a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)'s [is popup](https://html.spec.whatwg.org/multipage/document-sequences.html#is-popup) boolean for the following purposes:

*   Deciding whether or not to provide a minimal web browser user interface for the corresponding [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable).

*   Performing the optional steps in [set up browsing context features](https://drafts.csswg.org/cssom-view/#set-up-browsing-context-features).

In both cases user agents might additionally incorporate user preferences, or present a choice as to whether to go down the popup route.

User agents that provide a minimal user interface for such popups are encouraged to not hide the browser's location bar.

[← 7.5 Document lifecycle](https://html.spec.whatwg.org/multipage/document-lifecycle.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8 Web application APIs →](https://html.spec.whatwg.org/multipage/webappapis.html)
