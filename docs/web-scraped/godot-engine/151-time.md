# Time

# Time
Inherits:Object
A singleton for working with time data.

## Description
The Time singleton allows converting time between various formats and also getting time information from the system.
This class conforms with as many of the ISO 8601 standards as possible. All dates follow the Proleptic Gregorian calendar. As such, the day before1582-10-15is1582-10-14, not1582-10-04. The year before 1 AD (aka 1 BC) is number0, with the year before that (2 BC) being-1, etc.
Conversion methods assume "the same timezone", and do not handle timezone conversions or DST automatically. Leap seconds are also not handled, they must be done manually if desired. Suffixes such as "Z" are not handled, you need to strip them away manually.
When getting time information from the system, the time can either be in the local timezone or UTC depending on theutcparameter. However, theget_unix_time_from_system()method always uses UTC as it returns the seconds passed since theUnix epoch.
Important:The_from_systemmethods use the system clock that the user can manually set.Never usethis method for precise time calculation since its results are subject to automatic adjustments by the user or the operating system.Always useget_ticks_usec()orget_ticks_msec()for precise time calculation instead, since they are guaranteed to be monotonic (i.e. never decrease).

## Methods

| Dictionary | get_date_dict_from_system(utc:bool= false)const |
|---|---|
| Dictionary | get_date_dict_from_unix_time(unix_time_val:int)const |
| String | get_date_string_from_system(utc:bool= false)const |
| String | get_date_string_from_unix_time(unix_time_val:int)const |
| Dictionary | get_datetime_dict_from_datetime_string(datetime:String, weekday:bool)const |
| Dictionary | get_datetime_dict_from_system(utc:bool= false)const |
| Dictionary | get_datetime_dict_from_unix_time(unix_time_val:int)const |
| String | get_datetime_string_from_datetime_dict(datetime:Dictionary, use_space:bool)const |
| String | get_datetime_string_from_system(utc:bool= false, use_space:bool= false)const |
| String | get_datetime_string_from_unix_time(unix_time_val:int, use_space:bool= false)const |
| String | get_offset_string_from_offset_minutes(offset_minutes:int)const |
| int | get_ticks_msec()const |
| int | get_ticks_usec()const |
| Dictionary | get_time_dict_from_system(utc:bool= false)const |
| Dictionary | get_time_dict_from_unix_time(unix_time_val:int)const |
| String | get_time_string_from_system(utc:bool= false)const |
| String | get_time_string_from_unix_time(unix_time_val:int)const |
| Dictionary | get_time_zone_from_system()const |
| int | get_unix_time_from_datetime_dict(datetime:Dictionary)const |
| int | get_unix_time_from_datetime_string(datetime:String)const |
| float | get_unix_time_from_system()const |

Dictionary
get_date_dict_from_system(utc:bool= false)const
Dictionary
get_date_dict_from_unix_time(unix_time_val:int)const
String
get_date_string_from_system(utc:bool= false)const
String
get_date_string_from_unix_time(unix_time_val:int)const
Dictionary
get_datetime_dict_from_datetime_string(datetime:String, weekday:bool)const
Dictionary
get_datetime_dict_from_system(utc:bool= false)const
Dictionary
get_datetime_dict_from_unix_time(unix_time_val:int)const
String
get_datetime_string_from_datetime_dict(datetime:Dictionary, use_space:bool)const
String
get_datetime_string_from_system(utc:bool= false, use_space:bool= false)const
String
get_datetime_string_from_unix_time(unix_time_val:int, use_space:bool= false)const
String
get_offset_string_from_offset_minutes(offset_minutes:int)const
get_ticks_msec()const
get_ticks_usec()const
Dictionary
get_time_dict_from_system(utc:bool= false)const
Dictionary
get_time_dict_from_unix_time(unix_time_val:int)const
String
get_time_string_from_system(utc:bool= false)const
String
get_time_string_from_unix_time(unix_time_val:int)const
Dictionary
get_time_zone_from_system()const
get_unix_time_from_datetime_dict(datetime:Dictionary)const
get_unix_time_from_datetime_string(datetime:String)const
float
get_unix_time_from_system()const

