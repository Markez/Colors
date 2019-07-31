$(document).ready(function(){
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    //    ajax for login handling
    $('form.registerUser').on('submit',
      function(form){
        form.preventDefault();
                $.ajax({
                    type:'POST',
                    url:'/home/register/',
                    data:{
                        username:$('#username').val(),
                        email:$('#email').val(),
                        password:$('#password').val(),
                        csrfmiddlewaretoken: csrftoken,
                    },

                    // handle a successful response
                    success : function(data){
                        if(data=='passed'){
                                $('#username').val(''); // remove the value from the input
                                $('#email').val(''); // remove the value from the input
                                $('#password').val(''); // remove the value from the input
                                alert("Successful!");
                        }
                         else if(data=='wrongpwd'){
                               alert("Wrong  combination!");
                        }
                         else if(data=='notActive'){
                               alert("Account Not Active!!");
                        }
                        else
                         alert ('Failed');
                    },
                    // handle a non-successful response
                    error : function(data) {
                        alert("Encountered an Error");

                    }
                });


      });

});


