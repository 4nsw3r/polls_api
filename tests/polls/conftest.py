import pytest
from model_bakery import baker


@pytest.fixture()
def polls_factory():
    def factory(**kwargs):
        poll = baker.make("polls.Poll", **kwargs)
        return poll

    return factory


@pytest.fixture()
def questions_factory():
    def factory(**kwargs):
        question = baker.make("polls.Questions", **kwargs)
        return question

    return factory


@pytest.fixture()
def answer_factory():
    def factory(**kwargs):
        answer = baker.make("polls.Answer", **kwargs)
        return answer

    return factory