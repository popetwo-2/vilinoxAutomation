from models import *

if __name__ == '__main__':
    node = ConditionNode('On Sign-up')  # Step 1. Condition is created first.

    new_task = Task(name='Sign Up', node=node.name, owner_email='w@h.com')  # Step 2. Task is created.
    new_task.create_task()  # Step 3. Triggers an action.
    print(new_task.name, new_task.condition)
    print(new_task.owner)
