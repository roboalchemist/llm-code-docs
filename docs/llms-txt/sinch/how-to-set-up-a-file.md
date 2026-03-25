# Source: https://docs.sinch.com/send-a-message/how-to-set-up-a-file.md

# How to Set Up a File

{% hint style="info" %}
**Requirement: Your contact file can be in XLSX, CSV, or TXT and should have a maximum of 15 MB.**
{% endhint %}

## **How to Set Up an XLSX File**

To set up the file on Excel or Google Spreadsheet, you should follow a few guidelines:

* The **first row** consists of a **header;**
* The **first column** must have the title **destination** and the **contact numbers;**
* The **remaining columns** are filled by **placeholders or variables** that can be used in the body of the message or HSM variables;
* **One of the columns** may be used as **Correlation ID** (with the title **correlationid**) for identifying customers by reports;

Example of an .xlsx file: [**XLSX File**](https://messaging2.movile.com/assets/files/valid.xlsx)**​**

Example:

| destination   | name   | info | correlationid |
| ------------- | ------ | ---- | ------------- |
| 5511987654321 | André  | Wavy | campaign\_X   |
| 5511912345678 | Mozart | Wavy | campaign\_Y   |

{% hint style="info" %}
Tip: to prevent conflicts or issues, we suggest clearing the table formatting. In order to clear it on Excel, select the entire table and click **Clear** / **Clear all formats**. Then select the first column (destination), right click and select **Format Cells**, select **Numbers** and set **0 decimal places**.
{% endhint %}

![Excel: Clear / Clear all formats](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7bibM5YjgS4hXH%2F0.gif?generation=1633456330333299\&alt=media)

![Excel: First column / Format Cells / Numbers \[decimal places = 0](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7cniJJ5FsPEAOC%2F1.gif?generation=1633456330742539\&alt=media)

![Google Spreadsheet: Format / Clear formatting](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7dlvdUMbMxA1An%2F2.gif?generation=1633456330300490\&alt=media)

## **How to Set Up a CSV File**

To set up the file on Excel or Google Spreadsheet, follow the same procedure above for the XLSX file and save in CSV.

Example of a .csv file: [**CSV File**](https://messaging2.movile.com/assets/files/valid.csv)**​**

![Excel: Save as / File Format CSV](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7e8qCOWxXmPUJ9%2F3.gif?generation=1633456329927880\&alt=media)

![Google Spreadsheet: Download as / Comma-separated values](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7fYZXbBOmwogGF%2F4.gif?generation=1633456330136359\&alt=media)

## **How to Set Up a TXT File**

To set up a TXT file, just fill out the first line of the file with the following information: destination: reserved for all phone numbers separated by ";" the other "columns" of the file. Example of a .txt file: [**TXT File**](https://messaging2.movile.com/assets/files/valid.txt)
