<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <span>DEPTH - </span>
                <span class="font-weight-light">Dashboard</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
        </v-app-bar>

        <v-container class="mt-10">
            <v-layout wrap>
                <router-view/>
            </v-layout>
        </v-container>

    </v-app>
</template>

<script>
    export default {
        name: 'App',
    };
</script>
