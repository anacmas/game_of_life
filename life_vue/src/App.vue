<template>
  <div id="app">
    <h1>GAME OF LIFE</h1>
    <GameOfLife />
  </div>
</template>

<script>
import GameOfLife from "./components/GameOfLife.vue";

export default {
  name: "App",
  components: {
    GameOfLife,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #b6b6b6;
  margin-top: 100px;
}
</style>
