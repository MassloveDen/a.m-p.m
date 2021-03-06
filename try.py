b = ["10:00am", "11:45pm", "5:00am", "12:01am"]
# b = ["1:10pm", "4:40am", "5:00pm"]

hour = ([[i for i in row] for row in b])
minutes = []
for i in b:
    time = i
    # print(time)
    h = int(time[:-5])
    m = time[-2:]

    if m == 'am':
        if h == 12:
            h = h + 12
        else:
            h = (h + 1) % 12 - 1
        normal = h * 60 + int(time[-4:-2])

    elif m == 'pm':
        h = h % 12 + 12
        normal = h * 60 + int(time[-4:-2])
    minutes.append(normal)

answer = sorted(minutes)
print(answer)
diff = 1440
for i in range(len(answer)-1):
    c = answer[i+1] - answer[i]
    if c < diff:
        diff = c

print(diff)



# HTML - элементы Попросите функцию HTMLElements(str) прочитать передаваемый
# параметр str, который будет строкой элементов HTML DOM и обычного текста.Будут использоваться следующие
# элементы: b, i, em, div, p.Например: если str равно
# "<div> <b> <p> hello world </p> </b> </div>", то эта строка элементов DOM вложена
# правильно, поэтому ваша программа должна вернуть строку true.
# Если строка вложена неправильно, верните первый встреченный элемент, где при
# изменении на другой элемент будет получена
# правильно отформатированная строка.Если строка не отформатирована должным образом,
# то нужно будет изменить только один элемент.
# Например: если strравно « < div > < i > hello < / i > world < / b >», тогда
# ваша программа должна вернуть строку div, потому что если бы первый элемент < div >
# был изменен на < b >, строка была бы правильно отформатирована.