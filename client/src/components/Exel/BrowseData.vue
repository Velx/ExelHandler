<template>
    <v-container>
        <v-layout row wrap>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                    </v-card-title>

                    <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.subject" label='Название учебной дисциплины'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field
                                            v-model="editedItem.date"
                                            label='Дата'
                                            hint="YYYY-MM-DD"
                                            persistent-hint
                                    ></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.course" label='Курс'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.group_name" label=Группа></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <!--<v-text-field v-model="editedItem.base" label='База обучения'></v-text-field>-->
                                    <v-autocomplete
                                            v-model="editedItem.base"
                                            ref="editedItem.base"
                                            :items="['B', 'C']"
                                            label='База обучения'
                                    ></v-autocomplete>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.term" label='Семестр'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.lectures" label='Лекции'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.practise_less" label='Практические (сем.) занятия'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.lab_works" label='Лабораторные занятия'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.modular_control" label='Модульный контроль'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.term_consultation" label='Семестр (консультации)'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.exam_consultation" label='Экзамен (консультации)'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.credit" label='Зачеты'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.exam" label='Экзамены'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.course_work" label='Курсовые работы'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.vkr_bac" label='ВКР бакалавров'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.vkr_spec" label='ВКР специалистов'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.vkr_mag" label='ВКР магистров'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.practise_ruk" label='Руководство практикой'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.gos_exam" label='Госэкзамены'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.rez_vkr" label='Рецензирование ВКР'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.zach_vkr" label='Защита ВКР'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.asp_ruk" label='Руководство аспирантами'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.other" label='Другие виды учеб. нагрузки'></v-text-field>
                                </v-flex>
                                <v-flex xs12 sm6 md6>
                                    <v-text-field v-model="editedItem.all" label='Количество часов всего'></v-text-field>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
                        <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <!--EMAIL NEXT-->
            <v-dialog v-model="dialog2" max-width="500px">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" dark class="mb-2" v-on="on">Send data</v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="headline ">Enter email</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                                <v-flex xs12 sm12 md12>
                                    <v-text-field
                                            v-model="email"
                                            label='Email'
                                            :rules="[value => !!value || 'Required.']"></v-text-field>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" flat @click="sendMail" :disabled="dis">Send</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-flex xs12>
                <v-data-table
                        v-model="selected"
                        select-all
                        :headers="headers"
                        :items="data"
                        class="elevation-1"
                        disable-initial-sort
                        :rows-per-page-items='[10, 25, {"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}]'

                >
                    <template v-slot:items="props">
                        <!--<td class="hide">{{ props.item.id }}</td>-->
                        <td>
                            <v-checkbox
                                    v-model="props.selected"
                                    primary
                                    hide-details
                            ></v-checkbox>
                        </td>
                        <td>{{ props.item.subject }}</td>
                        <td class="text-xs-center">{{ props.item.date || "-"}}</td>
                        <td class="text-xs-center">{{ props.item.course || "-" }}</td>
                        <td class="text-xs-center">{{ props.item.group_name || "-" }}</td>
                        <td class="text-xs-center">{{ props.item.base || "-" }}</td>
                        <td class="text-xs-center">{{ props.item.term }}</td>
                        <td class="text-xs-center">{{ props.item.lectures }}</td>
                        <td class="text-xs-center">{{ props.item.practise_less }}</td>
                        <td class="text-xs-center">{{ props.item.lab_works }}</td>
                        <td class="text-xs-center">{{ props.item.modular_control }}</td>
                        <td class="text-xs-center">{{ props.item.term_consultation }}</td>
                        <td class="text-xs-center">{{ props.item.exam_consultation }}</td>
                        <td class="text-xs-center">{{ props.item.credit }}</td>
                        <td class="text-xs-center">{{ props.item.exam }}</td>
                        <td class="text-xs-center">{{ props.item.course_work }}</td>
                        <td class="text-xs-center">{{ props.item.vkr_bac }}</td>
                        <td class="text-xs-center">{{ props.item.vkr_spec }}</td>
                        <td class="text-xs-center">{{ props.item.vkr_mag }}</td>
                        <td class="text-xs-center">{{ props.item.practise_ruk }}</td>
                        <td class="text-xs-center">{{ props.item.gos_exam }}</td>
                        <td class="text-xs-center">{{ props.item.rez_vkr }}</td>
                        <td class="text-xs-center">{{ props.item.zach_vkr }}</td>
                        <td class="text-xs-center">{{ props.item.asp_ruk }}</td>
                        <td class="text-xs-center">{{ props.item.other }}</td>
                        <td class="text-xs-center">{{ props.item.all }}</td>
                        <td class="justify-center layout px-0">
                            <v-icon
                                    small
                                    class="mr-2"
                                    @click="editItem(props.item)"
                            >
                                edit
                            </v-icon>
                            <v-icon
                                    small
                                    @click="deleteItem(props.item)"
                            >
                                delete
                            </v-icon>
                        </td>
                    </template>
                    <template v-slot:no-data>
                        <v-alert :value="true" color="error" icon="warning">
                            Sorry, nothing to display here :(
                        </v-alert>
                        <v-btn color="primary" @click="getFromState">Reset</v-btn>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>

export default {
    data () {
        return {
            dis: true,
            dialog: false,
            dialog2: false,
            email: '',
            editedIndex: -1,
            data: [],
            selected: [],
            headers: [
                // { text: 'id', value: 'id', class: 'hide'},
                {
                    text: 'Название учебной дисциплины',
                    align: 'left',
                    sortable: false,
                    value: 'subject'
                },
                { text: 'Дата', value: 'date'},
                { text: 'Курс', value: 'course' },
                { text: 'Группа', value: 'group_name' },
                { text: 'База обучения', value: 'base' },
                { text: 'Семестр', value: 'term' },
                { text: 'Лекции', value: 'lectures'}, //class: 'vertical-text'
                { text: 'Практические (сем.) занятия', value: 'practise_less' },
                { text: 'Лабораторные занятия', value: 'lab_works' },
                { text: 'Модульный контроль', value: 'modular_control' },
                { text: 'Семестр (консультации)', value: 'term_consultation' },
                { text: 'Экзамен (консультации)', value: 'exam_consultation' },
                { text: 'Зачеты', value: 'credit' },
                { text: 'Экзамены', value: 'exam' },
                { text: 'Курсовые работы', value: 'course_work' },
                { text: 'ВКР бакалавров', value: 'vkr_bac' },
                { text: 'ВКР специалистов', value: 'vkr_spec' },
                { text: 'ВКР магистров', value: 'vkr_mag' },
                { text: 'Руководство практикой', value: 'practise_ruk' },
                { text: 'Госэкзамены', value: 'gos_exam' },
                { text: 'Рецензирование ВКР', value: 'rez_vkr' },
                { text: 'Защита ВКР', value: 'zach_vkr' },
                { text: 'Руководство аспирантами', value: 'asp_ruk' },
                { text: 'Другие виды учеб. нагрузки', value: 'other' },
                { text: 'Количество часов всего', value: 'all' },
            ],
            editedItem: {
                subject: '',
                date: '',
                course: 0,
                group_name: '',
                base: '',
                term: 0,
                lectures: 0,
                practise_less: 0,
                lab_works: 0,
                modular_control: 0,
                term_consultation: 0,
                exam_consultation: 0,
                credit: 0,
                exam: 0,
                course_work: 0,
                vkr_bac: 0,
                vkr_spec: 0,
                vkr_mag: 0,
                practise_ruk: 0,
                gos_exam: 0,
                rez_vkr: 0,
                zach_vkr: 0,
                asp_ruk: 0,
                other: 0,
                all: 0,
            },
            defaultItem: {
                subject: '',
                date: '',
                course: 0,
                group_name: '',
                base: '',
                term: 0,
                lectures: 0,
                practise_less: 0,
                lab_works: 0,
                modular_control: 0,
                term_consultation: 0,
                exam_consultation: 0,
                credit: 0,
                exam: 0,
                course_work: 0,
                vkr_bac: 0,
                vkr_spec: 0,
                vkr_mag: 0,
                practise_ruk: 0,
                gos_exam: 0,
                rez_vkr: 0,
                zach_vkr: 0,
                asp_ruk: 0,
                other: 0,
                all: 0
            }
        }
    },
    computed: {
        formTitle () {
            return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },

    },
    watch: {
        dialog (val) {
            val || this.close()
        },
        //TODO: bad idea
        email () {
            if (this.email !== '' || this.email !== 'Required') {
                this.dis = false
            }
        }
    },
    created() {
        this.initialize()
    },
    methods: {
        initialize () {
            this.data = this.$store.getters.data
        },
        getFromState () {
            this.$store.dispatch('getData')
            this.data = this.$store.getters.data
        },
        editItem (item) {
            this.editedIndex = this.data.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },
        deleteItem (item) {
            const index = this.data.indexOf(item)
            confirm('Are you sure you want to delete this item?') && this.data.splice(index, 1)
            this.$store.dispatch('deleteItem', item)
        },
        close () {
            this.dialog = false
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            }, 1000)
        },
        save () {
            if (this.editedIndex > -1) {
                this.$store.dispatch('editItem', this.editedItem).then((val) => {
                    Object.assign(this.data[this.editedIndex], this.editedItem)
                    this.close()
                })
            } else {
                this.$store.dispatch('addItem', this.editedItem).then( (val) => {
                        this.data.push(val);
                        this.close()
                })
            }
        },
        sendMail () {
            if (this.selected.length === 0) {
                this.dialog2 = false
                this.$store.dispatch('setError', 'Please select rows to send on email')
            } else {
                this.$store.dispatch('sendMail', {email: this.email, selected: this.selected})
                this.email = ''
                this.dialog2 = false
            }

        }
    }
}
</script>

<style>
    .hide {
        /*visibility: collapse;*/
        display: none;
    }
/*.vertical-text {*/
    /*writing-mode: vertical-rl;*/
    /*text-orientation: mixed;*/
/*}*/
</style>