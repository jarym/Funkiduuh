<template lang="">
  {{obtenerMenor(id)}}
  <tr style="text-align: justify;" v-for="res in resultado" v-bind:key="res">
      <td class="text-start">{{res.primerNombre}} {{res.segundoNombre}} {{res.apellidoPaterno}} {{res.apellidoMaterno}}</td>
      <td class="text-end">{{res.fechaNacimiento.$date.substr(0,10)}}</td>
      <td class="text-center">{{res.edad}}</td>
  </tr>
</template>
<script>
import axios from 'axios'
export default {
  props: {
    id: String
  },
  data () {
    return {
      url: 'http://127.0.0.1:5000/menor/varios/',
      idMenor: null,
      resultado: '',
      posts: [],
      errors: []
    }
  },
  methods: {
    obtenerMenor (id) {
      this.idMenor = this.url + id
      axios.get(this.idMenor)
        .then((response) => {
          // JSON responses are automatically parsed.
          this.resultado = response.data
        })
        .catch((e) => {
          // this.errors.push(e)
          console.log(e)
        })
    }
  }
}
</script>
<style lang="">
</style>
