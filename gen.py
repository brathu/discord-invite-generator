import sys, time

def generate():
	pref = '\n$ '

	application_id = input(f'Application ID:{pref}') #example: 458276816071950337

	permcheck = input(f'Permission/s [a] for ADMIN or [c] for Custom:{pref}')

	if(permcheck == 'a'):
		perms = 8 #set perms to the admin perm(8)
	elif(permcheck == 'c'):
		#list of all perms: https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags
		perms = input(f'Custom Permissions:{pref}') #set your custom perm to perms
	else:
		print(permcheck,'is not available. Choose between a or c')
		exit()

	link = f'https://discord.com/oauth2/authorize?client_id={application_id}&permissions={perms}&scope=bot%20applications.commands'

	print(link)

try:
	if(sys.argv[1] == 'help'):
		print('use: py gen.py APPLICATION_ID PERMIS')
		print('example forAPPLICATION_ID: 458276816071950337')
		print('example for PERMS: 8')
		print('py gen.py 458276816071950337 8')
	else:
		application_id = sys.argv[1]
		perms = sys.argv[2]
		link = f'https://discord.com/oauth2/authorize?client_id={application_id}&permissions={perms}&scope=bot'
		print(link)

except:
	print('No args given! Generate function starts now.'); time.sleep(1)
	generate()

