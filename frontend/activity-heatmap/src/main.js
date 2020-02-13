import Vue from 'vue'
import App from './App.vue'
// import HeatMap from './components/HeatMap.vue'
// import HelloWorld from './components/HelloWorld.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false
// const routes = {
//   '/': HelloWorld,
//   '/heatmap': HeatMap
// }
new Vue({
  // data: {
  //   currentRoute: window.location.pathname
  // },
  // computed:{
  //   ViewComponent(){
  //     return routes[this.currentRoute] 
  //   }
  // },
  render: h => h (App),
  vuetify
}).$mount('#app')
