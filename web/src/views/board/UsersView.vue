<template>
  <main style="max-width: 768px; margin: auto">
    <h2>Users</h2>
    <section>
      <div v-if="fetching">Loading...</div>
      <div v-else-if="error">Oh no... {{ error }}</div>
      <div v-else>
        <ul v-if="data">
          <li v-for="user in data.users">
            {{ user.email }}
          </li>
        </ul>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { useQuery } from '@urql/vue'
import { graphql } from '@/gql'
import Users from '@/doc/query/Users'

const query = graphql(Users)

const { fetching, error, data } = useQuery({ query })
</script>
