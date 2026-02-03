# Making Remote Procedure Calls From Scripts

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# Making Remote Procedure Calls From Scripts
Starting with OS X version 10.1, the Apple Event Manager provides support for using the XML-RPC and SOAP protocols to make remote procedure calls from AppleScript scripts and from applications. This chapter provides sample scripts that show how to make remote procedure calls from scripts.
This chapter assumes you are familiar with the material inIntroduction to XML-RPC and SOAP Programming Guide. To test any of the scripts shown in this chapter, you must have an Internet connection.
Warning:The script examples in this chapter may not work because the web services they rely on may no longer be available. You can find additional script samples that make use of web services at/Library/Scripts/Internet Services. For example, theStock Quotescript uses a web service to look up the price for a stock specified by its symbol, while theCurrent Temperature by Zipcodescript looks up the temperature for a specified Zip code.

## Scripting an XML-RPC Call
To make an XML-RPC request from a script, you use the AppleScript termcall xmlrpc. The syntax for this term is described inXML-RPC Script Statements. You can find available XML-RPC services at sites such as XMethods athttp://www.xmethods.net/. There you can also find information about the parameters and return values for remote procedure calls to these services.
Listing 3-1shows a script that prompts a user for text, makes an XML-RPC request to an Internet server to check the spelling for that text, prompts the user to correct any words that may have been misspelled, and displays the final text.
Listing 2-1A script that makes an XML-RPC request to check the spelling of a text phrase.
```
---- Main script ----------------------------------------```
```
-- Supply default text to spell check.```
```
set spellCheckText to "My frst naem is John"```
```
 ```
```
----Query user for different text to check.```
```
set dialogResult to display dialog Â¬```
```
    "Enter a phrase to spell check:" default answer spellCheckText```
```
 ```
```
if button returned of dialogResult is "OK" then```
```
    set spellCheckText to text returned of dialogResult```
```
    -- Call spellCheck handler.```
```
    set resultList to spellCheck(spellCheckText)```
```
    (*```
```
    The returned data looks something like this:```
```
        {{suggestions:{"fast", "fest", "first", "fist", "Forst",```
```
        "frat", "fret", "frist", "frit", "frost", "frot", "fust"},```
```
        location:4, |word|:"frst"}, {suggestions:{"haem", "na em",```
```
        "na-em", "naam", "nae", "nae m", "nae-m", "nael", "Naim",```
```
        "nam", "name", "neem"}, location:9, |word|:"naem"}}```
```
    *)```
```
    -- Make list of words to spellcheck.```
```
    set wordList to every word of spellCheckText```
```
 ```
```
    -- Give user chance to correct each misspelled word.```
```
    repeat with eachItem in resultList```
```
        set newWord to choose from list suggestions of eachItem Â¬```
```
            with prompt "You misspelled \"" & |word| of eachItem & Â¬```
```
            "\"" without multiple selections allowed```
```
 ```
```
        -- If user selected a corrected word, insert it into list```
```
        if (newWord as string) is not equal to "false" then```
```
            set wordIndex to Â¬```
```
                findIt(every word of spellCheckText, location of eachItem)```
```
            copy newWord to item wordIndex of wordList```
```
        end if```
```
    end repeat```
```
 ```
```
    -- Display corrected text.```
```
    set spellCheckText to ""```
```
    repeat with oneWord in wordList```
```
        set spellCheckText to spellCheckText & oneWord & " "```
```
    end repeat```
```
 ```
```
    display dialog "Corrected text: " & spellCheckText```
```
end if```
```
 ```
```
-- spellCheck handler ------------------------------------------```
```
-- This handler makes the remote procedure call.```
```
on spellCheck(sentence)```
```
    tell application "http://www.stuffeddog.com/speller/speller-rpc.cgi"```
```
        return call xmlrpc {method name:"speller.spellCheck", Â¬```
```
        parameters:sentence}```
```
    end tell```
```
end spellCheck```
```
 ```
```
 ```
```
-- findIt handler ------------------------------------```
```
-- The "textList" parameter is a list of the words in the original text.```
```
-- The "index" parameter is the character index of a misspelled word.```
```
-- This handler returns the word at that index.```
```
-- For example, the misspelled word at character index four is "frst".```
```
--      Its word index is 2 (the 2nd word in the original text).```
```
on findIt(textList, index)```
```
    set curLength to 0```
```
    set ixWord to 1```
```
 ```
```
    repeat with oneWord in textList```
