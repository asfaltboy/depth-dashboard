import Vue from "vue";
import Vuex from "vuex";
import Axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        users: [],
        projects: [],
        baseUrl: 'http://localhost:3000'
    },
    mutations: {
        setUsers(state, data) {
            state.users = data;
        },
        setProjects(state, data) {
            state.projects = data;
        },
    },
    actions: {
        async fetchUsers({state, commit},) {
            const urlBase = state.baseUrl + "/user";
            let response = await Axios.get(urlBase);
            commit('setUsers', response.data);
            return response.data
        },
        async fetchProjects({state, commit},) {
            const urlBase = state.baseUrl + "/project";
            let response = await Axios.get(urlBase);
            commit('setProjects', response.data);
            return response.data
        },


        postUser({state}, dataObj) {
            const urlBase = state.baseUrl + "/user/";
            let data = Axios.post(urlBase, dataObj);
            return data
        },
        postProject({state}, dataObj) {
            const urlBase = state.baseUrl + "/project/";
            let data = Axios.post(urlBase, dataObj);
            return data
        },
    },
    getters: {
        getUser(state) {
            return state.users;
        },
        getProjects(state) {
            return state.projects;
        }
    }
});
