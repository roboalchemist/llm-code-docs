# Source: https://learn.sparkfun.com/tutorials/endless-runner-game

## Introduction

Popularized by mobile games like [Temple Run](https://en.wikipedia.org/wiki/Temple_Run), the [endless running](https://en.wikipedia.org/wiki/Platform_game#Endless_running_game) type of game is an extremely simplistic spin on the larger \"platform\" genre where a player has limited control over a character that is constantly moving forward. [Flappy bird](https://en.wikipedia.org/wiki/Flappy_Bird), while generally not considered a \"running\" game, was another popular infinite platform game with limited control over the character: users could only tap the screen to make the bird fly upward in order to navigate through obstacles while constantly moving to the right.

We\'re going to make our own endless runner game using an Arduino, button and character LCD. While not as visually appealing as Temple Run or Flappy Bird, it\'s almost as addicting.

The code for this game comes from [Joshua Brooks on Instructables](http://www.instructables.com/member/joshua.brooks/). The original project can be found [here.](http://www.instructables.com/id/Arduino-LCD-Game/)

[![Playing the endless runner Arduino game](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/6/SIKv4_Projects-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/6/SIKv4_Projects-14.jpg)

### Required Materials

You can complete this project with parts from the [SparkFun Inventor\'s Kit v4.0](https://www.sparkfun.com/products/14265). Specifically, you will need:

**Note:** If you purchase the parts separately, you will need to solder [headers](https://www.sparkfun.com/products/116) onto the LCD.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

## Hardware Assembly

Using jumper wires, connect the components as shown in the diagram below.

[![SIK v4.0 Endless Runner Game](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/6/Endless_Runner_bb1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/6/Endless_Runner_bb1.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

## Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Copy and paste the following code in the Arduino IDE. Click **Upload** to send your compiled code to the Arduino.

    language:c
    /**
     * Endless Runner
     * Date: August 18, 2017
     * Author: Joshua Brooks (http://www.instructables.com/member/joshua.brooks/)
     * Modified by: Shawn Hymel (SparkFun Electronics)
     * 
     * Adjust LCD contrast with the potentiometer. Press the button
     * to start the game. During gameplay, press the button to jump
     * and avoid obstacles. Running into an object will result in
     * restarting. Points are awarded based on distance.
     */

    #include <LiquidCrystal.h>

    // Constants
    #define BTN_PIN 7

    #define SPRITE_RUN1 1
    #define SPRITE_RUN2 2
    #define SPRITE_JUMP 3
    #define SPRITE_JUMP_UPPER '.'         // Use the '.' character for the head
    #define SPRITE_JUMP_LOWER 4
    #define SPRITE_TERRAIN_EMPTY ' '      // User the ' ' character
    #define SPRITE_TERRAIN_SOLID 5
    #define SPRITE_TERRAIN_SOLID_RIGHT 6
    #define SPRITE_TERRAIN_SOLID_LEFT 7

    #define HERO_HORIZONTAL_POSITION 1    // Horizontal position of hero on screen

    #define TERRAIN_WIDTH 16
    #define TERRAIN_EMPTY 0
    #define TERRAIN_LOWER_BLOCK 1
    #define TERRAIN_UPPER_BLOCK 2

    #define HERO_POSITION_OFF 0          // Hero is invisible
    #define HERO_POSITION_RUN_LOWER_1 1  // Hero is running on lower row (pose 1)
    #define HERO_POSITION_RUN_LOWER_2 2  //                              (pose 2)

    #define HERO_POSITION_JUMP_1 3       // Starting a jump
    #define HERO_POSITION_JUMP_2 4       // Half-way up
    #define HERO_POSITION_JUMP_3 5       // Jump is on upper row
    #define HERO_POSITION_JUMP_4 6       // Jump is on upper row
    #define HERO_POSITION_JUMP_5 7       // Jump is on upper row
    #define HERO_POSITION_JUMP_6 8       // Jump is on upper row
    #define HERO_POSITION_JUMP_7 9       // Half-way down
    #define HERO_POSITION_JUMP_8 10      // About to land

    #define HERO_POSITION_RUN_UPPER_1 11 // Hero is running on upper row (pose 1)
    #define HERO_POSITION_RUN_UPPER_2 12

    // Globals
    LiquidCrystal lcd(8, 9, 10, 11, 12, 13);
    static char terrainUpper[TERRAIN_WIDTH + 1];
    static char terrainLower[TERRAIN_WIDTH + 1];
    static bool buttonPushed = false;

    void setup() 

    void loop() 

      // Show start screen if not currently playing game
      if (!playing) 
        delay(250);
        blink = !blink;
        if (buttonPushed) 
        return;
      }

      // Shift the terrain to the left
      advanceTerrain(terrainLower, newTerrainType == TERRAIN_LOWER_BLOCK ? SPRITE_TERRAIN_SOLID : SPRITE_TERRAIN_EMPTY);
      advanceTerrain(terrainUpper, newTerrainType == TERRAIN_UPPER_BLOCK ? SPRITE_TERRAIN_SOLID : SPRITE_TERRAIN_EMPTY);

      // Make new terrain to enter on the right
      if (--newTerrainDuration == 0)  else 
      }

      // Jump if button is pressed
      if (buttonPushed) 

      // Draw hero on screen and check for collisions
      if (drawHero(heroPos, terrainUpper, terrainLower, distance >> 3))  else  else if ((heroPos >= HERO_POSITION_JUMP_3 && heroPos <= HERO_POSITION_JUMP_5) && terrainLower[HERO_HORIZONTAL_POSITION] != SPRITE_TERRAIN_EMPTY)  else if (heroPos >= HERO_POSITION_RUN_UPPER_1 && terrainLower[HERO_HORIZONTAL_POSITION] == SPRITE_TERRAIN_EMPTY)  else if (heroPos == HERO_POSITION_RUN_UPPER_2)  else 
        ++distance;
      }

      delay(100);
    }

    // Create custom character LCD graphics
    void initializeGraphics() ;
      int i;

      // Skip using character 0, this allows lcd.print() to be used
      // to quickly draw multiple characters
      for (i = 0; i < 7; ++i) 

      // Fill screen with empty terrain
      for (i = 0; i < TERRAIN_WIDTH; ++i) 
    }

    // Slide the terrain to the left in half-character increments
    void advanceTerrain(char* terrain, byte newTerrain) 
      }
    }

    // Draw hero on screen and check for collisions
    bool drawHero(byte position, char* terrainUpper, char* terrainLower, unsigned int score) 

      // Detect collisions with terrain
      if (upper != ' ') 
      if (lower != ' ') 

      // Calculate number of digits needed to draw the score
      byte digits = (score > 9999) ? 5 : (score > 999) ? 4 : (score > 99) ? 3 : (score > 9) ? 2 : 1;

      // Draw the scene
      terrainUpper[TERRAIN_WIDTH] = '\0';
      terrainLower[TERRAIN_WIDTH] = '\0';
      char temp = terrainUpper[16 - digits];
      terrainUpper[16 - digits] = '\0';
      lcd.setCursor(0, 0);
      lcd.print(terrainUpper);
      terrainUpper[16 - digits] = temp;
      lcd.setCursor(0, 1);
      lcd.print(terrainLower);

      // Draw score in upper right of screen
      lcd.setCursor(16 - digits, 0);
      lcd.print(score);

      terrainUpper[HERO_HORIZONTAL_POSITION] = upperSave;
      terrainLower[HERO_HORIZONTAL_POSITION] = lowerSave;

      return collide;
    }

### What You Should See

When the code finishes uploading, you should be presented with a flashing \"Press Start\" notification. If you do not see anything on the LCD, try turning the potentiometer to adjust the contrast.

[![Adjust the contrast with the potentiometer knob](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/6/SIKv4_Projects-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/6/SIKv4_Projects-15.jpg)

Press the button (the only button available) to begin the game. Once the game starts, you need to press the button again to jump in order to avoid the obstacles that zoom by. If you hit an obstacle, you must start over. The farther you run, the higher your score (as shown by the number in the upper right corner).

[![Playing the endless runner game](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/6/LCD-screen.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/6/LCD-screen.gif)