# Source: https://bulma.io/documentation/features/skeletons/

Title: Skeletons in Bulma

URL Source: https://bulma.io/documentation/features/skeletons/

Markdown Content:
A skeleton loader is a loading state that acts as a **placeholder** for content in an interface. Bulma v1 ships with 2 skeleton elements, and skeleton variants for most Bulma components.

All skeleton loaders share these CSS variables:

```
:root {
  --bulma-skeleton-background: var(--bulma-border);
  --bulma-skeleton-radius: var(--bulma-radius-small);
  --bulma-skeleton-block-min-height: 4.5em;
  --bulma-skeleton-lines-gap: 0.75em;
  --bulma-skeleton-line-height: 0.75em;
}
```

### Skeleton Block [#](https://bulma.io/documentation/features/skeletons/#skeleton-block)

The skeleton block is a simple block element with a pulsating background. It has a minimum height of `4.5em`.

Example

HTML

`<div class="skeleton-block"></div>`

If you insert text inside this block, you can make its height responsive:

Example

Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula ut id elit.

HTML

```
<div class="skeleton-block">
  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
  Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh,
  ut fermentum massa justo sit amet risus. Donec sed odio dui.
  Nullam quis risus eget urna mollis ornare vel eu leo.
  Cum sociis natoque penatibus et magnis dis parturient montes,
  nascetur ridiculus mus. Nullam id dolor id
  nibh ultricies vehicula ut id elit.
</div>
```

### Skeleton Lines [#](https://bulma.io/documentation/features/skeletons/#skeleton-lines)

The skeleton lines element is a loading element which resembles a **paragraph**. Each `<div></div>` will render as a separate loading line.

Example

HTML

```
<div class="skeleton-lines">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
```

### Bulma components with skeletons [#](https://bulma.io/documentation/features/skeletons/#bulma-components-with-skeletons)

Most Bulma elements and components have a skeleton variant, which can be enabled by adding either the `is-skeleton` or `has-skeleton` modifier.

#### Button [#](https://bulma.io/documentation/features/skeletons/#button)

Example

HTML

```
<div class="buttons">
  <button class="button is-skeleton">Button</button>
  <button class="button is-link is-skeleton">Link</button>
  <button class="button is-primary is-skeleton">Primary</button>
  <button class="button is-success is-skeleton">Success</button>
  <button class="button is-info is-skeleton">Info</button>
  <button class="button is-warning is-skeleton">Warning</button>
  <button class="button is-danger is-skeleton">Danger</button>
</div>
```

#### Icon [#](https://bulma.io/documentation/features/skeletons/#icon)

Example

HTML

```
<span class="icon is-skeleton">
  <i class="fas fa-reply"></i>
</span>
```

#### Image [#](https://bulma.io/documentation/features/skeletons/#image)

Example

HTML

```
<figure class="image is-16x16 is-skeleton">
  <img alt="Placeholder" src="https://placehold.co/16x16">
</figure>

<figure class="image is-32x32 is-skeleton">
  <img alt="Placeholder" src="https://placehold.co/32x32">
</figure>

<figure class="image is-64x64 is-skeleton">
  <img alt="Placeholder" src="https://placehold.co/64x64">
</figure>

<figure class="image is-128x128 is-skeleton">
  <img alt="Placeholder" src="https://placehold.co/128x128">
</figure>
```

#### Media Object [#](https://bulma.io/documentation/features/skeletons/#media-object)

Example

![Image 1: Placeholder image](https://placehold.co/128x128)

**John Smith**@johnsmith 31m

 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.

HTML

```
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64 is-skeleton">
      <img src="https://placehold.co/128x128" alt="Placeholder image">
    </p>
  </figure>
  <div class="media-content">
    <div class="content is-skeleton">
      <p>
        <strong>John Smith</strong> <small>@johnsmith</small> <small>31m</small>
        <br>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor
        sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus est non commodo luctus,
        nisi erat porttitor ligula, eget lacinia odio sem nec elit
        vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.
      </p>
    </div>
    <nav class="level is-mobile">
      <div class="level-left">
        <a class="level-item"><span class="icon is-small is-skeleton"><i class="fas fa-reply"></i></span></a>
        <a class="level-item"><span class="icon is-small is-skeleton"><i class="fas fa-retweet"></i></span></a>
        <a class="level-item"><span class="icon is-small is-skeleton"><i class="fas fa-heart"></i></span></a>
      </div>
    </nav>
  </div>
  <div class="media-right">
    <button aria-label="delete" class="delete is-skeleton"></button>
  </div>
</article>
```

Example

![Image 2: Placeholder image](https://placehold.co/128x128)

Press enter to submit

HTML

```
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64 is-skeleton">
      <img src="https://placehold.co/128x128" alt="Placeholder image">
    </p>
  </figure>
  <div class="media-content">
    <div class="field">
      <p class="control">
        <textarea class="textarea is-skeleton" placeholder="Add a comment..."></textarea>
      </p>
    </div>
    <nav class="level">
      <div class="level-left">
        <div class="level-item">
          <a class="button is-info is-skeleton">Submit</a>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item">
          <label class="checkbox is-skeleton"> <input type="checkbox"> Press enter to submit </label>
        </div>
      </div>
    </nav>
  </div>
</article>
```

#### Notification [#](https://bulma.io/documentation/features/skeletons/#notification)

Example

Curabitur blandit tempus porttitor. Etiam porta sem malesuada magna mollis euismod. Cras justo odio, dapibus ac facilisis in, egestas eget quam.

HTML

```
<div class="notification is-skeleton">
  Curabitur blandit tempus porttitor. Etiam porta sem malesuada magna mollis euismod. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
</div>
```

#### Tag [#](https://bulma.io/documentation/features/skeletons/#tag)

Example

Tag Link Primary Info Success Warning Danger

HTML

```
<span class="tag is-skeleton">Tag</span>
<span class="tag is-link is-skeleton">Link</span>
<span class="tag is-primary is-skeleton">Primary</span>
<span class="tag is-info is-skeleton">Info</span>
<span class="tag is-success is-skeleton">Success</span>
<span class="tag is-warning is-skeleton">Warning</span>
<span class="tag is-danger is-skeleton">Danger</span>
```

#### Title and Subtitle [#](https://bulma.io/documentation/features/skeletons/#title-and-subtitle)

The `.title` and `.subtitle` elements have both an `is-skeleton` and `has-skeleton` variant: * `is-skeleton` will turn the whole block into a loading skeleton * `has-skeleton` will turn only a small part of its content into a loading skeleton, to simulate loading only the inner text rather than the whole block

Example

Title
-----

HTML

```
<h1 class="title is-skeleton">
  Title
</h1>
```

Example

Title
-----

HTML

```
<h1 class="title has-skeleton">
  Title
</h1>
```

Example

Subtitle
--------

HTML

```
<h2 class="subtitle is-skeleton">
  Subtitle
</h2>
```

Example

Subtitle
--------

HTML

```
<h2 class="subtitle has-skeleton">
  Subtitle
</h2>
```

Example

Title
-----

Subtitle
--------

HTML

```
<h1 class="title is-skeleton">
  Title
</h1>
<h2 class="subtitle is-skeleton">
  Subtitle
</h2>
```

Example

Title
-----

Subtitle
--------

HTML

```
<h1 class="title has-skeleton">
  Title
</h1>
<h2 class="subtitle has-skeleton">
  Subtitle
</h2>
```

#### Form Controls [#](https://bulma.io/documentation/features/skeletons/#form-controls)

Example

HTML

`<input class="input is-skeleton">`

Example

HTML

`<textarea class="textarea is-skeleton"></textarea>`
