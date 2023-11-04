import { Axios1 } from "./axios";

export function wxlogin(code) {
  return Axios1.post("/stu/signin", { code });
}
export function applysendmsg(a, b,) {
  return Axios1.post(
    "/apply/send_msg",
    { index: a, obname: b },
    { params: { token: localStorage.getItem("token") } }
  );
}
export function getallclub() {
  return Axios1.get("/club/allclub");
}
export function sendmsg(form) {
  return Axios1.post("/stu/stu_msg", form, {
    params: { token: localStorage.getItem("token") },
  });
}
export function getmsg() {
  return Axios1.get("/stu/get_msg", {
    params: { token: localStorage.getItem("token") },
  });
}
export function delapply(index) {
  return Axios1.post(
    "/apply/del_apply",
    {},
    { params: { index, token: localStorage.getItem("token") } }
  );
}
export function getapply() {
  return Axios1.get("/apply/get_pratical", {
    params: { token: localStorage.getItem("token") },
  });
}
export function getoptions() {
  return Axios1.get("/apply/options");
}
