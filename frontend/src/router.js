import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "metricsView",
            component: () =>
                import("@/components/metricsView.vue")
        }, {
            path: "/user_dashboard",
            name: "dashboard",
            component: () =>
                import("@/components/dashboard.vue")
        },
        {
            path: "/metrics",
            name: "metrics",
            component: () =>
                import("@/components/metricsView.vue")
        },
        {
            path: "/add_users",
            name: "Add Users",
            component: () =>
                import("@/components/Users/userAdd.vue")
        },
        {
            path: "/edit_users",
            name: "Edit Users",
            component: () =>
                import("@/components/Users/usersEdit.vue")
        },
        {
            path: "/add_projects",
            name: "Add projects",
            component: () =>
                import("@/components/Projects/projectAdd.vue")
        },
        {
            path: "/edit_projects",
            name: "Edit projects",
            component: () =>
                import("@/components/Projects/projectEdict.vue")
        }

    ]
});
