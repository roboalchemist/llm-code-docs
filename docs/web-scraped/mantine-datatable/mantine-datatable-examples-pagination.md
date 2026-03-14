# Source: https://icflorescu.github.io/mantine-datatable/examples/pagination/

Title: Examples › Pagination | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/pagination/

Markdown Content:
You can enable pagination by setting the following Mantine DataTable properties:

*   `page: number`

The current page number.
*   `onPageChange`

A callback that is executed when the user changes the current page.
*   `totalRecords: number`

The total number of records in the dataset.
*   `recordsPerPage: number`

The number of records per page.

|  |  |  |  |
| --- | --- | --- | --- |
| Jerald | Howell | Jerald.Howell32@yahoo.com | May 21 1950 |
| Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Dec 19 1943 |
| Erica | Volkman | Erica.Volkman37@gmail.com | Jan 29 1955 |
| Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Mar 6 1979 |
| Alison | Kling | Alison16@gmail.com | Jan 27 1997 |
| Sue | Zieme | Sue.Zieme29@hotmail.com | Sep 12 1960 |
| Felicia | Gleason | Felicia30@yahoo.com | Mar 9 1977 |
| Alfredo | Zemlak | Alfredo22@yahoo.com | Nov 12 1988 |
| Emily | Bartoletti | Emily.Bartoletti@gmail.com | Jan 5 1968 |
| Delores | Reynolds | Delores.Reynolds@yahoo.com | Jun 4 2004 |
| Louis | Schamberger | Louis6@yahoo.com | Sep 7 1994 |
| Beverly | Heller | Beverly_Heller@gmail.com | Nov 29 2001 |
| Eugene | Feest | Eugene88@hotmail.com | Feb 20 1954 |
| Martin | Bahringer | Martin_Bahringer10@gmail.com | May 26 1945 |
| Ellis | Miller | Ellis36@hotmail.com | May 24 1950 |

No records

If you’re not happy with the default pagination behavior, you can override it by setting these**optional** properties:

*   `loadingText: string`

A text to display while loading records.
*   `noRecordsText: string`

A text to display when no records are present.
*   `paginationText`

A callback receiving an object in the shape of`{ from: number; to: number; totalRecords: number }` and returning a `ReactNode`representing the pagination text.
*   `paginationSize: 'xs' | 'sm' | 'md' | 'lg' | 'xl'`

The pagination size.
*   `paginationWrapBreakpoint: 'xs' | 'sm' | 'md' | 'lg' | 'xl' | (string & {}) | number`

A breakpoint below which the pagination footer content will wrap on multiple lines. Defaults to`sm`.

You can also provide a `string` like `'300px'` or `'20rem'`, or a`number`, in which case it will be interpreted as a pixel value and converted to rem value before being applied.
*   `paginationActiveTextColor: MantineColor | { light: MantineColor; dark: MantineColor }`

Color applied to active page button text.

Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string), or an object with `light` and `dark` keys and `MantineColor` values.

Defaults to white.
*   `paginationActiveBackgroundColor: MantineColor | { light: MantineColor; dark: MantineColor }`

Color applied to active page button background.

Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string), or an object with `light` and `dark` keys and `MantineColor` values.

Defaults to primary theme color.

Here is the code:

### [Displaying a page size selector](https://icflorescu.github.io/mantine-datatable/examples/pagination/)

You can display a selector to let the user choose the page size by setting the following component properties:

*   `recordsPerPageOptions: number[]`

An array of page size numbers to display in the page size selector.
*   `onRecordsPerPageChange`

A callback that is executed when the user changes the page size. Receives the new page size as its argument.
*   `recordsPerPageLabel`

The page size selector label, defaulting to 'Records per page'.

