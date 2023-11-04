<template>
  <div>
    <div id="header">
      <van-image
        round
        width="10rem"
        height="10rem"
        src="https://22sher.oss-cn-guangzhou.aliyuncs.com/shetuan/csu.gif"
      />
    </div>
    <div id="name">
      <h1>{{ name }}</h1>
    </div>
    <div id="content">
      <div style="margin: 16px; display: flex; justify-content: center">
        <van-button
          round
          block
          type="info"
          native-type="submit"
          style="font-size: larger; width: 75%"
          @click="onSubmit"
          >报名</van-button
        >
      </div>
    </div>
  </div>
</template>
<script>
import { applysendmsg } from "../../request/api";
import { Toast, Dialog } from "vant";
export default {
  name: "main-clubpage",
  data() {
    return {
      id: "",
      name: "",
      position: "",
      join_time: "",
      showPicker: false,
      ub_pattern: /^最多同时报名(\d+)个社团/,
    };
  },
  methods: {
    onSubmit() {
      applysendmsg(this.id, this.name).then((res) => {
        if (res.data.status) {
          //success
          Dialog.alert({
            title: "注册成功",
            message: "成功完成注册",
          }).then(() => {
            this.$router.replace("/index");
          });
        } else {
          if (res.data.msg === "已经报名此社团") {
            //already
            Dialog.alert({
              title: "已经报名此社团",
              message: "请不要重复注册",
            }).then(() => {
              this.$router.replace("/index");
            });
          } else if (this.ub_pattern.test(res.data.msg)) {
            // 最多同时报名n个社团
            Dialog.alert({
              title: res.data.msg,
              message: "请不要超出上限",
            }).then(() => {
              this.$router.replace("/index");
            });
          } else {
            console.log(res.data.msg);
            Dialog.alert({
              title:"error",
              message: res.data.msg,
            });
          }
        }
      });
    },
  },
  mounted() {
    this.id = this.$route.query.id;
    this.name = this.$route.query.name;
  },
};
</script>
<style scoped>
#header {
  display: flex;
  justify-content: center;
  padding-top: 10vh;
}
#name {
  text-align: center;
}
</style>
