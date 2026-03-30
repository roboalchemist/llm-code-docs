Package com.github.javafaker

## Class Faker

- java.lang.Object

- 

  - com.github.javafaker.Faker

- 

---

```
public class Faker
extends java.lang.Object
```

Provides utility methods for generating fake strings, such as names, phone
 numbers, addresses. generate random strings with given patterns

Author:
ren

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`Faker()`
 

`Faker​(FakeValuesService fakeValuesService,
     RandomService random)`
 

`Faker​(java.util.Locale locale)`
 

`Faker​(java.util.Locale locale,
     RandomService randomService)`
 

`Faker​(java.util.Locale locale,
     java.util.Random random)`
 

`Faker​(java.util.Random random)`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Address`
`address()`
 

`Ancient`
`ancient()`
 

`Animal`
`animal()`
 

`App`
`app()`
 

`AquaTeenHungerForce`
`aquaTeenHungerForce()`
 

`Artist`
`artist()`
 

`Avatar`
`avatar()`
 

`Aviation`
`aviation()`
 

`BackToTheFuture`
`backToTheFuture()`
 

`Beer`
`beer()`
 

`Book`
`book()`
 

`Bool`
`bool()`
 

`java.lang.String`
`bothify​(java.lang.String string)`

Applies both a `numerify(String)` and a `letterify(String)`
 over the incoming string.

`java.lang.String`
`bothify​(java.lang.String string,
       boolean isUpper)`

Applies both a `numerify(String)` and a `letterify(String)`
 over the incoming string.

`Buffy`
`buffy()`
 

`Business`
`business()`
 

`Cat`
`cat()`
 

`ChuckNorris`
`chuckNorris()`
 

`Code`
`code()`
 

`Color`
`color()`
 

`Commerce`
`commerce()`
 

`Company`
`company()`
 

`Country`
`country()`
 

`Crypto`
`crypto()`
 

`Currency`
`currency()`
 

`DateAndTime`
`date()`
 

`Demographic`
`demographic()`
 

`Dog`
`dog()`
 

`DragonBall`
`dragonBall()`
 

`Dune`
`dune()`
 

`Educator`
`educator()`
 

`ElderScrolls`
`elderScrolls()`
 

`Esports`
`esports()`
 

`java.lang.String`
`expression​(java.lang.String expression)`

Allows the evaluation of native YML expressions to allow you to build your own.

`File`
`file()`
 

`Finance`
`finance()`
 

`Food`
`food()`
 

`Friends`
`friends()`
 

`FunnyName`
`funnyName()`
 

`GameOfThrones`
`gameOfThrones()`
 

`Hacker`
`hacker()`
 

`HarryPotter`
`harryPotter()`
 

`Hipster`
`hipster()`
 

`HitchhikersGuideToTheGalaxy`
`hitchhikersGuideToTheGalaxy()`
 

`Hobbit`
`hobbit()`
 

`HowIMetYourMother`
`howIMetYourMother()`
 

`IdNumber`
`idNumber()`
 

`static Faker`
`instance()`

Constructs Faker instance with default argument.

`static Faker`
`instance​(java.util.Locale locale)`

Constructs Faker instance with provided `Locale`.

`static Faker`
`instance​(java.util.Locale locale,
        java.util.Random random)`

Constructs Faker instance with provided `Locale` and `Random`.

`static Faker`
`instance​(java.util.Random random)`

Constructs Faker instance with provided `Random`.

`Internet`
`internet()`
 

`Job`
`job()`
 

`LeagueOfLegends`
`leagueOfLegends()`
 

`Lebowski`
`lebowski()`
 

`java.lang.String`
`letterify​(java.lang.String letterString)`

Returns a string with the '?' characters in the parameter replaced with random alphabetic
 characters.

`java.lang.String`
`letterify​(java.lang.String letterString,
         boolean isUpper)`

Returns a string with the '?' characters in the parameter replaced with random alphabetic
 characters.

`LordOfTheRings`
`lordOfTheRings()`
 

`Lorem`
`lorem()`
 

`Matz`
`matz()`
 

`Medical`
`medical()`
 

`Music`
`music()`
 

`Name`
`name()`
 

`Nation`
`nation()`
 

`Number`
`number()`
 

`java.lang.String`
`numerify​(java.lang.String numberString)`

Returns a string with the '#' characters in the parameter replaced with random digits between 0-9 inclusive.

`Options`
`options()`
 

`Overwatch`
`overwatch()`
 

`PhoneNumber`
`phoneNumber()`
 

`Pokemon`
`pokemon()`
 

`PrincessBride`
`princessBride()`
 

`ProgrammingLanguage`
`programmingLanguage()`
 

`RandomService`
`random()`
 

`java.lang.String`
`regexify​(java.lang.String regex)`

Generates a String that matches the given regular expression.

`Relationships`
`relationships()`
 

`java.lang.String`
`resolve​(java.lang.String key)`
 

`RickAndMorty`
`rickAndMorty()`
 

`Robin`
`robin()`
 

`RockBand`
`rockBand()`
 

`Shakespeare`
`shakespeare()`
 

`SlackEmoji`
`slackEmoji()`
 

`Space`
`space()`
 

`StarTrek`
`starTrek()`
 

`Stock`
`stock()`
 

`Superhero`
`superhero()`
 

`Team`
`team()`
 

`TwinPeaks`
`twinPeaks()`
 

`University`
`university()`
 

`Weather`
`weather()`
 

`Witcher`
`witcher()`
 

`Yoda`
`yoda()`
 

`Zelda`
`zelda()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Faker

