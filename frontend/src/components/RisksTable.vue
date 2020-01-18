<template>
  <div class="container">
        <!-- risk table -->
        <div class="row">
            <div class="col-md-10">
                <vuetable 
                    ref="vuetable"
                    :api-mode="false"
                    :data="elements"
                    :fields="fields"
                ></vuetable>
            </div>
            <div class="col-md-2">
                <button class="btn btn-primary" @click="showModal">Add risk</button>
            </div>
        </div>
        <!-- add risk popup -->
        <risk-form :popup="popupContent"></risk-form>    
  </div>  
</template>
<script>
import Vue from 'vue'
import Vuetable from 'vuetable-2/src/components/Vuetable'
import moment from 'moment'
import CustomAction from '@/components/CustomAction'
import ClipLoader from 'vue-spinner/src/ClipLoader.vue'
import riskheaders from '@/components/riskheaders.js'
import { mapGetters } from 'vuex'
import RiskForm from '@/components/RiskForm'

Vue.component('custom-action', CustomAction)
export default {
  components: {
    Vuetable,
    ClipLoader,
    RiskForm
  },
  data () {
    return {
      fields: riskheaders,
      popupContent: {
        loading: false,
        mode: 'Add',
        name: 'add-risk',
        id: ''
      }
    }
  },
  created: function () {
    this.$store.dispatch('fetchRisks')
  },
  methods: {
    formatDate (val, fmt = 'DD MM YYYY HH:mm a') {
      return val === null
       ? ''
       : moment(val).format(fmt)
    },
    showModal () {
      this.popupContent.loading = true
      this.$modal.show(this.popupContent.name)
    }
  },
  computed: {
    ...mapGetters({
      elements: 'getRisks'
    })
  },
  watch: {
    elements: function (data) {
      this.$refs.vuetable.setData(data)
    }
  }
}
</script>
<style>
    .v--modal-overlay[data-modal="add-risk"] {
        background-color: transparent !important;
    }
    .align-add-risk-input {
        margin-top: 20px;
    }
    .custom-pull-buttons {
        margin-right: 55px;
    }
    .add-risk-header {
        padding-top: 20px;
    }
    textarea {
        resize: none;
    }
    .v-spinner-loader {
        margin-top: 100px;
    }
</style>