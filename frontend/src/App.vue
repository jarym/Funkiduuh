<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark"
    style="background: linear-gradient(86deg, #3155e0 5%, #5f0fc8 17%, rgb(123,25,188) 49%, var(--bs-pink) 100%); text-color=#ffffff;"
  >
    <div class="container">
      <a href="/">
        <img src="./assets/img/m.png" alt="" width="130" height="50" />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a href="/registrarVisita" class="nav-link active" aria-current="page">Registrar Visita</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <router-view></router-view>
  <footer class="footer-dark">
    <div class="container">
      <div class="row">
        <div class="col-sm-6 col-md-3 item">
          <h3>Services</h3>
          <ul>
            <li><a href="#">Web design</a></li>
            <li><a href="#">Development</a></li>
            <li><a href="#">Hosting</a></li>
          </ul>
        </div>
        <div class="col-sm-6 col-md-3 item">
          <h3>About</h3>
          <ul>
            <li><a href="#">Company</a></li>
            <li><a href="#">Team</a></li>
            <li><a href="#">Careers</a></li>
          </ul>
        </div>
        <div class="col-md-6 item text">
          <h3>Company Name</h3>
          <p>
            Praesent sed lobortis mi. Suspendisse vel placerat ligula. Vivamus
            ac sem lacus. Ut vehicula rhoncus elementum. Etiam quis tristique
            lectus. Aliquam in arcu eget velit pulvinar dictum vel in justo.
          </p>
        </div>
        <div class="col item social">
          <a href="#"><i class="icon ion-social-facebook"></i></a
          ><a href="#"><i class="icon ion-social-twitter"></i></a
          ><a href="#"><i class="icon ion-social-snapchat"></i></a
          ><a href="#"><i class="icon ion-social-instagram"></i></a>
        </div>
      </div>
      <p class="copyright">Company Name © 2022</p>
    </div>
  </footer>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
