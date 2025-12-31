# Source: https://learn.sparkfun.com/tutorials/geofence-treasure-hunt-with-artemis-global-tracker

## The Story

The Artemis Global Tracker is a highly functional sensor device with professional grade pressure, humidity, and temperature sensing with the onboard TE MS8607 PHT sensor, and location data through the onboard u-blox ZOE-M8Q GNSS receiver. It can also be programmed with the Arduino IDE through the Artemis processor and transfer information through the Iridium Satellite Network due to the Iridium 9603N Short Burst Data modem. The goal of this project is to demonstrate the ease of working with this device, and the accuracy and potential of its onboard sensors, specifically the GNSS receiver.

This project will use the Artemis Global Tracker (AGT) to create a "Treasure Game" in which the player begins the game, the AGT will randomly select a position in a 20 meter radius (designated the "treasure spot"), and the onboard LED will blink faster as the player moves toward the "treasure spot" - winning when they find it exactly. In this way, the onboard LED will lead the player to the "treasure spot". This game will also transfer location information to a computer using the Iridium Satellite Network, meaning it could be played even where no WIFI or wireless data is accessible.

## The Components

 

 

NOTE: To connect to the Iridium Satellite Network requires a monthly fee of \$17 and a purchase of credits, however, you can pick and choose the periods to access the network.

\

![](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/0/8/image2.png)

\

## The Setup

The first step in the development setup is the software setup. If you have not programmed with the Arduino IDE before, SparkFun made a great introductory guide to setup with the Artemis module which can be [found here](https://learn.sparkfun.com/tutorials/artemis-development-with-the-arduino-ide). It notes the need to add the Artemis module within the Arduino IDE boards manager using the following link:

    https://raw.githubusercontent.com/sparkfun/Arduino_Apollo3/main/package_sparkfun_apollo3_index.json

You will also need to add the following libraries to the Arduino IDE: SparkFun u-blox GNSS Arduino Library, IridiumSBDi2c. If you want to make use of the PHT sensor, you will also need the SparkFun PHT MS8607 Arduino Library. These can all be found within the Arduino Library Manager.

To begin development, you will need to connect the Artemis Global Tracker to your device with the Arduino IDE using the USB-C cable, and select the designated board (RedBoard Artemis ATP).

## The Logic

The code enables the GNSS module funcitonality, finds the current longitude and latitude of the AGT device, randomly generates a target distance and angle based on the current location, and begins blinking the onboard LED with intervals relating to the distance between the current location and target location. We will also mark the location of a 30 meter radius around the starting location using the "addGeofence" function from the SparkFun u-blox GNSS Arduino Library. If the device leaves this radius while playing the game, the player will lose. The treasure position is chosen by randomly selecting a distance between 15 and 30 meters and a distance between 0 and 360 degrees from the starting position.

The magic here involves calculating distances and angles with spherical coordinates. The game should be playable on a large (potentially worldly) scale, which means no assuming the Earth is flat. Therefore, from two sets of spherical coordinates (the initial and current position of the AGT device), we need to compute the effective spherical angle and distance between them. Through research, making use of the haversine and bearing equations, where the haversine function calculates the distance between the two positions and the bearing function calculates the angle, seemed like the best approach. They work as follows:

#### Haversine Distance Function

\

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/0/8/image5.png)

\

