import requests

waluta = input('Podaj kod waluty: ')

check_api = 'http://api.nbp.pl/api/exchangerates/tables/a?format=json'
json_check_data = requests.get(check_api).json()

waluty = []
for curr in json_check_data[0]['rates']:
    waluty.append(curr['code'])

def currency_rate():
    global rate
    main_api = 'http://api.nbp.pl/api/exchangerates/rates/a/'
    format = '/?format=json'

    url = '{}{}{}'.format(main_api, waluta, format)
    json_data = requests.get(url).json()

    rate = json_data['rates'][0]['mid']
    date = json_data['rates'][0]['effectiveDate']
    print('Średni kurs {} na dzień '.format(waluta.upper()) + str(date) + ': ' + (str(round(rate, 2))) + ' zł.')

currency_rate()

amount_usd = input('Podaj kwotę w {}: '.format(waluta.upper()))
amount_converted = float(amount_usd) * rate
print('{} {} kosztuje '.format(amount_usd, waluta.upper()) + str(round(amount_converted, 2)) + ' zł.')
