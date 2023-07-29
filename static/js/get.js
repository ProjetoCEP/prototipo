let marker = null;
let findInMap = (lat, lon) => {
    let mapOptions = {
        center:[lat, lon],
        zoom:100
    }
    
    let map = new L.map('map' , mapOptions);
    
    let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    map.addLayer(layer);
    
    marker = new L.marker([lat, lon]).addTo(map);
}

$(document).ready(function() {
    // Evento do clique no botão
    $("#validButton").on("click", function() {
      var code = $("#endereco").val(); // Obtém o valor do campo de entrada

      // Faz a requisição GET para a API com o parâmetro "code" na URL
      $.get("/api/ler/" + code, function(data) {
        // Manipule os dados de resposta aqui
        latitude = data.result.lat
        longitude = data.result.lon
        findInMap(latitude, longitude);

      });
    });
  });