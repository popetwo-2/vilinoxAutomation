from tasks import *


class ConditionNode:
    def __init__(self, name):
        self.name = name


class Task:
    tasks = []

    def __init__(self, name, node, owner_email):
        self.name = name
        self.condition = node
        self.owner = owner_email

    def create_task(self, ):
        if self.condition == 'On Sign-up':
            task = Task(self.name, self.condition, self.owner)
            self.tasks.append(task)
            create_user.delay(self.owner)
            return task
        elif self.condition == 'On Product Purchase':
            # do something i.e action to be taken. defined in tasks.py
            pass
        elif self.condition == ' Check Purchase Status':
            # do something
            pass
        elif self.condition == ' Check Webinar Status':
            # do something
            pass
        elif self.condition == ' Check Subscriber Status':
            # do something
            pass
        elif self.condition == ' Returning Customers':
            # do something
            pass
        elif self.condition == ' Check Device Type':
            # do something
            pass
        elif self.condition == ' Returning Customers':
            # do something
            pass
        elif self.condition == 'On-Purchase Failure':
            # do something
            pass
        else:
            message = 'This might now work as there is no action'
            return message


class SuperUser:
    users = []

    def __init__(self, username, password, email, is_signed_up=True):
        self.username = username
        self.email = email
        self.password = password
        self.is_signed_up = is_signed_up

    def save_user(self,):
        user = SuperUser(username=self.username, password=self.password, email=self.email, is_signed_up=True)
        send_mail.delay(user.email)
        self.users.append(user)
        return user

    def get_user(self, email):
        for user in self.users:
            if email == user.email:
                return user


if __name__ == 'main':
    user = SuperUser('welzatm', "password", 'w@gmail.com')
    user3 = SuperUser('welzatm3', "password3", 'w3@gmail.com')
    print(user.username)
    print(user.email)
    print(user.is_signed_up)

    user2 = SuperUser('welzatm2', "password2", 'tpsolesi@gmail.com')
    new_user = user2.save_user()

    print(new_user.username)
    print(new_user.email)
    for user in new_user.all_users():
        print(user.email)

    condition = Condition('On Sign-up')
    print(condition.name)

    new_task = Task(name='Sign Up', condition=condition.name, owner=user2.email)
    print(new_task.name, new_task.condition)
