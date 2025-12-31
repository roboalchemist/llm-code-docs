# Source: https://learn.sparkfun.com/tutorials/alphanumeric-gps-wall-clock

## Introduction

The GPS Alphanumeric Clock is the clock you never have to set! Using UTC time and date we are able to parse out the local time using a Gregorian date calculator and some rules for US daylight savings time ([DST](http://en.wikipedia.org/wiki/Daylight_saving_time)). Calculating what day of the week it was on June 7th of 1983 is actually a bit of a challenge. Similarly, figuring out if we were or were not is DST for any given year was not as easy as you might think. This tutorial gives a good breakdown of how to calculate day of the week from any date and a simple way to make your clock set itself (assuming you know the date).

[![GPS wall clock](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_3.jpg)

### Suggested Reading

To better understand this project, you should be familiar with the following topics:

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

## Hardware

It's been awhile since we built the [12' GPS wall clock](https://www.sparkfun.com/tutorials/47). The GPS Alphanumeric Wall Clock is measurably smaller in size compared to the last one but a lot more sophisticated with its knowledge of local time.

[![Wiring of GPS clock](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_1.jpg)

This particular clock uses 6 of the [1" alphanumeric displays](https://www.sparkfun.com/products/9933) with [controllers](https://www.sparkfun.com/products/10103) to create a 6 character display. While not as glitzy as EMSL's awesome [Alpha Clock Five](http://shop.evilmadscientist.com/productsmenu/tinykitlist/589), this setup allows us really simple control from an Arduino to scroll time, date, day, and some simple messages. These are controlled with a [simple library](https://cdn.sparkfun.com/datasheets/Components/LED/AlphaNumeric_Driver.zip) using an Arduino Uno. A [5V walwart](https://www.sparkfun.com/products/12889) provides all the power for the displays and to power the Arduino. I originally used the [Locosys LS20031 GPS receiver](https://www.sparkfun.com/products/8975). This worked great for three years. Once my original DST code broke I decided to upgrade to the smaller, more sensitive [GP635T GPS receiver](https://www.sparkfun.com/products/11571).

If you\'d like to build your own, we reccomend this parts list to get started:

## Woes of Daylight Savings Time (DST)

The hardware was pretty straightforward; the trick was stitching the code together. I originally built this project back in February of 2011 and I hard-coded the DST dates:

    language:c
    if(year == 2011) 

If the year was 2011, and the date was between March 12th and November 6th then add an hour for daylight savings time. What about 2012? Well, I'll hard code those dates too (March 10, November 3). What about 2014? Forget 2014 - something will break before 2014 and I'll just fix it then...

So 2014 rolls around, and there's nothing more annoying than a clock on the wall that tells you the wrong time. This was my first lesson:

What you are building will last longer than you expect.

Perhaps it's just me and my projects, but I always assume they're going to break within a few days. When really, silicon and the code we load onto it will run for many tens of years in the right conditions; possibly longer than we will *be alive*.

Shoot. Where did I put that code? 2011 was before we started using [github](https://learn.sparkfun.com/tutorials/using-github-to-share-with-sparkfun) at SparkFun so I got to go digging through old hard drives. Yuck. Next lesson:

If a project doesn\'t have a publicly accessible repo it will break and no one will fix it.

I finally found the original code. I could have simply updated the hard coded values for the next 5-10 years, but what's the fun in that?

#### Daylight Savings Rules

The history of daylight savings sucked up a few hours of my time, but setting that aside, the US government changed the rules (thanks guys!) back in 2007. We now go from -7 UTC (here in Boulder, CO) to -6 UTC between the 2nd Sunday in March and returns to -7 UTC on the 1st Sunday in November. From the date, we know when we're in March or April, but how do we tell if we're after the 2nd Sunday? We need to know the day of the week!

#### A Tuesday Next Year

Marty in [Back To the Future](http://www.imdb.com/title/tt0088763/) went into the future to October 21, 2015. Holy smokes there's already a [countdown website](http://www.october212015.com/). Neat! But how do we determine what day of the week October 21st will be? Luckily for us this is a wonderful problem for academics and math students to figure out. There is a reasonably straight forward formula to help us out:

    language:c
    //Pulled from Wikipedia: http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    //Posted by Tomohiko Sakamoto in 1993, it is accurate for any Gregorian date:
    static int t[] = ;
    year -= month < 3;
    day_of_week = (year + year/4 - year/100 + year/400 + t[month-1] + day) % 7; //0 = Sunday

Given a day/month/year and these three lines of code, we can establish that October 21st, 2015 will be a Wednesday. Now that we know the day of the week, we can determine if we are in or out of DST.

[![Clock showing monday](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Alpha_Clock_2.jpg)

## Lock Problems

Mikal Hart\'s [TinyGPS++ library](http://arduiniana.org/libraries/tinygpsplus/) is excellent to get you up and running quickly with GPS.

*Google map of our roof.*

The problem I found is that GPS clocks are often indoors, and, in the case of the SparkFun building, that makes it seriously difficult to get a GPS lock. We have lots of concrete, metal girders, and a large solar array that wreaks havoc with GPS signals (and pretty much all cellular carriers for that matter). TinyGPS++ reports the Time/Date only after you have a lock, so, when we moved the original GPS Wall Clock to our new building, I was somewhat mystified why it wasn\'t working. Posting a \'NOGPS\' debug statement to the display helped show that we almost never get sufficient enough satellites to allow TinyGPS to report time and date. Luckily, it doesn\'t take a full lock to get date and time from GPS.

[![GPS time from NMEA sentences](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Time_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Time_1.png)

If you look at the raw NMEA sentences above, you should be able to pick out \'040054\' or 4:00.54 UTC. With only 1 satellite and a very bad view of the sky, we are able to grab time from GPS.

[![GPS date and time from NMEA sentences](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Time_and_Date.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/3/GPS_Time_and_Date.png)

After a few seconds we can see the date come in as well - \'220115\' or January 22nd, 2015. The latest version of the Alphanumeric GPS Wall Clock uses a custom NMEA parser rather than relying on TinyGPS. It looks only for the availability of time and date, no GPS lock necessary. This allows us to display time in much harsher GPS environments.