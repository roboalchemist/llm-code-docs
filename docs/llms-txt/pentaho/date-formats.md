# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/common-formats/date-formats.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats/date-formats.md

# Date formats

The following table describes common date formats used by PDI transformation steps and job entries:

| Symbol | Meaning                      | Type           | Example                                                                                                |
| ------ | ---------------------------- | -------------- | ------------------------------------------------------------------------------------------------------ |
| G      | Era                          | Text           | "GG" -> "AD"                                                                                           |
| y      | Year                         | Number         | <p>"yy" -> "03"</p><p>"yyyy" -> "2003"</p>                                                             |
| M      | Month                        | Text or Number | <p>"M" -> "7"</p><p>"M" -> "12"</p><p>"MM" -> "07"</p><p>"MMM" -> "Jul"</p><p>"MMMM" -> "December"</p> |
| d      | Day in month                 | Number         | <p>"d" -> "3"</p><p>"dd" -> "03"</p>                                                                   |
| h      | Hour(1-12, AM/PM)            | Number         | <p>"h" -> "3"</p><p>"hh" -> "03"</p>                                                                   |
| H      | Hour (0-23)                  | Number         | <p>"H" -> "15"</p><p>"HH" -> "15"</p>                                                                  |
| k      | Hour (1-24)                  | Number         | <p>"k" -> "3"</p><p>"kk" -> "03"</p>                                                                   |
| K      | Hour (0-11, AM/PM)           | Number         | <p>"K" -> "15"</p><p>"KK" -> "15"</p>                                                                  |
| m      | Minute                       | Number         | <p>"m" -> "7"</p><p>"m" -> "15"</p><p>"mm" -> "15"</p>                                                 |
| s      | Second                       | Number         | <p>"s" -> "15"</p><p>"ss" -> "15"</p>                                                                  |
| S      | Millisecond (0-999)          | Number         | "SSS" -> "007"                                                                                         |
| E      | Day in week                  | Text           | <p>"EEE" -> "Tue"</p><p>"EEEE" -> "Tuesday"</p>                                                        |
| D      | Day in year (1-365 or 1-364) | Number         | <p>"D" -> "65"</p><p>"DDD" -> "065"</p>                                                                |
| F      | Day of week in month (1-5)   | Number         | "F" -> "1"                                                                                             |
| w      | Week in year (1-53)          | Number         | "w" -> "7"                                                                                             |
| W      | Week in month (1-5)          | Number         | "W" -> "3"                                                                                             |
| a      | AM/PM                        | Text           | <p>"a" -> "AM"</p><p>"aa" -> "AM"</p>                                                                  |
| z      | Time zone                    | Text           | <p>"z" -> "EST"</p><p>"zzz" -> EST"</p><p>"zzzz" -> Eastern Standard Time"</p>                         |
| X      | Time zone offset             | Text           | "XXX" -> "-08:00"                                                                                      |
| '      | Escape for text              | Delimiter      | "hour'h" -> "hour 9"                                                                                   |
| ''     | Single quote                 | Literal        | "ss''SSS" -> "45'876". Use two quote marks in a row to create a single quote in a string.              |
