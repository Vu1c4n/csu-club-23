<template>
  <div
    class="CardShow"
    v-on:click="send"
  >
    <van-row>
      <van-col
        span="7"
        class="img"
      >
        <van-image
          round
          src="https://avatar-tuanzi.oss-cn-wuhan-lr.aliyuncs.com/%E5%83%8F%E7%B4%A0%E9%A3%8E%E6%A0%A1%E5%BE%BD%E5%B0%8F%E5%9B%A2%E5%AD%90.png"
          width="2.5rem"
          height="2.5rem"
        />
      </van-col>
      <van-col
        span="14"
        class="font"
      >
        <div>{{msg}}</div>
      </van-col>
    </van-row>
  </div>
</template>

<script>

export default {
  data () {
    return {
      page: ['page1']
    }
  },
  name: 'CardShow',
  methods: {
    send () {
      this.$router.push({ path: 'ClubPage', query: { id: this.id, name: this.name } })
    }
  },
  props: {
    msg: String,
    id: String,
    name: String
  }
}
</script>
<style scoped>
.img {
  display: flex;
  justify-content: center;
  align-items: center;
}
.font {
  display: flex;
  justify-content: left;
  align-items: center;
  color:#2c2c2c;
  font-family:lightRS;
  font-weight: bold;
  font-size: large;
  /* font-family: 'RegularDD'; */
}
.van-row {
  width: 100%;
  height: 100%;
}
.van-col {
  height: 100%;
}
.CardShow{
    height: 70px;
    margin-top: 12px;
    color: #fff;
    background: #fff;
    border-radius: 10px;
    margin-bottom: 12px;
    border:1px solid #dedddd;
    
    /* box-shadow: 3px 3px 3px 1px rgb(222, 222, 222); */
}
</style>