Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/time-zone-scheduling

# Scheduling meetings across time zones

Coordinating meetings across different time zones can be a logistical headache. It requires switching between apps and doing mental calculations to convert time zones, which is tedious and prone to errors. Streamline this process with Slack!

Using Workflow Builder, we'll create an automation that takes a proposed meeting time in your timezone, converts it to the timezone of the person you’re scheduling with, and schedules the meeting.

Your timezone scheduler workflow will consist of the following steps:

1. **Built-in function**: Collect info in a form
2. **Custom function**: Timezone-aware meeting schedule
3. **Built-in function**: Send a message with the time conversion and a button to create the calendar invite
4. **Calendar connector**: Use the Google Calendar connector to create the meeting
5. **Built-in function**: Reply with a message in thread with the confirmation of the meeting creation

## Get started {#get-started}

### Set up tools {#set-up-tools}

We are using the [Slack CLI](/tools/slack-cli) and [Deno Slack SDK](/tools/deno-slack-sdk) to create an app where the custom function exists and can be pulled into Workflow Builder to be used as a step. You should be familiar with the Slack CLI and how it works before going further. If this is new for you, we recommend starting with the [Hello world app](/tools/deno-slack-sdk/tutorials/hello-world-app) first.

### Create the project {#create-the-project}

Navigate to a directory where you have permission to create new files. Using the Slack CLI, run the following command to create a new project from a template:

```text
slack create time-zone-app --template slack-samples/deno-blank-template
```

This creates your project from a blank template. After that, navigate to your project folder.

```text
cd time-zone-app
```

Open the project in VSCode.

```text
code .
```

## Code the app {#code-the-app}

### Update the manifest {#update-the-manifest}

The app manifest is where your app's configurations are stored. Navigate to the `manifest.ts` file in your project and replace the template code with what is shown here.

```python
import { Manifest } from "deno-slack-sdk/mod.ts";/** * The app manifest contains the app's configuration. This * file defines attributes like app name and description. */export default Manifest({  name: "Time zone scheduler",  description: "Assists in scheduling meetings across time zones",  icon: "app_icon.png",  functions: [],  workflows: [],  outgoingDomains: ["timeapi.io"],  botScopes: ["commands", "chat:write", "chat:write.public"],});
```

We're going to be creating a custom function to be used as a workflow step in Workflow Builder, so we need to declare that in the manifest. Add this import to the top of the file:

```python
import { TimeZoneSchedulerFunction } from "./functions/timezone_scheduler_function.ts";
```

In the `functions` object, add the function reference, like this:

```text
functions: [TimeZoneSchedulerFunction],
```

Additionally, use the icon of your choice and update the reference in the `icon` property. It is a required field. Save your changes.

### Code the custom function {#code-the-custom-function}

A custom function in Slack requires two components: the function definition, `DefineFunction`, and the function logic, `SlackFunction`. Create a new folder in your project named `functions`, then create a file in that folder named `timezone_scheduler_function.ts`. Copy and paste the code below into the new file, then save it.

