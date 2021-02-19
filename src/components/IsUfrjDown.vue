<template>
  <div class="hello">
    <h1>Is UFRJ down?</h1>
    <h2>Real-time verification for UFRJ servers availability</h2>
    <p>
      If you'd like to add servers to the list please<br />
      submit an issue at
      <a
        href="https://github.com/gabriel-milan/is_ufrj_down"
        target="_blank"
        rel="noopener"
        >the official repository</a
      >.
    </p>
    <h3>Servers</h3>
    <ul id="server-list">
      <li v-for="(obj, host) in servers" :key="host">
        <md-icon
          :style="{
            color:
              obj.status === 'on'
                ? 'green'
                : obj.status === 'off'
                ? 'red'
                : 'gray',
          }"
          >fiber_manual_record</md-icon
        >
        {{ host }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "IsUfrjDown",
  data() {
    return {
      updateDelayMs: 5000,
      checkTimeoutMs: 1500,
      servers: {
        "cos.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "laspi.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "lps.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "poli.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "nce.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "im.ufrj.br": {
          status: "unk",
          updated: false,
        },
        "if.ufrj.br": {
          status: "unk",
          updated: false,
        },
      },
    };
  },
  mounted() {
    for (let host in this.servers) {
      setTimeout(() => {
        this.checkServer(host, this.checkTimeoutMs);
      }, 0);
      setInterval(() => {
        this.checkServer(host, this.checkTimeoutMs);
      }, this.updateDelayMs);
    }
    this.keepLooping = false;
  },
  methods: {
    // sleep(ms) {
    //   return new Promise((resolve) => setTimeout(resolve, ms));
    // },
    handleErrors(response) {
      if (
        (!response.ok || response.status != 200) &&
        response.type != "opaque"
      ) {
        throw Error(response.statusText);
      }
      return response;
    },
    checkServer(hostname, timeout) {
      const controller = new AbortController();
      const signal = controller.signal;
      const options = { mode: "no-cors", signal };
      this.servers[hostname].updated = false;
      let url = `http://${hostname}`;
      fetch(url, options)
        .then((resp) => {
          setTimeout(() => {
            controller.abort();
            if (!this.servers[hostname].updated) {
              this.servers[hostname].status = "off";
              this.servers[hostname].updated = true;
            }
          }, timeout);
          this.handleErrors(resp);
        })
        .then(() => {
          this.servers[hostname].status = "on";
          this.servers[hostname].updated = true;
        })
        .catch(() => {
          this.servers[hostname].status = "off";
          this.servers[hostname].updated = true;
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
