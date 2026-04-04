# Source: https://xmlgraphics.apache.org/fop/compliance.html

Title: Apache(tm) FOP - Compliance

URL Source: https://xmlgraphics.apache.org/fop/compliance.html

Markdown Content:
Apache™ FOP Compliance Page
---------------------------

W3C XSL-FO 1.1 Standard
-----------------------

One of Apache™ FOP's design goals is conformance to the [W3C XSL-FO 1.1 standard](http://www.w3.org/TR/xsl/), which specifies three levels of "conformance": basic, extended, and complete. Although FOP does not currently conform to any of these levels, it is nevertheless a useful work-in-progress for many applications. The information presented here demonstrates FOP's progress toward the goal of conformance, which progress consists of implementation of specific objects and properties in the standard. The information presented is useful not only to the developers as a sort of "to do" list, but also for setting proper expectations for users and potential users.

The following table shows the legend used for the tables below:

|  |  |
| --- | --- |
| yes | indicates conformance |
| partial | indicates partial conformance |
| no | indicates a lack of conformance |
| na | indicates that the item is "not applicable" to FOP usually because FOP supports only visual media |

XSL-FO Object Support Table (§6)
--------------------------------

The following is a summary of FOP's current support for the standard XSL-FO objects.

| Citation | Object Name | XSL-FO Conformance Level | FOP 1.0 | FOP 1.1 | FOP 2.0 | FOP 2.3 | FOP 2.4 to 2.8 | FOP 2.9 to 2.10 | FOP dev | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [§6.4](http://www.w3.org/TR/xsl/#d0e7057) | Declarations and Pagination and Layout Formatting Objects | { #fo-object-decl-section} |  |  |  |  |  |  |  |  |
| [§6.4.2](http://www.w3.org/TR/xsl/#fo_root) | root | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.3](http://www.w3.org/TR/xsl/#fo_declarations) | declarations | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.4](http://www.w3.org/TR/xsl/#fo_color-profile) | color-profile | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.5](http://www.w3.org/TR/xsl/#fo_page-sequence) | page-sequence | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.6](http://www.w3.org/TR/xsl/#fo_page-sequence-wrapper) | page-sequence-wrapper | Basic | no | no | no | no | no | no | no |  |
| [§6.4.7](http://www.w3.org/TR/xsl/#fo_layout-master-set) | layout-master-set | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.8](http://www.w3.org/TR/xsl/#fo_page-sequence-master) | page-sequence-master | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.9](http://www.w3.org/TR/xsl/#fo_single-page-master-reference) | single-page-master-reference | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.10](http://www.w3.org/TR/xsl/#fo_repeatable-page-master-reference) | repeatable-page-master-reference | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.11](http://www.w3.org/TR/xsl/#fo_repeatable-page-master-alternatives) | repeatable-page-master-alternatives | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.12](http://www.w3.org/TR/xsl/#fo_conditional-page-master-reference) | conditional-page-master-reference | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.13](http://www.w3.org/TR/xsl/#fo_simple-page-master) | simple-page-master | Basic | partial | partial | partial | partial | partial | partial | partial | The page width may not change among pages of the same page-sequence unless a forced break is inserted. |
| [§6.4.14](http://www.w3.org/TR/xsl/#fo_region-body) | region-body | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.15](http://www.w3.org/TR/xsl/#fo_region-before) | region-before | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.16](http://www.w3.org/TR/xsl/#fo_region-after) | region-after | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.17](http://www.w3.org/TR/xsl/#fo_region-start) | region-start | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.18](http://www.w3.org/TR/xsl/#fo_region-end) | region-end | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.19](http://www.w3.org/TR/xsl/#fo_flow) | flow | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.20](http://www.w3.org/TR/xsl/#fo_static-content) | static-content | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.21](http://www.w3.org/TR/xsl/#fo_title) | title | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.4.22](http://www.w3.org/TR/xsl/#fo_flow-map) | flow-map | Extended | no | no | no | no | no | no | no |  |
| [§6.4.23](http://www.w3.org/TR/xsl/#fo_flow-assignment) | flow-assignment | Extended | no | no | no | no | no | no | no |  |
| [§6.4.24](http://www.w3.org/TR/xsl/#fo_flow-source-list) | flow-source-list | Extended | no | no | no | no | no | no | no |  |
| [§6.4.25](http://www.w3.org/TR/xsl/#fo_flow-name-specifier) | flow-name-specifier | Extended | no | no | no | no | no | no | no |  |
| [§6.4.26](http://www.w3.org/TR/xsl/#fo_flow-target-list) | flow-target-list | Extended | no | no | no | no | no | no | no |  |
| [§6.4.27](http://www.w3.org/TR/xsl/#fo_region-name-specifier) | region-name-specifier | Extended | no | no | no | no | no | no | no |  |
| [§6.5](http://www.w3.org/TR/xsl/#d0e9451) | Block Formatting Objects | { #fo-object-block-section} |  |  |  |  |  |  |  |  |
| [§6.5.2](http://www.w3.org/TR/xsl/#fo_block) | block | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.5.3](http://www.w3.org/TR/xsl/#fo_block-container) | block-container | Extended | partial | partial | partial | partial | partial | partial | partial |  |
| [§6.6](http://www.w3.org/TR/xsl/#d0e9759) | Inline Formatting Objects | { #fo-object-inline-section} |  |  |  |  |  |  |  |  |
| [§6.6.2](http://www.w3.org/TR/xsl/#fo_bidi-override) | bidi-override | Extended | no | yes | yes | yes | yes | yes | yes |  |
| [§6.6.3](http://www.w3.org/TR/xsl/#fo_character) | character | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.6.4](http://www.w3.org/TR/xsl/#fo_initial-property-set) | initial-property-set | Extended | no | no | no | no | no | no | no |  |
| [§6.6.5](http://www.w3.org/TR/xsl/#fo_external-graphic) | external-graphic | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.6.6](http://www.w3.org/TR/xsl/#fo_instream-foreign-object) | instream-foreign-object | Extended | yes | yes | yes | yes | yes | yes | yes | Built-in support for SVG only, additional namespaces through optional extensions. |
| [§6.6.7](http://www.w3.org/TR/xsl/#fo_inline) | inline | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.6.8](http://www.w3.org/TR/xsl/#fo_inline-container) | inline-container | Extended | no | no | partial | partial | partial | partial | partial | [FOP 2.0] initial support: not all properties are implemented. See[FOP-1524](https://issues.apache.org/jira/browse/FOP-1524) |
| [§6.6.9](http://www.w3.org/TR/xsl/#fo_leader) | leader | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.6.10](http://www.w3.org/TR/xsl/#fo_page-number) | page-number | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.6.11](http://www.w3.org/TR/xsl/#fo_page-number-citation) | page-number-citation | Extended | partial | partial | partial | partial | partial | partial | partial | After the page number is known, no relayout is performed. The appearance may be suboptimal depending on the use case. |
| [§6.6.12](http://www.w3.org/TR/xsl/#fo_page-number-citation-last) | page-number-citation-last | Extended | partial | partial | partial | partial | partial | partial | partial | Works only for page-sequence so far. After the page number is known, no relayout is performed. The appearance may be suboptimal depending on the use case. |
| [§6.6.13](http://www.w3.org/TR/xsl/#fo_folio-prefix) | folio-prefix | Extended | no | no | no | no | no | no | no |  |
| [§6.6.14](http://www.w3.org/TR/xsl/#fo_folio-suffix) | folio-suffix | Extended | no | no | no | no | no | no | no |  |
| [§6.6.15](http://www.w3.org/TR/xsl/#fo_scaling-value-citation) | scaling-value-citation | Extended | no | no | no | no | no | no | no |  |
| [§6.7](http://www.w3.org/TR/xsl/#d0e11404) | Table Formatting Objects | { #fo-object-table-section} |  |  |  |  |  |  |  |  |
| [§6.7.2](http://www.w3.org/TR/xsl/#fo_table-and-caption) | table-and-caption | Basic | no | no | no | no | no | no | no |  |
| [§6.7.3](http://www.w3.org/TR/xsl/#fo_table) | table | Basic | partial | partial | partial | partial | partial | partial | partial | No support for auto layout yet |
| [§6.7.4](http://www.w3.org/TR/xsl/#fo_table-column) | table-column | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.7.5](http://www.w3.org/TR/xsl/#fo_table-caption) | table-caption | Extended | no | no | no | no | no | no | no |  |
| [§6.7.6](http://www.w3.org/TR/xsl/#fo_table-header) | table-header | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.7.7](http://www.w3.org/TR/xsl/#fo_table-footer) | table-footer | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.7.8](http://www.w3.org/TR/xsl/#fo_table-body) | table-body | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.7.9](http://www.w3.org/TR/xsl/#fo_table-row) | table-row | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.7.10](http://www.w3.org/TR/xsl/#fo_table-cell) | table-cell | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.8](http://www.w3.org/TR/xsl/#d0e12374) | List Formatting Objects | { #fo-object-list-section} |  |  |  |  |  |  |  |  |
| [§6.8.2](http://www.w3.org/TR/xsl/#fo_list-block) | list-block | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.8.3](http://www.w3.org/TR/xsl/#fo_list-item) | list-item | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.8.4](http://www.w3.org/TR/xsl/#fo_list-item-body) | list-item-body | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.8.5](http://www.w3.org/TR/xsl/#fo_list-item-label) | list-item-label | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.9](http://www.w3.org/TR/xsl/#d0e12855) | Link and Multi Formatting Objects | { #fo-object-link-section} |  |  |  |  |  |  |  |  |
| [§6.9.2](http://www.w3.org/TR/xsl/#fo_basic-link) | basic-link | Extended | yes | yes | yes | yes | yes | yes | yes | both internal and external supported |
| [§6.9.3](http://www.w3.org/TR/xsl/#fo_multi-switch) | multi-switch | Extended | no | no | partial | partial | partial | partial | partial | [FOP 2.0] initial support: used with fox:auto-toggle extension |
| [§6.9.4](http://www.w3.org/TR/xsl/#fo_multi-case) | multi-case | Basic | no | no | partial | partial | partial | partial | partial | [FOP 2.0] initial support: space attributes not currently supported; dynamic content inside a table cell does not work |
| [§6.9.5](http://www.w3.org/TR/xsl/#fo_multi-toggle) | multi-toggle | Extended | no | no | no | no | no | no | no |  |
| [§6.9.6](http://www.w3.org/TR/xsl/#fo_multi-properties) | multi-properties | Extended | no | no | no | no | no | no | no |  |
| [§6.9.7](http://www.w3.org/TR/xsl/#fo_multi-property-set) | multi-property-set | Extended | no | no | no | no | no | no | no |  |
| [§6.10](http://www.w3.org/TR/xsl11/#d0e13293) | Formatting Objects for Indexing | { #fo-object-indexing-section} |  |  |  |  |  |  |  |  |
| [§6.10.2](http://www.w3.org/TR/xsl11/#fo_index-page-number-prefix) | index-page-number-prefix | Extended | no | no | no | no | no | no | no |  |
| [§6.10.3](http://www.w3.org/TR/xsl11/#fo_index-page-number-suffix) | index-page-number-suffix | Extended | no | no | no | no | no | no | no |  |
| [§6.10.4](http://www.w3.org/TR/xsl11/#fo_index-range-begin) | index-range-begin | Extended | no | no | no | no | no | no | no |  |
| [§6.10.5](http://www.w3.org/TR/xsl11/#fo_index-range-end) | index-range-end | Extended | no | no | no | no | no | no | no |  |
| [§6.10.6](http://www.w3.org/TR/xsl11/#fo_index-key-reference) | index-key-reference | Extended | no | no | no | no | no | no | no |  |
| [§6.10.7](http://www.w3.org/TR/xsl11/#fo_index-page-citation-list) | index-page-citation-list | Extended | no | no | no | no | no | no | no |  |
| [§6.10.8](http://www.w3.org/TR/xsl11/#fo_index-page-citation-list-separator) | index-page-citation-list-separator | Extended | no | no | no | no | no | no | no |  |
| [§6.10.9](http://www.w3.org/TR/xsl11/#fo_index-page-citation-range-separator) | index-page-citation-range-separator | Extended | no | no | no | no | no | no | no |  |
| [§6.11](http://www.w3.org/TR/xsl11/#d0e14206) | Formatting Objects for Bookmarks | { #fo-object-bookmarks-section} |  |  |  |  |  |  |  |  |
| [§6.11.1](http://www.w3.org/TR/xsl11/#fo_bookmark-tree) | bookmark-tree | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.11.2](http://www.w3.org/TR/xsl11/#fo_bookmark) | bookmark | Extended | partial | partial | partial | partial | partial | partial | partial | external-destination is not yet supported. |
| [§6.11.3](http://www.w3.org/TR/xsl11/#fo_bookmark-title) | bookmark-title | Extended | partial | partial | partial | partial | partial | partial | partial | color, font-style and font-weight are not supported, yet. |
| [§6.12](http://www.w3.org/TR/xsl/#d0e14340) | Out-of-line Formatting Objects | { #fo-object-outofline-section} |  |  |  |  |  |  |  |  |
| [§6.12.2](http://www.w3.org/TR/xsl/#fo_float) | float | Extended | no | no | partial | partial | partial | partial | partial | [See restrictions](http://xmlgraphics.apache.org/fop/fo.html#floats) |
| [§6.12.3](http://www.w3.org/TR/xsl/#fo_footnote) | footnote | Extended | partial | partial | partial | partial | partial | partial | partial | Restrictions with multi-column documents. |
| [§6.12.4](http://www.w3.org/TR/xsl/#fo_footnote-body) | footnote-body | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.13](http://www.w3.org/TR/xsl/#d0e14653) | Other Formatting Objects | { #fo-object-other-section} |  |  |  |  |  |  |  |  |
| [§6.13.2](http://www.w3.org/TR/xsl/#fo_change-bar-begin) | change-bar-begin | Extended | no | no | no | no | yes | yes | yes |  |
| [§6.13.3](http://www.w3.org/TR/xsl/#fo_change-bar-end) | change-bar-end | Extended | no | no | no | no | yes | yes | yes |  |
| [§6.13.4](http://www.w3.org/TR/xsl/#fo_wrapper) | wrapper | Basic | yes | yes | yes | yes | yes | yes | yes | Only works as expected with inline-level content. |
| [§6.13.5](http://www.w3.org/TR/xsl/#fo_marker) | marker | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.13.6](http://www.w3.org/TR/xsl/#fo_retrieve-marker) | retrieve-marker | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§6.13.7](http://www.w3.org/TR/xsl/#fo_retrieve-table-marker) | retrieve-table-marker | Extended | no | no | partial | partial | partial | partial | partial | [FOP 2.0] initial support: marker element needs to be an element that does not change the BPD of the containing cell. |

XSL-FO Property Support Table (§7)
----------------------------------

The following is a summary of FOP's current support for the standard XSL-FO properties.

| Citation | Property Name | XSL-FO Conformance Level | FOP 1.0 | FOP 1.1 | FOP 2.0 | FOP 2.3 | FOP 2.4 to 2.8 | FOP 2.9 to 2.10 | FOP dev | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [§7.5](http://www.w3.org/TR/xsl/#common-accessibility-properties) | Common Accessibility Properties | { #fo-property-commonaccess-section} |  |  |  |  |  |  |  |  |
| [§7.5.1](http://www.w3.org/TR/xsl/#source-document) | source-document | Basic | no | no | no | no | no | no | no |  |
| [§7.5.2](http://www.w3.org/TR/xsl/#role) | role | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.6](http://www.w3.org/TR/xsl/#common-absolute-position-properties) | Common Absolute Position Properties | { #fo-property-commonabspos-section} |  |  |  |  |  |  |  |  |
| [§7.6.1](http://www.w3.org/TR/xsl/#absolute-position) | absolute-position | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.6.2](http://www.w3.org/TR/xsl/#top) | top | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.6.3](http://www.w3.org/TR/xsl/#right) | right | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.6.4](http://www.w3.org/TR/xsl/#bottom) | bottom | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.6.5](http://www.w3.org/TR/xsl/#left) | left | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.7](http://www.w3.org/TR/xsl/#common-aural-properties) | Common Aural Properties | { #fo-property-commonaural-section} |  |  |  |  |  |  |  |  |
| [§7.7.1](http://www.w3.org/TR/xsl/#azimuth) | azimuth | Basic | na | na | na | na | na | na | na |  |
| [§7.7.2](http://www.w3.org/TR/xsl/#cue-after) | cue-after | Basic | na | na | na | na | na | na | na |  |
| [§7.7.3](http://www.w3.org/TR/xsl/#cue-before) | cue-before | Basic | na | na | na | na | na | na | na |  |
| [§7.7.4](http://www.w3.org/TR/xsl/#elevation) | elevation | Basic | na | na | na | na | na | na | na |  |
| [§7.7.5](http://www.w3.org/TR/xsl/#pause-after) | pause-after | Basic | na | na | na | na | na | na | na |  |
| [§7.7.6](http://www.w3.org/TR/xsl/#pause-before) | pause-before | Basic | na | na | na | na | na | na | na |  |
| [§7.7.7](http://www.w3.org/TR/xsl/#pitch) | pitch | Basic | na | na | na | na | na | na | na |  |
| [§7.7.8](http://www.w3.org/TR/xsl/#pitch-range) | pitch-range | Basic | na | na | na | na | na | na | na |  |
| [§7.7.9](http://www.w3.org/TR/xsl/#play-during) | play-during | Basic | na | na | na | na | na | na | na |  |
| [§7.7.10](http://www.w3.org/TR/xsl/#richness) | richness | Basic | na | na | na | na | na | na | na |  |
| [§7.7.11](http://www.w3.org/TR/xsl/#speak) | speak | Basic | na | na | na | na | na | na | na |  |
| [§7.7.12](http://www.w3.org/TR/xsl/#speak-header) | speak-header | Basic | na | na | na | na | na | na | na |  |
| [§7.7.13](http://www.w3.org/TR/xsl/#speak-numeral) | speak-numeral | Basic | na | na | na | na | na | na | na |  |
| [§7.7.14](http://www.w3.org/TR/xsl/#speak-punctuation) | speak-punctuation | Basic | na | na | na | na | na | na | na |  |
| [§7.7.15](http://www.w3.org/TR/xsl/#speech-rate) | speech-rate | Basic | na | na | na | na | na | na | na |  |
| [§7.7.16](http://www.w3.org/TR/xsl/#stress) | stress | Basic | na | na | na | na | na | na | na |  |
| [§7.7.17](http://www.w3.org/TR/xsl/#voice-family) | voice-family | Basic | na | na | na | na | na | na | na |  |
| [§7.7.18](http://www.w3.org/TR/xsl/#volume) | volume | Basic | na | na | na | na | na | na | na |  |
| [§7.8](http://www.w3.org/TR/xsl/#common-border-padding-and-background-properties) | Common Border, Padding, and Background Properties | { #fo-property-commonenv-section} |  |  |  |  |  |  |  |  |
| [§7.8.1](http://www.w3.org/TR/xsl/#background-attachment) | background-attachment | Extended | no | no | no | no | no | no | no |  |
| [§7.8.2](http://www.w3.org/TR/xsl/#background-color) | background-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.3](http://www.w3.org/TR/xsl/#background-image) | background-image | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.4](http://www.w3.org/TR/xsl/#background-repeat) | background-repeat | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.5](http://www.w3.org/TR/xsl/#background-position-horizontal) | background-position-horizontal | Extended | partial | partial | partial | partial | partial | partial | partial | Ignored when background-repeat set to "repeat" or "repeat-x" |
| [§7.8.6](http://www.w3.org/TR/xsl/#background-position-vertical) | background-position-vertical | Extended | partial | partial | partial | partial | partial | partial | partial | Ignored when background-repeat set to "repeat" or "repeat-y" |
| [§7.8.7](http://www.w3.org/TR/xsl/#border-before-color) | border-before-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.8](http://www.w3.org/TR/xsl/#border-before-style) | border-before-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.9](http://www.w3.org/TR/xsl/#border-before-width) | border-before-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.10](http://www.w3.org/TR/xsl/#border-after-color) | border-after-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.11](http://www.w3.org/TR/xsl/#border-after-style) | border-after-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.12](http://www.w3.org/TR/xsl/#border-after-width) | border-after-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.13](http://www.w3.org/TR/xsl/#border-start-color) | border-start-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.14](http://www.w3.org/TR/xsl/#border-start-style) | border-start-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.15](http://www.w3.org/TR/xsl/#border-start-width) | border-start-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.16](http://www.w3.org/TR/xsl/#border-end-color) | border-end-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.17](http://www.w3.org/TR/xsl/#border-end-style) | border-end-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.18](http://www.w3.org/TR/xsl/#border-end-width) | border-end-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.19](http://www.w3.org/TR/xsl/#border-top-color) | border-top-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.20](http://www.w3.org/TR/xsl/#border-top-style) | border-top-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.21](http://www.w3.org/TR/xsl/#border-top-width) | border-top-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.22](http://www.w3.org/TR/xsl/#border-bottom-color) | border-bottom-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.23](http://www.w3.org/TR/xsl/#border-bottom-style) | border-bottom-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.24](http://www.w3.org/TR/xsl/#border-bottom-width) | border-bottom-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.25](http://www.w3.org/TR/xsl/#border-left-color) | border-left-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.26](http://www.w3.org/TR/xsl/#border-left-style) | border-left-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.27](http://www.w3.org/TR/xsl/#border-left-width) | border-left-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.28](http://www.w3.org/TR/xsl/#border-right-color) | border-right-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.29](http://www.w3.org/TR/xsl/#border-right-style) | border-right-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.30](http://www.w3.org/TR/xsl/#border-right-width) | border-right-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.31](http://www.w3.org/TR/xsl/#padding-before) | padding-before | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.32](http://www.w3.org/TR/xsl/#padding-after) | padding-after | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.33](http://www.w3.org/TR/xsl/#padding-start) | padding-start | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.34](http://www.w3.org/TR/xsl/#padding-end) | padding-end | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.35](http://www.w3.org/TR/xsl/#padding-top) | padding-top | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.36](http://www.w3.org/TR/xsl/#padding-bottom) | padding-bottom | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.37](http://www.w3.org/TR/xsl/#padding-left) | padding-left | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.8.38](http://www.w3.org/TR/xsl/#padding-right) | padding-right | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.9](http://www.w3.org/TR/xsl/#common-font-properties) | Common Font Properties | { #fo-property-commonfont-section} |  |  |  |  |  |  |  |  |
| [§7.9.2](http://www.w3.org/TR/xsl/#font-family) | font-family | Basic | partial | partial | partial | partial | partial | yes | yes |  |
| [§7.9.3](http://www.w3.org/TR/xsl/#font-selection-strategy) | font-selection-strategy | Complete | no | no | no | no | no | yes | yes |  |
| [§7.9.4](http://www.w3.org/TR/xsl/#font-size) | font-size | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.9.5](http://www.w3.org/TR/xsl/#font-stretch) | font-stretch | Extended | no | no | no | no | no | no | no |  |
| [§7.9.6](http://www.w3.org/TR/xsl/#font-size-adjust) | font-size-adjust | Extended | no | no | no | no | no | no | no |  |
| [§7.9.7](http://www.w3.org/TR/xsl/#font-style) | font-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.9.8](http://www.w3.org/TR/xsl/#font-variant) | font-variant | Basic | no | no | no | no | no | no | no |  |
| [§7.9.9](http://www.w3.org/TR/xsl/#font-weight) | font-weight | Basic | partial | partial | partial | partial | partial | partial | partial | TODO <relative> font weights |
| [§7.10](http://www.w3.org/TR/xsl/#common-hyphenation-properties) | Common Hyphenation Properties | { #fo-property-commonhyphen-section} |  |  |  |  |  |  |  |  |
| [§7.10.1](http://www.w3.org/TR/xsl/#country) | country | Extended | yes | yes | yes | yes | yes | yes | yes | For PDF output: Only 2-letter codes from ISO 3166 are supported properly to identify the natural language! |
| [§7.10.2](http://www.w3.org/TR/xsl/#language) | language | Extended | yes | yes | yes | yes | yes | yes | yes | For PDF output: Only 2-letter codes from ISO 639 are supported properly to identify the natural language! Also used with complex scripts features. |
| [§7.10.3](http://www.w3.org/TR/xsl/#script) | script | Extended | no | yes | yes | yes | yes | yes | yes | Used with complex scripts features to override default script heuristics. |
| [§7.10.4](http://www.w3.org/TR/xsl/#hyphenate) | hyphenate | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.10.5](http://www.w3.org/TR/xsl/#hyphenation-character) | hyphenation-character | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.10.6](http://www.w3.org/TR/xsl/#hyphenation-push-character-count) | hyphenation-push-character-count | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.10.7](http://www.w3.org/TR/xsl/#hyphenation-remain-character-count) | hyphenation-remain-character-count | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11](http://www.w3.org/TR/xsl/#common-margin-properties-block) | Common Margin Properties - Block | { #fo-property-commonmarginblock-section} |  |  |  |  |  |  |  |  |
| [§7.11.1](http://www.w3.org/TR/xsl/#margin-top) | margin-top | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11.2](http://www.w3.org/TR/xsl/#margin-bottom) | margin-bottom | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11.3](http://www.w3.org/TR/xsl/#margin-left) | margin-left | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11.4](http://www.w3.org/TR/xsl/#margin-right) | margin-right | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11.5](http://www.w3.org/TR/xsl/#space-before) | space-before | Basic | partial | partial | partial | partial | partial | partial | partial | Space adjustment may not fully work everywhere, yet. |
| [§7.11.6](http://www.w3.org/TR/xsl/#space-after) | space-after | Basic | partial | partial | partial | partial | partial | partial | partial | Space adjustment may not fully work everywhere, yet. |
| [§7.11.7](http://www.w3.org/TR/xsl/#start-indent) | start-indent | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.11.8](http://www.w3.org/TR/xsl/#end-indent) | end-indent | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.12](http://www.w3.org/TR/xsl/#common-margin-properties-inline) | Common Margin Properties - Inline | { #fo-property-commonmargininline-section} |  |  |  |  |  |  |  |  |
| [§7.12.1](http://www.w3.org/TR/xsl/#d0e21775) | margin-top | Basic | no | no | no | no | no | no | no |  |
| [§7.12.2](http://www.w3.org/TR/xsl/#d0e21783) | margin-bottom | Basic | no | no | no | no | no | no | no |  |
| [§7.12.3](http://www.w3.org/TR/xsl/#d0e21791) | margin-left | Basic | no | no | no | no | no | no | no |  |
| [§7.12.4](http://www.w3.org/TR/xsl/#d0e21799) | margin-right | Basic | no | no | no | no | no | no | no |  |
| [§7.12.5](http://www.w3.org/TR/xsl/#space-end) | space-end | Basic | no | no | no | no | no | no | no |  |
| [§7.12.6](http://www.w3.org/TR/xsl/#space-start) | space-start | Basic | no | no | no | no | no | no | no |  |
| [§7.13](http://www.w3.org/TR/xsl/#common-relative-position-properties) | Common Relative Position Properties | { #fo-property-commonrelpos-section} |  |  |  |  |  |  |  |  |
| [§7.13.1](http://www.w3.org/TR/xsl/#d0e21934) | top | Extended | no | no | no | no | no | no | no |  |
| [§7.13.2](http://www.w3.org/TR/xsl/#d0e21942) | right | Extended | no | no | no | no | no | no | no |  |
| [§7.13.3](http://www.w3.org/TR/xsl/#d0e21950) | bottom | Extended | no | no | no | no | no | no | no |  |
| [§7.13.4](http://www.w3.org/TR/xsl/#d0e21958) | left | Extended | no | no | no | no | no | no | no |  |
| [§7.13.5](http://www.w3.org/TR/xsl/#relative-position) | relative-position | Extended | no | no | no | no | no | no | no |  |
| [§7.14](http://www.w3.org/TR/xsl/#area-alignment) | Area Alignment Properties | { #fo-property-areaalign-section} |  |  |  |  |  |  |  |  |
| [§7.14.1](http://www.w3.org/TR/xsl/#alignment-adjust) | alignment-adjust | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.14.2](http://www.w3.org/TR/xsl/#alignment-baseline) | alignment-baseline | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.14.3](http://www.w3.org/TR/xsl/#baseline-shift) | baseline-shift | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.14.4](http://www.w3.org/TR/xsl/#display-align) | display-align | Extended | partial | partial | partial | partial | partial | partial | partial | TODO Check e-g, i-f-o. |
| [§7.14.5](http://www.w3.org/TR/xsl/#dominant-baseline) | dominant-baseline | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.14.6](http://www.w3.org/TR/xsl/#relative-align) | relative-align | Extended | no | no | no | no | no | no | no |  |
| [§7.15](http://www.w3.org/TR/xsl/#d0e22982) | Area Dimension Properties | { #fo-property-areadim-section} |  |  |  |  |  |  |  |  |
| [§7.15.1](http://www.w3.org/TR/xsl/#allowed-height-scale) | allowed-height-scale | Extended | no | no | no | no | no | no | no |  |
| [§7.15.2](http://www.w3.org/TR/xsl/#allowed-width-scale) | allowed-width-scale | Extended | no | no | no | no | no | no | no |  |
| [§7.15.3](http://www.w3.org/TR/xsl/#block-progression-dimension) | block-progression-dimension | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.4](http://www.w3.org/TR/xsl/#content-height) | content-height | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.5](http://www.w3.org/TR/xsl/#content-width) | content-width | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.6](http://www.w3.org/TR/xsl/#height) | height | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.7](http://www.w3.org/TR/xsl/#inline-progression-dimension) | inline-progression-dimension | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.8](http://www.w3.org/TR/xsl/#max-height) | max-height | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.9](http://www.w3.org/TR/xsl/#max-width) | max-width | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.10](http://www.w3.org/TR/xsl/#min-height) | min-height | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.11](http://www.w3.org/TR/xsl/#min-width) | min-width | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.12](http://www.w3.org/TR/xsl/#scaling) | scaling | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.15.13](http://www.w3.org/TR/xsl/#scaling-method) | scaling-method | Extended | no | no | no | no | no | no | no |  |
| [§7.15.14](http://www.w3.org/TR/xsl/#width) | width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16](http://www.w3.org/TR/xsl/#d0e24119) | Block and Line-related Properties | { #fo-property-blockandline-section} |  |  |  |  |  |  |  |  |
| [§7.16.1](http://www.w3.org/TR/xsl/#hyphenation-keep) | hyphenation-keep | Extended | no | no | no | no | no | no | no |  |
| [§7.16.2](http://www.w3.org/TR/xsl/#hyphenation-ladder-count) | hyphenation-ladder-count | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.3](http://www.w3.org/TR/xsl/#last-line-end-indent) | last-line-end-indent | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.4](http://www.w3.org/TR/xsl/#line-height) | line-height | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.5](http://www.w3.org/TR/xsl/#line-height-shift-adjustment) | line-height-shift-adjustment | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.6](http://www.w3.org/TR/xsl/#line-stacking-strategy) | line-stacking-strategy | Basic | partial | partial | partial | partial | partial | partial | partial | value "line-height" not supported |
| [§7.16.7](http://www.w3.org/TR/xsl/#linefeed-treatment) | linefeed-treatment | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.8](http://www.w3.org/TR/xsl/#white-space-treatment) | white-space-treatment | Extended | partial | partial | partial | partial | partial | partial | partial | inline elements may interfere with correct handling of this property in some cases |
| [§7.16.9](http://www.w3.org/TR/xsl/#text-align) | text-align | Basic | partial | partial | partial | partial | partial | partial | partial | Only start, end, center and justify are supported |
| [§7.16.10](http://www.w3.org/TR/xsl/#text-align-last) | text-align-last | Extended | partial | partial | partial | partial | partial | partial | partial | Only start, end, center and justify are supported |
| [§7.16.11](http://www.w3.org/TR/xsl/#text-indent) | text-indent | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.12](http://www.w3.org/TR/xsl/#white-space-collapse) | white-space-collapse | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.16.13](http://www.w3.org/TR/xsl/#wrap-option) | wrap-option | Basic | partial | partial | partial | partial | partial | partial | partial | Only supported on fo:block. |
| [§7.17](http://www.w3.org/TR/xsl/#d0e25178) | Character Properties | { #fo-property-char-section} |  |  |  |  |  |  |  |  |
| [§7.17.1](http://www.w3.org/TR/xsl/#character) | character | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.17.2](http://www.w3.org/TR/xsl/#letter-spacing) | letter-spacing | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.17.3](http://www.w3.org/TR/xsl/#suppress-at-line-break) | suppress-at-line-break | Extended | no | no | no | no | no | no | no |  |
| [§7.17.4](http://www.w3.org/TR/xsl/#text-decoration) | text-decoration | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.17.5](http://www.w3.org/TR/xsl/#text-shadow) | text-shadow | Extended | no | no | no | no | no | no | no |  |
| [§7.17.6](http://www.w3.org/TR/xsl/#text-transform) | text-transform | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.17.7](http://www.w3.org/TR/xsl/#treat-as-word-space) | treat-as-word-space | Extended | no | no | no | no | no | no | no |  |
| [§7.17.8](http://www.w3.org/TR/xsl/#word-spacing) | word-spacing | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.18](http://www.w3.org/TR/xsl/#d0e25895) | Color-related Properties | { #fo-property-color-section} |  |  |  |  |  |  |  |  |
| [§7.18.1](http://www.w3.org/TR/xsl/#color) | color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.18.2](http://www.w3.org/TR/xsl/#color-profile-name) | color-profile-name | Extended | no | no | no | no | no | no | no |  |
| [§7.18.3](http://www.w3.org/TR/xsl/#rendering-intent) | rendering-intent | Extended | no | no | no | no | no | no | no |  |
| [§7.19](http://www.w3.org/TR/xsl/#d0e26080) | Float-related Properties | { #fo-property-float-section} |  |  |  |  |  |  |  |  |
| [§7.19.1](http://www.w3.org/TR/xsl/#clear) | clear | Extended | no | no | no | no | no | no | no |  |
| [§7.19.2](http://www.w3.org/TR/xsl/#float) | float | Extended | no | no | no | no | no | no | no |  |
| [§7.19.3](http://www.w3.org/TR/xsl/#intrusion-displace) | intrusion-displace | Extended | no | no | no | no | no | no | no |  |
| [§7.20](http://www.w3.org/TR/xsl/#d0e26492) | Keeps and Breaks Properties | { #fo-property-keepsbreaks-section} |  |  |  |  |  |  |  |  |
| [§7.20.1](http://www.w3.org/TR/xsl/#break-after) | break-after | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.20.2](http://www.w3.org/TR/xsl/#break-before) | break-before | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.20.3](http://www.w3.org/TR/xsl/#keep-together) | keep-together | Extended | partial | partial | partial | partial | partial | partial | partial | [1.0 and later] minimal support for <integer> value. |
| [§7.20.4](http://www.w3.org/TR/xsl/#keep-with-next) | keep-with-next | Basic | partial | partial | partial | partial | partial | partial | partial | Works on all implemented block-level FOs, but not on inline-level FOs. Minimal support for <integer> value. |
| [§7.20.5](http://www.w3.org/TR/xsl/#keep-with-previous) | keep-with-previous | Basic | partial | partial | partial | partial | partial | partial | partial | works on all implemented block-level FOs, but not on inline-level FOs. Minimal support for <integer> value. |
| [§7.20.6](http://www.w3.org/TR/xsl/#orphans) | orphans | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.20.7](http://www.w3.org/TR/xsl/#widows) | widows | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.21](http://www.w3.org/TR/xsl/#d0e26965) | Layout-related Properties | { #fo-property-layout-section} |  |  |  |  |  |  |  |  |
| [§7.21.1](http://www.w3.org/TR/xsl/#clip) | clip | Extended | no | no | no | no | no | no | no |  |
| [§7.21.2](http://www.w3.org/TR/xsl/#overflow) | overflow | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.21.3](http://www.w3.org/TR/xsl/#reference-orientation) | reference-orientation | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.21.4](http://www.w3.org/TR/xsl/#span) | span | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.22](http://www.w3.org/TR/xsl/#d0e27308) | Leader and Rule Properties | { #fo-property-leader-section} |  |  |  |  |  |  |  |  |
| [§7.22.1](http://www.w3.org/TR/xsl/#leader-alignment) | leader-alignment | Extended | no | no | no | no | no | no | no | Not supported |
| [§7.22.2](http://www.w3.org/TR/xsl/#leader-pattern) | leader-pattern | Basic | yes | yes | yes | yes | yes | yes | yes | Value "use-content" does not work in all circumstances. |
| [§7.22.3](http://www.w3.org/TR/xsl/#leader-pattern-width) | leader-pattern-width | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.22.4](http://www.w3.org/TR/xsl/#leader-length) | leader-length | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.22.5](http://www.w3.org/TR/xsl/#rule-style) | rule-style | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.22.6](http://www.w3.org/TR/xsl/#rule-thickness) | rule-thickness | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.23](http://www.w3.org/TR/xsl/#d0e27719) | Properties for Dynamic Effects Formatting Objects | { #fo-property-dynamiceffects-section} |  |  |  |  |  |  |  |  |
| [§7.23.1](http://www.w3.org/TR/xsl/#active-state) | active-state | Extended | no | no | no | no | no | no | no |  |
| [§7.23.2](http://www.w3.org/TR/xsl/#auto-restore) | auto-restore | Extended | no | no | no | no | no | no | no |  |
| [§7.23.3](http://www.w3.org/TR/xsl/#case-name) | case-name | Extended | no | no | no | no | no | no | no |  |
| [§7.23.4](http://www.w3.org/TR/xsl/#case-title) | case-title | Extended | no | no | no | no | no | no | no |  |
| [§7.23.5](http://www.w3.org/TR/xsl/#destination-placement-offset) | destination-placement-offset | Extended | no | no | no | no | no | no | no |  |
| [§7.23.6](http://www.w3.org/TR/xsl/#external-destination) | external-destination | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.23.7](http://www.w3.org/TR/xsl/#indicate-destination) | indicate-destination | Extended | no | no | no | no | no | no | no |  |
| [§7.23.8](http://www.w3.org/TR/xsl/#internal-destination) | internal-destination | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.23.9](http://www.w3.org/TR/xsl/#show-destination) | show-destination | Extended | partial | partial | partial | partial | partial | partial | partial | [1.0 and later] only has effect in PDF output, for external PDF destinations (links pointing to destinations in _another_ PDF), and only works reliably when the PDF is viewed in a standalone PDF viewer. Adobe's browser plugin, for example, ignores the `/NewWindow` flag. |
| [§7.23.10](http://www.w3.org/TR/xsl/#starting-state) | starting-state | Extended | partial | partial | partial | partial | partial | partial | partial | support for starting-state on fo:bookmark |
| [§7.23.11](http://www.w3.org/TR/xsl/#switch-to) | switch-to | Extended | no | no | no | no | no | no | no |  |
| [§7.23.12](http://www.w3.org/TR/xsl/#target-presentation-context) | target-presentation-context | Extended | no | no | no | no | no | no | no |  |
| [§7.23.13](http://www.w3.org/TR/xsl/#target-processing-context) | target-processing-context | Extended | no | no | no | no | no | no | no |  |
| [§7.23.14](http://www.w3.org/TR/xsl/#target-stylesheet) | target-stylesheet | Extended | no | no | no | no | no | no | no |  |
| [§7.24](http://www.w3.org/TR/xsl/#d0e28521) | Properties for Indexing | { #fo-property-indexing-section} |  |  |  |  |  |  |  |  |
| [§7.24.1](http://www.w3.org/TR/xsl/#index-class) | index-class | Extended | no | no | no | no | no | no | no |  |
| [§7.24.2](http://www.w3.org/TR/xsl/#index-key) | index-key | Extended | no | no | no | no | no | no | no |  |
| [§7.24.3](http://www.w3.org/TR/xsl/#page-number-treatment) | page-number-treatment | Extended | no | no | no | no | no | no | no |  |
| [§7.24.4](http://www.w3.org/TR/xsl/#merge-ranges-across-index-key-references) | merge-ranges-across-index-key-references | Extended | no | no | no | no | no | no | no |  |
| [§7.24.5](http://www.w3.org/TR/xsl/#merge-sequential-page-numbers) | merge-sequential-page-numbers | Extended | no | no | no | no | no | no | no |  |
| [§7.24.6](http://www.w3.org/TR/xsl/#merge-pages-across-index-key-references) | merge-pages-across-index-key-references | Extended | no | no | no | no | no | no | no |  |
| [§7.24.7](http://www.w3.org/TR/xsl/#ref-index-key) | ref-index-key | Extended | no | no | no | no | no | no | no |  |
| [§7.25](http://www.w3.org/TR/xsl/#d0e28896) | Properties for Markers | { #fo-property-markers-section} |  |  |  |  |  |  |  |  |
| [§7.25.1](http://www.w3.org/TR/xsl/#marker-class-name) | marker-class-name | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.25.2](http://www.w3.org/TR/xsl/#retrieve-boundary-within-table) | retrieve-boundary-within-table | Extended | no | no | no | no | no | no | no |  |
| [§7.25.3](http://www.w3.org/TR/xsl/#retrieve-class-name) | retrieve-class-name | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.53.4](http://www.w3.org/TR/xsl/#retrieve-position) | retrieve-position | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.25.5](http://www.w3.org/TR/xsl/#retrieve-boundary) | retrieve-boundary | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.25.6](http://www.w3.org/TR/xsl/#retrieve-position-within-table) | retrieve-position-within-table | Extended | no | no | no | no | no | no | no |  |
| [§7.26](http://www.w3.org/TR/xsl/#d0e29313) | Properties for Number to String Conversion | { #fo-property-numberstring-section} |  |  |  |  |  |  |  |  |
| [§7.26.1](http://www.w3.org/TR/xsl/#format) | format | Basic | partial | yes | yes | yes | yes | yes | yes | [1.0 and earlier] only values '0*1', 'a', 'A', 'i', 'I' supported |
| [§7.26.2](http://www.w3.org/TR/xsl/#grouping-separator) | grouping-separator | Extended | no | yes | yes | yes | yes | yes | yes |  |
| [§7.26.3](http://www.w3.org/TR/xsl/#grouping-size) | grouping-size | Extended | no | yes | yes | yes | yes | yes | yes |  |
| [§7.26.4](http://www.w3.org/TR/xsl/#letter-value) | letter-value | Basic | no | yes | yes | yes | yes | yes | yes |  |
| [§7.27](http://www.w3.org/TR/xsl/#d0e29484) | Pagination and Layout Properties | { #fo-property-pagination-section} |  |  |  |  |  |  |  |  |
| [§7.27.1](http://www.w3.org/TR/xsl/#blank-or-not-blank) | blank-or-not-blank | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.2](http://www.w3.org/TR/xsl/#column-count) | column-count | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.3](http://www.w3.org/TR/xsl/#column-gap) | column-gap | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.4](http://www.w3.org/TR/xsl/#extent) | extent | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.5](http://www.w3.org/TR/xsl/#flow-name) | flow-name | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.6](http://www.w3.org/TR/xsl/#force-page-count) | force-page-count | Extended | yes | yes | yes | yes | yes | yes | yes | [FOP 2.12]: additionally the extended values doubly-even, doubly-odd, end-on-doubly-even and end-on-doubly-odd are supported |
| [§7.27.7](http://www.w3.org/TR/xsl/#initial-page-number) | initial-page-number | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.8](http://www.w3.org/TR/xsl/#master-name) | master-name | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.9](http://www.w3.org/TR/xsl/#master-reference) | master-reference | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.10](http://www.w3.org/TR/xsl/#maximum-repeats) | maximum-repeats | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.11](http://www.w3.org/TR/xsl/#media-usage) | media-usage | Extended | no | no | no | no | no | no | no |  |
| [§7.27.12](http://www.w3.org/TR/xsl/#odd-or-even) | odd-or-even | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.13](http://www.w3.org/TR/xsl/#page-height) | page-height | Basic | partial | partial | partial | partial | partial | partial | partial | value "indefinite" not yet supported |
| [§7.27.14](http://www.w3.org/TR/xsl/#page-position) | page-position | Extended | yes | yes | yes | yes | yes | yes | yes | value "only" not supported |
| [§7.27.15](http://www.w3.org/TR/xsl/#page-width) | page-width | Basic | partial | partial | partial | partial | partial | partial | partial | value "indefinite" not yet supported |
| [§7.27.16](http://www.w3.org/TR/xsl/#precedence) | precedence | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.17](http://www.w3.org/TR/xsl/#region-name) | region-name | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.27.18](http://www.w3.org/TR/xsl/#flow-map-name) | flow-map-name | Extended | no | no | no | no | no | no | no |  |
| [§7.27.19](http://www.w3.org/TR/xsl/#flow-map-reference) | flow-map-reference | Extended | no | no | no | no | no | no | no |  |
| [§7.27.20](http://www.w3.org/TR/xsl/#flow-name-reference) | flow-name-reference | Extended | no | no | no | no | no | no | no |  |
| [§7.27.21](http://www.w3.org/TR/xsl/#region-name-reference) | region-name-reference | Extended | no | no | no | no | no | no | no |  |
| [§7.28](http://www.w3.org/TR/xsl/#d0e30798) | Table Properties | { #fo-property-table-section} |  |  |  |  |  |  |  |  |
| [§7.28.1](http://www.w3.org/TR/xsl/#border-after-precedence) | border-after-precedence | Basic | no | no | no | no | no | no | no |  |
| [§7.28.2](http://www.w3.org/TR/xsl/#border-before-precedence) | border-before-precedence | Basic | no | no | no | no | no | no | no |  |
| [§7.28.3](http://www.w3.org/TR/xsl/#border-collapse) | border-collapse | Extended | partial | partial | partial | partial | partial | partial | partial | value "collapse-with-precedence" not yet supported |
| [§7.28.4](http://www.w3.org/TR/xsl/#border-end-precedence) | border-end-precedence | Basic | no | no | no | no | no | no | no |  |
| [§7.28.5](http://www.w3.org/TR/xsl/#border-separation) | border-separation | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.6](http://www.w3.org/TR/xsl/#border-start-precedence) | border-start-precedence | Basic | no | no | no | no | no | no | no |  |
| [§7.28.7](http://www.w3.org/TR/xsl/#caption-side) | caption-side | Complete | no | no | no | no | no | no | no |  |
| [§7.28.8](http://www.w3.org/TR/xsl/#column-number) | column-number | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.9](http://www.w3.org/TR/xsl/#column-width) | column-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.10](http://www.w3.org/TR/xsl/#empty-cells) | empty-cells | Extended | no | no | no | no | no | no | no |  |
| [§7.28.11](http://www.w3.org/TR/xsl/#ends-row) | ends-row | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.12](http://www.w3.org/TR/xsl/#number-columns-repeated) | number-columns-repeated | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.13](http://www.w3.org/TR/xsl/#number-columns-spanned) | number-columns-spanned | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.14](http://www.w3.org/TR/xsl/#number-rows-spanned) | number-rows-spanned | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.15](http://www.w3.org/TR/xsl/#starts-row) | starts-row | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.16](http://www.w3.org/TR/xsl/#table-layout) | table-layout | Extended | no | no | no | no | no | no | no |  |
| [§7.28.17](http://www.w3.org/TR/xsl/#table-omit-footer-at-break) | table-omit-footer-at-break | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.28.18](http://www.w3.org/TR/xsl/#table-omit-header-at-break) | table-omit-header-at-break | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.29](http://www.w3.org/TR/xsl/#writing-mode-related) | Writing-mode-related Properties | { #fo-property-writingmode-section} |  |  |  |  |  |  |  |  |
| [§7.29.1](http://www.w3.org/TR/xsl/#direction) | direction | Basic | no | no | no | no | no | no | no |  |
| [§7.29.2](http://www.w3.org/TR/xsl/#glyph-orientation-horizontal) | glyph-orientation-horizontal | Extended | no | no | no | no | no | no | no |  |
| [§7.29.3](http://www.w3.org/TR/xsl/#glyph-orientation-vertical) | glyph-orientation-vertical | Extended | no | no | no | no | no | no | no |  |
| [§7.29.4](http://www.w3.org/TR/xsl/#text-altitude) | text-altitude | Extended | no | no | no | no | no | no | no |  |
| [§7.29.5](http://www.w3.org/TR/xsl/#text-depth) | text-depth | Extended | no | no | no | no | no | no | no |  |
| [§7.29.6](http://www.w3.org/TR/xsl/#unicode-bidi) | unicode-bidi | Extended | no | no | no | no | no | no | no |  |
| [§7.29.7](http://www.w3.org/TR/xsl/#writing-mode) | writing-mode | Basic | no | partial | partial | partial | partial | partial | partial | [1.1 and later] only horizontal left-to-right and right-to-left modes |
| [§7.30](http://www.w3.org/TR/xsl/#d0e32871) | Miscellaneous Properties | { #fo-property-misc-section} |  |  |  |  |  |  |  |  |
| [§7.30.1](http://www.w3.org/TR/xsl/#change-bar-class) | change-bar-class | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.2](http://www.w3.org/TR/xsl/#change-bar-color) | change-bar-color | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.3](http://www.w3.org/TR/xsl/#change-bar-offset) | change-bar-offset | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.4](http://www.w3.org/TR/xsl/#change-bar-placement) | change-bar-placement | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.5](http://www.w3.org/TR/xsl/#change-bar-style) | change-bar-style | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.6](http://www.w3.org/TR/xsl/#change-bar-width) | change-bar-width | Extended | no | no | no | no | yes | yes | yes |  |
| [§7.30.7](http://www.w3.org/TR/xsl/#content-type) | content-type | Extended | no | no | no | no | no | no | no |  |
| [§7.30.8](http://www.w3.org/TR/xsl/#id) | id | Basic | partial | partial | partial | partial | partial | partial | partial | IDs on table-header, table-footer, table-body, table-row, table-and-caption, table-caption, inline-container and bidi-override are not available, yet. |
| [§7.30.9](http://www.w3.org/TR/xsl/#intrinsic-scale-value) | intrinsic-scale-value | Extended | no | no | no | no | no | no | no |  |
| [§7.30.10](http://www.w3.org/TR/xsl/#page-citation-strategy) | page-citation-strategy | Extended | no | no | no | no | no | no | no |  |
| [§7.30.11](http://www.w3.org/TR/xsl/#provisional-label-separation) | provisional-label-separation | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.30.12](http://www.w3.org/TR/xsl/#provisional-distance-between-starts) | provisional-distance-between-starts | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.30.13](http://www.w3.org/TR/xsl/#ref-id) | ref-id | Extended | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.30.14](http://www.w3.org/TR/xsl/#scale-option) | scale-option | Extended | no | no | no | no | no | no | no |  |
| [§7.30.15](http://www.w3.org/TR/xsl/#score-spaces) | score-spaces | Extended | no | no | no | no | no | no | no |  |
| [§7.30.16](http://www.w3.org/TR/xsl/#src) | src | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.30.17](http://www.w3.org/TR/xsl/#visibility) | visibility | Extended | no | no | no | no | no | no | no |  |
| [§7.30.18](http://www.w3.org/TR/xsl/#z-index) | z-index | Extended | no | no | no | no | no | no | no |  |
| [§7.31](http://www.w3.org/TR/xsl/#d0e33965) | Shorthand Properties | { #fo-property-shorthand-section} |  |  |  |  |  |  |  |  |
| [§7.31.1](http://www.w3.org/TR/xsl/#background) | background | Complete | no | no | no | no | no | no | no |  |
| [§7.31.2](http://www.w3.org/TR/xsl/#background-position) | background-position | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.3](http://www.w3.org/TR/xsl/#border) | border | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.4](http://www.w3.org/TR/xsl/#border-bottom) | border-bottom | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.5](http://www.w3.org/TR/xsl/#border-color) | border-color | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.6](http://www.w3.org/TR/xsl/#border-left) | border-left | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.7](http://www.w3.org/TR/xsl/#border-right) | border-right | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.8](http://www.w3.org/TR/xsl/#border-style) | border-style | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.9](http://www.w3.org/TR/xsl/#border-spacing) | border-spacing | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.10](http://www.w3.org/TR/xsl/#border-top) | border-top | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.11](http://www.w3.org/TR/xsl/#border-width) | border-width | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.12](http://www.w3.org/TR/xsl/#cue) | cue | Complete | na | na | na | na | na | na | na |  |
| [§7.31.13](http://www.w3.org/TR/xsl/#font) | font | Complete | partial | partial | partial | partial | partial | partial | partial | Enum values other than "inherit" not yet supported. |
| [§7.31.14](http://www.w3.org/TR/xsl/#margin) | margin | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.15](http://www.w3.org/TR/xsl/#padding) | padding | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.16](http://www.w3.org/TR/xsl/#page-break-after) | page-break-after | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.17](http://www.w3.org/TR/xsl/#page-break-before) | page-break-before | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.18](http://www.w3.org/TR/xsl/#page-break-inside) | page-break-inside | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.19](http://www.w3.org/TR/xsl/#pause) | pause | Complete | na | na | na | na | na | na | na |  |
| [§7.31.20](http://www.w3.org/TR/xsl/#position) | position | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.21](http://www.w3.org/TR/xsl/#size) | size | Complete | no | no | no | no | no | no | no |  |
| [§7.31.22](http://www.w3.org/TR/xsl/#vertical-align) | vertical-align | Complete | partial | partial | partial | partial | partial | partial | partial | Percentages are not supported, yet. |
| [§7.31.23](http://www.w3.org/TR/xsl/#white-space) | white-space | Complete | yes | yes | yes | yes | yes | yes | yes |  |
| [§7.31.24](http://www.w3.org/TR/xsl/#xml.lang) | xml:lang | Complete | yes | yes | yes | yes | yes | yes | yes | Very basic parsing; no validation of the specified value. |

XSL-FO Core Function Library Support Table (§5.10)
--------------------------------------------------

The following is a summary of FOP's current support for the XSL-FO Core Function Library.

| Citation | Function Name | XSL-FO Conformance Level | FOP 1.0 | FOP 1.1 | FOP 2.0 | FOP 2.3 | FOP 2.4 to 2.8 | FOP 2.9 to 2.10 | FOP dev | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | Number Functions | { #fo-function-number-section} |  |  |  |  |  |  |  |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | floor | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | ceiling | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | round | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | min | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | max | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.1](http://www.w3.org/TR/xsl/#d0e5860) | abs | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.2](http://www.w3.org/TR/xsl/#expr-color-functions) | Color Functions | { #fo-function-color-section} |  |  |  |  |  |  |  |  |
| [§5.10.2](http://www.w3.org/TR/xsl/#expr-color-functions) | rgb | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.2](http://www.w3.org/TR/xsl/#expr-color-functions) | rgb-icc | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.2](http://www.w3.org/TR/xsl/#expr-color-functions) | system-color | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.3](http://www.w3.org/TR/xsl/#d0e5948) | Font Functions | { #fo-function-font-section} |  |  |  |  |  |  |  |  |
| [§5.10.3](http://www.w3.org/TR/xsl/#d0e5948) | system-font | Basic | no | no | no | no | no | no | no |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | Property Value Functions | { #fo-function-property-value-section} |  |  |  |  |  |  |  |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | inherited-property-value | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | label-end | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | body-start | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | from-parent | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | from-nearest-specified-value | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | from-page-master-region | Basic | no | no | no | no | no | no | no |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | from-table-column | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | proportional-column-width | Basic | yes | yes | yes | yes | yes | yes | yes |  |
| [§5.10.4](http://www.w3.org/TR/xsl/#d0e5961) | merge-property-values | Basic | no | no | no | no | no | no | no |  |
