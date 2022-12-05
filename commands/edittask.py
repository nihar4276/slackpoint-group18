from copy import deepcopy
import random
from models import *
from datetime import date


class EditTask:
    """
    This class handles the Edit Task functionality.
    """

    # base_edit_task_block_format = {
    #     "type": "section",
    #     "text": {
    #         "type": "mrkdwn",
    #         "text": ">{greeting}! Your task SP-{id} was edit successfully.",
    #     },
    # }
    #
    # greetings = ["Awesome", "Great", "Congratulations", "Well done", "Let's go"]

    def __init__(self, task_id=None):
        """
        Constructor to initialize payload object

        :param:
        :type:
        :raise:
        :return: None
        :rtype: None

        """
        self.task_id = task_id
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def edit_task_input_blocks(self):
        """
        Edit blocks list containing input fields for description, deadline, points of a task, along with a button to edit the task

        :param:
        :type:
        :raise:
        :return: Blocks list
        :rtype: list

        """
        block_description = {
            "type": "input",
            "element": {
                "type": "plain_text_input",
                "action_id": "edit_action_description",
            },
            "label": {"type": "plain_text", "text": "Description", "emoji": True},
        }
        block_deadline = {
            "type": "input",
            "element": {
                "type": "datepicker",
                "initial_date": date.today(),
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a date",
                    "emoji": True,
                },
                "action_id": "edit_action_deadline",
            },
            "label": {"type": "plain_text", "text": "Deadline", "emoji": True},
        }
        block_points = {
            "type": "input",
            "element": {
                "type": "static_select",
                "placeholder": {"type": "plain_text", "text": "Select", "emoji": True},
                "options": [
                    {
                        "text": {"type": "plain_text", "text": "1", "emoji": False},
                        "value": "1",
                    },
                    {
                        "text": {"type": "plain_text", "text": "2", "emoji": False},
                        "value": "2",
                    },
                    {
                        "text": {"type": "plain_text", "text": "3", "emoji": False},
                        "value": "3",
                    },
                    {
                        "text": {"type": "plain_text", "text": "4", "emoji": False},
                        "value": "4",
                    },
                    {
                        "text": {"type": "plain_text", "text": "5", "emoji": False},
                        "value": "5",
                    },
                ],
                "action_id": "edit_action_points",
            },
            "label": {"type": "plain_text", "text": "Points", "emoji": True},
        }
        block_actions_button = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Edit task"
            },
            "action_id": "edit_action_button",
        }
        block_actions = {"type": "actions", "elements": []}
        block_actions["elements"].append(block_actions_button)

        blocks = []
        blocks.append({"task_id": self.task_id})
        blocks.append(block_description)
        blocks.append(block_deadline)
        blocks.append(block_points)
        blocks.append(block_actions)
        return blocks

    def is_editable(self):
        current_task_id = self.task_id

        # check if task id exists
        exists = db.session.query(db.exists().where(Task.task_id == current_task_id)).scalar()

        task_progress = Assignment.query.filter_by(assignment_id=current_task_id, progress=0.0).all()

        if exists is False:
            return False, helper.get_command_help("no_task_id")

            # check if task is done
        elif exists is True and len(task_progress) == 0:
            return False, helper.get_command_help("cannot_edit_completed_task")

        # if task is not done
        elif exists is True and task_progress[0].progress == 0.0:
            return True, None

    def edit_task(self, desc, points, deadline, t_id):
        """
        Edits a task in database and returns payload with success message

        :param desc: Description of task
        :type desc: str
        :param points: Points of task
        :type points: int
        :param deadline: Deadline of task
        :type deadline: Date
        :param deadline: ID of task
        :type deadline: int
        :raise:
        :return: Blocks list of response payload
        :rtype: list

        """
        helper = ErrorHelper()
        db.session.query(Task).filter_by(assignment_id=t_id).update(
            dict(description=desc, points=points, deadline=deadline)
        )
        db.session.commit()
        return helper.get_command_help("task_edited")

