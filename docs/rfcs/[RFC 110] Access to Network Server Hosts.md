---
rfc: 110
title: "Access to Network Server Hosts"
date: March 1971
---
1. character escape $NOT [1]
2. system escape     |
3. character delete  @
4. line delete      $CENT [1]
5. logical linend    #

For the 7 ASCII graphics not on a 2741 terminal, the following
character escape and graphic pairs are recommended:

```
      $NOT <           to translate to         [
      $NOT >           to translate to         ]
      $NOT (           to translate to         {
      $NOT )           to translate to         }
      $NOT "           to translate to         ^
      $NOT /           to translate to         \
      $NOT '           to translate to         `

```

To permit the special function characters to be keyed, the following
character escape and graphic pairs are recommended:

```
      $NOT -           to translate to        $NOT
      $NOT :           to translate to         |
      $NOT ,           to translate to         @
      $NOT .           to translate to        $CENT
      $NOT =           to translate to         #

```

To key in the ASCII control codes, it is recommended that the
character escape followed by two letters be used to specify a control
code.  These two letters are derived from the mnemonic name of the
ASCII control function and are as follows:

```
      $NOT AC          to translate to         ACK             X'06'
      $NOT BE          to translate to         BEL             X'07'
      $NOT BS          to translate to         BS              X'08'
      $NOT CA          to translate to         CAN             X'18'
      $NOT CR          to translate to         CR              X'0D'
      $NOT D1          to translate to         DC1             X'11'
      $NOT D2          to translate to         DC2             X'12'
      $NOT D3          to translate to         DC3             X'13'
      $NOT D4          to translate to         DC4             X'14'
      $NOT DE          to translate to         DEL             X'7F'
      $NOT DL          to translate to         DLE             X'10'
      $NOT EM          to translate to         EM              X'19'
      $NOT EN          to translate to         ENQ             X'05'
      $NOT EO          to translate to         EOT             X'04'
      $NOT ES          to translate to         ESC             X'1B'
      $NOT EB          to translate to         ETB             X'17'
      $NOT EX          to translate to         ETX             X'03'
      $NOT FF          to translate to         FF              X'0C'
      $NOT FS          to translate to         FS              X'1C'
      $NOT GS          to translate to         GS              X'1D'
      $NOT HT          to translate to         HT              X'09'
      $NOT LF          to translate to         LF              X'0A'
      $NOT NA          to translate to         NAK             X'15'
      $NOT NU          to translate to         NUL             X'00'
      $NOT RS          to translate to         RS              X'1E'
      $NOT SI          to translate to         SI              X'0F'
      $NOT SO          to translate to         SO              X'0E'
      $NOT SH          to translate to         SOH             X'01'
      $NOT SP          to translate to         SP              X'20'
      $NOT ST          to translate to         STX             X'02'
      $NOT SU          to translate to         SUB             X'1A'
      $NOT SY          to translate to         SYN             X'16
      $NOT US          to translate to         US              X'1F'
      $NOT VT          to translate to         VT              X'0B'

```

Note that the controls SP, BS, and HT can be specified using the
character escape character or directly by keying the appropriate key
on a 2741 terminal.

Endnote

[1] The following identifiers are substituted for graphics not in
ASCII:

```
         $CENT   Cent sign
         $NOT    Logical NOT ("bent bar")

   See the PDF version of this document for graphics that cannot be
   represented in ASCII format.

          [This RFC was put into machine readable form for entry]
          [into the online RFC archives by Lorrie Shiota, 10/02]

```