from models import *
from helpers.errorhelper import ErrorHelper


class TaskDone:
    def __init__(self, data):
        self.data = data
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }
    
    # if get user id of given slack id/ create if not exists and return user id
    def get_or_create(self, uid):
        instance = db.session.query(User).filter_by(slack_user_id=uid).first()

        if instance:
            return instance
            
        else:
            instance = db.session.add(User(slack_user_id = uid))
            db.session.commit()
            return instance

    def update_points(self):

        helper = ErrorHelper()
        current_task_id = int(self.data.get('text'))
        current_slack_id = self.data.get('user_id')
    
        # check if task id exists
        exists = db.session.query(db.exists().where(Task.task_id == current_task_id)).scalar()
        
        task_progress = Assignment.query.filter_by(assignment_id = current_task_id, progress = 0.0).all()

        if exists is False:
            return helper.get_command_help("no_task_id") 
        
        # check if task is done
        elif exists is True and len(task_progress) == 0:
            return helper.get_command_help("task_already_done")


        # if task is not done
        elif exists is True and task_progress[0].progress == 0.0:

            my_query = self.get_or_create(current_slack_id)
            user_id = my_query.user_id
            
            db.session.query(Assignment).filter_by(assignment_id=current_task_id).update(dict(progress=1.0,user_id=user_id))
            db.session.commit()

            return helper.get_command_help("task_done")
        pass
    