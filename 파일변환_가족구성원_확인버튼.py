import fitz
import os
import shutil
try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import tkinter as tk
    from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import pandas as pd

# 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input')
output_path = os.path.join(current_dir, 'output')

def create_directories(input_folder, output_folder):
    """입력 및 출력 폴더를 생성합니다."""
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

def batch_convert_pdf_to_csv(input_folder, output_folder):
    """입력 폴더의 모든 PDF 파일을 출력 폴더에 CSV 파일로 변환합니다."""
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_file = os.path.join(input_folder, filename)
            csv_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.csv')
            pdf_to_csv(pdf_file, csv_file)

def pdf_to_csv(pdf_file, csv_file):
    """PDF 파일을 CSV 파일로 변환합니다."""
    doc = fitz.open(pdf_file)
    with open(csv_file, 'w', encoding='utf-8-sig') as f:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            text = text.replace('\n', ' ').replace(',', '')
            f.write(f'{page_num + 1} {text} ')
    print(f'PDF 파일 {pdf_file}을 CSV 파일 {csv_file}로 변환 완료')

def csv_to_array(csv_file):
    """CSV 파일의 모든 값을 공백을 기준으로 일차원 배열로 변환합니다."""
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    data_array = data.split()  # 공백을 기준으로 문자열을 나누어 배열로 변환
    return data_array

def get_elements_after_keywords(data_array, keywords):
    """배열에서 각 키워드 뒤의 원소를 변수로 저장합니다."""
    results = {}
    for keyword in keywords:
        found = False
        for i, element in enumerate(data_array):
            if keyword in str(element):  # element를 문자열로 변환
                try:
                    results[keyword] = data_array[i+1]
                    found = True
                    break
                except IndexError:
                    results[keyword] = None
                    found = True
                    break
        if not found:
            results[keyword] = None
    return results

def family_member(elements):
    """'배우자'와 '부양가족(' 키워드 뒤의 원소를 이용해 계산한 값을 반환합니다."""
    spouse_value = elements.get('배우자', '0')
    dependents_value = elements.get('부양가족(', '0')
    
    try:
        spouse_value = int(spouse_value)
        if spouse_value != 0:
            spouse_value = 1
    except ValueError:
        spouse_value = 0

    try:
        dependents_value = int(dependents_value) // 1500000
    except ValueError:
        dependents_value = 0
    
    total_value = spouse_value + dependents_value
    return total_value

def process_csv_files(output_folder):
    """출력 폴더의 모든 CSV 파일을 처리합니다."""
    arrays_dict = {}
    keywords_dict = {}
    family_member_values = {}
    keywords = ['액', '주(현)근무지', '적용시에는연간근로소득)', '근로소득공제', '근로소득금액', '차감소득금액', '배우자', '⑪근무기간', '부양가족(']  # 키워드를 여기에 설정

    for filename in os.listdir(output_folder):
        if filename.endswith('.csv'):
            csv_file = os.path.join(output_folder, filename)
            data_array = csv_to_array(csv_file)

            # 일차원 배열 저장 / return {파일 이름: csv 배열}
            arrays_dict[filename] = data_array

            elements_after_keywords = get_elements_after_keywords(data_array, keywords)

            # 키워드 뒤의 원소 저장 / return {파일 이름:{키워드: 뒤의 원소}}
            keywords_dict[filename] = elements_after_keywords

            print(f'\nCSV 파일 {filename}의 일차원 배열:')
            print(arrays_dict[filename])

            print(f'\nCSV 파일 {filename}에서 키워드 뒤의 원소들:')
            for keyword, element in keywords_dict[filename].items():
                if element:
                    print(f'키워드 "{keyword}" 뒤의 원소: {element}')
                else:
                    print(f'키워드 "{keyword}" 뒤에 원소가 없습니다.')

            # family_member 함수 호출 및 결과 출력 / return (가족수의 총합)
            family_member_value = family_member(elements_after_keywords)
            family_member_values[filename] = family_member_value + 1
            print(f'\nCSV 파일 {filename}의 배우자 및 부양가족 계산 결과: {family_member_values}')

    return arrays_dict, keywords_dict, family_member_values

