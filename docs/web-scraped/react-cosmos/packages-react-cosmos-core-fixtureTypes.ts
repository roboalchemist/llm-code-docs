# React Cosmos Documentation
# Source: https://raw.githubusercontent.com/react-cosmos/react-cosmos/main/packages/react-cosmos-core/src/userModules/fixtureTypes.ts
# Path: packages/react-cosmos-core/src/userModules/fixtureTypes.ts

export type FixtureId = {
  path: string;
  name?: string;
};

export type FixtureListItem =
  | { type: 'single' }
  | { type: 'multi'; fixtureNames: string[] };

export type FixtureList = {
  [fixturePath: string]: FixtureListItem;
};
