import re


# 把识别后的最上面一行的y坐标和最下面一行的y坐标相减，然后分成7行的方位，在进行正则匹配，并进行纠正输出
context = '''
中华人民共和国机动车行驶证
Vehicle License of the People's Republic of china
号牌号码粤E15K05
车辆类型小轿车
Plate No.
Vehicle Type
所有人李沫潼
Owner
住址广东省佛山市禅城区张槎街道朗沙路71号宿
使用性质非运营
品牌型号别克牌SGM7161LEAT
广东省佛山车辆识别代号LSGJT52U67H106722
VINLSGJT52U67H106722
市公安局交发动机号码76110577
Engine No.
通警察支队注册日期2012-09-06发证日期2014-08-27
发证日期2014-08-27
RegisterDate
IssueDate
'''
abbr = ['京', '沪', '津', '渝', '黑', '吉', '辽', '蒙', '冀', '新', '甘', '青', '陕', '宁', '豫', '鲁',
        '晋', '皖', '鄂', '湘', '苏', '川', '黔', '滇', '桂', '藏', '浙', '赣', '粤', '闽', '台', '琼', '港', '澳']
pattern1 = r'[号牌号码]+([\u4e00-\u9fa5]{1}[A-Za-z0-9]{6})'
pattern2 = r'[所有人]+(.+)'
pattern3 = r'[品牌型号]+(.+)'
pattern4 = r'[车辆识别代号]+([A-Za-z0-9]{10,17})$'
pattern4_2 = r'VIN([A-Za-z0-9]{10,17})$'
pattern5 = r'[发动机号码]+([A-Za-z0-9]{3,15})$'
pattern6 = r'[注册日期]+([A-Za-z0-9-]{5,10})'
pattern7 = r'[发证日期]+([A-Za-z0-9-]{5,10})$'

# 如果全部文本里面有出现哪个市名字，直接把首个字符纠正为该市的简称，有O字母的话肯定是0，第二个字符肯定是英文字母，如果是数字需要纠正
chepai = re.findall(pattern1, context)
owner = re.findall(pattern2, context)  # 可以是人名或公司名，对公司名的固定字串可以进行纠正
model = re.findall(pattern3, context)  # 暂无方案纠正
vin_1 = re.findall(pattern4, context, re.M)  # 暂无方案纠正
vin_2 = re.findall(pattern4_2, context, re.M)  # 暂无方案纠正
engine = re.findall(pattern5, context, re.M)  # 暂无方案纠正
regDate = re.findall(pattern6, context)  # 纠正年月日的合理范围，不能超过当前系统的时间，发证日期大于注册日期
# 纠正年月日的合理范围，月份大于0小于等于12，日大于0小于等于31
issueDate = re.findall(pattern7, context, re.M)
print(chepai, owner, model, vin_1, vin_2, engine, regDate, issueDate, sep='\n')