def drop(event):
    """드롭 이벤트 핸들러 함수."""
    files = root.tk.splitlist(event.data)
    for file in files:
        if os.path.isfile(file):
            shutil.copy(file, input_path)
            print(f"Moved {file} to {input_path}")
    batch_convert_pdf_to_csv(input_path, output_path)

def on_confirm():
    """확인 버튼 클릭 시 호출되는 함수."""
    if not os.listdir(input_path):
        messagebox.showerror("오류", "파일을 넣어주십시오")
    else:
        global arrays_dict, keywords_dict, family_member_values
        arrays_dict, keywords_dict, family_member_values = process_csv_files(output_path) # return arrays_dict, keywords_dict, family_member_value
        root.destroy()
        main_UI()

def setup_gui():
    """GUI를 설정합니다."""
    global root
    root = TkinterDnD.Tk()
    root.title("경정청구 자동 프로그램")
    root.geometry("600x400")

    label = tk.Label(root, text="파일을 드래그해 놓으십시오", width=50, height=10, bg="lightgrey")
    label.pack(padx=20, pady=20)

    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', drop)

    confirm_button = tk.Button(root, text="확인", command=on_confirm)
    confirm_button.pack(pady=10)
    root.mainloop()

def years_storage(keywords_dict):
    """키워드 딕셔너리에서 파일 이름과 근무기간을 딕셔너리 저장하는 함수 {파일명:연도월일}"""
    years_dict = {}
    for keyword_key in keywords_dict.keys():
        for keyword, element in keywords_dict[keyword_key].items():
            if keyword =='⑪근무기간':
                years_dict[keyword_key] = element
    return years_dict

def year_spliting(years_dict):
    """근무기간 연도/월/일 중 연도만 추출하는 함수{파일명:연도}"""
    for key, element in years_dict.items():
        splited_element = element.split('-')
        years_dict[key] = splited_element[0]
    # sorted_dict = sorted(years_dict.items(), key = lambda item: item[1])
    # sorted 사용시 리스트로 변환 되어 딕셔너리용 함수 따로 제작
    print(years_dict)
    return years_dict

def year_sorting(years_dict):
    """딕셔너리를 딕셔너리로 정렬하는 함수(key:연도 value: 파일명)"""
    sorted_dict = {}
    sorting_array = []
    for element in years_dict.values():
        sorting_array.append(element)
    sorted(sorting_array)
    for sort_element in sorting_array:
        for key, element in years_dict.items():
            if sort_element == element:
                sorted_dict[sort_element] = key
    return sorted_dict

def sorting_dict_used_file(keywords_dict):
    years_dict = years_storage(keywords_dict)
    years_dict = year_spliting(years_dict)
    sorted_dict = year_sorting(years_dict)
    return sorted_dict


