# Source: https://docs.xano.com/xanoscript/filter-reference/timestamp.md

# Source: https://docs.xano.com/the-function-stack/filters/timestamp.md

# Source: https://docs.xano.com/the-function-stack/data-types/timestamp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Timestamp

### Timestamps

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/zfW1x6DKyLw" title="Xano - Timestamps" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Xano stores timestamps as a **unix timestamp in milliseconds**. Unix timestamp is a way to track time as a running total of seconds. This count starts at the Unix Epoch on January 1st, 1970 at UTC.

For example: 1604959474 seconds since Jan 01 1970. (UTC). This epoch translates to 11/09/2020 @ 10:04pm (UTC). Since Xano uses milliseconds, the timestamp would be **1604959474000**.

There is **no timezone in a timestamp** because it is the number of milliseconds from the unix epoch - Jan 1, 1970.

### **What is the difference between a timezone region, a timezone abbreviation, and a timezone offset?**

A **timezone region** handles daylight savings time for you. For example: America/Los\_Angeles will automatically be PST or PDT depending on the actual timestamp. It handles this behind the scenes so you always have the right timezone offset. [Timezone regions are listed here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

A **timezone abbreviation** is the shortened 3 letter abbreviation (PST, PDT, etc.). This represents a **timezone offset**: PST is -0800 and PDT is -0700. These values are always the same. It is recommended to use the timezone region mentioned above so you don’t need to keep changing the abbreviation selection with daylight savings time changes.

### **When I choose a time from the database table viewer, what timezone is used there?**

The database table view is using the unix timestamp internally but transforming it in the spreadsheet view to the timezone of your browser. This means that if someone else was looking at it from a different timezone, they would see the time that is local to themselves. However, you can change the browser default settings to your preferences for the date & time format and timezone offset that is shown in your database on the [account](https://app.xano.com/admin/account) page.

### **What are my options for inputting a timestamp into Xano through the API?**

* **Raw timestamp** in milliseconds (this would not need any timezone information). For example: 1604959474000

* **ISO 8601** format, which is Year-Month-Day then a “T” and then 24hour-minute-second then “the timezone offset in hours and minutes”:

  2004-02-12T15:19:21+00:00

* **Postgres** database format, which is similar to the ISO 8601 format: 2020-11-09 14:13:18-0800 (Note: a space is used to separate the date from the time instead of the “T” character in ISO 8601. Also, the offset does not include the colon.)

* **Relative time**. Xano uses relative time [formats](https://www.php.net/manual/en/datetime.formats.php#datetime.formats.relative) from php.net[.](https://www.php.net/manual/en/datetime.formats.php#datetime.formats.relative) For example: now, last Monday, +7 days, etc. (Relative times normally don’t have any timezone information, so it will often be important to reference the timezone in any type of [filter](/the-function-stack/filters/timestamp#parse_timestamp).)

* \*\*Parse Timestamp \*\*the parse\_timestamp [filter](/the-function-stack/filters/timestamp#parse_timestamp) allows you to take a human-readable time format and parse it into a Unix timestamp in milliseconds to be stored in the Xano database. The characters used are the same as formatting date and time and can be found [here from php.net](https://www.php.net/manual/en/datetime.format.php).

### **What are my options with formatting date and time?**

There are lots of options available. [A full list is available here from php.net](https://www.php.net/manual/en/datetime.format.php). Here are a just few examples:

* c = 2004-02-12T15:19:21+00:00

* r = Thu, 21 Dec 2000 16:01:07 +0200

* Y-m-d H:i:s = 2000-01-01 00:00:00

See the [Timestamp Filters](/the-function-stack/filters/timestamp) page to see how to use timestamp filters in Xano.


Built with [Mintlify](https://mintlify.com).