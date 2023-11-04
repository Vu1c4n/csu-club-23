<template>
  <div id="all">
    <div id="header" class="indexheader">
      <div class="navbar"></div>
      <van-search
        v-model="value"
        shape="round"
        background="#fcfcfc"
        placeholder="请输入搜索关键词"
        @search="onSearch"
      />
    </div>
    <van-row class="background-row row" id="top">
      <van-col span="6">
        <div id="left">
          <van-sidebar
            v-model="activeKey"
            @change="onChange"
            style="height: 100%; background: #f9fafb;overflow: hidden;"
          >
            <van-sidebar-item title="全部" />
            <van-sidebar-item title="学术类" />
            <van-sidebar-item title="文艺类" />
            <van-sidebar-item title="科技类" />
            <van-sidebar-item title="体育类" />
            <van-sidebar-item title="公益类" />
            <van-sidebar-item title="实践类" />
            <img
              src="https://22sher.oss-cn-guangzhou.aliyuncs.com/shetuan/csu.gif"
              style="opacity: 30%; margin-top: 30px; height: 20%"
            />
          </van-sidebar>
        </div>
      </van-col>
      <van-col span="17">
        <div id="top"></div>
        <div id="right">
          <CardShow
            v-for="(item, index) in items"
            :msg="item"
            :key="index"
            :id="index"
            :name="item"
          >
          </CardShow>
        </div>
      </van-col>
      <van-sticky style="height: 100vh">
        <a href="#top">
          <svg
            t="1698237670728"
            class="icon backtop"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="5033"
            width="3rem"
            height="3rem"
            style="top: 70vh"
          >
            <path
              d="M512 0C230.4 0 0 230.4 0 512s230.4 512 512 512 512-230.4 512-512S793.6 0 512 0zM697.6 582.4 627.2 582.4c-12.8 0-19.2 6.4-19.2 19.2l0 108.8c0 6.4-6.4 12.8-12.8 12.8L428.8 723.2c-6.4 0-12.8-6.4-12.8-12.8L416 595.2c0-6.4-6.4-19.2-19.2-19.2L326.4 576C320 582.4 320 576 320 576l179.2-172.8c6.4-6.4 12.8-6.4 19.2 0L704 576C704 576 704 582.4 697.6 582.4zM704 364.8 320 364.8c-19.2 0-32-12.8-32-32S300.8 300.8 320 300.8l384 0c19.2 0 32 12.8 32 32S723.2 364.8 704 364.8z"
              fill="#6495ed"
              p-id="5034"
            ></path>
          </svg>
        </a>
      </van-sticky>
    </van-row>
    <!-- 返回顶部 -->
  </div>
</template>
<script>
import { getallclub, getmsg } from "../../request/api";
import CardShow from "../../components/CardShow.vue";
import { Dialog } from "vant";
import { BackTop } from "vant";

export default {
  name: "main-index",
  components: {
    CardShow,
  },
  data() {
    return {
      value: "",
      activeKey: 0,
      items: {},
      itemsplus: {},
      token: localStorage.getItem("token"),
      resData: localStorage.getItem("resData"),
      person_info:{
        name:"...",
        sex:"..."
      }
    };
  },
  methods: {
    onSearch() {
      const all = Object.values(this.itemsplus);
      function findKey(obj, value, compare = (a, b) => a === b) {
        return Object.keys(obj).find((k) => compare(obj[k], value));
      }
      const that = this; // console.log(findKey(this.itemsplus, this.value))
      const prefect = all.filter(function (a) {
        return a.search(that.value) !== -1;
      });
      console.log(prefect);
      let i = 0;
      const x = {};
      while (prefect[i] !== undefined) {
        x[findKey(this.itemsplus, prefect[i])] = prefect[i];
        i += 1;
      }
      this.items = x;
    },
    onCancel() {
      this.value = "";
    },
    onChange() {
      if (this.activeKey === 0) {
        const x = {};
        for (let i = 0; i <= 115; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 1) {
        const x = {};
        for (let i = 0; i <= 25; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 2) {
        const x = {};
        for (let i = 26; i <= 49; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 3) {
        const x = {};
        for (let i = 50; i <= 60; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 4) {
        const x = {};
        for (let i = 61; i <= 92; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 5) {
        const x = {};
        for (let i = 93; i <= 102; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
      if (this.activeKey === 6) {
        const x = {};
        for (let i = 103; i <= 117; i++) {
          x[i] = this.itemsplus[i];
        }
        this.items = x;
      }
    },
  },
  mounted() {
    getallclub().then((res) => {
      this.items = res.data;
      this.itemsplus = res.data;
    });
    if (!window.localStorage) {
      alert("浏览器不支持localstorage");
      return false;
    } else {
      getmsg().then((res) => {
        this.person_info = {
          name: res.data.data.name,
          sex: res.data.data.sex,
          nation: res.data.data.nation,
          birth: res.data.data.birth,
          political: res.data.data.political,
          stu_id: res.data.data.stu_id,
          stu_type: res.data.data.stu_type,
          academy: res.data.data.academy,
          specialty: res.data.data.specialty,
          grade: res.data.data.grade,
          stu_class: res.data.data.stu_class,
          from_location: res.data.data.from_location,
          phone: res.data.data.phone,
          qq: res.data.data.qq,
        };
        localStorage.setItem("person_info", JSON.stringify(this.person_info));
        console.log(this.person_info)
        if (res.data.data.phone === "") {
          Dialog.alert({
            title: "信息尚未填写",
            message: "请点击确认按钮前往填写信息",
          }).then(() => {
            this.$router.replace("/login");
          });
        } else {
          console.log("是个老油条啦");
        }
      });
    }
  },
};
</script>
<style scoped>
html,
body {
  width: 100%;
  height: 100%;
  color: #c0c0c0;
}
.van-sidebar-item {
  padding-bottom: 10px;
  padding-top: 10px;
  height: 55px;
}
</style>

<style lang="less">
@navheight: 0;
.navbar {
  height: @navheight;
  width: 100%;
  background: #6495ed;
}
.row {
  padding-top: @navheight+54px;
  padding-bottom: 50px;
}
</style>

<style>
.indexheader {
  position: fixed;
  z-index: 3;
  width: 100%;
}
#left {
  height: 100%;
  position: fixed;
  z-index: 0;

}
.van-sticky {
  width: 100%;
  top: 80vh;
}
.background-row {
  background: #f5f5f5;
}
.backtop {
  padding-left: 80%;
}
</style>