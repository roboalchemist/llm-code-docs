# Source: https://plivo.com/docs/voice/concepts/ssml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started with Speech Synthesis Markup Language (SSML)

> Control speech output with SSML — pitch, volume, and pronunciation

The World Wide Web Consortium (W3C) created Speech Synthesis Markup Language ([SSML](https://www.w3.org/TR/speech-synthesis11/)) as an XML-based markup language to assist in generating natural-sounding synthesized speech. The Plivo Speak XML element supports the generation of SSML-based speech, powered by [Amazon Polly](https://aws.amazon.com/polly/). It supports 27 languages and more than 40 voices, and allows developers to  control pronunciation, pitch, and volume.

Here‘s how SSML appears within Plivo Speak XML elements:

```xml  theme={null}
<Response>
    <Speak voice="MAN">Go Green, Go Plivo</Speak> //Basic Text-to-Speech
    <Speak voice="Polly.Joey">
        <emphasis level="moderate">Go Green, Go Plivo</emphasis> //Text-to-Speech using SSML
    </Speak>
</Response>
```

To synthesize SSML speech on Plivo, specify one of the [Amazon Polly voices](/voice/concepts/ssml/#ssml-voices) in the `voice` attribute of Plivo’s \<Speak> XML tag. Note that Polly voices must be namespaced with a `Polly` prefix.

For example:

```xml  theme={null}
<Response>
    <Speak voice="Polly.Joey">
        <emphasis level="moderate">Go Green, Go Plivo</emphasis>
    </Speak>
</Response>
```

## SSML tags

You can use these SSML tags within Plivo XML.

| SSML Tag    | Action                                                                                                                      | Description                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| \<break>    | [Add a pause](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#break-tag)                                     | Use this tag to include a pause in the speech.                                                  |
| \<emphasis> | [Emphasize words](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#emphasis-tag)                              | Use this tag to change the rate and voice of the speech.                                        |
| \<lang>     | [Specify another language for specific words](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#lang-tag)      | Use this tag to set the natural language of the text.                                           |
| \<p>        | [Add a pause between paragraphs](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#p-tag)                      | Use this tag to represent a paragraph.                                                          |
| \<phoneme>  | [Use phonetic pronunciation](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#phoneme-tag)                    | Use this tag to set phonetic pronunciation for specific text.                                   |
| \<prosody>  | [Control volume, speaking rate, and pitch](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#prosody-tag)      | Use this tag to modify the volume, speaking rate, and pitch of the tagged text.                 |
| \<s>        | [Add a pause between sentences](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#s-tag)                       | Use this tag to represent a sentence. This adds a strong break before and after the tag.        |
| \<say-as>   | [Control how special types of words are spoken](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#say-as-tag)  | Use this tag to describe how to interpret the text.                                             |
| \<sub>      | [Pronounce acronyms and abbreviations](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#sub-tag)              | Use this tag to pronounce the specified words or phrases as different words or phrases.         |
| \<w>        | [Improve pronunciation by specifying parts of speech](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#w-tag) | Use this tag to customize the pronunciation of words by specifying the part of speech they are. |

**Note**: Plivo doesn’t support these Amazon Polly-specific tags in Plivo XML:

* \<amazon:auto-breaths>
* \<amazon:effect name="drc">
* \<amazon:effect phonation="soft">
* \<amazon:effect vocal-tract-length>
* \<amazon: effect name="whispered">

## SSML voices

Plivo supports these Amazon Polly voices for use with Plivo XML:

| Language                     | Female                                                                                                                                          | Male                                                                                                                              |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Australian English (en-AU)   | [Polly.Nicole](https://d1.awsstatic.com/product-marketing/Polly/voices/nicole.8656c0be485fb3c43c29a7cc799960211fa224e5.mp3)                     | [Polly.Russell](https://d1.awsstatic.com/product-marketing/Polly/voices/russell.85286a07b33c9ee2bd97dd994294ccebb50a784d.mp3)     |
| Brazilian Portuguese (pt-BR) | [Polly.Vitória](https://d1.awsstatic.com/product-marketing/Polly/voices/vitoria.dccdde767360bb45f5ef615d4ae93245e43a4320.mp3)                   | [Polly.Ricardo](https://d1.awsstatic.com/product-marketing/Polly/voices/ricardo.485ed1dff89ee3606e46ef0f84b14d73fcd42a6b.mp3)     |
| Canadian French (fr-CA)      | [Polly.Chantal](https://d1.awsstatic.com/product-marketing/Polly/voices/chantal.322a64f32393d0c6a5a291465f451cbcd681c295.mp3)                   | -                                                                                                                                 |
| Danish (da-DK)               | [Polly.Naja](https://d1.awsstatic.com/product-marketing/Polly/voices/naja.b704af10c1e90008689ef17863d949c7b3d229a5.mp3)                         | [Polly.Mads](https://d1.awsstatic.com/product-marketing/Polly/voices/mads.84fb272b1941303d0b744f267d5a7bbe940b34f4.mp3)           |
| Dutch (nl-NL)                | [Polly.Lotte](https://d1.awsstatic.com/product-marketing/Polly/voices/lotte.b60b7c845c0135c05852c837813038abe87a824a.mp3)                       | [Polly.Ruben](https://d1.awsstatic.com/product-marketing/Polly/voices/ruben.e8d339872f9d4aac2cf9c6844ab793f81550a015.mp3)         |
| French (fr-FR)               | [Polly.Lea](https://d1.awsstatic.com/product-marketing/Polly/voices/lea.23bfaf13f5727801c654d1e2f028496f39ba6f0d.mp3)                           | [Polly.Celine](https://d1.awsstatic.com/product-marketing/Polly/voices/celine.e6c15212622f6f5225f234d980a65e9a41201196.mp3)       |
|                              | [Polly.Mathieu](https://d1.awsstatic.com/product-marketing/Polly/voices/mathieu.feedabefbaa9a94fe1bdeae8e503b49819f910c5.mp3)                   | -                                                                                                                                 |
| German (de-DE)               | [Polly.Vicki](https://d1.awsstatic.com/product-marketing/Polly/voices/vicki.cafbf81c1cb7f9c5c060b02ffda104a7f6ee6cb9.mp3)                       | [Polly.Hans](https://d1.awsstatic.com/product-marketing/Polly/voices/hans.c8171993a58a550ba31d7c7c9caadb4042d01609.mp3)           |
|                              | [Polly.Marlene](https://d1.awsstatic.com/product-marketing/Polly/voices/marlene.39191e409bfc0031ea32c63aa8f6027e2110da96.mp3)                   | -                                                                                                                                 |
| Hindi (hi-IN)                | [Polly.Aditi](https://d1.awsstatic.com/product-marketing/Polly/voices/aditi_hindi.87e7512d4a1eb60235e8fc4edd08ab2071a8718c.mp3)                 | -                                                                                                                                 |
| Icelandic (is-IS)            | [Polly.Dora](https://d1.awsstatic.com/product-marketing/Polly/voices/dora.7579e97fbfe4a3d4ff00df48dd9c588b377f3308.mp3)                         | [Polly.Karl](https://d1.awsstatic.com/product-marketing/Polly/voices/karl.5ea12538bbd81ede68314aca4b6dbf7e73405be3.mp3)           |
| Indian English (en-IN)       | [Polly.Raveena](https://d1.awsstatic.com/product-marketing/Polly/voices/raveena.1819674fbbf0720fdf94018f1df918ade38ebf5a.mp3)                   | -                                                                                                                                 |
|                              | [Polly.Aditi](https://d1.awsstatic.com/product-marketing/Polly/voices/aditi.09b7fbaf5620f9b49b6b759f6b2df58fdcbc5d3e.mp3)                       | -                                                                                                                                 |
| Italian (it-IT)              | [Polly.Carla](https://d1.awsstatic.com/product-marketing/Polly/voices/carla.a990b3137f13cb66ef3b9d80e1eba87e30855386.mp3)                       | [Polly.Giorgio](https://d1.awsstatic.com/product-marketing/Polly/voices/giorgio.74927aa24bee5d8eea0b09619e29379ed8053010.mp3)     |
| Japanese (ja-JP)             | [Polly.Mizuki](https://d1.awsstatic.com/product-marketing/Polly/voices/mizuki.ae1d119948ee76011e51299748db48c25943e82e.mp3)                     | [Polly.Takumi](https://d1.awsstatic.com/product-marketing/Polly/voices/takumi.b3728282feaaea563b23345fb9fb434d9b727c7c.mp3)       |
| Korean (ko-KR)               | [Polly.Seoyeon](https://d1.awsstatic.com/product-marketing/Polly/HelloKorean_Seoyeon.b0ae8ddfc55e602e3f0657afe112b8902282880a.wav)              | -                                                                                                                                 |
| Mandarin Chinese (cmn-CN)    | [Polly.Zhiyu](https://d1.awsstatic.com/product-marketing/Polly/voices/Zhiyu-hi.9785e6f8b598d3e6bdcb5c2a9ec95859bfd1292d.mp3)                    | -                                                                                                                                 |
| Norwegian (nb-NO)            | [Polly.Liv](https://d1.awsstatic.com/product-marketing/Polly/voices/liv.b5a39b3792911ed1d8d35c6c6f327850aae05972.mp3)                           | -                                                                                                                                 |
| Polish (pl-PL)               | [Polly.Ewa](https://d1.awsstatic.com/product-marketing/Polly/voices/ewa.497d83b9f6c486ce14d0b78b9514591a18d4f1b8.mp3)                           | [Polly.Jacek](https://d1.awsstatic.com/product-marketing/Polly/voices/jacek.8851713e855fb82baaf76e1eb4e97fed97f65a36.mp3)         |
|                              | [Polly.Maja](https://d1.awsstatic.com/product-marketing/Polly/voices/maja.c24bddf411c7c750c6aa621fc8fc4c009c0866f3.mp3)                         | [Polly.Jan](https://d1.awsstatic.com/product-marketing/Polly/voices/jan.9bb856fb6dfe128cc7033943d7009c19f0dddd73.mp3)             |
| Portuguese - Iberic (pt-PT)  | [Polly.Ines](https://d1.awsstatic.com/product-marketing/Polly/voices/ines.136466e69d98c766946a311d151b13a0b6e86dfa.mp3)                         | [Polly.Cristiano](https://d1.awsstatic.com/product-marketing/Polly/voices/cristiano.aec3b12945b55ae6990c6b78f534031fb3ee9b6a.mp3) |
| Romanian (ro-RO)             | [Polly.Carmen](https://d1.awsstatic.com/product-marketing/Polly/voices/carmen.b732da15cb57ac7c873dd3d016193437cb8ea93c.mp3)                     | -                                                                                                                                 |
| Russian (ru-RU)              | [Polly.Tatyana](https://d1.awsstatic.com/product-marketing/Polly/voices/tatyana.1f33b6e72ad56ce6a22c577c5090fdc7ca6c8dd0.mp3)                   | [Polly.Maxim](https://d1.awsstatic.com/product-marketing/Polly/voices/maxim.30cd883f122322e8afd315a49b72efcca91130d2.mp3)         |
| Spanish - Castilian (es-ES)  | [Polly.Conchita](https://d1.awsstatic.com/product-marketing/Polly/voices/conchita.103a380cdb2471d794dbdc4808e18f4bcf52e299.mp3)                 | [Polly.Enrique](https://d1.awsstatic.com/product-marketing/Polly/voices/enrique.22473b31f265f8b050f91df18a8b36a89d19b70e.mp3)     |
| Spanish - Mexican (es-MX)    | [Polly.Mia](https://d1.awsstatic.com/product-marketing/Polly/voices/Mia.575350d0eeeafa39c121f756c4bfac6437c4e650.mp3)                           | -                                                                                                                                 |
| US - Spanish (es-US)         | [Polly.Penelope](https://d1.awsstatic.com/product-marketing/Polly/voices/penelope.7723493fdb9c6b7e1400efe02a5c1e7848310ba4.mp3)                 | [Polly.Miguel](https://d1.awsstatic.com/product-marketing/Polly/voices/miguel.91030339cc81f8df461e3ab7325168fa5fdc0035.mp3)       |
|                              | [Polly.Lupe-Standard](https://d1.awsstatic.com/product-marketing/Polly/voices/Lupe%20\(Standard\).85d69fc3a36ee08455b352221435154afd19420c.mp3) | -                                                                                                                                 |
| Swedish (sv-SE)              | [Polly.Astrid](https://d1.awsstatic.com/product-marketing/Polly/voices/astrid.4c9e160e86557f9610fa718f1d871a0caf61e586.mp3)                     | -                                                                                                                                 |
| Turkish (tr-TR)              | [Polly.Filiz](https://d1.awsstatic.com/product-marketing/Polly/voices/filiz.15c85361bbac56743b00ebf345c2a7d54a3e99f8.mp3)                       | -                                                                                                                                 |
| UK English (en-GB)           | [Polly.Amy](https://d1.awsstatic.com/product-marketing/Polly/voices/amy.19b8f5cf54bce4bc1010b4234ec6e9ea1496e97f.mp3)                           | [Polly.Brian](https://d1.awsstatic.com/product-marketing/Polly/voices/brian.f5abc46f50f1042bac587d990dd05912daf09089.mp3)         |
|                              | [Polly.Emma](https://d1.awsstatic.com/product-marketing/Polly/voices/emma.21bd3065d00d15f8f7df800436c0e52970953d36.mp3)                         | -                                                                                                                                 |
| US English (en-US)           | [Polly.Joanna](https://d1.awsstatic.com/product-marketing/Polly/voices/joanna.84722a684fbb16e766944ea6e34dd0042195571c.mp3)                     | [Polly.Matthew](https://d1.awsstatic.com/product-marketing/Polly/voices/matthew.b2a8b7d5b329742fc718c7a8d0efdad1c11fb25f.mp3)     |
|                              | [Polly.Salli](https://d1.awsstatic.com/product-marketing/Polly/voices/salli.20a721cb6b8a5fbb016ab6d9ded37f9a91fe7a58.mp3)                       | [Polly.Justin](https://d1.awsstatic.com/product-marketing/Polly/voices/justin.acfadcd365d37a1ecc88fdb2a640f1a75f83bdf7.mp3)       |
|                              | [Polly.Kendra](https://d1.awsstatic.com/product-marketing/Polly/voices/kendra.d768f43e12c08892d4495511e84e82f1b7195673.mp3)                     | [Polly.Joey](https://d1.awsstatic.com/product-marketing/Polly/voices/joey.3abd7f17e6dae6c9248cacd7eb0ec910c691c4f4.mp3)           |
|                              | [Polly.Kimberly](https://d1.awsstatic.com/product-marketing/Polly/voices/kimberly.42e50dd5056c92a5fff41952d0c057a7f09adca3.mp3)                 | -                                                                                                                                 |
|                              | [Polly.Ivy](https://d1.awsstatic.com/product-marketing/Polly/voices/ivy.70016451b3c186bcacba09acf5ee1b68c12db745.mp3)                           | -                                                                                                                                 |
| Welsh (cy-GB)                | [Polly.Gwyneth](https://d1.awsstatic.com/product-marketing/Polly/voices/gwyneth.be497813ff11614acbdac0fb6c334b94bce20b45.mp3)                   | -                                                                                                                                 |
| Welsh English (en-GB-WLS)    | -                                                                                                                                               | [Polly.Geraint](https://d1.awsstatic.com/product-marketing/Polly/voices/geraint.4aa21b628bd99741c0275c77d8daa0ff7290265e.mp3)     |

## Character limit

To ensure quick synthesis, Plivo caps the length of text that can be synthesized in one \<Speak> tag at 3,000 characters.

## Pricing

Support for SSML-based speech synthesis is currently in beta and free for all Plivo users. We expect to eventually charge for text-to-speech on the basis of the number of characters synthesized.

## SSML support in Plivo Server SDKs

SSML tags are supported in all of our [Server SDKs](/sdk/server/).

## Example

This example use the [Joey](https://d1.awsstatic.com/product-marketing/Polly/voices/joey.3abd7f17e6dae6c9248cacd7eb0ec910c691c4f4.mp3) voice for US English (en-US). Use the \<Speak voice> tag to specify the voice for your text.

### say-as

The say-as tag describes how to interpret the text.

<CodeGroup>
  ```py Python theme={null}
  from flask import Flask, Response, request, url_for
  from plivo import plivoxml

  app = Flask(__name__)

  @app.route("/ssml/", methods=["GET", "POST"])
  def ssml():
      element = plivoxml.ResponseElement()
      response = (
          element.add(
              plivoxml.SpeakElement(content="The date is", voice="Polly.Joey", language="en-US")
              .add_say_as("20200626", interpret_as="date")
          )
          .to_string(False)
      )
      print(response)
      return Response(response, mimetype="text/xml")

  if __name__ == "__main__":
      app.run(host="0.0.0.0", debug=True)
  ```

  ```rb Ruby theme={null}
  class PlivoController < ApplicationController
    def ssml
      response = Plivo::XML::Response.new
      speak_elem = response.addSpeak('The date is', voice: 'Polly.Joey', language: 'en-US')
      speak_elem.addSayAs('20200626', 'interpret-as' => 'date')
      xml = Plivo::XML::PlivoXML.new(response)
      puts xml.to_xml()
      render xml: xml.to_xml
    end
  end
  ```

  ```js Node.js theme={null}
  var plivo = require('plivo');
  var express = require('express');
  var app = express();
  app.set('port', (process.env.PORT || 5000));
  app.use(express.static(__dirname + '/public'));

  app.all('/ssml/', function (request, response) {
      if (request.method == "GET") {
          var r = new plivo.Response();
          const speakElem = r.addSpeak('The date is', {
              'voice': 'Polly.Joey',
              'language': 'en-US'
          });
          speakElem.addSayAs('20200626', {
              'interpret-as': 'date',
          });
          console.log(r.toXML());
          response.set({
              'Content-Type': 'text/xml'
          });
          response.end(r.toXML());
      }
  });

  app.listen(app.get('port'), function () {
      console.log('Node app is running on port', app.get('port'));
  });
  ```

  ```php PHP theme={null}
  <?php

  namespace App\Http\Controllers;

  require '../vendor/autoload.php';
  use Plivo\RestClient;
  use Plivo\XML\Response;
  use Illuminate\Http\Request;

  class ReceivecallController extends Controller
  {
      public function ssml()
      {
          $response = new Response();
          $speak_elem = $response->addSpeak('The date is', ['language'=>"en-US", 'voice'=>"Polly.Joey"]);
          $speak_elem->addSayAs('20200626', ['interpret-as'=>"date"]);
          $xml_response = $response->toXML(); 
          return response($xml_response, 200)->header('Content-Type', 'application/xml');
      }
  }
  ```

  ```java Java theme={null}
  package com.example.SsmlHandler;
  import com.plivo.api.exceptions.PlivoXmlException;
  import com.plivo.api.xml.*;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.web.bind.annotation.*;
  @SpringBootApplication
  @RestController
  public class SsmlApplication {
  	public static void main(String[] args) {
  		SpringApplication.run(SsmlHandlerApplication.class, args);
  	}
  	@RequestMapping(value = "/ssml/", produces = { "application/xml" }, method = { RequestMethod.GET, RequestMethod.POST })
  	public Response SsmlHandler() throws PlivoXmlException {
  		Response response = new Response().children(new Speak("The date is").
  						children(new SayAs("20200626", "date")));
  		System.out.println(response.toXmlString());
  		return response;
  	}
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"net/http"

  	"github.com/go-martini/martini"
  	"github.com/plivo/plivo-go/v7/xml"
  )

  func main() {
  	m := martini.Classic()
  	m.Any("/ssml/", func(w http.ResponseWriter, r *http.Request) string {
  		w.Header().Set("Content-Type", "application/xml")
  		response := xml.ResponseElement{
  			Contents: []interface{}{
  				new(xml.SpeakElement).
  					AddSpeak("The date is", "Polly.Joey", "en-US", 1).
  					AddSayAs("20200626", "date", ""),
  			},
  		}
  		return response.String()
  	})

  	m.Run()
  }
  ```

  ```cs .NET theme={null}
  using System.Collections.Generic;
  using Plivo.XML;
  using Microsoft.AspNetCore.Mvc;

  namespace Voicemail.Controllers
  {
      public class SsmlController : Controller
      {
          // GET: /<controller>/
          public IActionResult Index()
          {
              var resp = new Response();
              Speak speak_elem = new Speak("The date is", new Dictionary<string, string>() {
                  {"voice","Polly.Joey"},
                  {"language","en-US"},
              });
              resp.Add(speak_elem);
              speak_elem.AddSayAs("20200626", new Dictionary<string, string>() {
                  { "interpret-as", "date" }
              });
              var output = resp.ToString();
              return this.Content(output, "text/xml");
          }
      }
  }
  ```
</CodeGroup>

The rendered XML document would be:

```xml  theme={null}
<Response>
    <Speak voice="Polly.Joey">The date is
      <say-as interpret-as="date">20200626</say-as>
    </Speak>
</Response>
```

### w

The w tag lets you customize the pronunciation of a word by specifying its part of speech.

<CodeGroup>
  ```py Python theme={null}
  from flask import Flask, Response, request, url_for
  from plivo import plivoxml

  app = Flask(__name__)

  @app.route("/ssml/", methods=["GET", "POST"])
  def ssml():
      element = plivoxml.ResponseElement()
      response = (
          element.add(
              plivoxml.SpeakElement(content="The word", voice="Polly.Joey", language="en-US")
              .add_say_as("read", interpret_as="characters")
              .add_s("may be interpreted as either the present simple form")
              .add_w("read", role="amazon:VB")
              .add_s("or the past participle form")
              .add_w("read", role="amazon:VBD")
          )
          .to_string(False)
      )
      print(response)
      return Response(response, mimetype="text/xml")

  if __name__ == "__main__":
      app.run(host="0.0.0.0", debug=True)
  ```

  ```rb Ruby theme={null}
  class PlivoController < ApplicationController
    def ssml
      response = Plivo::XML::Response.new
      speak_elem = response.addSpeak('The word', voice: 'Polly.Joey', language: 'en-US')
      speak_elem.addSayAs('read', 'interpret-as' => 'characters')
      speak_elem.addS('may be interpreted as either the present simple form')
      speak_elem.addW('read', 'role' => 'amazon:VB')
      speak_elem.addS('or the past participle form')
      speak_elem.addW('read', 'role' => 'amazon:VBD')
      xml = Plivo::XML::PlivoXML.new(response)
      puts xml.to_xml()
      render xml: xml.to_xml
    end
  end
  ```

  ```js Node.js theme={null}
  var plivo = require('plivo');
  var express = require('express');
  var app = express();
  app.set('port', (process.env.PORT || 5000));
  app.use(express.static(__dirname + '/public'));

  app.all('/ssml/', function(request, response) {
      if (request.method == "GET") {
          var r = new plivo.Response();
          const speakElem = r.addSpeak('The word', {
              'voice': 'Polly.Joey',
              'language': 'en-US'
          });
          speakElem.addSayAs('read', {
              'interpret-as': 'characters'
          });
          speakElem.addS('may be interpreted as either the present simple form');
          speakElem.addW('read', {
              'role': 'amazon:VB'
          });
          speakElem.addS('or the past participle form');
          speakElem.addW('read', {
              'role': 'amazon:VBD'
          });
          console.log(r.toXML());
          response.set({
              'Content-Type': 'text/xml'
          });
          response.end(r.toXML());
      }
  });

  app.listen(app.get('port'), function() {
      console.log('Node app is running on port', app.get('port'));
  });
  ```

  ```php PHP theme={null}
  <?php

  namespace App\Http\Controllers;

  require '../vendor/autoload.php';
  use Plivo\RestClient;
  use Plivo\XML\Response;
  use Illuminate\Http\Request;

  class ReceivecallController extends Controller
  {
      public function ssml()
      {
          $response = new Response();
          $speak_elem = $response->addSpeak('The word', ['language'=>"en-US", 'voice'=>"Polly.Joey"]);
          $speak_elem->addSayAs('read', ['interpret-as'=>"characters"]);
          $speak_elem->addS('may be interpreted as either the present simple form');
          $speak_elem->addW('read', ['role'=>"amazon:VB"]);
          $speak_elem->addS('or the past participle form');
          $speak_elem->addW('read', ['role'=>"amazon:VBD"]);
          $xml_response = $response->toXML(); 
          return response($xml_response, 200)->header('Content-Type', 'application/xml');
      }
  }
  ```

  ```java Java theme={null}
  package com.example.SsmlHandler;
  import com.plivo.api.exceptions.PlivoXmlException;
  import com.plivo.api.xml.*;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.web.bind.annotation.*;
  @SpringBootApplication
  @RestController
  public class SsmlApplication {
  	public static void main(String[] args) {
  		SpringApplication.run(SsmlHandlerApplication.class, args);
  	}
  	@RequestMapping(value = "/ssml/", produces = { "application/xml" }, method = { RequestMethod.GET, RequestMethod.POST })
  	public Response Ssml() throws PlivoXmlException {
  		Response response = new Response().children(new Speak("The word","Polly.Joey","en-US",1)
  				.children(new SayAs("read", "characters"))
  				.addS("may be interpreted as either the present simple form")
  				.addW("read", "amazon:VB")
  				.addS("or the past participle form")
  				.addW("read", "amazon:VBD"));
  		System.out.println(response.toXmlString());
  		return response;
  	}
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"net/http"

  	"github.com/go-martini/martini"
  	"github.com/plivo/plivo-go/v7/xml"
  )

  func main() {
  	m := martini.Classic()
  	m.Any("/ssml/", func(w http.ResponseWriter, r *http.Request) string {
  		w.Header().Set("Content-Type", "application/xml")
  		response := xml.ResponseElement{
  			Contents: []interface{}{
  				new(xml.SpeakElement).
  					AddSpeak("The word", "Polly.Joey", "en-US", 1).
  					AddSayAs("read", "characters", "").
  					AddS("may be interpreted as either the present simple form").
  					AddW("read", "amazon:VB").
  					AddS("or the past participle form").
  					AddW("read", "amazon:VBD"),
  			},
  		}
  		return response.String()
  	})

  	m.Run()
  }
  ```

  ```cs .NET theme={null}
  using System.Collections.Generic;
  using Plivo.XML;
  using Microsoft.AspNetCore.Mvc;

  namespace Voicemail.Controllers
  {
      public class SsmlController : Controller
      {
          // GET: /<controller>/
          public IActionResult Index()
          {
              var resp = new Response();
              Speak speak_elem = new Speak("The word", new Dictionary<string, string>() {
                  {"voice","Polly.Joey"},
                  {"language","en-US"},
              });
              resp.Add(speak_elem);
              speak_elem.AddSayAs("read", new Dictionary<string, string>() {
                  { "interpret-as", "characters" }
              });
              speak_elem.AddS("may be interpreted as either the present simple form");
              speak_elem.AddW("read", new Dictionary<string, string>() {
                  { "role", "amazon:VB" }
              });
              speak_elem.AddS("or the past participle form");
              speak_elem.AddW("read", new Dictionary<string, string>() {
                  { "role", "amazon:VBD" }
              });
              var output = resp.ToString();
              return this.Content(output, "text/xml");
          }
      }
  }
  ```
</CodeGroup>

The rendered XML document would be:

```xml  theme={null}
<Response>
    <Speak voice="Polly.Joey">The word
      <say-as interpret-as="characters">read</say-as>
      <s>
          may be interpreted as either the present simple form
      </s>
      <w role="amazon:VB">read</w>
      <s>or the past participle form</s>
      <w role="amazon:VBD">read</w>
    </Speak>
</Response>
```

### More examples

```xml  theme={null}
<Response>
    <Speak>I can speak in a 
      <prosody pitch="high">higher pitched voice</prosody>
      , or I can speak 
      <prosody pitch="low">in a lower pitched voice</prosody>
    </Speak>
</Response>

<Response>
    <Speak>I can speak 
      <prosody rate="x-slow">really slowly</prosody>
      , or  I can speak 
      <prosody rate="x-fast">really fast</prosody>
    </Speak>
</Response>

<Response>
    <Speak>I can also speak 
      <prosody volume="x-loud">very loudly</prosody>
      , or I can speak <prosody volume="x-soft">very quietly</prosody>. 
    </Speak>
</Response>
```