## Enumerations
enumMonth:🔗
MonthMONTH_JANUARY=1
The month of January, represented numerically as01.
MonthMONTH_FEBRUARY=2
The month of February, represented numerically as02.
MonthMONTH_MARCH=3
The month of March, represented numerically as03.
MonthMONTH_APRIL=4
The month of April, represented numerically as04.
MonthMONTH_MAY=5
The month of May, represented numerically as05.
MonthMONTH_JUNE=6
The month of June, represented numerically as06.
MonthMONTH_JULY=7
The month of July, represented numerically as07.
MonthMONTH_AUGUST=8
The month of August, represented numerically as08.
MonthMONTH_SEPTEMBER=9
The month of September, represented numerically as09.
MonthMONTH_OCTOBER=10
The month of October, represented numerically as10.
MonthMONTH_NOVEMBER=11
The month of November, represented numerically as11.
MonthMONTH_DECEMBER=12
The month of December, represented numerically as12.
enumWeekday:🔗
WeekdayWEEKDAY_SUNDAY=0
The day of the week Sunday, represented numerically as0.
WeekdayWEEKDAY_MONDAY=1
The day of the week Monday, represented numerically as1.
WeekdayWEEKDAY_TUESDAY=2
The day of the week Tuesday, represented numerically as2.
WeekdayWEEKDAY_WEDNESDAY=3
The day of the week Wednesday, represented numerically as3.
WeekdayWEEKDAY_THURSDAY=4
The day of the week Thursday, represented numerically as4.
WeekdayWEEKDAY_FRIDAY=5
The day of the week Friday, represented numerically as5.
WeekdayWEEKDAY_SATURDAY=6
The day of the week Saturday, represented numerically as6.

