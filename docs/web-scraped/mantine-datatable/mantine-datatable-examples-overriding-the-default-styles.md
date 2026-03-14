# Source: https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/

Title: Examples › Overriding the default styles | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/

Markdown Content:
Mantine DataTable closely follows the current Mantine theme, so it should look great out of the box in most cases.

However, if you’re not happy with the default Mantine DataTable styling, there are several ways to override it.

### [With color properties](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)

You can quickly customize the default colors using the `c`, `backgroundColor`,`borderColor` and `rowBorderColor` properties.

Each of these properties can be set to a `MantineColor` (key of `theme.colors` or any valid CSS color `string`) or an object with `dark` and `light` keys and`MantineColor` values, which will be used to style dark and light themes accordingly.

The `c` property refers to the text color and is applied to:

*   the table body, header and footer;
*   the [pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/) component (if present).

The `backgroundColor` is applied to:

*   the table body, header and footer;
*   the [pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/) component (if present).

The `borderColor` is applied to:

*   the table outer border (if enabled by[`withTableBorder` property](https://icflorescu.github.io/mantine-datatable/examples/basic-table-properties/));
*   header bottom border;
*   footer top border (see[column footers](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/#column-footers));
*   [pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/) top border (if present).

The `rowBorderColor` is applied to:

*   the bottom of each row;
*   the column borders (if enabled by[`withTableBorder` property](https://icflorescu.github.io/mantine-datatable/examples/basic-table-properties/)).

If you’re using [pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/), you can also customize its colors using the `paginationTextColor` and `paginationActiveTextColor` properties.

For example, this code:

…will produce the following table:

|  |  |  |  |
| --- | --- | --- | --- |
| Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
| Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
| Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
| Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
| 13 companies |  | 12 cities | 7 states |

No records

There are even more elaborate ways to destroy the default styling of Mantine DataTable besides setting its[basic properties](https://icflorescu.github.io/mantine-datatable/examples/basic-table-properties/) and the aforementioned colors.

### [With className](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)

You can specify a `className` that will target the DataTable component root:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | Incubate cross-platform metrics. | 632 Broadway Avenue | North Louie | WY |

No records

Here is the code for the above example:

### [With a style object or function](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)

You can target the DataTable component root with a `style` object:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | Incubate cross-platform metrics. | 632 Broadway Avenue | North Louie | WY |

No records

Here is the code for the above example:

The `style` property also accepts a function that receives the current theme as argument and returns a style object:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | Incubate cross-platform metrics. | 632 Broadway Avenue | North Louie | WY |

No records

Here is the code for the above example:

### [With multiple class names](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)

You can specifically target the component root, table, header, footer and pagination with different`classNames`:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| 13 companies | Avg. chars: 31.23076923076923 |  |  | 7 states |

No records

Here is the code for the above example:

### [With multiple style objects or functions](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)

You can specifically target the component root, table, header, footer and pagination with different`styles` objects or functions:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | Incubate cross-platform metrics. | 632 Broadway Avenue | North Louie | WY |

No records

Here is the code for the above example:

Head over to the next example to discover more features.
