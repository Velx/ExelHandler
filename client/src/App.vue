<template>
    <v-app>
        <v-navigation-drawer
                app
                temporary
                v-model="drawer"

        >
            <v-list>
                <v-list-tile
                        v-for="link in links"
                        :key="link.title"
                        :to="link.url"
                >
                    <v-list-tile-action>
                        <v-icon>{{ link.icon }}</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title v-text="link.title"></v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile
                        v-if="isUserLoggedIn"
                        @click="onLogout"
                >
                    <v-list-tile-action>
                        <v-icon>exit_to_app</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title v-text="'Logout'"></v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app color="green darken-1">
            <v-toolbar-side-icon
                    @click="drawer = !drawer"
                    class="hidden-md-and-up"
            ></v-toolbar-side-icon>

            <v-toolbar-title>
                <router-link to="/" class="toolbar-title">ExelHandler</router-link>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn
                        flat
                        v-for="link of links"
                        :key="link.title"
                        :to="link.url"
                >
                    <v-icon left>{{ link.icon }} </v-icon>
                    {{link.title}}
                </v-btn>
                <v-btn
                        flat
                        @click="onLogout"
                        v-if="isUserLoggedIn"
                >
                    <v-icon left>exit_to_app</v-icon>
                    Logout
                </v-btn>

            </v-toolbar-items>
        </v-toolbar>
        <v-content>
            <router-view></router-view>
        </v-content>
        <template v-if="error">
            <v-snackbar
                    :multi-line="true"
                    :timeout="5000"
                    color="error"
                    @input="closeError"
                    :value = "true"
            >
                {{ error }}
                <v-btn
                        dark
                        flat
                        @click="closeError"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </template>
    </v-app>
</template>

<script>

    export default {
        data () {
            return {
                drawer: false
            }
        },
        computed: {
            error () {
                return this.$store.getters.error
            },
            isUserLoggedIn () {
                return this.$store.getters.isUserLoggedIn
            },
            links () {
                if (this.isUserLoggedIn) {
                    return [
                        // {title: 'Log out ', icon: 'exit_to_app', url: '/logout'},
                        {title: 'Browse data', icon: 'table_chart', url: '/browse'},
                    ]
                }
                else {
                    return [
                        {title: 'Login', icon: 'account_circle', url: '/login'},
                        {title: 'Register', icon: 'face', url: '/registration'},
                    ]
                }
            }
        },
        methods: {
            closeError () {
                this.$store.dispatch('clearError')
            },
            onLogout () {
                this.$store.dispatch('logoutUser')
                this.$router.push('/')
            }
        }
    }
</script>

<style scoped>
  .toolbar-title {
    color: inherit;
    text-decoration: inherit;
  }
</style>