# Source: https://docs.avaamo.com/user-guide/ref/speech-synthesis-markup-language-ssml.md

# Supported SSML tags

**Speech Synthesis Markup Language** (**SSML**) is an XML-based markup language for speech synthesis applications. It is a recommendation of the W3C's voice browser working group. SSML is often embedded in VoiceXML scripts to drive interactive telephony systems. See [Speech Synthesis Markup Language (SSML) Version 1.1](https://www.w3.org/TR/speech-synthesis11/), for more information.

Avaamo Platform provides all the standard SSML tags out-of-the-box as per the W3C specifications. You can add these tags in your agent responses to build a conversational flow for your C-IVR channel. See [Conversation - IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.

This article aims to provide a detailed list of all supported SSML tags in the Avaamo Platform with examples for easy understanding.

## At-a-glance

The following table summarizes a list of supported SSML tags in the Avaamo Platform that helps you to provide agent responses when you deploy your agent in the C-IVR or the phone channel:

The following example demonstrates the usage of SSML tags supported in the Avaamo Platform:

```markup
<speak> 
    Alright. Let's start with your Order number. 
    Can you tell me your Order number, one digit at a time 
    or enter your Order number on your phone's dial pad.
</speak>
```

{% hint style="success" %}
**Key point:** All the SSML tags listed in this section are supported in built-in voice.  However, only certain tags are supported in custom voice. See`Supported in Custom voice?` column for more information.
{% endhint %}

<table><thead><tr><th width="134">Tag</th><th width="355">What and When to use?</th><th align="center">Supported in Custom voice?</th></tr></thead><tbody><tr><td><a href="#less-than-speak-greater-than">&#x3C;speak></a></td><td>This is where you start constructing the SSML for the C-IVR channel. It is the root element and all the other SSML elements must be enclosed in the &#x3C;speak> tag.</td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr><tr><td><a href="#less-than-break-greater-than">&#x3C;break></a></td><td>Use this to add a pause to your text or to remove in-built pauses added by the Platform. This can be very useful when the agent response has a lengthy text or if the text contains punctuations or conjunctions.</td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr><tr><td><a href="#less-than-lang-greater-than">&#x3C;lang></a></td><td>Use this to add a specific language accent in your text. This is useful when the agent voice and the response are in different languages or when you have a mixed set of language responses in your agent.</td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr><tr><td><a href="#less-than-emphasis-greater-than">&#x3C;emphasis></a></td><td>Use this to emphasize certain phrases or text in your agent response. This is useful when you wish to express a tone of exclamation or when you wish to stress the importance of certain phrases or sentences in the agent response.</td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr><tr><td><a href="#less-than-say-as-greater-than">&#x3C;say-as></a></td><td><p>Use this with the <code>interpret-as</code> attribute to help your agent say special certain words, phrases, numbers, or text, in a way it must be said. </p><p></p><p><code>expletive</code> and <code>fractions</code> tags are not supported for custom voice.</p></td><td align="center">All except fractions and expletive</td></tr><tr><td><a href="#less-than-phoneme-greater-than">&#x3C;phoneme></a></td><td><p>Use this to read out a phonetic pronunciation of the specified text. </p><p></p><p>This tag is not supported for custom voice.</p></td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td><a href="#less-than-sub-greater-than">&#x3C;sub></a></td><td><p>Use this with an <em>alias</em> attribute to read out a different word for the specified text. Typically, used for abbreviations or acronyms. </p><p></p><p>This tag is not supported for custom voice.</p></td><td align="center"><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td><a href="#less-than-p-greater-than">&#x3C;p> or Paragraph tag</a></td><td>Use this when you wish to add a pause between paragraphs in your text.</td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr><tr><td><a href="#less-than-s-greater-than">&#x3C;s> or Sentence tag</a></td><td>Use this when you wish to add pauses between lines or sentences in your text.  </td><td align="center"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8u9eAz_C3fB4AfkLGj%2F-M8ujzex_9ztIPnAARsZ%2Ficonfinder_tick_16_22643.png?alt=media&#x26;token=73b2f354-f54f-4c80-9d52-0655faa2010b" alt="" data-size="line"></td></tr></tbody></table>

## \<speak>

This is the root element of all the SSML tags in the Avaamo Platform. All the SSML elements must be enclosed in the \<speak> tag.

```markup
<speak> 
    Alright. Let's start with your Order number. 
    Can you tell me your Order number, one digit at a time 
    or enter your Order number on your phone's dial pad.
</speak>
```

## \<break>

You can use the **break** tag to add pauses to your text or to remove in-built pauses added by the Platform. This can be very useful when the agent response has a lengthy text or if the text contains conjunctions and punctuations that require pauses to deliver the responses to the users smoothly.&#x20;

Example: In the following example, there is a pause of 3 seconds before the conjunction "or":

```markup
<speak> 
    Alright. Let's start with your Order number. 
    Can you tell me your Order number, one digit at a time 
    or <break time="3s"/>
    enter your Order number on your phone's dial pad.
</speak>
```

#### Format:&#x20;

You can set the pause duration based on the time attribute (in seconds or milliseconds) or based on the strength (pause of a comma, sentence, or paragraph) attribute.&#x20;

```markup
<break time="string"/>

<break strength="string"/>
```

| Attributes | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | <p>Mandatory </p><p>Or Optional</p> |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------: |
| time       | <p>Indicates the duration of the pause in seconds or milliseconds in the format:</p><p><code><\<number>>s</code> or <code><\<number>>ms</code></p><p>Example: 3s or 500ms. You can set a maximum value of 5000ms.</p>                                                                                                                                                                                                                                                                                                                                     |               Optional              |
| strength   | <p>Indicates the duration of the pause with respect to its strength: </p><ul><li><strong>none/x-weak</strong>: No pause. Use this if you wish to remove the default pause, say after full-stop or a period. </li><li><strong>weak/medium</strong>: Sets a pause duration equivalent to the pause required after a comma.</li><li><strong>strong</strong>: Sets a pause duration equivalent to the pause required after a sentence.</li><li><strong>x-strong</strong>: Sets a pause duration equivalent to the pause required after a paragraph.</li></ul> |               Optional              |

This is an optional tag and if not used, the pause is determined by the context of the sentence.&#x20;

## \<lang>

You can use the **lang** tag to add a specific language accent in your text. This is useful when the agent's voice and the response are in different languages or when you have a mixed set of language responses in your agent.&#x20;

Example: Consider that by default, your agent's default voice is in en-US language and you have a French text in your response. Unless the **lang** tag is specified, all the responses read out to the user is in the en-US accent. If you wish the French text in your response to be read out in a French native accent, then you can use the **lang** tag.

```markup
<speak> 
    <lang xml:lang="fr-FR">Bonjour. J'espère que tu vas bien.</lang> 
    Alright. Let's start with your Order number. 
    Can you tell me your Order number, one digit at a time or 
    <break time="0.3s"/>enter your Order number on your phone's dial pad.
</speak>
```

#### **Format**:&#x20;

```markup
<lang xml:lang="string">Specify the required text </lang>
```

In the lang tag, specify the language using the **xml:lang** attribute.

| Attributes | Description                                                                                                                                                                                                                                                                                                                                                                                                    | <p>Mandatory </p><p>Or Optional</p> |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------: |
| xml:lang   | <p>Adds a specified language accent to the specified text in the tag. <br></p><p>Language code is in ISO language format. See <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">List of ISO 639-1 codes</a> and <a href="../../how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone#supported-languages-in-c-ivr-channel">Support languages</a>, for more information.</p> |              Mandatory              |

## \<emphasis>

You can use the **emphasis** tag to emphasize certain phrases or text in your agent response. This is useful when you wish to express a tone of exclamation or when you wish to stress the importance of certain phrases or sentences in the agent response.&#x20;

Example: In the following example, the order number MP0543 has an emphasis with a strong level, hence the text is read out louder and slower.

```markup
<speak>
     Confirming your order. 
     Your order number is <emphasis level="strong">MP0543</emphasis> 
</speak>
```

#### Format:

```markup
<emphasis level="string">Specify the required text </lang>
```

When you use this tag, the tone and speed of the phrase specified in the tag change. More emphasis text is read out louder and slower. Less emphasis text is quieter and faster. The level of emphasis can be specified using the **level** attribute:

| Attributes | Description                                                                                                                                                                                                                                                                                                                                                                          | <p>Mandatory Or</p><p> Optional</p> |
| :--------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------: |
|    level   | <p>Indicates the level of emphasis to be used for the specified text:</p><ul><li><strong>strong</strong>: Volume is louder and speed is slower.</li><li><strong>moderate</strong>: Volume is louder and speed is slower but still comparatively faster than strong. This is the default emphasis.</li><li><strong>reduced</strong>: Volume is quieter and speed is faster.</li></ul> |              Mandatory              |

## \<say-as>

You can use the **say-as** tag with the **interpret-as** attribute to help your agent say special certain words, phrases, numbers, or text, in a way it must be said. Using this tag helps your agent understand what it has to say without confusion.

Example: In the following example, the date is read out as "December thirty-first, twenty-twenty":

```markup
<speak> 
    Your order will be dispatched on 
    <say-as interpret-as="date" format="mdy">12-31-2020</say-as>.
</speak>
```

#### Format:

```markup
<say-as interpret-as="string" format="string">
        Specify the text here
</say-as>

format -> Is an optional attribute and used for interpreting "date" and "time".
```

|  Attributes  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | <p>Mandatory Or</p><p> Optional</p> |
| :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------: |
| interpret-as | <p>Indicates the level of emphasis to be used for the specified text:</p><ul><li><a href="#ordinal">ordinal</a>: Interprets the numerical text as ordinals such as first, second, third.</li><li><a href="#cardinal">cardinal</a>: Interprets the numerical text as cardinal numbers.</li><li><a href="#characters">characters</a>: Interprets each character in the text separately.</li><li><a href="#date">date</a>: Interprets the date in the text according to the specified format.</li><li><a href="#digits">digits</a>: Interprets each digit in the numerical text separately.</li><li><a href="#fractions">fractions</a>: Interprets the proper fractions and mixed fractions in the text.</li><li><a href="#expletive">expletive</a>: Beeps out the content in the tag.</li><li><a href="#telephone">telephone</a>: Interprets the text provided in the telephone format. </li></ul> |              Mandatory              |
|    format    | Indicates the format to be used for interpreting date text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  Optional. Mandatory only for date. |

### ordinal

Interprets the numerical text as ordinals such as first, second, and third. Example: The following text is read out as "Congratulations. Your first order is on its way. "

```markup
<speak> 
    Congratulations. 
    Your <say-as interpret-as="ordinal">1</say-as> order is on its way. 
</speak>
```

### cardinal

Interprets the numerical text as cardinal numbers. Example: The following text is read out as "Ninety- eight thousand six hundred and fifty-four. "&#x20;

Note that the interpreting cardinal is based on the chosen language of the agent.&#x20;

Example: In an en-IN language, 1023456 is interpreted as "Ten lakhs twenty-three thousand four hundred and fifty-six", whereas, in en-US language, it is interpreted as "One million twenty-three thousand four hundred and fifty-six".

```markup
<speak>
    <say-as interpret-as="cardinal">98654</say-as>
</speak>
```

### characters

Interprets the characters in the text separately. Example: The following text is read out as "S", "P", "O", and "T" separately instead of the word "Spot".

```markup
<speak>
    <say-as interpret-as="characters">SPOT</say-as>
</speak>
```

### date

Interprets the date in the text. **date** must be specified with a format such as mdy, dmy. Example: The following text is read out as "December 2nd, 2006".

```markup
<speak> 
    Your order will be dispatched on 
    <say-as interpret-as="date" format="mdy">12-2-2006</say-as>.
</speak>
```

The following formats are supported:

| Format | Description    |
| ------ | -------------- |
| mdy    | month-day-year |
| dmy    | day-month-year |
| ymd    | year-month-day |
| md     | month-day      |
| dm     | day-month      |
| ym     | year-month     |
| my     | month-year     |
| dy     | day-year       |
| yd     | year-day       |
| d      | day            |
| m      | month          |
| y      | year           |

### digits

Interprets each digit individually in the numerical text. Example: The following text is read out as "9", "8", "6", "5", and "4" digits separately.

```markup
<speak>
    <say-as interpret-as="digits">98654</say-as>
</speak>
```

### fractions

{% hint style="info" %}
**Note**: `fractions` tag is supported only for built-in voice and not supported for custom voice.&#x20;
{% endhint %}

Interprets the fractions and mixed fractions in the text. Note that mixed fractions must be of the form: `cardinal number`+`cardinal number`/`cardinal number`&#x20;

Example: The following text is read out as "three half":

```markup
<speak>
    <say-as interpret-as="fractions">3+1/2</say-as>
</speak>
```

Example: The following text is read out as "three tenths":

```markup
<speak>
    <say-as interpret-as="fractions">3/10</say-as>
</speak>
```

### expletive&#x20;

{% hint style="info" %}
**Note**: `expletive` tag is supported only for built-in voice and not supported for custom voice.&#x20;
{% endhint %}

'Beeps out the content in the tag. Typically, used for censored or confidential content.

```markup
<speak>
    <say-as interpret-as="expletive">bleep this</say-as>
</speak>
```

### telephone

Interprets the text provided in telephone format. This is useful when you have a text with continuous numbers and not in the telephone format such as 222-678-1234. By default, the text in the format is read out with pauses in the telephone format without requiring you to specify the "telephone" format. You can also use this value to handle telephone extensions, such as 2122241555x896.

Note that the interpreting telephone is based on the chosen language of the agent. Example: In an en-IN language, 2122241555 is interpreted as "two one two <\<pause>> double two-four <\<pause>> triple three-five", whereas, in en-US language, it is interpreted as one digit at a time with pauses after every three digits.

```markup
<speak>
    My number is <say-as interpret-as="telephone">2122241555</say-as>
</speak>
```

{% hint style="info" %}
**Note**: Currently the telephone tag option is available for voices speaking in the following languages:&#x20;

* English language variants (en-AU, en-GB, en-IN, and en-US)
* Spanish language variants (es-ES, es-MX, and es-US)
* French language variants (fr-FR and fr-CA)
* Portuguese variants (pt-BR and pt-PT)
* German (de-DE)
* Italian (it-IT)
* Japanese (ja-JP)
* Russian (ru-RU).&#x20;

Also note that in some cases, languages such as Arabic (arb) automatically handle the number set as a telephone number and hence telephone tag is not required.
{% endhint %}

## \<phoneme>

{% hint style="info" %}
**Note**: `phoneme` tag is supported only for built-in voice and not supported for custom voice.&#x20;
{% endhint %}

You can use this tag to read out a phonetic pronunciation of the specified text. This is useful when you have text that requires a different pronunciation than the standard pronunciation associated by default with the language.

Example: In the following example, "pecan" is assigned different pronunciation using alphabet and ph attributes:

```markup
<speak>
    You say, <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>.
    I say, <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>.
</speak>
```

#### Format:

```markup
<phoneme alphabet="string" ph="string">
    Specify the text here.
</phoneme>
```

| Attributes | Format or Values                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Mandatory or Optional |
| ---------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------: |
| alphabet   | <ul><li>ipa </li><li>x-sampa</li></ul> | <ul><li><strong>ipa</strong>: Indicates that the International Phonetic Alphabet (IPA) must be used for phonetic pronunciation.</li><li><strong>x-sampa</strong>: Indicates that the Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA) must be used for phonetic pronunciation.</li></ul>                                                                                                                                                                                                              |       Mandatory       |
| ph         | String                                 | <p>Indicates phonetic symbols of pronunciations. See <a href="../../how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone#supported-languages-in-c-ivr-channel">Supported languages in C-IVR channel</a>. Also, see </p><p><a href="https://en.wikipedia.org/wiki/International_Phonetic_Alphabet">International Phonetic Alphabet (IPA)</a> and <a href="https://en.wikipedia.org/wiki/X-SAMPA">Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA)</a>, for more information.</p> |       Mandatory       |

