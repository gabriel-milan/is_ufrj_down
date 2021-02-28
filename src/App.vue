<template>
  <div id="app">
    <img alt="Vue logo" width="200" src="./assets/logo.png" />
    <IsUfrjDown />
    <br />
    <MadeWithLove by="Gabriel Milan" link="https://github.com/gabriel-milan/" />
  </div>
</template>

<script>
import IsUfrjDown from "./components/IsUfrjDown.vue";
import MadeWithLove from "./components/MadeWithLove.vue";

export default {
  name: "App",
  components: {
    IsUfrjDown,
    MadeWithLove,
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
