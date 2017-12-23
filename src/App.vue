<template>
  <div>
    <b-navbar toggleable="md" type="dark" style="background-color: black;">

      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand href="#">HipHop DB</b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item to="map">Map</b-nav-item>
          <b-nav-item to="articles">Articles</b-nav-item>
          <b-nav-item href="#" disabled>Feature Network</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown text="Eras" >
            <b-dropdown-item href="#">2013 - 2017</b-dropdown-item>
            <b-dropdown-item href="#">2008 - 2012</b-dropdown-item>
            <b-dropdown-item href="#">2002 - 2007</b-dropdown-item>
            <b-dropdown-item href="#">1997 - 2001</b-dropdown-item>
            <b-dropdown-item href="#">1992 - 1996</b-dropdown-item>
            <b-dropdown-item href="#">1987 - 1991</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown text="Cities" style="margin-left: 3vw">
            <b-dropdown-item href="#">New York</b-dropdown-item>
            <b-dropdown-item href="#">Los Angeles</b-dropdown-item>
            <b-dropdown-item href="#">Atlanta</b-dropdown-item>
            <b-dropdown-item href="#">Chicago</b-dropdown-item>
            <b-dropdown-item href="#">Houston</b-dropdown-item>
            <b-dropdown-item href="#">Bay Area</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-button size="sm" class="my-2 my-sm-0" type="submit" style="margin-left: 5vw">Subscribe</b-button>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>

    <side_panel v-if="displaySide"></side_panel>


    <router-view id="full_div"/>
    <!--<component id="full_div" :is="currentView"></component>-->
  </div>
</template>

<script>

  import SidePanel from './components/leaflet/SidePanel.vue';

export default {
  name: 'app',
  components: {
    side_panel: SidePanel
  },
  data () {
    return {
      currentView: 'simple',
      displaySide: false
    }
  },
  methods: {
    showAlert() {
      alert('this is ' + 'sparta');
    }

  }
}
</script>

<style>
.leaflet-fake-icon-image-2x {
  background-image: url(../node_modules/leaflet/dist/images/marker-icon-2x.png);
}
.leaflet-fake-icon-shadow {
  background-image: url(../node_modules/leaflet/dist/images/marker-shadow.png);
}
@import "../node_modules/leaflet/dist/leaflet.css";
@import "../node_modules/bootstrap/dist/css/bootstrap.css";
@import '../node_modules/bootstrap-vue/dist/bootstrap-vue.css';

body {
  margin: 0px;
  font-family: Helvetica, Verdana, sans-serif;
}

#side {
  float:left;
  width:350px;
}

#full_div {
  position: absolute;
  overflow-x: auto;
  top: 56px;
  right: 0;
  left: 350px;
  bottom: 0;
  padding-left: 8px;
  border-left: 1px solid #ccc;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}


li {
  font: 200 15px/1.5 Helvetica, Verdana, sans-serif;
  border-bottom: 1px solid #ccc;
}

li:last-child {
  border: none;
}

li a {
  font-size: 15px;
  padding-left: 8px;
  text-decoration: none;
  color: #000;
  display: block;

  -webkit-transition: font-size 0.3s ease, background-color 0.3s ease;
  -moz-transition: font-size 0.3s ease, background-color 0.3s ease;
  -o-transition: font-size 0.3s ease, background-color 0.3s ease;
  -ms-transition: font-size 0.3s ease, background-color 0.3s ease;
  transition: font-size 0.3s ease, background-color 0.3s ease;
}

li a:hover {
  font-size: 20px;
  background: #f6f6f6;
}
</style>