|  |  |  |  |
| --- | --- | --- | --- |
| Jerald | Howell | Jerald.Howell32@yahoo.com | May 21 1950 |
| Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Dec 19 1943 |
| Erica | Volkman | Erica.Volkman37@gmail.com | Jan 29 1955 |
| Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Mar 6 1979 |
| Alison | Kling | Alison16@gmail.com | Jan 27 1997 |
| Sue | Zieme | Sue.Zieme29@hotmail.com | Sep 12 1960 |
| Felicia | Gleason | Felicia30@yahoo.com | Mar 9 1977 |
| Alfredo | Zemlak | Alfredo22@yahoo.com | Nov 12 1988 |
| Emily | Bartoletti | Emily.Bartoletti@gmail.com | Jan 5 1968 |
| Delores | Reynolds | Delores.Reynolds@yahoo.com | Jun 4 2004 |
| Louis | Schamberger | Louis6@yahoo.com | Sep 7 1994 |
| Beverly | Heller | Beverly_Heller@gmail.com | Nov 29 2001 |
| Eugene | Feest | Eugene88@hotmail.com | Feb 20 1954 |
| Martin | Bahringer | Martin_Bahringer10@gmail.com | May 26 1945 |
| Ellis | Miller | Ellis36@hotmail.com | May 24 1950 |

No records

You can fully customize pagination by providing the `renderPagination` prop. The callback receives a context with default controls as factories:

*   `Controls.Text`: the pagination text.
*   `Controls.PageSizeSelector`: the page size selector (if enabled).
*   `Controls.Pagination`: the pagination component.

This allows you to render them in any order, inject your own elements, or override their props. The example below shows how to add a "jump to page" control between page size selector and pagination controls.

|  |  |  |  |
| --- | --- | --- | --- |
| Jerald | Howell | Jerald.Howell32@yahoo.com | May 21 1950 |
| Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Dec 19 1943 |
| Erica | Volkman | Erica.Volkman37@gmail.com | Jan 29 1955 |
| Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Mar 6 1979 |
| Alison | Kling | Alison16@gmail.com | Jan 27 1997 |
| Sue | Zieme | Sue.Zieme29@hotmail.com | Sep 12 1960 |
| Felicia | Gleason | Felicia30@yahoo.com | Mar 9 1977 |
| Alfredo | Zemlak | Alfredo22@yahoo.com | Nov 12 1988 |
| Emily | Bartoletti | Emily.Bartoletti@gmail.com | Jan 5 1968 |
| Delores | Reynolds | Delores.Reynolds@yahoo.com | Jun 4 2004 |
| Louis | Schamberger | Louis6@yahoo.com | Sep 7 1994 |
| Beverly | Heller | Beverly_Heller@gmail.com | Nov 29 2001 |
| Eugene | Feest | Eugene88@hotmail.com | Feb 20 1954 |
| Martin | Bahringer | Martin_Bahringer10@gmail.com | May 26 1945 |
| Ellis | Miller | Ellis36@hotmail.com | May 24 1950 |

No records

You can provide additional props to pagination controls by using the `getPaginationControlProps`callback. For example, if you’re not happy with the default accessibility aria-labels, you can override them like so:

|  |  |  |  |
| --- | --- | --- | --- |
| Jerald | Howell | Jerald.Howell32@yahoo.com | May 21 1950 |
| Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Dec 19 1943 |
| Erica | Volkman | Erica.Volkman37@gmail.com | Jan 29 1955 |
| Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Mar 6 1979 |
| Alison | Kling | Alison16@gmail.com | Jan 27 1997 |
| Sue | Zieme | Sue.Zieme29@hotmail.com | Sep 12 1960 |
| Felicia | Gleason | Felicia30@yahoo.com | Mar 9 1977 |
| Alfredo | Zemlak | Alfredo22@yahoo.com | Nov 12 1988 |
| Emily | Bartoletti | Emily.Bartoletti@gmail.com | Jan 5 1968 |
| Delores | Reynolds | Delores.Reynolds@yahoo.com | Jun 4 2004 |
| Louis | Schamberger | Louis6@yahoo.com | Sep 7 1994 |
| Beverly | Heller | Beverly_Heller@gmail.com | Nov 29 2001 |
| Eugene | Feest | Eugene88@hotmail.com | Feb 20 1954 |
| Martin | Bahringer | Martin_Bahringer10@gmail.com | May 26 1945 |
| Ellis | Miller | Ellis36@hotmail.com | May 24 1950 |

No records

Head over to the next example to discover more features.
