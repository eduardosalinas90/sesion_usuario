function verificar(){

var v1 = 0, v2=0,v3=0;

v1 = validacion('nombre');
v2 = validacion('apellido');
v3 = validacion('sexo');

if(v1 === false || v2 ===false || v3 === false ){

	$("#exito").hide();
	$("#error").show();
}else {

	$("#error").hide();
	$("#exito").show();
}


}



function validacion(campo){

if(campo == 'nombre') {

var nombre = $("#nombre").val();

if(nombre == ""){

	$("#icono"+campo).remove();
	$('#'+campo).parent().parent().attr("class", "form-group has-error has-feedback");
    $('#'+campo).parent().children('span').text("Ingrese algo").show();
    $('#'+campo).parent().append("<span id='icono"+campo+"' class='glyphicon glyphicon-remove form-control-feedback'></span>");
    return false;


}else {

	 $("#icono"+campo).remove();
     $('#'+campo).parent().parent().attr("class", "form-group has-success has-feedback");
     $('#'+campo).parent().children('span').hide();
     $('#'+campo).parent().append("<span id='icono"+campo+"' class='glyphicon glyphicon-ok form-control-feedback'></span>");
             
     return true;
}

}


if(campo == 'apellido') {

var apellido = $("#apellido").val();

if(apellido == ""){

	$("#icono"+campo).remove();
	$('#'+campo).parent().parent().attr("class", "form-group has-error has-feedback");
    $('#'+campo).parent().children('span').text("Ingrese algo").show();
    $('#'+campo).parent().append("<span id='icono"+campo+"' class='glyphicon glyphicon-remove form-control-feedback'></span>");
    return false;


}else {

	 $("#icono"+campo).remove();
     $('#'+campo).parent().parent().attr("class", "form-group has-success has-feedback");
     $('#'+campo).parent().children('span').hide();
     $('#'+campo).parent().append("<span id='icono"+campo+"' class='glyphicon glyphicon-ok form-control-feedback'></span>");
             
     return true;
}

}


if(campo == 'sexo') {

var opciones = $(campo);

var seleccionado = false;
for (var i = 0; i < opciones.length; i++){
	if(opciones[i].checked) {
        seleccionado = true;
         break;
                  }

}


  if(!seleccionado) {
     $('#male').parent().parent().attr("class", "form-group has-error has-feedback");
     $('#male').parent().parent().next().append("<span id='sexo'  class='glyphicon glyphicon-remove form-control-feedback'></span>");


     return false;
     }
         else{
         $("#sexo").remove();
         $('#male').parent().parent().parent().attr("class", "form-group has-success");
         return true;
                }


}



}