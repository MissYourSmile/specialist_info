function extract() {
    re = /^[\u4E00-\u9FA5A-Za-z0-9_]+$/;

    $('#category').removeClass("input-error");
    $('#name').removeClass("input-error");
    $('#num').removeClass("input-error");

    if (!re.test($('#name').val())) {
        $('#name').addClass('input-error');
        return false;
    }

    if ($('#category').val() == "0") {
        $('#category').addClass("input-error");
        return false;
    }

    if ($('#num').val < 0) {
        $('#num').addClass("input-error");
        return false;
    }

    return true;
}