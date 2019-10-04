<template>
    <v-form v-model="valid">
        <v-container>
            <v-row>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="First name"
                            outlined required
                            v-model="data['name']"
                    ></v-text-field>
                </v-col>
                <v-col
                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :rules="emailRules"
                            label="E-mail"
                            outlined required
                            v-model="data['email']"
                    ></v-text-field>
                </v-col>
                <v-col cols="12"
                       md="4">
                    <v-select
                            :items="sex"
                            outlined
                            item-text="name"
                            item-value="id"
                            return-object
                            label="Sex"
                            required
                            v-model="data['sex']"
                    ></v-select>
                </v-col>

                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Mother Tounge"
                            outlined required
                            v-model="data['tounge']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Program languages"
                            outlined required
                            v-model="data['program_languages']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Team"
                            outlined required
                            v-model="data['team']"
                    ></v-text-field>
                </v-col>

                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Role"
                            outlined required
                            v-model="data['role']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Office Location"
                            outlined required
                            v-model="data['office_location']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Projects"
                            outlined required
                            v-model="data['projects']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Nationalitie"
                            outlined required
                            v-model="data['nationalities']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Age"
                            outlined required
                            v-model="data['age']"
                    ></v-text-field>
                </v-col>

                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Favorite Movie"
                            outlined required
                            v-model="data['fav_movie']"
                    ></v-text-field>
                </v-col>
                <v-col

                        cols="12"
                        md="4"
                >
                    <v-text-field
                            :counter="10"
                            :rules="nameRules"
                            label="Operative System"
                            outlined required
                            v-model="data['os']"
                    ></v-text-field>
                </v-col>
                <v-space></v-space>
                <v-btn
                        :disabled="!valid"
                        @click="save"
                        class="mr-4"
                        color="success"
                >
                    Save
                </v-btn>
            </v-row>
        </v-container>
    </v-form>
</template>

<script>
    export default {
        data: () => ({
            data: [],
            sex:[
                {id:1,name:'Male'},
                {id:2,name:'Famale'}
            ],
            nameRules: [
                v => !!v || 'Name is  outlined required',
                v => v.length <= 10 || 'Name must be less than 10 characters',
            ],
            emailRules: [
                v => !!v || 'E-mail is  outlined required',
                v => /.+@.+/.test(v) || 'E-mail must be valid',
            ],
        }),
        methods: {
            save() {
                let   user = {
                    "id": 2,
                    "name": this.data['name'],
                    "email": this.data['email'],
                    "tounge": this.data['tounge'],
                    "sex": this.data['sex'],
                    "program_languages": [
                        this.data['program_languages']
                    ],
                    "nationalities": [
                        this.data['nationalities']
                    ],
                    "projects": [
                        this.data['projects']
                    ],
                    "team": this.data['team'],
                    "role": this.data['role'],
                    "oficce_location": this.data['oficce_location'],
                    "age": this.data['age'],
                    "fav_movie": this.data['fav_movie'],
                    "os": [this.data['os']]
                }
                this.$store.dispatch("postUser", user )
            }
        }
    }
</script>

