import {HTTP} from "./AixoisConst";
import axios from 'axios'

class DataTable {
    constructor (id, group_name, subject, term, date, course, base, lectures, practise_less, lab_works, modular_control,
                 term_consultation, exam_consultation, credit, exam, course_work, vkr_bac, vkr_spec, vkr_mag,
                 practise_ruk, gos_exam, rez_vkr, zach_vkr, asp_ruk, other, all) {
        this.id = id;
        this.group_name = group_name.group_name;
        this.subject = subject;
        this.term = term;
        this.date = date;
        this.course = course;
        this.base = base;
        this.lectures = lectures;
        this.practise_less = practise_less;
        this.lab_works = lab_works;
        this.modular_control = modular_control;
        this.term_consultation = term_consultation;
        this.exam_consultation = exam_consultation;
        this.credit = credit;
        this.exam = exam;
        this.course_work = course_work;
        this.vkr_bac = vkr_bac;
        this.vkr_spec = vkr_spec;
        this.vkr_mag = vkr_mag;
        this.practise_ruk = practise_ruk;
        this.gos_exam = gos_exam;
        this.rez_vkr = rez_vkr;
        this.zach_vkr = zach_vkr;
        this.asp_ruk = asp_ruk;
        this.other = other;
        this.all = all
    }
}

