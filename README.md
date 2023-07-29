# Projeto CEP

**Novo Código de Endereçamento Postal**, para auxiliar na transferência de metadados entre pessoas físicas e/ou jurídicas em coordenadas geográficas brasileiras, em especial naquelas em que ainda não há registro formal de logradouro.

Este projeto corresponde a uma das propostas submetidas ao **Hackathon Correios**, da **Campus Party Brasil** (CPBR15), realizada em julho de 2023.

## Tech stack

**Front-end:** HTML5; CSS3; JavaScript.

**Back-end:** Flask (Python 3.10 ou superior).

## Deploy

Para fazer o _deploy_ desse projeto, é requerida a instalação dos seguintes recursos:

- **Python** (versão 3.10 ou superior)
- **pip**

Em seguida, instale as dependências deste projeto:

```bash
  pip install -r requirements.txt
```

Para inicializar a aplicação, execute o comando como segue. Uma mensagem será exibida no terminal, contendo o endereço e a porta do servidor ativo.

```bash
  python -m flask --app app run
```

### Variáveis de Ambiente

Este projeto permite a definição de variáveis de ambiente. Para configurá-las, crie um arquivo `.env` no diretório-raiz da aplicação e configure os valores a seguir.

| Parâmetro    | Tipo       | Valor padrão    |
| :----------- | :--------- | :-------------- |
| `SECRET_KEY` | `string`   | `secret-key`    |
| `DEBUG`      | `boolean`  | `False`         |

## Documentação da API

### Obter coordenadas geográficas de logradouro

```http
  POST /api/find
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `address` | `string` | O logradouro do qual serão obtidas as coordenadas geográficas |

### Gerar um Novo Código de Endereçamento Postal

```http
  POST /api/gerar
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `address` | `string` | O logradouro do qual serão obtidas as coordenadas geográficas |
| `landmark` | `string` | Um ponto de referência descritivo para orientar a localização aproximada. Opcional |
| `lat` | `string` | A coordenada geográfica _latitude_. Opcional se informado um `address` válido |
| `lon` | `string` | A coordenada geográfica _longitude_. Opcional se informado um `address` válido |

### Decodificar um Novo Código de Endereçamento Postal

```http
  POST /api/ler
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `code` | `string` | O Novo Código de Endereçamento Postal gerado previamente, a ser decodificado |
