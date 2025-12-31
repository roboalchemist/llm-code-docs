# Source: https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units

## Introduction

Metric Prefixes are incredibly useful for describing quantities of the [International System of Units (SI)](http://en.wikipedia.org/wiki/International_System_of_Units) in a more succinct manner.

When exploring the world of electronics, these units of measurement are very important and allow people from all over the world to communicate and share their work and discoveries. Some common units used in electronics include voltage for electrical potential difference, ampere for electrical current, watts for power, farad for capacitance, henry\'s for inductance, and ohms for resistance.

This tutorial will not only go over some of the most commonly used units in electronics but will also teach you the metric prefixes that help describe all of these base units in quantities ranging from the insanely large to the incredibly small.

### Suggested Reading

If you would like to know more about the components that use the units and prefixes described in this tutorial, check out some of these related tutorials.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/capacitors)

### Capacitors 

Learn about all things capacitors. How they\'re made. How they work. How they look. Types of capacitors. Series/parallel capacitors. Capacitor applications.

You should also be familiar with binary in order to help you understand binary prefixes.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

## SI Units

We\'ve been measuring stuff for millennia, and our units used for those measures have been evolving since then. There are now dozens of units to describe physical quantities. For example, length can be measured by the foot, meter, fathom, chain, parsec, league, and [so on](http://en.wikipedia.org/wiki/Unit_of_length). In order to better communicate measurements, we needed a standardized system of units, which every scientist and measurer could use to share their findings. This standardized system has come to be called the \\ **International System of Units** \\\</epic voice\>, abbreviated **SI**.

### Physical SI Units

  Quantity      SI Unit   Unit Abbreviation
  ------------- --------- -------------------
  Time          second    s
  Length        meter     m
  Mass          gram      g
  Temperature   kelvin    K
  Force         newton    N

\

While we can still use units like feet or miles for distance (instead of meters), liters to describe volume (instead of m^3^), and Fahrenheit or Celsius to describe temperature (instead of °K), the units above are a **standardized** way for every scientist to share their measurements. Using the units above means everyone is speaking the same language.

### Common Electronics Units

In dealing with electronics, there are a handful of units we\'ll be encountering more often than others. These include:

  Quantity                                  SI Unit   Unit Abbreviation
  ----------------------------------------- --------- -------------------
  Electric Potential Difference (Voltage)   volts     V
  Electric Current                          ampere    A
  Power                                     watt      W
  Energy/Work/Heat                          joule     J
  Electric Charge                           coulomb   C
  Resistance                                ohm       Ω
  Capacitance                               farad     F
  Inductance                                henry     H
  Frequency                                 hertz     Hz

------------------------------------------------------------------------

Now that we know the units, let\'s look at how they can be augmented with prefixes to make them even more usable!

## The Prefixes

When first learning about metric prefixes, chances are you were taught these six prefixes first:

  --------------------- ----------- ----------------------------
  **Prefix (Symbol)**   **Power**   **Numeric Representation**
  kilo (k)              10^3^       1,000
  hecto (h)             10^2^       100
  deka (da)             10^1^       10
  no prefix             10^0^       1 unit
  deci (d)              10^-1^      0.1
  centi (c)             10^-2^      0.01
  milli (m)             10^-3^      0.001
  --------------------- ----------- ----------------------------

\

These are what we\'ll consider the standard six prefixes taught in most High School science courses. You may have even learned a fun mnemonic to go along with these such as *Kangaroos Have Dirty Underwear During Cold Months*. However, as you\'ll soon see, when learning about electronics and computer science, the range of prefixes well exceeds the standard six. While these prefixes cover a rang of 10^-3^ to 10^3^, many electronic values can have a much larger range.

### Describing the Large

  --------------------- ----------- ----------------------------
  **Prefix (Symbol)**   **Power**   **Numeric Representation**
  yotta (Y)             10^24^      1 septillion
  zetta (Z)             10^21^      1 sextillion
  exa (E)               10^18^      1 quintillion
  peta (P)              10^15^      1 quadrillion
  tera (T)              10^12^      1 trillion
  giga (G)              10^9^       1 billion
  mega (M)              10^6^       1 million
  kilo (k)              10^3^       1 thousand
  no prefix             10^0^       1 unit
  --------------------- ----------- ----------------------------

\

These above prefixes dramatically help describe quanities of units in large amounts. Instead of saying 3,200,000,000 Hertz, you can say 3.2 GigaHertz, or 3.2 GHz for shorthand written notation. This allows us to describe incredibly large numbers of units succinctly. There are also prefixes for helping communicate tiny numbers as well.

### Describing the Small

  --------------------- ----------- ----------------------------
  **Prefix (Symbol)**   **Power**   **Numeric Representation**
  no prefix             10^0^       1 unit
  milli (m)             10^-3^      1 thousandth
  micro (µ)             10^-6^      1 millionth
  nano (n)              10^-9^      1 billionth
  pico (p)              10^-12^     1 trillionth
  femto (f)             10^-15^     1 quadrillionth
  atto (a)              10^-18^     1 quintillionth
  zepto (z)             10^-21^     1 sextillionth
  yocto (y)             10^-24^     1 septillionth
  --------------------- ----------- ----------------------------

\

Now, instead one trillionth of a second, it can be referred to as a picosecond. One thing to notice about the prefixes for small values, is that their shorthand notations are all lower case while the large number prefixes are upper case (with the exception of kilo-\*, hecto- and deca-). This allows you to distinguish between the two when they use the same letter. As an example, one mW (milliwatt) does not equal one MW (megawatt).

