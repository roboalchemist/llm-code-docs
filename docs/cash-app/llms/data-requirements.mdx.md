# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/introduction/data-requirements.mdx

***

## stoplight-id: puuszshkzbjen

# Data requirements for select verticals

Depending on the goods and services you provide to customers, you may need to provide additional data in your Create Checkout payloads. If required, add this data to the optional `custom` object within the Create Checkout request payload. See data requirements below.

<Note>
  These merchant category flags are intended to provide a general understanding of the requirements across various verticals, though they may not cover all scenarios. Please note while your business may align with these verticals, all merchants must be reviewed and approved through Block's standard onboarding process. Your Delivery Manager will guide you through the specific flags needed for your integration. Block reserves the right to update merchant category requirements as needed.
</Note>

### Consumer electronics

This data is required to be present for each Item object; it will appear in the checkout's `items` array.

| Attribute             | Data Type                 | Description                                                   |
| --------------------- | ------------------------- | ------------------------------------------------------------- |
| name                  | string                    | The name of the item                                          |
| sku                   | string                    | The SKU of the item                                           |
| quantity              | integer                   | The quantity of the item ordered                              |
| pageUrl               | string                    | The URL of the item on your store’s website                   |
| imageUrl              | string                    | The URL of the item’s image on your store’s website           |
| price                 | object                    | The price of the item, containing the amount and the currency |
| categories            | array of array of strings | The category or categories that the item belongs to           |
| estimatedShipmentDate | string                    | The estimated ship date for the item                          |

**Payload structure:**

```json
"items": [
  {
    "name": "Waterproof Bluetooth Speaker",
    "sku": "12341234",
    "quantity": 1,
    "pageUrl": "https://merchant.example.com/bluetoothspeaker-354193.html",
    "imageUrl": "https://merchant.example.com/bluetoothspeaker-7378-391453-1.jpg",
    "price": {
      "amount": "100.00",
      "currency": "USD"
    },
    "categories": [
      [
        "Bluetooth",
        "Speaker",
        "Portables"]
        "Rechargeable"
      ]
      [
        "Sale",
        "Portable Speakers"
      ]
    ],
	  "estimatedShipmentDate": "2025-08-01"
  }
 ],

}
```

### Digital goods (software, applications)

| Attribute       | Data Type | Description                                                                   |
| --------------- | --------- | ----------------------------------------------------------------------------- |
| productType     | string    | The type of product.                                                          |
| productCategory | string    | The category of the product.                                                  |
| subSellerId     | string    | The ID of the sub-seller, if applicable.                                      |
| subSellerName   | string    | The name of the sub-seller of this product, if applicable.                    |
| recipientEmail  | string    | The email address of the consumer who is receiving the product.               |
| purchaseType    | string    | Whether this was a subscription or one-time purchase.                         |
| consumerTenure  | string    | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
 "productType": "Software",
 "productCategory": "Software License",
 "subSellerId": "abc123",
 "subSellerName":"Userabc123",
 "recipientEmail": "johnsmith@email.com",
 "purchaseType": "subscription",
 "consumerTenure": "membership level 1"
}
```

### Education services and courses

| Attribute      | Data Type         | Description                                                                   |
| -------------- | ----------------- | ----------------------------------------------------------------------------- |
| educationType  | string            | The type of educational service or course (e.g., course, workshop, tutoring). |
| startDate      | string (datetime) | The start date and time of the service or course.                             |
| endDate        | string (datetime) | The end date and time of the service or course.                               |
| eventLocation  | string            | Whether the service/course is online or offline.                              |
| purchaseType   | string            | Indicates whether it is a subscription-based or one-time purchase.            |
| consumerTenure | string            | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
 "educationType": "course",
 "startDate":"2022-07-10 15:00:00.000",
 "endDate":"2022-07-10 15:00:00.000",
 "eventLocation":"online",
 "purchaseType": "one-time-purchase",
 "consumerTenure": "membership level 1"
}
```

### Experience and ticket sales/events

| Attribute      | Data Type         | Description                                                                   |
| -------------- | ----------------- | ----------------------------------------------------------------------------- |
| eventName      | string            | The name of the event.                                                        |
| ticketQuantity | integer           | The number of tickets purchased.                                              |
| ticketPrice    | string            | The price of a single ticket.                                                 |
| eventDate      | string (datetime) | The date and time of the event, in timestamp format.                          |
| eventCity      | string            | The city where the event is taking place.                                     |
| eventState     | string            | The state where the event is taking place.                                    |
| eventCountry   | string            | The country where the event is taking place.                                  |
| subSellerId    | string            | The ID of the sub-seller, if applicable.                                      |
| subSellerName  | string            | The name of the sub-seller, if applicable.                                    |
| eventId        | string            | The unique identifier for the event, if applicable.                           |
| purchaseType   | string            | Whether this was a subscription or one-time purchase.                         |
| consumerTenure | string            | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
 "eventName": "Glastonbury Festival",
 "ticketQuantity": "2",
 "ticketPrice": "400.00",
 "eventDate":"2022-07-10 15:00:00.000",
 "eventCity": "Los Angeles",
 "eventState": "California",
 "eventCountry": "US",
 "subSellerId": "abc123",
 "subSellerName":"Userabc123",
 "eventId":"1234567",
 "purchaseType": "one-time-purchase",
 "consumerTenure": "membership level 1"
}
```

### Marketplaces

| Attribute      | Data Type | Description                                                                   |
| -------------- | --------- | ----------------------------------------------------------------------------- |
| subSellerId    | string    | The ID of the sub-seller.                                                     |
| subSellerName  | string    | The name of the sub-seller.                                                   |
| consumerTenure | string    | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
 "subSellerId": "abc123",
 "subSellerName":"Userabc123",
 "consumerTenure": "membership level 1"
}
```

