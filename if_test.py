kg = float(input('请输入您的体重(Kg):'))
h = float(input('请输入您的身高(Cm):'))
bmi = 100*(kg/h)**2
if bmi <= 18.5:
    print('您的BMI值为:%.2f'%bmi,'您的体重过轻！')
elif bmi <= 25:
    print('您的BMI值为:%.2f'%bmi,'您的体重正常！')
elif bmi <= 28:
    print('您的BMI值为:%.2f'%bmi,'您的体重过重！')
elif bmi <= 32:
    print('您的BMI值为:%.2f'%bmi,'您的体重属于肥胖！' )
else:
    print('您的BMI值为:%.2f'%bmi,'您的体重属于严重肥胖！')