import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/loading' //记得改回来
  },
  {
    path: '/loading', // 加载页面很正常
    name: 'Loading',
    component: () => import('../pages/login/loading'),
    meta: {
      showTab: false
    }
  },
  {
    path: '/login', // 信息填写
    name: 'Login',
    component: () => import('../pages/login/login'),
    meta: {
      showTab: false
    }
  },
  {
    path: '/index', // 主页 第一次是从这个东西跳到login页面
    name: 'Index',
    component: () => import('../pages/index/index'),
    meta: {
      showTab: true
    }

  },
  {
    path: '/home', // 主页也是需要的
    name: 'Home',
    redirect: '/home/main',
    component: () => import('../pages/home/home'),
    children: [{
      path: 'main',
      name: 'Main',
      component: () => import('../pages/home/main'),
      meta: {
        showTab: true
      }
    }, {
      path: 'person',
      name: 'Person',
      component: () => import('../pages/home/person'),
      meta: {
        showTab: false
      }
    }, {
      path: 'apply',
      name: 'Apply',
      component: () => import('../pages/home/apply'),
      meta: {
        showTab: false
      }
    }]
  },
  {
    path: '/clubpage',
    name: 'ClubPage',
    component: () => import('../pages/clubpage/clubpage'),
    meta: {
      showTab: false
    }
  }

]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  // document.title = '学生社团年审注册'
  next()
})

export default router
