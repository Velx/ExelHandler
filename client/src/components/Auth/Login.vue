<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md5>
                <v-card class="elevation-12">
                    <v-toolbar color="green darken-1">
                        <v-toolbar-title>Login form</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form v-model="valid" ref="form" validation>
                            <v-text-field
                                    prepend-icon="person"
                                    name="login"
                                    label="Login"
                                    type="text"
                                    v-model="login"
                                    :rules="nameRules"
                            ></v-text-field>
                            <v-text-field
                                    prepend-icon="lock"
                                    name="password"
                                    label="Password"
                                    type="password"
                                    v-model="password"
                                    :rules="passwordRules"
                                    :counter="0"
                            ></v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                                color="primary"
                                @click="onSubmit"
                                :loading="loading"
                                :disabled="!valid || loading"
                        >Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    export default {
        data () {
            return {
                login: '',
                password: '',
                valid: false,
                nameRules: [
                    v => !!v || 'Login is required',
                    v => v.length >= 4 || 'Login must be equal or more than 4 characters'
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => v.length >= 6 || 'Password must be equal or more than 6 characters'
                ]
            }
        },
        methods: {
            onSubmit() {
                //logic
                if (this.$refs.form.validate()) {
                    const user = {
                        login: this.login,
                        password: this.password
                    }
                    this.$store.dispatch('loginUser', user)
                        .then(() => {
                            this.$router.push('/')
                        })
                        .catch( () => {})
                }
            }
        },
        computed: {
            loading () {
                return this.$store.getters.loading
            }
        },
        created() {
            if (this.$route.query['loginError']) {
                this.$store.dispatch('setError', 'Please log in to access this page.')
            }
        }
    }
</script>

<style scoped>

</style>