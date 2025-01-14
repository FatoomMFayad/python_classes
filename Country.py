class Country:
    name = ''
    population = 0
    capital = ''
    outcome = 0
    income = 0

    def cal_revenue(self):
        return self.outcome - self.income

c1 = Country()
c1.name = 'Palestine'
c1.capital = 'Jerusalem'
c1.population = 13000000
c1.outcome = 70000
c1.income = 10000

c2 = Country()
c2.name = 'Yemen'
c2.capital = 'Sanaa'
c2.population = 8000000
c2.outcome = 60000
c2.income = 10000

countries = [c1, c2]
for country in countries:
    print(country.cal_revenue())


