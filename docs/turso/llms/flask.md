# Source: https://docs.turso.tech/sdk/python/guides/flask.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Flask + Turso

> Set up Turso in your Flask project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=29d0d7405a0b24c0f3ccf312ac32ad4b" alt="Flask banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/flask-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8950504620a6928be70f6c82db873dd8 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1ee389b2952213f82cd94b5b0c65bca0 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ababf954914cdd9a4e1d292b63e7ba71 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5d5182974b80e1bdb6d43bb2717b1b41 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=eebe61e88f400ee0017d1c4823d1e34d 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/flask-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=337ac8c1fa7f32586d3c4cde541894e6 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Flask app — [learn more](https://flask.palletsprojects.com/en/3.0.x/installation/#create-an-environment)

<Steps>
  <Step title="Install the libSQL dialect">
    ```bash  theme={null}
    pip install sqlalchemy-libsql python-dotenv
    ```
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Create database models">
    ```python models.py theme={null}
    from sqlalchemy import String
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column

    class Base(DeclarativeBase):
        pass

    class Item(Base):
        __tablename__ = "items"
        id: Mapped[str] = mapped_column(primary_key=True)
        foo: Mapped[str] = mapped_column(String(255))
        bar: Mapped[str] = mapped_column(String(100))
        def __repr__(self) -> str:
            return f"Item(id={self.id!r}, foo={self.foo!r}, bar={self.bar!r})"
    ```
  </Step>

  <Step title="Query">
    ```python  theme={null}
    from dotenv import load_dotenv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy import select
    from models import Item

    load_dotenv()

    # Get environment variables
    TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

    # construct special SQLAlchemy URL
    dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

    engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)

    @app.route("/", methods=(["GET"]))
    def home():
        session = Session(engine)

        # get & print items
        stmt = select(Item)

        for item in session.scalars(stmt):
            print(item)
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Social App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-find-me-on-python-htmx">
    See the full source code
  </Card>
</CardGroup>