```
public Faker()
```

    - 

#### Faker

```
public Faker​(java.util.Locale locale)
```

    - 

#### Faker

```
public Faker​(java.util.Random random)
```

    - 

#### Faker

```
public Faker​(java.util.Locale locale,
             java.util.Random random)
```

    - 

#### Faker

```
public Faker​(java.util.Locale locale,
             RandomService randomService)
```

    - 

#### Faker

```
public Faker​(FakeValuesService fakeValuesService,
             RandomService random)
```

  - 

### Method Detail

    - 

#### instance

```
public static Faker instance()
```

Constructs Faker instance with default argument.

Returns:
`Faker()`

    - 

#### instance

```
public static Faker instance​(java.util.Locale locale)
```

Constructs Faker instance with provided `Locale`.

Parameters:
`locale` - - `Locale`
Returns:
`Faker(Locale)`

    - 

#### instance

```
public static Faker instance​(java.util.Random random)
```

Constructs Faker instance with provided `Random`.

Parameters:
`random` - - `Random`
Returns:
`Faker(Random)`

    - 

#### instance

```
public static Faker instance​(java.util.Locale locale,
                             java.util.Random random)
```

Constructs Faker instance with provided `Locale` and `Random`.

Parameters:
`locale` - - `Locale`
`random` - - `Random`
Returns:
`Faker(Locale, Random)`

    - 

#### numerify

```
public java.lang.String numerify​(java.lang.String numberString)
```

Returns a string with the '#' characters in the parameter replaced with random digits between 0-9 inclusive.
 

 For example, the string "ABC##EFG" could be replaced with a string like "ABC99EFG".

Parameters:
`numberString` - 
Returns:

    - 

#### letterify

```
public java.lang.String letterify​(java.lang.String letterString)
```

Returns a string with the '?' characters in the parameter replaced with random alphabetic
 characters.
 

 For example, the string "12??34" could be replaced with a string like "12AB34".

Parameters:
`letterString` - 
Returns:

    - 

#### letterify

```
public java.lang.String letterify​(java.lang.String letterString,
                                  boolean isUpper)
```

Returns a string with the '?' characters in the parameter replaced with random alphabetic
 characters.
 

 For example, the string "12??34" could be replaced with a string like "12AB34".

Parameters:
`letterString` - 
`isUpper` - 
Returns:

    - 

#### bothify

```
public java.lang.String bothify​(java.lang.String string)
```

Applies both a `numerify(String)` and a `letterify(String)`
 over the incoming string.

Parameters:
`string` - 
Returns:

    - 

#### bothify

```
public java.lang.String bothify​(java.lang.String string,
                                boolean isUpper)
```

Applies both a `numerify(String)` and a `letterify(String)`
 over the incoming string.

Parameters:
`string` - 
`isUpper` - 
Returns:

    - 

#### regexify

```
public java.lang.String regexify​(java.lang.String regex)
```

Generates a String that matches the given regular expression.

    - 

#### random

```
public RandomService random()
```

    - 

#### currency

```
public Currency currency()
```

    - 

#### ancient

```
public Ancient ancient()
```

    - 

#### app

```
public App app()
```

    - 

#### artist

```
public Artist artist()
```

    - 

#### avatar

```
public Avatar avatar()
```

    - 

#### aviation

```
public Aviation aviation()
```

    - 

#### music

```
public Music music()
```

    - 

#### name

```
public Name name()
```

    - 

#### number

```
public Number number()
```

    - 

#### internet

```
public Internet internet()
```

    - 

#### phoneNumber

```
public PhoneNumber phoneNumber()
```

    - 

#### pokemon

```
public Pokemon pokemon()
```

    - 

#### lorem

```
public Lorem lorem()
```

    - 

#### address

```
public Address address()
```

    - 

#### book

```
public Book book()
```

    - 

#### buffy

```
public Buffy buffy()
```

    - 

#### business

```
public Business business()
```

    - 

