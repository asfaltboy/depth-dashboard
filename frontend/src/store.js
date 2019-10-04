import Vue from "vue";
import Vuex from "vuex";
import Axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        users: [],
        baseUrl: 'http://localhost:3000'
    },
    mutations: {
        setUsers(state, data) {
            state.users = data;
        },
    },
    actions: {
        async fetchUsers({state, commit},) {
            const urlBase = state.baseUrl + "/user";
            let response = await Axios.get(urlBase);
            commit('setUsers', response.data);
            return response.data

        },
    },
    getters: {
        getUser(state) {
            return state.users;
        }
    }
});
