from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


def test_days_left_counts_days_until_due():
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)

    result = days_left(due, today)

    assert result == 4


# TODO 1
def test_days_left_is_negative_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)

    result = days_left(due, today)

    assert result == -2


# TODO 2
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)

    result = is_urgent(due, today)

    assert result is True


# TODO 3
def test_is_urgent_when_due_in_exactly_two_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)

    result = is_urgent(due, today)

    assert result is True


# TODO 4
def test_is_not_urgent_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)

    result = is_urgent(due, today)

    assert result is False


# TODO 5
def test_sort_by_due_puts_soonest_task_first():
    tasks = [
        {"title": "Assignment", "due": date(2026, 10, 25)},
        {"title": "Quiz", "due": date(2026, 10, 20)},
        {"title": "Project", "due": date(2026, 10, 22)},
    ]

    result = sort_by_due(tasks)

    assert result[0]["title"] == "Quiz"
    assert result[1]["title"] == "Project"
    assert result[2]["title"] == "Assignment"


# TODO 6
def test_completion_rate_when_there_are_no_tasks():
    result = completion_rate(0, 0)

    assert result == 0.0


# TODO 7
def test_completion_rate_one_out_of_three():
    result = completion_rate(1, 3)

    assert result == 33.3