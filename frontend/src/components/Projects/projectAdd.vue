<template>
    <v-form v-model="valid">
             <v-card>
                <v-card-title class="">
                    Create a new project
                </v-card-title>
                <v-card-text>
                    <v-row>
                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Name"
                                    outlined
                                    required v-model="data['name']"

                            ></v-text-field>
                        </v-col>

                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Lenguage"
                                    outlined
                                    required v-model="data['Lenguage']"

                            ></v-text-field>
                        </v-col>

                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Vertical"
                                    outlined
                                    required v-model="data['vertical']"

                            ></v-text-field>
                        </v-col>
                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Hosting"
                                    outlined
                                    required v-model="data['hosting']"

                            ></v-text-field>
                        </v-col>
                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Services"
                                    outlined
                                    required v-model="data['services']"

                            ></v-text-field>
                        </v-col>
                        <v-col
                                cols="12"
                                md="6"
                        >
                            <v-text-field
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Jira"
                                    outlined
                                    required v-model="data['jira']"

                            ></v-text-field>
                        </v-col>

                    </v-row>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            :disabled="!valid"
                            @click="save"
                            class="mr-4"
                            color="success"
                    >
                        Create Project
                    </v-btn>
                </v-card-actions>
            </v-card>
     </v-form>
</template>

<script>
    const uuidv1 = require('uuid/v1');

    export default {
        data: () => ({
            data: [],
            nameRules: [
                v => !!v || 'Name is required',
                v => v.length <= 10 || 'Name must be less than 10 characters',
            ],
        }),
        methods:{
            save(){
                let project = {
                    id:uuidv1(),
                    "languages": this.data['languages'],
                    "name": this.data['name'],
                    "vertical": this.data['vertical'],
                    "hosting": this.data['hosting'],
                    "services": this.data['services'],
                    "jira": this.data['jira']
                }
                this.$store.dispatch("postProject",project)
                    .then(()=>{
                    this.$refs.form.reset()
                }).catch((error)=>{
                    console.log(error)
                })
            }
        }
    }
</script>
