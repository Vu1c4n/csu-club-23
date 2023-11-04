<template>
  <div>
    <van-nav-bar title="Loading..." />
  </div>
</template>
<script>
import { wxlogin } from "../../request/api";

export default {
  name: "gameLoading",
  mounted() {
    history.pushState(null, null, document.URL);
    window.addEventListener("popstate", function () {
      history.pushState(null, null, document.URL);
    });

    if (process.env.NODE_ENV === "production") {
      const res = window.location.search
        .substring(1)
        .match(/(^|&|\?)code=([^&]*)(&|$)/);
      let code = "";
      if (res) {
        code = decodeURIComponent(res[2]);
      }
      if (!code) {
        window.location.href = `https://open.weixin.qq.com/connect/oauth2/authorize?appid=${"wx2fdfc27744ffa252"}
&redirect_uri=${encodeURIComponent("https://shetuan.54sher.com")}
&response_type=code
&scope=snsapi_userinfo
#wechat_redirect`;
      } else {
        wxlogin(code)
          .then((res) => {
            console.log(res.data);
            const { data } = res.data;
            localStorage.setItem("token", data.token);
            localStorage.setItem("picture", data.picture);
          })
          .finally(() => {
            this.$router.replace("/index");
          });
      }
     } 
     else {
      this.$router.replace("/index");
    }
  },
};
</script>

<style>
.van-nav-bar {
  text-align: center;
  background-color: #f3f3f4;
  height: 45px;
  line-height: 2.7rem;
}
</style>