## \<sub>

{% hint style="info" %}
**Note**: `sub` tag is supported only for built-in voice and not supported for custom voice.&#x20;
{% endhint %}

You can use this tag with an *alias* attribute to read out a different word for the specified text. Typically, used for abbreviations or acronyms.&#x20;

Example: In the following example SSML text is read out as "Speech Synthesis Markup Language":

```markup
<speak>
     <sub alias="Speech Synthesis Markup Language">SSML</sub>
</speak>
```

#### Format:

```markup
<sub alias="string">Specify the required text</sub>
```

| Attributes | Format or Values | Description                                                 | Mandatory or Optional |
| ---------- | :--------------: | ----------------------------------------------------------- | :-------------------: |
| alias      |      String      | Indicates the alias that is read out for the specified text |       Mandatory       |

## \<p> or paragraph tag

You can use this tag to add pauses between paragraphs in your text. By default, pauses are added at the end of a paragraph.&#x20;

Adding \<p> between lines provides the same effect as adding a [break](#less-than-break-greater-than) tag with an **x-strong** attribute.&#x20;

```markup
<speak>
     <p>This is the first paragraph. I want to break
     and add pause at the end.</p>
     <p> This is the second paragraph. There is a pause here too </p>
</speak> 
```

#### Format:

```markup
<p>Specify the required text </p>
```

## \<s> or Sentence tag

You can use this tag to add pauses between lines or sentences in your text. By default, pauses are added at the end of a period. However, you can add \<s> between lines or sentences in your text to add additional pauses as required.&#x20;

Adding \<s> tag provides the same effect as adding a period at the end of the sentence or adding a [break](#less-than-break-greater-than) tag with a **strong** attribute.

```markup
<speak>
     Adding a pause here 
     <s>between sentence</s> 
     is the same as adding a period at the end.
</speak> 
```

#### Format:

```markup
<s>Specify the required text</s>
```
