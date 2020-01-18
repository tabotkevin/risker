<template>
  <div class="container">
        <!-- risk table -->
        <div class="row">
           <div class="col-md-10">
           <h4>Risk</h4>
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ this.$store.state.risk.name }}</td>
                  <td>{{ this.$store.state.risk.description }}</td>
                </tr>
              </tbody>
            </table>

           </div>
        </div>
        <div class="row">
            <div class="col-md-10">
                <h4>Fields</h4>
                <vuetable 
                    ref="vuetable"
                    :api-mode="false"
                    :data="elements"
                    :fields="fields"
                ></vuetable>
            </div>
            <div class="col-md-2">
                <h4>&nbsp;</h4>
                <button class="btn btn-primary" @click="showModal">Add Field</button>
            </div>
        </div>
        <!-- add risk popup -->
        <field-form :popup="popupContent"></field-form>    
  </div>  
</template>
<script>
import Vue from 'vue'
import Vuetable from 'vuetable-2/src/components/Vuetable'
import moment from 'moment'
import CustomActionField from '@/components/CustomActionField'
import ClipLoader from 'vue-spinner/src/ClipLoader.vue'
import fieldheaders from '@/components/fieldheaders.js'
import { mapGetters } from 'vuex'
import FieldForm from '@/components/FieldForm'

Vue.component('custom-action-field', CustomActionField)
export default {
  components: {
    Vuetable,
    ClipLoader,
    FieldForm
  },
  data () {
    return {
      fields: fieldheaders,
      popupContent: {
        loading: false,
        mode: 'Add',
        name: 'add-field',
        id: ''
      }
    }
  },
  created: function () {
    this.$store.dispatch('fetchFields', this.$route.params.id)
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
      elements: 'getFields'
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