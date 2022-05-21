<template>
  <div>
    <div  class="container" style="padding-top: 12px">
      <div class="row" style="margin-top: 6px">
        <div ref="pdf1" class="col-md-10 col-lg-8 col-xl-8 mx-auto">
          <header class="text-center text-white masthead" style="background: linear-gradient(86deg, #3155e0 5%, #5f0fc8 17%, rgb(123,25,188) 49%, var(--bs-pink) 100%);padding: 1px 0px;">
            <div>
                <div class="row">
                    <div class="col"></div>
                    <div class="col-sm-3 col-md-3 mx-auto"><img class="img-fluid" src="assets/img/logotipo-cuadrado.png" style="max-height: 80px;"></div>
                    <div class="col-sm-7 col-md-5 mx-auto position-relative" style="padding-right: 0px;">
                        <p class="text-uppercase" style="font-size: 18px;font-family: 'Be Vietnam Pro', sans-serif;"><strong>Funkiduuh</strong><br></p>
                        <p style="font-size: 16px;">Grupo Inmobiliario CYKA</p>
                    </div>
                    <div class="col"></div>
                </div>
            </div>
          </header>
          <div class="row">
            <div class="col">
              <!--
              <p style=" text-align: left; font-weight: bold; " >
                Folio de compra: ---FOLIO---
              </p>-->
            </div>
            <div class="col">
              <p style=" text-align: right; font-weight: bold; " v-show="fechaActual" >
                Fecha: {{ fechaActual }}
              </p>
            </div>
          </div>
          <p style="font-size: 14px; font-weight: bold">
            Carta de Advertencia de Riesgos y Reconocimiento y Aceptación de
            Responsabilidades, por el uso de instalaciones y participación de
            actividades dentro del complejo operativo y de atracción
            identificado como FUNKIDUUH! .
          </p>
          <div>
            <h6 style="font-weight: bold">
              I.- Advertencia de Riesgos al Usuario:
            </h6>
            <p style="text-align: justify; font-size: 12px">
              En un primer término a través de la presente, se hace del
              conocimiento del usuario, responsable, padre y/o tutor, que las
              instalaciones, aditamentos y elementos que conforman la atracción
              denominada FUNKIDUUH, presenta riesgos significativos en sus
              actividades asociadas principalmente con el uso de trampolines,
              camas elásticas, laberintos, juegos interactivos y actividades
              complementarias, por ello Grupo Inmobiliario Cyka FUNKIDUUH ha
              tomado las medidas requeridas para proporcionarle el equipo y la
              asesoría de un personal calificado, pero no obstante de ello, como
              se menciona, las actividades asociadas a la presente atracción, no
              están exentas de riesgos implícitos que no pueden eliminarse sin
              destruir el carácter único de la atracción, por lo tanto para su
              seguridad y la de otros participantes, es importante que usted sea
              notificado de los riesgos y siga en todo momento las instrucciones
              de nuestro personal capacitado.
            </p>
          </div>
          <div>
            <h6 style="font-weight: bold">
              II.- Reconocimiento de Riesgos por el Usuario:
            </h6>
            <p style="text-align: justify; font-size: 12px">
              Por medio del presente, el presente usuario, responsable, padre
              y/o tutor de ser necesario reconozco que a continuación se
              describen algunos, pero no todos, de los riesgos de lesiones
              personales, accidentes y enfermedades, incluyendo, pero no
              limitando a lo siguiente:
            </p>
            <ul style="font-size: 12px; text-align: justify">
              <li style="text-align: left">Esguince.</li>
              <li style="text-align: left">Roturas de ligamentos.</li>
              <li style="text-align: left">
                Lesiones musculares de cualquier índole.
              </li>
              <li style="text-align: left">Huesos fracturados o rotos.</li>
              <li style="text-align: left">Lesiones oculares.</li>
              <li style="text-align: left">
                Cortes, heridas, rasguños, raspaduras, contusiones.
              </li>
              <li style="text-align: left">Exposición a deshidratación.</li>
              <li style="text-align: left">Falta de oxígeno.</li>
              <li style="text-align: left">Lesiones de columna vertebral.</li>
              <li style="text-align: left">Lesiones del cerebro y cuello.</li>
              <li style="text-align: left">
                Reacción alérgica, parálisis, shock o muerte.
              </li>
            </ul>
            <p style="text-align: justify; font-size: 12px">
              Por lo anterior el presente usuario, responsable, padre y/o
              tutor,entiendo que la descripción de estos riesgos, no se ha
              completado y que los riesgos desconocidos o inesperados pueden dar
              lugar a lesiones, enfermedades o la muerte.
            </p>
          </div>
          <div>
            <h6 style="font-weight: bold">
              III.- Aceptación de riesgos y responsabilidad por el Usuario.
            </h6>
            <p style="text-align: justify; font-size: 12px">
              El usuario, responsable, padre y/o tutor, estoy de acuerdo en
              asumir la responsabilidad derivada del uso de las instalaciones de
              Grupo Inmobiliario Cyka FUNKIDUUH, por los riesgos descritos e
              identificados en el presente documento y los riesgos no
              identificados.<br /><br />Por lo anterior y por conducto del
              presente declaro y constato, que participación en estas
              actividades
              <strong
                >es completamente voluntaria, consiente y aceptada.</strong
              >
            </p>
            <p style="text-align: justify; font-size: 12px">
              Luego entonces previo al inicio de la atracción, el usuario,
              responsable, padre y/o tutor acepta que tanto en su persona como
              en sus dependientes y/o menores a su cargo, están físicamente
              aptos para el desarrollo de la actividad, que no presentan alguna
              limitación física y medica visible, que no se encuentran bajo la
              influencia de enervantes, drogas y alcohol y que se reconoce estar
              lo suficientemente calificado, entrenado y capaza de participar en
              esta actividades por lo tanto, el usuario, responsable, padre y/o
              tutor asume la completa responsabilidad por sí mismo y de los
              menores a su cargo, responsabilizándose de los daños corporales,
              accidentes, enfermedades, muerte, perdida de propiedad personal y
              los gastos que se actualicen como consecuencia de cualquier
              accidente que pudiera ocurrir en el transcurso del desempeño de la
              atracción., por ello el usuario, responsable, padre y/o tutor,
              <strong
                ><span style="text-decoration: underline"
                  >una vez estando enterado sobre los riesgos y
                  responsabilidades, externa su elección de participar en la
                  atracción.</span
                ></strong
              >
            </p>
          </div>
        </div>
        <div ref="pdf2" class="col-md-10 col-lg-8 col-xl-8 mx-auto">
          <div>
            <h6 style="font-weight: bold">
              IV.- Autorización de primeros auxilios.
            </h6>
            <p style="text-align: justify; font-size: 12px">
              El usuario, responsable, padre y/o tutor, autoriza por medio de la
              presente a Grupo Inmobiliario Cyka FUNKIDUUH (por medio de su
              personal), para la aplicación y/o prestación tanto en su persona
              como en los menores a su cargo, de primeros auxilios, que se
              consideren necesarios en el caso de alguna lesión durante su
              participación en la atracción., el usuario, responsable, padre y/o
              tutor manifiesta estar de acuerdo en pagar todos los costos de
              rescate y/o servicios médicos en que se pueda incurrir.
            </p>
          </div>
          <div>
            <h6 style="font-weight: bold">
              V.- Exoneración de responsabilidades a Grupo Inmobiliario Cyka
              FUNKIDUUH:
            </h6>
            <p style="text-align: justify; font-size: 12px">
              En consideración a los servicios o bienes prestados el usuario,
              responsable, padre y/o tutor, así como los menores de los que soy
              padre, tutor legal, líder del grupo o de otra manera responsable,
              representante personal o asignado temporal de guarda y custodia,
              estoy de acuerdo que Grupo Inmobiliario Cyka FUNKIDUUH, sus
              directivos, funcionarios, empleados y voluntarios, no tendrán
              responsabilidad de cualquier naturaleza por cualquier daño o
              lesión que sufra mi persona, hijo/os y otras personas o
              propiedades, como consecuencia del desempeño de la presente
              atracción.
            </p>
          </div>
          <section>
            <div class="row">
              <div class="col" style="margin: 5px; padding: 6px">
                <h6 style="text-align: justify; font-weight: bold">
                  Atentamente
                </h6>
                <p class="text-start" style="text-align: justify">
                  Información del Tutor&nbsp;👩👨
                </p>
                <div class="table-responsive-md">
                  <table class="table">
                    <thead style="color: black">
                      <tr>
                        <th class="text-start">nombre 💬</th>
                        <th class="text-end">correo ✉️</th>
                        <th class="text-center">tel 📱</th>
                        <th class="text-center">tel (2) 📱</th>
                      </tr>
                    </thead>
                    <tbody style="color: black">
                      <tutor-datos :id="idTutor"></tutor-datos>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col" style=" margin: 5px; padding: 6px; " >
                <p class="text-start" style="text-align: justify">
                  Menores 🧒
                </p>
                <div class="table-responsive">
                  <table class="table">
                    <thead>
                      <tr>
                        <th class="text-start">nombre 💬</th>
                        <th class="text-end">nacimiento 🎂</th>
                        <th class="text-center">edad 📜</th>
                      </tr>
                    </thead>
                    <tbody>
                      <menor-datos :id="idTutor"></menor-datos>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="row">
              <div>
                <about-component></about-component>
                <p>___________________________<br>Firma del Tutor</p>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
    <button @click="download">Download PDF</button>
  </div>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import jsPDF from "jspdf";
