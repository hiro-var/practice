from datetime import date

d_today = date.today()
new_years_day = date(d_today.year + 1,1,1)
diff_date = new_years_day - d_today
print(f'今年はあと{diff_date.days}日')

#-----------------------------------------------

# 前期売り上げ
first_h_sales = [
  300_000_000, 440_000_000, 340_000_000, 
  420_000_000, 700_000_000, 600_000_000
]
# 後期売り上げ
second_h_sales = [
    230_000_000, 120_000_000, 440_000_000, 
    520_000_000, 280_000_000, 390_000_000
]

#------------------------------------------------

total_sales = first_h_sales + second_h_sales

print('==== 2021年売り上げ ====')
print(f'前期: {sum(first_h_sales):,}円')
print(f'後期: {sum(second_h_sales):,}円')
print(f'合計: {sum(total_sales):,}円')
print('====================')

scores = {
  '国語': 87, '数学': 86, '英語': 70, '理科': 73, '社会': 80
}

def three_subject_score_avg(scores):
    total_score = 0
    for key, value in scores.items():
        if key in ['国語', '数学', '英語']:
            total_score += value  # valueを加算
    return total_score / 3  # ループ後に平均を返す

result = three_subject_score_avg(scores)
print(result)

#------------------------------------------------

