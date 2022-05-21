<template >
    <div style="--bs-body-bg: var(--bs-purple);background: url(assets/img/fondo-cuadricula-purpura.jpeg) bottom / contain, rgb(255,255,255);border-left-style: solid;">
        <div class="container" style="padding-top: 12px; min-height: 600px;color:white">
            <h4 style="padding-top: 12px; padding-bottom: 12px">Bienvenido a FUNKIDUUH!, por favor ingresa los datos <br> para comenzar con tu diversion</h4>
            <div v-if="idTutor==''">
                <h5>- Datos del tutor -</h5>
                <form class="row mb-2" v-on:submit.prevent="submitFormTutor">
                    <div class="row mb-2 justify-content-center align-items-center">
                        <div class="col-md-2">
                            <label for="nombre" class="form-label">Nombre(s)</label>
                            <input type="text" class="form-control" id="nombre" v-model="formTutor.nombre">
                        </div>
                        <div class="col-md-2">
                            <label for="apellidopaterno" class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" id="apellidoPaterno" v-model="formTutor.apellidoPaterno">
                        </div>
                        <div class="col-md-2">
                            <label for="apellidomaterno" class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" id="apellidoMaterno" v-model="formTutor.apellidoMaterno">
                        </div>
                    </div>
                    <div class="row mb-4 justify-content-center align-items-center">
                        <div class="col-md-2 ">
                            <label for="email" class="form-label">Email</label>
                            <input type="email" class="form-control" id="correo" v-model="formTutor.correo">
                        </div>
                        <div class="col-md-2">
                            <label for="telprincipal" class="form-label">Telefono Principal</label>
                            <input type="tel" class="form-control" id="telPrincipal" v-model="formTutor.telPrincipal">
                        </div>
                        <div class="col-md-2">
                            <label for="telsecundario" class="form-label">Telefono Secundario</label>
                            <input type="tel" class="form-control" id="telSecundario" v-model="formTutor.telSecundario">
                        </div>
                    </div>
                    <div class="col-4 mx-auto gap-2 d-grid">
                        <button class="btn btn-success" style="color:white">Continuar</button>
                    </div>
                </form>
            </div>
            <div v-else class="row">
                <div class="col" style="background: rgba(0,0,0,0.25);margin: 0 200px 0 200px;padding: 6px;">
                    <h5 style="color: rgb(227,185,255);text-align: center;">Información del Tutor&nbsp;👩👨</h5>
                    <div class="table-responsive-md" style="padding-top: 20px;">
                        <table class="table">
                            <thead style="color: rgb(227,185,255);">
                                <tr>
                                    <th class="text-start">nombre 💬</th>
                                    <th class="text-end">correo ✉️</th>
                                    <th class="text-center">tel 📱</th>
                                    <th class="text-center">tel (2) 📱</th>
                                </tr>
                            </thead>
                            <tbody style="color: white">
                                <tutor-datos :id="idTutor"></tutor-datos>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <br>
            <div v-if="idTutor!=''">
                <div v-if="menorAdd==1">
                    <div class="col" style="background: rgba(0,0,0,0.25);margin: 0 188px 0 188px;padding: 6px;">
                        <h5 style="color: rgb(227,185,255);font-weight: bold;text-align: center;">Informacion de los Menores 🧒</h5>
                        <div class="table-responsive" style="padding-top: 20px;">
                            <table class="table">
                                <thead style="color: rgb(227,185,255);">
                                    <tr>
                                        <th class="text-start">nombre 💬</th>
                                        <th class="text-end">nacimiento 🎂</th>
                                        <th class="text-center">edad 📜</th>
                                    </tr>
                                </thead>
                                <tbody style="color: white">
                                    <menor-datos :id="idTutor"></menor-datos>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                <form v-if="terminarRegistro==false" id="FormMenor" class="row mb-2" v-on:submit.prevent="submitFormMenor" style="padding-top:10px">
                    <h5>Agrega nuevo Menor</h5>
                    <div class="row mb-2 justify-content-center align-items-center">
                        <div class="col-md-2">
                            <label for="primerNombre" class="form-label">Primer Nombre</label>
                            <input type="text" class="form-control" id="primerNombre" v-model="formMenor.primerNombre">
                        </div>
                        <div class="col-md-2">
                            <label for="segundoNombre" class="form-label">Segundo Nombre</label>
                            <input type="text" class="form-control" id="segundoNombre" v-model="formMenor.segundoNombre">
                        </div>
                        <div class="col-md-2">
                            <label for="apellidopaterno" class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" id="apellidoPaterno" v-model="formMenor.apellidoPaterno">
                        </div>
                    </div>
                    <div class="row mb-4 justify-content-center align-items-center">
                        <div class="col-md-3">
                            <label for="apellidomaterno" class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" id="apellidoMaterno" v-model="formMenor.apellidoMaterno">
                        </div>
                        <div class="col-md-3 ">
                            <label for="fechaNacimiento" class="form-label">Fecha de Nacimiento</label>
                            <input type="date" class="form-control" id="fechaNacimiento" v-model="formMenor.fechaNacimiento">
                        </div>
                    </div>
                    <div class="col-2 mx-auto gap-2 d-grid">
                        <button type="submit" class="btn btn-success" style="color:white;">Agregar</button>
                    </div>
                </form>
                <br>
                <form v-if="terminarRegistro==false" class="row mb-2" v-on:submit.prevent="submitVisita">
                    <div v-if="menorAdd!=0" class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-outline-warning" >Continuar</button>
                    </div>
                </form>
                <div v-if="terminarRegistro==true" class="row" style="margin: 0 200px 0 200px">
                    <div class="d-grid gap-2 col-4 mx-auto">
                        <button @click="submitVisita()" class="btn btn-warning" type="button">Agregar otro Menor</button>
                    </div>
                    <div class="d-grid gap-2 col-4 mx-auto">
                            <button @click="cancelarRegistro();home();" class="btn btn-danger">Cancelar Registro</button>
                    </div>
                    <div class="d-grid gap-2 col-4 mx-auto">
                        <button @click="finalizarRegistro()" class="btn btn-success" type="button" style="color:white;">Finalizar Registro</button>
                    </div>
                </div>
                <br><br>
            </div>
        </div>
    </div>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import axios from "axios";
