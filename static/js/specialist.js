
function add_specialist() {
    var phone = $('#phone').val();
    var email = $('#email').val();

    var rePhone = /^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/
    var reEmail = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/

    $('#category1').removeClass("input-error");
    $('#category2').removeClass("input-error");
    $('#phone').removeClass("input-error");
    $('#email').removeClass("input-error");

    if ($('#category1').val() == "0") {
        $('#category1').addClass("input-error");
        return false;
    }

    if ($('#category2').val() == "0") {
        $('#category2').addClass("input-error");
        return false;
    }

    if (!rePhone.test(phone)) {
        $('#phone').addClass("input-error");
        return false;
    }

    if (!reEmail.test(email)) {
        $('#email').addClass("input-error");
        return false;
    }

    return true;
}