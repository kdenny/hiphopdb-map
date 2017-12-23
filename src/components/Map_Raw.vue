<template>
  <div>
    <!--<div style="height: 10%; overflow: hidden;">-->
      <!--<h3>Simple map with custom component</h3>-->
      <!--Marker and Popup added using custom component MarkerPopup-->
    <!--</div>-->
    <div v-if="show" id="mapid" style="height: 900px;"></div>
    <!--<v-map style="height: 90%" :zoom="zoom" :center="center">-->
      <!--<v-tilelayer :url="url" :attribution="attribution"></v-tilelayer>-->
      <!--<v-geojson-layer v-if="show" :geojson="geojson" :options="options"></v-geojson-layer>-->
      <!--<v-marker-popup :position="marker" :text="text" :title="title"></v-marker-popup>-->
      <!--<v-icondefault :image-path="path"></v-icondefault>-->
    <!--</v-map>-->
  </div>
</template>

<script>
import Vue2Leaflet from 'vue2-leaflet';
import MarkerPopup from './leaflet/MarkerPopup';
import cities from '../assets/geojson/cities';
import charts from '../assets/geojson/chartData';
let year = 1998;
var timerObj;

export default {
  name: 'HipHopMap',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-geojson-layer' :Vue2Leaflet.GeoJSON,
    'v-marker-popup': MarkerPopup,
    'v-icondefault': Vue2Leaflet.IconDefault
  },
  data () {
    return {
      zoom:5,
      year: '1989',
      center: L.latLng(37.0819, -89.3647),
      url:'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_nolabels/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
      marker: L.latLng(47.413220, -1.219482),
      show: false,
      options: {pointToLayer: function (feature, latlng) {
      console.log(year)
      console.log(charts.hiphopCharts[year])
      if (feature.properties.City_Type == 1) {
        let r;
        if (charts.hiphopCharts[year][feature.properties.City]) {
          console.log(charts.hiphopCharts[year][feature.properties.City])
          r = charts.hiphopCharts[year][feature.properties.City]['score'] / 110;
        }
        else {
          r = 10;
        }
        console.log()
        return L.circleMarker(latlng, {
          radius: r,
          fill: 'green'
        });

      }}},
      geojson: cities.hipHopCities,
      path: '/images/',
      text: 'my marker popup text',
      title: 'My marker popup title'
    }
  },
  mounted () {
    console.log(this)
    console.log(this.$el.children[0])
    this.show = true;
    this.map = L.map(this.$el).setView(this.center, 5);
    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_nolabels/{z}/{x}/{y}.png', {
        maxZoom: 18,
        id: 'carto-dark'
    }).addTo(this.map);

    this.glayer = L.geoJson(this.geojson, {
      pointToLayer: function (feature, latlng) {
      console.log(year)
      console.log(charts.hiphopCharts[year])
      if (feature.properties.City_Type == 1) {
        let r;
        if (charts.hiphopCharts[year][feature.properties.City]) {
          console.log(charts.hiphopCharts[year][feature.properties.City])
          r = charts.hiphopCharts[year][feature.properties.City]['score'] / 110;
        }
        else {
          r = 1;
        }
        console.log()
        return L.circleMarker(latlng, {
          radius: r,
          fill: 'green'
        });

      }}
  }).addTo(this.map);

    this.startTimer();

  },
  watch: {
    year: function() {
      this.show = false;
      var me = this;
      console.log(year)
      this.glayer = L.geoJson(this.geojson, {
        pointToLayer: function (feature, latlng) {
        console.log(year)
        console.log(charts.hiphopCharts[year])
        if (feature.properties.City_Type == 1) {
          let r;
          if (charts.hiphopCharts[year][feature.properties.City]) {
            console.log(charts.hiphopCharts[year][feature.properties.City])
            r = charts.hiphopCharts[year][feature.properties.City]['score'] / 110;
          }
          else {
            r = 1;
          }
          console.log()
          return L.circleMarker(latlng, {
            radius: r,
            fill: 'green'
          });

        }}
    }).addTo(this.map);
      this.show = true;
      return year;
    }
  },
  methods: {
    icon () {
      return L.icon({
        iconUrl: '/images/',
        iconSize: [40, 40],
        iconAnchor: [20, 20]
      })
    },
    startTimer(){
        timerObj = window.setInterval(this.timerTick, 1000);
    },

    stopTimer(){
        window.clearInterval(timerObj);
        timerObj = null;
    },

    timerTick(){
        console.log("Tick")
        if (parseInt(year) < 2017) {
            let y = parseInt(year) + 1;
            this.year = y.toString()
            this.map.removeLayer(this.glayer);
            this.options = {};
            year = this.year;
//            this.show = false;

        } else {
            this.stopTimer();
            // Some broadcast stuff to disable answering
        }
    }
  }
}
</script>
<style scoped>
  .leaflet-container { background: black };
</style>