import * as html2canvas from "html2canvas";
import AboutComponent from "../components/AboutComponent.vue";
import TutorDatos from "../components/TutorDatos.vue";
import MenorDatos from "../components/MenorDatos.vue";
export default {
  name: "AboutView",
  components: {
    AboutComponent,
    TutorDatos,
    MenorDatos,
  },
  mounted() {
    if (window.opener) {
      document.querySelector("#firma").src = window.opener.obtenerImagen();
    }
  },
  methods: {
    printDate: function () {
      return new Date().toLocaleDateString();
    },
    download() {
      const pdfRef1 = this.$refs.pdf1;
      const pdfRef2 = this.$refs.pdf2;
      const pdf = new jsPDF("p", "mm", "a4");
      html2canvas(pdfRef1, { scale: 1 }).then((canvas) => {
        const pdfImage1 = canvas.toDataURL('image/png');
        html2canvas(pdfRef2, { scale: 1 }).then(canvas => {
          const pdfImage2 = canvas.toDataURL('image/png');
          pdf.addImage(pdfImage1, 'JPEG', 4, 5);
          pdf.addPage();//aqui hago un salto de pagina, una imagen en cada pagina
          pdf.addImage(pdfImage2, 'JPEG', 4, 5);
          pdf.save('test.pdf');
        });
      });
    },
  },
  data() {
    return {
      fechaActual: "",
      idTutor: ""
    };
  },
  created() {
    this.fechaActual = this.printDate();
    this.idTutor = localStorage.getItem('idTutor');
  }
};
</script>
