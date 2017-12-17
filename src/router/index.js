import Vue from 'vue';
import Router from 'vue-router';
import example from '@/components/Simple';
import MarkerPopupExample from '@/components/MarkerPopupExample';


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Example',
      component: example,
    },
    {
      path: '/custom-component',
      name: 'MarkerPopupExample',
      component: MarkerPopupExample,
    },
  ],
});