```
        set curLength to curLength + (length of oneWord) + 1```
```
        if curLength â¥ index then```
```
            exit repeat```
```
        end if```
```
        set ixWord to ixWord + 1```
```
    end repeat```
```
    log ixWord```
```
    return ixWord```
```
end findIt```
This script has a main section and two handlers. In the main section, it performs the following actions:
- It sets a default text string to be checked.
It sets a default text string to be checked.
- It displays a dialog that prompts the user to enter different text.
It displays a dialog that prompts the user to enter different text.
- If the user accepts the dialog, it calls thespellCheckhandler to check the spelling. That handler, described below, contains the only script statements needed to make a remote procedure call to a spell-checking server.The handler returns a list that contains, for each misspelled word, a list of suggested corrections, the character location of the word in the text, and the misspelled word itself. The returned list looks something like this:The returned data looks something like this:{{suggestions:{"fast", "fest", "first", "fist", "Forst","frat", "fret", "frist", "frit", "frost", "frot", "fust"},location:4, |word|:"frst"}, {suggestions:{"haem", "na em","na-em", "naam", "nae", "nae m", "nae-m", "nael", "Naim","nam", "name", "neem"}, location:9, |word|:"naem"}}Note that this is not the raw data returned from the remote procedure call. Rather, the Apple Event Manager has interpreted the XML returned by the procedure call and built an Apple event to encapsulate it. This list of records is the result. Becausewordis a reserved word in AppleScript, it is enclosed in vertical bars (|word|) when used as an identifier (in this case as a label in a record).
If the user accepts the dialog, it calls thespellCheckhandler to check the spelling. That handler, described below, contains the only script statements needed to make a remote procedure call to a spell-checking server.
The handler returns a list that contains, for each misspelled word, a list of suggested corrections, the character location of the word in the text, and the misspelled word itself. The returned list looks something like this:
```
The returned data looks something like this:```
```
        {{suggestions:{"fast", "fest", "first", "fist", "Forst",```
```
        "frat", "fret", "frist", "frit", "frost", "frot", "fust"},```
```
        location:4, |word|:"frst"}, {suggestions:{"haem", "na em",```
```
        "na-em", "naam", "nae", "nae m", "nae-m", "nael", "Naim",```
```
        "nam", "name", "neem"}, location:9, |word|:"naem"}}```
