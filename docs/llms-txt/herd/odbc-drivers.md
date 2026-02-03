# Source: https://herd.laravel.com/docs/macos/troubleshooting/odbc-drivers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ODBC Drivers

# Using Microsoft ODBC Drivers on macOS

You might encounter the following error message when trying to use the Microsoft ODBC Driver for SQL Server on macOS:

> "This extension requires the Microsoft ODBC Driver for SQL Server to communicate with SQL Server."

In order to install the missing ODBC driver, please take a alook at the latest official [ODBC Driver installation guide](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver16#microsoft-odbc-18) from Microsoft.

After installing the driver, you will need to manually symlink the Homebrew installed driver to the default location where the Microsoft ODBC Driver for SQL Server expects it to be. This can be done by running the following command:

<CodeGroup>
  ```bash ARM macOS theme={null}
  sudo ln -s /opt/homebrew/etc/odbcinst.ini /etc/odbcinst.ini
  sudo ln -s /opt/homebrew/etc/odbc.ini /etc/odbc.ini
  ```

  ```bash Intel macOS theme={null}
  sudo ln -s /usr/local/etc/odbcinst.ini /etc/odbcinst.ini
  sudo ln -s /usr/local/etc/odbc.ini /etc/odbc.ini
  ```
</CodeGroup>
