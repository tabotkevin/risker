<template>
    <modal :name="modalData.name" width="50%" height="40%">
        <div v-if="modalData.loading" class="v-spinner-loader">
            <clip-loader></clip-loader>
        </div>
        <div v-else>
            <div  class="row">
                <h3 class="text-center text-primary add-field-header">{{ modalData.mode }} field</h3>
                <div class="col-md-10 col-md-offset-1">
                  <div class="form-group align-add-field-input">
                      <input type="text" class="form-control" 
                        v-model="fieldName"
                        placeholder="add new field" id="addFieldContainer">
                  </div>
                  <div class="form-group align-add-field-input">
                      <select v-model="fieldType" class="form-control" v-on:change="setType()">
                        <option value="" disabled selected hidden>Select value type..</option>
                        <option value="date">Date</option>
                        <option value="enum">Enum</option>
                        <option value="number">Number</option>
                        <option value="text">Text</option>
                      </select>
                  </div>
                  <div class="form-group align-add-field-input" v-if="!hideText">
                      <input type="text" class="form-control" 
                        v-model="fieldValue"
                        placeholder="Enter Value" id="addFieldContainer">
                  </div>
                  <div class="form-group align-add-field-input" v-if="!hideNumber">
                      <input type="number" class="form-control" 
                        v-model="fieldValue"
                        placeholder="Enter Value" id="addFieldContainer">
                  </div>
                  <div class="form-group align-add-field-input" v-if="!hideDate">
                      <input type="date" class="form-control" 
                        v-model="fieldValue"
                        placeholder="Enter date" id="addFieldContainer">
                  </div>
                  <div class="form-group align-add-field-input" v-if="!hideEnum">
                      <select v-model="fieldValue" class="form-control">
                        <option value="option1">Option 1</option>
                        <option value="option2">Option 2</option>
                        <option value="option3">Option 3</option>
                        <option value="option4">Option 4</option>
                      </select>
                  </div>
                </div>
                <div class="col-sm-1"></div>
            </div>
            <div class="pull-right custom-pull-buttons">
                <button class="btn btn-primary" @click="addOrEditField(modalData.mode, modalData.id)">{{ modalData.mode !== 'Edit' ? 'Submit' :  modalData.mode }}</button>
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
      fieldName: '',
      fieldValue: '',
      fieldType: '',
      fieldRoldId: '',
      hideText: true,
      hideDate: true,
      hideEnum: true,
      hideNumber: true
    }
  },
  methods: {
    hideModal () {
      this.$modal.hide(this.popup.name)
    },
    setType () {
      if (this.fieldType === 'text') {
        this.hideText = false
        this.hideEnum = true
        this.hideDate = true
        this.hideNumber = true
      }
      if (this.fieldType === 'enum') {
        this.hideEnum = false
        this.hideText = true
        this.hideDate = true
        this.hideNumber = true
      }
      if (this.fieldType === 'date') {
        this.hideDate = false
        this.hideText = true
        this.hideEnum = true
        this.hideNumber = true
      }
      if (this.fieldType === 'number') {
        this.hideNumber = false
        this.hideText = true
        this.hideEnum = true
        this.hideDate = true
      }
    },
    updateField (operation) {
      this.$store.dispatch(operation, {
        name: this.fieldName,
        value: this.fieldValue,
        type: this.fieldType,
        risk_id: this.$route.params.id
      }).then(() => {
        this.hideModal()
      })
    },
    addOrEditField (mode) {
      if (mode !== 'Edit') {
        this.updateField('addField')
      } else {
        this.updateField('editField')
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
      this.modalData = this.popup
    }
  }
}
</script>
