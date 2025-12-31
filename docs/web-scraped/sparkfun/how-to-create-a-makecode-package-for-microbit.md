# Source: https://learn.sparkfun.com/tutorials/how-to-create-a-makecode-package-for-microbit

## Introduction

Microsoft MakeCode is a block based coding language designed to introduce people to coding. MakeCode is nice because it allows the basic structures and thought processes used in algorithm design to take place without having to worry about syntax or data type. Under the hood, MakeCode is based on [static typescript](https://makecode.com/language) and javascript. In this tutorial, we\'ll develop a MakeCode extension for the [Soil Moisture Sensor](https://www.sparkfun.com/products/13322) using an existing SparkFun extension.

[![A Few Existing SparkFun Extensions in MakeCode for micro:bit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/4/MicroBit_SparkFun_Extensions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/4/MicroBit_SparkFun_Extensions.jpg)

*A Few Existing SparkFun Extensions in MakeCode for micro:bit*

## Thing\'s You\'ll Need

First, let\'s set up our build environment, we\'ll start by downloading and installing [Node.js](https://nodejs.org/).

[Download Node.js](https://nodejs.org/)

You\'ll also need a GitHub account. Now go ahead and [open any old command prompt](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and navigate to to where you store your GitHub files (I create a GitHub folder on my **C:\\** drive so for me this is **C:\\GitHub**). Then go ahead and run the following commands. This installs a few npm packages to use.

    language:bash
    npm install
    npm install jake
    npm install typings

We\'ll then clone the PXT directory into our GitHub folder and run these npm packages we just installed. At the end, back out to the GitHub folder once more. This is accomplished with the following commands.

    language:bash
    git clone https://github.com/microsoft/pxt
    cd pxt
    git checkout
    npm install
    typings install
    jake
    cd..

We\'ll then clone in the Micro:Bit target, and install pxt there.

    language:bash
    git clone https://github.com/Microsoft/pxt-microbit
    cd pxt-microbit
    npm install -g pxt
    npm install
    cd..

This should be everything we need to build our project, now let\'s clone in an existing SparkFun MakeCode package and get started editing it.

    language:bash
    git clone https://github.com/sparkfun/pxt-gator-light

## What to Change

Let\'s go ahead and [create a new GitHub repository](https://help.github.com/en/articles/create-a-repo) for our new MakeCode package, we\'ll call it **pxt-gator-moisture**. Clone this repo into your GitHub folder, then go ahead and copy over the contents of the **pxt-gator-light** repo. We\'ll mainly be looking at the two **gatorlight** files, the **pxt.JSON** file, the **README.MD**, and eventually the **icon.png**.

[![pxt-gator-moisture](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/6/folder.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/6/folder.JPG)

*We must change these files. Click the image to enlarge*

First, we\'re going to go through and rename everything to **gatormoisture**, so go ahead and rename the two **gatorlight** files, once we\'ve renamed them, go ahead and open up **pxt.json** and replace every instance of the word **light** with **moisture**. The **\*.json** file tells MakeCode which files to include, and since we changed our filenames, we\'ll have to change them here as well. Don\'t neglect to roll the version number back to **0.0.1** as well as change the description to something that makes more sense. We\'re then going to open up both **gatormoisture** files and replace every instance of light with moisture once again.

Let\'s now look at where the code behind our blocks actually lives, the blocks live in the **\*.ts** file while the actual functions live in the **\*.cpp**. Let\'s check out the **\*.cpp** first. We make sure to include `pxt.h` with every package, as well as use the `pxt` namespace. We then create a namespace, \"`gatormoisture`\" and put the function that calculates lux from a given ADC value. It\'s a pretty simple function but we\'ll be able to call it from our **\*.ts** file, which is what we really wanted.

    language:c
    #include "pxt.h"
    #include <cstdint>
    #include <math.h>

    using namespace pxt;

    namespace gatorMoisture 

    }

While we\'re here, let\'s change `getLux` to a `getMoisture` function that returns a float in between 0 and 1 instead of a value in lux. For this, we will simply divide the `ADCVal` passed in by the full-scale range of the ADC (1023). In the end, our **gatormoisture.cpp** looks like the following.

    language:c
    #include "pxt.h"
    #include <cstdint>
    #include <math.h>

    using namespace pxt;

    namespace gatorMoisture 
    }

Now let\'s check out how our blocks are created in the **\*.ts** file, which should look like the following after we\'ve changed everything from light to moisture.

    language:c
    enum gatorMoistureType

    //% color=#f44242 icon="\uf185"
    namespace gatorMoisture 
        }

        /**
         * Function used for simulator, actual implementation is in gatormoisture.cpp
         */
        //% shim=gatorMoisture::getMoisture
        function getMoisture(ADCVal: number) 
    }

