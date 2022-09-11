import vampytest

from ..available_tags import parse_available_tags
from ...forum_tag import ForumTag


def test__parse_available_tags():
    """
    Tests whether ``parse_available_tags`` works as intended.
    """
    forum_tag = ForumTag.precreate(202209110002, name = 'ExistRuth')
    
    for input_data, expected_output in (
        ({}, None),
        ({'available_tags': None}, None),
        ({'available_tags': []}, None),
        ({'available_tags': [forum_tag.to_data(include_identifiers = True)]}, (forum_tag, ))
    ):
        output = parse_available_tags(input_data)
        
        vampytest.assert_eq(output, expected_output)
