var re = /^\w{3,16}$/;
var re2 = /^\w{6,18}$/;

var username_error_str = "用户名应为3-16位数字、字母、下划线";
var password1_error_str = "密码应为6-18位数字、字母、下划线";
var password2_error_str = "两次输入密码不一致"

/* 登录表单验证 */
function login() {
    var username = document.forms["userinfo"]["username"].value;
    var password = document.forms["userinfo"]["password"].value;

    if (!re.test(username)) {
        document.getElementById('username_error').innerText = username_error_str;
        return false;
    }

    if (!re2.test(password)) {
        document.getElementById('password_error').innerText = password1_error_str;
        return false;
    }

    var hash = hex_md5(password);
    document.forms["userinfo"]["password"].value = hash;

    return true;
}

/* 注册表单验证 */
function signin() {
    var username = document.forms["userinfo"]["username"].value;
    var password1 = document.forms["userinfo"]["password1"].value;
    var password2 = document.forms["userinfo"]["password2"].value;

    if (!re.test(username)) {
        document.getElementById('username_error').innerText = username_error_str;
        return false;
    }

    if (!re2.test(password1)) {
        document.getElementById('password1_error').innerText = password1_error_str;
        return false;
    }

    if (password1 != password2) {
        document.getElementById('password2_error').innerText = password2_error_str;
        return false;
    }

    var hash = hex_md5(password1);
    document.forms["userinfo"]["password1"].value = hash;
    document.forms["userinfo"]["password2"].value = hash;
    return true;
}

/* 修改用户名表单验证 */
function change_username() {
    var username = document.forms["form1"]["username"].value;

    if (!re.test(username)) {
        document.getElementById('username_error').innerText = username_error_str;
        return false;
    }

    return true;
}

/* 修改密码表单验证 */
function change_password() {
    var password1 = document.forms["form2"]["password1"].value;
    var password2 = document.forms["form2"]["password2"].value;

    if (!re2.test(password1)) {
        document.getElementById('password1_error').innerText = password1_error_str;
        return false;
    }

    if (password1 != password2) {
        document.getElementById('password2_error').innerText = password2_error_str;
        return false;
    }

    var hash = hex_md5(password1);
    document.forms["form2"]["password1"].value = hash;
    document.forms["form2"]["password2"].value = hash;
}