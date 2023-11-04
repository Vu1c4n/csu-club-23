<template>
  <div id="app">
    <div id="header">
      <van-image
        round
        fit="cover"
        width="7rem"
        height="7rem"
        :src="picture"
        style="box-shadow: 0px 1px 3px #d5d5d5"
      />
    </div>
    <div id="content">
      <van-cell-group inset>
        <van-cell
          is-link
          title="个人信息"
          to="person"
          style="font-size: large; padding-top: 1rem; padding-bottom: 1.7rem"
        />
        <van-cell
          is-link
          title="已注册社团信息"
          to="apply"
          style="font-size: large; padding-bottom: 1.7rem"
        />
      </van-cell-group>
      <div class="imgdiv">
        <img src="../../assets/QQ图片20231026215703.png" class="img-tuanzi" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "home-main",
  data() {
    return { picture: "" };
  },
  mounted() {
    this.picture = localStorage.getItem("picture");
  },
};
</script>
<style scoped>
#app {
  padding-top: 20%;
  background: #daeeff;
  height: 100vh;
  width: 100%;
  position: fixed;
}
#header {
  display: flex;
  justify-content: center;
}
#content {
  /* box-shadow:0px -2px 3px #f5f7ff; */
  margin-top: 10%;
  border-radius: 30px;
  padding-top: 10%;
  padding-bottom: 10%;
  background: #fff;
  height: 100%;
  width: 100%;
  position: fixed;
  overflow: hidden;
}
.imgdiv {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 15vh;
  margin-top: 30vh;
}
.img-tuanzi {
  opacity: 30%;
  height: 100%;
}
.van-cell {
  border: 0px !important;
}
</style>
