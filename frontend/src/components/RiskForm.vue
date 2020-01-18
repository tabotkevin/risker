<template>
    <modal :name="modalData.name" width="50%" height="40%">
        <div v-if="modalData.loading" class="v-spinner-loader">
            <clip-loader></clip-loader>
        </div>
        <div v-else>
            <div  class="row">
                <h3 class="text-center text-primary add-risk-header">{{ modalData.mode }} risk</h3>
                <div class="col-md-10 col-md-offset-1">
                <div class="form-group align-add-risk-input">
                    <input type="text" class="form-control" 
                      v-model="riskName"
                      placeholder="add new risk" id="addRiskContainer">
                </div>
                <div class="form-group align-add-risk-input">
                    <textarea v-model="riskDesc" class="form-control"
                     placeholder="add description"></textarea>
                </div>
                </div>
                <div class="col-sm-1"></div>
            </div>
            <div class="pull-right custom-pull-buttons">
                <button class="btn btn-primary" @click="addOrEditRisk(modalData.mode, modalData.id)">{{ modalData.mode !== 'Edit' ? 'Submit' :  modalData.mode }}</button>
                <button class="btn btn-default" @click="hideModal">Cancel</button>
            </div>
        </div>
    </modal> 
</template>
<script>
import ClipLoader from 'vue-spinner/src/ClipLoader.vue'
export default {
  components: {
    ClipLoader
  },
  props: {
    popup: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      modalData: this.popup,
      riskName: '',
      riskDesc: ''
    }
  },
  methods: {
    hideModal () {
      this.$modal.hide(this.popup.name)
    },
    updateRisk (operation) {
      this.$store.dispatch(operation, {
        name: this.riskName,
        description: this.riskDesc
      }).then(() => {
        this.hideModal()
      })
    },
    addOrEditRisk (mode) {
      if (mode !== 'Edit') {
        this.updateRisk('addRisk')
      } else {
        this.updateRisk('editRisk')
      }
    }
  },
  created: function () {
    setInterval(() => {
      this.popup.loading = false
    }, 1000)
  },
  watch: {
    popup: function (data) {
      console.log('watcher is called')
      this.modalData = this.popup
    }
  }
}
</script>