If we want to have options in dropdowns for our blocks, we create them using an enum. We will be able to choose whether we want moisture, a value between 0 and 1, or the straight adcVal. So outside of the namespace, we create an enum (shown below) for our possible data types.

    language:c
    enum gatorMoistureType

We then must pick a color and icon for our extension, which is done in the line before we declare our namespace. The color can be any 6-digit, hexadecimal value, while the icon will use it\'s identifier from the [FontAwesome](https://fontawesome.com/icons?from=io) icon library. The color and icon declarations are shown below.

    language:c
    //% color=#f44242 icon="\uf185"

We then need to define what our block looks like and where it sits relative to other blocks. This is done by setting **weight**, **blockId**, and **block**. A block with weight 100 will list itself above blocks with weights below 100 and and below blocks with weights above 100. This allows you to decide how you want all of your blocks to be listed. The blockId **MUST** be `mynamespacetitle_functionTitle` so for our `moisture` block, which is in the `gatorMoisture` namespace, our blockId will be `gatorMoisture_moisture`. Finally, we decide exactly what goes into the text for the block using the `block` string. Any variable that we want to become a dropdown will be prefaced with a `%`. The following code will create a block with a dropdown for pin selection and a dropdown that allows you to choose between **moisture** and **adcVal**. This block will call the function `moisture` using whatever arguments that have been selected from the dropdown.

    language:c
    //% weight=30 blockId="gatorMoisture_moisture" block="Get moisture on pin %pin | in %gatorMoistureType"

Finally, we\'ll need to write the function that actually reads our pin. Any function that is declared as `export` will appear as a block in MakeCode. Arguments for this function will be whatever we declared as dropdown capable variables and we\'ll usually need to set up a switch statement based on the type to return the proper values for each type selected. Notice how we call `getMoisture`, the function contained in our **\*.cpp** when our type is `moisture`. We also must declare what the function returns, in this case, a number.

    language:c
    export function moisture(pin: AnalogPin, type: gatorMoistureType): number
    }

Any functions in our **\*.cpp** will need a dummy function for the simulator. We create the analog for our `getMoisture` function as follows. Notice how, since it isn\'t exported, we won\'t see it in MakeCode.

    language:c
    //% shim=gatorMoisture::getMoisture
    function getMoisture(ADCVal: number) 

Finally, we\'ll need to change the final part of the `README` (line 49) to our namespace followed by the GitHub address, this looks like `gatorMoisture=github:sparkfun/pxt-gator-soil` and allows the package to be recognized as a MakeCode extension.

## Compiling your Code

Now that we\'ve written all of our code, it\'s time to compile and test it, go ahead and open up a command prompt window and navigate to the directory where your MakeCode package lives. Once there, run the following commands to link to install the necessary PXT tools to build your code

    language:bash
    npm install
    npm install typings
    npm install jake
    npm link ../pxt
    pxt target microbit
    pxt install

We then want to build our code and commit and push our changes to GitHub.

    language:bash
    pxt build
    git add -A
    git commit -m "changing names to gator:moisture"
    pxt bump

The `pxt bump` command will prompt you to enter a version number with which to tag your release, just make sure it\'s higher than or equal to the version that you are being prompted to enter. The command will then tag your commit and push it to GitHub as a release.

[![PXT Bump](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/6/pxtbump.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/6/pxtbump.JPG)

*PXT Bump*

## Test, Rinse, Repeat!

To test our code, let\'s go ahead and open up the [MakeCode Website](https://makecode.microbit.org/#editor) and navigate down to extensions.

[![Extensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/6/ext.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/6/ext.png)

*Extensions*

From there, we\'ll log into our GitHub using a token, to do this, simply follow the instructions when you click `login to GitHub`.

[![Login to Github](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/6/ext2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/6/ext2.png)

*Login to Github*

After we log in, we can paste the URL for the GitHub repo into the extension search bar, click on the result to include it! If it doesn\'t pop up, ensure that your repository is public.

Once you\'ve included your extension, feel free to check out its various features, edit the code as necessary and re-upload it to GitHub until you\'re satisfied!