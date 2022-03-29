# import the modules you want to call        
import netmiko, getpass, datetime



def backupconfig(username,password,ip):

    cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
    }

    net_connect = netmiko.ConnectHandler(**cisco_ios)

    # get the prompt as a string
    prompt = net_connect.find_prompt()

    hostname = net_connect.send_command('show run | i host')
    hostname.split(" ")
    col1,col2 = hostname.split(" ")
    print('working on '+col2)
    date = datetime.date.today()


    filename = col2 + '_' + str(date) + '.txt'
    location = 'C:/new project/configurations/'+filename
    showrun = net_connect.send_command('show run')
    showvlan = net_connect.send_command('show vlan')
    showver = net_connect.send_command('show ver')
    log_file = open(location, "a")   # in append mode
    log_file.write(showrun)
    log_file.write("\n")