#### chuckNorris

```
public ChuckNorris chuckNorris()
```

    - 

#### color

```
public Color color()
```

    - 

#### commerce

```
public Commerce commerce()
```

    - 

#### company

```
public Company company()
```

    - 

#### crypto

```
public Crypto crypto()
```

    - 

#### hacker

```
public Hacker hacker()
```

    - 

#### idNumber

```
public IdNumber idNumber()
```

    - 

#### options

```
public Options options()
```

    - 

#### code

```
public Code code()
```

    - 

#### file

```
public File file()
```

    - 

#### finance

```
public Finance finance()
```

    - 

#### food

```
public Food food()
```

    - 

#### elderScrolls

```
public ElderScrolls elderScrolls()
```

    - 

#### gameOfThrones

```
public GameOfThrones gameOfThrones()
```

    - 

#### date

```
public DateAndTime date()
```

    - 

#### demographic

```
public Demographic demographic()
```

    - 

#### dog

```
public Dog dog()
```

    - 

#### educator

```
public Educator educator()
```

    - 

#### slackEmoji

```
public SlackEmoji slackEmoji()
```

    - 

#### shakespeare

```
public Shakespeare shakespeare()
```

    - 

#### space

```
public Space space()
```

    - 

#### superhero

```
public Superhero superhero()
```

    - 

#### bool

```
public Bool bool()
```

    - 

#### team

```
public Team team()
```

    - 

#### beer

```
public Beer beer()
```

    - 

#### university

```
public University university()
```

    - 

#### cat

```
public Cat cat()
```

    - 

#### stock

```
public Stock stock()
```

    - 

#### lordOfTheRings

```
public LordOfTheRings lordOfTheRings()
```

    - 

#### zelda

```
public Zelda zelda()
```

    - 

#### harryPotter

```
public HarryPotter harryPotter()
```

    - 

#### rockBand

```
public RockBand rockBand()
```

    - 

#### esports

```
public Esports esports()
```

    - 

#### friends

```
public Friends friends()
```

    - 

#### hipster

```
public Hipster hipster()
```

    - 

#### job

```
public Job job()
```

    - 

#### twinPeaks

```
public TwinPeaks twinPeaks()
```

    - 

#### rickAndMorty

```
public RickAndMorty rickAndMorty()
```

    - 

#### yoda

```
public Yoda yoda()
```

    - 

#### matz

```
public Matz matz()
```

    - 

#### witcher

```
public Witcher witcher()
```

    - 

#### dragonBall

```
public DragonBall dragonBall()
```

    - 

#### funnyName

```
public FunnyName funnyName()
```

    - 

#### hitchhikersGuideToTheGalaxy

```
public HitchhikersGuideToTheGalaxy hitchhikersGuideToTheGalaxy()
```

    - 

#### hobbit

```
public Hobbit hobbit()
```

    - 

#### howIMetYourMother

```
public HowIMetYourMother howIMetYourMother()
```

    - 

#### leagueOfLegends

```
public LeagueOfLegends leagueOfLegends()
```

    - 

#### overwatch

```
public Overwatch overwatch()
```

    - 

#### robin

```
public Robin robin()
```

    - 

#### starTrek

```
public StarTrek starTrek()
```

    - 

#### weather

```
public Weather weather()
```

    - 

#### lebowski

```
public Lebowski lebowski()
```

    - 

#### medical

```
public Medical medical()
```

    - 

#### country

```
public Country country()
```

    - 

#### animal

```
public Animal animal()
```

    - 

#### backToTheFuture

```
public BackToTheFuture backToTheFuture()
```

    - 

#### princessBride

```
public PrincessBride princessBride()
```

    - 

#### relationships

```
public Relationships relationships()
```

    - 

#### nation

```
public Nation nation()
```

    - 

#### dune

```
public Dune dune()
```

    - 

#### aquaTeenHungerForce

```
public AquaTeenHungerForce aquaTeenHungerForce()
```

    - 

#### programmingLanguage

```
public ProgrammingLanguage programmingLanguage()
```

    - 

#### resolve

```
public java.lang.String resolve​(java.lang.String key)
```

    - 

#### expression

```
public java.lang.String expression​(java.lang.String expression)
```

Allows the evaluation of native YML expressions to allow you to build your own.
 

 The following are valid expressions:
 

 
      - #{regexify '(a|b){2,3}'}
 
      - #{regexify '\\.\\*\\?\\+'}
 
      - #{bothify '????','false'}
 
      - #{Name.first_name} #{Name.first_name} #{Name.last_name}
 
      - #{number.number_between '1','10'}
 

Parameters:
`expression` - (see examples above)
Returns:
the evaluated string expression
Throws:
`java.lang.RuntimeException` - if unable to evaluate the expression