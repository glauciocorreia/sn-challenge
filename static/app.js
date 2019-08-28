$('#div_id_cep').keypress(function() {
  $('#div_id_cep :input').mask('00.000-000')
})

$('#div_id_telefone').keypress(function() {
  $('#div_id_telefone :input').mask('(00) 00000-0000')
})