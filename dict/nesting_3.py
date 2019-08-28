users = {
	'user_0': {
		'name': '张三',
		'sex': '男',
		'age': '18',
	},

	'user_1': {
		'name': '李四',
		'sex': '女',
		'age': '20',
	},
}

for username, user_info in users.items():
	print("用户名：" + username)
	print("\t姓名：" + user_info['name'])
	print("\t性别：" + user_info['sex'])
