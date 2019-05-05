import Vue from 'vue'
import Router from 'vue-router'
import AuthGuard from './auth-guard'

import Home from '@/components/Home'
import Login from '@/components/Auth/Login'
import Registration from '@/components/Auth/Registration'
import ResetPassword from '@/components/Auth/ResetPassword'
import BrowseData from '@/components/Exel/BrowseData'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '',
            name: 'home',
            component: Home
        },{
            path: '/login',
            name: 'login',
            component: Login
        },{
            path: '/registration',
            name: 'reg',
            component: Registration
        },{
            path: '/resetPassword',
            name: 'reset',
            component: ResetPassword
        },{
            path: '/browse',
            name: 'browse',
            component: BrowseData,
            beforeEnter: AuthGuard
        }
    ],
    mode: 'history'
})