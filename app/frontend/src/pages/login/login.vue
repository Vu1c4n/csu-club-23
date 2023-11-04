<template>
  <div id="page">
    <div id="form">
      <van-nav-bar>
        <template #title><div class="nav-title">个人信息</div></template>
      </van-nav-bar>
    </div>
    <div id="name">
      <van-field v-model="form.name" label="姓名" placeholder="请输入姓名" />
    </div>
    <div id="sex">
      <van-field name="sex" label="性别">
        <template #input>
          <van-radio-group v-model="form.sex" direction="horizontal">
            <van-radio name="男">男</van-radio>
            <van-radio name="女">女</van-radio>
          </van-radio-group>
        </template>
      </van-field>
    </div>
    <div id="nation">
      <van-field
        readonly
        clickable
        name="picker1"
        :value="form.nation"
        label="民族"
        placeholder="选择民族"
        @click="showPicker = true"
      />
      <van-popup v-model="showPicker" position="bottom">
        <van-picker
          show-toolbar
          :columns="nationcolumns"
          @confirm="onConfirm"
          @cancel="showPicker = false"
        />
      </van-popup>
    </div>
    <div id="birth">
      <van-field
        readonly
        clickable
        name="datetimePicker"
        :value="form.birth"
        label="出生年月"
        placeholder="点击选择时间"
        @click="showPicker1 = true"
      />
      <van-popup v-model="showPicker1" position="bottom">
        <van-datetime-picker
          type="year-month"
          v-model="currentDate"
          :min-date="minDate"
          :max-date="maxDate"
          @confirm="onConfirm1"
          @cancel="showPicker1 = false"
        />
      </van-popup>
    </div>
    <div id="political">
      <van-field
        readonly
        clickable
        name="picker2"
        :value="form.political"
        label="政治面貌"
        placeholder="点击选择"
        @click="showPicker2 = true"
      />
      <van-popup v-model="showPicker2" position="bottom">
        <van-picker
          show-toolbar
          :columns="politicalcolumns"
          @confirm="onConfirm2"
          @cancel="showPicker2 = false"
        />
      </van-popup>
    </div>
    <div id="stu_id">
      <van-field
        readonly
        name="stu_id"
        v-model="form.stu_id"
        label="学号"
        placeholder="输入学号"
        @click="show_stu_id = true"
      />
      <van-number-keyboard
        :show="show_stu_id"
        extra-key="L"
        close-button-text="完成"
        @blur="show_stu_id = false"
        @input="onInput_stu_id"
        @delete="onDelete_stu_id"
      />
    </div>
    <div id="warn" v-if="this.id_warn">学号输入格式错误，请检查</div>
    <div id="stu_type">
      <van-field
        readonly
        clickable
        name="picker3"
        :value="form.stu_type"
        label="培养层次"
        placeholder="点击选择"
        @click="showPicker3 = true"
      />
      <van-popup v-model="showPicker3" position="bottom">
        <van-picker
          show-toolbar
          :columns="stu_typecolumns"
          @confirm="onConfirm3"
          @cancel="showPicker3 = false"
        />
      </van-popup>
    </div>
    <div id="grade">
      <van-field
        readonly
        clickable
        name="picker5"
        :value="form.grade"
        label="年级"
        placeholder="点击选择"
        @click="showPicker5 = true"
      />
      <van-popup v-model="showPicker5" position="bottom">
        <van-picker
          show-toolbar
          :columns="gradecolumns"
          @confirm="onConfirm5"
          @cancel="showPicker5 = false"
        />
      </van-popup>
    </div>
    <div id="academy_specialty" v-if='form.grade != ""||form.grade'>
      <van-field
        v-model="showAcademy"
        is-link
        readonly
        label="学院专业"
        placeholder="请选择学院专业"
        @click="schoolshow = true"
      />
      <van-popup v-model="schoolshow" round position="bottom">
        <van-cascader
          active-color="#1989fa"
          v-model="form.specialty"
          title="请选择学院专业"
          :options="options"
          @close="schoolshow = false"
          @finish="onFinish"
        />
      </van-popup>
    </div>
    <div id="stu_class">
      <van-field
        v-model="form.stu_class"
        name="stu_class"
        label="专业班级"
        placeholder="例: 土木2101"
      />
    </div>
    <div id="from_location">
      <van-field
        readonly
        clickable
        name="picker4"
        :value="form.from_location"
        label="生源地"
        placeholder="点击选择"
        @click="showPicker4 = true"
      />
      <van-popup v-model="showPicker4" position="bottom">
        <van-picker
          show-toolbar
          :columns="location_typecolumns"
          @confirm="onConfirm4"
          @cancel="showPicker4 = false"
        />
      </van-popup>
    </div>
    <div id="phone">
      <van-field
        v-model="form.phone"
        name="phone"
        type="tel"
        label="手机号"
        class="phone"
      />
      <div id="warn" v-if="this.phone_warn">手机号输入格式错误，请检查</div>
    </div>
    <div id="qq">
      <van-field v-model="form.qq" type="tel" label="QQ" class="QQ" />
    </div>
    <div id="button">
      <van-button round type="info" @click="send_msg" size="large"
        >提交信息</van-button
      >
    </div>
  </div>
