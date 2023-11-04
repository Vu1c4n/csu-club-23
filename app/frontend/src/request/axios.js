import axios from "axios";
// 设计两种请求，2携带token，1不带
export const Axios1 = axios.create({
  baseURL: "https://club23.54sher.com/api",
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});
