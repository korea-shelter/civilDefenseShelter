import os


raw_csv = "../../data/raw/민방위 대피소(API)_재난안전데이터포털_재분류.csv"
target_csv = "../../data/interim/shelter_preprocess.csv"

if os.path.exists(target_csv):
    os.remove(target_csv)

newline = os.linesep  # Defines the newline based on your OS.

source_fp = open(raw_csv, 'r')
target_fp = open(target_csv, 'w')
first_row = True
for row in source_fp:
    if first_row:
        row = row.replace("경도", "lon")
        row = row.replace("위도", "lat")
        print(row)
        first_row = False
    target_fp.write(row)
