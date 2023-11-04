<template>
  <div>
    <router-view></router-view>
    <van-tabbar route v-if="this.$route.meta.showTab">
      <van-tabbar-item replace to="/index" icon="home-o">注册</van-tabbar-item>
      <van-tabbar-item replace to="/home" icon="friends-o"
        >个人信息</van-tabbar-item
      >
    </van-tabbar>
  </div>
</template>

<style>
@font-face {
  font-family: "lightRS";
  font-weight: 400;
  src: url("./assets/SourceHanSansCN-Light.otf");
  font-display: swap;
}

html,
body {
  font-family: "lightRS";
  width: 100%;
  height: 100%;
}
</style>
