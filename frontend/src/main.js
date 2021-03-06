import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from './plugins/vuetify';
import Vuetify from 'vuetify'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'
import "material-design-icons-iconfont/dist/material-design-icons.css";


Vue.use(Chartkick.use(Chart))
Vue.use(Vuetify)
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