def main_UI():
    global c1_1, c1_2, c1_4, c2_1, c2_2, c2_4, c3_1, c3_2, c3_4, c4_1, c4_2, c4_4, c5_1, c5_2, c5_4
    c1_1 = 0
    c1_2 = 0
    c1_4 = 0
    c2_1 = 0
    c2_2 = 0
    c2_4 = 0
    c3_1 = 0
    c3_2 = 0
    c3_4 = 0
    c4_1 = 0
    c4_2 = 0
    c4_4 = 0
    c5_1 = 0
    c5_2 = 0
    c5_4 = 0

    #메인창 띄우기
    main_tap = tk.Tk()
    main_tap.title('main UI')
    main_tap.grid()

    #n년차 받아야할 데이터들
    CHK_Val_1_1 = tk.IntVar()
    CHK_Val_1_2 = tk.IntVar()
    CHK_Val_1_3 = tk.StringVar()
    CHK_Val_1_4 = tk.IntVar()


    def CHK_check_1_1():
        global c1_1
        c1_1 = CHK_Val_1_1.get()

    def CHK_check_1_2():
        global c1_2
        c1_2 = CHK_Val_1_2.get()

    def CHK_check_1_3():
        global c1_3
        c1_3 = CHK_Val_1_3.get()

    def CHK_check_1_4():
        global c1_4
        c1_4 = CHK_Val_1_4.get()

    tk.Label(main_tap,text=" 1년차 경정 청구 여부").grid(column=0,row=1)
    tk.Checkbutton(main_tap,variable=CHK_Val_1_1, command= CHK_check_1_1).grid(column=1, row=1)

    tk.Label(main_tap,text="중소기업 여부").grid(column=0, row=2)
    tk.Checkbutton(main_tap,variable=CHK_Val_1_2, command=CHK_check_1_2).grid(column=1, row=2)

    tk.Label(main_tap,text="가족 구성원 수").grid(column=0, row=3)
    tk.Entry(main_tap, textvariable= CHK_Val_1_3).grid(column=1, row=3)

    tk.Label(main_tap,text="34세 초과").grid(column=0, row=4)
    tk.Checkbutton(main_tap,variable=CHK_Val_1_4, command=CHK_check_1_4).grid(column=1, row=4)


    CHK_Val_2_1 = tk.IntVar()
    CHK_Val_2_2 = tk.IntVar()
    CHK_Val_2_3 = tk.StringVar()
    CHK_Val_2_4 = tk.IntVar()

    def CHK_check_2_1():
        global c2_1
        c2_1 = CHK_Val_2_1.get()

    def CHK_check_2_2():
        global c2_2
        c2_2 = CHK_Val_2_2.get()

    def CHK_check_2_3():
        global c2_3
        c2_3 = CHK_Val_2_3.get()

    def CHK_check_2_4():
        global c2_4
        c2_4 = CHK_Val_2_4.get()

    tk.Label(main_tap,text=" 2년차 경정 청구 여부").grid(column=2,row=1)
    tk.Checkbutton(main_tap,variable=CHK_Val_2_1, command= CHK_check_2_1).grid(column=3, row=1)

    tk.Label(main_tap,text="중소기업 여부").grid(column=2, row=2)
    tk.Checkbutton(main_tap,variable=CHK_Val_2_2, command=CHK_check_2_2).grid(column=3, row=2)

    tk.Label(main_tap,text="가족 구성원 수").grid(column=2, row=3)
    tk.Entry(main_tap, textvariable= CHK_Val_2_3).grid(column=3, row=3)

    tk.Label(main_tap,text="34세 초과").grid(column=2, row=4)
    tk.Checkbutton(main_tap,variable=CHK_Val_2_4, command=CHK_check_2_4).grid(column=3, row=4)

    CHK_Val_3_1 = tk.IntVar()
    CHK_Val_3_2 = tk.IntVar()
    CHK_Val_3_3 = tk.StringVar()
    CHK_Val_3_4 = tk.IntVar()

    def CHK_check_3_1():
        global c3_1
        c3_1 = CHK_Val_3_1.get()

    def CHK_check_3_2():
        global c3_2
        c3_2 = CHK_Val_3_2.get()

    def CHK_check_3_3():
        global c3_3
        c3_3 = CHK_Val_3_3.get()

    def CHK_check_3_4():
        global c3_4
        c3_4 = CHK_Val_3_4.get()

    tk.Label(main_tap,text=" 3년차 경정 청구 여부").grid(column=4,row=1)
    tk.Checkbutton(main_tap,variable=CHK_Val_3_1, command= CHK_check_3_1).grid(column=5, row=1)

    tk.Label(main_tap,text="중소기업 여부").grid(column=4, row=2)
    tk.Checkbutton(main_tap,variable=CHK_Val_3_2, command=CHK_check_3_2).grid(column=5, row=2)

    tk.Label(main_tap,text="가족 구성원 수").grid(column=4, row=3)
    tk.Entry(main_tap, textvariable= CHK_Val_3_3).grid(column=5, row=3)

    tk.Label(main_tap,text="34세 초과").grid(column=4, row=4)
    tk.Checkbutton(main_tap,variable=CHK_Val_3_4, command=CHK_check_3_4).grid(column=5, row=4)

    CHK_Val_4_1 = tk.IntVar()
    CHK_Val_4_2 = tk.IntVar()
    CHK_Val_4_3 = tk.StringVar()
    CHK_Val_4_4 = tk.IntVar()

    def CHK_check_4_1():
        global c4_1
        c4_1 = CHK_Val_4_1.get()

    def CHK_check_4_2():
        global c4_2
        c4_2 = CHK_Val_4_2.get()

    def CHK_check_4_3():
        global c4_3
        c4_3 = CHK_Val_4_3.get()

    def CHK_check_4_4():
        global c4_4
        c4_4 = CHK_Val_4_4.get()

    tk.Label(main_tap,text=" 4년차 경정 청구 여부").grid(column=6,row=1)
    tk.Checkbutton(main_tap,variable=CHK_Val_4_1, command= CHK_check_4_1).grid(column=7, row=1)

    tk.Label(main_tap,text="중소기업 여부").grid(column=6, row=2)
    tk.Checkbutton(main_tap,variable=CHK_Val_4_2, command=CHK_check_4_2).grid(column=7, row=2)

    tk.Label(main_tap,text="가족 구성원 수").grid(column=6, row=3)
    tk.Entry(main_tap, textvariable= CHK_Val_4_3).grid(column=7, row=3)

    tk.Label(main_tap,text="34세 초과").grid(column=6, row=4)
    tk.Checkbutton(main_tap,variable=CHK_Val_4_4, command=CHK_check_4_4).grid(column=7, row=4)

    CHK_Val_5_1 = tk.IntVar()
    CHK_Val_5_2 = tk.IntVar()
    CHK_Val_5_3 = tk.StringVar()
    CHK_Val_5_4 = tk.IntVar()

    def CHK_check_5_1():
        global c5_1
        c5_1 = CHK_Val_5_1.get()

    def CHK_check_5_2():
        global c5_2
        c5_2 = CHK_Val_5_2.get()

    def CHK_check_5_3():
        global c5_3
        c5_3 = CHK_Val_5_3.get()

    def CHK_check_5_4():
        global c5_4
        c5_4 = CHK_Val_5_4.get()

    tk.Label(main_tap,text=" 5년차 경정 청구 여부").grid(column=8,row=1)
    tk.Checkbutton(main_tap,variable=CHK_Val_5_1, command= CHK_check_5_1).grid(column=9, row=1)

    tk.Label(main_tap,text="중소기업 여부").grid(column=8, row=2)
    tk.Checkbutton(main_tap,variable=CHK_Val_5_2, command=CHK_check_5_2).grid(column=9, row=2)

    tk.Label(main_tap,text="가족 구성원 수").grid(column=8, row=3)
    tk.Entry(main_tap, textvariable= CHK_Val_5_3).grid(column=9, row=3)

    tk.Label(main_tap,text="34세 초과").grid(column=8, row=4)
    tk.Checkbutton(main_tap,variable=CHK_Val_5_4, command=CHK_check_5_4).grid(column=9, row=4)

    #가족이름/ 주민번호
    name_1 = tk.StringVar()
    name_2 = tk.StringVar()
    name_3 = tk.StringVar()
    name_4 = tk.StringVar()
    name_5 = tk.StringVar()
    ss_num_1 = tk.StringVar()
    ss_num_2 = tk.StringVar()
    ss_num_3 = tk.StringVar()
    ss_num_4 = tk.StringVar()
    ss_num_5 = tk.StringVar()

    def CHK_check_name():
        global n_1, n_2, n_3, n_4, n_5, ss_n_1, ss_n_2, ss_n_3, ss_n_4, ss_n_5
        n_1 = name_1.get()
        n_2 = name_2.get()
        n_3 = name_3.get()
        n_4 = name_4.get()
        n_5 = name_5.get()
        ss_n_1 = ss_num_1.get()
        ss_n_2 = ss_num_2.get()
        ss_n_3 = ss_num_3.get()
        ss_n_4 = ss_num_4.get()
        ss_n_5 = ss_num_5.get()

    tk.Label(main_tap,text="이름").grid(column=1, row=5)
    tk.Label(main_tap,text="주민등록번호").grid(column=2, row=5)
    tk.Label(main_tap,text="본인").grid(column=0, row=6)
    tk.Entry(main_tap, textvariable= name_1).grid(column=1, row=6)
    tk.Entry(main_tap, textvariable= ss_num_1).grid(column=2, row=6)
    tk.Label(main_tap,text="배우자").grid(column=0, row=7)
    tk.Entry(main_tap, textvariable= name_2).grid(column=1, row=7)
    tk.Entry(main_tap, textvariable= ss_num_2).grid(column=2, row=7)
    tk.Label(main_tap,text="자녀1").grid(column=0, row=8)
    tk.Entry(main_tap, textvariable= name_3).grid(column=1, row=8)
    tk.Entry(main_tap, textvariable= ss_num_3).grid(column=2, row=8)
    tk.Label(main_tap,text="자녀2").grid(column=0, row=9)
    tk.Entry(main_tap, textvariable= name_4).grid(column=1, row=9)
    tk.Entry(main_tap, textvariable= ss_num_4).grid(column=2, row=9)
    tk.Label(main_tap,text="자녀3").grid(column=0, row=10)
    tk.Entry(main_tap, textvariable= name_5).grid(column=1, row=10)
    tk.Entry(main_tap, textvariable= ss_num_5).grid(column=2, row=10)

    #UI data 정렬 함수
    def UI_data_sorted(c1_1, c1_2, c1_4, c2_1, c2_2, c2_4, c3_1, c3_2, c3_4, c4_1, c4_2, c4_4, c5_1, c5_2, c5_4, n_1, n_2, n_3, n_4, n_5, ss_n_1, ss_n_2, ss_n_3, ss_n_4, ss_n_5):
        data_1year = []
        data_1year.append(c1_1)
        data_1year.append(c1_2)
        data_1year.append(c1_4)
        data_2year = []
        data_2year.append(c2_1)
        data_2year.append(c2_2)
        data_2year.append(c2_4)
        data_3year = []
        data_3year.append(c3_1)
        data_3year.append(c3_2)
        data_3year.append(c3_4)
        data_4year = []
        data_4year.append(c4_1)
        data_4year.append(c4_2)
        data_4year.append(c4_4)
        data_5year = []
        data_5year.append(c5_1)
        data_5year.append(c5_2)
        data_5year.append(c5_4)
        family_ss_name = []
        family_ss_name.append(n_1)
        family_ss_name.append(ss_n_1)
        family_ss_name.append(n_2)
        family_ss_name.append(ss_n_2)
        family_ss_name.append(n_3)
        family_ss_name.append(ss_n_3)
        family_ss_name.append(n_4)
        family_ss_name.append(ss_n_4)
        family_ss_name.append(n_5)
        family_ss_name.append(ss_n_5)
        data = [data_1year, data_2year, data_3year, data_4year, data_5year]
    
        return CHK_claim_status, data_1year, data_2year, data_3year, data_4year, data_5year, family_ss_name, data

    #닫기 버튼(마지막에 UI data 정렬 후 값 return 해줌)
    def on_exit():
        main_tap.destroy()
    
    tk.Button(main_tap, text="닫기", command=on_exit).grid(column=9,row=10)

    main_tap.mainloop()

    if main_tap.aftercancel:
        CHK_check_1_3()
        CHK_check_2_3()
        CHK_check_3_3()
        CHK_check_4_3()
        CHK_check_5_3()
        CHK_check_name()
        global CHK_claim_status, data_1year, data_2year, data_3year, data_4year, data_5year, family_ss_name, data
        CHK_claim_status, data_1year, data_2year, data_3year, data_4year, data_5year, family_ss_name, data = UI_data_sorted(c1_1, c1_2, c1_4, c2_1, c2_2, c2_4, c3_1, c3_2, c3_4, c4_1, c4_2, c4_4, c5_1, c5_2, c5_4, n_1, n_2, n_3, n_4, n_5, ss_n_1, ss_n_2, ss_n_3, ss_n_4, ss_n_5)
        # return CHK_claim_status, data_1year, data_2year, data_3year, data_4year, data_5year, family_ss_name

        global sorted_dict
        sorted_dict = sorting_dict_used_file(keywords_dict)
        """여기부터 이어서 하면됨"""

