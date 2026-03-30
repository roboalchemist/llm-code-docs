# Source: https://docs.anyscale.com/jobs/schedules.md

# Job schedules

[View Markdown](/jobs/schedules.md)

# Job schedules

Schedules allow you to run Anyscale jobs at a specified cadence using a cron expression. For example you can schedule a training or inference workload to automatically run every day at a specified time. You can reuse an existing job's config to specify the job to run at the desired cadence.

```
timezone: local
cron_expression: 0 0 * * * *
job_config:
    name: SCHEDULE_NAME
    entrypoint: python main.py
    max_retries: 5
    ... # Your JobConfig
```

Then, run the following command to create or update a schedule:

```
anyscale schedule apply -f schedule.yaml  # Run the job every night
```

For more info about the Anyscale Job YAML spec, see the [reference docs](/reference/job-api.md#jobconfig). For more information about how to specify cron expressions and timezones, see [cron expressions and timezones](/jobs/schedules.md#cron-timezones). The rest of this guide covers a more comprehensive example.

## Creating a schedule[​](#creating-a-schedule "Direct link to Creating a schedule")

important

Schedules have unique names within an [Anyscale project](/administration/organization/permissions.md#projects). If you try to create a schedule with an existing name, this action updates the existing schedule rather than creating a new one.

In this example, create a simple schedule that runs an Anyscale job every 10 minutes to say "Hello world!"

In a new directory, create a file `hello_world.py` that contains the following:

```
import ray

@ray.remote
def hello_world():
    return "Hello World!"

result = ray.get(hello_world.remote())
print(result)
```

* CLI
* SDK

To create a schedule with the CLI, create a file named `schedule.yaml` with the schedule's configuration, as in the following example:

```
timezone: local
cron_expression: "*/10 * * * *"
job_config:
    name: schedule-demo
    entrypoint: python hello_world.py
    working_dir: .
```

From the same directory, run the following command to create the schedule:

```
anyscale schedule apply -f schedule.yaml
```

The following code uses the Python SDK to create a schedule:

```
import anyscale
from anyscale.job.models import JobConfig
from anyscale.schedule.models import ScheduleConfig

anyscale.schedule.apply(
    ScheduleConfig(
        cron_expression="*/10 * * * *",
        job_config=JobConfig(
            name="schedule-demo",
            entrypoint="python hello_world.py",
            working_dir=".",
        )
    )
)
```

To update the schedule, modify the `schedule.yaml` or the `ScheduleConfig` and then rerun the corresponding command in the CLI or SDK. This updates the existing schedule in place.

## Viewing the status of a schedule[​](#viewing-the-status-of-a-schedule "Direct link to Viewing the status of a schedule")

You can view the status of a schedule:

* CLI
* SDK

```
anyscale schedule status --name schedule-demo
```

```
id: cronjob_UXq1VqfXkbQRBeLTfsbveY7r
name: schedule-demo
state: ENABLED
```

```
import anyscale

print(anyscale.schedule.status(name="schedule-demo"))
```

```
ScheduleStatus(
  config=ScheduleConfig(
    job_config=JobConfig(
      name='schedule-demo',
      image_uri=None,
      compute_config=ComputeConfig(cloud='anyscale_v2_default_cloud'),
      env_vars=None,
      py_modules=None,
      cloud='anyscale_v2_default_cloud',
      project=None,
      ray_version=None,
      job_queue_config=None
    ),
    cron_expression='*/10 * * * *',
    timezone='UTC'
  ),
  id='cronjob_UXq1VqfXkbQRBeLTfsbveY7r',
  name='schedule-demo',
  state=<ScheduleState.ENABLED: 'ENABLED'>
)
```

## Manually run the schedule[​](#manually-run-the-schedule "Direct link to Manually run the schedule")

If you don't want to wait for the next trigger time, you can manually run the schedule by name to start a job immediately.

* CLI
* SDK

```
anyscale schedule run --name schedule-demo
```

```
import anyscale

anyscale.schedule.trigger(name="schedule-demo")
```

## Enable and disable a schedule[​](#enable-and-disable-a-schedule "Direct link to Enable and disable a schedule")

To pause a schedule, run the following:

* CLI
* SDK

```
anyscale schedule pause --name schedule-demo
```

```
import anyscale
from anyscale.schedule.models import ScheduleState

anyscale.schedule.set_state(name="schedule-demo", state=ScheduleState.DISABLED)
```

Here is how to resume the schedule:

* CLI
* SDK

```
anyscale schedule resume --name schedule-demo
```

```
import anyscale
from anyscale.schedule.models import ScheduleState

anyscale.schedule.set_state(name="schedule-demo", state=ScheduleState.ENABLED)
```

## cron expressions and timezones[​](#cron-timezones "Direct link to cron expressions and timezones")

Job schedules let you specify when to trigger the schedule based on a `cron_expression`. The format of a cron expression is:

```
*        *        *        *        *
min    hour  day(month)  month   day(week)
```

For example, the cron expression:

```
0 9 1 * *
```

means fire at:

1. The 0th minute
2. The 9th hour
3. The first day of the month
4. Every month
5. Every day of the week

In other words, 9 AM on the first of each month.

Schedules also let you specify a timezone in which to interpret the cron expression. For example, to tell the schedule to fire at 9 AM on the first of each month in Pacific Standard Time, use the following config:

```
schedule:
  cron_expression: 0 9 1 * *
  timezone: "America/Los_Angeles"
```

In the CLI, specify `timezone: local` to detect the local timezone.

For more help constructing a cron expression, and to view the extended syntax, see [crontab.guru](https://crontab.guru).

All supported timezones are shown below. You can view more information about these timezones [in Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

All supported timezones

Africa/Abidjan<br />Africa/Accra<br />Africa/Addis\_Ababa<br />Africa/Algiers<br />Africa/Asmara<br />Africa/Asmera<br />Africa/Bamako<br />Africa/Bangui<br />Africa/Banjul<br />Africa/Bissau<br />Africa/Blantyre<br />Africa/Brazzaville<br />Africa/Bujumbura<br />Africa/Cairo<br />Africa/Casablanca<br />Africa/Ceuta<br />Africa/Conakry<br />Africa/Dakar<br />Africa/Dar\_es\_Salaam<br />Africa/Djibouti<br />Africa/Douala<br />Africa/El\_Aaiun<br />Africa/Freetown<br />Africa/Gaborone<br />Africa/Harare<br />Africa/Johannesburg<br />Africa/Juba<br />Africa/Kampala<br />Africa/Khartoum<br />Africa/Kigali<br />Africa/Kinshasa<br />Africa/Lagos<br />Africa/Libreville<br />Africa/Lome<br />Africa/Luanda<br />Africa/Lubumbashi<br />Africa/Lusaka<br />Africa/Malabo<br />Africa/Maputo<br />Africa/Maseru<br />Africa/Mbabane<br />Africa/Mogadishu<br />Africa/Monrovia<br />Africa/Nairobi<br />Africa/Ndjamena<br />Africa/Niamey<br />Africa/Nouakchott<br />Africa/Ouagadougou<br />Africa/Porto-Novo<br />Africa/Sao\_Tome<br />Africa/Timbuktu<br />Africa/Tripoli<br />Africa/Tunis<br />Africa/Windhoek<br />America/Adak<br />America/Anchorage<br />America/Anguilla<br />America/Antigua<br />America/Araguaina<br />America/Argentina/Buenos\_Aires<br />America/Argentina/Catamarca<br />America/Argentina/ComodRivadavia<br />America/Argentina/Cordoba<br />America/Argentina/Jujuy<br />America/Argentina/La\_Rioja<br />America/Argentina/Mendoza<br />America/Argentina/Rio\_Gallegos<br />America/Argentina/Salta<br />America/Argentina/San\_Juan<br />America/Argentina/San\_Luis<br />America/Argentina/Tucuman<br />America/Argentina/Ushuaia<br />America/Aruba<br />America/Asuncion<br />America/Atikokan<br />America/Atka<br />America/Bahia<br />America/Bahia\_Banderas<br />America/Barbados<br />America/Belem<br />America/Belize<br />America/Blanc-Sablon<br />America/Boa\_Vista<br />America/Bogota<br />America/Boise<br />America/Buenos\_Aires<br />America/Cambridge\_Bay<br />America/Campo\_Grande<br />America/Cancun<br />America/Caracas<br />America/Catamarca<br />America/Cayenne<br />America/Cayman<br />America/Chicago<br />America/Chihuahua<br />America/Coral\_Harbour<br />America/Cordoba<br />America/Costa\_Rica<br />America/Creston<br />America/Cuiaba<br />America/Curacao<br />America/Danmarkshavn<br />America/Dawson<br />America/Dawson\_Creek<br />America/Denver<br />America/Detroit<br />America/Dominica<br />America/Edmonton<br />America/Eirunepe<br />America/El\_Salvador<br />America/Ensenada<br />America/Fort\_Nelson<br />America/Fort\_Wayne<br />America/Fortaleza<br />America/Glace\_Bay<br />America/Godthab<br />America/Goose\_Bay<br />America/Grand\_Turk<br />America/Grenada<br />America/Guadeloupe<br />America/Guatemala<br />America/Guayaquil<br />America/Guyana<br />America/Halifax<br />America/Havana<br />America/Hermosillo<br />America/Indiana/Indianapolis<br />America/Indiana/Knox<br />America/Indiana/Marengo<br />America/Indiana/Petersburg<br />America/Indiana/Tell\_City<br />America/Indiana/Vevay<br />America/Indiana/Vincennes<br />America/Indiana/Winamac<br />America/Indianapolis<br />America/Inuvik<br />America/Iqaluit<br />America/Jamaica<br />America/Jujuy<br />America/Juneau<br />America/Kentucky/Louisville<br />America/Kentucky/Monticello<br />America/Knox\_IN<br />America/Kralendijk<br />America/La\_Paz<br />America/Lima<br />America/Los\_Angeles<br />America/Louisville<br />America/Lower\_Princes<br />America/Maceio<br />America/Managua<br />America/Manaus<br />America/Marigot<br />America/Martinique<br />America/Matamoros<br />America/Mazatlan<br />America/Mendoza<br />America/Menominee<br />America/Merida<br />America/Metlakatla<br />America/Mexico\_City<br />America/Miquelon<br />America/Moncton<br />America/Monterrey<br />America/Montevideo<br />America/Montreal<br />America/Montserrat<br />America/Nassau<br />America/New\_York<br />America/Nipigon<br />America/Nome<br />America/Noronha<br />America/North\_Dakota/Beulah<br />America/North\_Dakota/Center<br />America/North\_Dakota/New\_Salem<br />America/Nuuk<br />America/Ojinaga<br />America/Panama<br />America/Pangnirtung<br />America/Paramaribo<br />America/Phoenix<br />America/Port-au-Prince<br />America/Port\_of\_Spain<br />America/Porto\_Acre<br />America/Porto\_Velho<br />America/Puerto\_Rico<br />America/Punta\_Arenas<br />America/Rainy\_River<br />America/Rankin\_Inlet<br />America/Recife<br />America/Regina<br />America/Resolute<br />America/Rio\_Branco<br />America/Rosario<br />America/Santa\_Isabel<br />America/Santarem<br />America/Santiago<br />America/Santo\_Domingo<br />America/Sao\_Paulo<br />America/Scoresbysund<br />America/Shiprock<br />America/Sitka<br />America/St\_Barthelemy<br />America/St\_Johns<br />America/St\_Kitts<br />America/St\_Lucia<br />America/St\_Thomas<br />America/St\_Vincent<br />America/Swift\_Current<br />America/Tegucigalpa<br />America/Thule<br />America/Thunder\_Bay<br />America/Tijuana<br />America/Toronto<br />America/Tortola<br />America/Vancouver<br />America/Virgin<br />America/Whitehorse<br />America/Winnipeg<br />America/Yakutat<br />America/Yellowknife<br />Antarctica/Casey<br />Antarctica/Davis<br />Antarctica/DumontDUrville<br />Antarctica/Macquarie<br />Antarctica/Mawson<br />Antarctica/McMurdo<br />Antarctica/Palmer<br />Antarctica/Rothera<br />Antarctica/South\_Pole<br />Antarctica/Syowa<br />Antarctica/Troll<br />Antarctica/Vostok<br />Arctic/Longyearbyen<br />Asia/Aden<br />Asia/Almaty<br />Asia/Amman<br />Asia/Anadyr<br />Asia/Aqtau<br />Asia/Aqtobe<br />Asia/Ashgabat<br />Asia/Ashkhabad<br />Asia/Atyrau<br />Asia/Baghdad<br />Asia/Bahrain<br />Asia/Baku<br />Asia/Bangkok<br />Asia/Barnaul<br />Asia/Beirut<br />Asia/Bishkek<br />Asia/Brunei<br />Asia/Calcutta<br />Asia/Chita<br />Asia/Choibalsan<br />Asia/Chongqing<br />Asia/Chungking<br />Asia/Colombo<br />Asia/Dacca<br />Asia/Damascus<br />Asia/Dhaka<br />Asia/Dili<br />Asia/Dubai<br />Asia/Dushanbe<br />Asia/Famagusta<br />Asia/Gaza<br />Asia/Harbin<br />Asia/Hebron<br />Asia/Ho\_Chi\_Minh<br />Asia/Hong\_Kong<br />Asia/Hovd<br />Asia/Irkutsk<br />Asia/Istanbul<br />Asia/Jakarta<br />Asia/Jayapura<br />Asia/Jerusalem<br />Asia/Kabul<br />Asia/Kamchatka<br />Asia/Karachi<br />Asia/Kashgar<br />Asia/Kathmandu<br />Asia/Katmandu<br />Asia/Khandyga<br />Asia/Kolkata<br />Asia/Krasnoyarsk<br />Asia/Kuala\_Lumpur<br />Asia/Kuching<br />Asia/Kuwait<br />Asia/Macao<br />Asia/Macau<br />Asia/Magadan<br />Asia/Makassar<br />Asia/Manila<br />Asia/Muscat<br />Asia/Nicosia<br />Asia/Novokuznetsk<br />Asia/Novosibirsk<br />Asia/Omsk<br />Asia/Oral<br />Asia/Phnom\_Penh<br />Asia/Pontianak<br />Asia/Pyongyang<br />Asia/Qatar<br />Asia/Qostanay<br />Asia/Qyzylorda<br />Asia/Rangoon<br />Asia/Riyadh<br />Asia/Saigon<br />Asia/Sakhalin<br />Asia/Samarkand<br />Asia/Seoul<br />Asia/Shanghai<br />Asia/Singapore<br />Asia/Srednekolymsk<br />Asia/Taipei<br />Asia/Tashkent<br />Asia/Tbilisi<br />Asia/Tehran<br />Asia/Tel\_Aviv<br />Asia/Thimbu<br />Asia/Thimphu<br />Asia/Tokyo<br />Asia/Tomsk<br />Asia/Ujung\_Pandang<br />Asia/Ulaanbaatar<br />Asia/Ulan\_Bator<br />Asia/Urumqi<br />Asia/Ust-Nera<br />Asia/Vientiane<br />Asia/Vladivostok<br />Asia/Yakutsk<br />Asia/Yangon<br />Asia/Yekaterinburg<br />Asia/Yerevan<br />Atlantic/Azores<br />Atlantic/Bermuda<br />Atlantic/Canary<br />Atlantic/Cape\_Verde<br />Atlantic/Faeroe<br />Atlantic/Faroe<br />Atlantic/Jan\_Mayen<br />Atlantic/Madeira<br />Atlantic/Reykjavik<br />Atlantic/South\_Georgia<br />Atlantic/St\_Helena<br />Atlantic/Stanley<br />Australia/ACT<br />Australia/Adelaide<br />Australia/Brisbane<br />Australia/Broken\_Hill<br />Australia/Canberra<br />Australia/Currie<br />Australia/Darwin<br />Australia/Eucla<br />Australia/Hobart<br />Australia/LHI<br />Australia/Lindeman<br />Australia/Lord\_Howe<br />Australia/Melbourne<br />Australia/NSW<br />Australia/North<br />Australia/Perth<br />Australia/Queensland<br />Australia/South<br />Australia/Sydney<br />Australia/Tasmania<br />Australia/Victoria<br />Australia/West<br />Australia/Yancowinna<br />Brazil/Acre<br />Brazil/DeNoronha<br />Brazil/East<br />Brazil/West<br />CET<br />CST6CDT<br />Canada/Atlantic<br />Canada/Central<br />Canada/Eastern<br />Canada/Mountain<br />Canada/Newfoundland<br />Canada/Pacific<br />Canada/Saskatchewan<br />Canada/Yukon<br />Chile/Continental<br />Chile/EasterIsland<br />Cuba<br />EET<br />EST<br />EST5EDT<br />Egypt<br />Eire<br />Etc/GMT<br />Etc/GMT+0<br />Etc/GMT+1<br />Etc/GMT+10<br />Etc/GMT+11<br />Etc/GMT+12<br />Etc/GMT+2<br />Etc/GMT+3<br />Etc/GMT+4<br />Etc/GMT+5<br />Etc/GMT+6<br />Etc/GMT+7<br />Etc/GMT+8<br />Etc/GMT+9<br />Etc/GMT-0<br />Etc/GMT-1<br />Etc/GMT-10<br />Etc/GMT-11<br />Etc/GMT-12<br />Etc/GMT-13<br />Etc/GMT-14<br />Etc/GMT-2<br />Etc/GMT-3<br />Etc/GMT-4<br />Etc/GMT-5<br />Etc/GMT-6<br />Etc/GMT-7<br />Etc/GMT-8<br />Etc/GMT-9<br />Etc/GMT0<br />Etc/Greenwich<br />Etc/UCT<br />Etc/UTC<br />Etc/Universal<br />Etc/Zulu<br />Europe/Amsterdam<br />Europe/Andorra<br />Europe/Astrakhan<br />Europe/Athens<br />Europe/Belfast<br />Europe/Belgrade<br />Europe/Berlin<br />Europe/Bratislava<br />Europe/Brussels<br />Europe/Bucharest<br />Europe/Budapest<br />Europe/Busingen<br />Europe/Chisinau<br />Europe/Copenhagen<br />Europe/Dublin<br />Europe/Gibraltar<br />Europe/Guernsey<br />Europe/Helsinki<br />Europe/Isle\_of\_Man<br />Europe/Istanbul<br />Europe/Jersey<br />Europe/Kaliningrad<br />Europe/Kiev<br />Europe/Kirov<br />Europe/Lisbon<br />Europe/Ljubljana<br />Europe/London<br />Europe/Luxembourg<br />Europe/Madrid<br />Europe/Malta<br />Europe/Mariehamn<br />Europe/Minsk<br />Europe/Monaco<br />Europe/Moscow<br />Europe/Nicosia<br />Europe/Oslo<br />Europe/Paris<br />Europe/Podgorica<br />Europe/Prague<br />Europe/Riga<br />Europe/Rome<br />Europe/Samara<br />Europe/San\_Marino<br />Europe/Sarajevo<br />Europe/Saratov<br />Europe/Simferopol<br />Europe/Skopje<br />Europe/Sofia<br />Europe/Stockholm<br />Europe/Tallinn<br />Europe/Tirane<br />Europe/Tiraspol<br />Europe/Ulyanovsk<br />Europe/Uzhgorod<br />Europe/Vaduz<br />Europe/Vatican<br />Europe/Vienna<br />Europe/Vilnius<br />Europe/Volgograd<br />Europe/Warsaw<br />Europe/Zagreb<br />Europe/Zaporozhye<br />Europe/Zurich<br />GB<br />GB-Eire<br />GMT<br />GMT+0<br />GMT-0<br />GMT0<br />Greenwich<br />HST<br />Hongkong<br />Iceland<br />Indian/Antananarivo<br />Indian/Chagos<br />Indian/Christmas<br />Indian/Cocos<br />Indian/Comoro<br />Indian/Kerguelen<br />Indian/Mahe<br />Indian/Maldives<br />Indian/Mauritius<br />Indian/Mayotte<br />Indian/Reunion<br />Iran<br />Israel<br />Jamaica<br />Japan<br />Kwajalein<br />Libya<br />MET<br />MST<br />MST7MDT<br />Mexico/BajaNorte<br />Mexico/BajaSur<br />Mexico/General<br />NZ<br />NZ-CHAT<br />Navajo<br />PRC<br />PST8PDT<br />Pacific/Apia<br />Pacific/Auckland<br />Pacific/Bougainville<br />Pacific/Chatham<br />Pacific/Chuuk<br />Pacific/Easter<br />Pacific/Efate<br />Pacific/Enderbury<br />Pacific/Fakaofo<br />Pacific/Fiji<br />Pacific/Funafuti<br />Pacific/Galapagos<br />Pacific/Gambier<br />Pacific/Guadalcanal<br />Pacific/Guam<br />Pacific/Honolulu<br />Pacific/Johnston<br />Pacific/Kanton<br />Pacific/Kiritimati<br />Pacific/Kosrae<br />Pacific/Kwajalein<br />Pacific/Majuro<br />Pacific/Marquesas<br />Pacific/Midway<br />Pacific/Nauru<br />Pacific/Niue<br />Pacific/Norfolk<br />Pacific/Noumea<br />Pacific/Pago\_Pago<br />Pacific/Palau<br />Pacific/Pitcairn<br />Pacific/Pohnpei<br />Pacific/Ponape<br />Pacific/Port\_Moresby<br />Pacific/Rarotonga<br />Pacific/Saipan<br />Pacific/Samoa<br />Pacific/Tahiti<br />Pacific/Tarawa<br />Pacific/Tongatapu<br />Pacific/Truk<br />Pacific/Wake<br />Pacific/Wallis<br />Pacific/Yap<br />Poland<br />Portugal<br />ROC<br />ROK<br />Singapore<br />Turkey<br />UCT<br />US/Alaska<br />US/Aleutian<br />US/Arizona<br />US/Central<br />US/East-Indiana<br />US/Eastern<br />US/Hawaii<br />US/Indiana-Starke<br />US/Michigan<br />US/Mountain<br />US/Pacific<br />US/Samoa<br />UTC<br />Universal<br />W-SU<br />WET<br />Zulu<br />
