$(document).ready(function() {

$('.ver').click(  function(e) { 
	var value = parseInt($("#credito").val());
	$('#credito').val(value-1);
	if (value<1) {
		alert('No hay mas creditos');
		
	}else {
       $.ajax({
                type:'get',
                url: '/descuentaCredito/'+ $(this).attr('pk'),
                dataType: "json",
               // data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    // alert("complete");
                },
                success: function (data) {
                    // alert(data.pk+'r');
                    $('.'+data.pk+'r').css('display', 'none');
                    $('.'+data.pk+'v').css('display', 'block');

  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });


	};
  });



});


