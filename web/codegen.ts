import type { CodegenConfig } from '@graphql-codegen/cli'

const config: CodegenConfig = {
  schema: 'http://api:5000/graphql/',
  documents: ['src/doc/**/*.ts'],
  generates: {
    './src/gql/': {
      preset: 'client',
      config: {
        useTypeImports: true,
        scalars: {
          DateTime: 'string'
        }
      }
    }
  }
}

export default config;