import TutorDatos from "../components/TutorDatos.vue";
import MenorDatos from "../components/MenorDatos.vue";
export default {
    name: 'RegistrarVisitaView',
    components: {
        TutorDatos,
        MenorDatos
    },
    props: {
        idTutor: String
    },
    data() {
        return {
            formTutor: {
                    nombre: '',
                    apellidoPaterno: '',
                    apellidoMaterno: '',
                    correo: '',
                    telPrincipal: '',
                    telSecundario: ''
                },
            formMenor: {
                    primerNombre: '',
                    segundoNombre:'',
                    apellidoPaterno: '',
                    apellidoMaterno: '',
                    fechaNacimiento:''
                },
            idTutor:'',
            idVisita:'',
            menorAdd:0,
            terminarRegistro:false,
            irAhome:0,
        };
    },
    methods: {
        submitFormTutor(){
            axios.post('http://127.0.0.1:5000/tutor', this.formTutor)
                 .then((res) => {
                     this.idTutor=res.data._id;
                 })
                 .catch((error) => {
                     console.log(error)
                 })
        },
        submitFormMenor(){
            const url='http://127.0.0.1:5000/menor/'+this.idTutor;
            axios.post(url, this.formMenor)
                 .then((res) => {
                     this.idMenor=res.data._id;
                     this.menorAdd=1;
                 })
                 .catch((error) => {
                     console.log(error)
                 })
            document.getElementById("FormMenor").reset();
        },
        submitVisita(){
           this.terminarRegistro=!this.terminarRegistro
           document.getElementById("FormMenor").reset()
        },
        finalizarRegistro(){
            this.$router.push({name:"cartacompromiso",params:{data:this.idTutor}})
            localStorage.setItem('idTutor',this.idTutor);
        },
        cancelarRegistro(){
            const uriMenores='http://127.0.0.1:5000/menor/varios/'+this.idTutor;
            const uriTutor='http://127.0.0.1:5000/tutor/'+this.idTutor;
            axios.delete(uriMenores)
                .then((res)=>{
                    console.log(res.data)
                })
                .catch((err)=>{
                    console.log("Error Menores")
                    console.log(err)
                })
            axios.delete(uriTutor)
                .then()
                .catch((err)=>{
                    console.log("Error Tutor")
                    console.log(err)
                })
        },
        home(){
            this.$router.push({name:"home"})
        }
    }
}
</script>
<style lang="">
</style>
