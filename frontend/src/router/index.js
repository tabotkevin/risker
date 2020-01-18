import Vue from 'vue'
import Router from 'vue-router'
import Landing from '@/components/Landing'
import Profile from '@/components/Profile'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import store from '../store'
import RisksTable from '@/components/RisksTable'
import RiskTable from '@/components/RiskTable'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing
  },
  {
    path: '/profile',
    name: 'Profile',
    meta: {
      requireAuth: true
    },
    component: Profile
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/risks',
    name: 'Risks',
    meta: {
      requireAuth: true
    },
    component: RisksTable
  },
  {
    path: '/risk/:id',
    name: 'Risk',
    meta: {
      requireAuth: true
    },
    props: true,
    component: RiskTable
  }
]

const router = new Router({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.token) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
})

export default router