def main():
    """프로그램의 메인 함수."""
    create_directories(input_path, output_path)
    setup_gui()

if __name__ == '__main__':
    main()


#변수 설정'총급여액', '과세표준', '근로소득세액공제', '세액공제계
#종합소득 과세표준
def taxable_income_change_func():
    for key,value in sorted_dict.items():
        if key == 2019:
            child_num = c1_3
        elif key == 2020:
            child_num = c2_3
        elif key == 2021:
            child_num = c3_3
        elif key == 2022:
            child_num = c4_3
        elif key == 2023:
            child_num = c5_3
        
        for family_key, family_value in family_member_values.items():
            if family_key == value:
                if child_num == 1:
                    break
                elif child_num >= 2:
                    taxable_income_change = taxable_income - 1500000*(child_num - family_value)
            else:
                continue
            
    return taxable_income_change

#산출세액
def outcome_tax_func(tax_year, taxable_income_change):
    if tax_year == [2023]:
        if taxable_income_change<=0:
            outcome_tax = 0
        elif taxable_income_change<=14000000:
            outcome_tax = taxable_income_change*0.06
        elif taxable_income_change<=50000000:
            outcome_tax = taxable_income_change*0.15-1260000
        elif taxable_income_change<=88000000:
            outcome_tax = taxable_income_change*0.24-5760000
        elif taxable_income_change<=150000000:
            outcome_tax = taxable_income_change*0.35-15440000
        elif taxable_income_change<=300000000:
            outcome_tax = taxable_income_change*0.38-19940000
        elif taxable_income_change<=500000000:
            outcome_tax = taxable_income_change*0.4-25940000
        elif taxable_income_change<=1000000000:
            outcome_tax = taxable_income_change*0.42-35940000
        else:
            outcome_tax = taxable_income_change*0.45-65940000
    
        return outcome_tax
    
    elif tax_year in [2021,2022]:
        if taxable_income_change <= 0:
            outcome_tax = 0
        elif taxable_income_change <= 12000000:
            outcome_tax = taxable_income_change * 0.06
        elif taxable_income_change <= 46000000:
            outcome_tax = taxable_income_change * 0.15 - 1080000
        elif taxable_income_change <= 88000000:
            outcome_tax = taxable_income_change * 0.24 - 5220000
        elif taxable_income_change <= 150000000:
            outcome_tax = taxable_income_change * 0.35 - 14900000
        elif taxable_income_change <= 300000000:
            outcome_tax = taxable_income_change * 0.38 - 19400000
        elif taxable_income_change <= 500000000:
            outcome_tax = taxable_income_change * 0.4 - 25400000
        elif taxable_income_change <= 1000000000:
            outcome_tax = taxable_income_change * 0.42 - 35400000
        else:
            outcome_tax = taxable_income_change * 0.45 - 65400000
        
        return outcome_tax
        
    elif tax_year in [2019,2020]:
        if taxable_income_change <= 0:
            outcome_tax = 0
        elif taxable_income_change <= 12000000:
            outcome_tax = taxable_income_change * 0.06
        elif taxable_income_change <= 46000000:
            outcome_tax = taxable_income_change * 0.15 - 1080000
        elif taxable_income_change <= 88000000:
            outcome_tax = taxable_income_change * 0.24 - 5220000
        elif taxable_income_change <= 150000000:
            outcome_tax = taxable_income_change * 0.35 - 14900000
        elif taxable_income_change <= 300000000:
            outcome_tax = taxable_income_change * 0.38 - 19400000
        elif taxable_income_change <= 500000000:
            outcome_tax = taxable_income_change * 0.4 - 25400000
        else:
            outcome_tax = taxable_income_change * 0.42 - 35400000
        
        return outcome_tax

