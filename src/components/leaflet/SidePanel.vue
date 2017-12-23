<template>
  <ul id="side">
    <h1>Queens</h1>
    <li>
      <b-btn variant="info" class="m-1">
        Show alert
      </b-btn>
    </li>
    <li>
      <a href="/" @click="currentView='simple'">Simple map</a>
    </li>
    <li>
      <router-link to="map">Custom Component</router-link>
    </li>
  </ul>
</template>

<script>

export default {
  name: 'SidePanel',
  props: ['text', 'position', 'title'],
}
</script>
