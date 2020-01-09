from amadeus import Client, ResponseError

amadeus = Client()

print('Flight Busiest Traveling Period')
try:
    '''
    What were the busiest months for Madrid in 2017?
    '''
    response = amadeus.travel.analytics.air_traffic.busiest_period.get(cityCode='MAD', period='2017', direction='ARRIVING')
    print(response.data)
except ResponseError as error:
    print(error)