#중소기업 청년 감면
def youth_discount_func(outcome_tax):
        
    youth_discount = min(outcome_tax*0.9, 1500000)
        
    return youth_discount

#근로소득 세액공제액 한도
def payment_tax_limit_func(total_salary):
    if total_salary<=33000000:
        payment_tax_limit = 740000
    elif total_salary<=70000000:
        payment_tax_limit = 740000-[(total_salary-33000000)*0.08]
    elif total_salary<=120000000:
        payment_tax_limit = 660000-[(total_salary-70000000)*0.5]
    else:
        payment_tax_limit = 500000-[(total_salary-120000000)*0.5]
    return payment_tax_limit

#근로소득
def payment_tax_func(outcome_tax, payment_tax_limit):
    if outcome_tax<=1300000:
        payment_tax_change = min((outcome_tax*0.55),740000)
    else:
        payment_tax_change = min((715000+(outcome_tax-1300000)*0.3),payment_tax_limit)
    return payment_tax_change


#청년 취업 감면 세액 공제
def youth_employment_discount_func(outcome_tax, youth_discount):
    if (outcome_tax*(1-(youth_discount/outcome_tax))) == 0:
        youth_employment_discount = 0
        return youth_employment_discount
    else:
        youth_employment_discount = (outcome_tax*(1-(youth_discount/outcome_tax)))
        
    return youth_employment_discount


