import aminofix, json, os
from time import sleep as ts
magenta = '\033[35m'
red = '\033[32m'
red_error = '\033[3;31m'
green = '\033[32m'
for i in ['community.txt', 'account.json']:
				if i not in os.listdir():
					print(f"\t{red}Required file {i} not found!!\n")
					exit()
with open("account.json", "r") as json_file:
    json_info = json.load(json_file)
with open('community.txt', 'r') as file:
    linkes = file.read().split('\n')
def check_com(comId):
    try:
        client.join_community(comId)
        client.leave_community(comId)
        locked = "Open"
        return locked
    except:
        locked = "Close"
        return locked
client = aminofix.Client(json_info["deviceId"])
def login():
	try:
		client.login(email=json_info["email"], password=json_info["password"])
		print(f"\t{green}Login is successful!{magenta}\n")
	except Exception as e:
                    print(f"{red}\tLogin error, error text>> {red_error}\n{e}{magenta}\n")
                    exit()
def main():
	login()
	for link in linkes:
		link = link.split('$')
		comId = None
		try:
			code=client.get_from_code(link[0])
			comId=code.comId
		except Exception as e:
			print(f"{red}\tError Text>> {red_error}\n{e}{magenta}\n")
			continue
		result = check_com(comId)
		infocom = client.get_community_info(comId).json
		name = infocom["name"]
		count = infocom["membersCount"]
		status = infocom["status"]
		langue = infocom["primaryLanguage"]
		ts(2)
		print(f"\tCommunity with ID '{comId}'\n\tName of Community>> '{name}'\n\tCount of Members>> {count}\n\tСommunity status>> '{status}'\n\tLanguage>>{langue}\n\tСommunity has>> {result}\n")
		if result == "Open":
                    try:
                        fl = open(f"checketlinks/community_{langue}.txt", "a")
                        fl.write(f"{link[0]}\n")
                        fl.close()
                        print(f"\t{green}The community is open and recorded in a file!{magenta}\n")
                    except:
                        print(f"\t{red}The key folder was not found, we are creating it..{magenta}\n")
                        this_dir = os.getcwd()
                        os.mkdir(f"{this_dir}/checketlinks")
                        fl = open(f"checketlinks/community_{langue}.txt", "a")
                        fl.write(f"{link[0]}\n")
                        fl.close()
                        print(f"\t{green}The community is open and recorded in a file!{magenta}\n")

main()
	
	
	