export default {
    state: {
        data: []
    },
    mutations: {
        setNullData(state) {
          state.data = []
        },
        setData(state, payload) {
            state.data.push(payload)
        }
    },
    actions: {
        async getData ({commit, rootState}) {
            commit('clearError');
            commit('setLoading', true);
            commit('setNullData');
            try {
                let res = await HTTP.get(
                    'data/',
                    {headers: {
                            'Authorization': 'Token ' + rootState.user.user.token
                        }}
                )
                for (const item of res.data) {
                    commit('setData', new DataTable(
                        item.id,
                        item.group || "-",
                        item.subject.subject_name,
                        item.term,
                        item.date || "-",
                        item.course || "-",
                        item.base || "-",
                        item.lectures,
                        item.practise_less,
                        item.lab_works,
                        item.modular_control,
                        item.term_consultation,
                        item.exam_consultation,
                        item.credit,
                        item.exam,
                        item.course_work,
                        item.vkr_bac,
                        item.vkr_spec,
                        item.vkr_mag,
                        item.practise_ruk,
                        item.gos_exam,
                        item.rez_vkr,
                        item.zach_vkr,
                        item.asp_ruk,
                        item.other,
                        item.all
                    ))
                }
                commit('setLoading', false);
                //TODO: add data array from response to state
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        },
        async deleteItem({commit, rootState}, {id}){
            commit('clearError');
            commit('setLoading', true);
            try {
                let res = await HTTP.delete(
                    'data/' + id,
                    {headers: {
                            'Authorization': 'Token ' + rootState.user.user.token
                        }}
                )
                commit('setLoading', false);
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        },
        async addItem({commit, rootState}, payload) {
            commit('clearError');
            commit('setLoading', true);
            let grp = null;
            if (payload.group_name !== null) {
                grp = { group_name: payload.group_name }
            }
            try {
                let resp = await HTTP.post(
                    'data/',
                    {
                        group : grp,
                        subject : { subject_name: payload.subject},
                        term: payload.term,
                        date: payload.date, //change fromat YYYY-MM-DD
                        course: payload.course,
                        base: payload.base,
                        lectures: payload.lectures,
                        practise_less: payload.practise_less,
                        lab_works: payload.lab_works,
                        modular_control: payload.modular_control,
                        term_consultation: payload.term_consultation,
                        exam_consultation: payload.exam_consultation,
                        credit: payload.credit,
                        exam: payload.exam,
                        course_work: payload.course_work,
                        vkr_bac: payload.vkr_bac,
                        vkr_spec: payload.vkr_spec,
                        vkr_mag: payload.vkr_mag,
                        practise_ruk: payload.practise_ruk,
                        gos_exam: payload.gos_exam,
                        rez_vkr: payload.rez_vkr,
                        zach_vkr: payload.zach_vkr,
                        asp_ruk: payload.asp_ruk,
                        other: payload.other,
                        all: payload.all
                    },
                    {headers: {
                            'Authorization': 'Token ' + rootState.user.user.token
                        }}
                )
                commit('setLoading', false);
                let dt =  new DataTable(
                    resp.data.id,
                    resp.data.group || "-",
                    resp.data.subject.subject_name,
                    resp.data.term,
                    resp.data.date || "-",
                    resp.data.course || "-",
                    resp.data.base || "-",
                    resp.data.lectures,
                    resp.data.practise_less,
                    resp.data.lab_works,
                    resp.data.modular_control,
                    resp.data.term_consultation,
                    resp.data.exam_consultation,
                    resp.data.credit,
                    resp.data.exam,
                    resp.data.course_work,
                    resp.data.vkr_bac,
                    resp.data.vkr_spec,
                    resp.data.vkr_mag,
                    resp.data.practise_ruk,
                    resp.data.gos_exam,
                    resp.data.rez_vkr,
                    resp.data.zach_vkr,
                    resp.data.asp_ruk,
                    resp.data.other,
                    resp.data.all
                );
                commit('setData', dt);
                return dt
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        },
        async editItem ({commit, rootState}, payload) {
            commit('clearError');
            commit('setLoading', true);
            let grp = null;
            if (payload.group_name !== null) {
                grp = { group_name: payload.group_name }
            }
            try {
                let resp = await HTTP.put(
                    'data/' + payload.id + '/',
                    {
                        group : grp,
                        subject : { subject_name: payload.subject},
                        term: payload.term,
                        date: payload.date, //change fromat YYYY-MM-DD
                        course: payload.course,
                        base: payload.base,
                        lectures: payload.lectures,
                        practise_less: payload.practise_less,
                        lab_works: payload.lab_works,
                        modular_control: payload.modular_control,
                        term_consultation: payload.term_consultation,
                        exam_consultation: payload.exam_consultation,
                        credit: payload.credit,
                        exam: payload.exam,
                        course_work: payload.course_work,
                        vkr_bac: payload.vkr_bac,
                        vkr_spec: payload.vkr_spec,
                        vkr_mag: payload.vkr_mag,
                        practise_ruk: payload.practise_ruk,
                        gos_exam: payload.gos_exam,
                        rez_vkr: payload.rez_vkr,
                        zach_vkr: payload.zach_vkr,
                        asp_ruk: payload.asp_ruk,
                        other: payload.other,
                        all: payload.all
                    },
                    {headers: {
                            'Authorization': 'Token ' + rootState.user.user.token
                        }}
                )
                commit('setLoading', false);
                return new DataTable(
                    resp.data.id,
                    resp.data.group || "-",
                    resp.data.subject.subject_name,
                    resp.data.term,
                    resp.data.date || "-",
                    resp.data.course || "-",
                    resp.data.base || "-",
                    resp.data.lectures,
                    resp.data.practise_less,
                    resp.data.lab_works,
                    resp.data.modular_control,
                    resp.data.term_consultation,
                    resp.data.exam_consultation,
                    resp.data.credit,
                    resp.data.exam,
                    resp.data.course_work,
                    resp.data.vkr_bac,
                    resp.data.vkr_spec,
                    resp.data.vkr_mag,
                    resp.data.practise_ruk,
                    resp.data.gos_exam,
                    resp.data.rez_vkr,
                    resp.data.zach_vkr,
                    resp.data.asp_ruk,
                    resp.data.other,
                    resp.data.all
                );
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }
        },
        async sendMail ({commit, rootState}, {email, selected}) {
            commit('clearError');
            commit('setLoading', true);
            try {
                let resp = await HTTP.post(
                    'email',
                    {
                        email : email,
                        items: selected
                    },
                    {headers: {
                            'Authorization': 'Token ' + rootState.user.user.token
                        }})
            } catch (err) {
                commit('setLoading', false);
                commit('setError', err.message);
                throw  err
            }

        }
    },
    getters: {
        data (state) {
            return state.data
        }
    }
}