```python
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";// Function definitionexport const TimeZoneSchedulerFunction = DefineFunction({  callback_id: "time_zone_scheduler",  title: "Time Zone-Aware Meeting Scheduler",  description:    "Converts a proposed meeting time to the participant's time zone and calculates the end time.",  source_file: "functions/timezone_scheduler_function.ts",  input_parameters: {    properties: {      meeting_time: {        type: Schema.types.string,        description:          "Proposed meeting time (e.g., '2023-08-12T14:30:00Z' or 'Aug 12, 2023, 2:30:00 PM')",      },      user_timezone: {        type: Schema.types.string,        description:          "User's local date and time with timezone (e.g., 'August 14th, 2024 at 11:06 PM GMT+2')",      },      from_timezone: {        type: Schema.types.string,        description:          "Time zone of the user who proposed the meeting (e.g., 'America/New_York')",      },      target_timezone: {        type: Schema.types.string,        description:          "Time zone of the meeting participant (e.g., 'Europe/London')",      },      duration_minutes: {        type: Schema.types.number,        description: "The duration of the meeting in minutes"      }    },    required: [      "meeting_time",      "user_timezone",      "from_timezone",      "target_timezone",      "duration_minutes"    ],  },  output_parameters: {    properties: {      readable_time_origin: {        type: Schema.types.string,        description: "Readable meeting time in the user's time zone",      },      readable_time_participant: {        type: Schema.types.string,        description: "Readable meeting time in the participant's time zone",      },      calendar_meeting_time: {        type: Schema.slack.types.timestamp,        description: "Meeting time in the user's timezone",      },      calendar_end_time: {        type: Schema.slack.types.timestamp,        description: "Ending meeting time"      }    },    required: [        "readable_time_origin",        "readable_time_participant",        "calendar_meeting_time",        "calendar_end_time"    ],  },});export default SlackFunction(  TimeZoneSchedulerFunction,  async ({ inputs }) => {    let readableTimeOrigin: string | null = null;    let readableTimeParticipant: string | null = null;    let calendarMeetingTime: number | null = null;    let calendarEndTime: number | null = null;    try {      // Step 1: Correctly format the meeting time for API usage      const formattedMeetingTime = formatDateTimeForAPI(        inputs.meeting_time,      );      const meetingConversionResult = await convertTimeZone(        inputs.from_timezone,        formattedMeetingTime,        inputs.target_timezone,      );      if (        !meetingConversionResult ||        !meetingConversionResult.conversionResult      ) {        throw new Error("Invalid DateTime format from API.");      }      // Step 2: Convert meeting_time from from_timezone to user timezone      const calendarConversionResult = await convertTimeZone(        inputs.from_timezone,        formattedMeetingTime,        inputs.user_timezone,      );      if (        !calendarConversionResult || !calendarConversionResult.conversionResult      ) {        throw new Error("Invalid DateTime format from API.");      }      // Extract the calendar meeting time in user's timezone      const userTimeZoneDate = new Date(        calendarConversionResult.conversionResult.dateTime,      );      calendarMeetingTime = Math.floor(userTimeZoneDate.getTime() / 1000);      // Step 4: Calculate readable times      const originTime = new Date(inputs.meeting_time);      readableTimeOrigin = originTime.toLocaleString("en-US", {        hour: "numeric",        minute: "numeric",        hour12: true,      });      const participantDateTime = new Date(        meetingConversionResult.conversionResult.dateTime,      );      readableTimeParticipant = participantDateTime.toLocaleString("en-US", {        hour: "numeric",        minute: "numeric",        hour12: true,      });      // Step 5: Calculate end time for user      const endTimeUser = new Date(        userTimeZoneDate.getTime() + inputs.duration_minutes * 60000,      );      calendarEndTime = Math.floor(endTimeUser.getTime() / 1000);    } catch (error) {      return {        error: `Error converting time: ${error.message}`,      };    }    return {      outputs: {        readable_time_origin: readableTimeOrigin,        readable_time_participant: readableTimeParticipant,        calendar_meeting_time: calendarMeetingTime,        calendar_end_time: calendarEndTime,      },    };  },);
```

You may notice in the function logic, we call a couple of helper functions: `formatDateTimeForAPI` and `convertTimeZone`. We'll create those function files next.

### Add support files {#add-support-files}

There are a few other files we need to support this app; we will create them now.

Add a new folder to the project named `util`. Create a file in that folder named `api_date_formatter.ts`. This file will help to parse and format dates. Copy and paste the following code into the file, then save.

