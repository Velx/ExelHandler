<template>
    <v-container>
        <v-layout row >
            <v-flex xs12>
                <v-data-table
                        :headers="headers"
                        :items="this.$store.state.data"
                        :search="search"
                        hide-actions
                        :pagination.sync="pagination"
                        :total-items="this.$store.getters.elementsCount"
                        disable-page-reset
                        class="elevation-1"
                >
                    <template v-slot:items="props">
                        <td>{{ props.item.date }}</td>
                        <td class="text-xs-center">{{ props.item.course }}</td>
                        <td class="text-xs-center">{{ props.item.group_name}}</td>
                        <td class="text-xs-center">{{ props.item.base }}</td>
                        <td class="text-xs-center">{{ props.item.term }}</td>
                        <td class="text-xs-center">{{ props.item.subject }}</td>
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
                    </template>
                </v-data-table>
                <div class="text-xs-center pt-2">
                    <v-pagination
                            v-model="pagination.page"
                            :length="pages"
                            circle
                    ></v-pagination>
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        data () {
            return {
                search: '',
                pagination: {
                    rowsPerPage: 10,
                    page: 1
                },
                selected: [],
                headers: [
                    {
                        text: 'Дата',
                        align: 'left',
                        sortable: false,
                        value: 'date'
                    },
                    { text: 'Курс', value: 'course' },
                    { text: 'Группа', value: 'group_name' },
                    { text: 'База обучения', value: 'base' },
                    { text: 'Семестр', value: 'term' },
                    { text: 'Название учебной дисциплины', value: 'subject' },
                    { text: 'Лекции', value: 'lectures' },
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
                data: this.$store.getters.data
            }
        },
        watch: {
            'pagination.page': function (val, oldVal) {
                console.log(this.pagination.page)
                //TODO: error when update data, datatable reset
                this.$store.dispatch('getData', val)
            }
        },
        computed: {
            totalItems () {
                return this.$store.getters.elementsCount
            },
            pages () {
                if (this.pagination.rowsPerPage == null ||
                    this.$store.getters.elementsCount == null
                ) return 0

                return Math.ceil(this.$store.getters.elementsCount / this.pagination.rowsPerPage)
            },

        },
        methods: {
        }
    }
</script>

<style scoped>

</style>