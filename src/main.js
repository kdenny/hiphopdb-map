import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import router from './router'

L.Icon.Default.imagePath = "/images/";

Vue.use(BootstrapVue);

new Vue({
  el: '#main',
  router,
  template: '<App/>',
  components: { App }
});