```javascript
 export const formatDateTimeForAPI = (dateTimeString: string): string => {  const date = new Date(dateTimeString);  if (isNaN(date.getTime())) {    throw new Error(`Invalid date format: ${dateTimeString}`);  }  const year = date.getFullYear();  const month = String(date.getMonth() + 1).padStart(2, "0");  const day = String(date.getDate()).padStart(2, "0");  const hours = String(date.getHours()).padStart(2, "0");  const minutes = String(date.getMinutes()).padStart(2, "0");  const seconds = String(date.getSeconds()).padStart(2, "0");  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;}
```

Create another file in the `util` folder and name it `convert_timezone.ts`. This file converts the `from` time zone to the `to` time zone. Copy and paste the following code into it, then save.

```python
/** * Converts a given date and time from one timezone to another using the Time API. * @param fromTimeZone - The original timezone of the date and time. * @param dateTime - The date and time to be converted. * @param toTimeZone - The target timezone for the conversion. * @returns A promise that resolves to the converted date and time result. */export async function convertTimeZone(  fromTimeZone: string,  dateTime: string,  toTimeZone: string): Promise<any> {  try {    const response = await fetch(      "https://timeapi.io/api/Conversion/ConvertTimeZone",      {        method: "POST",        headers: {          accept: "application/json",          "Content-Type": "application/json",        },        body: JSON.stringify({          fromTimeZone,          dateTime,          toTimeZone,          dstAmbiguity: "",        }),      }    );    if (!response.ok) {      throw new Error("Failed to convert time zone");    }    const data = await response.json();    return data;  } catch (error) {    console.error("Error during time zone conversion:", error);    throw error;  }}
```

Be sure to add the imports for these files to the top of the `timezone_scheduler_function.ts` file, like this:

```python
import { formatDateTimeForAPI } from "../util/api_date_formatter.ts";import { convertTimeZone } from "../util/convert_timezone.ts";
```

Create one more file in the `util` folder and name it `timezones.txt`. This is the full list of available time zones. Copy and paste the following text into it, then save the file.

Time zones