\***Note:** Since the upper case \'K\' was already used to describe Kelvins, a lower case \'k\' was chosen to represent the prefix kilo-. As you\'ll see in the [Bits and Bytes section](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units/bits-and-bytes), there is also some confusion with k and K when dealing with the binary (base 2) prefixes.

## Conversion

The beautiful thing about these metric prefixes is that, once you get the hang of conversion between a few of them, translating that ability to all the other prefixes is easy.

As a first simple example, lets translate 1 Ampere (A) into smaller values. A milliampere is 1 thousandth of the unit Ampere hence 1 Ampere is equal to 1000 milliamperes. Going further, 1 milliampere is equivalent to 1000 microamperes and so on. Going in the opposite direction, 1 Ampere is .001 Kiloampere, or 1000 Amperes is 1 Kiloampere. Now that\'s a lot of current!

As you may have noticed, switching between prefixes is the same as moving the decimal point over by 3 places. This is also the same as multiplying or dividing by 1000. When you\'re going up to a larger prefix, from Kilo to Mega for example, the decimal place is moved three places to the left. 100,000 Kilowatts equals 100 Megawatts. 10 Kilowatts equals .01 Megawatts. Mega is the prefix right above Kilo so regardless of whether we are talking about Watts, Amperes, Farads, or whatever unit, the movement of the decimal place by three positions to the left still works when moving up a prefix.

When moving down a prefix, let\'s say from nano- to pico-, the decimal place is moved three places to the right. 1 nanoFarad equals 1000 picoFarads. .5 nanoFarad equals 500 picoFarads. Here\'s a short list so you can see the pattern:

1 Giga- = 1000 Mega-\
1 Mega- = 1000 Kilo-\
1 Kilo- = 1000 units\
1 unit = 1000 milli-\
1 milli- = 1000 micro-\

See the trend? Each prefix is a thousand times larger than the previous. While a little overwhelming at first, translation from one prefix to another eventually becomes second nature.

## Bits and Bytes

Working with bits and bytes can cause a bit confusion (pun intended). Since computers work with base 2 numbers instead of base 10, it is often unclear which number base one is referring to when using the metric prefixes. For example, 1 Kilobyte is often used to mean 1000 bytes (base 10), or it can be used to represent 1024 bytes (base 2), resulting in misunderstandings.

To eliminate these mix-ups, the International Electrotechnial Commision came up with some new prefixes for the base 2 bits and bytes. These are referred to as [binary prefixes](http://en.wikipedia.org/wiki/Binary_prefix).

  --------------------- ----------- ----------------------------
  **Prefix (Symbol)**   **Power**   **Numeric Representation**
  exbi- (Ei-)           2^60^       1,152,921,504,606,846,976
  pebi- (Pi-)           2^50^       1,125,899,906,842,624
  tebi- (Ti-)           2^40^       1,099,511,627,776
  gibi (Gi-)            2^30^       1,073,741,824
  mebi- (Mi-)           2^20^       1,048,576
  kibi- (Ki-)           2^10^       1,024
  no prefix             2^0^        1 bit or byte
  --------------------- ----------- ----------------------------

\

Adopting this would mean 1 Megabyte = 1000 Kilobytes while 1 Mebibyte equals 1024 Kibibytes. Essentially for bits and bytes, each jump in prefix would be a multiple of 1024 (2\^10) instead of 1000 (10\^3). Unfortunately, this system is not widely used in practice, so anytime you hear a number of bytes or bits, you have to wonder if they are talking about them in base 2 or base 10.

Hard drive companies and others typically sell products in base 10 as it makes it sound larger. A 1 Terabyte hard drive will turn out to actually be about 931.3 Gibibytes.

This is where we run into the upper case and lower case \'k\' situation. The proper prefix for kibi if \'Ki\'. However, it will sometimes appear as just and upper case \'K\', which, again, represents temperature in Kelvins. So, any time you hear the word Kilobyte, you still have to wonder if it signifies 1000 bytes (base 10) or 1024 bytes (base 2). On the other hand, if you see the term kibibyte, you know for sure it\'s talking about the base 2 version interpretation of digital storage (1024 bytes).

### Converting Bits to Bytes and Bytes to Bits

We\'ve covered converting bits and bytes to larger or smaller numbers of each, but there is also the matter of converting bits *to* bytes and vise versa. Remember that 1 Byte is equal to 8 bits (a majority of the time), and one bit is equal to 0.125 bytes (or 1/8). Granted, there are many [orders of magnitude](http://en.wikipedia.org/wiki/Orders_of_magnitude_%28data%29) pertaining to bits, but byte is typically used most frequently. The practice of converting between one and the other is not all that common, but it is still useful information when dealing with electronics, especially when it comes to memory. For example, you could be writing code that stores individual bits, but your memory is defined as bytes.

## Practice

Now for some practice exercises. We\'ll use standard abreviations for each unit type we\'ll convert:

- A for Amperes
- V for Volts
- W for Watts
- Hz for Hertz
- F for Farads
- H for Henry\'s
- Ω for Ohms
- s for Seconds
- B for Bytes
- b for bits

### Conversion Example:

- Convert: 400 mA to A
- Answer: 400 mA = .4 A

### Convert:

1.  50 mA to A
2.  10 nF to pF
3.  500 kW to W
4.  .01 mV to µV
5.  20,000 kΩ to MΩ
6.  4680 MHz to GHz
7.  4 TiB to GiB
8.  200 Mb to kb
9.  .00007 s to µs
10. 1450 nH to µH

## Practice Answers

1.  .05 A
2.  10,000 pF
3.  500,000 W
4.  10 µV
5.  20 MΩ
6.  4.68 GHz
7.  4096 GiB
8.  200,000 kb
9.  70 µs
10. 1.45 µH

Soon, switching between prefixes when needed becomes very quick.