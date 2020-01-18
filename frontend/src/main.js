// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import * as backendAPI from './common/backendAPI'
import VueResource from 'vue-resource'
import VModal from 'vue-js-modal'

import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.css'

Vue.use(VModal)
Vue.use(VueResource)

Vue.config.productionTip = false

Vue.prototype.$api = backendAPI


new Vue({ 
    el: '#app', 
    router, 
    store, 
    render: h => h(App) 
})
