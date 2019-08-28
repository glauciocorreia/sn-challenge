// Máscara de CEP
$('#div_id_cep').keypress(function () {
  $('#div_id_cep :input').mask('00.000-000')
})

// Máscara de Telefone
$('#div_id_telefone').keypress(function () {
  $('#div_id_telefone :input').mask('(00) 00000-0000')
})

// ViaCEP
$(document).ready(function () {

  function limpa_formulário_cep() {
    // Limpa valores do formulário de cep.
    $("#div_id_endereco :input").val("");
    $("#div_id_cidade :input").val("");
    $("#div_id_estado :input").val("");
  }

  //Quando o campo cep perde o foco.
  $("#div_id_cep :input").blur(function () {

    //Nova variável "cep" somente com dígitos.
    var cep = $(this).val().replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep != "") {

      //Expressão regular para validar o CEP.
      var validacep = /^[0-9]{8}$/;

      console.log(cep)
      //Valida o formato do CEP.
      if (validacep.test(cep)) {

        //Preenche os campos com "..." enquanto consulta webservice.
        $("#div_id_endereco :input").val("...");
        $("#div_id_cidade :input").val("...");
        $("#div_id_estado :input").val("...");

        //Consulta o webservice viacep.com.br/
        $.getJSON("https://viacep.com.br/ws/" + cep + "/json/", function (dados) {

          if (!("erro" in dados)) {
            //Atualiza os campos com os valores da consulta.
            $("#div_id_endereco :input").val(dados.logradouro);
            $("#div_id_cidade :input").val(dados.localidade);
            $("#div_id_estado :input").val(dados.uf);
            $("#div_id_numero :input").focus();
          } //end if.
          else {
            //CEP pesquisado não foi encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
            
          }
        });
      } //end if.
      else {
        //cep é inválido.
        limpa_formulário_cep();
        alert("Formato de CEP inválido.");
      }
    } //end if.
    else {
      //cep sem valor, limpa formulário.
      limpa_formulário_cep();
    }
  });
});
