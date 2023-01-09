<template>
  <div>
    <div class="board">
      <table>
        <tr v-for="(line, index) in grid" :key="index">
          <td
            v-for="(cell, idx) in line"
            :key="idx"
            @click="handleClick(index, idx)"
            :class="cell == 1 ? 'active' : 'non-active'"
          ></td>
        </tr>
      </table>
    </div>
    <div class="buttons">
      <button class="start">Start</button>
      <button class="stop">Stop</button>
      <button class="clear">Clear</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameOfLife",
  props: {
    msg: String,
  },
  data() {
    return {
      grid: [
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
      ],
      update: 0,
    };
  },
  methods: {
    handleClick(index, idx) {
      this.active = !this.active;
      this.grid[index].splice(idx, 1, !this.grid[index][idx]);
      console.log(this.grid);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.alive {
  background-color: rgb(100, 139, 174);
}

td {
  width: 20px;
  height: 20px;
}

.active {
  background-color: rgb(237, 108, 172);
}

.non-active {
  background-color: rgb(188, 177, 219);
}

button {
  width: 60px;
  height: 30px;
  margin-left: 10px;
  border: none;
  cursor: pointer;
  border-radius: 3px;
}

button:hover {
  opacity: 60%;
  transition: 0.3s;
}

.start {
  background-color: rgb(206, 245, 245);
}

.stop {
  background-color: rgb(255, 215, 215);
}
</style>
