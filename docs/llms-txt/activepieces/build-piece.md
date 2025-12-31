# Source: https://www.activepieces.com/docs/build-pieces/misc/build-piece.md

# Source: https://www.activepieces.com/docs/developers/misc/build-piece.md

# Build Custom Pieces

You can use the CLI to build custom pieces for the platform. This process compiles the pieces and exports them as a `.tgz` packed archive.

### How It Works

The CLI scans the `packages/pieces/` directory for the specified piece. It checks the **name** in the `package.json` file. If the piece is found, it builds and packages it into a `.tgz` archive.

### Usage

To build a piece, follow these steps:

1. Ensure you have the CLI installed by cloning the repository.
2. Run the following command:

```bash  theme={null}
npm run build-piece
```

You will be prompted to enter the name of the piece you want to build. For example:

```bash  theme={null}
? Enter the piece folder name : google-drive
```

The CLI will build the piece and you will be given the path to the archive. For example:

```bash  theme={null}
Piece 'google-drive' built and packed successfully at dist/packages/pieces/community/google-drive
```

You may also build the piece non-interactively by passing the piece name as an argument.  For example:

```bash  theme={null}
npm run build-piece google-drive
```
