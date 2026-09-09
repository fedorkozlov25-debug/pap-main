$(document).ready(function(){
    $('#registrationForm').on('submit',function(e){
        e.preventDefault();
        error =0;
        if ($('#fullName').val().trim() === '' || $('#password').val().trim() != $('#confirmPassword').val().trim()){
            error = 1;
        }else{
            error = 0;
        }
        if (error == 0){
            $.ajax({
                url: '/user_register',
                method: 'POST',
                contentType: 'application/json',
                data:JSON.stringify({
                    name: $('#fullName').val(),
                    password: $('#password').val(),
                    email: $('#email').val()
                })
            })
        }

    })
})