```text
[  "Africa/Abidjan",  "Africa/Accra",  "Africa/Addis_Ababa",  "Africa/Algiers",  "Africa/Asmara",  "Africa/Asmera",  "Africa/Bamako",  "Africa/Bangui",  "Africa/Banjul",  "Africa/Bissau",  "Africa/Blantyre",  "Africa/Brazzaville",  "Africa/Bujumbura",  "Africa/Cairo",  "Africa/Casablanca",  "Africa/Ceuta",  "Africa/Conakry",  "Africa/Dakar",  "Africa/Dar_es_Salaam",  "Africa/Djibouti",  "Africa/Douala",  "Africa/El_Aaiun",  "Africa/Freetown",  "Africa/Gaborone",  "Africa/Harare",  "Africa/Johannesburg",  "Africa/Juba",  "Africa/Kampala",  "Africa/Khartoum",  "Africa/Kigali",  "Africa/Kinshasa",  "Africa/Lagos",  "Africa/Libreville",  "Africa/Lome",  "Africa/Luanda",  "Africa/Lubumbashi",  "Africa/Lusaka",  "Africa/Malabo",  "Africa/Maputo",  "Africa/Maseru",  "Africa/Mbabane",  "Africa/Mogadishu",  "Africa/Monrovia",  "Africa/Nairobi",  "Africa/Ndjamena",  "Africa/Niamey",  "Africa/Nouakchott",  "Africa/Ouagadougou",  "Africa/Porto-Novo",  "Africa/Sao_Tome",  "Africa/Timbuktu",  "Africa/Tripoli",  "Africa/Tunis",  "Africa/Windhoek",  "America/Adak",  "America/Anchorage",  "America/Anguilla",  "America/Antigua",  "America/Araguaina",  "America/Argentina/Buenos_Aires",  "America/Argentina/Catamarca",  "America/Argentina/ComodRivadavia",  "America/Argentina/Cordoba",  "America/Argentina/Jujuy",  "America/Argentina/La_Rioja",  "America/Argentina/Mendoza",  "America/Argentina/Rio_Gallegos",  "America/Argentina/Salta",  "America/Argentina/San_Juan",  "America/Argentina/San_Luis",  "America/Argentina/Tucuman",  "America/Argentina/Ushuaia",  "America/Aruba",  "America/Asuncion",  "America/Atikokan",  "America/Atka",  "America/Bahia",  "America/Bahia_Banderas",  "America/Barbados",  "America/Belem",  "America/Belize",  "America/Blanc-Sablon",  "America/Boa_Vista",  "America/Bogota",  "America/Boise",  "America/Buenos_Aires",  "America/Cambridge_Bay",  "America/Campo_Grande",  "America/Cancun",  "America/Caracas",  "America/Catamarca",  "America/Cayenne",  "America/Cayman",  "America/Chicago",  "America/Chihuahua",  "America/Ciudad_Juarez",  "America/Coral_Harbour",  "America/Cordoba",  "America/Costa_Rica",  "America/Creston",  "America/Cuiaba",  "America/Curacao",  "America/Danmarkshavn",  "America/Dawson",  "America/Dawson_Creek",  "America/Denver",  "America/Detroit",  "America/Dominica",  "America/Edmonton",  "America/Eirunepe",  "America/El_Salvador",  "America/Ensenada",  "America/Fort_Nelson",  "America/Fort_Wayne",  "America/Fortaleza",  "America/Glace_Bay",  "America/Godthab",  "America/Goose_Bay",  "America/Grand_Turk",  "America/Grenada",  "America/Guadeloupe",  "America/Guatemala",  "America/Guayaquil",  "America/Guyana",  "America/Halifax",  "America/Havana",  "America/Hermosillo",  "America/Indiana/Indianapolis",  "America/Indiana/Knox",  "America/Indiana/Marengo",  "America/Indiana/Petersburg",  "America/Indiana/Tell_City",  "America/Indiana/Vevay",  "America/Indiana/Vincennes",  "America/Indiana/Winamac",  "America/Indianapolis",  "America/Inuvik",  "America/Iqaluit",  "America/Jamaica",  "America/Jujuy",  "America/Juneau",  "America/Kentucky/Louisville",  "America/Kentucky/Monticello",  "America/Knox_IN",  "America/Kralendijk",  "America/La_Paz",  "America/Lima",  "America/Los_Angeles",  "America/Louisville",  "America/Lower_Princes",  "America/Maceio",  "America/Managua",  "America/Manaus",  "America/Marigot",  "America/Martinique",  "America/Matamoros",  "America/Mazatlan",  "America/Mendoza",  "America/Menominee",  "America/Merida",  "America/Metlakatla",  "America/Mexico_City",  "America/Miquelon",  "America/Moncton",  "America/Monterrey",  "America/Montevideo",  "America/Montreal",  "America/Montserrat",  "America/Nassau",  "America/New_York",  "America/Nipigon",  "America/Nome",  "America/Noronha",  "America/North_Dakota/Beulah",  "America/North_Dakota/Center",  "America/North_Dakota/New_Salem",  "America/Nuuk",  "America/Ojinaga",  "America/Panama",  "America/Pangnirtung",  "America/Paramaribo",  "America/Phoenix",  "America/Port_of_Spain",  "America/Port-au-Prince",  "America/Porto_Acre",  "America/Porto_Velho",  "America/Puerto_Rico",  "America/Punta_Arenas",  "America/Rainy_River",  "America/Rankin_Inlet",  "America/Recife",  "America/Regina",  "America/Resolute",  "America/Rio_Branco",  "America/Rosario",  "America/Santa_Isabel",  "America/Santarem",  "America/Santiago",  "America/Santo_Domingo",  "America/Sao_Paulo",  "America/Scoresbysund",  "America/Shiprock",  "America/Sitka",  "America/St_Barthelemy",  "America/St_Johns",  "America/St_Kitts",  "America/St_Lucia",  "America/St_Thomas",  "America/St_Vincent",  "America/Swift_Current",  "America/Tegucigalpa",  "America/Thule",  "America/Thunder_Bay",  "America/Tijuana",  "America/Toronto",  "America/Tortola",  "America/Vancouver",  "America/Virgin",  "America/Whitehorse",  "America/Winnipeg",  "America/Yakutat",  "America/Yellowknife",  "Antarctica/Casey",  "Antarctica/Davis",  "Antarctica/DumontDUrville",  "Antarctica/Macquarie",  "Antarctica/Mawson",  "Antarctica/McMurdo",  "Antarctica/Palmer",  "Antarctica/Rothera",  "Antarctica/South_Pole",  "Antarctica/Syowa",  "Antarctica/Troll",  "Antarctica/Vostok",  "Arctic/Longyearbyen",  "Asia/Aden",  "Asia/Almaty",  "Asia/Amman",  "Asia/Anadyr",  "Asia/Aqtau",  "Asia/Aqtobe",  "Asia/Ashgabat",  "Asia/Ashkhabad",  "Asia/Atyrau",  "Asia/Baghdad",  "Asia/Bahrain",  "Asia/Baku",  "Asia/Bangkok",  "Asia/Barnaul",  "Asia/Beirut",  "Asia/Bishkek",  "Asia/Brunei",  "Asia/Calcutta",  "Asia/Chita",  "Asia/Choibalsan",  "Asia/Chongqing",  "Asia/Chungking",  "Asia/Colombo",  "Asia/Dacca",  "Asia/Damascus",  "Asia/Dhaka",  "Asia/Dili",  "Asia/Dubai",  "Asia/Dushanbe",  "Asia/Famagusta",  "Asia/Gaza",  "Asia/Harbin",  "Asia/Hebron",  "Asia/Ho_Chi_Minh",  "Asia/Hong_Kong",  "Asia/Hovd",  "Asia/Irkutsk",  "Asia/Istanbul",  "Asia/Jakarta",  "Asia/Jayapura",  "Asia/Jerusalem",  "Asia/Kabul",  "Asia/Kamchatka",  "Asia/Karachi",  "Asia/Kashgar",  "Asia/Kathmandu",  "Asia/Katmandu",  "Asia/Khandyga",  "Asia/Kolkata",  "Asia/Krasnoyarsk",  "Asia/Kuala_Lumpur",  "Asia/Kuching",  "Asia/Kuwait",  "Asia/Macao",  "Asia/Macau",  "Asia/Magadan",  "Asia/Makassar",  "Asia/Manila",  "Asia/Muscat",  "Asia/Nicosia",  "Asia/Novokuznetsk",  "Asia/Novosibirsk",  "Asia/Omsk",  "Asia/Oral",  "Asia/Phnom_Penh",  "Asia/Pontianak",  "Asia/Pyongyang",  "Asia/Qatar",  "Asia/Qostanay",  "Asia/Qyzylorda",  "Asia/Rangoon",  "Asia/Riyadh",  "Asia/Saigon",  "Asia/Sakhalin",  "Asia/Samarkand",  "Asia/Seoul",  "Asia/Shanghai",  "Asia/Singapore",  "Asia/Srednekolymsk",  "Asia/Taipei",  "Asia/Tashkent",  "Asia/Tbilisi",  "Asia/Tehran",  "Asia/Tel_Aviv",  "Asia/Thimbu",  "Asia/Thimphu",  "Asia/Tokyo",  "Asia/Tomsk",  "Asia/Ujung_Pandang",  "Asia/Ulaanbaatar",  "Asia/Ulan_Bator",  "Asia/Urumqi",  "Asia/Ust-Nera",  "Asia/Vientiane",  "Asia/Vladivostok",  "Asia/Yakutsk",  "Asia/Yangon",  "Asia/Yekaterinburg",  "Asia/Yerevan",  "Atlantic/Azores",  "Atlantic/Bermuda",  "Atlantic/Canary",  "Atlantic/Cape_Verde",  "Atlantic/Faeroe",  "Atlantic/Faroe",  "Atlantic/Jan_Mayen",  "Atlantic/Madeira",  "Atlantic/Reykjavik",  "Atlantic/South_Georgia",  "Atlantic/St_Helena",  "Atlantic/Stanley",  "Australia/ACT",  "Australia/Adelaide",  "Australia/Brisbane",  "Australia/Broken_Hill",  "Australia/Canberra",  "Australia/Currie",  "Australia/Darwin",  "Australia/Eucla",  "Australia/Hobart",  "Australia/LHI",  "Australia/Lindeman",  "Australia/Lord_Howe",  "Australia/Melbourne",  "Australia/North",  "Australia/NSW",  "Australia/Perth",  "Australia/Queensland",  "Australia/South",  "Australia/Sydney",  "Australia/Tasmania",  "Australia/Victoria",  "Australia/West",  "Australia/Yancowinna",  "Brazil/Acre",  "Brazil/DeNoronha",  "Brazil/East",  "Brazil/West",  "Canada/Atlantic",  "Canada/Central",  "Canada/Eastern",  "Canada/Mountain",  "Canada/Newfoundland",  "Canada/Pacific",  "Canada/Saskatchewan",  "Canada/Yukon",  "CET",  "Chile/Continental",  "Chile/EasterIsland",  "CST6CDT",  "Cuba",  "EET",  "Egypt",  "Eire",  "EST",  "EST5EDT",  "Etc/GMT",  "Etc/GMT-0",  "Etc/GMT-1",  "Etc/GMT-10",  "Etc/GMT-11",  "Etc/GMT-12",  "Etc/GMT-13",  "Etc/GMT-14",  "Etc/GMT-2",  "Etc/GMT-3",  "Etc/GMT-4",  "Etc/GMT-5",  "Etc/GMT-6",  "Etc/GMT-7",  "Etc/GMT-8",  "Etc/GMT-9",  "Etc/GMT+0",  "Etc/GMT+1",  "Etc/GMT+10",  "Etc/GMT+11",  "Etc/GMT+12",  "Etc/GMT+2",  "Etc/GMT+3",  "Etc/GMT+4",  "Etc/GMT+5",  "Etc/GMT+6",  "Etc/GMT+7",  "Etc/GMT+8",  "Etc/GMT+9",  "Etc/GMT0",  "Etc/Greenwich",  "Etc/UCT",  "Etc/Universal",  "Etc/UTC",  "Etc/Zulu",  "Europe/Amsterdam",  "Europe/Andorra",  "Europe/Astrakhan",  "Europe/Athens",  "Europe/Belfast",  "Europe/Belgrade",  "Europe/Berlin",  "Europe/Bratislava",  "Europe/Brussels",  "Europe/Bucharest",  "Europe/Budapest",  "Europe/Busingen",  "Europe/Chisinau",  "Europe/Copenhagen",  "Europe/Dublin",  "Europe/Gibraltar",  "Europe/Guernsey",  "Europe/Helsinki",  "Europe/Isle_of_Man",  "Europe/Istanbul",  "Europe/Jersey",  "Europe/Kaliningrad",  "Europe/Kiev",  "Europe/Kirov",  "Europe/Kyiv",  "Europe/Lisbon",  "Europe/Ljubljana",  "Europe/London",  "Europe/Luxembourg",  "Europe/Madrid",  "Europe/Malta",  "Europe/Mariehamn",  "Europe/Minsk",  "Europe/Monaco",  "Europe/Moscow",  "Europe/Nicosia",  "Europe/Oslo",  "Europe/Paris",  "Europe/Podgorica",  "Europe/Prague",  "Europe/Riga",  "Europe/Rome",  "Europe/Samara",  "Europe/San_Marino",  "Europe/Sarajevo",  "Europe/Saratov",  "Europe/Simferopol",  "Europe/Skopje",  "Europe/Sofia",  "Europe/Stockholm",  "Europe/Tallinn",  "Europe/Tirane",  "Europe/Tiraspol",  "Europe/Ulyanovsk",  "Europe/Uzhgorod",  "Europe/Vaduz",  "Europe/Vatican",  "Europe/Vienna",  "Europe/Vilnius",  "Europe/Volgograd",  "Europe/Warsaw",  "Europe/Zagreb",  "Europe/Zaporozhye",  "Europe/Zurich",  "GB",  "GB-Eire",  "GMT",  "GMT-0",  "GMT+0",  "GMT0",  "Greenwich",  "Hongkong",  "HST",  "Iceland",  "Indian/Antananarivo",  "Indian/Chagos",  "Indian/Christmas",  "Indian/Cocos",  "Indian/Comoro",  "Indian/Kerguelen",  "Indian/Mahe",  "Indian/Maldives",  "Indian/Mauritius",  "Indian/Mayotte",  "Indian/Reunion",  "Iran",  "Israel",  "Jamaica",  "Japan",  "Kwajalein",  "Libya",  "MET",  "Mexico/BajaNorte",  "Mexico/BajaSur",  "Mexico/General",  "MST",  "MST7MDT",  "Navajo",  "NZ",  "NZ-CHAT",  "Pacific/Apia",  "Pacific/Auckland",  "Pacific/Bougainville",  "Pacific/Chatham",  "Pacific/Chuuk",  "Pacific/Easter",  "Pacific/Efate",  "Pacific/Enderbury",  "Pacific/Fakaofo",  "Pacific/Fiji",  "Pacific/Funafuti",  "Pacific/Galapagos",  "Pacific/Gambier",  "Pacific/Guadalcanal",  "Pacific/Guam",  "Pacific/Honolulu",  "Pacific/Johnston",  "Pacific/Kanton",  "Pacific/Kiritimati",  "Pacific/Kosrae",  "Pacific/Kwajalein",  "Pacific/Majuro",  "Pacific/Marquesas",  "Pacific/Midway",  "Pacific/Nauru",  "Pacific/Niue",  "Pacific/Norfolk",  "Pacific/Noumea",  "Pacific/Pago_Pago",  "Pacific/Palau",  "Pacific/Pitcairn",  "Pacific/Pohnpei",  "Pacific/Ponape",  "Pacific/Port_Moresby",  "Pacific/Rarotonga",  "Pacific/Saipan",  "Pacific/Samoa",  "Pacific/Tahiti",  "Pacific/Tarawa",  "Pacific/Tongatapu",  "Pacific/Truk",  "Pacific/Wake",  "Pacific/Wallis",  "Pacific/Yap",  "Poland",  "Portugal",  "PRC",  "PST8PDT",  "ROC",  "ROK",  "Singapore",  "Turkey",  "UCT",  "Universal",  "US/Alaska",  "US/Aleutian",  "US/Arizona",  "US/Central",  "US/East-Indiana",  "US/Eastern",  "US/Hawaii",  "US/Indiana-Starke",  "US/Michigan",  "US/Mountain",  "US/Pacific",  "US/Samoa",  "UTC",  "W-SU",  "WET",  "Zulu"]
```

