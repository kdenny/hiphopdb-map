import Vue from 'vue'
import App from './App'
import router from './router'

L.Icon.Default.imagePath = "/images/";

new Vue({
  el: '#main',
  router,
  template: '<App/>',
  components: { App }
});
