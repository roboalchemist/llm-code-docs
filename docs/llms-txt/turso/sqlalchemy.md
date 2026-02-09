# Source: https://docs.turso.tech/sdk/python/orm/sqlalchemy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# SQLAlchemy + Turso

> Configure SQLAlchemy to work with your Turso database

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c43a5833c30b4a5d3403fd4d68fd84e2" alt="SQLAlchemy Quickstart" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/sqlalchemy-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=bf9161005342db8e96f7340f48b52af6 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3153839be444a4fd1ed6f4e510849da3 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1ff30339afd65c8ccc38358bde6fe90d 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=180f1d982006bce507bc4778e39d6302 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8794b2dd589b0ab1ceb28ff6cc654f85 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/sqlalchemy-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=e7e5feb8e49ceced92f91be9ed5a2cd4 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)

<Steps>
  <Step title="Install the libSQL dialect for SQLAlchemy">
    ```bash  theme={null}
    pip install sqlalchemy-libsql
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

    class Foo(Base):
        __tablename__ = "foo"
        id: Mapped[str] = mapped_column(primary_key=True)
        bar: Mapped[str] = mapped_column(String(100))
        def __repr__(self) -> str:
            return f"Item(id={self.id!r}, bar={self.bar!r})"

    ```
  </Step>

  <Step title="Create engine">
    <AccordionGroup>
      <Accordion title="Embedded Replicas">
        ```python  theme={null}
        from dotenv import load_dotenv
        from sqlalchemy import create_engine

        TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
        TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

        engine = create_engine(
             "sqlite+libsql:///embedded.db",
             connect_args={
                 "auth_token": TURSO_AUTH_TOKEN,
                 "sync_url": TURSO_DATABASE_URL,
             },
        )
        ```
      </Accordion>

      <Accordion title="Remote only">
        ```python  theme={null}
        from dotenv import load_dotenv
        from sqlalchemy import create_engine

        TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
        TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

        engine = create_engine(
            f"sqlite+{TURSO_DATABASE_URL}?secure=true",
            connect_args={
                "auth_token": TURSO_AUTH_TOKEN,
            },
        )
        ```
      </Accordion>

      <Accordion title="Memory Only">
        ```python  theme={null}
        from sqlalchemy import create_engine

        engine = create_engine("sqlite+libsql://")
        ```
      </Accordion>

      <Accordion title="Local only">
        ```python  theme={null}
        from sqlalchemy import create_engine

        engine = create_engine("sqlite+libsql:///local.db")
        ```
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Query">
    ```py app.py theme={null}
    from sqlalchemy.orm import Session
    from sqlalchemy import select
    from models import Foo

    @app.route("/", methods=(["GET"]))
    def home():
        session = Session(engine)

        # get & print foos
        stmt = select(Foo)

        for item in session.scalars(stmt):
            print(item)

    ```
  </Step>
</Steps>
