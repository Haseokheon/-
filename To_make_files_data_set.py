import make_template_to_str
#---------------------------- 청년 경정청구 필요한 값
def tax_decision_data_youth(bank_name,bank_srial_name,name_data,serial_name_data,address,pdf_extract_array,caculated_array,check_time_split):
    #배열 초기화 필요
    tax_decision_array = []
    tax_decision_location_array = []
    tax_decision_page_array = []
    """과세 표준 및 세액의 결정 청구서(청년)"""
    #이름
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (175, 120)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    tax_decision_array.append(c_serial_name)
    c_serial_name_location = (235, 135)
    tax_decision_location_array.append(c_serial_name_location)
    tax_decision_page_array.append(0)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[2]
    tax_decision_array.append(c_c_serial_num)
    c_c_serial_num_location = (400, 135)
    tax_decision_location_array.append(c_c_serial_num_location)
    tax_decision_page_array.append(0)

    #주소
    c_address = address
    tax_decision_array.append(c_address)
    c_address_location = (175, 155)
    tax_decision_location_array.append(c_address_location)
    tax_decision_page_array.append(0)

    #전화번호
    c_p_num = "070-4286-8075"
    tax_decision_array.append(c_p_num)
    c_p_num_location = (455, 161)
    tax_decision_location_array.append(c_p_num_location)
    tax_decision_page_array.append(0)

    #법정신고일 / 최초 신고일 (월은 5/31일 고정 연도만 변경)
    l_date = str(pdf_extract_array[0])+"-05-31"
    tax_decision_array.append(l_date)
    l_date_location = (180, 217)
    tax_decision_location_array.append(l_date_location)
    tax_decision_page_array.append(0)

    f_date = str(pdf_extract_array[0])+"-05-31"
    tax_decision_array.append(f_date)
    f_date_location = (430, 217)
    tax_decision_location_array.append(f_date_location)
    tax_decision_page_array.append(0)
    #경정 청구 이유
    tax_payback_reason = "중소기업 취업청년에 대한 소득세 감면 (조특법$30)"
    tax_decision_array.append(tax_payback_reason)
    tax_payback_reason_location = (180, 235)
    tax_decision_location_array.append(tax_payback_reason_location)
    tax_decision_page_array.append(0)

    #구분 (최초 신고 / 경정(결정)청구)
    #과세표준금액(이전/이후)
    origin_taxable_income = pdf_extract_array[4]
    tax_decision_array.append(origin_taxable_income)
    origin_taxable_income_location = (220, 286)
    tax_decision_location_array.append(origin_taxable_income_location)
    tax_decision_page_array.append(0)

    taxable_income_change = caculated_array[1]
    tax_decision_array.append(taxable_income_change)
    taxable_income_change_location = (410, 286)
    tax_decision_location_array.append(taxable_income_change_location)
    tax_decision_page_array.append(0)

    #산출세액(이전/이후)
    origin_c_tax = pdf_extract_array[6]
    tax_decision_array.append(origin_c_tax)
    origin_c_tax_location = (220, 302)
    tax_decision_location_array.append(origin_c_tax_location)
    tax_decision_page_array.append(0)

    c_tax = caculated_array[2]
    tax_decision_array.append(c_tax)
    c_tax_location = (410, 302)
    tax_decision_location_array.append(c_tax_location)
    tax_decision_page_array.append(0)

    #공제 및 감면세액(이전/이후)
    if caculated_array[9] == 1:
        origin_decision_tax = pdf_extract_array[7] + 130000
    else:
        origin_decision_tax = pdf_extract_array[7] 
    
    tax_decision_array.append(origin_decision_tax)
    origin_decision_tax_location = (220, 336)
    tax_decision_location_array.append(origin_decision_tax_location)
    tax_decision_page_array.append(0)

    if caculated_array[9] == 1:
        decision_tax = caculated_array[4] + 130000
    else:
        decision_tax = caculated_array[4]

    tax_decision_array.append(decision_tax)
    decision_tax_location = (410, 336)
    tax_decision_location_array.append(decision_tax_location)
    tax_decision_page_array.append(0)

    #납부할세액(이후만)
    minus_value = caculated_array[6]
    tax_decision_array.append(minus_value)
    minus_value_location = (410, 352)
    tax_decision_location_array.append(minus_value_location)
    tax_decision_page_array.append(0)

    #국세 환급금 계좌신고 (은행 이름, 계좌번호)
    bank = bank_name
    tax_decision_array.append(bank)
    bank_location = (235, 370)
    tax_decision_location_array.append(bank_location)
    tax_decision_page_array.append(0)

    bank_num = bank_srial_name
    tax_decision_array.append(bank_num)
    bank_num_location = (410, 370)
    tax_decision_location_array.append(bank_num_location)
    tax_decision_page_array.append(0)

    #환급받을세액
    to_refund_money = caculated_array[0]
    tax_decision_array.append(to_refund_money)
    to_refund_money_location = (410, 387)
    tax_decision_location_array.append(to_refund_money_location)
    tax_decision_page_array.append(0)

    #스캔일 (파일을 넣는 기준으로 스캔일 생성)
    scan_time_year = check_time_split[0]
    tax_decision_array.append(scan_time_year)
    scan_time_year_location = (440, 428)
    tax_decision_location_array.append(scan_time_year_location)
    tax_decision_page_array.append(0)

    scan_time_month = check_time_split[1]
    tax_decision_array.append(scan_time_month)
    scan_time_month_location = (480, 428)
    tax_decision_location_array.append(scan_time_month_location)
    tax_decision_page_array.append(0)

    scan_time_date = check_time_split[2]
    tax_decision_array.append(scan_time_date)
    scan_time_date_location = (505, 430)
    tax_decision_location_array.append(scan_time_date_location)
    tax_decision_page_array.append(0)

    #이름
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (345, 445)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)

    #위임자
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (360, 530)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)

    return tax_decision_array, tax_decision_location_array, tax_decision_page_array