</template>
<script>
import { sendmsg, getoptions,getmsg } from "../../request/api";
import { Toast } from "vant";
Toast.setDefaultOptions({ duration: 1000 });
export default {
  name: "main-login",
  data() {
    return {
      id_warn: 0,
      phone_warn: 0,
      id_pattern: /^\d{10}/,
      phone_pattern: /^[1]\d{10}$/,
      show_stu_id: false,
      showPicker: false,
      nationcolumns: [
        "汉族",
        "蒙古族",
        "回族",
        "藏族",
        "维吾尔族",
        "苗族",
        "彝族",
        "壮族",
        "布依族",
        "朝鲜族",
        "满族",
        "侗族",
        "瑶族",
        "白族",
        "土家族",
        "哈尼族",
        "哈萨克族",
        "傣族",
        "黎族",
        "傈僳族",
        "佤族",
        "畲族",
        "高山族",
        "拉祜族",
        "水族",
        "东乡族",
        "纳西族",
        "景颇族",
        "柯尔克孜族",
        "土族",
        "达斡尔族",
        "仫佬族",
        "羌族",
        "布朗族",
        "撒拉族",
        "毛南族",
        "仡佬族",
        "锡伯族",
        "阿昌族",
        "普米族",
        "塔吉克族",
        "怒族",
        "乌孜别克族",
        "俄罗斯族",
        "鄂温克族",
        "德昂族",
        "保安族",
        "裕固族",
        "京族",
        "塔塔尔族",
        "独龙族",
        "鄂伦春族",
        "赫哲族",
        "门巴族",
        "珞巴族",
        "基诺族",
        "其他",
      ],
      showPicker1: false,
      minDate: new Date(1970, 0, 1),
      maxDate: new Date(2020, 11, 1),
      currentDate: new Date(2000, 0, 1),
      showPicker2: false,
      politicalcolumns: ["共青团员", "中共预备党员", "中共党员", "其他"],
      show: false,
      showPicker3: false,
      stu_typecolumns: ["本科", "硕士研究生", "博士研究生"],
      location_typecolumns: [
        "中国内地（大陆)",
        "中国香港",
        "中国澳门",
        "中国台湾",
        "国外",
      ],
      showPicker4: false,
      gradecolumns: ["2023级", "2022级", "2021级", "2020级", "2019级"],
      showPicker5: false,
      showAcademy: "",
      schoolshow: false,
      cascaderValue: "",
      options: [
        // {
        //   text: '自动化学院',
        //   children: [{ text: '电气工程及其自动化' }, { text: '自动化' }, { text: '测控技术与仪器' }, { text: '电子信息工程' }, { text: '智能科学与技术' }, { text: '探测制导与控制技术' }]
        // },
        // {
        //   text: '国际教育学院',
        //   children: [{ text: '国际经济与贸易' }, { text: '金融学' }, { text: '信息管理与信息系统' }, { text: '工商管理' }, { text: '会计学' }]
        // }
      ],
      form: {
        name: "",
        sex: "",
        nation: "",
        birth: "",
        political: "",
        stu_id: "",
        stu_type: "",
        from_location: "",
        grade: "",
        academy: "",
        specialty: "",
        phone: "",
        qq: "",
      },
      option_freshman: [],
      option_all: [],
    };
  },
  methods: {
    onConfirm(nation) {
      this.form.nation = nation;
      this.showPicker = false;
    },
    onConfirm1(birth) {
      const x = birth.getFullYear();
      const y = birth.getMonth();
      this.form.birth = String(x) + "年" + String(y + 1) + "月";
      this.showPicker1 = false;
    },
    onConfirm2(political) {
      this.form.political = political;
      this.showPicker2 = false;
    },
    onConfirm3(type) {
      this.form.stu_type = type;
      this.showPicker3 = false;
    },
    onConfirm4(loaction) {
      this.form.from_location = loaction;
      this.showPicker4 = false;
    },
    onConfirm5(grade) {
      this.form.grade = grade;
      this.showPicker5 = false;
      console.log(grade);
      if (grade == "2023级") this.options = this.option_freshman;
      else this.options = this.option_all;
      console.log(this.options);
    },
    onFinish({ selectedOptions }) {
      this.schoolshow = false;
      this.fieldValue = selectedOptions.map((option) => option.text).join("/");
      const xyzy = this.fieldValue.split("/");
      this.form.academy = xyzy[0];
      this.form.specialty = xyzy[1];
      this.showAcademy = this.form.academy + "-" + this.form.specialty;
    },
    //stu_id键盘
    onInput_stu_id(value) {
      this.form.stu_id = this.form.stu_id + value.toString();
    },
    onDelete_stu_id() {
      this.form.stu_id = this.form.stu_id.substring(
        0,
        this.form.stu_id.length - 1
      );
    },
    clearEvent(e) {
      console.log(e);
      if (this.keyboard_type == "phone") this.form.phone = "";
      else if (this.keyboard_type == "QQ") this.form.qq = "";
    },
    onInput(value) {
      console.log(value);
      if (this.keyboard_type == "phone")
        this.form.phone = this.form.phone + value.toString();
      else if (this.keyboard_type == "QQ")
        this.form.qq = this.form.qq + value.toString();
    },
    onDelete() {
      console.log();
      if (this.keyboard_type == "phone")
        this.form.phone = this.form.phone.substring(
          0,
          this.form.phone.length - 1
        );
      else if (this.keyboard_type == "QQ")
        this.form.qq = this.form.qq.substring(0, this.form.qq.length - 1);
    },
    // 功能函数
    send_msg() {
      if (!this.phone_pattern.test(this.form.phone)) {
        this.phone_warn = 1;
      } else {
        this.phone_warn = 0;
      }
      if (Object.values(this.form).includes("") || this.phone_warn == 1) {
        Toast("有信息未填写或填写错误");
      } else {
        sendmsg(this.form).then((res) => {
          Toast(res.data.msg);
          setTimeout(this.$router.replace("/index"), 1000);
        });
      }
    },
  },
  mounted() {
    getoptions().then((res) => {
      this.option_freshman = res.data.data[0];
      this.option_all = res.data.data[1];
      console.log(res.data.data);
      if (grade == "2023级") this.options = this.option_freshman;
      else this.options = this.option_all;
      console.log(this.options);
      
      this.person_info = JSON.parse(localStorage.getItem("person_info"));
      this.form = this.person_info;
      console.log(this.form);
      if (this.form.academy == undefined) this.showAcademy = "未选择学院专业";
      else this.showAcademy = this.form.academy + "-" + this.form.specialty;
      console.log(form.grade)
    });
  },
};
</script>
<style scoped>
.van-field {
  height: 50px;
}
#button {
  margin: 34px;
}
</style>
<style>
#form {
  overflow: scroll;
}
#warn {
  font-size: x-small;
  color: rgb(255, 0, 0);
  display: flex;
  justify-content: center;
}
.nav-title {
  font-weight: bolder;
  font-size: large;
}
</style>