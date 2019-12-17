/**页面初始化时一级分类加载 */
$('document').ready( function () {
    $.ajax({
        url:"/specialist/category/", //请求的url地址
        dataType:"json", //返回格式为json
        async:true,//请求是否异步，默认为异步，这也是ajax重要特性
        data:{}, //参数值
        type:"GET", //请求方式
        beforeSend:function(){
            //请求前的处理
        },
        success:function(req){
            //请求成功时处理
            $('#category1').html("");
            $("#category1").prepend("<option value=0>请选择</option>");//添加第一个option值
            $.each(req, function(name, value) {
                $("#category1").append("<option value=" + name + ">" + value + "</option>");
            })
        },
        complete:function(){
            //请求完成的处理
        },
        error:function(){
            //请求出错处理
        }
    });

    $('#category1').change( function () {
        var key = $('#category1').val();
        $.ajax({
            url:"/specialist/category/", //请求的url地址
            dataType:"json", //返回格式为json
            async:true,//请求是否异步，默认为异步，这也是ajax重要特性
            data:{"key": key}, //参数值
            type:"GET", //请求方式
            beforeSend:function(){
                //请求前的处理
            },
            success:function(req){
                //请求成功时处理
                $('#category2').html("");
                $("#category2").prepend("<option value=0>请选择</option>");//添加第一个option值
                $.each(req, function(name, value) {
                    $("#category2").append("<option value=" + name + ">" + value + "</option>");
                })
            },
            complete:function(){
                //请求完成的处理
            },
            error:function(){
                //请求出错处理
            }
        });
    });
});