The last file we'll create is a `slack.json` file. Create this in the project (the root of the project, not within folder) and paste the code here into it, then save:

```text
{  "hooks": {    "get-hooks": "deno run -q --allow-read --allow-net https://deno.land/x/deno_slack_hooks@1.3.1/mod.ts"  }}
```

This allows your app to access an external source - the time conversion API.

### Run the app {#run-the-app}

In your terminal window, run the following command:

```text
slack run
```

Select the workspace you'd like to run the app in. If successful, you'll see a message that says `Connected awaiting events`.

## Build the workflow in Workflow Builder {#build-the-workflow-in-workflow-builder}

To create a new workflow, you will need to open Workflow Builder in Slack. You can open Workflow Builder using one of the following methods.

* **Use the message box:** In any channel, type `/workflow` and select **Create a workflow**.
* **Use the sidebar:** Navigate to the left sidebar in Slack and click **More**, then **Tools**, then **Workflows**. Click **+New** then **Build Workflow** to create a new workflow.

Under **Start the workflow...**, click **Choose an event**, then select **From a link in Slack**.

The first step of the workflow is to collect info in a form.

* Click the button to continue, then select **Add steps** to **Collect info in a form**.
* Give the form a name, like `Time zone scheduler`, and click **\+ Add question**. Enter `From which time zone?` as the question and use **Short answer** for the Question type. Click **Done**.
* Repeat the process for adding the following questions and types:
  * `Date and time of the meeting?` → date/time picker
  * `How long is your meeting (in minutes)?` → number
  * `To which time zone?` → short answer
  * `What is your meeting about?` → short answer
  * `Email of your contact` → short answer
  * `Your time zone when running the workflow` → short answer

