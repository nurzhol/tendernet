$(document).ready(function(){

    $('.form_buying_product').on('submit', function(e){
        e.preventDefault();
        var submit_btn = $('#submit_btn1');
        var data = {};
        data["product_id"] = submit_btn.data("product_id1");
        data["user_id"] = submit_btn.data("user_id1");
        data["request_path"] = submit_btn.data("request_path1");
        data["csrfmiddlewaretoken"] = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();

        data2 = data;
        data2['type'] = "form_buying_product";

        if(verifyUserClick(data2)) {
            return;
        }


        if (confirm("Вы действительно желаете участвовать?")) {
            alert('Спасибо за обращение. В ближайшее время с вами свяжется менеджер. А пока сохраните этот лот в Избранные.');
            var url = $('#form_buying_product').attr("action");
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    alert('Заявка на участие отправлена');
                },
                error: function(){
                    console.log("error")
                }
            });
        } else {
            return false;
        }
        
    });


    $('.buying_doc').on('submit', function(e){
        e.preventDefault();
        var submit_btn = $('#submit_btn_doc');
        var data = {};
        data["product_id"] = submit_btn.data("product_id");
        data["user_id"] = submit_btn.data("user_id");
        data["request_path"] = submit_btn.data("request_path");

        data2 = data;
        data2['type'] = "buying_doc";
        
        if(verifyUserClick(data2)) {
            return;
        }

        if (confirm("Вы запрашиваете Аудит конкурсной документации. Он необходим, чтобы узнать какие ресурсы необходимы для участия в этом тендере.")) {
            alert('Спасибо за обращение. В ближайшее время с вами свяжется менеджер. А пока сохраните этот лот в Избранные.');
            var csrf_token = $('#buying_doc [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            var url = $('#buying_doc').attr("action");

            console.log(data);
            console.log('we are working the data');

            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    alert('Заявка на запрос документов отправлена');
                },
                error: function(){
                    console.log("error")
                }
            });
        } else {
            return false;
        }
        
    });


    function verifyUserClick(data2) {
        const key = `verify_data-${data2['type']}-${data2['user_id']}-${data2['product_id']}`;
        if(localStorage.getItem(key)) {
            const verify_data = JSON.parse(localStorage.getItem(key));
            if(verify_data['product_id'] === data2['product_id'] && verify_data['user_id'] === data2['user_id'] &&  verify_data['type'] === data2['type']) {
                alert('Вы уже нажали на эту кнопку. в самое ближайшее время менеджер с вами свяжется');
                return true;
            } else {
                localStorage.setItem(key, JSON.stringify(data2));
            }
        } else {
            localStorage.setItem(key, JSON.stringify(data2));
        }
    }

    $(document).on("click", ".un-authorized", function(e){
        e.preventDefault();
        const url = $(this).attr('href');
        const message = $(this).data('message') ? 'Вы должны авторизоваться' : 'Вы должны авторизоваться или зарегистрироваться в системе';
        const favorite = $(this).data('favorite');

        swal(message, '', 'info')
        .then(r => {
            if(favorite) {
                window.open(url, 'blank');
            } else {
                window.location.href=url;
            }
        });

    });

});