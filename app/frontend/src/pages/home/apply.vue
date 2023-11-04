<template>
  <div id="page">
    <div
      id="info-header"
      style="font-size: larger; padding: 10px; font-weight: bold"
    >
      已注册社团
    </div>
    <div v-for="item in items" :key="item.index">
      <div class="card">
        <img
          src="https://avatar-tuanzi.oss-cn-wuhan-lr.aliyuncs.com/%E5%83%8F%E7%B4%A0%E9%A3%8E%E6%A0%A1%E5%BE%BD%E5%B0%8F%E5%9B%A2%E5%AD%90.png"
          class="img"
        />
        <div class="title">{{ item.obname }}</div>
        <van-button class="footer" type="info" round @click="del(item.index)"
          >取消注册
        </van-button>
      </div>
    </div>
    <div v-if="!haveClub" class="tips">你还没有加入任何社团...</div>
  </div>
</template>
<script>
import { Toast, Dialog } from "vant";

import { delapply, getapply } from "../../request/api";
Toast.setDefaultOptions({ duration: 1000 });
export default {
  name: "home-apply",
  data() {
    return {
      haveClub: 1,
      items: [
        {
          obname: "...",
        },
      ],
    };
  },
  methods: {
    del(index) {
      Dialog.confirm({
        title: "是否确定取消注册",
        message: "请慎重选择",
      })
        .then(() => {
          delapply(index).then((res) => {
            Toast("取消成功");
            location.reload();
          });
        })
        .catch(() => {
          console.log("用户取消了修改,未进行任何操作");
        });
    },
  },
  mounted() {
    getapply().then((res) => {
      this.items = res.data.data;
      if (this.items.length == 0) this.haveClub = 0;
      console.log(this.haveClub);
      console.log(res.data.data);
    });
  },
};
</script>
<style scoped>
.card {
  display: flex;
  align-items: center;
  font-size: 20px;
  border: 1px solid #d7d7d7;
  border-radius: 10px;
  margin: 1rem 0.8rem 1rem 0.8rem;
  padding: 0.5rem;
  box-shadow: 3px 3px 5px #ebebeb;
  /* background: #f3f3f3; */
}
.img {
  height: 5rem;
}
.title {
  display: flex;
  align-items: center;
  justify-content: left;
  text-align: left;
  font-size: large;
  margin: 0.5rem;
  width: 60%;
}
.footer {
  position: relative;
  float: right;
  font-size: small;
  padding: 0.2rem;
  width: 6rem;
}
.tips {
  width: 100%;
  padding-top: 10vh;
  color: #aeaeae;
  display: flex;
  justify-content: center;
}
</style>
<style>
#info-header {
  background: #f1f6ff;
  height: 2.5rem;
  letter-spacing: 0.2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #d2d2d2;
  border-radius: 5px;
  color: #3f3f3f;
}
#page {
  height: 100vh;
  /* background: #ffffff; */
}
</style>