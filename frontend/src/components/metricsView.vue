<template>
    <v-flex :key="dom" class="xs12">
        <v-layout wrap>
            <v-flex class="xs12 md8 pa-3">
                <v-card class="pa-5">
                    <scatter-chart :data="[[174.0, 80.0], [176.5, 82.3],[123.0, 10.0], [156.5, 22.3]]" xtitle="Size"
                                   ytitle="Population"></scatter-chart>

                </v-card>
            </v-flex>
            <v-flex class="xs12 md4 pa-3">
                <v-card class="pa-4 ma-4">
                    <line-chart :data="{'2017-01-01': 11, '2017-01-02': 6}"></line-chart>

                </v-card>
                <v-card class="pa-4 ma-4">
                    <pie-chart :data="[['Blueberry', 44], ['Strawberry', 23]]"></pie-chart>

                </v-card>
                <v-card class="pa-4 ma-4">
                    <column-chart :data="[['Sun', 32], ['Mon', 46], ['Tue', 28],['Sun', 32], ['Wen', 46], ['Fra', 28]]"></column-chart>

                </v-card>

            </v-flex>

        </v-layout>
    </v-flex>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        name: "metricsView",
        data() {
            return {
                graficData: [],
                Ages: [],
                Role: [],
                Team: [],
                getNationalities: [],
                getOS: [],
                dom: 0
            }
        },
        methods: {
            init: function () {
                this.$store.dispatch("fetchUsers").then((response) => {
                   this.Ages =  this.getElementes('age', response);
                   this.Role =  this.getElementes('role', response);
                    this.Team = this.getElementes('team', response);
                }, this);
            },
            getElementes(ele, data) {
                let elements = [];
                data.forEach(function (element) {
                    elements.push({ele : element[ele]})
                });
               return elements
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