<template>
  <div>
    <b-navbar toggleable="md" type="dark" variant="info">

      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand href="#">NavBar</b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>

    <ul id="side">
      <li>
        <b-btn @click="showAlert" variant="info" class="m-1">
          Show alert
        </b-btn>
      </li>
      <li>
        <a href="/" @click="currentView='simple'">Simple map</a>
      </li>
      <li>
        <router-link to="custom-component">Custom Component</router-link>
      </li>
      <!--<li>-->
        <!--<a href="#" @click="currentView='multi-map'">Two maps</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='custom-path'">Custom path</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='custom-url-params'">Custom Url Params</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='set-bounds'">Set bounds</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='example'">Some examples</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='geometry-test'">Geometry</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='popup-on-geometry-test'">Popup on Geometry</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='world-copy-jump'">Jump on World Copy</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='geo-json'">GeoJSON</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='geo-json2'">GeoJSON 2</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='wms-layers'">WMS Tile Layers</a>-->
      <!--</li>-->
      <!--<li>-->
        <!--<a href="#" @click="currentView='crs'">CRS and Image Overlay</a>-->
      <!--</li>-->
    </ul>
    <router-view id="full_div"/>
    <!--<component id="full_div" :is="currentView"></component>-->
  </div>
</template>

<script>
import CRSAndImageOverlay from './components/CRSAndImageOverlay';
import CustomPath from './components/CustomPath';
import CustomUrlParams from './components/CustomUrlParams';
import Example from './components/Example';
import GeoJSON from './components/GeoJSON';
import GeoJSON2 from './components/GeoJSON2';
import GeometryTest from './components/GeometryTest';
import MarkerPopupExample from './components/MarkerPopupExample';
import MultiMap from './components/MultiMap';
import PopupOnGeometryTest from './components/PopupOnGeometryTest';
import SetBounds from './components/SetBounds';
import Simple from './components/Simple';
import WMSLayers from './components/WMSLayers';
import WorldCopyJump from './components/WorldCopyJump';

export default {
  name: 'app',
  components: {
    CustomPath,
    CustomUrlParams,
    Example,
    GeometryTest,
    MarkerPopupExample,
    MultiMap,
    PopupOnGeometryTest,
    SetBounds,
    Simple,
    WorldCopyJump,
    'geo-json': GeoJSON,
    'geo-json2': GeoJSON2,
    'wms-layers': WMSLayers,
    'crs': CRSAndImageOverlay,
  },
  data () {
    return {
      currentView: 'simple'
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
  width:208px;
}

#full_div {
  position: absolute;
  overflow-x: auto;
  top: 56px;
  right: 0;
  left: 208px;
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
