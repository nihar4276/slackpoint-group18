from commands.viewpoints import ViewPoints
import datetime

class Reminders:
    """
        This class handles the Create Reminder functionality.
    """
    def createReminder(self):
        #Method to create reminder
        #Fetch pending task list
        vp = ViewPoints(progress=0.0)
        pending_tasks = vp.get_list()
        # print("payload", payload)



