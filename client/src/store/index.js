import Vue from 'vue'
import Vuex from 'vuex'
import user from './user'
import shared from './shared'
import data from  './data'

import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        user, shared, data
    },
    plugins: [
        createPersistedState({
            paths: ["user"],
            getState: (key) => Cookies.getJSON(key),
            setState: (key, state) => Cookies.set(key, state, { expires: 3, secure: false })
        })
    ]
})