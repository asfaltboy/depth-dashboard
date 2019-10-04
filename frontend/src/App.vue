<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <span>DEPTH - </span>
                <span class="font-weight-light">Dashboard</span>
            </v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-menu
                        :key="index"
                        offset-y
                        v-for="(item, index) in topMenuBar"
                >
                    <v-btn
                            :to="item.href"
                            class="no_border_radius no_Shadow"

                            slot="activator"
                    >
                        <v-icon class="ml-2 pa-2"
                        >
                            {{ item.icon }}
                        </v-icon>
                        {{ item.name }}
                    </v-btn>
                </v-menu>

            </v-toolbar-items>
        </v-app-bar>

        <v-container class="mt-10">
            <v-layout wrap class="pt-6">
                <router-view/>
            </v-layout>
        </v-container>

    </v-app>
</template>

<script>
    export default {
        name: 'App',
        data() {
            return {
                topMenuBar: [
                    {icon: "home", name: "Home", href: "/"},
                    {icon: "subscriptions", name: "Users Dashboard", href: "/user_dashboard"},
                    {icon: "filter_list", name: "Add Users", href: "/add_users"},
                    {icon: "domain_disabled", name: "Add Projects", href: "/add_projects"}

                ]
            }
        }
    };
</script>