def final_tax_func(youth_discount, youth_employment_discount, payment_tax_change):
    final_tax_discount = youth_discount + youth_employment_discount + payment_tax_change
        
    return final_tax_discount

def final_tax_child_discount_func(family_tax_discount, youth_employment_discount, payment_tax_change):
    final_tax_child_discount = family_tax_discount + youth_employment_discount + payment_tax_change
        
    return final_tax_child_discount
    
#차감 징수액
def tax_gap_func(origin_final_tax_discount, final_tax_discount):
    tax_gap = origin_final_tax_discount - final_tax_discount
    return tax_gap

#원래 납부할 세액과의 차
def final_func(tax_gap):
    final = 0 - tax_gap
    return final

#환급받을 세금
def return_tax_func(final):
    return_tax = final*0.3
    return return_tax

#자녀 감면
def child_tax_discount_func():
    for x in sorted_dict.key():
        if x == 2019:
            child_num = c1_3
        elif x == 2020:
            child_num = c2_3
        elif x == 2021:
            child_num = c3_3
        elif x == 2022:
            child_num = c4_3
        elif x == 2023:
            child_num = c5_3
        
    if child_num == 0:
        family_tax_discount = 0
    elif child_num == 1:
        family_tax_discount = 150000
    elif child_num == 2:
        family_tax_discount = 300000
    else:
        family_tax_discount = (child_num - 2)*300000 + 350000
    return family_tax_discount