Save the form.

### Add custom function {#add-custom-function}

With your custom function now available in Workflow Builder (after running `slack run`), add it as the second step in the workflow by clicking **\+ Add steps**, then searching for your app by name in the left sidebar search. Select **Time Zone-Aware Meeting Scheduler** as the step.

We need to connect the info we collected on the previous step to pass it as input of our function. For that we’re going to use variables. Click on the `{}` on the right side of the inputs and choose the following:

* **Meeting time**: `{}Answer to: Date and time of the meeting?` Then click on the caret and choose the local compact format (that’s the format we expect in the code of our custom function).
* **User timezone**: `{}Answer to: Your timezone when running the workflow`
* **From timezone**: `{}Answer to: From which timezone`
* **Target timezone**: `{}Answer to: To which timezone`
* **Duration in minutes**: `{}Answer to: How long is your meeting (in minutes)?`

Save your changes.

### Send a message {#send-a-message}

Now, inform the user of the time conversion results. Add another step to the workflow and in the sidebar, search for **Messages** > **Send a message to a person**.

You can craft your own message using all the variables available from previous steps. Here’s an example:

![Send message step](/assets/images/send-message-237f57c0d633b32222fc0aa7ffbec04f.png)

Enable the **Include a button** option and customize the button label. The workflow will pause here and continue once the user clicks the button. Save your changes to continue.

