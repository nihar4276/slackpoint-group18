from commands.reminders import Reminders
from helpers import helper


def test_createReminder(mock_get_sqlalchemy,):

    """
    Test the view createReminder function

    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.add_columns.return_value.filter.return_value.all.return_value = (
        []
    )
    rem = Reminders()
    msg = rem.createReminder()
    if len(msg) > 0:
        return True 
 


def test_reminder_msg_block():
    """
    Test the test_reminder_msg function

    :param 
    :type 
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    rem = Reminders()
    #msg = rem.createReminder()
    msg = ["test_text"]
    out = rem.reminder_msg_block(msg)
    if out == {'blocks': [{'type': 'section','text': {'type': 'mrkdwn','text': '*Reminder : Urgent Tasks Due Completion :*'}},{'type': 'section', 'text': {'type': 'mrkdwn', 'text': 'test_text'}}]} :
        return True