# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

#1. O padrão começa com \(: Isso corresponde ao caractere de parêntese aberto "(" literal. Como os parênteses são metacaracteres em expressões regulares e são usados para criar grupos de captura, precisamos escapá-los com uma barra invertida para indicar que queremos correspondência literal com o caractere "(".
#2. Em seguida, temos \d{2}: Isso corresponde a dois dígitos consecutivos. O metacaractere \d corresponde a qualquer dígito de 0 a 9, e {2} especifica que queremos exatamente dois dígitos.
#3. Depois, temos \) seguido de um espaço: Isso corresponde ao caractere de parêntese fechado ")" literal seguido por um espaço em branco.
#4. Então, temos o dígito 9 literal, seguido de \d{4}: Isso corresponde ao dígito 9 seguido por exatamente quatro dígitos.
#5. Após isso, temos o caractere hífen - literal.
#6. Por fim, temos \d{4} novamente: Isso corresponde a exatamente quatro dígitos.
#Juntando tudo isso, o padrão da expressão regular fica assim: \(\d{2}\)\s9\d{4}-\d{4}. Essa expressão regular é usada para validar números de telefone no formato especificado: "(XX) 9XXXX-XXXX", onde X representa um dígito de 0 a 9 e os espaços são respeitados conforme necessário.

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
  pattern = r"\(\d{2}\)\s9\d{4}-\d{4}"
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
  if re.match(pattern, phone_number):
      # TODO: Agora crie um return, para retornar que o número de telefone é válido:
    return "Número de telefone válido."
      # TODO: Crie um else e return, caso não o número de telefone seja inválido:
  else:
    return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)
# Imprime o resultado:
print(result)
