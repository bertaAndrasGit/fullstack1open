users = [
    (1,"Bob","pass"),
    (2,"Alice","123"),
    (3,"Jose","yolo"),
    (4,"Mark","longpassword"),
    (5,"John","longerpassword12345"),
]

#ez
username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])

#ezt csinálja
for user in users:
    if user[1] == "Bob":
        print(user)
