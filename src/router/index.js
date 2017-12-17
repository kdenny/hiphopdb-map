import Vue from 'vue';
import Router from 'vue-router';
import example from '@/components/Example';
import HipHopMap from '@/components/Map';


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Example',
      component: example,
    },
    {
      path: '/map',
      name: 'HipHopMap',
      component: HipHopMap,
    },
  ],
});
