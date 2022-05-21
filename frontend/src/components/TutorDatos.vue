<template lang="">
  {{obtenerTutor(id)}}
    <tr style="text-align: justify;">
        <td class="text-start">{{resultado.nombre}} {{resultado.apellidoPaterno}} {{resultado.apellidoMaterno}}</td>
        <td class="text-end">{{resultado.correo}}</td>
        <td class="text-center">{{resultado.telPrincipal}}</td>
        <td class="text-center">{{resultado.telSecundario}}</td>
    </tr>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import axios from "axios";
export default {
  props: {
    id: String,
  },
  data() {
    return {
      url: "http://127.0.0.1:5000/tutor/",
      idTutor: '',
      resultado: '',
      posts: [],
      errors: [],
    };
  },
  methods: {
    obtenerTutor(id) {
      const uri = this.url + id;
      console.log(uri)
      axios.get(uri)
        .then((response) => {
          // JSON responses are automatically parsed.
          this.resultado = response.data;
        })
        .catch((e) => {
          // this.errors.push(e)
          console.log(e);
        });
    },
  },
};
</script>
<style lang="">
</style>
