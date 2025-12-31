# Source: https://learn.sparkfun.com/tutorials/scio-pocket-molecular-scanner-teardown-

## Introduction 

The [SCiO](https://www.consumerphysics.com/scio-for-consumers/) (pronounced ski-ō) is advertised as \"the world's first pocket-sized connected micro-spectrometer.\" Developed by San Francisco and Israel-based company [Consumer Physics](https://www.consumerphysics.com/business/about-consumer-physics/), the SCiO has been the topic of much debate on the internet for years. Some have lauded its attempts to bring spectrometry to the masses, while others have claimed that it cannot possibly do all the things it advertises.

[![SCiO on stand](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_01.jpg)

*The SCiO sitting on its calibration and scanning stand*

SparkFun recently got its hands on some very affordable spectral imaging ICs, the [AS7262](https://cdn.sparkfun.com/assets/parts/1/2/2/4/9/AS7262_Datasheet.pdf) and the [AS7263](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/3/AS7263_Datasheet.pdf) from [ams](http://ams.com/eng).

[![SparkFun Spectral Sensor Breakout - AS7262 Visible (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/2/6/14347-01.jpg)](https://www.sparkfun.com/sparkfun-spectral-sensor-breakout-as7262-visible-qwiic.html)

### [SparkFun Spectral Sensor Breakout - AS7262 Visible (Qwiic)](https://www.sparkfun.com/sparkfun-spectral-sensor-breakout-as7262-visible-qwiic.html) 

[ SEN-14347 ]

The SparkFun AS7262 Visible Spectral Sensor Breakout brings spectroscopy to the palm of your hand, making it easier than ever...

[ [\$28.50] ]

[![SparkFun Spectral Sensor Breakout - AS7263 NIR (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/3/8/14351-01.jpg)](https://www.sparkfun.com/sparkfun-spectral-sensor-breakout-as7263-nir-qwiic.html)

### [SparkFun Spectral Sensor Breakout - AS7263 NIR (Qwiic)](https://www.sparkfun.com/sparkfun-spectral-sensor-breakout-as7263-nir-qwiic.html) 

[ SEN-14351 ]

The SparkFun AS7263 Near Infrared (NIR) Spectral Sensor Breakout brings spectroscopy to the palm of your hand, making it easi...

[ [\$33.95] ]

After playing around with the AS7262/3, we were curious to see what technology was used in handheld scanners such as the SCiO and to see if what was under the hood had the capabilities to really bring citizen science spectral analysis to the mainstream. We got our hands on a SCiO, and after playing around with it, we decided to tear it apart and see what was inside.

## SCiO Backstory

The company behind the SCiO, Consumer Physics, launched a [Kickstarter campaign](https://www.kickstarter.com/projects/903107259/scio-your-sixth-sense-a-pocket-molecular-sensor-fo) back in April 2014 and raised about \$2.7 million. An amazing feat considering that many attempts to make similar devices using crowdfunding had been [labeled as scams](https://pando.com/2014/04/04/revealed-healbe-isnt-indiegogos-first-giant-medical-scam/). Their campaign was even [commended as a success](https://pando.com/2014/04/30/consumer-physics-kickstarter-campaign-shows-that-not-all-crowd-funding-has-to-be-a-dishonest-mystery/) compared with previous attempts. However, that praise was short lived.

What started as high hopes for the product quickly turned into anger. Many [doubted](https://www.cnet.com/news/kickstarter-science-beware-the-marketing-hype/) that the device could do [what it claimed](http://spectrum.ieee.org/tech-talk/consumer-electronics/gadgets/handheld-spectroscopy-tool-lets-you-examine-the-molecular-composition-of-your-food), and after waiting more than two years and still not receiving their promised SCiO, many backers of the product took their [frustration](https://techcrunch.com/2016/09/16/scio-the-pocket-sized-molecular-analyzer-is-making-everyone-angry/) to the [internet](http://spectrum.ieee.org/the-human-os/biomedical/devices/angry-kickstarter-backers-ask-scio-wheres-my-pocketsized-molecular-sensor).

Original ship dates for the Kickstarter campaign rewards ranged from October 2014 to February 2015. By late 2016, there were still many backers who had not received their SCiO. To make matters worse, the Kickstarter campaign page was taken down and remains down to this day, removing the main line of communication between the company and its backers. This was originally thought to be over intellectual property disputes, but it was later revealed that the reason was a trademark dispute over the name SCiO rather than a dispute over the technology SCiO uses. SCiO\'s CEO, Dror Sharon, [claimed](https://www.crowdfundinsider.com/2016/09/90225-consumer-physics-rep-confirms-no-intellectual-property-dispute-around-scio/), \"This is solely in regards to using the term 'SCiO' in the product name. The sensor technology is not affected in any way."

The company responded to the late delivery of their product, claiming that existing technology wouldn\'t allow for the size and price point they were looking for, which resulted in an unanticipated redesign. Sharon [stated](http://spectrum.ieee.org/the-human-os/biomedical/devices/angry-kickstarter-backers-ask-scio-wheres-my-pocketsized-molecular-sensor), "We started to ship units in April 2015, but as we ramped up production we discovered issues --- sometimes with our parts, sometimes with our designs."

Despite all the setbacks and angry backers, the company fulfilled all their Kickstarter pledges, and the SCiO was made available for sale to the general public in late 2016/early 2017. What remains to be seen is if a large enough community will form around the product to catapult it and its app to the forefront of daily use in grocery stores and around the home or if the information it provides is not useful enough to justify carrying around yet another handheld device.

## Unboxing and Initial Thoughts 

The SCiO was unboxed promptly upon receipt. Inside was the device, a stand that doubles as a housing for scanning small items such as pills, a small shade spacer for controlling the light source purity, a microUSB cable and a couple of booklets, including a Quick Start guide.

[![unboxing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_00.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_00.jpg)

The functionality of the SCiO was tested before the teardown took place. Taking spectral scans of items really was easy right from the get-go, and the sleek design and small form factor left a lasting first impression.

However, it soon became clear that what was delivered was a hardware platform with very little software or app support. The SCiO app, while sleek and easy to use, seemed rather bare in terms of functionality. Many of capabilities promised in SCiO promotional material was very unpolished or nonexistent, such as the fruit scanning applet having only about a half dozen fruits to choose from. Writing the applets for scanning various items has been mostly left up to the users and developers. While the tools to create your own applets exist, it would have been nice to have a larger selection of items to scan out of the box.

Particularly conspicuous was the absence of any sort of plant-scanning applet. As the resident [aquaponics enthusiast](https://www.sparkfun.com/news/tags/aquaponics) here at SparkFun, that was one of the major features that attracted me to the SCiO in the first place: being able to scan plant leaves and derive plant health data from the spectral image.

[![SCiO App](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_App.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_App.png)

*The SCiO app for iOS, pictured as of this writing (Courtesy [iTunes App Store](https://itunes.apple.com/us/app/scio-pocket-molecular-sensor/id1037962554?mt=8)*)

That said, there were still lots of applets to play with in the app. The fruit and vegetable scanner was fun, though the number of fruits and veggies listed in the database was smaller than expected. Other food items that had applets included meats, cheeses and chocolate.

The body fat index applet was another fun one to play with. Scanning your skin and entering basic data about yourself allows you to get a rough estimate from the device calculating your body fat percentage. While the data coming back from the device seemed like it could be accurate, it was hard to confirm.

It would seem that, for now, creating useful applications using this hardware is left in the hands of the community.

## Device Teardown

Enough talk\...let\'s get to the good stuff, the teardown!

To begin, the plastic housing was dissected. This enclosure was not meant to be taken apart and reassembled \-\-- at least not easily.

[![dissection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_02.jpg)

There was not a whole lot to the device inside. Three screws held the LiPo battery housing to the enclosure, with the PCB sandwiched between. The only real user interfaces were the large, singular button for powering and scanning, the microUSB slot for charging and the charging indicator LED.

[![first layer of parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_03.jpg)

The most noticeable part of the assembly was the very large heatsink that wrapped around the PCB and was affixed to the imaging sensor with heat-transferring adhesive. The only thing connecting the PCB to the sensor was a flat flex cable assembly with a socket connector on the end.

[![heatsink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_04.jpg)

All we were left with was the bare PCB. It had an impressive amount of technology packed onto one little board. One side was populated with a majority of the ICs and the user interface button, complete with reverse-mounted LED.

[![bare pcb top](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_08.jpg)

The other side was populated with the socket connector for the sensor, microUSB connector, battery connection, Bluetooth® antenna and other various bits and pieces.

[![bare pcb bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_09.jpg)

## Optical Sensor Teardown 

It was time to open up the really interesting bit: the optical sensor. This is the magic behind the SCiO, an NIR spectrometer the size of an IC. This sensor was completely custom made, as has been mentioned in interviews with Consumer Physics\' CEO. The most standout marking on the sensor denoted it was made, at least in part, by Taiwanese-based manufacturer [Ichia](http://www.ichia.com/index.php?option=com_content&view=article&id=597&Itemid=1275&lang=en), which specializes in \"high-end fine pitch flexible circuit board.\"

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_05.jpg)

Noting the number of connections on the socket connector for the sensor, it was clear that they were not understating the \"fine pitch\" portion of their business model.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_06.jpg)

The sensor/heatsink combo was attached to the front of the enclosure with two more screws, bringing the total number of screws used in the entire assembly to five. One nice feature of the housing was the magnets embedded within, which allowed for a magnetic bond between the device and its stands, as seen in the image below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_07.jpg)

The sensor was pried apart from the heatsink, leaving us with the last bit to tear down. Using a Dremel and a cutting wheel, the epoxy surrounding the sensor was carefully cut away to reveal its insides.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-12.jpg)

Inside was a very complex photodiode array with many layers. Alongside was the very bright LED light source and an additional IC, presumably used to control the light source.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-13.jpg)

The remaining layers of the photodiode array were pulled out with tweezers. There was what appeared to be a diffusion layer: a single sheet of white paper-like material. It\'s assumed this is meant to diffuse the light even across all the photodiodes. Next, there was a filter layer with visibly different filters covering each of the 12 receptors. Underneath that was an aperture layer: a very thin, opaque layer with different aperture hole sizes for each receptor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-14.jpg)

At the very bottom of the sensor stack was a lens layer: a plastic piece with 12 seemingly identical spherical lenses pointed toward the photodiodes.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-15.jpg)

With all those layers removed, all that was left was the bare wire-bonded sensor array, a testament to the customization that went into this device.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCIO_Teardown_Images-16.jpg)

## Integrated Circuits 

What teardown would be complete without a look at the electronics used inside the device? Let\'s see what information we could derive from the ICs found inside the SCiO.

The largest and easiest to identify IC was the [Blackfin ADSP-BF512 Embedded Processor](http://www.analog.com/media/en/technical-documentation/data-sheets/ADSP-BF512_514_514F16_516_518_518F16.pdf) from Analog Devices.

Located next to the processor is the [AS4C8M16SA](http://www.alliancememory.com/pdf/dram/128M-AS4C8M16SA.pdf) from Alliance Memory, 128 Mbits of SDRAM. The other three ICs alongside the memory could not be identified.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_10.jpg)

The largest IC on the opposite side is the [CC2540F256](http://www.ti.com/lit/ds/symlink/cc2540.pdf) 2.4-GHz Bluetooth low energy System-on-Chip from Texas Instruments. The traces from this IC extend out to the onboard antenna.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/7/SCiO_Teardown_11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/SCiO_Teardown_11.jpg)

### Data Matrices

As electronics and the products they go into continue to decrease in size, so too must the marking on those devices shrink. As a result, many products, be it an IC or a molded piece of plastic, now have [data matrices](https://en.wikipedia.org/wiki/Data_Matrix) stamped, stickered, or even laser etched onto them. These matrices allow for lots of information to exist in a small amount of space. The SCiO was covered in data matrices, from the case that holds the SCiO, to the flat flex cable, to the ICs found within. While looking up the info contained in these did not produce any meaningful data (most of the information contained within the matrix pertains to the manufacturer and can relate to anything from the firmware that was uploaded to an IC to the batch data from a group of molded pieces), it was still fun to look up. For those who are curious, here is the data found from each matrix:

- Data Matrix Code found on the Analog Devices Blackfin IC: PF041700RU/CP-PCA0031-C-7/ 641240/6A1
- Data Matrix Code found on the ichia flat flex cable: SF421601JN/CP-MA00005-2-16/641103/921
- Data Matrix Code found on the plastic cover for the SCiO: AC50160263

## Final Thoughts

There is no doubt that a ton of engineering went into the SCiO. It was impressive to see that much technology packed into such a tiny package. And, the complexity of the sensor left no doubt in my mind that this device is more complex than the spectral sensor ICs offered on our breakout boards.

That said, SCiO seems to have already shifted its focus from making a stand-alone scanning device to creating a small enough assembly to [embed its technology inside smartphones](http://thespoon.tech/consumer-physics-maker-of-controversial-scio-food-sensor-pursues-a-scio-inside-strategy/). [This article](http://spectrum.ieee.org/view-from-the-valley/at-work/start-ups/israeli-startup-consumer-physics-says-its-scio-food-analyzer-is-finally-ready-for-prime-timeso-we-took-it-grocery-shopping) even shows a sneak peek of the new technology, created in conjunction with Consumer Physics and Analog Devices.

[![embedable SCiO](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/phoneSCiO.jpeg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/7/phoneSCiO.jpeg)

*Photo courtesy of Tekla Perry via [ieee.org](http://spectrum.ieee.org/view-from-the-valley/at-work/start-ups/israeli-startup-consumer-physics-says-its-scio-food-analyzer-is-finally-ready-for-prime-timeso-we-took-it-grocery-shopping)*

As this and other technologies continue to push to be in smartphones by default, the closer we get to a world where [Tricorders](http://www.tricorderproject.org/) are very real, and they also happen to make phone calls!