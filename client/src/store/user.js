import {HTTP} from "./AixoisConst";


class User {
    constructor(token, username) {
        this.token = token
        this.username = username
    }
}

export default {
    state: {
        user: null
    },
    mutations: {
        setUser (state, payload) {
            state.user = payload
        }
    },
    actions: {
        async registerUser ({commit}, {login, password}) {
            commit('clearError');
            commit('setLoading', true);
            try {
                await HTTP.post('register', {
                    username: login,
                    password: password,
                    });
                commit('setLoading', false)
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        },
        async loginUser ({commit}, {login, password}) {
            commit('clearError');
            commit('setLoading', true);
            try {
                const res = await HTTP.post('/login', {
                    username: login,
                    password: password,
                });
                commit('setUser', new User(res.data.token, res.data.username));
                //TODO: throw error with 404 code == user or password wrong
                commit('setLoading', false)
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        }, //TODO: async logout
        logoutUser ({commit, state}) {
            HTTP.post('/logout', null, {headers: {
                    'Authorization': 'Token ' + state.user.token
                }}
            )
            commit('setUser', null)
        }
    },
    getters: {
        user (state) {
            return state.user
        },
        isUserLoggedIn (state) {
            return state.user !== null
        }
    }
}