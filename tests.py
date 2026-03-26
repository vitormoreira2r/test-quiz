import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


def test_crete_choice_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice(12, True)

def test_remove_choice_that_not_exist():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.remove_choice_by_id(2)

def test_find_choice_in_question_without_choices():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.set_correct_choices([1,2])

def test_find_choices_in_question():
    question = Question(title='q1')

    question.add_choice('a', False)

    question.add_choice('b', False)

    question.set_correct_choices([1,2])

def test_return_none_correct_choice():
    question = Question(title='q1', points=2, max_selections=2)

    question.add_choice('a', False)

    question.add_choice('b', False)

    question.set_correct_choices([1,2])

    choices = question.correct_selected_choices([3, 4])

    assert len(choices) == 0

def test_return_correct_choices():
    question = Question(title='q1', points=2, max_selections=2)

    question.add_choice('a', False)

    question.add_choice('b', False)

    question.set_correct_choices([1,2])

    choices = question.correct_selected_choices([1, 2])

    assert len(choices) == 2

def test_pass_max_selections():
    question = Question(title='q1', points=2, max_selections=1)

    question.add_choice('a', False)

    question.add_choice('b', False)

    question.set_correct_choices([1,2])

    with pytest.raises(Exception):
        choices = question.correct_selected_choices([1, 2])

def test_find_choice_after_remove_all_choices():
    question = Question(title='q1', points=2, max_selections=1)

    question.add_choice('a', False)

    question.remove_all_choices()

    with pytest.raises(Exception):
        choices = question._find_choice_by_id(1)

def test_remove_choice_y_id():
    question = Question(title='q1', points=2, max_selections=1)

    question.add_choice('a', False)

    question.add_choice('b', False)

    question.remove_choice_by_id(1)

    len(question.choices) == 1

def test_remove_choice_using_invalid_id():
    question = Question(title='q1', points=2, max_selections=1)

    question.add_choice('a', False)

    question.add_choice('b', False)
    with pytest.raises(Exception):
        question.remove_choice_by_id('adawdawdaw')

@pytest.fixture
def wrong_id():
    return 'r'

@pytest.fixture
def correct_id():
    return 1

@pytest.fixture
def max_points():
    return 100

def test_mixed_valid_and_invalid_ids_to_remove_choice(wrong_id, correct_id):
    question = Question(title='q1', points=2, max_selections=2)

    question.add_choice('a', True)
    question.add_choice('b', False)

    question.remove_choice_by_id(correct_id)

    with pytest.raises(Exception):
        question.remove_choice_by_id(wrong_id)

def test_create_question_with_invalid_points(max_points):
    with pytest.raises(Exception):
        question = Question(title='q1', points=max_points + 1, max_selections=1)

