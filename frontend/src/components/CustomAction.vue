<template>
    <div class="custom-actions">
      <button class="ui basic button" @click="viewItem(rowData.id)"><i class="zoom icon"></i></button>
      <button class="ui basic button" @click="editItem(rowData.id)"><i class="edit icon"></i></button>
      <button class="ui basic button" @click="deleteItem(rowData.id)"><i class="delete icon"></i></button>
      <risk-form :popup="popupContent"></risk-form>
    </div>
  </template> 
  <script>
  import RiskForm from '@/components/RiskForm'
  import * as types from '@/store/mutation-types.js'

  export default {
    components: {RiskForm},
    props: {
      rowData: {
        type: Object,
        required: true
      },
      rowIndex: {
        type: Number
      }
    },
    data () {
      return {
        popupContent: {
          loading: false,
          mode: 'Edit',
          name: 'risk-edit',
          id: this.rowData.id
        }
      }
    },
    methods: {
      editItem (id) {
        this.popupContent.loading = true
        this.$store.commit(types.EDIT_RISK, id)
        this.$modal.show(this.popupContent.name)
      },
      viewItem (id) {
        this.$router.push({path: '/risk', name: 'Risk', params: {'id': id}})
      },
      deleteItem (index) {
        this.$store.dispatch('deleteRisk', index)
      }
    }
  }
  </script>

  <style>
    .custom-actions button.ui.button {
      padding: 8px 8px;
    }
    .custom-actions button.ui.button > i.icon {
      margin: auto !important;
    }
  </style>