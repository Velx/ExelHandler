<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md5>
                <v-card class="elevation-12">
                    <v-toolbar color="green darken-1">
                        <v-toolbar-title>Registration form</v-toolbar-title>
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
                            <v-text-field
                                    prepend-icon="lock"
                                    name="password2"
                                    label="Confirm password"
                                    type="password"
                                    v-model="password2"
                                    :rules="ConfPasswordRules"
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
                        >Sign up</v-btn>
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
                password2: '',
                valid: false,
                nameRules: [
                    v => !!v || 'Login is required',
                    v => v.length >= 4 || 'Login must be equal or more than 4 characters'
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => v.length >= 6 || 'Password must be equal or more than 6 characters'
                ],
                ConfPasswordRules: [
                    v => !!v || 'Password is required',
                    v => v === this.password || 'Password should match'
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
                    this.$store.dispatch('registerUser', user)
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
        }
    }
</script>

<style scoped>

</style>