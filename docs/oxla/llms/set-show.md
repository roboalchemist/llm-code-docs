# Source: https://docs.oxla.com/sql-reference/sql-statements/set-show.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SET/SHOW

## Overview

The `SET` statement lets you set specific options while the `SHOW` statement helps you see the current values in Oxla.

## Syntax

The syntax for these functions is as follows:

<Tabs>
  <Tab title="SET">
    ```sql  theme={null}
    SET <option> TO <value>;
    ```

    <Note>
      For options that accept boolean values, `<value>` can be either `ON` or `OFF`, which correspond to `TRUE` or `FALSE` respectively
    </Note>
  </Tab>

  <Tab title="SHOW">
    ```sql  theme={null}
    SHOW <option>;
    ```
  </Tab>
</Tabs>

The available options that can be set and shown are:

* `extra_float_digits`: by default, Oxla displays a limited number of digits, but you can set how many extra digits are displayed after the decimal point in floating-point numbers by using this option
* `application_name`: sets a custom name for the application
* `timezone`: determines the time zone used for date and time functions
* `client_min_messages`: sets the message levels sent to the client (valid values are `DEBUG5`, `DEBUG4`, `DEBUG3`, `DEBUG2`, `DEBUG1`, `LOG`, `NOTICE`, `WARNING` and `ERROR`)
* `search_path`: defines namespaces at which Oxla looks for tables
* `enable_fast_math`: enables mathematical optimizations that trade precision for speed by utilizing faster, less accurate mathematical functions

## Examples

### SET Statement

<Tabs>
  <Tab title="Extra_float_digits">
    To change the number of displayed digits for floating-point values, use the `SET` statement in a following way:

    ```sql  theme={null}
    SET extra_float_digits TO 2;
    ```

    ```sql  theme={null}
    SHOW extra_float_digits;
    ```

    ```sql  theme={null}
     extra_float_digits 
    --------------------
     2
    ```
  </Tab>

  <Tab title="Client_min_messages">
    To change the client message, use the `SET` statement as follows:

    ```sql  theme={null}
    SET client_min_messages TO 'WARNING';
    ```

    ```sql  theme={null}
    SHOW client_min_messages;
    ```

    ```sql  theme={null}
     client_min_messages 
    ---------------------
     warning
    ```
  </Tab>

  <Tab title="Enable_fast_math">
    To change the mode of the fast math option, use the `SET` statement like this:

    ```sql  theme={null}
    SET oxla.enable_fast_math = ON;
    ```

    ```sql  theme={null}
    SHOW oxla.enable_fast_math;
    ```

    ```sql  theme={null}
     oxla_enable_fast_math 
    -----------------------
     1
    (1 row)
    ```
  </Tab>
</Tabs>

### SHOW Statement

<Tabs>
  <Tab title="Timezone">
    To display the current timezone setting, use the following query:

    ```sql  theme={null}
    SHOW timezone;
    ```

    ```sql  theme={null}
     timezone 
    ----------
     Etc/UTC
    ```
  </Tab>

  <Tab title="Search_path">
    To display the current search path, run the query below:

    ```sql  theme={null}
    SHOW search_path;
    ```

    ```sql  theme={null}
     search_path 
    -------------
     public
    ```
  </Tab>

  <Tab title="Enable_fast_math">
    To check the status of the fast math option, use the following method:

    ```sql  theme={null}
    SHOW oxla.enable_fast_math;
    ```

    ```sql  theme={null}
     oxla_enable_fast_math 
    -----------------------
     0
    (1 row)
    ```
  </Tab>
</Tabs>
