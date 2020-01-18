import Vuex from 'vuex'
import Vue from 'vue'
import * as types from './mutation-types'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import VueResource from 'vue-resource'

const debug = process.env.NODE_EVN !== 'production'
const API_URL = 'http://localhost:8000/'
const RISK_URL = API_URL + 'risks/'
const FIELD_URL = API_URL + 'fields/'
const LOGIN_URL = API_URL + 'api-token-auth/'

Vue.use(VueResource)
Vue.use(Vuex)

const state = {
  user: {},
  token: null,
  risks: [],
  risk: {},
  field: {},
  fields: [],
  editRiskId: '',
  editFieldId: '',
  viewRiskId: ''
}

const mutations = {
  [types.LOGIN]: (state, payload) => {
    state.token = payload.token
    state.user = payload.user
    router.push(payload.redirect)
  },
  [types.LOGOUT]: (state, payload) => {
    state.token = null
    state.user = {}
    router.push(payload.redirect)
  },
  [types.TITLE]: (state, data) => {
    state.title = data
  },
  [types.GET_RISKS] (state, { items }) {
    state.risks = items
  },
  [types.GET_RISK] (state, { items }) {
    state.risk = items
  },

  [types.ADD_RISK] (state, { item }) {
    state.risks.push(item)
  },
  [types.EDIT_RISK] (state, id) {
    state.editRiskId = id
    state.risk = state.risks.find(p => p.id === id)
  },
  [types.VIEW_RISK] (state, id) {
    state.viewRiskId = id
    state.risk = state.risks.find(p => p.id === id)
  },
  [types.UPDATE_RISKS] (state, { item }) {
    const record = state.risks.find(p => p.id === item.id)
    if (record) {
      record.name = item.name
      record.description = item.description
    }
  },
  [types.DELETE_RISK] (state, { id }) {
    const record = state.risks.findIndex(p => p.id === id)
    if (record >= 0) {
      state.risks.splice(record, 1)
    }
  },

  [types.GET_FIELDS] (state, { items }) {
    state.fields = items
  },
  [types.ADD_FIELD] (state, { item }) {
    state.fields.push(item)
  },
  [types.EDIT_FIELD] (state, id) {
    state.editFieldId = id
    state.field = state.fields.find(p => p.id === id)
  },
  [types.UPDATE_FIELDS] (state, { item }) {
    const record = state.fields.find(p => p.id === item.id)
    if (record) {
      record.name = item.name
      record.value = item.value
    }
  },
  [types.DELETE_FIELD] (state, { id }) {
    const record = state.fields.findIndex(p => p.id === id)
    if (record >= 0) {
      state.fields.splice(record, 1)
    }
  }
}

const actions = {
  [types.LOGIN] ({ commit }, payload) {
    axios.post(LOGIN_URL, payload.credential)
    .then(response => {
      if (response.data.token) {
        var mutationPayload = {}
        mutationPayload.token = response.data.token
        mutationPayload.user = JSON.parse(atob(response.data.token.split('.')[1]))
        mutationPayload.user.authenticated = true
        mutationPayload.redirect = payload.redirect
        commit(types.LOGIN, mutationPayload)
      }
    })
    .catch(e => {
      payload.error = 'Incorrect username or password'
      console.log(e)
    })
  },

  fetchRisks ({ commit }) {
    axios.get(RISK_URL)
    .then(response => {
      commit(types.GET_RISKS, {
        items: response.data
      })
    })
    .catch(e => {
      console.log(e)
    })
  },

  fetchRisk ({ commit, state }, risk) {
    axios.get(RISK_URL + risk)
    .then(response => {
      commit(types.GET_RISK, {
        items: response.data
      })
    })
    .catch(e => {
      console.log(e)
    })
  },

  addRisk ({ commit, state }, risk) {
    axios.post(RISK_URL, risk)
    .then(response => {
      commit(types.ADD_RISK, {
        item: response.data
      })
    })
    .catch(e => {
      console.log(e)
    })
  },

  editRisk ({ commit, state }, risk) {
    axios.put(RISK_URL + state.editRiskId + '/', risk)
    .then(response => {
      commit(types.UPDATE_RISKS, {
        item: response.data
      })
    })
    .catch(error => {
      console.log(error)
    })
  },

  deleteRisk ({ commit }, id) {
    axios.delete(RISK_URL + id + '/')
    .then(response => {
      commit(types.DELETE_RISK, { id })
      console.log('risk deleted successfully!!')
    })
    .catch(e => {
      console.log(e)
    })
  },

  fetchFields ({ commit }, riskId) {
    axios.get(FIELD_URL + 'risk/' + riskId + '/')
    .then(response => {
      commit(types.GET_FIELDS, {
        items: response.data
      })
      commit(types.VIEW_RISK, riskId)
    })
    .catch(e => {
      console.log(e)
    })
  },

  addField ({ commit, state }, field) {
    console.log(field)
    axios.post(FIELD_URL, field)
    .then(response => {
      commit(types.ADD_FIELD, {
        item: response.data
      })
    })
    .catch(e => {
      console.log(e)
    })
  },

  editField ({ commit, state }, field) {
    axios.put(FIELD_URL + state.editFieldId + '/', field)
    .then(response => {
      commit(types.UPDATE_FIELDS, {
        item: response.data
      })
    })
    .catch(error => {
      console.log(error)
    })
  },

  deleteField ({ commit }, id) {
    axios.delete(FIELD_URL + id + '/')
    .then(response => {
      commit(types.DELETE_FIELD, { id })
      console.log('field deleted successfully!!')
    })
    .catch(e => {
      console.log(e)
    })
  }

}

const getters = {
  getRisks: state => state.risks,
  getRisk: state => state.risk,
  getEditRiskId: state => state.editRiskId,
  getFields: state => state.fields,
  getEditFieldId: state => state.editFieldId
}

const store = new Vuex.Store({
  state,
  strict: debug,
  getters,
  mutations,
  actions,
  plugins: [
    createPersistedState()
  ]
})

export default store
