<template>
  <div>
    <div id="signature-pad" class="signature-pad">
      <div class="signature-pad--body">
        <canvas
          style="width: 300px; height: 150px; border: 1px black solid"
          id="canvas"
        ></canvas>
      </div>
      <p style="text-align: center;color: rgb(227,185,255);font-weight: bold;">firma</p>
    </div>
    <br>
    <button id="btnGenerarCarta" class="btn btn-warning">Finalizar</button>
  </div>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import SignaturePad from '../assets/firma/signature_pad.js'
export default {
  mounted () {
    const wrapper = document.getElementById('signature-pad')
    const canvas = wrapper.querySelector('canvas')
    const signaturePad = new SignaturePad(canvas, {
      backgroundColor: 'rgb(255, 255, 255)'
    })

    function resizeCanvas () {
      const ratio = Math.max(window.devicePixelRatio || 1, 1)

      canvas.width = canvas.offsetWidth * ratio
      canvas.height = canvas.offsetHeight * ratio
      canvas.getContext('2d').scale(ratio, ratio)

      signaturePad.clear()
    }

    window.onresize = resizeCanvas
    resizeCanvas()

    const $canvas = document.getElementById("canvas"),
        $btnGenerarCarta = document.getElementById("btnGenerarCarta");

    window.obtenerImagen = () => {
        return $canvas.toDataURL();
    };

    $btnGenerarCarta.onclick = () => {
        window.open("about");
    };
  }
}
</script>
<style>
</style>
