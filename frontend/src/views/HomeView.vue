<template>
  <div class="home">
    <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel" style="margin-top:20px;margin-bottom:20px;">
      <div class="carousel-inner" style="width=200px;height:600px">
        <div class="carousel-item active" data-bs-interval="3000" >
          <img src="./assets/carrusel/1.jpeg" class="" alt="..." style="border-radius:50px;">
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img src="./assets/carrusel/2.jpeg" class="" alt="..." style="border-radius:50px">
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img src="./assets/carrusel/3.jpeg" class="" alt="..." style="border-radius:50px">
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img src="./assets/carrusel/4.jpeg" class="" alt="..." style="border-radius:50px">
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img src="./assets/carrusel/5.jpeg" class="" alt="..." style="border-radius:50px">
        </div>
      </div>
    </div>
    <a href="/registrarVisita" class="rainbow-button" alt="Registrar Visita"></a>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>
<style>
.home {
  margin:0;
  background-image: url("./assets/img/fondo-violeta.jpg");
  background-size: 100% 100%;
  min-height:400px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-family:Helvetica,Sans-serif;
}
a {
  text-decoration:none;
  color:#FFF;
}
a:hover {
  color: rgb(191, 214, 57);
  cursor: pointer;
}
.rainbow-button {
  width:calc(35vw + 6px);
  height:calc(8vw + 6px);
  background-image: linear-gradient(90deg, #00C0FF 0%, #FFCF00 49%, #FC4F4F 80%, #00C0FF 100%);
  border-radius:5px;
  display:flex;
  align-items:center;
  justify-content:center;
  text-transform:uppercase;
  font-size:3vw;
  font-weight:bold;
  position: absolute;
}
.rainbow-button:after{
  content: attr(alt);
  width: 34.5vw;
  height: 7.5vw;
  background-color: #191919;
  display: flex;
  align-items: center;
  justify-content: center;
}
.rainbow-button:hover{
  animation: slidebg 1.5s linear infinite;
}
@keyframes slidebg {
  to {
    background-position: 35vw;
  }

}
</style>
