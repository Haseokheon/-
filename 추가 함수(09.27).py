def payment_tax_limit_func(tax_year, total_salary):
    if tax_year in [2023]:
        if total_salary <= 33000000:
            payment_tax_limit = 740000
        elif total_salary <= 43000000:
            payment_tax_limit = max(740000 - (total_salary - 33000000) * 0.008, 660000)
        elif total_salary <= 70000000:
            payment_tax_limit = 660000
        elif total_salary <= 70320000:
            payment_tax_limit = max(660000 - (total_salary - 70000000) * 0.5, 550000)
        elif total_salary <= 120000000:
            payment_tax_limit = 500000
        elif total_salary <= 120600000:
            payment_tax_limit = max(500000 - (total_salary - 120000000) * 0.5, 200000)
        else:
            payment_tax_limit = 200000
    else: #tax_year in [2019,2020,2021,2022]
        if total_salary <= 33000000:
            payment_tax_limit = 740000
        elif total_salary <= 43000000:
            payment_tax_limit = max(740000 - (total_salary - 33000000) * 0.008, 660000)
        elif total_salary <= 70000000:
            payment_tax_limit = 660000
        elif total_salary <= 70320000:
            payment_tax_limit = max(660000 - (total_salary - 70000000) * 0.5, 500000)
        else:
            payment_tax_limit = 500000
    return payment_tax_limit

def payment_tax_change_func(outcome_tax, payment_tax_limit):
    if outcome_tax <= 1300000:
        payment_tax_change = min(outcome_tax * 0.55, payment_tax_limit)
    else:
        payment_tax_change = (outcome_tax * 0.3 + 325000, payment_tax_limit)
    return payment_tax_change

def payment_tax_youth_change_func(outcome_tax, payment_tax_change, youth_discount):
    payment_tax_youth_change = payment_tax_change * (1 - youth_discount / outcome_tax)




def youth_day_calculate_func(tax_year, date1, date2, date3, date4):
    #date1-date2: 첫번째 감면기간 date3-date4: 두번째 감면기간
    jan = 31
    feb = 28
    feb_20 = 29
    mar = 31
    april = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31

    data = [date1, date2, date3, date4]
    if tax_year == 2020:
        if len(data) == 4:

            return date            
        else:
            day_plus = 1000
            return day_plus

def youth_day_calculate_func(tax_year, date1, date2, date3, date4):
    #date1-date2: 첫번째 감면기간 date3-date4: 두번째 감면기간
    data = [date1, date2, date3, date4]
    if len(data) == 4:
        if tax_year == 2019: #2019 outcome_tax
            minus_start = datetime.strptime(date2, "%Y-%m-%d")
            minus_finish = datetime.strptime(date3, "%Y-%m-%d")
            minus = minus_finish - minus_start
        return minus
    else:
        minus = 100000
        return minus
    
def youth_day_discount_func(tax_year, outcome_tax, minus):
    if minus == 10000:
        return outcome_tax
    else:
        outcome_tax = outcome_tax*((365 - minus)/365)
        return outcome_tax
    

def youth_day_discount_func(tax_year, outcome_tax, minus1, minus2):
    company_year = minus1 + minus2
    outcome_tax = outcome_tax * (company_year/365)
    return outcome_tax 