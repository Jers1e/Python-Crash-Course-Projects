import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_score_single_response(language_survey):
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)


def test_score_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert 'English' in language_survey.responses
