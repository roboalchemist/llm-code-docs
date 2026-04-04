# Source: https://fastapi.tiangolo.com/de/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/de/

Markdown Content:
🌐 Übersetzung durch KI und Menschen
Diese Übersetzung wurde von KI erstellt, angeleitet von Menschen. 🤝

Sie könnte Fehler enthalten, etwa Missverständnisse des ursprünglichen Sinns oder unnatürliche Formulierungen, usw. 🤖

Sie können diese Übersetzung verbessern, indem Sie [uns helfen, die KI-LLM besser anzuleiten](https://fastapi.tiangolo.com/de/contributing/#translations).

[Englische Version](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/de)

_FastAPI-Framework, hohe Performanz, leicht zu lernen, schnell zu entwickeln, produktionsreif_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Testabdeckung](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package-Version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Unterstützte Python-Versionen](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Dokumentation**: [https://fastapi.tiangolo.com/de](https://fastapi.tiangolo.com/de)

**Quellcode**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI ist ein modernes, schnelles (hoch performantes) Webframework zur Erstellung von APIs mit Python auf Basis von Standard-Python-Typhinweisen.

Seine Schlüssel-Merkmale sind:

*   **Schnell**: Sehr hohe Performanz, auf Augenhöhe mit **NodeJS** und **Go** (dank Starlette und Pydantic). [Eines der schnellsten verfügbaren Python-Frameworks](https://fastapi.tiangolo.com/de/#performance).
*   **Schnell zu entwickeln**: Erhöhen Sie die Geschwindigkeit bei der Entwicklung von Features um etwa 200 % bis 300 %. *
*   **Weniger Bugs**: Verringern Sie die von Menschen (Entwicklern) verursachten Fehler um etwa 40 %. *
*   **Intuitiv**: Hervorragende Editor-Unterstützung. Code-Vervollständigung überall. Weniger Zeit mit Debuggen verbringen.
*   **Einfach**: So konzipiert, dass es einfach zu benutzen und zu erlernen ist. Weniger Zeit mit dem Lesen von Dokumentation verbringen.
*   **Kurz**: Minimieren Sie die Verdoppelung von Code. Mehrere Features aus jeder Parameterdeklaration. Weniger Bugs.
*   **Robust**: Erhalten Sie produktionsreifen Code. Mit automatischer, interaktiver Dokumentation.
*   **Standards-basiert**: Basierend auf (und vollständig kompatibel mit) den offenen Standards für APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (früher bekannt als Swagger) und [JSON Schema](https://json-schema.org/).

* Schätzung basierend auf Tests, die von einem internen Entwicklungsteam durchgeführt wurden, das Produktionsanwendungen erstellt.

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Gold- und Silber-Sponsoren[¶](https://fastapi.tiangolo.com/de/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Andere Sponsoren](https://fastapi.tiangolo.com/de/fastapi-people/#sponsors)

Meinungen[¶](https://fastapi.tiangolo.com/de/#opinions)
-------------------------------------------------------

„_[...] Ich verwende **FastAPI** heutzutage sehr oft. [...] Ich habe tatsächlich vor, es für alle **ML-Services meines Teams bei Microsoft** zu verwenden. Einige davon werden in das Kernprodukt **Windows** und einige **Office**-Produkte integriert._“

Kabir Khan – **Microsoft**[(Ref.)](https://github.com/fastapi/fastapi/pull/26)

* * *

„_Wir haben die **FastAPI**-Bibliothek übernommen, um einen **REST**-Server zu erstellen, der für **Vorhersagen** abgefragt werden kann. [für Ludwig]_“

Piero Molino, Yaroslav Dudin, und Sai Sumanth Miryala – **Uber**[(Ref.)](https://eng.uber.com/ludwig-v0-2/)

* * *

„_**Netflix** freut sich, die Open-Source-Veröffentlichung unseres **Krisenmanagement**-Orchestrierung-Frameworks bekannt zu geben: **Dispatch**! [erstellt mit **FastAPI**]_“

Kevin Glisson, Marc Vilanova, Forest Monsen – **Netflix**[(Ref.)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

„_Ich bin hellauf begeistert von **FastAPI**. Es macht so viel Spaß!_“

* * *

„_Ehrlich, was Du gebaut hast, sieht super solide und poliert aus. In vielerlei Hinsicht ist es so, wie ich **Hug** haben wollte – es ist wirklich inspirierend, jemanden so etwas bauen zu sehen._“

* * *

„_Wenn Sie ein **modernes Framework** zum Erstellen von REST-APIs erlernen möchten, schauen Sie sich **FastAPI** an. [...] Es ist schnell, einfach zu verwenden und leicht zu lernen [...]_“

„_Wir haben zu **FastAPI** für unsere **APIs** gewechselt [...] Ich denke, es wird Ihnen gefallen [...]_“

* * *

„_Falls irgendjemand eine Produktions-Python-API erstellen möchte, kann ich **FastAPI** wärmstens empfehlen. Es ist **wunderschön konzipiert**, **einfach zu verwenden** und **hoch skalierbar**; es ist zu einer **Schlüsselkomponente** unserer API-First-Entwicklungsstrategie geworden und treibt viele Automatisierungen und Services an, wie etwa unseren Virtual TAC Engineer._“

Deon Pillsbury – **Cisco**[(Ref.)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

FastAPI Mini-Dokumentarfilm[¶](https://fastapi.tiangolo.com/de/#fastapi-mini-documentary)
-----------------------------------------------------------------------------------------

Es gibt einen [FastAPI-Mini-Dokumentarfilm](https://www.youtube.com/watch?v=mpR8ngthqiE), veröffentlicht Ende 2025, Sie können ihn online ansehen:

[![Image 25: FastAPI Mini-Dokumentarfilm](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, das FastAPI der CLIs[¶](https://fastapi.tiangolo.com/de/#typer-the-fastapi-of-clis)
----------------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Wenn Sie eine CLI-Anwendung für das Terminal erstellen, anstelle einer Web-API, schauen Sie sich [**Typer**](https://typer.tiangolo.com/) an.

**Typer** ist die kleine Schwester von FastAPI. Und es soll das **FastAPI der CLIs** sein. ⌨️ 🚀

Anforderungen[¶](https://fastapi.tiangolo.com/de/#requirements)
---------------------------------------------------------------

FastAPI steht auf den Schultern von Giganten:

*   [Starlette](https://www.starlette.dev/) für die Webanteile.
*   [Pydantic](https://docs.pydantic.dev/) für die Datenanteile.

Installation[¶](https://fastapi.tiangolo.com/de/#installation)
--------------------------------------------------------------

Erstellen und aktivieren Sie eine [virtuelle Umgebung](https://fastapi.tiangolo.com/de/virtual-environments/) und installieren Sie dann FastAPI:

**Hinweis**: Stellen Sie sicher, dass Sie `"fastapi[standard]"` in Anführungszeichen setzen, damit es in allen Terminals funktioniert.

Beispiel[¶](https://fastapi.tiangolo.com/de/#example)
-----------------------------------------------------

### Erstellung[¶](https://fastapi.tiangolo.com/de/#create-it)

Erstellen Sie eine Datei `main.py` mit:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

Oder verwenden Sie `async def` ...
Wenn Ihr Code `async` / `await` verwendet, benutzen Sie `async def`:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**Hinweis**:

Wenn Sie das nicht kennen, schauen Sie sich den Abschnitt _„In Eile?“_ über [`async` und `await` in der Dokumentation](https://fastapi.tiangolo.com/de/async/#in-a-hurry) an.

### Starten[¶](https://fastapi.tiangolo.com/de/#run-it)

Starten Sie den Server mit:

Über den Befehl `fastapi dev main.py` ...
Der Befehl `fastapi dev` liest Ihre `main.py`-Datei, erkennt die **FastAPI**-App darin und startet einen Server mit [Uvicorn](https://www.uvicorn.dev/).

Standardmäßig wird `fastapi dev` mit aktiviertem Auto-Reload für die lokale Entwicklung gestartet.

Sie können mehr darüber in der [FastAPI CLI Dokumentation](https://fastapi.tiangolo.com/de/fastapi-cli/) lesen.

### Es testen[¶](https://fastapi.tiangolo.com/de/#check-it)

Öffnen Sie Ihren Browser unter [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

Sie sehen die JSON-Response als:

```
{"item_id": 5, "q": "somequery"}
```

Sie haben bereits eine API erstellt, welche:

*   HTTP-Requests auf den _Pfaden_`/` und `/items/{item_id}` entgegennimmt.
*   Beide _Pfade_ nehmen `GET`_Operationen_ (auch bekannt als HTTP-_Methoden_) entgegen.
*   Der _Pfad_`/items/{item_id}` hat einen _Pfad-Parameter_`item_id`, der ein `int` sein sollte.
*   Der _Pfad_`/items/{item_id}` hat einen optionalen `str`-_Query-Parameter_`q`.

### Interaktive API-Dokumentation[¶](https://fastapi.tiangolo.com/de/#interactive-api-docs)

Gehen Sie nun auf [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Sie sehen die automatische interaktive API-Dokumentation (bereitgestellt von [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API-Dokumentation[¶](https://fastapi.tiangolo.com/de/#alternative-api-docs)

Und jetzt gehen Sie auf [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Sie sehen die alternative automatische Dokumentation (bereitgestellt von [ReDoc](https://github.com/Rebilly/ReDoc)):

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

Beispielaktualisierung[¶](https://fastapi.tiangolo.com/de/#example-upgrade)
---------------------------------------------------------------------------

Ändern Sie jetzt die Datei `main.py`, um den Body eines `PUT`-Requests zu empfangen.

Deklarieren Sie den Body mit Standard-Python-Typen, dank Pydantic.

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

Der `fastapi dev`-Server sollte automatisch neu laden.

### Interaktive API-Dokumentation aktualisieren[¶](https://fastapi.tiangolo.com/de/#interactive-api-docs-upgrade)

Gehen Sie jetzt auf [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

*   Die interaktive API-Dokumentation wird automatisch aktualisiert, einschließlich des neuen Bodys:

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   Klicken Sie auf den Button „Try it out“, damit können Sie die Parameter ausfüllen und direkt mit der API interagieren:

![Image 30: Swagger UI Interaktion](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   Klicken Sie dann auf den Button „Execute“, die Benutzeroberfläche wird mit Ihrer API kommunizieren, die Parameter senden, die Ergebnisse erhalten und sie auf dem Bildschirm anzeigen:

![Image 31: Swagger UI Interaktion](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Alternative API-Dokumentation aktualisieren[¶](https://fastapi.tiangolo.com/de/#alternative-api-docs-upgrade)

Und jetzt gehen Sie auf [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

*   Die alternative Dokumentation wird ebenfalls den neuen Query-Parameter und Body widerspiegeln:

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Zusammenfassung[¶](https://fastapi.tiangolo.com/de/#recap)

Zusammengefasst deklarieren Sie **einmal** die Typen von Parametern, Body, usw. als Funktionsparameter.

Das machen Sie mit modernen Standard-Python-Typen.

Sie müssen keine neue Syntax, Methoden oder Klassen einer bestimmten Bibliothek usw. lernen.

Nur Standard-**Python**.

Zum Beispiel für ein `int`:

```
item_id: int
```

oder für ein komplexeres `Item`-Modell:

```
item: Item
```

... und mit dieser einen Deklaration erhalten Sie:

*   Editor-Unterstützung, einschließlich:
    *   Vervollständigung.
    *   Typprüfungen.

*   Validierung von Daten:
    *   Automatische und eindeutige Fehler, wenn die Daten ungültig sind.
    *   Validierung sogar für tief verschachtelte JSON-Objekte.

*   Konvertierung von Eingabedaten: Aus dem Netzwerk kommend, zu Python-Daten und -Typen. Lesen von:
    *   JSON.
    *   Pfad-Parametern.
    *   Query-Parametern.
    *   Cookies.
    *   Headern.
    *   Formularen.
    *   Dateien.

*   Konvertierung von Ausgabedaten: Konvertierung von Python-Daten und -Typen zu Netzwerkdaten (als JSON):
    *   Konvertieren von Python-Typen (`str`, `int`, `float`, `bool`, `list`, usw.).
    *   `datetime`-Objekte.
    *   `UUID`-Objekte.
    *   Datenbankmodelle.
    *   ... und viele mehr.

*   Automatische interaktive API-Dokumentation, einschließlich zwei alternativer Benutzeroberflächen:
    *   Swagger UI.
    *   ReDoc.

* * *

Um auf das vorherige Codebeispiel zurückzukommen, **FastAPI** wird:

*   Validieren, dass es eine `item_id` im Pfad für `GET`- und `PUT`-Requests gibt.
*   Validieren, ob die `item_id` vom Typ `int` für `GET`- und `PUT`-Requests ist.
    *   Falls nicht, sieht der Client einen hilfreichen, klaren Fehler.

*   Prüfen, ob es einen optionalen Query-Parameter namens `q` (wie in `http://127.0.0.1:8000/items/foo?q=somequery`) für `GET`-Requests gibt.
    *   Da der `q`-Parameter mit `= None` deklariert ist, ist er optional.
    *   Ohne das `None` wäre er erforderlich (wie der Body im Fall von `PUT`).

*   Bei `PUT`-Requests an `/items/{item_id}` den Body als JSON lesen:
    *   Prüfen, ob er ein erforderliches Attribut `name` hat, das ein `str` sein muss.
    *   Prüfen, ob er ein erforderliches Attribut `price` hat, das ein `float` sein muss.
    *   Prüfen, ob er ein optionales Attribut `is_offer` hat, das ein `bool` sein muss, falls vorhanden.
    *   All dies würde auch für tief verschachtelte JSON-Objekte funktionieren.

*   Automatisch von und nach JSON konvertieren.
*   Alles mit OpenAPI dokumentieren, welches verwendet werden kann von:
    *   Interaktiven Dokumentationssystemen.
    *   Automatisch Client-Code generierenden Systemen für viele Sprachen.

*   Zwei interaktive Dokumentations-Weboberflächen direkt bereitstellen.

* * *

Wir haben nur an der Oberfläche gekratzt, aber Sie bekommen schon eine Vorstellung davon, wie das Ganze funktioniert.

Versuchen Sie, diese Zeile zu ändern:

```
return {"item_name": item.name, "item_id": item_id}
```

... von:

```
... "item_name": item.name ...
```

... zu:

```
... "item_price": item.price ...
```

... und sehen Sie, wie Ihr Editor die Attribute automatisch vervollständigt und ihre Typen kennt:

![Image 33: Editor Unterstützung](https://fastapi.tiangolo.com/img/vscode-completion.png)

Für ein vollständigeres Beispiel, mit weiteren Funktionen, siehe das [Tutorial – Benutzerhandbuch](https://fastapi.tiangolo.com/de/tutorial/).

**Spoiler-Alarm**: Das Tutorial – Benutzerhandbuch enthält:

*   Deklaration von **Parametern** von anderen verschiedenen Stellen wie: **Header**, **Cookies**, **Formularfelder** und **Dateien**.
*   Wie man **Validierungs-Constraints** wie `maximum_length` oder `regex` setzt.
*   Ein sehr leistungsfähiges und einfach zu bedienendes System für **Dependency Injection**.
*   Sicherheit und Authentifizierung, einschließlich Unterstützung für **OAuth2** mit **JWT-Tokens** und **HTTP Basic** Authentifizierung.
*   Fortgeschrittenere (aber ebenso einfache) Techniken zur Deklaration **tief verschachtelter JSON-Modelle** (dank Pydantic).
*   **GraphQL**-Integration mit [Strawberry](https://strawberry.rocks/) und anderen Bibliotheken.
*   Viele zusätzliche Features (dank Starlette) wie:
    *   **WebSockets**
    *   extrem einfache Tests auf Basis von HTTPX und `pytest`
    *   **CORS**
    *   **Cookie-Sessions**
    *   ... und mehr.

### Ihre App deployen (optional)[¶](https://fastapi.tiangolo.com/de/#deploy-your-app-optional)

Optional können Sie Ihre FastAPI-App in die [FastAPI Cloud](https://fastapicloud.com/) deployen, gehen Sie und treten Sie der Warteliste bei, falls noch nicht geschehen. 🚀

Wenn Sie bereits ein **FastAPI Cloud**-Konto haben (wir haben Sie von der Warteliste eingeladen 😉), können Sie Ihre Anwendung mit einem einzigen Befehl deployen.

Stellen Sie vor dem Deployen sicher, dass Sie eingeloggt sind:

Stellen Sie dann Ihre App bereit:

Das war’s! Jetzt können Sie unter dieser URL auf Ihre App zugreifen. ✨

#### Über FastAPI Cloud[¶](https://fastapi.tiangolo.com/de/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)** wird vom selben Autor und Team hinter **FastAPI** entwickelt.

Es vereinfacht den Prozess des **Erstellens**, **Deployens** und **Zugreifens** auf eine API mit minimalem Aufwand.

Es bringt die gleiche **Developer-Experience** beim Erstellen von Apps mit FastAPI auch zum **Deployment** in der Cloud. 🎉

FastAPI Cloud ist der Hauptsponsor und Finanzierer der _FastAPI and friends_ Open-Source-Projekte. ✨

#### Bei anderen Cloudanbietern deployen[¶](https://fastapi.tiangolo.com/de/#deploy-to-other-cloud-providers)

FastAPI ist Open Source und basiert auf Standards. Sie können FastAPI-Apps bei jedem Cloudanbieter Ihrer Wahl deployen.

Folgen Sie den Anleitungen Ihres Cloudanbieters, um FastAPI-Apps dort bereitzustellen. 🤓

Performanz[¶](https://fastapi.tiangolo.com/de/#performance)
-----------------------------------------------------------

Unabhängige TechEmpower-Benchmarks zeigen **FastAPI**-Anwendungen, die unter Uvicorn laufen, als [eines der schnellsten verfügbaren Python-Frameworks](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), nur hinter Starlette und Uvicorn selbst (intern von FastAPI verwendet). (*)

Um mehr darüber zu erfahren, siehe den Abschnitt [Benchmarks](https://fastapi.tiangolo.com/de/benchmarks/).

Abhängigkeiten[¶](https://fastapi.tiangolo.com/de/#dependencies)
----------------------------------------------------------------

FastAPI hängt von Pydantic und Starlette ab.

### `standard`-Abhängigkeiten[¶](https://fastapi.tiangolo.com/de/#standard-dependencies)

Wenn Sie FastAPI mit `pip install "fastapi[standard]"` installieren, kommt es mit der `standard`-Gruppe optionaler Abhängigkeiten:

Verwendet von Pydantic:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) – für E-Mail-Validierung.

Verwendet von Starlette:

*   [`httpx`](https://www.python-httpx.org/) – erforderlich, wenn Sie den `TestClient` verwenden möchten.
*   [`jinja2`](https://jinja.palletsprojects.com/) – erforderlich, wenn Sie die Default-Template-Konfiguration verwenden möchten.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) – erforderlich, wenn Sie Formulare mittels `request.form()`„parsen“ möchten.

Verwendet von FastAPI:

*   [`uvicorn`](https://www.uvicorn.dev/) – für den Server, der Ihre Anwendung lädt und bereitstellt. Dies umfasst `uvicorn[standard]`, das einige Abhängigkeiten (z. B. `uvloop`) beinhaltet, die für eine Bereitstellung mit hoher Performanz benötigt werden.
*   `fastapi-cli[standard]` – um den `fastapi`-Befehl bereitzustellen.
    *   Dies beinhaltet `fastapi-cloud-cli`, das es Ihnen ermöglicht, Ihre FastAPI-Anwendung auf [FastAPI Cloud](https://fastapicloud.com/) bereitzustellen.

### Ohne `standard`-Abhängigkeiten[¶](https://fastapi.tiangolo.com/de/#without-standard-dependencies)

Wenn Sie die `standard` optionalen Abhängigkeiten nicht einschließen möchten, können Sie mit `pip install fastapi` statt `pip install "fastapi[standard]"` installieren.

### Ohne `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/de/#without-fastapi-cloud-cli)

Wenn Sie FastAPI mit den Standardabhängigkeiten, aber ohne das `fastapi-cloud-cli` installieren möchten, können Sie mit `pip install "fastapi[standard-no-fastapi-cloud-cli]"` installieren.

### Zusätzliche optionale Abhängigkeiten[¶](https://fastapi.tiangolo.com/de/#additional-optional-dependencies)

Es gibt einige zusätzliche Abhängigkeiten, die Sie installieren möchten.

Zusätzliche optionale Pydantic-Abhängigkeiten:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) – für die Verwaltung von Einstellungen.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) – für zusätzliche Typen zur Verwendung mit Pydantic.

Zusätzliche optionale FastAPI-Abhängigkeiten:

*   [`orjson`](https://github.com/ijl/orjson) – erforderlich, wenn Sie `ORJSONResponse` verwenden möchten.
*   [`ujson`](https://github.com/esnme/ultrajson) – erforderlich, wenn Sie `UJSONResponse` verwenden möchten.

Lizenz[¶](https://fastapi.tiangolo.com/de/#license)
---------------------------------------------------

Dieses Projekt ist unter den Bedingungen der MIT-Lizenz lizenziert.
