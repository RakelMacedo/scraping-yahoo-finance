# scraping-yahoo-finance

Scraping com Python + Selenium + CSV

Obtendo dados específicos - "Date" e "Close" - dos últimos 10 dias do Yahoo Finance
e salvando-os em um arquivo CSV, chamado “eur_btc_rates.csv”, com duas colunas - “Date” e “BTC Closing Value”.

## eur_btc_rates.csv
```bash
,Date,BTC Closing Value
0,"Jun 12, 2022","26,560.93"
1,"Jun 11, 2022","26,958.94"
2,"Jun 10, 2022","27,648.17"
3,"Jun 09, 2022","28,356.05"
4,"Jun 08, 2022","28,192.89"
5,"Jun 07, 2022","29,123.80"
6,"Jun 06, 2022","29,346.38"
7,"Jun 05, 2022","27,881.74"
8,"Jun 04, 2022","27,831.81"
9,"Jun 03, 2022","27,708.94"            
```

## Tecnologias usadas:
<table>
  <tr>
    <td>Python</td>
    <td>Selenium</td>
    <td>Pandas</td>
  </tr>
  <tr>
    <td>3.*</td>
    <td>4.2</td>
    <td>1.4</td>
  </tr>
</table>


## Como executar:

1) Execute no terminal:
```bash
pip install -r requirements.txt
```
2) O Selenium requer um driver para fazer interface com o seu navegador. Seguem links para alguns dos drivers de navegador mais populares:

<table border="1" class="docutils">
<colgroup>
<col width="16%" />
<col width="84%" />
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Chrome</strong>:</td>
<td><a class="reference external" href="https://sites.google.com/chromium.org/driver/">https://sites.google.com/chromium.org/driver/</a></td>
</tr>
<tr class="row-even"><td><strong>Edge</strong>:</td>
<td><a class="reference external" href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/</a></td>
</tr>
<tr class="row-odd"><td><strong>Firefox</strong>:</td>
<td><a class="reference external" href="https://github.com/mozilla/geckodriver/releases">https://github.com/mozilla/geckodriver/releases</a></td>
</tr>
<tr class="row-even"><td><strong>Safari</strong>:</td>
<td><a class="reference external" href="https://webkit.org/blog/6900/webdriver-support-in-safari-10/">https://webkit.org/blog/6900/webdriver-support-in-safari-10/</a></td>
</tr>
</tbody>
</table>

Depois de baixar o driver de acordo com seu sistema operacional e navegador, faça o uplode do mesmo na raiz do projeto. 
No meu caso, esse arquivo em questão é o 'chromedriver' referente a versão mais recente do Driver do Chrome no momento. 

Sinta-se a vontade para exclui-lo quando der o Fork no código, pois provavelmente esta versão já terá sido ultrapassada e baixando o seu próprio driver ele será desnecessário. Priorize sempre a versão mais recente ;)

##

Pronto! Você esta pronto para rodar o código e obter os dados do Yahoo Finance. =)
