# Source: https://learn.sparkfun.com/tutorials/ascii

## Introduction

If computers operate in binary, then how are we able to store letters and words? To do this, we assign numbers to characters. This is known as [character encoding](https://en.wikipedia.org/wiki/Character_encoding).

[![Example of ASCII encoding](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/9/ASCII_Text_Doc.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/9/ASCII_Text_Doc.png)

*Looking at the internals of a simple text document*

To understand how character encoding works, let\'s create a simple example. First, assign the numbers 1-26 to the English alphabet:

    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

To write a simple encoded message, we substitute the numbers for the letters. For example, `8 5 12 12 15`. By using numbers, we have constructed the word `h e l l o`.

But to completely capture the English alphabet \-- including upper and lower-case letters, numbers, and punctuation \-- we needed more than 26 characters. As a result, the **American Standard Code for Information Interchange (ASCII)** was created as one of the first character encoding standards for computers.

### What You Will Learn

The following topics will be covered in this tutorial:

- A brief history of ASCII
- How to translate decimal, binary, and hexadecimal numbers to ASCII

### Suggested Reading

There are a few concepts that you might want to be familiar with before starting to read this guide:

- [Binary](https://learn.sparkfun.com/tutorials/binary) - Knowing how a computer stores numbers is useful to translating those numbers to characters.
- [Hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal) - Hexadecimal is often used to express binary numbers in groups of 4 bits.
- [Installing Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide) - Arduino is a good way to try printing ASCII characters.

## History

The American Standards Association (ASA), now the American National Standards Institute (ANSI), began work on ASCII on October 6, 1960. The encoding scheme had origins in the 5-bit telegraph codes invented by [Émile Baudot](https://en.wikipedia.org/wiki/%C3%89mile_Baudot). The committee eventually decided on a 7-bit code for ASCII.

7 bits allow for 128 characters. While only American English characters and symbols were chosen for this encoding set, 7 bits meant minimized costs associated with transmitting this data (as opposed to say, 8 bits).

The first 32 characters of ASCII were reserved control characters. These characters were used to relay special instructions to other devices, like printers. For example, a user could advance a line, delete a character, and on some devices, ring a bell (such as on the [Teletype Model 33](https://en.wikipedia.org/wiki/Teletype_Model_33) ASR).

ASA published the first version of ASCII in 1963 and revised it in 1967. The last major update to the standard occurred in 1986. ASCII first saw commercial use in the American Telephone & Telegraph (AT&T) TeletypeWriter Exchange (TWX) network.

[![Teletype Model 33 ASR](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/9/ASR-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/9/ASR-33.jpg)

*Teleprinters, like this Teletype Model 33 ASR, were used to send typed messages to one or more other teleprinters across various communication channels (Image courtesy of [Arnold Reinhold of Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ASR-33_at_CHM.agr.jpg))*

On March 11, 1968 President Lyndon B. Johnson mandated that all US federal government computers must support ASCII, thus cementing ASCII\'s place in American computing history.

Other encoding schemes existed at the time, such as the [International Telegraph Alphabet No. 2](https://en.wikipedia.org/wiki/Baudot_code#ITA2) (ITA2), but ASCII quickly became the standard for American English encoding. ASCII was the most common encoding found on the Internet until it was surpassed by UTF-8 in 2007.

## ASCII Table

To identify a character\'s ASCII value, it is common to look it up on an ASCII table. The ASCII table pairs each character to its assigned value between 0 and 127.

### Control Characters

Control characters make up the first 32 characters of the ASCII table. These characters are not intended to be printed, instead they are used to send command instructions to another device, such as a printer. Note that we have included the [octal](https://en.wikipedia.org/wiki/Octal) representation of the ASCII characters in the off chance that you might be working with a particularly old system (such as the 12-bit [PDP-8](https://en.wikipedia.org/wiki/PDP-8)).

  Dec   Bin         Oct   Hex   Char   Description
  ----- ----------- ----- ----- ------ ---------------------------
  0     0000 0000   000   00    NUL    null
  1     0000 0001   001   01    SOH    start of heading
  2     0000 0010   002   02    STX    start of text
  3     0000 0011   003   03    ETX    end of text
  4     0000 0100   004   04    EOT    end of transmission
  5     0000 0101   005   05    ENQ    enquiry
  6     0000 0110   006   06    ACK    acknowledge
  7     0000 0111   007   07    BEL    bell
  8     0000 1000   010   08    BS     backspace
  9     0000 1001   011   09    TAB    horizontal tab
  10    0000 1010   012   0A    LF     line feed, new line
  11    0000 1011   013   0B    VT     vertical tab
  12    0000 1100   014   0C    FF     form feed, new page
  13    0000 1101   015   0D    CR     carriage return
  14    0000 1110   016   0E    SO     shift out
  15    0000 1111   017   0F    SI     shift in
  16    0001 0000   020   10    DLE    data link escape
  17    0001 0001   021   11    DC1    device control 1
  18    0001 0010   022   12    DC2    device control 2
  19    0001 0011   023   13    DC3    device control 3
  20    0001 0100   024   14    DC4    device control 4
  21    0001 0101   025   15    NAK    negative acknowledge
  22    0001 0110   026   16    SYN    synchronous idle
  23    0001 0111   027   17    ETB    end of transmission block
  24    0001 1000   030   18    CAN    cancel
  25    0001 1001   031   19    EM     end of medium
  26    0001 1010   032   1A    SUB    substitute
  27    0001 1011   033   1B    ESC    escape
  28    0001 1100   034   1C    FS     file separator
  29    0001 1101   035   1D    GS     group separator
  30    0001 1110   036   1E    RS     record separator
  31    0001 1111   037   1F    US     unit separator
  127   0111 1111   177   7F    DEL    delete

### Printable Characters

There are 95 printable characters in the ASCII encoding scheme. Note that the \"space\" character denotes a printable space (\" \").

  Dec   Bin         Oct   Hex   Char
  ----- ----------- ----- ----- -------
  32    0010 0000   040   20    space
  33    0010 0001   041   21    !
  34    0010 0010   042   22    \"
  35    0010 0011   043   23    \#
  36    0010 0100   044   24    \$
  37    0010 0101   045   25    \%
  38    0010 0110   046   26    &
  39    0010 0111   047   27    \'
  40    0010 1000   050   28    (
  41    0010 1001   051   29    )
  42    0010 1010   052   2A    \*
  43    0010 1011   053   2B    \+
  44    0010 1100   054   2C    ,
  45    0010 1101   055   2D    \-
  46    0010 1110   056   2E    .
  47    0010 1111   057   2F    /
  48    0011 0000   060   30    0
  49    0011 0001   061   31    1
  50    0011 0010   062   32    2
  51    0011 0011   063   33    3
  52    0011 0100   064   34    4
  53    0011 0101   065   35    5
  54    0011 0110   066   36    6
  55    0011 0111   067   37    7
  56    0011 1000   070   38    8
  57    0011 1001   071   39    9
  58    0011 1010   072   3A    :
  59    0011 1011   073   3B    ;
  60    0011 1100   074   3C    \<
  61    0011 1101   075   3D    =
  62    0011 1110   076   3E    \>
  63    0011 1111   077   3F    ?

  Dec   Bin         Oct   Hex   Char
  ----- ----------- ----- ----- ------
  64    0100 0000   100   40    @
  65    0100 0001   101   41    A
  66    0100 0010   102   42    B
  67    0100 0011   103   43    C
  68    0100 0100   104   44    D
  69    0100 0101   105   45    E
  70    0100 0110   106   46    F
  71    0100 0111   107   47    G
  72    0100 1000   110   48    H
  73    0100 1001   111   49    I
  74    0100 1010   112   4A    J
  75    0100 1011   113   4B    K
  76    0100 1100   114   4C    L
  77    0100 1101   115   4D    M
  78    0100 1110   116   4E    N
  79    0100 1111   117   4F    O
  80    0101 0000   120   50    P
  81    0101 0001   121   51    Q
  82    0101 0010   122   52    R
  83    0101 0011   123   53    S
  84    0101 0100   124   54    T
  85    0101 0101   125   55    U
  86    0101 0110   126   56    V
  87    0101 0111   127   57    W
  88    0101 1000   130   58    X
  89    0101 1001   131   59    Y
  90    0101 1010   132   5A    Z
  91    0101 1011   133   5B    \[
  92    0101 1100   134   5C    \\
  93    0101 1101   135   5D    \]
  94    0101 1110   136   5E    \^
  95    0101 1111   137   5F    \_

  Dec   Bin         Oct   Hex   Char
  ----- ----------- ----- ----- ------
  96    0110 0000   140   60    \`
  97    0110 0001   141   61    a
  98    0110 0010   142   62    b
  99    0110 0011   143   63    c
  100   0110 0100   144   64    d
  101   0110 0101   145   65    e
  102   0110 0110   146   66    f
  103   0110 0111   147   67    g
  104   0110 1000   150   68    h
  105   0110 1001   151   69    i
  106   0110 1010   152   6A    j
  107   0110 1011   153   6B    k
  108   0110 1100   154   6C    l
  109   0110 1101   155   6D    m
  110   0110 1110   156   6E    n
  111   0110 1111   157   6F    o
  112   0111 0000   160   70    p
  113   0111 0001   161   71    q
  114   0111 0010   162   72    r
  115   0111 0011   163   73    s
  116   0111 0100   164   74    t
  117   0111 0101   165   75    u
  118   0111 0110   166   76    v
  119   0111 0111   167   77    w
  120   0111 1000   170   78    x
  121   0111 1001   171   79    y
  122   0111 1010   172   7A    z
  123   0111 1011   173   7B    
  126   0111 1110   176   7E    \~

## Try It

If you would like to try printing something using ASCII encoding, you can try it out using Arduino. See [this tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) for getting started with Arduino.

Open the Arduino IDE and paste in the following code:

    language:c
    void setup() 
    

    void loop() 
    

Run it on your Arduino, and open a Serial console. You should see the \"Hello!\" appear over and over:

[![Arduino saying Hello!](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/9/Arduino_Hello.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/9/Arduino_Hello.png)

Notice that we had to use `Serial.write()` instead of `Serial.print()`. The `write()` command sends a raw byte across the serial line. `print()`, on the other hand, will try and interpret the number and send the ASCII-encoded version of that number. For example, `Serial.print(0x48)` would print `72` in the console.

Also, notice that we used the ASCII character `0x0A`, which is the \"line feed\" control character. This causes the printer (or console in this case) to advance to the next line. It is similar to pressing the \'enter\' key.