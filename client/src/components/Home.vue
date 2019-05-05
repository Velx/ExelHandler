<template>
    <v-container>
        <v-layout row >
            <v-flex xs12>
                <vue-dropzone v-if='isUserLoggedIn'
                              ref="myVueDropzone"
                              id="dropzone"
                              :options="dropzoneOptions"

                ></vue-dropzone>
                <!--@vdropzone-sending="sendingEvent"-->
                <h2 v-else class="display-3 text-md-center pt-4" >Please log in to use site functions</h2>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import vue2Dropzone from 'vue2-dropzone'
    import 'vue2-dropzone/dist/vue2Dropzone.min.css'

    export default {
        data () {
            return {
                dropzoneOptions: {
                    url: 'http://127.0.0.1:8000/api/upload',
                    method: "put",
                    thumbnailWidth: 250,
                    addRemoveLinks: true,
                    maxFiles: 1,
                    acceptedFiles: '.xlsx,.xls',
                    headers: {
                        'Authorization': 'Token ' + (this.$store.getters.user).token
                    }
                }
            }
        },
        methods: {
            // sendingEvent (file, xhr, formData) {
            //     formData.append('filename', 'testname');
            // }
        },
        computed: {
            isUserLoggedIn () {
                return this.$store.getters.isUserLoggedIn
            }
        },
        components: {
            vueDropzone: vue2Dropzone
        }
    }
</script>

<style scoped>

</style>