const LogIn = async () => {
    let regexPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regexPattern.test(logInEmail.value))
      ElMessage({
        showClose: true,
        message: "登录邮箱非法！",
        type: "error"
      });
    else if (logInPassword.value.length < 8 || logInPassword.value.length > 20)
      ElMessage({
        showClose: true,
        message: "密码长度非法！",
        type: "error"
      });
  
    // 发送数据
    try {
      const response = await axios.post("http://127.0.0.1:8000/log-in/", {
        user_mail: logInEmail.value,
        user_password: logInPassword.value
      });
      if (response.data["code"] == -1) {
        ElMessage({
          showClose: true,
          message: "用户请求格式不正确！",
          type: "error"
        });
        return;
      } else if (response.data["code"] == 0) {
        ElMessage({
          showClose: true,
          message: "登录邮箱 " + logInEmail.value + " 未注册！",
          type: "error"
        });
        return;
      } else if (response.data["code"] == 2) {
        ElMessage({
          showClose: true,
          message: "登录密码不正确！",
          type: "error"
        });
        return;
      } else if (response.data["code"] == 1) {
        ElMessage({
          showClose: true,
          message: "登录成功！",
          type: "success"
        });
        user_data.value = response.data["user"];
      }
    } catch (error) {
      let errorMessage = "请求错误！";
      if (error.response && error.response.data && error.response.data.detail) {
        errorMessage += " 详情: " + error.response.data.detail;
      }
      ElMessage({
        showClose: true,
        message: errorMessage,
        type: "error"
      });
      return;
    }
}