## Method Descriptions
Dictionaryget_date_dict_from_system(utc:bool= false)const🔗
Returns the current date as a dictionary of keys:year,month,day, andweekday.
The returned values are in the system's local time whenutcisfalse, otherwise they are in UTC.
Dictionaryget_date_dict_from_unix_time(unix_time_val:int)const🔗
Converts the given Unix timestamp to a dictionary of keys:year,month,day, andweekday.
Stringget_date_string_from_system(utc:bool= false)const🔗
Returns the current date as an ISO 8601 date string (YYYY-MM-DD).
The returned values are in the system's local time whenutcisfalse, otherwise they are in UTC.
Stringget_date_string_from_unix_time(unix_time_val:int)const🔗
Converts the given Unix timestamp to an ISO 8601 date string (YYYY-MM-DD).
Dictionaryget_datetime_dict_from_datetime_string(datetime:String, weekday:bool)const🔗
Converts the given ISO 8601 date and time string (YYYY-MM-DDTHH:MM:SS) to a dictionary of keys:year,month,day,weekday,hour,minute, andsecond.
Ifweekdayisfalse, then theweekdayentry is excluded (the calculation is relatively expensive).
Note:Any decimal fraction in the time string will be ignored silently.
Dictionaryget_datetime_dict_from_system(utc:bool= false)const🔗
Returns the current date as a dictionary of keys:year,month,day,weekday,hour,minute,second, anddst(Daylight Savings Time).
Dictionaryget_datetime_dict_from_unix_time(unix_time_val:int)const🔗
Converts the given Unix timestamp to a dictionary of keys:year,month,day,weekday,hour,minute, andsecond.
The returned Dictionary's values will be the same as theget_datetime_dict_from_system()if the Unix timestamp is the current time, with the exception of Daylight Savings Time as it cannot be determined from the epoch.
Stringget_datetime_string_from_datetime_dict(datetime:Dictionary, use_space:bool)const🔗
Converts the given dictionary of keys to an ISO 8601 date and time string (YYYY-MM-DDTHH:MM:SS).
The given dictionary can be populated with the following keys:year,month,day,hour,minute, andsecond. Any other entries (includingdst) are ignored.
If the dictionary is empty,0is returned. If some keys are omitted, they default to the equivalent values for the Unix epoch timestamp 0 (1970-01-01 at 00:00:00).
Ifuse_spaceistrue, the date and time bits are separated by an empty space character instead of the letter T.
Stringget_datetime_string_from_system(utc:bool= false, use_space:bool= false)const🔗
Returns the current date and time as an ISO 8601 date and time string (YYYY-MM-DDTHH:MM:SS).
The returned values are in the system's local time whenutcisfalse, otherwise they are in UTC.
Ifuse_spaceistrue, the date and time bits are separated by an empty space character instead of the letter T.
Stringget_datetime_string_from_unix_time(unix_time_val:int, use_space:bool= false)const🔗
Converts the given Unix timestamp to an ISO 8601 date and time string (YYYY-MM-DDTHH:MM:SS).
Ifuse_spaceistrue, the date and time bits are separated by an empty space character instead of the letter T.
Stringget_offset_string_from_offset_minutes(offset_minutes:int)const🔗
Converts the given timezone offset in minutes to a timezone offset string. For example, -480 returns "-08:00", 345 returns "+05:45", and 0 returns "+00:00".
intget_ticks_msec()const🔗
Returns the amount of time passed in milliseconds since the engine started.
Will always be positive or 0 and uses a 64-bit value (it will wrap after roughly 500 million years).
intget_ticks_usec()const🔗
Returns the amount of time passed in microseconds since the engine started.
Will always be positive or 0 and uses a 64-bit value (it will wrap after roughly half a million years).
Dictionaryget_time_dict_from_system(utc:bool= false)const🔗
Returns the current time as a dictionary of keys:hour,minute, andsecond.
The returned values are in the system's local time whenutcisfalse, otherwise they are in UTC.
Dictionaryget_time_dict_from_unix_time(unix_time_val:int)const🔗
Converts the given time to a dictionary of keys:hour,minute, andsecond.
Stringget_time_string_from_system(utc:bool= false)const🔗
Returns the current time as an ISO 8601 time string (HH:MM:SS).
The returned values are in the system's local time whenutcisfalse, otherwise they are in UTC.
Stringget_time_string_from_unix_time(unix_time_val:int)const🔗
Converts the given Unix timestamp to an ISO 8601 time string (HH:MM:SS).
Dictionaryget_time_zone_from_system()const🔗
Returns the current time zone as a dictionary of keys:biasandname.
- biasis the offset from UTC in minutes, since not all time zones are multiples of an hour from UTC.
biasis the offset from UTC in minutes, since not all time zones are multiples of an hour from UTC.
- nameis the localized name of the time zone, according to the OS locale settings of the current user.
nameis the localized name of the time zone, according to the OS locale settings of the current user.
intget_unix_time_from_datetime_dict(datetime:Dictionary)const🔗
Converts a dictionary of time values to a Unix timestamp.
The given dictionary can be populated with the following keys:year,month,day,hour,minute, andsecond. Any other entries (includingdst) are ignored.
If the dictionary is empty,0is returned. If some keys are omitted, they default to the equivalent values for the Unix epoch timestamp 0 (1970-01-01 at 00:00:00).
You can pass the output fromget_datetime_dict_from_unix_time()directly into this function and get the same as what was put in.
Note:Unix timestamps are often in UTC. This method does not do any timezone conversion, so the timestamp will be in the same timezone as the given datetime dictionary.
intget_unix_time_from_datetime_string(datetime:String)const🔗
Converts the given ISO 8601 date and/or time string to a Unix timestamp. The string can contain a date only, a time only, or both.
Note:Unix timestamps are often in UTC. This method does not do any timezone conversion, so the timestamp will be in the same timezone as the given datetime string.
Note:Any decimal fraction in the time string will be ignored silently.
floatget_unix_time_from_system()const🔗
Returns the current Unix timestamp in seconds based on the system time in UTC. This method is implemented by the operating system and always returns the time in UTC. The Unix timestamp is the number of seconds passed since 1970-01-01 at 00:00:00, theUnix epoch.
Note:Unlike other methods that use integer timestamps, this method returns the timestamp as afloatfor sub-second precision.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.