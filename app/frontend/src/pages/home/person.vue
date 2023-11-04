<template>
  <div>
    <!-- 这个页面是展示个人信息 -->
    <!-- 展示的方式就是用vant组件里的可读这个方式 -->
    <van-nav-bar>
      <template #title><div class="nav-title">个人信息</div></template>
      <template #left>
        <div style="padding-top: 1.5vh" @click="backToHome">
          <svg
            t="1698672459633"
            class="icon"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="3996"
            width="20"
            height="20"
          >
            <path
              d="M710.153924 8.980397L266.007127 460.692524a81.118646 81.118646 0 0 0 0.861532 114.476097l446.192936 441.050666a26.922883 26.922883 0 0 0 37.853573-38.284339L304.722232 536.884282a27.27288 27.27288 0 0 1-0.323074-38.445877L748.545955 46.726278A26.922883 26.922883 0 1 0 710.180847 9.00732z"
              fill="#222222"
              p-id="3997"
            ></path>
          </svg>
        </div>
      </template>
    </van-nav-bar>
    <van-cell-group>
      <van-field label="姓名" :value="person_info.name" readonly />
      <van-field label="性别" :value="person_info.sex" readonly />
      <van-field label="民族" :value="person_info.nation" readonly />
      <van-field label="出生日期" :value="person_info.birth" readonly />
      <van-field label="政治面貌" :value="person_info.political" readonly />
      <van-field label="学号" :value="person_info.stu_id" readonly />
      <van-field label="培养层次" :value="person_info.stu_type" readonly />
      <van-field label="学院" :value="person_info.academy" readonly />
      <van-field label="专业" :value="person_info.specialty" readonly />
      <van-field label="年级" :value="person_info.grade" readonly />
      <van-field label="专业班级" :value="person_info.stu_class" readonly />
      <van-field label="生源地" :value="person_info.from_location" readonly />
      <van-field label="电话" :value="person_info.phone" readonly />
      <van-field label="QQ" :value="person_info.qq" readonly />
    </van-cell-group>
    <div id="button-o">
      <van-button
        round
        type="info"
        @click="Onchange"
        size="large"
        class="button-i"
      >
        修改
      </van-button>
    </div>
  </div>
</template>
<script>
import { Dialog } from "vant";
import { getmsg } from "../../request/api";
export default {
  name: "home-person",
  data() {
    return {
      person_info: {
        name: "...",
        sex: "...",
      },
    };
  },
  methods: {
    // 一个函数跳转的login,从login去进行修改信息操作
    Onchange() {
      Dialog.confirm({
        title: "是否确定修改个人信息",
        message: "请慎重修改",
      })
        .then(() => {
          this.$router.push({ path: "/login" });
        })
        .catch(() => {
          console.log("用户取消了修改,未进行任何操作");
        });
    },
    backToHome() {
      this.$router.replace("/home/main");
    },
  },
  mounted() {
    this.person_info = JSON.parse(localStorage.getItem("person_info"));
    if (this.person_info.academy == undefined)
      this.showAcademy = "未选择学院专业";
    else
      this.showAcademy =
        this.person_info.academy + "-" + this.person_info.specialty;
  },
};
</script>
<style scoped>
#info-header {
  height: 2.5rem;
  letter-spacing: 0.2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #d2d2d2;
  border-radius: 5px;
  color: #3f3f3f;
  background: #f1f6ff;
}
#button-o {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}
.button-i {
  width: 75%;
  padding-top: 5px;
}
.nav-title {
  font-weight: bolder;
  font-size: large;
}
</style>