Note that this is not the raw data returned from the remote procedure call. Rather, the Apple Event Manager has interpreted the XML returned by the procedure call and built an Apple event to encapsulate it. This list of records is the result. Becausewordis a reserved word in AppleScript, it is enclosed in vertical bars (|word|) when used as an identifier (in this case as a label in a record).
- For each word (if any) in the returned list of misspelled words, it lets the user choose a correction (using the standard scripting additionchoose from list).It then calls thefindIthandler to find the location of the misspelled word in the text phrase and replaces it with the user choice.
For each word (if any) in the returned list of misspelled words, it lets the user choose a correction (using the standard scripting additionchoose from list).
It then calls thefindIthandler to find the location of the misspelled word in the text phrase and replaces it with the user choice.
- It displays the corrected text (possibly the same as the original text, if no corrections were made).
It displays the corrected text (possibly the same as the original text, if no corrections were made).
ThespellCheckhandler contains the one and only statement in the script that makes a remote procedure call. It performs the following operations:
- It uses a Tell statement to identify the location of the remote XML-RPC server (http://www.stuffeddog.com/speller/speller-rpc.cgi).
It uses a Tell statement to identify the location of the remote XML-RPC server (http://www.stuffeddog.com/speller/speller-rpc.cgi).
- It uses the AppleScript termcall xmlrpcto make the remote procedure call, specifying the method name (speller.spellCheck) and passing the specified text for the single parameter.
It uses the AppleScript termcall xmlrpcto make the remote procedure call, specifying the method name (speller.spellCheck) and passing the specified text for the single parameter.
- It returns the result of the remote procedure call. That consists of a list that contains, for each misspelled word, a list of suggested corrections, the location of the word in the text, and the misspelled word itself.
It returns the result of the remote procedure call. That consists of a list that contains, for each misspelled word, a list of suggested corrections, the location of the word in the text, and the misspelled word itself.
Note that AppleScript, working through the Apple Event Manager, did all the work of formatting thecall xmlrpcscript statement into proper XML, opening a connection to the specified server, sending the message, waiting for a reply, formatting the returned XML into an Apple event, and returning the event.
ThefindIthandler merely returns the word position in the original text of the word that corresponds to the passed character index of a misspelled word (returned by the remote procedure handler). For example, the character index of the first misspelled word (frst) is 4. That word is the second word in the original text, sofinditwould return the value 2.
For a script that shows a more flexible type of handler and includes error handling, seeListing 3-3.

## Scripting a SOAP Request
To make a SOAP request from a script, you use the AppleScript termcall soap. The syntax for these calls is described inSOAP Script Statements. You can find available SOAP services at sites such as XMethods athttp://www.xmethods.net/. There you can also find information about the parameters and return values for SOAP requests to these services.

### A Simple Translation Script
Listing 3-2shows a script that prompts a user for text, makes a SOAP request to an Internet server to translate that text to French, and displays the translated text.
Listing 2-2A simple script that calls a SOAP translation server.
```
---- Main script ----------------------------------------```
```
-- Supply default text to translate.```
```
set defaultText to "The spirit is willing but the mind is weak"```
```
 ```
```
--Display dialog and let user type different text to translate.```
```
display dialog "Enter the text to translate into French:" Â¬```
```
    default answer defaultText```
```
set this_text to the text returned of the result```
```
 ```
```
-- Call translation handler```
```
set the new_text to translate("en_fr", this_text)```
```
 ```
```
--Show translated text and allow user to copy it to Clipboard.```
```
display dialog new_text buttons {"Clipboard", "OK"} default button 2```
```
if the button returned of the result is "Clipboard" then```
```
    set the clipboard to new_text```
```
end if```
```
 ```
```
-- translate handler ------------------------------------------```
```
-- This handler makes the SOAP request.```
```
on translate(direction, theText)```
```
    tell application "http://services.xmethods.net:80/perl/soaplite.cgi"```
```
        return call soap {method name:"BabelFish", Â¬```
```
        method namespace uri:"urn:xmethodsBabelFish", Â¬```
```
        parameters:{translationmode:direction as string, Â¬```
```
        sourcedata:theText as string}, Â¬```
```
        SOAPAction:"urn:xmethodsBabelFish#BabelFish"}```
```
    end tell```
```
end translate```
This script starts has a main section and one handler to make the translation SOAP request. In the main section, it performs the following actions:
- It sets a default text string to be translated from English to French.
It sets a default text string to be translated from English to French.
- It displays a dialog that prompts the user to enter different text.
It displays a dialog that prompts the user to enter different text.
- It calls thetranslatehandler to translate the text. That handler, described below, contains the only script statements needed to make a SOAP request to a translation server.The handler returns the translated text.
It calls thetranslatehandler to translate the text. That handler, described below, contains the only script statements needed to make a SOAP request to a translation server.
The handler returns the translated text.
- It displays the translated text and allows the user to copy it to the Clipboard.
It displays the translated text and allows the user to copy it to the Clipboard.
Thetranslatehandler contains the one and only statement in the script that makes a SOAP request. It performs the following operations:
- It uses a Tell statement to identify the location of the remote SOAP server (http://services.xmethods.net:80/perl/soaplite.cgi).
It uses a Tell statement to identify the location of the remote SOAP server (http://services.xmethods.net:80/perl/soaplite.cgi).
- It uses the AppleScript termcall soapto make the SOAP request. You can obtain certain values you need to make a SOAP request from the service itself. In this example, the call includes the following:method name:"BabelFish"specifies the required method namemethod namespace uri:"urn:xmethodsBabelFish"specifies the required method namespace URIparameters:{translationmode:direction as string, sourcedata:theText as string}specifies the parameter names and the values to pass for those parameters; a method may have no parametersSOAPAction:"urn:xmethodsBabelFish#BabelFish"specifies the required SOAPAction value
It uses the AppleScript termcall soapto make the SOAP request. You can obtain certain values you need to make a SOAP request from the service itself. In this example, the call includes the following:
- method name:"BabelFish"specifies the required method name
method name:"BabelFish"specifies the required method name
- method namespace uri:"urn:xmethodsBabelFish"specifies the required method namespace URI
method namespace uri:"urn:xmethodsBabelFish"specifies the required method namespace URI
- parameters:{translationmode:direction as string, sourcedata:theText as string}specifies the parameter names and the values to pass for those parameters; a method may have no parameters
parameters:{translationmode:direction as string, sourcedata:theText as string}specifies the parameter names and the values to pass for those parameters; a method may have no parameters
- SOAPAction:"urn:xmethodsBabelFish#BabelFish"specifies the required SOAPAction value
SOAPAction:"urn:xmethodsBabelFish#BabelFish"specifies the required SOAPAction value
- It returns the result of the SOAP request. That consists of a text string that contains the translated text.
It returns the result of the SOAP request. That consists of a text string that contains the translated text.
Note that AppleScript, working through the Apple Event Manager, did all the work of formatting thecall soapscript statement into proper XML, opening a connection to the specified server, sending the message, waiting for a reply, formatting the returned XML into an Apple event, and returning the event.

### A More Complex Translation Script
The script inListing 3-3performs the same task as the script inListing 3-2, translating an English phrase to French. However, it is more flexible and sophisticated in several ways:
- It turns the translation handler into a flexible SOAP request routine that can call different SOAP servers and different methods depending on the parameters passed to it.
It turns the translation handler into a flexible SOAP request routine that can call different SOAP servers and different methods depending on the parameters passed to it.
- It uses error handling in the SOAP request handler and sets a boolean parameter value so that the caller can check for success. The main script checks that parameter and displays an error message if the SOAP request was unsuccessful.
It uses error handling in the SOAP request handler and sets a boolean parameter value so that the caller can check for success. The main script checks that parameter and displays an error message if the SOAP request was unsuccessful.
- The main script also shows how to use atryblock to handle errors. In this case, it checks for errors while displaying a dialog: for any returned error number except -128 (the user cancelled), it beeps.
The main script also shows how to use atryblock to handle errors. In this case, it checks for errors while displaying a dialog: for any returned error number except -128 (the user cancelled), it beeps.
- It defines property values to make the script more readable and easier to modify.
It defines property values to make the script more readable and easier to modify.
Listing 2-3A more detailed script that calls a SOAP translation server.
```
-- Use properties to store default values.```
```
property SOAP_app : "http://services.xmethods.net:80/perl/soaplite.cgi"```
```
property method_name : "BabelFish"```
```
property method_namespace_URI : "urn:xmethodsBabelFish"```
```
property SOAP_action : "urn:xmethodsBabelFish#BabelFish"```
```
property English_to_French : "en_fr"```
```
 ```
```
---- Main script ----------------------------------------```
```
--Query user for text to translate.```
```
set this_text to "Hello my friend!"```
```
repeat```
```
    try```
```
        display dialog Â¬```
```
            "Enter the text to translate into French:" Â¬```
```
            default answer this_text```
```
        set this_text to the text returned of the result```
```
        if this_text is not "" then```
```
            set this_text to this_text as string```
```
            exit repeat```
```
        end if```
```
    on error number error_number```
```
        -- Don't show error if user just cancelled.```
```
        if the error_number is -128 then error number -128```
```
        beep```
```
    end try```
```
end repeat```
```
 ```
```
-- Create the parameter record.```
```
set the method_parameters to {translationmode:English_to_French, Â¬```
```
     sourcedata:this_text}```
```
 ```
```
-- Call the SOAP handler.```
```
copy my SOAP_call(SOAP_app, method_name, Â¬```
```
    method_namespace_URI, method_parameters, SOAP_action) Â¬```
```
    to {call_indicator, call_result}```
```
 ```
```
-- Check for error return from SOAP handler.```
```
if the call_indicator is false then```
```
    beep```
```
    display dialog "An error occurred." & return & return Â¬```
```
        & call_result buttons {"Cancel"} default button 1```
```
else```
```
    --Show translated text and allow user to copy it to Clipboard.```
```
    display dialog call_result buttons {"Clipboard", "OK"} Â¬```
```
        default button 2```
```
    if the button returned of the result is "Clipboard" then```
```
        set the clipboard to the call_result```
```
    end if```
```
end if```
```
 ```
```
-- SOAP translation handler ------------------------------```
```
on SOAP_call(SOAP_app, method_name, Â¬```
```
    method_namespace_URI, method_parameters, SOAP_action)```
```
    try```
```
        using terms from application "http://www.apple.com/placebo"```
```
            tell application SOAP_app```
```
                set this_result to call soap Â¬```
```
                    {method name:method_name Â¬```
```
                        , method namespace uri:method_namespace_URI Â¬```
```
                        , parameters:method_parameters Â¬```
```
                        , SOAPAction:SOAP_action}```
```
            end tell```
```
        end using terms from```
```
        return {true, this_result}```
```
    on error error_message```
```
        return {false, error_message}```
```
    end try```
```
end SOAP_call```
Copyright © 2001, 2014 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2014-07-15