import jenkins

try:
    server = jenkins.Jenkins('http://54.237.237.41:8080/', username='devops', password='devops')


    user = server.get_whoami()

    print(user['fullName'])
except:
    print("Please double check your credentials")