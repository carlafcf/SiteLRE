$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    // jQuery.validator.addMethod('answercheck', function (value, element) {
    //     return this.optional(element) || /^\bcat\b$/.test(value)
    // }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 10
                }
            },
            messages: {
                name: {
                    required: "Por favor, preencha o seu nome",
                    minlength: "Seu nome deve ter pelo menos 2 caracteres"
                },
                subject: {
                    required: "Por favor, preencha o assunto",
                    minlength: "O assunto deve ter pelo menos 4 caracteres"
                },
                email: {
                    required: "Por favor, coloque seu e-mail"
                },
                message: {
                    required: "Por favor, coloque aqui a mensagem que deseja enviar",
                    minlength: "Sua mensagem deve ter pelo menos 10 caracteres"
                }
            }
            // ,
        //     submitHandler: function(form) {
        //         $(form).ajaxSubmit({
        //             type:"POST",
        //             data: $(form).serialize(),
        //             url:"contact_process.php",
        //             success: function() {
        //                 $('#contactForm :input').attr('disabled', 'disabled');
        //                 $('#contactForm').fadeTo( "slow", 1, function() {
        //                     $(this).find(':input').attr('disabled', 'disabled');
        //                     $(this).find('label').css('cursor','default');
        //                     $('#success').fadeIn()
        //                     $('.modal').modal('hide');
		//                 	$('#success').modal('show');
        //                 })
        //             },
        //             error: function() {
        //                 $('#contactForm').fadeTo( "slow", 1, function() {
        //                     $('#error').fadeIn()
        //                     $('.modal').modal('hide');
		//                 	$('#error').modal('show');
        //                 })
        //             }
        //         })
        //     }
        // })
    })
        
 })(jQuery)
})