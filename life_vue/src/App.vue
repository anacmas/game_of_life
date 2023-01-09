<template>
  <div id="app">
    <h1 class="main-title">GAME OF LIFE</h1>
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
  margin-top: 60px;
}

.main-title {
  color: #b6b6b6;
}
</style>
