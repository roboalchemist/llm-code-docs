# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/regions-and-localization.mdx

***

## stoplight-id: debafcd6ec2e9

# Regions and Localization

## What are regions used for

The Cash App Pay API requires regions in requests to:

* Improve availability by allowing Cash App Pay to run in multiple, independent regions simultaneously without sacrificing consistency
* Reduce latencies by storing data closer to the geographic location of the API client
* Comply with data sovereignty regulations
* Support strongly consistent, idempotent processing of requests in independent regions; see [Idempotency](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/idempotency) for more details

## How do I know which region to use?"

The region you pick should be the one closest to where your own services are hosted. For example, if you are hosting your services in the [AWS US West (Oregon) region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) (also known as `us-west-2`), you would want to pick `PDX` as the region code, since Portland is the closest city to Oregon.

> **Data sovereignty laws overrule physical proximity:** If you are serving customers in a country with strict data sovereignty laws, you must pass a region code that is associated with a city within that country. This allows Cash App Pay to comply with data sovereignty regulations before any data is associated with a customer, which is important for privacy laws.",

## How do I set the region on a request

Set the `X-Region` header to one of the supported values to set the region for the request.

**X-Region Header**

```
X-Region: PDX
```

## Supported region / IATA airport codes

The following table contains the list of all region / IATA airport codes that will be accepted by the Cash App Pay API in the `X-Region` header. Other codes will be rejected with an `INVALID REGION` error (See  [General Validation Errors](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#general-validation-errors) `INVALID REGION` error code)

| Code | City                                       |
| ---- | ------------------------------------------ |
| ABJ  | Abidjan, Ivory Coast                       |
| ABQ  | Albuquerque, United States                 |
| ACC  | Accra, Ghana                               |
| ACE  | Arrecife, Spain                            |
| ADB  | Izmir, Turkey                              |
| ADD  | Addis Ababa, Ethiopia                      |
| ADL  | Adelaide, Australia                        |
| AEP  | Buenos Aires, Argentina                    |
| AER  | Sochi, Russia                              |
| AGP  | Malaga, Spain                              |
| AIT  | Aitutaki, Cook Islands                     |
| AKL  | Auckland, New Zealand                      |
| ALC  | Alicante, Spain                            |
| ALG  | Algiers, Algeria                           |
| AMD  | Ahmedabad, India                           |
| AMS  | Amsterdam, Netherlands                     |
| ANC  | Anchorage, United States                   |
| APW  | Faleolo, Samoa                             |
| ARN  | Stockholm, Sweden                          |
| ASU  | Asuncion, Paraguay                         |
| ATH  | Athens, Greece                             |
| ATL  | Atlanta, United States                     |
| AUH  | Abu Dhabi, United Arab Emirates            |
| AUS  | Austin, United States                      |
| AYT  | Antalya, Turkey                            |
| BCN  | Barcelona, Spain                           |
| BDL  | Windsor Locks, United States               |
| BEG  | Belgrade, Serbia                           |
| BGO  | Bergen, Norway                             |
| BGY  | Bergamo, Italy                             |
| BHX  | Birmingham, United Kingdom                 |
| BKI  | Kota Kinabalu, Malaysia                    |
| BKK  | Bangkok, Thailand                          |
| BLQ  | Bologna, Italy                             |
| BLR  | Bangalore, India                           |
| BNA  | Nashville, United States                   |
| BNE  | Brisbane, Australia                        |
| BOD  | Bordeaux, France                           |
| BOG  | Bogota, Colombia                           |
| BOM  | Mumbai, India                              |
| BOS  | Boston, United States                      |
| BPN  | Balkipapan, Indonesia                      |
| BRS  | Bristol, United Kingdom                    |
| BRU  | Brussels, Belgium                          |
| BSB  | Brasilia, Brazil                           |
| BSL  | Mulhouse, France                           |
| BTH  | Batam, Indonesia                           |
| BUD  | Budapest, Hungary                          |
| BUS  | Batumi, Georgia                            |
| BWI  | Baltimore, United States                   |
| BZE  | Belize City, Belize                        |
| CAI  | Cairo, Egypt                               |
| CAN  | Guangzhou, China                           |
| CBR  | Canberra, Australia                        |
| CCU  | Kolkata, India                             |
| CDG  | Paris, France                              |
| CEB  | Cebu, Phillippines                         |
| CGK  | Jakarta, Indonesia                         |
| CGN  | Cologne, Germany                           |
| CGO  | Zhengzhou, China                           |
| CGQ  | Changchun, China                           |
| CHC  | Christchurch, New Zealand                  |
| CJU  | Cheju, South Korea                         |
| CKG  | Chongqing, China                           |
| CLE  | Cleveland, United States                   |
| CLT  | Charlotte, United States                   |
| CMH  | Colombus, United States                    |
| CMN  | Casablanca, Morocco                        |
| CNF  | Belo Horizonte, Brazil                     |
| CNS  | Cairns, Australia                          |
| CNX  | Chiang Mai, Thailand                       |
| COK  | Kochi, India                               |
| COO  | Cotonou, Benin                             |
| CPH  | Copenhagen, Denmark                        |
| CPT  | Cape Town, South Africa                    |
| CRL  | Charleroi, Belgium                         |
| CSX  | Changcha, China                            |
| CTA  | Catania, Italy                             |
| CTS  | Sapporo, Japan                             |
| CTU  | Chengdu, China                             |
| CUN  | Cancun, Mexico                             |
| CVG  | Cincinnati, United States                  |
| CWB  | Curitiba, Brazil                           |
| DAD  | Danang, Vietnam                            |
| DAR  | Dar Es Salaam, Tanzania                    |
| DEL  | Delhi, India                               |
| DEN  | Denver, United States                      |
| DFW  | Dallas, United States                      |
| DKR  | Dakar, Senegal                             |
| DLA  | Doulala, Cameroon                          |
| DLC  | Dalian, China                              |
| DOH  | Doha, Qatar                                |
| DPS  | Denpasar, Indonesia                        |
| DTW  | Detroit, United States                     |
| DUB  | Dublin, Ireland                            |
| DUS  | Dusseldorf, Germany                        |
| DXB  | Dubai, United Arab Emirates                |
| EBB  | Entebbe, Uganda                            |
| ECN  | Nicosia, Cyprus                            |
| EDI  | Edinburgh, United Kingdom                  |
| ESB  | Ankara, Turkey                             |
| FAO  | Faro, Portugal                             |
| FCO  | Rome, Italy                                |
| FIH  | Kinshasa, Democratic Republic of the Congo |
| FOC  | Fuzhou, China                              |
| FRA  | Frankfurt, Germany                         |
| FUE  | Fuerteventura, Spain                       |
| FUK  | Fukuoka, Japan                             |
| GDL  | Guadalajara, Mexico                        |
| GIG  | Rio de Janeiro, Brazil                     |
| GLA  | Glasgow, United Kingdom                    |
| GOA  | Goa, India                                 |
| GOT  | Gothenborg, Sweden                         |
| GRU  | São Paulo, Brazil                          |
| GUA  | Guatemala City, Guatemala                  |
| GVA  | Geneva, Switzerland                        |
| HAK  | Haikou, China                              |
| HAM  | Hamburg, Germany                           |
| HAN  | Hanoi, Vietnam                             |
| HAV  | Havana, Cuba                               |
| HEL  | Helsinki, Finland                          |
| HER  | Heraklion, Greece                          |
| HET  | Hohhot, China                              |
| HFE  | Hefei, China                               |
| HGH  | Hangzhou, China                            |
| HKG  | Hong Kong, China                           |
| HKT  | Phuket, Thailand                           |
| HND  | Tokyo, Japan                               |
| HNL  | Honolulu, United States                    |
| HOU  | Houston, United States                     |
| HRB  | Harbin, China                              |
| HRE  | Harare, Zimbabwe                           |
| HYD  | Hyderabad, India                           |
| IAD  | Washington D.C., United States             |
| IAH  | Houston, United States                     |
| IBZ  | Ibiza, Spain                               |
| ICN  | Seoul, Korea                               |
| INC  | Yinchuan, China                            |
| IND  | Indianapolis, United States                |
| IST  | Istanbul, Turkey                           |
| JED  | Jeddah, Saudi Arabia                       |
| JFK  | New York, United States                    |
| JJN  | Quanzhou, China                            |
| JNB  | Johannesburg, South Africa                 |
| JOG  | Yogyakarta, Indonesia                      |
| KBP  | Kiev, Ukraine                              |
| KEF  | Keflavik, Iceland                          |
| KHH  | Kaohsiung, Taiwan                          |
| KHN  | Nanchang, China                            |
| KIX  | Osaka, Japan                               |
| KMG  | Kunming, China                             |
| KNO  | Medan, Indonesia                           |
| KRT  | Khartoum, Sudan                            |
| KUL  | Kuala Lumpur, Malaysia                     |
| KWE  | Guiyang, China                             |
| KWL  | Guilin, China                              |
| LAD  | Luanda, Angola                             |
| LAS  | Las Vegas, United States                   |
| LAX  | Los Angeles, United States                 |
| LED  | St. Petersburg, Russia                     |
| LHR  | London, United Kingdom                     |
| LHW  | Lanzhou, China                             |
| LIM  | Lima, Peru                                 |
| LIN  | Milano, Italy                              |
| LIS  | Lisbon, Portugal                           |
| LJG  | Lijiang, China                             |
| LOS  | Lagos, Nigeria                             |
| LPA  | Gran Canaria, Spain                        |
| LUX  | Luxembourg, Luxembourg                     |
| LYS  | Lyon, France                               |
| MAA  | Chennai, India                             |
| MAD  | Madrid, Spain                              |
| MAN  | Manchester, United Kingdom                 |
| MCI  | Kansas City, United States                 |
| MCO  | Orlando, United States                     |
| MED  | Madinah, Saudi Arabia                      |
| MEL  | Melbourne, Australia                       |
| MEX  | Mexico City, Mexico                        |
| MGA  | Managua, Nicaragua                         |
| MHD  | Mashhad, Iran                              |
| MIA  | Miami, United States                       |
| MLA  | Malta, Malta                               |
| MNL  | Manila, Philippines                        |
| MRS  | Marseille, France                          |
| MRU  | Plaisance, Mauritius                       |
| MSP  | Minneapolis, United States                 |
| MSQ  | Minsk, Belarus                             |
| MSY  | New Orleans, United States                 |
| MTY  | Monterrey, Mexico                          |
| MUC  | Munich, Germany                            |
| MUN  | Maturin, Venezuela                         |
| MXP  | Milano, Italy                              |
| NAN  | Nandi, Fiji                                |
| NAP  | Naples, Italy                              |
| NBO  | Nairobi, Kenya                             |
| NCE  | Nice, France                               |
| NGB  | Ninbo, China                               |
| NGO  | Nagoya, Japan                              |
| NIM  | Niamey, Niger                              |
| NKG  | Nanjing, China                             |
| NNG  | Nanning, China                             |
| OAK  | Oakland, United States                     |
| OKA  | Okinawa, Japan                             |
| OOL  | Coolangatta, Australia                     |
| OPO  | Porto, Portugal                            |
| ORD  | Chicago, United States                     |
| OSL  | Oslo, Norway                               |
| OTP  | Bucharest, Romania                         |
| OUA  | Ouagadougou, Burkina Faso                  |
| PDX  | Portland, United States                    |
| PEK  | Beijing, China                             |
| PEN  | Penang, Malaysia                           |
| PER  | Perth, Australia                           |
| PHL  | Philadelphia, United States                |
| PHX  | Phoenix, United States                     |
| PIT  | Pittsburgh, United States                  |
| PNQ  | Pune, India                                |
| POA  | Porto Alegre, Brazil                       |
| POM  | Port Moresby, Papua New Guinea             |
| PPG  | Pago Pago, American Samoa                  |
| PRG  | Prague, Czech Republic                     |
| PTY  | Panama City, Panama                        |
| PUS  | Busan, South Korea                         |
| PVG  | Shanghai, China                            |
| RDU  | Raleigh, United States                     |
| REC  | Recife, Brazil                             |
| RGN  | Yangon, Burma                              |
| RIX  | Riga, Latvia                               |
| RUH  | Riyadh, Saudi Arabia                       |
| RUR  | Rurutu, French Polynesia                   |
| SAL  | San Salvador, El Salvador                  |
| SAN  | San Diego, United States                   |
| SAP  | San Pedro Sula, Honduras                   |
| SAT  | San Antonio, United States                 |
| SCL  | Santiago, Chile                            |
| SEA  | Seattle, United States                     |
| SFO  | San Francisco, United States               |
| SGN  | Ho Chi Minh City, Vietnam                  |
| SHE  | Shenyang, China                            |
| SHU  | Sharjah, United Arab Emirates              |
| SID  | Amilcar Cabral, Cape Verde                 |
| SIN  | Singapore                                  |
| SJC  | San Jose, United States                    |
| SJJ  | Saajevo, Bosnia & Herzegovina              |
| SJO  | San Jose, Costa Rica                       |
| SJW  | Shijiazhuang, China                        |
| SKG  | Thessaloniki, Greece                       |
| SLC  | Salt Lake City, United States              |
| SMF  | Sacramento, United States                  |
| SNA  | Santa Ana, United States                   |
| SOF  | Sofia, Bulgaria                            |
| SSA  | Salvador, Brazil                           |
| STL  | St. Louis, United States                   |
| STR  | Stuttgart, Germany                         |
| SUB  | Surabaya, Indonesia                        |
| SVO  | Moscow, Russia                             |
| SYD  | Sydney, Australia                          |
| SYX  | Sanya, China                               |
| SZX  | Shenzhen, China                            |
| TAO  | Qingdao, China                             |
| TBU  | Tongatapu, Tonga                           |
| TFS  | Tenerife, Spain                            |
| THR  | Tehran, Iran                               |
| TIJ  | Tijuana, Mexico                            |
| TLS  | Toulouse, France                           |
| TLV  | Tel-Aviv, Israel                           |
| TNA  | Jinan, China                               |
| TNR  | Antananarivo, Madagascar                   |
| TPA  | Tampa, United States                       |
| TPE  | Taipei, Taiwan                             |
| TRW  | Tarawa, Kiribati                           |
| TSN  | Tianjin, China                             |
| TUN  | Tunis, Tunisia                             |
| TXL  | Berlin, Germany                            |
| TYN  | Taiyuan, China                             |
| UPG  | Ujung Pandang, Indonesia                   |
| URC  | Urumqi, China                              |
| VCE  | Venice, Italy                              |
| VCP  | Campinas, Brazil                           |
| VIE  | Vienna, Austria                            |
| VLC  | Valencia, Spain                            |
| WAW  | Warsaw, Poland                             |
| WLG  | Wellington, New Zealand                    |
| WLS  | Wallis, Wallis & Fortuna                   |
| WNZ  | Wenzhou, China                             |
| WUH  | Wuhan, China                               |
| WUX  | Wuxi, China                                |
| XIY  | Xi'an, China                               |
| XMN  | Xiamen, China                              |
| YEG  | Edmonton, Canada                           |
| YHZ  | Halifax, Canada                            |
| YNT  | Yantai, China                              |
| YOW  | Ottawa, Canada                             |
| YUL  | Montreal, Canada                           |
| YVR  | Vancouver, Canada                          |
| YWG  | Winnipeg, Canada                           |
| YYC  | Calgary, Canada                            |
| YYZ  | Toronto, Canada                            |
| ZAG  | Zagreb, Croatia                            |
| ZRH  | Zurich, Switzerland                        |
| ZUH  | Zhuhai, China                              |
