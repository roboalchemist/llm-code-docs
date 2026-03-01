# Source: https://fastapi.tiangolo.com/fr/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/fr/

Markdown Content:
🌐 Traduction par IA et humains
Cette traduction a été réalisée par une IA guidée par des humains. 🤝

Elle peut contenir des erreurs d'interprétation du sens original, ou paraître peu naturelle, etc. 🤖

Vous pouvez améliorer cette traduction en [nous aidant à mieux guider le LLM d'IA](https://fastapi.tiangolo.com/fr/contributing/#translations).

[Version anglaise](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/fr)

_Framework FastAPI, haute performance, facile à apprendre, rapide à coder, prêt pour la production_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Documentation** : [https://fastapi.tiangolo.com/fr](https://fastapi.tiangolo.com/fr)

**Code Source** : [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI est un framework web moderne et rapide (haute performance) pour la création d'API avec Python, basé sur les annotations de type standard de Python.

Les principales fonctionnalités sont :

*   **Rapide** : très hautes performances, au niveau de **NodeJS** et **Go** (grâce à Starlette et Pydantic). [L'un des frameworks Python les plus rapides](https://fastapi.tiangolo.com/fr/#performance).
*   **Rapide à coder** : augmente la vitesse de développement des fonctionnalités d'environ 200 % à 300 %. *
*   **Moins de bugs** : réduit d'environ 40 % les erreurs induites par le développeur. *
*   **Intuitif** : excellente compatibilité avec les éditeurs. Autocomplétion partout. Moins de temps passé à déboguer.
*   **Facile** : conçu pour être facile à utiliser et à apprendre. Moins de temps passé à lire les documents.
*   **Concis** : diminue la duplication de code. Plusieurs fonctionnalités à partir de chaque déclaration de paramètre. Moins de bugs.
*   **Robuste** : obtenez un code prêt pour la production. Avec une documentation interactive automatique.
*   **Basé sur des normes** : basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (précédemment connu sous le nom de Swagger) et [JSON Schema](https://json-schema.org/).

* estimation basée sur des tests d'une équipe de développement interne, construisant des applications de production.

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Sponsors Or et Argent[¶](https://fastapi.tiangolo.com/fr/#gold-and-silver-sponsors "Permanent link")

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Autres sponsors](https://fastapi.tiangolo.com/fr/fastapi-people/#sponsors)

Opinions[¶](https://fastapi.tiangolo.com/fr/#opinions "Permanent link")
-----------------------------------------------------------------------

« _[...] J'utilise beaucoup **FastAPI** ces derniers temps. [...] Je prévois de l'utiliser dans mon équipe pour tous les **services de ML chez Microsoft**. Certains d'entre eux sont intégrés au cœur de **Windows** et à certains produits **Office**._ »

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

« _Nous avons adopté la bibliothèque **FastAPI** pour créer un serveur **REST** qui peut être interrogé pour obtenir des **prédictions**. [pour Ludwig]_ »

Piero Molino, Yaroslav Dudin, et Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

« _**Netflix** est heureux d'annoncer la publication en open source de notre framework d'orchestration de **gestion de crise** : **Dispatch** ! [construit avec **FastAPI**]_ »

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

« _Je suis plus qu'enthousiaste à propos de **FastAPI**. C'est tellement fun !_ »

* * *

« _Honnêtement, ce que vous avez construit a l'air super solide et soigné. À bien des égards, c'est ce que je voulais que **Hug** soit — c'est vraiment inspirant de voir quelqu'un construire ça._ »

Timothy Crosley - **Créateur de [Hug](https://github.com/hugapi/hug)**[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

« _Si vous cherchez à apprendre un **framework moderne** pour créer des APIs REST, regardez **FastAPI** [...] C'est rapide, facile à utiliser et facile à apprendre [...]_ »

« _Nous sommes passés à **FastAPI** pour nos **APIs** [...] Je pense que vous l'aimerez [...]_ »

* * *

« _Si quelqu'un cherche à construire une API Python de production, je recommande vivement **FastAPI**. Il est **magnifiquement conçu**, **simple à utiliser** et **hautement scalable**. Il est devenu un **composant clé** de notre stratégie de développement API-first et alimente de nombreuses automatisations et services tels que notre ingénieur TAC virtuel._ »

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

Mini documentaire FastAPI[¶](https://fastapi.tiangolo.com/fr/#fastapi-mini-documentary "Permanent link")
--------------------------------------------------------------------------------------------------------

Un [mini documentaire FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE) est sorti fin 2025, vous pouvez le regarder en ligne :

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, le FastAPI des CLIs[¶](https://fastapi.tiangolo.com/fr/#typer-the-fastapi-of-clis "Permanent link")
--------------------------------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Si vous construisez une application CLI à utiliser dans un terminal au lieu d'une API web, regardez [**Typer**](https://typer.tiangolo.com/).

**Typer** est le petit frère de FastAPI. Et il est destiné à être le **FastAPI des CLIs**. ⌨️ 🚀

Prérequis[¶](https://fastapi.tiangolo.com/fr/#requirements "Permanent link")
----------------------------------------------------------------------------

FastAPI repose sur les épaules de géants :

*   [Starlette](https://www.starlette.dev/) pour les parties web.
*   [Pydantic](https://docs.pydantic.dev/) pour les parties données.

Installation[¶](https://fastapi.tiangolo.com/fr/#installation "Permanent link")
-------------------------------------------------------------------------------

Créez et activez un [environnement virtuel](https://fastapi.tiangolo.com/fr/virtual-environments/) puis installez FastAPI :

```
$ pip install "fastapi[standard]"

---> 100%
```

**Remarque** : Vous devez vous assurer de mettre « fastapi[standard] » entre guillemets pour garantir que cela fonctionne dans tous les terminaux.

Exemple[¶](https://fastapi.tiangolo.com/fr/#example "Permanent link")
---------------------------------------------------------------------

### Créer[¶](https://fastapi.tiangolo.com/fr/#create-it "Permanent link")

Créez un fichier `main.py` avec :

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

Ou utilisez `async def`...
Si votre code utilise `async` / `await`, utilisez `async def` :

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

**Remarque** :

Si vous ne savez pas, consultez la section « Vous êtes pressés ? » à propos de [`async` et `await` dans la documentation](https://fastapi.tiangolo.com/fr/async/#in-a-hurry).

### Lancer[¶](https://fastapi.tiangolo.com/fr/#run-it "Permanent link")

Lancez le serveur avec :

```
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

À propos de la commande `fastapi dev main.py`...
La commande `fastapi dev` lit votre fichier `main.py`, détecte l'application **FastAPI** qu'il contient et lance un serveur avec [Uvicorn](https://www.uvicorn.dev/).

Par défaut, `fastapi dev` démarre avec le rechargement automatique activé pour le développement local.

Vous pouvez en savoir plus dans la [documentation de la CLI FastAPI](https://fastapi.tiangolo.com/fr/fastapi-cli/).

### Vérifier[¶](https://fastapi.tiangolo.com/fr/#check-it "Permanent link")

Ouvrez votre navigateur à l'adresse [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

Vous verrez la réponse JSON :

```
{"item_id": 5, "q": "somequery"}
```

Vous avez déjà créé une API qui :

*   Reçoit des requêtes HTTP sur les _chemins_`/` et `/items/{item_id}`.
*   Les deux _chemins_ acceptent des _opérations_`GET` (également connues sous le nom de _méthodes_ HTTP).
*   Le _chemin_`/items/{item_id}` a un _paramètre de chemin_`item_id` qui doit être un `int`.
*   Le _chemin_`/items/{item_id}` a un _paramètre de requête_ optionnel `q` de type `str`.

### Documentation API interactive[¶](https://fastapi.tiangolo.com/fr/#interactive-api-docs "Permanent link")

Maintenant, rendez-vous sur [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Vous verrez la documentation interactive automatique de l'API (fournie par [Swagger UI](https://github.com/swagger-api/swagger-ui)) :

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Documentation API alternative[¶](https://fastapi.tiangolo.com/fr/#alternative-api-docs "Permanent link")

Et maintenant, rendez-vous sur [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Vous verrez la documentation alternative automatique (fournie par [ReDoc](https://github.com/Rebilly/ReDoc)) :

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

Mettre à niveau l'exemple[¶](https://fastapi.tiangolo.com/fr/#example-upgrade "Permanent link")
-----------------------------------------------------------------------------------------------

Modifiez maintenant le fichier `main.py` pour recevoir un corps depuis une requête `PUT`.

Déclarez le corps en utilisant les types Python standard, grâce à Pydantic.

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

Le serveur `fastapi dev` devrait se recharger automatiquement.

### Mettre à niveau la documentation API interactive[¶](https://fastapi.tiangolo.com/fr/#interactive-api-docs-upgrade "Permanent link")

Maintenant, rendez-vous sur [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

*   La documentation interactive de l'API sera automatiquement mise à jour, y compris le nouveau corps :

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   Cliquez sur le bouton « Try it out », il vous permet de renseigner les paramètres et d'interagir directement avec l'API :

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   Cliquez ensuite sur le bouton « Execute », l'interface utilisateur communiquera avec votre API, enverra les paramètres, obtiendra les résultats et les affichera à l'écran :

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Mettre à niveau la documentation API alternative[¶](https://fastapi.tiangolo.com/fr/#alternative-api-docs-upgrade "Permanent link")

Et maintenant, rendez-vous sur [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

*   La documentation alternative reflètera également le nouveau paramètre de requête et le nouveau corps :

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### En résumé[¶](https://fastapi.tiangolo.com/fr/#recap "Permanent link")

En résumé, vous déclarez **une fois** les types de paramètres, le corps, etc. en tant que paramètres de fonction.

Vous faites cela avec les types Python standard modernes.

Vous n'avez pas à apprendre une nouvelle syntaxe, les méthodes ou les classes d'une bibliothèque spécifique, etc.

Juste du **Python** standard.

Par exemple, pour un `int` :

```
item_id: int
```

ou pour un modèle `Item` plus complexe :

```
item: Item
```

... et avec cette déclaration unique, vous obtenez :

*   Une assistance dans l'éditeur, notamment :
    *   l'autocomplétion.
    *   la vérification des types.

*   La validation des données :
    *   des erreurs automatiques et claires lorsque les données ne sont pas valides.
    *   une validation même pour les objets JSON profondément imbriqués.

*   Conversion des données d'entrée : venant du réseau vers les données et types Python. Lecture depuis :
    *   JSON.
    *   Paramètres de chemin.
    *   Paramètres de requête.
    *   Cookies.
    *   En-têtes.
    *   Formulaires.
    *   Fichiers.

*   Conversion des données de sortie : conversion des données et types Python en données réseau (au format JSON) :
    *   Conversion des types Python (`str`, `int`, `float`, `bool`, `list`, etc).
    *   Objets `datetime`.
    *   Objets `UUID`.
    *   Modèles de base de données.
    *   ... et bien plus.

*   Documentation API interactive automatique, avec 2 interfaces utilisateur au choix :
    *   Swagger UI.
    *   ReDoc.

* * *

Pour revenir à l'exemple de code précédent, **FastAPI** va :

*   Valider la présence d'un `item_id` dans le chemin pour les requêtes `GET` et `PUT`.
*   Valider que `item_id` est de type `int` pour les requêtes `GET` et `PUT`.
    *   Si ce n'est pas le cas, le client verra une erreur utile et claire.

*   Vérifier s'il existe un paramètre de requête optionnel nommé `q` (comme dans `http://127.0.0.1:8000/items/foo?q=somequery`) pour les requêtes `GET`.
    *   Comme le paramètre `q` est déclaré avec `= None`, il est optionnel.
    *   Sans le `None`, il serait requis (comme l'est le corps dans le cas de `PUT`).

*   Pour les requêtes `PUT` vers `/items/{item_id}`, lire le corps au format JSON :
    *   Vérifier qu'il a un attribut obligatoire `name` qui doit être un `str`.
    *   Vérifier qu'il a un attribut obligatoire `price` qui doit être un `float`.
    *   Vérifier qu'il a un attribut optionnel `is_offer`, qui doit être un `bool`, s'il est présent.
    *   Tout cela fonctionne également pour les objets JSON profondément imbriqués.

*   Convertir automatiquement depuis et vers JSON.
*   Tout documenter avec OpenAPI, qui peut être utilisé par :
    *   des systèmes de documentation interactive.
    *   des systèmes de génération automatique de clients, pour de nombreux langages.

*   Fournir directement 2 interfaces web de documentation interactive.

* * *

Nous n'avons fait qu'effleurer la surface, mais vous avez déjà une idée de la façon dont tout fonctionne.

Essayez de changer la ligne contenant :

```
return {"item_name": item.name, "item_id": item_id}
```

... de :

```
... "item_name": item.name ...
```

... à :

```
... "item_price": item.price ...
```

... et voyez comment votre éditeur complète automatiquement les attributs et connaît leurs types :

![Image 33: compatibilité éditeur](https://fastapi.tiangolo.com/img/vscode-completion.png)

Pour un exemple plus complet comprenant plus de fonctionnalités, voir le [Tutoriel - Guide utilisateur](https://fastapi.tiangolo.com/fr/tutorial/).

**Alerte spoiler** : le tutoriel - guide utilisateur inclut :

*   Déclaration de **paramètres** provenant d'autres emplacements comme : **en-têtes**, **cookies**, **champs de formulaire** et **fichiers**.
*   Comment définir des **contraintes de validation** comme `maximum_length` ou `regex`.
*   Un système **d'injection de dépendances** très puissant et facile à utiliser.
*   Sécurité et authentification, y compris la prise en charge de **OAuth2** avec des **JWT tokens** et l'authentification **HTTP Basic**.
*   Des techniques plus avancées (mais tout aussi faciles) pour déclarer des **modèles JSON profondément imbriqués** (grâce à Pydantic).
*   Intégration **GraphQL** avec [Strawberry](https://strawberry.rocks/) et d'autres bibliothèques.
*   De nombreuses fonctionnalités supplémentaires (grâce à Starlette) comme :
    *   **WebSockets**
    *   des tests extrêmement faciles basés sur HTTPX et `pytest`
    *   **CORS**
    *   **Cookie Sessions**
    *   ... et plus encore.

### Déployer votre application (optionnel)[¶](https://fastapi.tiangolo.com/fr/#deploy-your-app-optional "Permanent link")

Vous pouvez, si vous le souhaitez, déployer votre application FastAPI sur [FastAPI Cloud](https://fastapicloud.com/), allez vous inscrire sur la liste d'attente si ce n'est pas déjà fait. 🚀

Si vous avez déjà un compte **FastAPI Cloud** (nous vous avons invité depuis la liste d'attente 😉), vous pouvez déployer votre application avec une seule commande.

Avant de déployer, assurez-vous d'être connecté :

```
$ fastapi login

You are logged in to FastAPI Cloud 🚀
```

Puis déployez votre application :

```
$ fastapi deploy

Deploying to FastAPI Cloud...

✅ Deployment successful!

🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev
```

C'est tout ! Vous pouvez maintenant accéder à votre application à cette URL. ✨

#### À propos de FastAPI Cloud[¶](https://fastapi.tiangolo.com/fr/#about-fastapi-cloud "Permanent link")

**[FastAPI Cloud](https://fastapicloud.com/)** est construit par le même auteur et la même équipe derrière **FastAPI**.

Il simplifie le processus de **construction**, de **déploiement** et **d'accès** à une API avec un effort minimal.

Il apporte la même **expérience développeur** de la création d'applications avec FastAPI au **déploiement** dans le cloud. 🎉

FastAPI Cloud est le principal sponsor et financeur des projets open source _FastAPI and friends_. ✨

#### Déployer sur d'autres fournisseurs cloud[¶](https://fastapi.tiangolo.com/fr/#deploy-to-other-cloud-providers "Permanent link")

FastAPI est open source et basé sur des standards. Vous pouvez déployer des applications FastAPI sur n'importe quel fournisseur cloud de votre choix.

Suivez les guides de votre fournisseur cloud pour y déployer des applications FastAPI. 🤓

Performance[¶](https://fastapi.tiangolo.com/fr/#performance "Permanent link")
-----------------------------------------------------------------------------

Les benchmarks TechEmpower indépendants montrent que les applications **FastAPI** s'exécutant sous Uvicorn sont [parmi les frameworks Python les plus rapides](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), juste derrière Starlette et Uvicorn eux-mêmes (utilisés en interne par FastAPI). (*)

Pour en savoir plus, consultez la section [Benchmarks](https://fastapi.tiangolo.com/fr/benchmarks/).

Dépendances[¶](https://fastapi.tiangolo.com/fr/#dependencies "Permanent link")
------------------------------------------------------------------------------

FastAPI dépend de Pydantic et Starlette.

### Dépendances `standard`[¶](https://fastapi.tiangolo.com/fr/#standard-dependencies "Permanent link")

Lorsque vous installez FastAPI avec `pip install "fastapi[standard]"`, il inclut le groupe `standard` de dépendances optionnelles :

Utilisées par Pydantic :

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - pour la validation des adresses e-mail.

Utilisées par Starlette :

*   [`httpx`](https://www.python-httpx.org/) - Obligatoire si vous souhaitez utiliser le `TestClient`.
*   [`jinja2`](https://jinja.palletsprojects.com/) - Obligatoire si vous souhaitez utiliser la configuration de template par défaut.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - Obligatoire si vous souhaitez prendre en charge l’« parsing » de formulaires avec `request.form()`.

Utilisées par FastAPI :

*   [`uvicorn`](https://www.uvicorn.dev/) - pour le serveur qui charge et sert votre application. Cela inclut `uvicorn[standard]`, qui comprend certaines dépendances (par ex. `uvloop`) nécessaires pour une haute performance.
*   `fastapi-cli[standard]` - pour fournir la commande `fastapi`.
    *   Cela inclut `fastapi-cloud-cli`, qui vous permet de déployer votre application FastAPI sur [FastAPI Cloud](https://fastapicloud.com/).

### Sans les dépendances `standard`[¶](https://fastapi.tiangolo.com/fr/#without-standard-dependencies "Permanent link")

Si vous ne souhaitez pas inclure les dépendances optionnelles `standard`, vous pouvez installer avec `pip install fastapi` au lieu de `pip install "fastapi[standard]"`.

### Sans `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/fr/#without-fastapi-cloud-cli "Permanent link")

Si vous souhaitez installer FastAPI avec les dépendances standard mais sans `fastapi-cloud-cli`, vous pouvez installer avec `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.

### Dépendances optionnelles supplémentaires[¶](https://fastapi.tiangolo.com/fr/#additional-optional-dependencies "Permanent link")

Il existe des dépendances supplémentaires que vous pourriez vouloir installer.

Dépendances optionnelles supplémentaires pour Pydantic :

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - pour la gestion des paramètres.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - pour des types supplémentaires à utiliser avec Pydantic.

Dépendances optionnelles supplémentaires pour FastAPI :

*   [`orjson`](https://github.com/ijl/orjson) - Obligatoire si vous souhaitez utiliser `ORJSONResponse`.
*   [`ujson`](https://github.com/esnme/ultrajson) - Obligatoire si vous souhaitez utiliser `UJSONResponse`.

Licence[¶](https://fastapi.tiangolo.com/fr/#license "Permanent link")
---------------------------------------------------------------------

Ce projet est soumis aux termes de la licence MIT.
