<template>
    <v-form v-model="valid">
        <v-container>
            <v-row>
                <v-col
                        cols="12"
                        md="4"
                >
                    <v-text-field
                            v-model="data"
                            :rules="nameRules"
                            :counter="10"
                            label="First name"
                            required
                    ></v-text-field>
                </v-col>

                <v-col
                        cols="12"
                        md="4"
                >
                    <v-text-field
                            v-model="data"
                            :rules="nameRules"
                            :counter="10"
                            label="Last name"
                            required
                    ></v-text-field>
                </v-col>

                <v-col
                        cols="12"
                        md="4"
                >
                    <v-text-field
                            v-model="data"
                            :rules="emailRules"
                            label="E-mail"
                            required
                    ></v-text-field>
                </v-col>
            </v-row>
        </v-container>
    </v-form>
</template>

<script>
    export default {
        data: () => ({
            data:[],
            nameRules: [
                v => !!v || 'Name is required',
                v => v.length <= 10 || 'Name must be less than 10 characters',
            ],
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+/.test(v) || 'E-mail must be valid',
            ],
        }),
    }
</script>