``` c
// GET COORDINATE DISTANCE - HAVERSINE FORMULA

double getCoordinateDistance(long La1, long Lo1, double La2, long Lo2) 

 } else 

   // Print the Geofencing status
   // 0 - Geofencing not available or not reliable; 1 - Geofencing active
   Serial.print(F(". status is: "));
   Serial.print(currentGeofenceState.status);

   // Print the numFences
   Serial.print(F(". numFences is: "));
   Serial.print(currentGeofenceState.numFences);

   // Print the state of the geofence
   // 0 - Unknown; 1 - Inside; 2 - Outside
   Serial.print(F(". The geofence stats is: "));
   Serial.print(currentGeofenceState.states[0]);

   byte fenceStatus = digitalRead(geofencePin); // Read the geofence pin
   digitalWrite(LED, !fenceStatus); // Set the LED (inverted)
   Serial.print(F(". Geofence pin (PIO14) is: ")); // Print the pin state
   Serial.print(fenceStatus);
   Serial.println(F("."));

   // GET CURRENT POSITION
   curr_lat = myGNSS.getLatitude(); // Get the latitude in degrees * 10^-7
   curr_long = myGNSS.getLongitude(); // Get the longitude in degrees * 10^-7
   curr_angle = (getCoordinateBearing(latitude, longitude, curr_lat, curr_long) + 180) % 360;
   curr_distance = getCoordinateDistance(latitude, longitude, curr_lat, curr_long);

   Serial.print(F("Current Latitude: "));
   Serial.print(curr_lat);
   Serial.print(F(". Current Longitude: "));
   Serial.println(curr_long);

   Serial.print(F("Goal Angle: "));
   Serial.print(goal_angle);
   Serial.print(F(". Goal Distance: "));
   Serial.println(goal_distance);

   Serial.print(F("Current Angle: "));
   Serial.print(curr_angle);
   Serial.print(F(". Current Distance: "));
   Serial.println(curr_distance);

   score = sqrt(curr_distance * curr_distance + goal_distance * goal_distance - 2 * goal_distance * curr_distance * cos((curr_angle * (2*PI/360)) - (goal_angle * (2*PI/360))));
   Serial.print(F("Current Score: "));
   Serial.print(score);

   if (score < 2)  if (score < 5)  else if (score < 12)  else if (score < 20)  else 
   Serial.println();

 }

 digitalWrite(LED, LOW);
 delay(score*5);
 digitalWrite(LED, HIGH);
 delay(score*5);
}
```

Once the player finds the treasure, the victory function runs, which connects the AGT to the Iridium network and sends a victory message.

``` c
void signalVictory() 
  Serial.println(F("Supercapacitors charged!"));

  // Enable power for the 9603N (Iridium Connection)
  Serial.println(F("Enabling 9603N power..."));
  digitalWrite(iridiumPwrEN, HIGH); // Enable Iridium Power
  delay(1000);
  modem.setPowerProfile(IridiumSBD::USB_POWER_PROFILE);

  // Startup the modem
  Serial.println(F("Starting modem..."));
  err = modem.begin();
  if (err != ISBD_SUCCESS)
  

  // Test the signal quality.
  err = modem.getSignalQuality(signalQuality);
  if (err != ISBD_SUCCESS)
  
  modem.useMSSTMWorkaround(false);

  Serial.print(F("On a scale of 0 to 5, signal quality is currently "));
  Serial.print(signalQuality);
  Serial.println(F("."));

  // Send the message
  Serial.println(F("Trying to send the message.  This might take several minutes."));
  err = modem.sendSBDText("YOU FOUND THE TREASURE!!");
  if (err != ISBD_SUCCESS)
  

  // POWER DOWN IRIDIUM CONNECTION

  // Clear the Mobile Originated message buffer
  Serial.println(F("Clearing the MO buffer."));
  err = modem.clearBuffers(ISBD_CLEAR_MO); // Clear MO buffer
  if (err != ISBD_SUCCESS)
  

  // Power down the modem
  Serial.println(F("Putting the 9603N to sleep."));
  err = modem.sleep();
  if (err != ISBD_SUCCESS)
  

  Serial.println(F("Disabling 9603N power..."));
  digitalWrite(iridiumPwrEN, LOW); // Disable Iridium Power

  Serial.println(F("Disabling the supercapacitor charger..."));
  digitalWrite(superCapChgEN, LOW); // Disable the super capacitor charger

  Serial.println(F("Game Complete!"));
}
```

## Next Steps

All of these components together creates a fun hide and seek game with your Artemis Global Tracker! There are many ways one could extend this example and create a higher functioning game. For one, you could create a website designed to take a POST request after a player wins the game and show stats from the game (ex: time until find, score, etc.). Also, you could add hardware components along with the AGT to graphically show game stats for the user while playing. For example, an LED meter would be a great way to show live score updates to the player.