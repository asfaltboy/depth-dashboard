<template>
  <v-container>
    <v-data-table
            :headers="headers"
            :items="getUser"
            class="sm6 xs12"
            v-if="getUser"
    >
      <template
              slot="items"
              slot-scope="props"
      >
        <td class="text-xs-justify">
          {{ props.item.name }}
        </td>
        <td class="text-xs-justify">
          {{ props.item.description }}
        </td>
        <td class="text-xs-justify">
          <v-btn
                  @click="edit(props.item._id,props.item )"
                  color="grey lighten-5"
                  dark
                  fab
                  flat
                  slot="activator"
                  small
          >
            <v-icon dark>
              edit
            </v-icon>
          </v-btn>
        </td>

        <td class="text-xs-justify">
          <v-btn
                  @click="pause(props.item._id,props.item.name,props.item.enabled)"
                  color="grey lighten-5"
                  dark
                  fab
                  flat
                  slot="activator"
                  small
          >
            <v-icon
                    dark
                    v-if="props.item.enabled"
            >
              pause
            </v-icon>
            <v-icon
                    dark
                    v-else
            >
              play_arrow
            </v-icon>
          </v-btn>
        </td>
      </template>
    </v-data-table>
    <div v-if="componentKey > 0">
      <siteEdit :key="componentKey"/>
    </div>
  </v-container>
</template>
<script>
   import {mapGetters} from 'vuex'
  export default {
    data() {
      return {
        headers: [
          {text: "Name", value: "name"},
          {text: "Description", value: "description"},
          {text: "Edit", value: "_id"},
          {text: "Enabled", value: "enabled"}
        ],
      };
    },
    methods: {
      init: function () {
        this.$store.dispatch("fetchUsers");
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
  };
</script>


