# Appendix A Example ATT Server contents

Table A.1 shows an example ATT Server and the attributes contained on the server.

## Note

Note: This example does not necessarily use UUIDs or services defined by the Bluetooth SIG or in adopted profiles.

Handle

Attribute Type

Attribute Value

0x0001

«Primary Service»

«GAP Service»

0x0004

«Characteristic»

{0x02, 0x0006, «Device Name»}

0x0006

«Device Name»

"Example Device"

0x0010

«Primary Service»

«GATT Service»

0x0011

«Characteristic»

{0x26, 0x0012, «Service Changed»}

0x0012

«Service Changed»

0x0000, 0x0000

0x0100

«Primary Service»

«Battery State Service»

0x0106

«Characteristic»

{0x02, 0x0110, «Battery State»}

0x0110

«Battery State»

0x04

0x0200

«Primary Service»

«Thermometer Humidity Service»

0x0201

«Include»

{0x0500, 0x0504, «Manufacturer Service»}

0x0202

«Include»

{0x0550,0x0568}

0x0203

«Characteristic»

{0x02, 0x0204, «Temperature»}

0x0204

«Temperature»

0x028A

0x0205

«Characteristic Presentation Format»

{0x0E, 0xFE, «degrees Celsius», 0x01,

«Outside»}

0x0206

«Characteristic User Description»

"Outside Temperature"

0x0210

«Characteristic»

{0x02, 0x0212, «Relative Humidity»}

0x0212

«Relative Humidity»

0x27

0x0213

«Characteristic Presentation Format»

{0x04, 0x00, «Percent», «Bluetooth SIG», «Outside»}

0x0214

«Characteristic User Description»

"Outside Relative Humidity"

0x0280

«Primary Service»

«Weight Service»

0x0281

«Include»

0x0505, 0x0509, «Manufacturer Service»}

0x0282

«Characteristic»

{0x02, 0x0283, «Weight kg»}

0x0283

«Weight kg»

0x00005582

0x0284

«Characteristic Presentation Format»

{0x08, 0xFD, «kilogram», «Bluetooth SIG», «Hanging»}

0x0285

«Characteristic User Description»

"Rucksack Weight"

0x0300

«Primary Service»

«Position Service»

0x0301

«Characteristic»

{0x02, 0x0302, «Latitude Longitude»}

0x0302

«Latitude Longitude»

0x28BEAFA40B320FCE

0x0304

«Characteristic»

{0x02, 0x0305, «Latitude Longitude Elevation»}

0x0305

«Latitude Longitude Elevation»

0x28BEAFA40B320FCE0176

0x0400

«Primary Service»

«Alert Service»

0x0401

«Characteristic»

{0x0E, 0x0402, «Alert Enumeration»}

0x0402

«Alert Enumeration»

0x00

0x0500

«Secondary Service»

«Manufacturer Service»

0x0501

«Characteristic»

{0x02, 0x0502, «Manufacturer Name»}

0x0502

«Manufacturer Name»

"ACME Temperature Sensor"

0x0503

«Characteristic»

{0x02, 0x0504, «Serial Number»}

0x0504

«Serial Number»

"237495-3282-A"

0x0505

«Secondary Service»

«Manufacturer Service»

0x0506

«Characteristic»

{0x02, 0x0507, «Manufacturer Name»}

0x0507

«Manufacturer Name»

"ACME Weighing Scales"

0x0508

«Characteristic»

{0x02, 0x0509, «Serial Number»}

0x0509

«Serial Number»

"11267-2327A00239"

0x0550

«Secondary Service»

«Vendor Specific Service»

0x0560

«Characteristic»

{0x02, 0x0568, «Vendor Specific Type»}

0x0568

«Vendor Specific Type»

0x56656E646F72
Table A.1: Examples of ATT Server contents

As can be seen, the ATT Server indicates support for ten services: GAP Service, GATT Service, Battery State Service, Thermometer Humidity Service, Weight Service, Position Service, Alert Service, two Manufacturer Services, and a Vendor Specific Service.

The server contains the following information about each of the services:

- The characteristic containing the name of the device is "Example Device".

- The characteristic indicating the server supports all the attribute opcodes, and supports two prepared write values.

- The characteristic containing the battery state with a value of 0x04, meaning it is discharging.

- The characteristic containing the outside temperature with a value of 6.5 °C.

- The characteristic containing the outside relative humidity with a value of 39%.

- The characteristic containing the weight hanging off the device with a value of 21.89 kg.

- The characteristic containing the position of this device with the value of 68.3585444 degrees north, 18.7830222 degrees east, with an elevation of 374 meters.

- The characteristic containing the temperature sensor manufacturer with the value of ACME Temperature Sensor.

- The characteristic containing the serial number for the temperature sensor with a value of 237495-3282-A.

- The characteristic containing the weighing sensor is manufacturer with a value of ACME Weight Scales.

- The characteristic containing the serial number for the weighing sensor with a value of 11267-2327A00239.

The device is therefore on the side of the Abisko Turiststation, Norrbottens Län, Sweden, with a battery in good state, measuring a relatively warm day, with low humidity, and a heavy rucksack.
