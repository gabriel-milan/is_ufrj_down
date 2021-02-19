<template>
  <div id="app">
    <img alt="Vue logo" width="200" src="./assets/logo.png" />
    <IsUfrjDown />
  </div>
</template>

<script>
import IsUfrjDown from "./components/IsUfrjDown.vue";

export default {
  name: "App",
  components: {
    IsUfrjDown,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
