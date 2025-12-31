# Source: https://learn.sparkfun.com/tutorials/badgerhack-gaming-add-on-kit

## Introduction 

The BadgerStick that you received by visiting a SparkFun booth at one of the various events we\'ve attended can be hacked to perform a wide variety of tasks. The display may be small (don\'t get your hopes up of running [Doom](https://learn.sparkfun.com/tutorials/setting-up-raspbian-and-doom) on an 8x7 monochrome display). However, we can use it to display information and even play some basic games.

[![BadgerHack](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)

This tutorial will guide you through turning your BadgerStick into a micro gaming system. Remember the game [Breakout](http://en.wikipedia.org/wiki/Breakout_%28video_game%29)? Let\'s make a Breakout clone on our BadgerStick by adding a joystick and some buttons!

[![Breakout on the Badger](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-42.jpg)

**NOTE:** The BadgerStick and RedStick are two different products. The BadgerStick (aka BadgerHack) originated as an event-only platform to aid SparkFun in teaching soldering and programming at events like Maker local Faires and SXSW. The [RedStick](https://www.sparkfun.com/products/13741) evolved from that concept and is the retail version of the BadgerStick, available for sale on SparkFun.com. All of the BadgerStick tutorials and expansion kits are compatible with both the BadgerStick and the RedStick, unless otherwise stated.

#### Required Materials

We will need a few other components to make a simple controller for the BadgerStick.

\

### Suggested Reading

Before starting this tutorial, we highly recommend you work through the main BadgerHack guide first.

[](https://learn.sparkfun.com/tutorials/badgerhack)

### BadgerHack 

September 23, 2015

This tutorial shows users how to solder their SparkFun interactive badges as well as put them to use in other projects.

Additionally, if you are new to soldering or electronics, we recommend you check out the following:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

When you are ready to start hacking your badge, we definitely recommend reading:

- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

## Hardware Hookup

To begin, snap off 15 pins from the break-away headers, and solder them to the through-holes on the side opposite the LED array of the BadgerStick.

[![Solder pins to the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-29.jpg)

Solder the Thumb Joystick to the Thumb Joystick Breakout board.

[![Solder joystick to breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-30.jpg)

Snap off 5 pins from the break-away headers, and solder them to the through-holes on the Joystick Breakout Board.

[![Solder pins to joystick breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-31.jpg)

#### Connections

Place the **BadgerStick** in the breadboard with pin **10** in position **i13** and pin **5V** in position **i27**.

Connect the rest of the components as follows:

+---------------------------+--------------------------------------------+
| Component                 | Breadboard                                 |
+===========================+==========+===========+==========+==========+
| Thumb Joystick Breakout\* | i7 (VCC) | i6 (VERT) | i5 (HOR) | i3 (GND) |
+---------------------------+----------+-----------+----------+----------+
| Pushbutton                | c20      | c22       | f20      | f22      |
+---------------------------+----------+-----------+----------+----------+
| Pushbutton                | c28      | c30       | f28      | f30      |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | ( - )    | g30       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | ( - )    | g25       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | ( - )    | g22       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | ( - )    | j3        |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | j7       | g23       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | j6       | g18       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | j5       | g17       |          |          |
+---------------------------+----------+-----------+----------+----------+
| Jumper Wire               | g21      | g28       |          |          |
+---------------------------+----------+-----------+----------+----------+

*\* Pins not listed are not used.*\

[![Gaming Badger Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/breakout_fritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/breakout_fritzing.png)

*Wire colors correspond to the colors of the table above.*

**IMPORTANT:** You can leave the battery pack soldered into the BadgerStick if you desire. If you remove the battery pack, you will need to supply power through another means, such as a USB port or a [USB extension cable](https://www.sparkfun.com/products/517).

You should now have a makeshift game controller with a tiny LED screen!

[![Gaming badger with batteries](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-38.jpg)

## The Code

Plug the USB side of your BadgerStick into your computer. Make sure \"BadgerStick\" and the associated COM port are selected in the Arduino IDE, and click upload.

    language:c
    /**
     * BadgerHack Breakout
     * Shawn Hymel @ SparkFun Electronics
     * September 23, 2015
     * 
     * A clone of the famous "Breakout" game on the BadgerHack platform. Use the
     * joystick to move the paddle and try to knock out the upper pixels with the
     * ball.
     * 
     * License: http://opensource.org/licenses/MIT
     * 
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

    #include <SparkFun_LED_8x7.h>
    #include <Chaplex.h>

    // Constants
    #define DEBUG                1
    #define FPS                  60
    #define SENSITIVITY          100
    #define MAX_X_SPAN           127
    #define PADDLE_SIZE          2
    #define INITIAL_BALL_SPEED   0.1
    #define BALL_SPEED_INC       0.004
    #define PAUSE_BEFORE_SHOOT   1000    // ms
    #define ROW_SIZE             7
    #define COL_SIZE             8
    #define FIELD_SIZE           ROW_SIZE * COL_SIZE

    // Pin definitions
    #define RNG_SEED_PIN  2
    #define X_PIN         0
    #define Y_PIN         1
    #define BUTTON_1_PIN  3
    #define BUTTON_2_PIN  4

    // Global variables
    byte led_pins[] = ; // Pins for LEDs
    uint16_t horz_zero;
    uint16_t vert_zero;
    uint8_t paddle_size;

    // Setup
    void setup() 

    // Loop - play the game forever
    void loop() 

    /****************************************************************
     * Functions
     ***************************************************************/

    // Play the game
    void playGame() ;
    #if DEBUG
      Serial.println("New game!");
      Serial.print("Field span: ");
      Serial.println(field_max);
    #endif

      // Note when we start the game (so we can shoot the ball)
      game_start = millis();
      ball_moving = false;

      // Assign an initial direction and speed to the ball
      ball_theta = initBallTheta();
      ball_speed = INITIAL_BALL_SPEED;

      // Play the game until we win or lose
      playing = true;
      while ( playing ) 
        }
        if ( win ) 

        // Read the value of the joystick and map to a movement
        paddle_move = analogRead(X_PIN) - horz_zero;
        paddle_move = paddle_move / SENSITIVITY;
    #if 0
        Serial.print("Moving: ");
        Serial.println(paddle_move);
    #endif

        // Move the paddle and calculate its real x position
        paddle_field = paddle_field + paddle_move;
        if ( paddle_field <= 0 ) 
        if ( paddle_field >= field_max ) 
        paddle_x = map(paddle_field, 0, field_max,
                       0, 6 - (paddle_size - 1));

        // If the ball has been shot, move it
        if ( ball_moving ) 

          // Allow ball to be deflected once it leaves paddle range
          if ( ball_y <= 6 ) 

          // Check if the ball moved past the paddle (lose)
          if ( ball_y > 7 ) 

          // Check the ball against the walls (and bounce!)
          if ( ball_y < 0 ) 
          if ( ball_x < 0 ) 
          if ( ball_x > 6 ) 

          // Bounce if we hit a block above the ball
          i = (floor(ball_y) * ROW_SIZE) + roundFloat(ball_x);
          if ( the_wall[i] > 0 ) 

          // Bounce if we hit a block below the ball
          i = (ceil(ball_y) * ROW_SIZE) + roundFloat(ball_x);
          if ( the_wall[i] > 0 ) 

          // Bounce if we hit a block to the left the ball
          i = (roundFloat(ball_y) * ROW_SIZE) + floor(ball_x);
          if ( the_wall[i] > 0 ) 

          // Bounce if we hit a block to the right the ball
          i = (roundFloat(ball_y) * ROW_SIZE) + ceil(ball_x);
          if ( the_wall[i] > 0 ) 

        } else 
        }

        // Round the ball's position to the nearest pixel
        ball_round_x = roundFloat(ball_x);
        ball_round_y = roundFloat(ball_y);

        // Draw tbe wall, the paddle, and the ball
        Plex.clear();

        for ( y = 0; y < COL_SIZE; y++ ) 
          }
        }
        for ( i = 0; i < paddle_size; i++ ) 
        Plex.pixel(ball_round_y, map(ball_round_x, 0, 6, 6, 0));
        Plex.display();

        // Wait until we reach our target end of frame
        while ( millis() < frame_start + millis_per_frame ) 
     #if 0
       Serial.print("FPS: ");
       Serial.println( 1000 / (millis() - frame_start) );
     #endif

      }
    }

    // Create a randomized ball launch angle
    unsigned int initBallTheta()  else 

    #if DEBUG
      Serial.print(" Theta:");
      Serial.println(theta);
    #endif

      return theta;
    }

    // Rounds a floating value to an integer
    int roundFloat(float x) 
      return (int) (x - 0.5);
    }

## Play

Once the sketch has been uploaded, prepare to play!

Use the joystick to move the paddle back and forth to bounce the ball. You win when you \"break\" all the lights on the top part of the screen. You lose if you let the ball go past your paddle.

[![Let\'s play Breakout!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/Badgerhack_Hookup_Guide-42.jpg)