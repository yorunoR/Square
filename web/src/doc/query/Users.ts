const QUERY = /* GraphQL */ `
  query Users {
    users {
      id
      activated
      email
      name
      profileImage
      role
      anonymous
    }
  }
`
export default QUERY
