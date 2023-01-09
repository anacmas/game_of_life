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
    <div>
      <button class="button-to-play start" @click="startCycle">Start</button>
      <button class="button-to-play stop" @click="stop">Stop</button>
      <button class="button-to-play clear" @click="resetGrid">Limpar</button>

      <div class="rules">
        <h1 class="rules-title">Regras</h1>
        <h2 class="second-title">Para um espaço preenchido:</h2>
        <p>Células com zero ou apenas um vizinho morrem, por solidão.</p>
        <p>
          Cada célula com quatro ou mais vizinhos morre, por superpopulação.
        </p>
        <p>Cada célula com dois ou três vizinhos sobrevive.</p>
        <h2 class="second-title">Para um espaço vazio ou não preenchido:</h2>
        <p>Cada célula com três vizinhos torna-se preenchida.</p>
      </div>

      <p class="about">
        Game Of Life de John Conway, por
        <span class="name"><u>Ana Carolina M</u></span>
      </p>
    </div>
  </div>
</template>

<script>
const clearGrid = [
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
];
const size = 14;

export default {
  name: "GameOfLife",
  data() {
    return {
      showModal: false,
      grid: clearGrid,
      started: null,
      running: false,
    };
  },
  methods: {
    handleClick(index, idx) {
      this.active = !this.active;
      this.grid[index].splice(idx, 1, !this.grid[index][idx]);
    },
    resetGrid() {
      this.stop();
      for (let i = 0; i < this.grid.length; i++) {
        for (let j = 0; j < this.grid[i].length; j++) {
          this.grid[i].splice(j, 1, false);
        }
      }
      return this.grid;
    },
    checkNeighbors(i, j) {
      let neighbors = 0;
      if (i != 0 && j != 0) {
        if (this.grid[i - 1][j - 1] == true) {
          neighbors += 1;
        }
      }

      if (i != 0) {
        if (this.grid[i - 1][j] == true) {
          neighbors += 1;
        }
      }

      if (j != 0) {
        if (this.grid[i][j - 1] == true) {
          neighbors += 1;
        }
      }

      if (i != size && j != size) {
        if (this.grid[i + 1][j + 1] == true) {
          neighbors += 1;
        }
      }

      if (i != size) {
        if (this.grid[i + 1][j] == true) {
          neighbors += 1;
        }
      }

      if (j != size) {
        if (this.grid[i][j + 1] == true) {
          neighbors += 1;
        }
      }

      if (i != 0 && j != size) {
        if (this.grid[i - 1][j + 1] == true) {
          neighbors += 1;
        }
      }

      if (i != size && j != 0) {
        if (this.grid[i + 1][j - 1] == true) {
          neighbors += 1;
        }
      }

      return neighbors;
    },
    mutateCells(i, j) {
      const isInactive = this.grid[i][j] == false;

      const neighbors = this.checkNeighbors(i, j);

      if (isInactive) {
        if (neighbors == 3) {
          return true;
        } else return false;
      }
      if (neighbors <= 1 || neighbors >= 4) {
        return false;
      }

      return true;
    },
    createNewCycle() {
      let gridCopy = JSON.parse(JSON.stringify(this.grid));
      for (let i = 0; i <= size; i++) {
        for (let j = 0; j <= size; j++) {
          gridCopy[i][j] = this.mutateCells(i, j);
        }
      }
      return gridCopy;
    },
    cycle() {
      const newGrid = this.createNewCycle();
      for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
          this.grid[i].splice(j, 1, newGrid[i][j]);
        }
      }
    },
    startCycle() {
      if (!this.running) {
        this.running = true;
        this.started = setInterval(this.cycle, 300);
      }
    },
    stop() {
      clearInterval(this.started);
      this.running = false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.board {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
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

td {
  cursor: pointer;
}

.button-to-play {
  width: 60px;
  height: 30px;
  margin-left: 10px;
  border: none;
  cursor: pointer;
  border-radius: 3px;
}

.button-to-play:hover {
  opacity: 60%;
  transition: 0.3s;
}

.start {
  background-color: rgb(206, 245, 245);
}

.stop {
  background-color: rgb(255, 215, 215);
}

.rules {
  color: #898989;
  margin-top: 35px;
}

.rules-title {
  font-size: 16px;
  color: #6e6e6e;
}

.second-title {
  font-size: 14px;
  margin-top: 20px;
}

.rules p {
  font-size: 13px;
}

.about {
  margin-top: 3rem;
  font-size: 13px;
}

.name {
  color: rgb(243, 33, 138);
  cursor: pointer;
}

.name:hover {
  color: rgb(188, 177, 219);
  transition: 0.3s;
}
</style>
