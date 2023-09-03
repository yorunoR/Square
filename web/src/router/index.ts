import { createRouter, createWebHistory } from 'vue-router'

import BoardLayout from '@/layouts/BoardLayout.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/board/users'
    },
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: 'ping',
          name: 'ping',
          meta: {
            title: 'ping'
          },
          component: async () => await import(/* webpackChunkName: "ping" */ '@/views/PingView.vue')
        },
        {
          path: 'sign_in',
          name: 'sign_in',
          meta: {
            title: 'sign_in'
          },
          component: async () =>
            await import(/* webpackChunkName: "sign_in" */ '@/views/SignInView.vue')
        }
      ]
    },

    {
      path: '/board',
      component: BoardLayout,
      children: [
        {
          path: 'users',
          name: 'users',
          meta: {
            title: 'users'
          },
          component: async () =>
            await import(/* webpackChunkName: "users" */ '@/views/board/UsersView.vue')
        }
      ]
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/board/users'
    }
  ]
})

router.afterEach((to) => {
  const title = to.meta.title as string
  document.title = title
})

export default router
