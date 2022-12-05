from commands.viewpoints import ViewPoints
import datetime
import re

class Reminders:
    """
    This class handles the Create Reminder functionality.
    """
    def createReminder(self):
        '''
        Method to create reminder
        '''
        #Fetch pending task list
        vp = ViewPoints(progress=0.0)
        pending_tasks = vp.get_list()
        print(pending_tasks)
        listofdict = pending_tasks["blocks"]
        tom_tasks=[]
        for taskinfo in listofdict:
            task_text = taskinfo["text"]["text"]
            #print("task_text ",task_text)
            str_date = re.findall("\d{4}-\d{2}-\d{2}",task_text)[0]
            #print("str_date :",str_date)
            curr_date = datetime.date.today()
            #print("curr_date",curr_date)
            task_date=datetime.datetime.strptime(str_date,"%Y-%m-%d").date()
            #print("task_date",task_date)
            tomorrow = curr_date + datetime.timedelta(days=1)
            #print("tomorrow :",tomorrow)
            if task_date==tomorrow:
                tom_tasks.append(task_text)

        # print(tom_tasks)
        return tom_tasks


    def reminder_msg_block(self,msg):
        '''
        Method to create message block
        Input - list of str
        Output - Slack block
        '''
        parent_msg = {"blocks": []}
        child_msg = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Reminder : Urgent Tasks Due Completion :*"
                }
            }

        parent_msg['blocks'].append(child_msg)
        for task_text in msg:
            child_msg = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": task_text
                 }
            }
            parent_msg['blocks'].append(child_msg)

        return parent_msg