### Use the Google Calendar connector {#use-the-google-calendar-connector}

Add another step to the workflow and in the sidebar, search for **Google Calendar** > **Create a calendar event** > **Add just the step**. Confirm by clicking the **Set Up** button. Fill in the event details using the variables from previous steps.

![Calendar connector step](/assets/images/calendar-connector-ef257ebebd5994ea3dcadbde544adcbb.png)

### Confirm with a message in thread {#confirm-with-a-message-in-thread}

To finish, let the user know the event has been successfully scheduled. Add another step to the workflow and in the sidebar, search for **Messages** > **Reply to a message in thread**.

Using the available variables, craft a message that says: Calendar invite sent for `{} Answer to: What's your meeting about?`. You can see it here `{} Event link` .

Where `{} Answer to: What's your meeting about?` and `{} Event link` are variables added by clicking the variable button.

## Test your function {#test-your-function}

Your workflow is now complete! Click the **Finish Up** button in Workflow Builder, name your workflow, click **Publish**, and copy the generated link trigger. Share the link in your test Slack channel or add it as a bookmark or to your channel canvas.

## Deploy your function {#deploy-your-function}

In the process of developing your function, you ran it on your local machine. As soon as you shut that environment down or turn off your computer, the function will stop running. Deploying your function to infrastructure managed by Slack ensures that the function is always available.

To deploy your function to production, run:

```text
slack deploy
```

Choose the appropriate workspace for deployment. Remember, the local version (`slack run`) and the production version (`slack deploy`) are separate. Update Workflow Builder to use the production function and reconnect input variables.
