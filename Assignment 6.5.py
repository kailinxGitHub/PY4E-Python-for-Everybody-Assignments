text = "X-DSPAM-Confidence:    0.8475"
ex = text.find('.')
data = text[ex-1:ex+5]
str_data = float(data)

print(str_data)
