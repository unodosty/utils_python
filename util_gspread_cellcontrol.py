import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from df2gspread import df2gspread as d2g

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'json file'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'input your spread sheet url'

# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('worksheet name')

# 셀 읽기
cell_data = worksheet.acell('B2').value

# 행 읽기
row_data = worksheet.row_values(2)

# 열 읽기
column_data = worksheet.col_values(1)

# 범위 읽기
range_list = worksheet.range('A1:D3')
for cell in range_list:
    print(cell.value)

# 셀 업데이트
worksheet.update_acell('B1', 'b1 updated')

# 행 추가
worksheet.append_row(['new1', 'new2', 'new3', 'new4'])

# 특정 행 추가
worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 5)

# 시트 크기맞추기
worksheet.resize(10,4)

# 셀 Formatting
# 글자 진하게
worksheet.format('G2', {'textFormat': {'bold': True}})
# 배경 노란색 포함
worksheet.format("G2", {'textFormat': {'bold': True},
                        "backgroundColor": {
                            "red": 1.0,
                            "green": 1.0,
                            "blue": 0.0
                        }})

# Getting All Values From a Worksheet as a List of Lists
list_of_lists = worksheet.get_all_values()

# Getting All Values From a Worksheet as a List of Dictionaries
list_of_dicts = worksheet.get_all_records()

# Find a cell matching a string:
cell = worksheet.find("Dough")
print("Found something at R%sC%s" % (cell.row, cell.col))
