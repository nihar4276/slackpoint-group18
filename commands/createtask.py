from copy import deepcopy
import random
from models import *


class CreateTask:
    base_create_task_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ">{greeting}! Your task SP-{id} was created successfully."
        }
    }

    greetings = ["Awesome", "Great", "Congratulations", "Well done", "Let's go"]

    def __init__(self):
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def create_task(self, desc, points, deadline):
        # db query to create task and return the id
        # parse them
        # DB call to add task, returns id
        task = Task()
        task.description = desc
        task.points = points
        task.deadline = deadline
        db.session.add(task)
        db.session.commit()
        db.session.refresh(task)

        id = task.task_id
        response = deepcopy(self.base_create_task_block_format)
        response["text"]["text"] = response["text"]["text"].format(greeting=random.choice(self.greetings), id=id)
        self.payload["blocks"].append(response)
        return self.payload