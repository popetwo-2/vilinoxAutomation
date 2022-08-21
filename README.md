# vilinoxAutomation

1. Run pip install -r requirements.txt
3. Open another cli and run 'celery -A tasks worker -l INFO' to ensure the underground task works. I used redis cloud 

Workflow Summary.Process is Conditional Node --> Task ---> Action

1. Conditional Node Creation The following nodes have been hard-coded in the script as seen in diagram however you can create one with Condition Class.
from models import *
node = ConditionNode("On Sign Up")
node.name = "On Sign Up"

For testing below nodes are supported,  just change name to any below node = ConditionNode("On Product Purchase")

On Sign Up 
On Product Purchase
Check Purchase Status
Check Webinar Status
Check Subscriber Status
Returning Customers
Check Device Type
Returning Customers
On-Purchase Failure
 
2. Task Creation: Once the task is created, an action is triggered as an underground task  using Celery/Redis.
from models import *


new_task = Task(name='Sign Up',node='On Sign-up', owner_email='w@h.com'))#	The node refers to the instance of Conditional node created above
 new_task.name = 'Sign Up'
 new_task.condition = "On Sign Up"
 
 Example followed is the send_email.
 1. Whwn task(Sign Up) and it equals the conditional node On Sign-up, a new user is created
 
 
 4. I have put a sample script i.e flow.py which you can run and the above flow will be implemented.  
  