#결정세액 = 내국세
def final_tax_child_discount_func(family_tax_discount, youth_employment_discount, payment_tax_change):
    final_tax_discount = family_tax_discount + youth_employment_discount + payment_tax_change
        
    return final_tax_discount

def variable_func():
    year5_list = []
    for value in sorted_dict.value():
        variable_list = []
        filename = value
        for keyword_filname, keyword_value in keywords_dict.items():
            if filename == keyword_filname:
                total_salary = keyword_value['총급여']
                taxable_income_change = keyword_value['과세표준']
                payment_tax = keyword_value['근로소득']
                origin_final_tax_discount = keyword_value['세액공제계']
                variable_list.append(total_salary)
                variable_list.append(taxable_income_change)
                variable_list.append(payment_tax)
                variable_list.append(origin_final_tax_discount)
                year5_list.append(variable_list)
        
        return year5_list

#자녀수 감면


#메인 함수(총급여, 종합소득 과세표준,근로소득,파일 연도,세액공제 계 필요)
def calculating_main(data):
    global year5_before_calculating_list
    year5_before_calculating_list = variable_func()
    for x in data:
        for key1 in sorted_dict.keys():
            tax_year = key1
            for k in x:
                if k == 1:
                    taxable_income_change = taxable_income_change_func()
                    payment_tax_change = payment_tax_func(outcome_tax, payment_tax)
                    payment_tax_limit = payment_tax_limit_func(total_salary)
                    youth_discount = youth_discount_func(outcome_tax)
                    youth_employment_discount = youth_employment_discount_func(outcome_tax, youth_discount)
                    family_tax_discount = child_tax_discount_func()
                    final_tax_discount = final_tax_child_discount_func(family_tax_discount, youth_employment_discount, payment_tax_change)
                    tax_gap = tax_gap_func(origin_final_tax_discount, final_tax_discount)
                    final = final_func(tax_gap)
                    return_tax = return_tax_func(final)
                    year5_list.append(taxable_income_change)
                    year5_list.append(payment_tax_change)
                    year5_list.append(final_tax_discount)
                    year5_list.append(final)
                    year5_list.append(return_tax)
                    break
                else:
                    outcome_tax = outcome_tax_func(tax_year, taxable_income_change)
                    youth_discount = youth_discount_func(outcome_tax)
                    payment_tax_limit = payment_tax_limit_func(total_salary)
                    payment_tax_change = payment_tax_func(outcome_tax, payment_tax_limit)
                    youth_employment_discount = youth_employment_discount_func(outcome_tax, youth_discount)
                    final_tax_discount = final_tax_func(youth_discount, youth_employment_discount, payment_tax_change)
                    tax_gap = tax_gap_func(origin_final_tax_discount, final_tax_discount)
                    final = final_func(tax_gap)
                    return_tax = return_tax_func(final)
                    year5_list.append(payment_tax_change)
                    year5_list.append(final_tax_discount)
                    year5_list.append(final)
                    year5_list.append(return_tax)
                