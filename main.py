"""A ideia do código é acessar o xml (não o html dessa vez) de um produto qualquer

da Amazon para verificar o seu preço diariamente e se esse preço for abaixo de um determinado

valor, passar um e-mail avisando """


"""primeiro são importadas as bibliotecas: request, para fazer a requisição get, lxml, para

lidar com o código e bs4 para trabalhar o código em txt"""

import requests

import lxml

from bs4 import BeautifulSoup

"""aqui fica a url do produto e abaixo o header que são informação que são passadas

para o site da Amazon, como o browser que se está usando, qual o computador, para verificar

essas informações é só acessar o site http://myhttpheader.com/"""

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"

header = {

 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

 "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"

}

"""a variável response guarda as informações do request, usando os atributos da url e do headers,

ou seja, guarda as informações que serão utilizadas passando os atributos mínimos obrigatórios"""

response = requests.get(url, headers=header)

"""a variável soup guarda o conteúdo da variável response, lembrando que aqui ao invés

de hmtl.parser, a página está em lxml, depois o prettify imprime o conteúdo de maneira mais visual"""

soup = BeautifulSoup(response.content, "lxml")

print(soup.prettify())

"""a variável price vai guardar o conteúdo da tag id transformada em texto, então,

o método split vai separar o conteúdo do text antes e depois do $ e vai guardar o valor no espaço

[1], então ele será transformado em um float e por fim, impresso"""

price = soup.find(id="priceblock_ourprice").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)

print(price_as_float)

"""aqui é o código para verificar se o preço é menor que o determinado, 200, nesse caso,

e, se for, passar o e-mail, conforme sintaxe da biblioteca smtplib, explicada anteriormente"""

import smtplib


title = soup.find(id="productTitle").get_text().strip()

print(title)


BUY_PRICE = 200


if price_as_float < BUY_PRICE:

 message = f"{title} is now {price}"


 with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:

 connection.starttls()

 result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)

 connection.sendmail(

 from_addr=YOUR_EMAIL,

 to_addrs=YOUR_EMAIL,

 msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"

 )