### Musical instruments

| Attribute      | Data Type | Description                                                                   |
| -------------- | --------- | ----------------------------------------------------------------------------- |
| condition      | string    | The condition of the instrument (e.g., new, used, second-hand).               |
| consumerTenure | string    | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
  "condition": "used",
  "consumerTenure": "membership level 1"
}
```

### Services

| Attribute      | Data Type         | Description                                                                   |
| -------------- | ----------------- | ----------------------------------------------------------------------------- |
| serviceType    | string            | The type of service provided (e.g., spa, cleaning, consulting).               |
| startDate      | string (datetime) | The start date and time of the service.                                       |
| endDate        | string (datetime) | The end date and time of the service.                                         |
| eventCity      | string            | The city where the service is provided.                                       |
| eventState     | string            | The state where the service is provided.                                      |
| eventCountry   | string            | The country where the service is provided.                                    |
| consumerTenure | string            | Indicates whether the consumer is new or existing, or their membership level. |

**Payload structure:**

```json
"custom": {
 "serviceType": "spa",
 "startDate":"2022-07-10 15:00:00.000",
 "endDate":"2022-07-10 15:00:00.000",
 "eventCity": "Los Angeles",
 "eventState": "California",
 "eventCountry": "US",
 "consumerTenure": "membership level 1"
}
```

### Travel

| Attribute      | Data Type | Description                                                                   |
| -------------- | --------- | ----------------------------------------------------------------------------- |
| consumerTenure | string    | Indicates whether the consumer is new or existing, or their membership level. |
| travel.type    | string    | Type of travel (e.g., flight, hotel, car rental, transportation, etc.).       |

<Note>
  All travel transactions must use the `consumerTenure` and `travel.type` attributes. For type-specific attributes, see the tables below.
</Note>

#### Flight details

| Attribute            | Data Type         | Description                                        |
| -------------------- | ----------------- | -------------------------------------------------- |
| flight.departureDate | string (datetime) | The date and time of the flight's departure.       |
| flight.arrivalDate   | string (datetime) | The date and time of the flight's arrival.         |
| flight.departureCity | string            | The city the flight departs from.                  |
| flight.arrivalCity   | string            | The city the flight arrives at.                    |
| flight.airline       | string            | The name of the airline.                           |
| flight.class         | string            | The flight class (e.g., economy, business, first). |
| flight.passengers    | integer           | The number of passengers on the flight.            |

#### Hotel details

| Attribute           | Data Type         | Description                               |
| ------------------- | ----------------- | ----------------------------------------- |
| hotel.checkInDate   | string (datetime) | The check-in date and time at the hotel.  |
| hotel.checkOutDate  | string (datetime) | The check-out date and time at the hotel. |
| hotel.hotelCity     | string            | The city where the hotel is located.      |
| hotel.hotelName     | string            | The name of the hotel.                    |
| hotel.hotelRating   | integer           | The star rating/class of the hotel.       |
| hotel.numberOfRooms | integer           | The number of rooms booked at the hotel.  |

#### Car rental details

| Attribute                 | Data Type         | Description                                            |
| ------------------------- | ----------------- | ------------------------------------------------------ |
| carRental.pickUpDate      | string (datetime) | The date and time for picking up the rental car.       |
| carRental.dropOffDate     | string (datetime) | The date and time for dropping off the rental car.     |
| carRental.pickUpLocation  | string            | The location for picking up the rental car.            |
| carRental.dropOffLocation | string            | The location for dropping off the rental car.          |
| carRental.make            | string            | The make of the rental car (e.g., Ford).               |
| carRental.model           | string            | The model of the rental car (e.g., Fiesta).            |
| carRental.namedDriver     | string            | The name of the driver responsible for the rental car. |

#### Bus/transportation details

| Attribute         | Data Type         | Description                              |
| ----------------- | ----------------- | ---------------------------------------- |
| bus.departureDate | string (datetime) | The departure date and time for the bus. |
| bus.arrivalDate   | string (datetime) | The arrival date and time for the bus.   |
| bus.departureCity | string            | The city the bus departs from.           |
| bus.arrivalCity   | string            | The city the bus arrives at.             |
| bus.busName       | string            | The name of the bus service.             |
| bus.passengers    | integer           | The number of passengers on the bus.     |

**Payload structure:**

```json
"custom": {
  "consumer tenure": "membership level 1", 
  "travel": {
      "type":"flight",
      "flight":{
        "departureDate":"2022-07-10 15:00:00.000",
        "arrivalDate":"2022-07-17 20:00:00.000",
        "departureCity": "New York",
        "arrivalCity": "London",
        "airline": "British Airways",
        "class": "economy",
        "passengers": "2"
      },
      "hotel":{
       "checkInDate": "2022-07-10 15:00:00.000",
       "checkOutDate": "2022-07-10 15:00:00.000",
       "hotelCity": "London", 
       "hotelName": "The Grand",
       "hotelRating": "3",
       "numberOfRooms": "2",
      },
     "carRental":{
       "pickUpDate":"2022-07-10 15:00:00.000",
       "dropOffDate":"2022-07-17 20:00:00.000",
       "pickUpLocation": "M4 6JD",
       "dropOffLocation": "M4 6JD",
       "make":"Ford",
       "model":"Fiesta",
       "namedDriver": "John Smith"
      },
      "bus":{
        "departureDate":"2022-07-10 15:00:00.000",
        "arrivalDate":"2022-07-11 20:00:00.000",
        "departureCity": "Los Angeles",
        "arrivalCity": "San Francisco",
        "busName": "California Charter",
        "passengers": "12"
      }
    }
}
```
