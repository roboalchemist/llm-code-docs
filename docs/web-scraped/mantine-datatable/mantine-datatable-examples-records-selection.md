# Source: https://icflorescu.github.io/mantine-datatable/examples/records-selection/

Title: Examples › Records selection | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/records-selection/

Markdown Content:
In order to enable records selection, you’ll have to add the following properties to the DataTable:

*   `selectedRecords` → an array of currently selected records (with the same TS type as the`records` property);
*   `onSelectedRecordsChange` → a callback that will be invoked when the user alters the current selection.

When adding these two properties, the component will render a selection checkbox column and handle user input as following:

*   _Clicking a row selection checkbox_ will result in selecting/deselecting the underlying record;
*   _Clicking the column header checkbox_ will result in selecting/deselecting all visible records;
*   **_Shift-clicking a row selection checkbox_ will result in intuitively selecting all records between the last clicked record and the current one.**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
|  | Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
|  | Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
|  | Runte Inc | 2996 Ronny Mount | McAllen | MA |
|  | Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
|  | Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
|  | Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
|  | Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
|  | Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
|  | Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

### [Disable selection of certain records](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

You can disable the selection of certain records by providing an `isRecordSelectable` property like so:

The above code will result in the following behavior:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
|  | Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
|  | Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
|  | Runte Inc | 2996 Ronny Mount | McAllen | MA |
|  | Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
|  | Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
|  | Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
|  | Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
|  | Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
|  | Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

### [Customizing the selection column className and style](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

By default, the selection column has an absolute width of `0`, to that it only takes up the space required by the selection checkboxes. If you’re not happy with this behavior, or you have other reasons to customize the column’s properties, you can do so by providing the `selectionColumnClassName` and/or`selectionColumnStyle` properties:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
|  | Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
|  | Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
|  | Runte Inc | 2996 Ronny Mount | McAllen | MA |
|  | Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
|  | Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
|  | Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
|  | Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
|  | Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
|  | Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

### [Additional selection checkbox props](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

You can pass additional props to the selection checkboxes by providing the following properties:

*   `checkboxProps` → an object of props that will be applied to all selection checkboxes (both the column header checkbox and the row selection checkboxes);
*   `allRecordsSelectionCheckboxProps` → an object of props that will be applied to the column header checkbox;
*   `getRecordSelectionCheckboxProps` → a function that receives the underlying record and record index and returns an object of props that will be applied to the row selection checkboxes.

In this example, the checkboxes will be rendered with a smaller size and will have custom`aria-label` attributes that will be read by screen readers (inspect the DOM to check these):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
|  | Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
|  | Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
|  | Runte Inc | 2996 Ronny Mount | McAllen | MA |
|  | Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
|  | Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
|  | Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
|  | Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
|  | Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
|  | Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

### [Selecting all records on all pages](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

When using [pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/), the best practice is to**only load the current page’s records from the server**.

This also means that Mantine DataTable can’t—and **shouldn’t**—know about your entire dataset, so the “select all” checkbox will only select/deselect the records on the currently visible page.

However, in certain you might want to give users the ability to “select all records on all pages” (like you have in Gmail’s user interface). In this case, you can use the `allRecordsSelectionCheckboxProps` to create your own selection mechanism:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Jerald | Howell | Jerald.Howell32@yahoo.com | Industrial | Runte Inc |
|  | Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Computers | Shanahan, Robel and Beier |
|  | Erica | Volkman | Erica.Volkman37@gmail.com | Toys | Goyette Inc |
|  | Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Automotive | Rau - O'Hara |
|  | Alison | Kling | Alison16@gmail.com | Jewelery | Goyette Inc |
|  | Sue | Zieme | Sue.Zieme29@hotmail.com | Books | Cummerata - Kuhlman |
|  | Felicia | Gleason | Felicia30@yahoo.com | Shoes | Doyle, Hodkiewicz and O'Connell |
|  | Alfredo | Zemlak | Alfredo22@yahoo.com | Games | Runte Inc |
|  | Emily | Bartoletti | Emily.Bartoletti@gmail.com | Automotive | Rau - O'Hara |
|  | Delores | Reynolds | Delores.Reynolds@yahoo.com | Industrial | Runte Inc |

No records

You have selected 0 records of a total of 500.

Here is the code for the above example:

### [Horizontal scrolling behavior](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

Notice how, when the table needs to be horizontally scrollable, the selection column will be fixed to the left side of the table, so that the selection checkboxes are always visible:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Jerald | Howell | Jerald.Howell32@yahoo.com | Industrial | Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
|  | Kathleen | Ruecker | Kathleen_Ruecker@hotmail.com | Computers | Shanahan, Robel and Beier | Synthesize customized portals. | 378 Berta Crescent | West Gerry | KS |
|  | Erica | Volkman | Erica.Volkman37@gmail.com | Toys | Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
|  | Clifford | Oberbrunner | Clifford.Oberbrunner@hotmail.com | Automotive | Rau - O'Hara | Innovate real-time applications. | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Alison | Kling | Alison16@gmail.com | Jewelery | Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |

No records

Code:

### [Maximizing the selection trigger area to the entire cell](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

By default, selection is triggered when the user clicks the row selection checkbox.

However, you can maximize the trigger area to the entire cell holding the checkbox by setting the`selectionTrigger` property value to `cell`:

In this case, clicking anywhere in the cell will result in selecting/deselecting the underlying record:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive Stromanport WY | Innovate bricks-and-clicks metrics. |
|  | Cummerata - Kuhlman | 6389 Dicki Stream South Gate NH | Harness real-time channels. |
|  | Goyette Inc | 8873 Mertz Rapid Dorthyside ID | Productize front-end web services. |

No records

Head over to the next example to discover more features.
