# Source: https://smartcar.com/docs/help/frequencies.md

# Data Freshness Frequencies

> Smartcar's goal is to provide as close to real-time data as possible based on available technologies and capabilities from OEMs. Although real-time is not yet available across all OEMs outside of commercial fleets, Smartcar continues to improve these frequencies as platforms and technologies evolve.

<Note>
  The values below indicate a range of how quickly you can expect to see fresh data and not how frequent you can receive data from Smartcar. i.e. You may request/receive odometer every three minutes from Smartcar, but its value won't change until it is refreshed by the OEM.
</Note>

**Data Frequency**: This indicates the frequency at which you receive vehicle data updates that Smartcar delivers to you via webhooks. This frequency can vary based on the vehicle make, the data type (such as location, odometer, or battery), and how frequently the vehicle is driven. In general, you can expect updates to arrive anywhere from every few minutes to once every few hours. While our slowest data rates for all OEMs is an hour, for many vehicles (including the fastest), when the vehicle is idle or "asleep", no updates will be provided since no change has occurred.

Smartcar automatically adjusts polling frequency based on vehicle status to balance timely updates with efficient resource use. While we aim to provide near real-time data when possible, exact timing depends on factors outside of Smartcar's control, such as OEM behavior and vehicle connectivity.

| Make          | Region     | Data Frequency Range (in min) |
| ------------- | ---------- | ----------------------------- |
| ACURA         | US, Canada | 30-60                         |
| ALFA ROMEO    | Global     | 5-10                          |
| AUDI          | Global     | 3-5                           |
| BMW           | Global     | 5-10                          |
| BUICK         | US, Canada | 30-45                         |
| BYD           | Europe     | 1-3                           |
| CADILLAC      | US, Canada | 30-45                         |
| CHEVROLET     | US, Canada | 30-45                         |
| CHRYSLER      | Global     | 5-10                          |
| CITROEN       | Europe     | 5-10                          |
| CUPRA         | Europe     | 5-10                          |
| DACIA         | Europe     | 30-60                         |
| DODGE         | Global     | 5-10                          |
| DS            | Europe     | 5-10                          |
| FIAT          | Global     | 5-10                          |
| FORD          | Global     | 5-10                          |
| GMC           | US, Canada | 30-45                         |
| HONDA         | US, Canada | 15-30                         |
| HYUNDAI       | Global     | 5                             |
| INFINITI      | US         | 5-10                          |
| JAGUAR        | Global     | 15-30                         |
| JEEP          | Global     | 5-10                          |
| KIA           | Global     | 5                             |
| LAND ROVER    | Global     | 15-30                         |
| LEXUS         | US         | 5-10                          |
| LINCOLN       | Global     | 5-10                          |
| MAZDA         | Global     | 5-10                          |
| MERCEDES BENZ | Global     | 5-10                          |
| MG            | Europe     | 30-60                         |
| MINI          | Global     | 30-60                         |
| NISSAN        | Europe     | 5-10                          |
| NISSAN        | US         | 5-10                          |
| OPEL          | Europe     | 5-10                          |
| PEUGEOT       | Europe     | 5-10                          |
| POLESTAR      | Global     | 1-3                           |
| PORSCHE       | Europe     | 30-60                         |
| RAM           | Global     | 5-10                          |
| RENAULT       | Europe     | 30-60                         |
| RIVIAN        | Global     | 3-5                           |
| SKODA         | Europe     | 5                             |
| SUBARU        | US         | 5-10                          |
| TESLA\*       | Global     | 1 sec - 5 min                 |
| TOYOTA        | US         | 30-60                         |
| VAUXHALL      | Europe     | 5-10                          |
| VOLKSWAGEN    | Europe     | 5-10                          |
| VOLKSWAGEN\*  | US         | 1-3                           |
| VOLVO         | Global     | 1-3                           |

## Notes

### \* Tesla

<Info>
  For Tesla vehicles capable of streaming, 3 minutes is the average of how often the data is refreshed. Depending on the data point and how often it changes, you may see data refreshed faster. For vehicles that do not support streaming, Smartcar fetches data from the vehicle every 5 minutes when the vehicle is awake.
</Info>

### \* Volkswagen US

<Info>
  For Volkswagen vehicles in the US, 3 minutes is the average of how often the data is refreshed. For EVs, you may see data refreshed faster when the vehicle is plugged in.
</Info>

{/*| -----------------------| */}

{/*| -                      | */}

{/*| 3 (US/CA/EUR)          | */}

{/*| 1 (US), 1 (CA)         | */}

{/*| 3 (US), 3 (CA)         | */}

{/*| 3 (EUR)                | */}

{/*| 3 (US), 3 (CA)         | */}

{/*| -                      | */}

{/*| 1 (CA)                 | */}

{/*| 1 (CA)                 | */}

{/*| 1 (US/CA/EUR)          | */}

{/*| 1 (US), 1 (CA), 3 (EUR)| */}

{/*| 1 (US), 2 (CA)         | */}

{/*| 3 (US/CA/EUR)          | */}

{/*| -                      | */}

{/*| 1 (EUR)                | */}

{/*| 3 (EUR)                | */}

{/*| 1 (US/EUR)             | */}

{/*| 1 (EUR)                | */}

{/*| 1 (EUR)                | */}

{/*| 1 (US/CA), 2 (EUR)     | */}

{/*| 1 (EUR)                | */}

{/*| 3 (US)                 | */}
