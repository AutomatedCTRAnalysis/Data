<template>
  <div id="app">
  <b-input placeholder="No label" rounded v-model="searchBar"></b-input>
  <b-button type="is-primary is-light" @click="submitSearchForm">Primary Light</b-button>
  <b-field>
    <b-input type="textarea"
      minlength="10"
      maxlength="100"
      placeholder="Input text"
      v-model="searchTextArea">
    </b-input> 
  </b-field>
  <b-button type="is-primary is-light" @click="submitTextForm">Primary Light</b-button>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      searchBar: '',
      searchTextArea: '',
    }
  },
  methods: {
    submitSearchForm() {
      alert(this.searchBar)
    },
    submitTextForm(){
      alert(this.searchTextArea)
    }
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  max-width: 768px;
  margin: 0 auto; 
}
</style>
