const qrcodeGen = (code) => {
  var opcoesQRCode = {
    width: 128,
    height: 128,
  };

  // Criação do QR Code
  var qrcode = new QRCode(document.getElementById("qrcode"), opcoesQRCode);
  qrcode.makeCode(code);
};

$(document).ready(function () {
  // Captura o evento de clique do botão "Enviar"
  $("#sendButton").click(function () {
    // Obtém o valor do input de endereço
    var addressValue = $("#endereco").val();
    var latitudeValue = $("#latitude").val();
    var longitudeValue = $("#longitude").val();
    var landmarkValue = $("#p_ref").val();

    // Cria um objeto de dados para enviar para o Flask
    var dataToSend = {
      address: addressValue,
      landmark: landmarkValue,
      lat: latitudeValue,
      lon: longitudeValue,
    };

    // Faz uma requisição POST para o Flask
    $.ajax({
      type: "POST",
      url: "/api/gerar", // Substitua pelo endpoint do Flask que irá processar os dados
      data: dataToSend,
      success: function (response) {
        // Aqui você pode lidar com a resposta do Flask, se necessário
        $("#gerar_cepx")[0].reset();
        $("#result_input").val(response.code);
        qrcodeGen(response.code);
      },
      error: function (error) {
        // Trate possíveis erros aqui
        console.error(error);
      },
    });
  });
});
