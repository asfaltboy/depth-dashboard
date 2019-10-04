<template>
    <v-flex class="xs12" :key="dom">
        <v-layout wrap>
            <v-flex class="xs12 md8 pa-3">
                <v-card>
                    <scatter-chart :data="[[174.0, 80.0], [176.5, 82.3]]" xtitle="Size" ytitle="Population"></scatter-chart>

                </v-card>
            </v-flex>
            <v-flex class="xs12 md4 pa-3">
                <v-card class="ma-3">
                    <line-chart :data="{'2017-01-01': 11, '2017-01-02': 6}"></line-chart>

                </v-card>
                <v-card class="ma-3">
                    <pie-chart :data="[['Blueberry', 44], ['Strawberry', 23]]"></pie-chart>

                </v-card>
                <v-card class="ma-3">
                    <column-chart :data="[['Sun', 32], ['Mon', 46], ['Tue', 28]]"></column-chart>

                </v-card>

            </v-flex>

        </v-layout>
    </v-flex>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        name: "metricsView",
        data(){
            return{
                graficData : [],
                getAges : [],
                getNationalities : [],
                getOS : [],
                dom:0
            }
        },
        methods: {
            init: function () {
                this.$store.dispatch("fetchUsers").then(()=>{
                    this.getElementes('age')
                    this.getElementes('age')
                    this.getElementes('age')
                },this);
            },
            getElementes(ele,data) {
                let vue = this
                data.forEach(function (element) {
                    console.log(element)
                    vue.graficData.push(element[ele])
                    vue.dom ++;
                });
                return true
            }

        },
        computed: {
            ...mapGetters([
                'getUser',
            ])
        },
        created() {
            this.init();
        },
    }
</script>

<style scoped>

</style>