def payment_caculation_data_youth(name_data,serial_name_data,family_num,address,pdf_extract_array,caculated_array,check_time_split):
    #배열 초기화 필요
    payment_caculation_array = []
    payment_caculation_location_array = []
    payment_caculation_page_array = []
    """종합소득세, 농어촌특별세 과세표준확정신고 및 납부 계산서(청년)"""
    """1쪽"""
    #연도
    year = pdf_extract_array[0]
    payment_caculation_array.append(year)
    year_location = (175, 105)
    payment_caculation_location_array.append(year_location)
    payment_caculation_page_array.append(0)

    #성명
    c_name = name_data[0]
    payment_caculation_array.append(c_name)
    c_name_location = (95, 176)
    payment_caculation_location_array.append(c_name_location)
    payment_caculation_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    payment_caculation_array.append(c_serial_name)
    c_serial_name_location = (350, 177)
    payment_caculation_location_array.append(c_serial_name_location)
    payment_caculation_page_array.append(0)

    #주소
    c_address = address
    payment_caculation_array.append(c_address)
    c_address_location = (100, 190)
    payment_caculation_location_array.append(c_address_location)
    payment_caculation_page_array.append(0)

    #주소지 전화번호
    c_p_num = "070-4286-8075"
    payment_caculation_array.append(c_p_num)
    c_p_num_location = (160, 207)
    payment_caculation_location_array.append(c_p_num_location)
    payment_caculation_page_array.append(0)

    #사업장 전화번호
    c_p_num = "070-4286-8075"
    payment_caculation_array.append(c_p_num)
    c_p_num_location = (400, 207)
    payment_caculation_location_array.append(c_p_num_location)
    payment_caculation_page_array.append(0)

    #세액의 계산 (추가 필요)
    #종합소득금액19
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (280, 363)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(0)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (280, 370)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(0)

    #소득공제20
    payment_deducation = 1500000 + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation)
    payment_deducation_location = (280, 377)
    payment_caculation_location_array.append(payment_deducation_location)
    payment_caculation_page_array.append(0)

    payment_deducation = 1500000 + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation)
    payment_deducation_location = (280, 385)
    payment_caculation_location_array.append(payment_deducation_location)
    payment_caculation_page_array.append(0)

    #과세표준21
    origin_taxable_income = pdf_extract_array[4]
    payment_caculation_array.append(origin_taxable_income)
    origin_taxable_income_location = (280, 390)
    payment_caculation_location_array.append(origin_taxable_income_location)
    payment_caculation_page_array.append(0)

    taxable_income = caculated_array[1]
    payment_caculation_array.append(taxable_income)
    taxable_income_location = (280, 395)
    payment_caculation_location_array.append(taxable_income_location)
    payment_caculation_page_array.append(0)

    #세율22
    percentage = caculated_array[3]
    payment_caculation_array.append(percentage)
    percentage_location = (280, 404)
    payment_caculation_location_array.append(percentage_location)
    payment_caculation_page_array.append(0)

    percentage = caculated_array[3]
    payment_caculation_array.append(percentage)
    percentage_location = (280, 411)
    payment_caculation_location_array.append(percentage_location)
    payment_caculation_page_array.append(0)

    #산출세액23
    origin_c_tax = pdf_extract_array[6]
    payment_caculation_array.append(origin_c_tax)
    origin_c_tax_location = (279, 419)
    payment_caculation_location_array.append(origin_c_tax_location)
    payment_caculation_page_array.append(0)

    c_tax = caculated_array[2]
    payment_caculation_array.append(c_tax)
    c_tax_location = (280, 423)
    payment_caculation_location_array.append(c_tax_location)
    payment_caculation_page_array.append(0)

    #세액감면24
    youth_discount = caculated_array[8]
    payment_caculation_array.append(youth_discount)
    youth_discount_location = (280, 438)
    payment_caculation_location_array.append(youth_discount_location)
    payment_caculation_page_array.append(0)

    #세액공제25
    if caculated_array[9] ==1:
        origin_payment_tax = pdf_extract_array[7] + pdf_extract_array[11]+ 130000
    else:
        origin_payment_tax = pdf_extract_array[7] + pdf_extract_array[11]

    payment_caculation_array.append(origin_payment_tax)
    origin_payment_tax_location = (280, 445)
    payment_caculation_location_array.append(origin_payment_tax_location)
    payment_caculation_page_array.append(0)

    if caculated_array[9] == 1:
        payment_tax = caculated_array[4] + pdf_extract_array[11] + 130000
    else:
        payment_tax = caculated_array[4] + pdf_extract_array[11]

    payment_caculation_array.append(payment_tax)
    payment_tax_location = (280, 450)
    payment_caculation_location_array.append(payment_tax_location)
    payment_caculation_page_array.append(0)

    #종합과세26 (23 -24 -25)
    origin_total_tax = origin_c_tax - origin_payment_tax
    payment_caculation_array.append(origin_total_tax)
    origin_total_tax_location = (280, 460)
    payment_caculation_location_array.append(origin_total_tax_location)
    payment_caculation_page_array.append(0)

    total_tax = c_tax - youth_discount - payment_tax
    payment_caculation_array.append(total_tax)
    total_tax_location = (280, 465)
    payment_caculation_location_array.append(total_tax_location)
    payment_caculation_page_array.append(0)

    #합계28
    origin_total_1 = origin_total_tax
    payment_caculation_array.append(origin_total_1)
    origin_total_1_location = (280, 487)
    payment_caculation_location_array.append(origin_total_1_location)
    payment_caculation_page_array.append(0)

    total_1 = total_tax
    payment_caculation_array.append(total_1)
    total_1_location = (280, 492)
    payment_caculation_location_array.append(total_1_location)
    payment_caculation_page_array.append(0)

    #합계31 (28+29+30)
    origin_total_2 = origin_total_1
    payment_caculation_array.append(origin_total_2)
    origin_total_2_location = (280, 534)
    payment_caculation_location_array.append(origin_total_2_location)
    payment_caculation_page_array.append(0)

    total_2 = total_1
    payment_caculation_array.append(total_2)
    total_2_location = (280, 541)
    payment_caculation_location_array.append(total_2_location)
    payment_caculation_page_array.append(0)

    #기납부세액32
    origin_prepayment = origin_total_1
    payment_caculation_array.append(origin_prepayment)
    origin_prepayment_location = (280, 549)
    payment_caculation_location_array.append(origin_prepayment_location)
    payment_caculation_page_array.append(0)

    prepayment = origin_total_1
    payment_caculation_array.append(prepayment)
    prepayment_location = (280, 554)
    payment_caculation_location_array.append(prepayment_location)
    payment_caculation_page_array.append(0)

    #납부할총세액33
    minus_data = caculated_array[0]
    payment_caculation_array.append(minus_data)
    minus_data_location = (280, 568)
    payment_caculation_location_array.append(minus_data_location)
    payment_caculation_page_array.append(0)

    #신고기한이내납부할세액
    minus_data = caculated_array[0]
    payment_caculation_array.append(minus_data)
    minus_data_location = (280, 621)
    payment_caculation_location_array.append(minus_data_location)
    payment_caculation_page_array.append(0)

    #충당후 납부할 세액
    #to_refund_tax = caculated_array[6]
    #payment_caculation_array.append(to_refund_tax)
    #to_refund_tax_location = (280, 649)
    #payment_caculation_location_array.append(to_refund_tax_location)
    #payment_caculation_page_array.append(0)

    #스캔일 (파일을 넣는 기준으로 스캔일 생성)
    scan_time_year = check_time_split[0]
    payment_caculation_array.append(scan_time_year)
    scan_time_year_location = (190, 702)
    payment_caculation_location_array.append(scan_time_year_location)
    payment_caculation_page_array.append(0)

    scan_time_month = check_time_split[1]
    payment_caculation_array.append(scan_time_month)
    scan_time_month_location = (238, 702)
    payment_caculation_location_array.append(scan_time_month_location)
    payment_caculation_page_array.append(0)

    scan_time_day = check_time_split[2]
    payment_caculation_array.append(scan_time_day)
    scan_time_day_location = (271, 702)
    payment_caculation_location_array.append(scan_time_day_location)
    payment_caculation_page_array.append(0)

    #이름
    s_name = name_data[0]
    payment_caculation_array.append(s_name)
    s_name_location = (360, 702)
    payment_caculation_location_array.append(s_name_location)
    payment_caculation_page_array.append(0)

    """2쪽"""
    #소득 구분 코드
    income_s_code = "51"
    payment_caculation_array.append(income_s_code)
    income_s_code_location = (40, 200)
    payment_caculation_location_array.append(income_s_code_location)
    payment_caculation_page_array.append(1)

    income_s_code = "51"
    payment_caculation_array.append(income_s_code)
    income_s_code_location = (40, 225)
    payment_caculation_location_array.append(income_s_code_location)
    payment_caculation_page_array.append(1)

    #일련 번호
    s_code = "1"
    payment_caculation_array.append(s_code)
    s_code_location = (70, 200)
    payment_caculation_location_array.append(s_code_location)
    payment_caculation_page_array.append(1)

    s_code = "1"
    payment_caculation_array.append(s_code)
    s_code_location = (70, 225)
    payment_caculation_location_array.append(s_code_location)
    payment_caculation_page_array.append(1)

    #상호
    c_c_name = pdf_extract_array[0]
    payment_caculation_array.append(c_c_name)
    c_c_name_location = (95, 195)
    payment_caculation_location_array.append(c_c_name_location)
    payment_caculation_page_array.append(1)

    c_c_name = pdf_extract_array[0]
    payment_caculation_array.append(c_c_name)
    c_c_name_location = (95, 222)
    payment_caculation_location_array.append(c_c_name_location)
    payment_caculation_page_array.append(1)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[1]
    payment_caculation_array.append(c_c_serial_num)
    c_c_serial_num_location = (115, 207)
    payment_caculation_location_array.append(c_c_serial_num_location)
    payment_caculation_page_array.append(1)

    c_c_serial_num = pdf_extract_array[1]
    payment_caculation_array.append(c_c_serial_num)
    c_c_serial_num_location = (115, 235)
    payment_caculation_location_array.append(c_c_serial_num_location)
    payment_caculation_page_array.append(1)

    #총수입금액
    total_salary = pdf_extract_array[3]
    payment_caculation_array.append(total_salary)
    total_salary_location = (205, 200)
    payment_caculation_location_array.append(total_salary_location)
    payment_caculation_page_array.append(1)

    total_salary = pdf_extract_array[3]
    payment_caculation_array.append(total_salary)
    total_salary_location = (205, 230)
    payment_caculation_location_array.append(total_salary_location)
    payment_caculation_page_array.append(1)

    #필요경비
    expenses = pdf_extract_array[3] - pdf_extract_array[5]
    payment_caculation_array.append(expenses)
    expenses_location = (280, 200)
    payment_caculation_location_array.append(expenses_location)
    payment_caculation_page_array.append(1)

    expenses = pdf_extract_array[3] - pdf_extract_array[5]
    payment_caculation_array.append(expenses)
    expenses_location = (280, 230)
    payment_caculation_location_array.append(expenses_location)
    payment_caculation_page_array.append(1)

    #소득금액
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (350, 200)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(1)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (350, 230)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(1)

    #소득세
    origin_final_tax_change = pdf_extract_array[13]
    payment_caculation_array.append(origin_final_tax_change)
    origin_final_tax_change_location = (425, 200)
    payment_caculation_location_array.append(origin_final_tax_change_location)
    payment_caculation_page_array.append(1)

    final_tax_change = caculated_array[5]
    payment_caculation_array.append(final_tax_change)
    final_tax_change_location = (425, 230)
    payment_caculation_location_array.append(final_tax_change_location)
    payment_caculation_page_array.append(1)

    """3쪽"""
    #근로소득금액, 합계 (1,5)
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 315)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 325)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 315)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money =  pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 325)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 385)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money =  pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 395)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 385)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money =  pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 395)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    """4쪽"""
    #인적공제
    if family_num >= 1:
        self_value = 1500000
        payment_caculation_array.append(self_value)
        self_value_location = (225, 178)
        payment_caculation_location_array.append(self_value_location)
        payment_caculation_page_array.append(3)

        self_value = 1500000
        payment_caculation_array.append(self_value)
        self_value_location = (225, 190)
        payment_caculation_location_array.append(self_value_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        spoonse_value = 1500000
        payment_caculation_array.append(spoonse_value)
        spoonse_value_location = (225, 215)
        payment_caculation_location_array.append(spoonse_value_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:    
        dependents_num = family_num - 2
        payment_caculation_array.append(dependents_num)
        dependents_num_location = (225, 229)
        payment_caculation_location_array.append(dependents_num_location)
        payment_caculation_page_array.append(3)

        dependents_value = 1500000 * dependents_num
        payment_caculation_array.append(dependents_value)
        dependents_value_location = (225, 240)
        payment_caculation_location_array.append(dependents_value_location)
        payment_caculation_page_array.append(3)

    #인적공제계
    family_value = 1500000
    payment_caculation_array.append(family_value)
    family_value_location =(225, 358)
    payment_caculation_location_array.append(family_value_location)
    payment_caculation_page_array.append(3)

    family_value = family_num * 1500000
    payment_caculation_array.append(family_value)
    family_value_location = (225, 370)
    payment_caculation_location_array.append(family_value_location)
    payment_caculation_page_array.append(3)

    #국민연금
    person_insurance = pdf_extract_array[8]
    payment_caculation_array.append(person_insurance)
    person_insurance_location = (475, 178)
    payment_caculation_location_array.append(person_insurance_location)
    payment_caculation_page_array.append(3)

    person_insurance = pdf_extract_array[8]
    payment_caculation_array.append(person_insurance)
    person_insurance_location = (475, 190)
    payment_caculation_location_array.append(person_insurance_location)
    payment_caculation_page_array.append(3)

    #보험료 공제
    health_insurance = pdf_extract_array[9]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 254)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    health_insurance = pdf_extract_array[9]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 265)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    #근로소득이 있는 자
    health_insurance = pdf_extract_array[10]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 331)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    health_insurance = pdf_extract_array[10]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 341)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    #인적공제대상자명세
    #관계
    if family_num >= 1:
        s1_relationship = 0
        payment_caculation_array.append(s1_relationship)
        s1_relationship_location = (40, 430)
        payment_caculation_location_array.append(s1_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        s2_relationship = 3
        payment_caculation_array.append(s2_relationship)
        s2_relationship_location = (40, 448)
        payment_caculation_location_array.append(s2_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        s3_relationship = 4
        payment_caculation_array.append(s3_relationship)
        s3_relationship_location = (40, 466)
        payment_caculation_location_array.append(s3_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        s4_relationship = 4
        payment_caculation_array.append(s4_relationship)
        s4_relationship_location = (40, 485)
        payment_caculation_location_array.append(s4_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        s5_relationship = 4
        payment_caculation_array.append(s5_relationship)
        s5_relationship_location = (300, 430)
        payment_caculation_location_array.append(s5_relationship_location)
        payment_caculation_page_array.append(3)

    #성명
    if family_num >= 1:
        s1_name = name_data[0]
        payment_caculation_array.append(s1_name)
        s1_name_location = (65, 430)
        payment_caculation_location_array.append(s1_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        s2_name = name_data[1]
        payment_caculation_array.append(s2_name)
        s2_name_location = (65, 448)
        payment_caculation_location_array.append(s2_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        s3_name = name_data[2]
        payment_caculation_array.append(s3_name)
        s3_name_location = (65, 466)
        payment_caculation_location_array.append(s3_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        s4_name = name_data[3]
        payment_caculation_array.append(s4_name)
        s4_name_location = (65, 485)
        payment_caculation_location_array.append(s4_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        s5_name = name_data[4]
        payment_caculation_array.append(s5_name)
        s5_name_location = (325, 430)
        payment_caculation_location_array.append(s5_name_location)
        payment_caculation_page_array.append(3)

    #내외국인
    if family_num >= 1:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 430)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 448)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 466)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 485)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (385, 430)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    #주민등록번호(외국인등록번호)
    if family_num >= 1:
        c1_serial_name = serial_name_data[0]
        payment_caculation_array.append(c1_serial_name)
        c1_serial_name_location = (145, 430)
        payment_caculation_location_array.append(c1_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        c2_serial_name = serial_name_data[1]
        payment_caculation_array.append(c2_serial_name)
        c2_serial_name_location = (145, 448)
        payment_caculation_location_array.append(c2_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        c3_serial_name = serial_name_data[2]
        payment_caculation_array.append(c3_serial_name)
        c3_serial_name_location = (145, 466)
        payment_caculation_location_array.append(c3_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        c4_serial_name = serial_name_data[3]
        payment_caculation_array.append(c4_serial_name)
        c4_serial_name_location = (145, 485)
        payment_caculation_location_array.append(c4_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        c5_serial_name = serial_name_data[4]
        payment_caculation_array.append(c5_serial_name)
        c5_serial_name_location = (405, 430)
        payment_caculation_location_array.append(c5_serial_name_location)
        payment_caculation_page_array.append(3)
        
    #소득공제 합계(인적공제계 + 국민연금 + 특별공제합계)
    payment_deducation_sum = 150000 + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation_sum)
    payment_deducation_sum_location = (190, 720)
    payment_caculation_location_array.append(payment_deducation_sum_location)
    payment_caculation_page_array.append(3)

    payment_deducation_sum = 150000*family_num + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation_sum)
    payment_deducation_sum_location = (190, 732)
    payment_caculation_location_array.append(payment_deducation_sum_location)
    payment_caculation_page_array.append(3)

    """5쪽"""
    #중소기업 취업 청년에 대한 감면
    tax_reason = "중소기업 취업 청년에 대한 감면"
    payment_caculation_array.append(tax_reason)
    tax_reason_location = (40, 113)
    payment_caculation_location_array.append(tax_reason_location)
    payment_caculation_page_array.append(4)

    #코드
    tax_code = 347 
    payment_caculation_array.append(tax_code)
    tax_code_location = (260, 113)
    payment_caculation_location_array.append(tax_code_location)
    payment_caculation_page_array.append(4)

    #세액감면
    youth_discount = caculated_array[8]
    payment_caculation_array.append(youth_discount)
    youth_discount_location = (310, 113)
    payment_caculation_location_array.append(youth_discount_location)
    payment_caculation_page_array.append(4)

    #세액감면 합계
    youth_discount = caculated_array[8]
    payment_caculation_array.append(youth_discount)
    youth_discount_location = (310, 176)
    payment_caculation_location_array.append(youth_discount_location)
    payment_caculation_page_array.append(4)

    #근로소득세액공제(이전 이후)
    origin_payment_tax = pdf_extract_array[7]
    payment_caculation_array.append(origin_payment_tax)
    origin_payment_tax_location = (405, 314)
    payment_caculation_location_array.append(origin_payment_tax_location)
    payment_caculation_page_array.append(4)

    payment_tax = caculated_array[4]
    payment_caculation_array.append(payment_tax)
    payment_tax_location = (405, 320)
    payment_caculation_location_array.append(payment_tax_location)
    payment_caculation_page_array.append(4)

    #표준세액공제
    if caculated_array[9] == 1:
        standard_tax_deducate = 130000
    else:
        standard_tax_deducate = 0
        payment_caculation_array.append(standard_tax_deducate)
        standard_tax_deducate_location = (405, 499)
        payment_caculation_location_array.append(standard_tax_deducate_location)
        payment_caculation_page_array.append(4)

    #월세 세액공제
    month_name = "월세세액공제"
    payment_caculation_array.append(month_name)
    month_name_location = (50, 595)
    payment_caculation_location_array.append(month_name_location)
    payment_caculation_page_array.append(4)

    #월세액 금액
    month_tax = pdf_extract_array[11]
    payment_caculation_array.append(month_tax)
    month_tax_location = (405, 595)
    payment_caculation_location_array.append(month_tax_location)
    payment_caculation_page_array.append(4)

    #세액공제합계(이전 이후)
    if caculated_array[9] == 1:
        origin_tax_deducate = origin_payment_tax + month_tax + 130000
    else:
        origin_tax_deducate = origin_payment_tax + month_tax

    payment_caculation_array.append(origin_tax_deducate)
    origin_tax_deducate_location = (405, 647)
    payment_caculation_location_array.append(origin_tax_deducate_location)
    payment_caculation_page_array.append(4)

    if caculated_array[9] == 1:
        tax_deducate = payment_tax + month_tax + 130000
    else:
        tax_deducate = payment_tax + month_tax 
    payment_caculation_array.append(tax_deducate)
    decision_tax_location = (405, 654)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(4)

    """6쪽"""
    #원천징수세액 및 납세조합징수세액 (근로소득)
    decision_tax = pdf_extract_array[13]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 764)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    decision_tax = caculated_array[5]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 769)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    #기납부세액 합계
    decision_tax = pdf_extract_array[13]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 809)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    decision_tax = pdf_extract_array[5]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 814)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    return payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array

def income_tax_exemption_data_youth(name_data,serial_name_data,country_name,address,pdf_extract_array,check_time_split,year_date):
    #배열 초기화 필요, ui 연결
    income_tax_exemption_array = []
    income_tax_exemption_location_array = []
    income_tax_exemption_page_array = []
    """소득 세액 공제신고서/근로자소득자 소득 세액 공제신고서 (청년)"""
    """1쪽"""
    #연도
    year = pdf_extract_array[0]
    income_tax_exemption_array.append(year)
    year_location = (378, 92)
    income_tax_exemption_location_array.append(year_location)
    income_tax_exemption_page_array.append(0)

    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (169, 167)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (434, 167)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(0)

    #근무처
    c_c_name = pdf_extract_array[1]
    income_tax_exemption_array.append(c_c_name)
    c_c_name_location = (169, 189)
    income_tax_exemption_location_array.append(c_c_name_location)
    income_tax_exemption_page_array.append(0)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[2]
    income_tax_exemption_array.append(c_c_serial_num)
    c_c_serial_num_location = (434, 189)
    income_tax_exemption_location_array.append(c_c_serial_num_location)
    income_tax_exemption_page_array.append(0)

    #국적 및 국적코드(UI/UX)
    country = country_name[0]
    income_tax_exemption_array.append(country)
    country_location = (410, 206)
    income_tax_exemption_location_array.append(country_location)
    income_tax_exemption_page_array.append(0)

    country_code = country_name[1]
    income_tax_exemption_array.append(country_code)
    country_code_location = (516, 207)
    income_tax_exemption_location_array.append(country_code_location)
    income_tax_exemption_page_array.append(0)

    #근무기간
    w_s_time = str(pdf_extract_array[0])+".01.01"
    income_tax_exemption_array.append(w_s_time)
    w_s_time_location = (151, 226)
    income_tax_exemption_location_array.append(w_s_time_location)
    income_tax_exemption_page_array.append(0)

    w_e_time = str(pdf_extract_array[0])+"12.31"
    income_tax_exemption_array.append(w_e_time)
    w_e_time_location = (245, 226)
    income_tax_exemption_location_array.append(w_e_time_location)
    income_tax_exemption_page_array.append(0)

    #감면기간
    d_s_time = str(pdf_extract_array[0])+".01.01"
    income_tax_exemption_array.append(d_s_time)
    d_s_time_location = (398, 226)
    income_tax_exemption_location_array.append(d_s_time_location)
    income_tax_exemption_page_array.append(0)

    d_e_time = str(pdf_extract_array[0])+"12.31"
    income_tax_exemption_array.append(d_e_time)
    d_e_time_location = (482, 226)
    income_tax_exemption_location_array.append(d_e_time_location)
    income_tax_exemption_page_array.append(0)

    """2쪽"""
    #국민연금보험료
    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (389, 106)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (504, 106)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    #국민연금보험료 계
    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (389, 142)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (504, 142)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    #국민건강보험료
    health_insurance = pdf_extract_array[9]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (389, 166)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    health_insurance = pdf_extract_array[9]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (504, 166)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    """#고용 보험료"""
    





    #보험료 계
    health_insurance = pdf_extract_array[10]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (389, 201)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    health_insurance = pdf_extract_array[10]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (504, 201)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    """3쪽"""
    #취업일 및 감면기간 종료일(UI/UX)
    year_date_start = year_date[0]
    income_tax_exemption_array.append(year_date_start)
    year_date_start_location = (329, 167)
    income_tax_exemption_location_array.append(year_date_start_location)
    income_tax_exemption_page_array.append(2)

    year_date_end = year_date[1]
    income_tax_exemption_array.append(year_date_end)
    year_date_end_location = (484, 167)
    income_tax_exemption_location_array.append(year_date_end_location)
    income_tax_exemption_page_array.append(2)

    #스캔일
    scan_time_year = check_time_split[0]
    income_tax_exemption_array.append(scan_time_year)
    scan_time_year_location = (481, 605)
    income_tax_exemption_location_array.append(scan_time_year_location)
    income_tax_exemption_page_array.append(2)

    scan_time_month = check_time_split[1]
    income_tax_exemption_array.append(scan_time_month)
    scan_time_month_location = (512, 605)
    income_tax_exemption_location_array.append(scan_time_month_location)
    income_tax_exemption_page_array.append(2)

    scan_time_day = check_time_split[2]
    income_tax_exemption_array.append(scan_time_day)
    scan_time_day_location = (532, 605)
    income_tax_exemption_location_array.append(scan_time_day_location)
    income_tax_exemption_page_array.append(2)

    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (383, 616)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(2)

    """4쪽"""
    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (204, 123)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(3)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (446, 123)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(3)

    #주소
    c_address = address
    income_tax_exemption_array.append(c_address)
    c_address_location = (203, 145)
    income_tax_exemption_location_array.append(c_address_location)
    income_tax_exemption_page_array.append(3)

    """5쪽"""
    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (204, 141)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(4)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (460, 141)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(4)

    #주소
    c_address = address
    income_tax_exemption_array.append(c_address)
    c_address_location = (208, 168)
    income_tax_exemption_location_array.append(c_address_location)
    income_tax_exemption_page_array.append(4)

    #세액공제 금액(원)
    month_tax = pdf_extract_array[11]
    income_tax_exemption_array.append(month_tax)
    month_tax_location = (501, 287)
    income_tax_exemption_location_array.append(month_tax_location)
    income_tax_exemption_page_array.append(4)

    return income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array

"""------------------------------------------------------------------"""
def tax_decision_data_child(bank_name,bank_srial_name,name_data,serial_name_data,address,pdf_extract_array,caculated_array,check_time_split):
    #배열 초기화 필요
    tax_decision_array = []
    tax_decision_location_array = []
    tax_decision_page_array = []
    """과세 표준 및 세액의 결정 청구서(청년)"""
    #이름
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (175, 120)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    tax_decision_array.append(c_serial_name)
    c_serial_name_location = (235, 135)
    tax_decision_location_array.append(c_serial_name_location)
    tax_decision_page_array.append(0)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[2]
    tax_decision_array.append(c_c_serial_num)
    c_c_serial_num_location = (400, 135)
    tax_decision_location_array.append(c_c_serial_num_location)
    tax_decision_page_array.append(0)

    #주소
    c_address = address
    tax_decision_array.append(c_address)
    c_address_location = (175, 155)
    tax_decision_location_array.append(c_address_location)
    tax_decision_page_array.append(0)

    #전화번호
    c_p_num = "070-4286-8075"
    tax_decision_array.append(c_p_num)
    c_p_num_location = (455, 161)
    tax_decision_location_array.append(c_p_num_location)
    tax_decision_page_array.append(0)

    #법정신고일 / 최초 신고일 (월은 5/31일 고정 연도만 변경)
    l_date = str(pdf_extract_array[0])+"-05-31"
    tax_decision_array.append(l_date)
    l_date_location = (180, 217)
    tax_decision_location_array.append(l_date_location)
    tax_decision_page_array.append(0)

    f_date = str(pdf_extract_array[0])+"-05-31"
    tax_decision_array.append(f_date)
    f_date_location = (430, 217)
    tax_decision_location_array.append(f_date_location)
    tax_decision_page_array.append(0)

    #경정 청구 이유
    tax_payback_reason = "인적공제_기본공제_부양자공제 (소득법$50)"
    tax_decision_array.append(tax_payback_reason)
    tax_payback_reason_location = (180, 235)
    tax_decision_location_array.append(tax_payback_reason_location)
    tax_decision_page_array.append(0)

    #구분 (최초 신고 / 경정(결정)청구)
    #과세표준금액(이전/이후)
    origin_taxable_income = pdf_extract_array[4]
    tax_decision_array.append(origin_taxable_income)
    origin_taxable_income_location = (220, 286)
    tax_decision_location_array.append(origin_taxable_income_location)
    tax_decision_page_array.append(0)

    taxable_income_change = caculated_array[1]
    tax_decision_array.append(taxable_income_change)
    taxable_income_change_location = (410, 286)
    tax_decision_location_array.append(taxable_income_change_location)
    tax_decision_page_array.append(0)

    #산출세액(이전/이후)
    origin_c_tax = pdf_extract_array[6]
    tax_decision_array.append(origin_c_tax)
    origin_c_tax_location = (220, 302)
    tax_decision_location_array.append(origin_c_tax_location)
    tax_decision_page_array.append(0)

    c_tax = caculated_array[2]
    tax_decision_array.append(c_tax)
    c_tax_location = (410, 302)
    tax_decision_location_array.append(c_tax_location)
    tax_decision_page_array.append(0)

    #공제 및 감면세액(이전/이후)
    origin_decision_tax = pdf_extract_array[13]
    tax_decision_array.append(origin_decision_tax)
    origin_decision_tax_location = (220, 336)
    tax_decision_location_array.append(origin_decision_tax_location)
    tax_decision_page_array.append(0)

    decision_tax = caculated_array[5]
    tax_decision_array.append(decision_tax)
    decision_tax_location = (410, 336)
    tax_decision_location_array.append(decision_tax_location)
    tax_decision_page_array.append(0)

    #납부할세액(이후만)
    minus_value = caculated_array[6]
    tax_decision_array.append(minus_value)
    minus_value_location = (410, 352)
    tax_decision_location_array.append(minus_value_location)
    tax_decision_page_array.append(0)

    #국세 환급금 계좌신고 (은행 이름, 계좌번호)
    bank = bank_name
    tax_decision_array.append(bank)
    bank_location = (235, 370)
    tax_decision_location_array.append(bank_location)
    tax_decision_page_array.append(0)

    bank_num = bank_srial_name
    tax_decision_array.append(bank_num)
    bank_num_location = (410, 370)
    tax_decision_location_array.append(bank_num_location)
    tax_decision_page_array.append(0)

    #환급받을세액
    to_refund_money = caculated_array[0]
    tax_decision_array.append(to_refund_money)
    to_refund_money_location = (410, 387)
    tax_decision_location_array.append(to_refund_money_location)
    tax_decision_page_array.append(0)

    #스캔일 (파일을 넣는 기준으로 스캔일 생성)
    scan_time_year = check_time_split[0]
    tax_decision_array.append(scan_time_year)
    scan_time_year_location = (440, 428)
    tax_decision_location_array.append(scan_time_year_location)
    tax_decision_page_array.append(0)

    scan_time_month = check_time_split[1]
    tax_decision_array.append(scan_time_month)
    scan_time_month_location = (480, 428)
    tax_decision_location_array.append(scan_time_month_location)
    tax_decision_page_array.append(0)

    scan_time_date = check_time_split[2]
    tax_decision_array.append(scan_time_date)
    scan_time_date_location = (505, 430)
    tax_decision_location_array.append(scan_time_date_location)
    tax_decision_page_array.append(0)

    #이름
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (345, 445)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)

    #위임자
    c_name = name_data[0]
    tax_decision_array.append(c_name)
    c_name_location = (360, 530)
    tax_decision_location_array.append(c_name_location)
    tax_decision_page_array.append(0)
    
    return tax_decision_array, tax_decision_location_array, tax_decision_page_array

def payment_caculation_data_child(name_data,serial_name_data,family_num,address,pdf_extract_array,caculated_array,check_time_split):
    #배열 초기화 필요
    payment_caculation_array = []
    payment_caculation_location_array = []
    payment_caculation_page_array = []
    """종합소득세, 농어촌특별세 과세표준확정신고 및 납부 계산서(부양)"""
    """1쪽"""
    #연도
    year = pdf_extract_array[0]
    payment_caculation_array.append(year)
    year_location = (175, 105)
    payment_caculation_location_array.append(year_location)
    payment_caculation_page_array.append(0)

    #성명
    c_name = name_data[0]
    payment_caculation_array.append(c_name)
    c_name_location = (95, 176)
    payment_caculation_location_array.append(c_name_location)
    payment_caculation_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    payment_caculation_array.append(c_serial_name)
    c_serial_name_location = (350, 177)
    payment_caculation_location_array.append(c_serial_name_location)
    payment_caculation_page_array.append(0)

    #주소
    c_address = address
    payment_caculation_array.append(c_address)
    c_address_location = (100, 190)
    payment_caculation_location_array.append(c_address_location)
    payment_caculation_page_array.append(0)

    #주소지 전화번호
    c_p_num = "070-4286-8075"
    payment_caculation_array.append(c_p_num)
    c_p_num_location = (160, 207)
    payment_caculation_location_array.append(c_p_num_location)
    payment_caculation_page_array.append(0)

    #사업장 전화번호
    c_p_num = "070-4286-8075"
    payment_caculation_array.append(c_p_num)
    c_p_num_location = (400, 207)
    payment_caculation_location_array.append(c_p_num_location)
    payment_caculation_page_array.append(0)

    #세액의 계산 (추가 필요)
    #종합소득금액19
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (280, 363)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(0)

    payment_tax_money =  pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (280, 370)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(0)

    #소득공제20
    payment_deducation = 1500000 + pdf_extract_array[8] + pdf_extract_array[9]
    payment_caculation_array.append(payment_deducation)
    payment_deducation_location = (280, 377)
    payment_caculation_location_array.append(payment_deducation_location)
    payment_caculation_page_array.append(0)

    payment_deducation = 1500000*family_num + pdf_extract_array[8] + pdf_extract_array[9]
    payment_caculation_array.append(payment_deducation)
    payment_deducation_location = (280, 385)
    payment_caculation_location_array.append(payment_deducation_location)
    payment_caculation_page_array.append(0)

    #과세표준21
    origin_taxable_income = pdf_extract_array[4]
    payment_caculation_array.append(origin_taxable_income)
    origin_taxable_income_location = (280, 390)
    payment_caculation_location_array.append(origin_taxable_income_location)
    payment_caculation_page_array.append(0)

    taxable_income = caculated_array[1]
    payment_caculation_array.append(taxable_income)
    taxable_income_location = (280, 395)
    payment_caculation_location_array.append(taxable_income_location)
    payment_caculation_page_array.append(0)

    #세율22
    percentage = caculated_array[3]
    payment_caculation_array.append(percentage)
    percentage_location = (280, 404)
    payment_caculation_location_array.append(percentage_location)
    payment_caculation_page_array.append(0)

    percentage = caculated_array[3]
    payment_caculation_array.append(percentage)
    percentage_location = (280, 411)
    payment_caculation_location_array.append(percentage_location)
    payment_caculation_page_array.append(0)

    #산출세액23
    origin_c_tax = pdf_extract_array[6]
    payment_caculation_array.append(origin_c_tax)
    origin_c_tax_location = (280, 419)
    payment_caculation_location_array.append(origin_c_tax_location)
    payment_caculation_page_array.append(0)

    c_tax = caculated_array[2]
    payment_caculation_array.append(c_tax)
    c_tax_location = (280, 423)
    payment_caculation_location_array.append(c_tax_location)
    payment_caculation_page_array.append(0)

    #세액공제25
    origin_payment_tax = pdf_extract_array[7]
    payment_caculation_array.append(origin_payment_tax)
    origin_payment_tax_location = (280, 445)
    payment_caculation_location_array.append(origin_payment_tax_location)
    payment_caculation_page_array.append(0)

    payment_tax = caculated_array[4]
    payment_caculation_array.append(payment_tax)
    payment_tax_location = (280, 450)
    payment_caculation_location_array.append(payment_tax_location)
    payment_caculation_page_array.append(0)

    #종합과세26 (23 -24 -25)
    origin_total_tax = origin_c_tax - origin_payment_tax
    payment_caculation_array.append(origin_total_tax)
    origin_total_tax_location = (280, 460)
    payment_caculation_location_array.append(origin_total_tax_location)
    payment_caculation_page_array.append(0)

    total_tax = c_tax - youth_discount - payment_tax
    payment_caculation_array.append(total_tax)
    total_tax_location = (280, 465)
    payment_caculation_location_array.append(total_tax_location)
    payment_caculation_page_array.append(0)

    #합계28
    origin_total_1 = origin_total_tax
    payment_caculation_array.append(origin_total_1)
    origin_total_1_location = (280, 487)
    payment_caculation_location_array.append(origin_total_1_location)
    payment_caculation_page_array.append(0)

    total_1 = total_tax
    payment_caculation_array.append(total_1)
    total_1_location = (280, 492)
    payment_caculation_location_array.append(total_1_location)
    payment_caculation_page_array.append(0)

    #합계31 (28+29+30)
    origin_total_2 = origin_total_1
    payment_caculation_array.append(origin_total_2)
    origin_total_2_location = (280, 534)
    payment_caculation_location_array.append(origin_total_2_location)
    payment_caculation_page_array.append(0)

    total_2 = total_1
    payment_caculation_array.append(total_2)
    total_2_location = (280, 541)
    payment_caculation_location_array.append(total_2_location)
    payment_caculation_page_array.append(0)

    #기납부세액32
    origin_prepayment = origin_total_1
    payment_caculation_array.append(origin_prepayment)
    origin_prepayment_location = (280, 549)
    payment_caculation_location_array.append(origin_prepayment_location)
    payment_caculation_page_array.append(0)

    prepayment = origin_total_1
    payment_caculation_array.append(prepayment)
    prepayment_location = (280, 554)
    payment_caculation_location_array.append(prepayment_location)
    payment_caculation_page_array.append(0)

    #납부할총세액33
    minus_data = caculated_array[6]
    payment_caculation_array.append(minus_data)
    minus_data_location = (280, 568)
    payment_caculation_location_array.append(minus_data_location)
    payment_caculation_page_array.append(0)

    #신고기한이내납부할세액
    minus_data = caculated_array[0]
    payment_caculation_array.append(minus_data)
    minus_data_location = (280, 621)
    payment_caculation_location_array.append(minus_data_location)
    payment_caculation_page_array.append(0)

    #충당후 납부할 세액
    to_refund_tax = caculated_array[0]
    payment_caculation_array.append(to_refund_tax)
    to_refund_tax_location = (280, 649)
    payment_caculation_location_array.append(to_refund_tax_location)
    payment_caculation_page_array.append(0)

    #스캔일 (파일을 넣는 기준으로 스캔일 생성)
    scan_time_year = check_time_split[0]
    payment_caculation_array.append(scan_time_year)
    scan_time_year_location = (190, 702)
    payment_caculation_location_array.append(scan_time_year_location)
    payment_caculation_page_array.append(0)

    scan_time_month = check_time_split[1]
    payment_caculation_array.append(scan_time_month)
    scan_time_month_location = (238, 702)
    payment_caculation_location_array.append(scan_time_month_location)
    payment_caculation_page_array.append(0)

    scan_time_day = check_time_split[2]
    payment_caculation_array.append(scan_time_day)
    scan_time_day_location = (271, 702)
    payment_caculation_location_array.append(scan_time_day_location)
    payment_caculation_page_array.append(0)

    #이름
    s_name = name_data[0]
    payment_caculation_array.append(s_name)
    s_name_location = (360, 702)
    payment_caculation_location_array.append(s_name_location)
    payment_caculation_page_array.append(0)

    """2쪽"""
    #소득 구분 코드
    income_s_code = "51"
    payment_caculation_array.append(income_s_code)
    income_s_code_location = (40, 200)
    payment_caculation_location_array.append(income_s_code_location)
    payment_caculation_page_array.append(1)

    income_s_code = "51"
    payment_caculation_array.append(income_s_code)
    income_s_code_location = (40, 225)
    payment_caculation_location_array.append(income_s_code_location)
    payment_caculation_page_array.append(1)

    #일련 번호
    s_code = "1"
    payment_caculation_array.append(s_code)
    s_code_location = (70, 200)
    payment_caculation_location_array.append(s_code_location)
    payment_caculation_page_array.append(1)

    s_code = "1"
    payment_caculation_array.append(s_code)
    s_code_location = (70, 225)
    payment_caculation_location_array.append(s_code_location)
    payment_caculation_page_array.append(1)

    #상호
    c_c_name = pdf_extract_array[1]
    payment_caculation_array.append(c_c_name)
    c_c_name_location = (95, 195)
    payment_caculation_location_array.append(c_c_name_location)
    payment_caculation_page_array.append(1)

    c_c_name = pdf_extract_array[1]
    payment_caculation_array.append(c_c_name)
    c_c_name_location = (95, 222)
    payment_caculation_location_array.append(c_c_name_location)
    payment_caculation_page_array.append(1)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[2]
    payment_caculation_array.append(c_c_serial_num)
    c_c_serial_num_location = (115, 207)
    payment_caculation_location_array.append(c_c_serial_num_location)
    payment_caculation_page_array.append(1)

    c_c_serial_num = pdf_extract_array[2]
    payment_caculation_array.append(c_c_serial_num)
    c_c_serial_num_location = (115, 235)
    payment_caculation_location_array.append(c_c_serial_num_location)
    payment_caculation_page_array.append(1)

    #총수입금액
    total_salary = pdf_extract_array[3]
    payment_caculation_array.append(total_salary)
    total_salary_location = (205, 200)
    payment_caculation_location_array.append(total_salary_location)
    payment_caculation_page_array.append(1)

    total_salary = pdf_extract_array[3]
    payment_caculation_array.append(total_salary)
    total_salary_location = (205, 230)
    payment_caculation_location_array.append(total_salary_location)
    payment_caculation_page_array.append(1)

    #필요경비
    expenses = pdf_extract_array[3] - pdf_extract_array[5]
    payment_caculation_array.append(expenses)
    expenses_location = (280, 200)
    payment_caculation_location_array.append(expenses_location)
    payment_caculation_page_array.append(1)

    expenses = pdf_extract_array[3] - pdf_extract_array[5]
    payment_caculation_array.append(expenses)
    expenses_location = (280, 230)
    payment_caculation_location_array.append(expenses_location)
    payment_caculation_page_array.append(1)

    #소득금액
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (350, 200)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(1)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (350, 230)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(1)

    #소득세
    origin_final_tax_change = pdf_extract_array[13]
    payment_caculation_array.append(origin_final_tax_change)
    origin_final_tax_change_location = (425, 200)
    payment_caculation_location_array.append(origin_final_tax_change_location)
    payment_caculation_page_array.append(1)

    final_tax_change = caculated_array[5]
    payment_caculation_array.append(final_tax_change)
    final_tax_change_location = (425, 230)
    payment_caculation_location_array.append(final_tax_change_location)
    payment_caculation_page_array.append(1)
    
    """3쪽"""
    #근로소득금액, 합계 (1,5)
    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 315)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 325)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 315)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 325)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 385)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (145, 395)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 385)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    payment_tax_money = pdf_extract_array[5]
    payment_caculation_array.append(payment_tax_money)
    payment_tax_money_location = (480, 395)
    payment_caculation_location_array.append(payment_tax_money_location)
    payment_caculation_page_array.append(2)

    #인적공제
    if family_num >= 1:
        self_value = 1500000
        payment_caculation_array.append(self_value)
        self_value_location = (225, 178)
        payment_caculation_location_array.append(self_value_location)
        payment_caculation_page_array.append(3)

        self_value = 1500000
        payment_caculation_array.append(self_value)
        self_value_location = (225, 190)
        payment_caculation_location_array.append(self_value_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        spoonse_value = 1500000
        payment_caculation_array.append(spoonse_value)
        spoonse_value_location = (225, 215)
        payment_caculation_location_array.append(spoonse_value_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:    
        dependents_num = family_num - 2
        payment_caculation_array.append(dependents_num)
        dependents_num_location = (165, 235)
        payment_caculation_location_array.append(dependents_num_location)
        payment_caculation_page_array.append(3)

        dependents_value = 1500000 * dependents_num
        payment_caculation_array.append(dependents_value)
        dependents_value_location = (225, 240)
        payment_caculation_location_array.append(dependents_value_location)
        payment_caculation_page_array.append(3)

    #인적공제계
    family_value = 1500000
    payment_caculation_array.append(family_value)
    family_value_location =(225, 358)
    payment_caculation_location_array.append(family_value_location)
    payment_caculation_page_array.append(3)

    family_value = family_num * 1500000
    payment_caculation_array.append(family_value)
    family_value_location = (225, 370)
    payment_caculation_location_array.append(family_value_location)
    payment_caculation_page_array.append(3)

    #국민연금
    person_insurance = pdf_extract_array[8]
    payment_caculation_array.append(person_insurance)
    person_insurance_location = (475, 178)
    payment_caculation_location_array.append(person_insurance_location)
    payment_caculation_page_array.append(3)

    person_insurance = pdf_extract_array[8]
    payment_caculation_array.append(person_insurance)
    person_insurance_location = (475, 190)
    payment_caculation_location_array.append(person_insurance_location)
    payment_caculation_page_array.append(3)

    #보험료 공제
    health_insurance = pdf_extract_array[9]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 254)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    health_insurance = pdf_extract_array[9]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 265)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    #근로소득이 있는 자
    health_insurance = pdf_extract_array[10]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 331)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    health_insurance = pdf_extract_array[10]
    payment_caculation_array.append(health_insurance)
    health_insurance_location = (475, 341)
    payment_caculation_location_array.append(health_insurance_location)
    payment_caculation_page_array.append(3)

    #인적공제대상자명세
    #관계
    if family_num >= 1:
        s1_relationship = 0
        payment_caculation_array.append(s1_relationship)
        s1_relationship_location = (40, 430)
        payment_caculation_location_array.append(s1_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        s2_relationship = 3
        payment_caculation_array.append(s2_relationship)
        s2_relationship_location = (40, 448)
        payment_caculation_location_array.append(s2_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        s3_relationship = 4
        payment_caculation_array.append(s3_relationship)
        s3_relationship_location = (40, 466)
        payment_caculation_location_array.append(s3_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        s4_relationship = 4
        payment_caculation_array.append(s4_relationship)
        s4_relationship_location = (40, 485)
        payment_caculation_location_array.append(s4_relationship_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        s5_relationship = 4
        payment_caculation_array.append(s5_relationship)
        s5_relationship_location = (300, 430)
        payment_caculation_location_array.append(s5_relationship_location)
        payment_caculation_page_array.append(3)

    #성명
    if family_num >= 1:
        s1_name = name_data[0]
        payment_caculation_array.append(s1_name)
        s1_name_location = (65, 430)
        payment_caculation_location_array.append(s1_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        s2_name = name_data[1]
        payment_caculation_array.append(s2_name)
        s2_name_location = (65, 448)
        payment_caculation_location_array.append(s2_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        s3_name = name_data[2]
        payment_caculation_array.append(s3_name)
        s3_name_location = (65, 466)
        payment_caculation_location_array.append(s3_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        s4_name = name_data[3]
        payment_caculation_array.append(s4_name)
        s4_name_location = (65, 485)
        payment_caculation_location_array.append(s4_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        s5_name = name_data[4]
        payment_caculation_array.append(s5_name)
        s5_name_location = (325, 430)
        payment_caculation_location_array.append(s5_name_location)
        payment_caculation_page_array.append(3)

    #내외국인
    if family_num >= 1:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 430)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 448)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 466)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (125, 485)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        foreign = 9
        payment_caculation_array.append(foreign)
        foreign_location = (385, 430)
        payment_caculation_location_array.append(foreign_location)
        payment_caculation_page_array.append(3)

    #주민등록번호(외국인등록번호)
    if family_num >= 1:
        c1_serial_name = serial_name_data[0]
        payment_caculation_array.append(c1_serial_name)
        c1_serial_name_location = (145, 430)
        payment_caculation_location_array.append(c1_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 2:
        c2_serial_name = serial_name_data[1]
        payment_caculation_array.append(c2_serial_name)
        c2_serial_name_location = (145, 448)
        payment_caculation_location_array.append(c2_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 3:
        c3_serial_name = serial_name_data[2]
        payment_caculation_array.append(c3_serial_name)
        c3_serial_name_location = (145, 466)
        payment_caculation_location_array.append(c3_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 4:
        c4_serial_name = serial_name_data[3]
        payment_caculation_array.append(c4_serial_name)
        c4_serial_name_location = (145, 485)
        payment_caculation_location_array.append(c4_serial_name_location)
        payment_caculation_page_array.append(3)

    if family_num >= 5:
        c5_serial_name = serial_name_data[4]
        payment_caculation_array.append(c5_serial_name)
        c5_serial_name_location = (405, 430)
        payment_caculation_location_array.append(c5_serial_name_location)
        payment_caculation_page_array.append(3)
        
    #소득공제 합계(인적공제계 + 국민연금 + 특별공제합계)
    payment_deducation_sum = family_value + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation_sum)
    payment_deducation_sum_location = (190, 720)
    payment_caculation_location_array.append(payment_deducation_sum_location)
    payment_caculation_page_array.append(3)

    payment_deducation_sum = family_value + pdf_extract_array[8] + pdf_extract_array[10]
    payment_caculation_array.append(payment_deducation_sum)
    payment_deducation_sum_location = (190, 732)
    payment_caculation_location_array.append(payment_deducation_sum_location)
    payment_caculation_page_array.append(3)

    """5쪽"""
    #세액감면 합계
    youth_discount = 0
    payment_caculation_array.append(youth_discount)
    youth_discount_location = (310, 176)
    payment_caculation_location_array.append(youth_discount_location)
    payment_caculation_page_array.append(4)

    #근로소득세액공제(이전 이후)
    origin_payment_tax = pdf_extract_array[7]
    payment_caculation_array.append(origin_payment_tax)
    origin_payment_tax_location = (405, 314)
    payment_caculation_location_array.append(origin_payment_tax_location)
    payment_caculation_page_array.append(4)

    payment_tax = caculated_array[4]
    payment_caculation_array.append(payment_tax)
    payment_tax_location = (405, 320)
    payment_caculation_location_array.append(payment_tax_location)
    payment_caculation_page_array.append(4)

    """#자녀 세액공제- 기본공제 자녀
    child_num = family_num -2
    payment_caculation_array.append(child_num)
    child_num_location = ()
    payment_caculation_location_array.append(child_num_location)
    payment_caculation_page_array.append(4)"""

    #자녀 세액공제 - 기본공제 자녀 금액
    child_discount = caculated_array[8]
    payment_caculation_array.append(child_discount)
    """child_discount_location = ()"""
    payment_caculation_location_array.append(child_discount_location)
    payment_caculation_page_array(4)

    #표준세액공제
    if caculated_array[9] == 1:
        standard_tax_deducate = 130000
        payment_caculation_array.append(standard_tax_deducate)
        standard_tax_deducate_location = (405, 499)
        payment_caculation_location_array.append(standard_tax_deducate_location)
        payment_caculation_page_array.append(4)

    #월세 세액공제
    month_name = "월세세액공제"
    payment_caculation_array.append(month_name)
    month_name_location = (50, 595)
    payment_caculation_location_array.append(month_name_location)
    payment_caculation_page_array.append(4)

    #월세액 금액
    month_tax = pdf_extract_array[11]
    payment_caculation_array.append(month_tax)
    month_tax_location = (405, 595)
    payment_caculation_location_array.append(month_tax_location)
    payment_caculation_page_array.append(4)

    #세액공제합계(이전 이후)
    origin_tax_deducate = origin_payment_tax + month_tax
    payment_caculation_array.append(origin_tax_deducate)
    origin_tax_deducate_location = (405, 647)
    payment_caculation_location_array.append(origin_tax_deducate_location)
    payment_caculation_page_array.append(4)

    if caculated_array[9] ==1:
        tax_deducate = payment_tax + month_tax + 130000
    else:
        tax_deducate = payment_tax + month_tax + 130000
    payment_caculation_array.append(tax_deducate)
    decision_tax_location = (405, 654)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(4)

    """6쪽"""
    #원천징수세액 및 납세조합징수세액 (근로소득)
    decision_tax = pdf_extract_array[13]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 764)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    decision_tax = pdf_extract_array[5]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 769)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    #기납부세액 합계
    decision_tax = pdf_extract_array[13]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 809)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    decision_tax = pdf_extract_array[5]
    payment_caculation_array.append(decision_tax)
    decision_tax_location = (320, 814)
    payment_caculation_location_array.append(decision_tax_location)
    payment_caculation_page_array.append(5)

    return payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array

def income_tax_exemption_data_child(name_data,serial_name_data,country_name,address,pdf_extract_array,check_time_split,year_date):
    #배열 초기화 필요
    income_tax_exemption_array = []
    income_tax_exemption_location_array = [] 
    income_tax_exemption_page_array = []
    """소득 세액 공제신고서/근로자소득자 소득 세액 공제신고서 (청년)"""
    """1쪽"""
    #연도
    year = pdf_extract_array[0]
    income_tax_exemption_array.append(year)
    year_location = (378, 92)
    income_tax_exemption_location_array.append(year_location)
    income_tax_exemption_page_array.append(0)

    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (169, 167)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(0)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (434, 167)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(0)

    #근무처
    c_c_name = pdf_extract_array[1]
    income_tax_exemption_array.append(c_c_name)
    c_c_name_location = (169, 189)
    income_tax_exemption_location_array.append(c_c_name_location)
    income_tax_exemption_page_array.append(0)

    #사업자등록번호
    c_c_serial_num = pdf_extract_array[2]
    income_tax_exemption_array.append(c_c_serial_num)
    c_c_serial_num_location = (434, 189)
    income_tax_exemption_location_array.append(c_c_serial_num_location)
    income_tax_exemption_page_array.append(0)

    #국적 및 국적코드(UI/UX)
    country = country_name[0]
    income_tax_exemption_array.append(country)
    country_location = (410, 206)
    income_tax_exemption_location_array.append(country_location)
    income_tax_exemption_page_array.append(0)

    country_code = country_name[1]
    income_tax_exemption_array.append(country_code)
    country_code_location = (516, 207)
    income_tax_exemption_location_array.append(country_code_location)
    income_tax_exemption_page_array.append(0)

    #근무기간
    w_s_time = str(pdf_extract_array[0])+".01.01"
    income_tax_exemption_array.append(w_s_time)
    w_s_time_location = (151, 226)
    income_tax_exemption_location_array.append(w_s_time_location)
    income_tax_exemption_page_array.append(0)

    w_e_time = str(pdf_extract_array[0])+"12.31"
    income_tax_exemption_array.append(w_e_time)
    w_e_time_location = (245, 226)
    income_tax_exemption_location_array.append(w_e_time_location)
    income_tax_exemption_page_array.append(0)

    #감면기간
    d_s_time = str(pdf_extract_array[0])+".01.01"
    income_tax_exemption_array.append(d_s_time)
    d_s_time_location = (398, 226)
    income_tax_exemption_location_array.append(d_s_time_location)
    income_tax_exemption_page_array.append(0)

    d_e_time = str(pdf_extract_array[0])+"12.31"
    income_tax_exemption_array.append(d_e_time)
    d_e_time_location = (482, 226)
    income_tax_exemption_location_array.append(d_e_time_location)
    income_tax_exemption_page_array.append(0)

    """2쪽"""
    #국민연금보험료
    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (389, 106)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (504, 106)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    #국민연금보험료 계
    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (389, 142)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    person_insurance = pdf_extract_array[8]
    income_tax_exemption_array.append(person_insurance)
    person_insurance_location = (504, 142)
    income_tax_exemption_location_array.append(person_insurance_location)
    income_tax_exemption_page_array.append(1)

    #국민건강보험료
    health_insurance = pdf_extract_array[9]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (389, 166)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    health_insurance = pdf_extract_array[9]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (504, 166)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    """#고용보험료"""



    #보험료 계
    health_insurance = pdf_extract_array[10]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (389, 201)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    health_insurance = pdf_extract_array[10]
    income_tax_exemption_array.append(health_insurance)
    health_insurance_location = (504, 201)
    income_tax_exemption_location_array.append(health_insurance_location)
    income_tax_exemption_page_array.append(1)

    """3쪽"""
    #취업일 및 감면기간 종료일(UI/UX)
    year_date_start = year_date[0]
    income_tax_exemption_array.append(year_date_start)
    year_date_start_location = (329, 167)
    income_tax_exemption_location_array.append(year_date_start_location)
    income_tax_exemption_page_array.append(2)

    year_date_end = year_date[1]
    income_tax_exemption_array.append(year_date_end)
    year_date_end_location = (484, 167)
    income_tax_exemption_location_array.append(year_date_end_location)
    income_tax_exemption_page_array.append(2)

    #스캔일
    scan_time_year = check_time_split[0]
    income_tax_exemption_array.append(scan_time_year)
    scan_time_year_location = (481, 605)
    income_tax_exemption_location_array.append(scan_time_year_location)
    income_tax_exemption_page_array.append(2)

    scan_time_month = check_time_split[1]
    income_tax_exemption_array.append(scan_time_month)
    scan_time_month_location = (512, 605)
    income_tax_exemption_location_array.append(scan_time_month_location)
    income_tax_exemption_page_array.append(2)

    scan_time_day = check_time_split[2]
    income_tax_exemption_array.append(scan_time_day)
    scan_time_day_location = (532, 605)
    income_tax_exemption_location_array.append(scan_time_day_location)
    income_tax_exemption_page_array.append(2)

    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (383, 616)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(2)

    """4쪽"""
    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (204, 123)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(3)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (446, 123)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(3)

    #주소
    c_address = address
    income_tax_exemption_array.append(c_address)
    c_address_location = (203, 145)
    income_tax_exemption_location_array.append(c_address_location)
    income_tax_exemption_page_array.append(3)

    """5쪽"""
    #이름
    s_name = name_data[0]
    income_tax_exemption_array.append(s_name)
    s_name_location = (204, 141)
    income_tax_exemption_location_array.append(s_name_location)
    income_tax_exemption_page_array.append(4)

    #주민등록번호
    c_serial_name = serial_name_data[0]
    income_tax_exemption_array.append(c_serial_name)
    c_serial_name_location = (460, 141)
    income_tax_exemption_location_array.append(c_serial_name_location)
    income_tax_exemption_page_array.append(4)

    #주소
    c_address = address
    income_tax_exemption_array.append(c_address)
    c_address_location = (208, 168)
    income_tax_exemption_location_array.append(c_address_location)
    income_tax_exemption_page_array.append(4)

    #세액공제 금액(원)
    month_tax = pdf_extract_array[11]
    income_tax_exemption_array.append(month_tax)
    month_tax_location = (501, 287)
    income_tax_exemption_location_array.append(month_tax_location)
    income_tax_exemption_page_array.append(4)

    return income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array

def final_output_file_data(bank_name, bank_srial_name, name_data, serial_name_data, country_name, address, pdf_extract_total_array, caculated_total_array, check_time_split, year_date_s_e):
    #최종 총 배열
    total_pdf_write_Data = []
    year_num = len(pdf_extract_total_array)
    for year in range(0,year_num,1):
        #연도 배열
        year_pdf_write_Data = []
        if len(caculated_total_array[year]) == 11:

            pdf_extract_array = pdf_extract_total_array[year]
            caculated_array = caculated_total_array[year]
            family_num = caculated_array[10]
            year_date = year_date_s_e[year]

            #과세표준A
            tax_decision_array, tax_decision_location_array, tax_decision_page_array = tax_decision_data_youth(bank_name,bank_srial_name,name_data,serial_name_data,address,pdf_extract_array,caculated_array,check_time_split)
            file_one_write_Data = [tax_decision_array, tax_decision_location_array, tax_decision_page_array]
            file_one_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_one_write_Data)
            file_one_write_Data = make_template_to_str.make_template_to_str(file_one_write_Data)

            # 종합소득세, 농어촌특별세 과세표준확정신고 및 납부 계산서(청년)B
            payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array = payment_caculation_data_youth(name_data,serial_name_data,family_num,address,pdf_extract_array,caculated_array,check_time_split)
            file_two_write_Data = [payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array]
            file_two_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_two_write_Data)
            file_two_write_Data = make_template_to_str.make_template_to_str(file_two_write_Data)

            # 소득 세액 공제신고서/근로자소득자 소득 세액 공제신고서C
            income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array = income_tax_exemption_data_youth(name_data,serial_name_data,country_name,address,pdf_extract_array,check_time_split,year_date)
            file_three_write_Data = [income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array]
            file_three_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_three_write_Data)
            file_three_write_Data = make_template_to_str.make_template_to_str(file_three_write_Data)

        elif len(caculated_total_array[year]) == 12:
            pdf_extract_array = pdf_extract_total_array[year]
            caculated_array = caculated_total_array[year]
            family_num = caculated_array[10]
            year_date = year_date_s_e[year]

            # 과세 표준 및 세액의 결정 청구서(자녀)
            tax_decision_array, tax_decision_location_array, tax_decision_page_array = tax_decision_data_child(bank_name,bank_srial_name,name_data,serial_name_data,address,pdf_extract_array,caculated_array,check_time_split)
            file_one_write_Data = [tax_decision_array, tax_decision_location_array, tax_decision_page_array]
            file_one_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_one_write_Data)
            file_one_write_Data = make_template_to_str.make_template_to_str(file_one_write_Data)

            # 종합소득세, 농어촌특별세 과세표준확정신고 및 납부 계산서(자녀)
            payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array = payment_caculation_data_child(name_data,serial_name_data,family_num,address,pdf_extract_array,caculated_array,check_time_split)
            file_two_write_Data = [payment_caculation_array, payment_caculation_location_array, payment_caculation_page_array]
            file_two_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_two_write_Data)
            file_two_write_Data = make_template_to_str.make_template_to_str(file_two_write_Data)

            # 소득 세액 공제신고서/근로자소득자 소득 세액 공제신고서 (2023 소득에 대한 연말 정산용)
            income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array = income_tax_exemption_data_child(name_data,serial_name_data,country_name,address,pdf_extract_array,check_time_split,year_date)
            file_three_write_Data = [income_tax_exemption_array, income_tax_exemption_location_array, income_tax_exemption_page_array]
            file_three_write_Data = make_template_to_str.make_int_to_seperate_by_com(file_three_write_Data)
            file_three_write_Data = make_template_to_str.make_template_to_str(file_three_write_Data)

        # print(file_one_write_Data)
        # print(file_two_write_Data)
        # print(file_three_write_Data)
        year_pdf_write_Data.append(file_one_write_Data)
        year_pdf_write_Data.append(file_two_write_Data)
        year_pdf_write_Data.append(file_three_write_Data)

        total_pdf_write_Data.append(year_pdf_write_Data)

    # 농어촌, 보험금 등 자료 서류, 환급금 양도, 가족관계 증명서
    # 번호, 스캔 일자, 성명, 외국인등록번호, 관할세무서, 경정 청구액, 수수료율, 수수료 금액, 누계, 입금 여부, 비고, 우편접수일, 실제접수일, 세무서담당자, 담당전화번호, 보완서류 비고
    # print(total_pdf_write_Data)
    return total_pdf_write_Data
